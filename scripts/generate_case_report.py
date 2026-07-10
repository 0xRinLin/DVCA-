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


def read_rows():
    if not DB_PATH.exists():
        return []
    with DB_PATH.open("r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row.setdefault("state", "SignalCaptured")
        row.setdefault("next_expected_state", "Outcome10")
        row.setdefault("lifecycle_status", "Open")
    return rows


def write_rows(rows):
    with DB_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


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
    return CASES_DIR


def default_case_path(row):
    filename = "_".join(
        [
            row["case_id"],
            clean_filename_part(row.get("symbol")),
            clean_filename_part(row.get("timeframe")),
            clean_filename_part(row.get("main_signal")),
        ]
    ) + ".md"
    return select_case_dir(row) / filename


def render_report(row):
    return f"""# DVCA 案例复盘：{row.get('case_id', '')}

## 基本信息
- 案例编号：{row.get('case_id', '')}
- 日期：{row.get('date', '')}
- 交易品种：{row.get('symbol', '')}
- 周期：{row.get('timeframe', '')}
- 方向：{row.get('direction', '')}
- 主信号：{row.get('main_signal', '')}
- 结果：{row.get('result', '')}

## 信号链
- 信号链：{row.get('signal_chain', '')}
- 线段类型：{row.get('pattern_type', '')}

## Case Lifecycle
- 当前状态：{row.get('state', '')}
- 下一步预期：{row.get('next_expected_state', '')}
- 生命周期状态：{row.get('lifecycle_status', '')}

## 大周期背景
- 行情背景：{row.get('market_context', '')}
- 说明：当前数据库用 `market_context` 统一记录背景；如需拆分 1H / 30m / 15m / 5m，可在 notes 中补充。

## EMA背景
- EMA背景：{row.get('ema_context', '')}

## 背离与VPA
- 背离代码：{row.get('divergence_code', '')}
- VPA类型：{row.get('vpa_type', '')}
- Zone分数：{row.get('zone_score', '')}

## 触发与确认
- 是否突破/跌破触发线：{row.get('trigger_break', '')}
- 是否PB确认：{row.get('pb_confirmed', '')}
- 是否出现TC：{row.get('tc_present', '')}
- 是否出现EXH：{row.get('exh_present', '')}

## 10/20/50根K线表现
- 信号后10根K线：{row.get('outcome_bars_10', '')}
- 信号后20根K线：{row.get('outcome_bars_20', '')}
- 信号后50根K线：{row.get('outcome_bars_50', '')}

## 空间与回撤
- 最大顺向空间：{row.get('max_favorable_move', '')}
- 最大反向回撤：{row.get('max_adverse_move', '')}

## 截图路径
- {row.get('screenshot_path', '')}

## 复盘结论
{row.get('notes', '')}
"""


def main():
    parser = argparse.ArgumentParser(description="根据 case_id 生成或更新案例 Markdown 报告")
    parser.add_argument("--case_id", required=True)
    args = parser.parse_args()

    rows = read_rows()
    for row in rows:
        if row.get("case_id") == args.case_id:
            case_file_path = row.get("case_file_path") or "Unknown"
            if case_file_path == "Unknown":
                path = default_case_path(row)
                row["case_file_path"] = str(path.relative_to(ROOT))
                write_rows(rows)
            else:
                path = ROOT / case_file_path

            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render_report(row), encoding="utf-8")
            print(f"已生成/更新案例报告：{path.relative_to(ROOT)}")
            return

    print(f"未找到案例：{args.case_id}")


if __name__ == "__main__":
    main()
