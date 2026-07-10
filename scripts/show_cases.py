#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "case_database.csv"

DISPLAY_FIELDS = [
    "case_id",
    "date",
    "symbol",
    "timeframe",
    "main_signal",
    "signal_chain",
    "result",
    "lifecycle_status",
    "next_expected_state",
    "case_file_path",
]


def read_rows():
    if not DB_PATH.exists():
        return []
    with DB_PATH.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def matches(row, args):
    filters = {
        "symbol": args.symbol,
        "timeframe": args.timeframe,
        "main_signal": args.main_signal,
        "pattern_type": args.pattern_type,
        "result": args.result,
        "lifecycle_status": args.lifecycle_status,
        "next_expected_state": args.next_expected_state,
    }
    for field, expected in filters.items():
        if expected and row.get(field) != expected:
            return False
    return True


def print_table(rows):
    if not rows:
        print("没有找到匹配案例。")
        return

    widths = {}
    for field in DISPLAY_FIELDS:
        widths[field] = max(len(field), *(len(row.get(field, "")) for row in rows))

    header = "  ".join(field.ljust(widths[field]) for field in DISPLAY_FIELDS)
    print(header)
    print("-" * len(header))
    for row in rows:
        print("  ".join(row.get(field, "").ljust(widths[field]) for field in DISPLAY_FIELDS))


def main():
    parser = argparse.ArgumentParser(description="查询 DVCA 案例数据库")
    parser.add_argument("--symbol")
    parser.add_argument("--timeframe")
    parser.add_argument("--main_signal")
    parser.add_argument("--pattern_type")
    parser.add_argument("--result")
    parser.add_argument("--lifecycle_status")
    parser.add_argument("--next_expected_state")
    args = parser.parse_args()

    rows = [row for row in read_rows() if matches(row, args)]
    print_table(rows)


if __name__ == "__main__":
    main()
