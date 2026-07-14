#!/usr/bin/env python3
"""DVCA 高周期验证案例的静态一致性检查。

本脚本不读取图像内容，不执行 OCR，不推断价格或交易信号。
"""

import argparse
import csv
import hashlib
import re
import sys
from collections import defaultdict
from pathlib import Path


DB_RELATIVE = Path("data/high_timeframe_validation/htf_case_database.csv")
CASE_ROOT_RELATIVE = Path("cases/high_timeframe_validation")
ALLOWED_MAIN_CODE = "indicator/current/dvca_v1_5_4.pine"

EXPECTED_FIELDS = [
    "htf_case_id", "case_file_path", "indicator_version", "indicator_code_path",
    "symbol", "market_type", "sample_start_time", "sample_end_time",
    "screenshot_files", "screenshot_1h_path", "screenshot_30m_path",
    "screenshot_15m_path", "market_state_1h", "market_state_30m",
    "market_state_15m", "objective_trend_start", "first_structure_change",
    "first_confirmed_structure_point", "structure_confirmation_time", "zone_type",
    "zone_first_seen_time", "zone_pivot_display_position", "zone_effective_time",
    "execution_signal_type", "execution_signal_first_seen_time",
    "pullback_signal_type", "pullback_signal_first_seen_time", "exh_signal_time",
    "signal_invalidation_time", "signal_expiration_time", "bars_trend_start_to_zone",
    "bars_zone_to_structure_confirmation", "bars_structure_confirmation_to_execution",
    "bars_trend_start_to_execution_total", "trend_completion_ratio_at_execution",
    "missed_main_move", "risk_reward_still_reasonable", "htf_ltf_conflict",
    "suppressed_by_range", "range_suppression_correct", "suppressed_by_transition",
    "transition_suppression_correct", "zone_without_timely_execution",
    "pivot_visual_delay", "reasonable_sparsity", "mechanical_lag", "outcome10",
    "outcome20", "outcome50", "final_classification", "v1_5_5_implication",
    "manual_review_notes", "case_status", "review_status", "screenshot_complete",
    "outcome10_complete", "outcome20_complete", "outcome50_complete",
    "evidence_quality", "suspected_issue", "requires_code_change", "reviewer_notes",
]

CLASSIFICATIONS = {
    "PENDING", "A_REASONABLE_SPARSE", "B_ACCEPTABLE_DELAY",
    "C_MECHANICAL_LAG", "D_OVER_FILTERING", "E_RANGE_PROTECTION_EFFECTIVE",
}
CASE_STATUSES = {"Draft", "Active", "Completed", "Rejected"}
REVIEW_STATUSES = {"Unreviewed", "InReview", "Reviewed"}
EVIDENCE_QUALITIES = {"Pending", "Low", "Medium", "High"}
YES_NO = {"Yes", "No"}
TRI_STATE = {"Yes", "No", "Unknown"}
SUSPECTED_ISSUES = {
    "UNDETERMINED", "NONE", "NORMAL_HTF_DELAY", "PIVOT_VISUAL_DELAY",
    "OVER_FILTERING", "SIGNAL_CHAIN_LAG", "HTF_LTF_MISMATCH",
    "RANGE_SUPPRESSION", "TRANSITION_SUPPRESSION", "ZONE_WITHOUT_EXECUTION",
    "OTHER",
}
INCOMPLETE_OUTCOMES = {"", "Pending", "Unknown", "NA"}
CASE_ID_RE = re.compile(r"^HTF-CASE-\d{4,}$")
PINE_REF_RE = re.compile(r"(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+\.pine")


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, message):
        self.errors.append(message)

    def warn(self, message):
        self.warnings.append(message)


def normalized(value):
    return (value or "").strip()


