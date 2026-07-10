#!/usr/bin/env python3
import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "case_database.csv"
SUMMARY_PATH = ROOT / "data" / "statistics_summary.md"


def read_rows():
    if not DB_PATH.exists():
        return []
    with DB_PATH.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def count_by(rows, field):
    return Counter(row.get(field, "Unknown") or "Unknown" for row in rows)


def success_rate(rows):
    total = len(rows)
    judged_rows = [
        row
        for row in rows
        if row.get("result") not in {"", "Unknown", "NoTrade"}
    ]
    judged = len(judged_rows)
    if total == 0:
        return "NA"
    if judged == 0:
        return f"NA (0 judged / {total} total)"
    success = sum(1 for row in judged_rows if row.get("result") == "Success")
    return f"{success}/{judged} ({success / judged:.1%}, {total} total)"


def group_rows(rows, *fields):
    groups = defaultdict(list)
    for row in rows:
        key = tuple(row.get(field, "Unknown") or "Unknown" for field in fields)
        groups[key].append(row)
    return groups


def format_counter(title, counter):
    lines = [f"## {title}", ""]
    if not counter:
        lines.append("- 暂无数据")
    else:
        for key, value in sorted(counter.items()):
            lines.append(f"- {key}: {value}")
    lines.append("")
    return lines


def format_success_table(title, groups):
    lines = [f"## {title}", ""]
    if not groups:
        lines.append("- 暂无数据")
    else:
        for key, items in sorted(groups.items()):
            label = " + ".join(key) if isinstance(key, tuple) else str(key)
            lines.append(f"- {label}: {success_rate(items)}")
    lines.append("")
    return lines


def build_report(rows):
    lines = ["# DVCA 案例统计摘要", ""]
    lines.append(f"- 总案例数量: {len(rows)}")
    lines.append("")

    lines.extend(format_counter("各 symbol 案例数量", count_by(rows, "symbol")))
    lines.extend(format_counter("各 timeframe 案例数量", count_by(rows, "timeframe")))
    lines.extend(format_counter("各 main_signal 案例数量", count_by(rows, "main_signal")))
    lines.extend(format_counter("各 lifecycle_status 案例数量", count_by(rows, "lifecycle_status")))
    lines.extend(format_counter("各 next_expected_state 案例数量", count_by(rows, "next_expected_state")))

    lines.extend(format_success_table("各 main_signal 成功率", group_rows(rows, "main_signal")))
    lines.extend(format_success_table("各 symbol + main_signal 成功率", group_rows(rows, "symbol", "main_signal")))
    lines.extend(format_success_table("各 pattern_type 成功率", group_rows(rows, "pattern_type")))
    lines.extend(format_success_table("PB确认案例与无PB案例对比", group_rows(rows, "pb_confirmed")))

    tc_rows = [row for row in rows if row.get("main_signal") in {"TC-L", "TC-S"}]
    lines.extend(format_success_table("TC-L / TC-S 成功率", group_rows(tc_rows, "main_signal")))

    exh_rows = [
        row
        for row in rows
        if row.get("main_signal") in {"EXH-L", "EXH-S"} or "EXH" in row.get("signal_chain", "")
    ]
    rough_conversion = [
        row
        for row in exh_rows
        if "LONG" in row.get("signal_chain", "") or "SHORT" in row.get("signal_chain", "")
    ]
    lines.append("## EXH 后转化为 LONG/SHORT 的案例数量")
    lines.append("")
    lines.append(f"- 当前可粗略识别案例数量: {len(rough_conversion)}")
    lines.append("- 说明: 当前字段没有单独的 `exh_conversion`，这里只通过 `signal_chain` 是否同时包含 EXH 与 LONG/SHORT 粗略统计。后续如需严格统计，可以新增独立字段。")
    lines.append("")

    return "\n".join(lines)


def main():
    rows = read_rows()
    report = build_report(rows)
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(report + "\n", encoding="utf-8")
    print(report)
    print(f"已写入：{SUMMARY_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
