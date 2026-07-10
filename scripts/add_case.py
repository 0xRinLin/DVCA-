#!/usr/bin/env python3
import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "case_database.csv"
CASES_DIR = ROOT / "cases"

FIELDS = [
    "case_id",
    "date",
    "symbol",
    "timeframe",
    "direction",
    "main_signal",
    "signal_chain",
    "pattern_type",
    "market_context",
    "ema_context",
    "divergence_code",
    "vpa_type",
    "zone_score",
    "trigger_break",
    "pb_confirmed",
    "tc_present",
    "exh_present",
    "result",
    "state",
    "next_expected_state",
    "lifecycle_status",
    "outcome_bars_10",
    "outcome_bars_20",
    "outcome_bars_50",
    "max_favorable_move",
    "max_adverse_move",
    "screenshot_path",
    "case_file_path",
    "notes",
]

DEFAULTS = {
    "date": "Unknown",
    "symbol": "Unknown",
    "timeframe": "Unknown",
    "direction": "Unknown",
    "main_signal": "Unknown",
    "signal_chain": "Unknown",
    "pattern_type": "Unknown",
    "market_context": "Unknown",
    "ema_context": "Unknown",
    "divergence_code": "None",
    "vpa_type": "Unknown",
    "zone_score": "NA",
    "trigger_break": "NA",
    "pb_confirmed": "NA",
    "tc_present": "No",
    "exh_present": "No",
    "result": "Unknown",
    "state": "SignalCaptured",
    "next_expected_state": "Outcome10",
    "lifecycle_status": "Open",
    "outcome_bars_10": "Unknown",
    "outcome_bars_20": "Unknown",
    "outcome_bars_50": "Unknown",
    "max_favorable_move": "NA",
    "max_adverse_move": "NA",
    "screenshot_path": "Unknown",
    "case_file_path": "Unknown",
    "notes": "",
}


def ensure_database():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not DB_PATH.exists():
        with DB_PATH.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
        return

    with DB_PATH.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        current_fields = reader.fieldnames or []

    if current_fields != FIELDS:
        for row in rows:
            for field in FIELDS:
                row.setdefault(field, DEFAULTS.get(field, "Unknown"))
        with DB_PATH.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)


def read_rows():
    ensure_database()
    with DB_PATH.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def next_case_id(rows):
    max_num = 0
    for row in rows:
        match = re.match(r"CASE-(\d+)$", row.get("case_id", ""))
        if match:
            max_num = max(max_num, int(match.group(1)))
    return f"CASE-{max_num + 1:04d}"


def clean_filename_part(value):
    value = value or "Unknown"
    value = value.replace("→", "-")
    value = re.sub(r"[^A-Za-z0-9_.-]+", "_", value)
    return value.strip("_") or "Unknown"


def select_case_dir(row):
    result = row.get("result", "")
    pattern = row.get("pattern_type", "")
    direction = row.get("direction", "")

    if result == "Fail" or pattern == "FailedBreakout":
        return CASES_DIR / "failed_signals"
    if pattern in {"TransitionToTrendDown", "TransitionToTrendUp"}:
        return CASES_DIR / "state_transition"
    if pattern == "TrendContinuation":
        return CASES_DIR / "trend_continuation"
    if pattern == "Exhaustion":
        return CASES_DIR / "exhaustion"
    if direction == "LONG" and pattern in {"Reversal", "Pullback", "TrendPullback"}:
        return CASES_DIR / "bullish"
    if direction == "SHORT" and pattern in {"Reversal", "Pullback", "TrendPullback"}:
        return CASES_DIR / "bearish"
    return CASES_DIR / "failed_signals" if result == "Fail" else CASES_DIR


def infer_related_flags(row):
    signal_text = f"{row.get('main_signal', '')} {row.get('signal_chain', '')}"
    if "TC-L" in signal_text or "TC-S" in signal_text:
        row["tc_present"] = "Yes"
    if "EXH-L" in signal_text or "EXH-S" in signal_text:
        row["exh_present"] = "Yes"
    if "PB-L" in signal_text or "PB-S" in signal_text:
        row["pb_confirmed"] = "Yes"


def render_case_markdown(row):
    return f"""# DVCA 案例复盘：{row['case_id']}

## 基本信息
- 案例编号：{row['case_id']}
- 日期：{row['date']}
- 交易品种：{row['symbol']}
- 周期：{row['timeframe']}
- 方向：{row['direction']}
- 主信号：{row['main_signal']}
- 结果：{row['result']}
- 截图路径：{row['screenshot_path']}

## 信号链
- 信号链：{row['signal_chain']}
- 线段类型：{row['pattern_type']}
- 行情背景：{row['market_context']}
- EMA背景：{row['ema_context']}

## Case Lifecycle
- 当前状态：{row['state']}
- 下一步预期：{row['next_expected_state']}
- 生命周期状态：{row['lifecycle_status']}

## 当前信号
- 背离代码：{row['divergence_code']}
- VPA类型：{row['vpa_type']}
- Zone分数：{row['zone_score']}
- 是否突破/跌破触发线：{row['trigger_break']}
- 是否PB确认：{row['pb_confirmed']}
- 是否出现TC：{row['tc_present']}
- 是否出现EXH：{row['exh_present']}

## 结果
- 信号后10根K线：{row['outcome_bars_10']}
- 信号后20根K线：{row['outcome_bars_20']}
- 信号后50根K线：{row['outcome_bars_50']}
- 最大顺向空间：{row['max_favorable_move']}
- 最大反向回撤：{row['max_adverse_move']}

## 总结
{row['notes']}
"""


def build_parser():
    parser = argparse.ArgumentParser(description="新增 DVCA 案例到 data/case_database.csv")
    for field in FIELDS:
        if field in {"case_id", "case_file_path"}:
            continue
        parser.add_argument(f"--{field}", default=None)
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    rows = read_rows()
    row = {field: DEFAULTS.get(field, "Unknown") for field in FIELDS}
    row["case_id"] = next_case_id(rows)

    for field in FIELDS:
        if field in {"case_id", "case_file_path"}:
            continue
        value = getattr(args, field, None)
        if value is not None:
            row[field] = value

    infer_related_flags(row)

    case_dir = select_case_dir(row)
    case_dir.mkdir(parents=True, exist_ok=True)
    filename = "_".join(
        [
            row["case_id"],
            clean_filename_part(row["symbol"]),
            clean_filename_part(row["timeframe"]),
            clean_filename_part(row["main_signal"]),
        ]
    ) + ".md"
    case_path = case_dir / filename
    row["case_file_path"] = str(case_path.relative_to(ROOT))

    with DB_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow(row)

    case_path.write_text(render_case_markdown(row), encoding="utf-8")

    print(f"新增案例编号：{row['case_id']}")
    print(f"案例文件路径：{row['case_file_path']}")


if __name__ == "__main__":
    main()