def resolve_project_path(root, value):
    raw = normalized(value)
    if not raw:
        return None
    candidate = Path(raw)
    return candidate if candidate.is_absolute() else root / candidate


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_enum(report, case_id, row, field, allowed):
    value = normalized(row.get(field))
    if value not in allowed:
        report.error(
            "{}: {}={} 非法；允许值：{}".format(
                case_id, field, value or "<empty>", ", ".join(sorted(allowed))
            )
        )


def validate_outcomes(report, case_id, row):
    stages = []
    for number in (10, 20, 50):
        outcome = normalized(row.get("outcome{}".format(number)))
        complete = normalized(row.get("outcome{}_complete".format(number)))
        is_complete = complete == "Yes"
        stages.append(is_complete)
        if is_complete and outcome in INCOMPLETE_OUTCOMES:
            report.error(
                "{}: Outcome{} 标记完成，但内容仍为 {}".format(
                    case_id, number, outcome or "<empty>"
                )
            )
        if complete == "No" and outcome not in INCOMPLETE_OUTCOMES:
            report.error(
                "{}: Outcome{} 标记未完成，但已填写完成型内容".format(case_id, number)
            )
    if stages[1] and not stages[0]:
        report.error("{}: Outcome20 完成但 Outcome10 未完成".format(case_id))
    if stages[2] and not stages[1]:
        report.error("{}: Outcome50 完成但 Outcome20 未完成".format(case_id))


def validate_markdown_code_refs(root, report):
    case_root = root / CASE_ROOT_RELATIVE
    for section in ("active", "completed"):
        directory = case_root / section
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            for ref in PINE_REF_RE.findall(text):
                if ref != ALLOWED_MAIN_CODE:
                    report.error(
                        "{}: 引用了 current 之外的主代码 {}".format(
                            path.relative_to(root), ref
                        )
                    )


def validate(root):
    report = Report()
    db_path = root / DB_RELATIVE
    screenshot_hash_cases = defaultdict(set)
    required_directories = [
        CASE_ROOT_RELATIVE / "templates", CASE_ROOT_RELATIVE / "active",
        CASE_ROOT_RELATIVE / "completed", Path("assets/screenshots/high_timeframe_validation"),
        Path("data/high_timeframe_validation"),
        Path("docs/research/high_timeframe_validation"),
    ]
    for relative in required_directories:
        if not (root / relative).is_dir():
            report.error("缺少目录：{}".format(relative))

    if not (root / ALLOWED_MAIN_CODE).is_file():
        report.error("正式主代码不存在：{}".format(ALLOWED_MAIN_CODE))
    if not db_path.is_file():
        report.error("专项数据库不存在：{}".format(DB_RELATIVE))
        return report, 0

    with db_path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        actual_fields = reader.fieldnames or []
        if actual_fields != EXPECTED_FIELDS:
            missing = [field for field in EXPECTED_FIELDS if field not in actual_fields]
            extra = [field for field in actual_fields if field not in EXPECTED_FIELDS]
            if missing:
                report.error("数据库缺少字段：{}".format(", ".join(missing)))
            if extra:
                report.error("数据库含未知字段：{}".format(", ".join(extra)))
            if not missing and not extra:
                report.error("数据库字段顺序与定义不一致")
        rows = list(reader)

    seen_ids = {}
    for row_number, row in enumerate(rows, start=2):
        case_id = normalized(row.get("htf_case_id")) or "row-{}".format(row_number)
        for field in EXPECTED_FIELDS:
            if not normalized(row.get(field)):
                report.error("{}: 必填字段 {} 为空".format(case_id, field))

        if not CASE_ID_RE.fullmatch(case_id):
            report.error("{}: Case ID 格式应为 HTF-CASE-XXXX".format(case_id))
        if case_id in seen_ids:
            report.error(
                "{}: Case ID 重复（数据库第 {}、{} 行）".format(
                    case_id, seen_ids[case_id], row_number
                )
            )
        else:
            seen_ids[case_id] = row_number

        if normalized(row.get("indicator_version")) != "DVCA v1.5.4":
            report.error("{}: indicator_version 必须为 DVCA v1.5.4".format(case_id))
        if normalized(row.get("indicator_code_path")) != ALLOWED_MAIN_CODE:
            report.error("{}: 主代码必须引用 {}".format(case_id, ALLOWED_MAIN_CODE))

        validate_enum(report, case_id, row, "final_classification", CLASSIFICATIONS)
        validate_enum(report, case_id, row, "case_status", CASE_STATUSES)
        validate_enum(report, case_id, row, "review_status", REVIEW_STATUSES)
        validate_enum(report, case_id, row, "evidence_quality", EVIDENCE_QUALITIES)
        validate_enum(report, case_id, row, "suspected_issue", SUSPECTED_ISSUES)
        for field in ("screenshot_complete", "outcome10_complete", "outcome20_complete", "outcome50_complete"):
            validate_enum(report, case_id, row, field, YES_NO)
        for field in (
            "missed_main_move", "risk_reward_still_reasonable", "htf_ltf_conflict",
            "suppressed_by_range", "range_suppression_correct", "suppressed_by_transition",
            "transition_suppression_correct", "zone_without_timely_execution",
            "pivot_visual_delay", "reasonable_sparsity", "mechanical_lag",
            "requires_code_change",
        ):
            validate_enum(report, case_id, row, field, TRI_STATE)

        case_path = resolve_project_path(root, row.get("case_file_path"))
        if case_path is not None and not case_path.is_file():
            report.error("{}: 案例文件不存在：{}".format(case_id, row["case_file_path"]))

        screenshot_paths = []
        for field in ("screenshot_1h_path", "screenshot_30m_path", "screenshot_15m_path"):
            path = resolve_project_path(root, row.get(field))
            if path is None or not path.is_file():
                report.error("{}: {} 截图不存在：{}".format(case_id, field, row.get(field, "")))
            else:
                screenshot_paths.append(path)
                screenshot_hash_cases[sha256(path)].add(case_id)

        all_screenshots_exist = len(screenshot_paths) == 3
        screenshot_complete = normalized(row.get("screenshot_complete"))
        if screenshot_complete == "Yes" and not all_screenshots_exist:
            report.error("{}: screenshot_complete=Yes，但 1H/30m/15m 截图不齐全".format(case_id))
        if screenshot_complete == "No" and all_screenshots_exist:
            report.warn("{}: 三周期截图均存在，但 screenshot_complete=No".format(case_id))

        validate_outcomes(report, case_id, row)
        if normalized(row.get("case_status")) == "Completed":
            if normalized(row.get("review_status")) != "Reviewed":
                report.error("{}: Completed 案例必须为 Reviewed".format(case_id))
            if normalized(row.get("outcome50_complete")) != "Yes":
                report.error("{}: Completed 案例必须完成 Outcome50".format(case_id))
            if normalized(row.get("final_classification")) == "PENDING":
                report.error("{}: Completed 案例不能保持 PENDING 分类".format(case_id))

    for digest, case_ids in sorted(screenshot_hash_cases.items()):
        if len(case_ids) > 1:
            report.error(
                "同一截图哈希被多个案例使用：{} -> {}".format(
                    digest, ", ".join(sorted(case_ids))
                )
            )

    validate_markdown_code_refs(root, report)
    if not rows:
        report.warn("专项数据库目前只有表头，尚无案例样本")
    return report, len(rows)


def main():
    parser = argparse.ArgumentParser(description="静态检查 DVCA 高周期验证案例")
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1],
        help="DVCA 项目根目录（默认根据脚本位置推断）",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    report, row_count = validate(root)
    print("DVCA HTF 静态检查")
    print("项目：{}".format(root))
    print("案例：{}".format(row_count))
    print("错误：{}".format(len(report.errors)))
    print("警告：{}".format(len(report.warnings)))
    for message in report.errors:
        print("ERROR: {}".format(message))
    for message in report.warnings:
        print("WARN: {}".format(message))
    if report.errors:
        print("结果：失败")
        return 1
    print("结果：通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
