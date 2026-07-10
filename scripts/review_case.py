#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "case_database.csv"

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

UNKNOWN_VALUES = {"", "Unknown", "NA", None}
FINAL_RESULTS = {"Success", "Fail", "Early", "Late", "NoTrade"}


def default_for(field):
    if field == "state":
        return "SignalCaptured"
    if field == "next_expected_state":
        return "Outcome10"
    if field == "lifecycle_status":
        return "Open"
    return "Unknown"


def read_rows():
    if not DB_PATH.exists():
        return []
    with DB_PATH.open("r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        for field in FIELDS:
            row.setdefault(field, default_for(field))
    return rows


def write_rows(rows):
    with DB_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def is_unknown(value):
    return value in UNKNOWN_VALUES


def update_lifecycle(row, force_close=False):
    if force_close:
        row["state"] = "Closed"
        row["next_expected_state"] = "None"
        row["lifecycle_status"] = "Closed"
        return

    if row.get("state") == "Closed" and row.get("lifecycle_status") == "Closed":
        row["next_expected_state"] = "None"
        return

    if is_unknown(row.get("outcome_bars_10")):
        row["state"] = "SignalCaptured"
        row["next_expected_state"] = "Outcome10"
        row["lifecycle_status"] = "Open"
    elif is_unknown(row.get("outcome_bars_20")):
        row["state"] = "Outcome10Recorded"
        row["next_expected_state"] = "Outcome20"
        row["lifecycle_status"] = "Review10"
    elif is_unknown(row.get("outcome_bars_50")):
        row["state"] = "Outcome20Recorded"
        row["next_expected_state"] = "Outcome50"
        row["lifecycle_status"] = "Review20"
    else:
        row["state"] = "Outcome50Recorded"
        row["next_expected_state"] = "None"
        row["lifecycle_status"] = "Closed"


def infer_result(row):
    outcomes = [
        row.get("outcome_bars_10", ""),
        row.get("outcome_bars_20", ""),
        row.get("outcome_bars_50", ""),
    ]
    if all(is_unknown(value) for value in outcomes):
        return "Unknown"

    text = " ".join(value for value in outcomes if not is_unknown(value)).lower()

    if any(word in text for word in ["notrade", "no trade", "不交易", "只观察"]):
        return "NoTrade"
    if any(word in text for word in ["fail", "失败", "反向", "失效", "止损", "invalid"]):
        return "Fail"
    if any(word in text for word in ["early", "过早"]):
        return "Early"
    if any(word in text for word in ["late", "过晚"]):
        return "Late"
    if any(word in text for word in ["success", "成功", "有效", "顺向", "继续跌", "继续涨", "延续", "到达"]):
        return "Success"
    return "Unknown"


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

## Case Lifecycle
- 当前状态：{row.get('state', '')}
- 下一步预期：{row.get('next_expected_state', '')}
- 生命周期状态：{row.get('lifecycle_status', '')}

## 信号链
- 信号链：{row.get('signal_chain', '')}
- 线段类型：{row.get('pattern_type', '')}

## 大周期背景
- 行情背景：{row.get('market_context', '')}

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

## Outcome10 / Outcome20 / Outcome50
- Outcome10：{row.get('outcome_bars_10', '')}
- Outcome20：{row.get('outcome_bars_20', '')}
- Outcome50：{row.get('outcome_bars_50', '')}

## 空间与回撤
- 最大顺向空间：{row.get('max_favorable_move', '')}
- 最大反向回撤：{row.get('max_adverse_move', '')}

## 截图路径
- {row.get('screenshot_path', '')}

## 复盘结论
{row.get('notes', '')}
"""


def refresh_markdown(row):
    case_file_path = row.get("case_file_path")
    if not case_file_path or case_file_path == "Unknown":
        return None
    path = ROOT / case_file_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_report(row), encoding="utf-8")
    return path


def prompt_yes_no(question):
    answer = input(f"{question} [y/N]: ").strip().lower()
    return answer in {"y", "yes"}


def prompt_text(question, default="Unknown"):
    answer = input(f"{question}: ").strip()
    return answer if answer else default


def apply_outcome_args(row, args):
    changed = False
    outcome_map = [
        (10, "outcome_bars_10", args.outcome10),
        (20, "outcome_bars_20", args.outcome20),
        (50, "outcome_bars_50", args.outcome50),
    ]
    for bars, field, value in outcome_map:
        if args.bars is not None and args.bars >= bars and is_unknown(row.get(field)) and value is None:
            row[field] = f"已达到 {bars} 根K；结果待补充"
            changed = True
        if value is not None:
            row[field] = value
            changed = True

    if args.max_favorable_move is not None:
        row["max_favorable_move"] = args.max_favorable_move
        changed = True
    if args.max_adverse_move is not None:
        row["max_adverse_move"] = args.max_adverse_move
        changed = True
    if args.notes:
        existing = row.get("notes", "")
        row["notes"] = f"{existing}\n\nReview note: {args.notes}".strip()
        changed = True
    return changed


def interactive_review(row):
    changed = False
    for bars, field in [
        (10, "outcome_bars_10"),
        (20, "outcome_bars_20"),
        (50, "outcome_bars_50"),
    ]:
        current = row.get(field, "Unknown")
        if not is_unknown(current):
            print(f"Outcome{bars} 已记录：{current}")
            continue
        if prompt_yes_no(f"是否已经达到 {bars} 根K？"):
            row[field] = prompt_text(f"请输入 Outcome{bars}")
            changed = True
        else:
            print(f"Outcome{bars} 暂未达到，保持 Unknown。")
            break

    if prompt_yes_no("是否更新最大顺向空间？"):
        row["max_favorable_move"] = prompt_text("最大顺向空间")
        changed = True
    if prompt_yes_no("是否更新最大反向回撤？"):
        row["max_adverse_move"] = prompt_text("最大反向回撤")
        changed = True
    if prompt_yes_no("是否追加复盘备注？"):
        note = prompt_text("复盘备注", "")
        if note:
            existing = row.get("notes", "")
            row["notes"] = f"{existing}\n\nReview note: {note}".strip()
            changed = True
    return changed


def print_reminder(row):
    print(f"案例：{row.get('case_id')}")
    print(f"信号：{row.get('main_signal')} | 链条：{row.get('signal_chain')}")
    print(f"当前生命周期：{row.get('lifecycle_status', 'Open')}")
    print(f"当前状态：{row.get('state', 'SignalCaptured')}")
    print(f"下一步预期：{row.get('next_expected_state', 'Outcome10')}")
    print("")
    for bars, field in [
        (10, "outcome_bars_10"),
        (20, "outcome_bars_20"),
        (50, "outcome_bars_50"),
    ]:
        value = row.get(field, "Unknown")
        status = "未记录" if is_unknown(value) else f"已记录：{value}"
        print(f"- {bars}根K：{status}")


def main():
    parser = argparse.ArgumentParser(description="复盘并更新 DVCA case lifecycle")
    parser.add_argument("case_id")
    parser.add_argument("--bars", type=int, choices=[10, 20, 50], help="当前已达到的K线数量")
    parser.add_argument("--outcome10")
    parser.add_argument("--outcome20")
    parser.add_argument("--outcome50")
    parser.add_argument("--max_favorable_move")
    parser.add_argument("--max_adverse_move")
    parser.add_argument("--result", choices=["Success", "Fail", "Early", "Late", "NoTrade", "Unknown"])
    parser.add_argument("--notes")
    parser.add_argument("--close", action="store_true")
    parser.add_argument("--no-interactive", action="store_true")
    args = parser.parse_args()

    rows = read_rows()
    found = None
    for row in rows:
        if row.get("case_id") == args.case_id:
            found = row
            break

    if found is None:
        print(f"未找到案例：{args.case_id}")
        return

    for row in rows:
        update_lifecycle(row)

    print_reminder(found)
    changed = apply_outcome_args(found, args)

    if not args.no_interactive:
        changed = interactive_review(found) or changed

    if args.result:
        found["result"] = args.result
        changed = True
    else:
        inferred = infer_result(found)
        if inferred != "Unknown" or found.get("result") in UNKNOWN_VALUES:
            found["result"] = inferred
            changed = True

    update_lifecycle(found, force_close=args.close)
    write_rows(rows)
    path = refresh_markdown(found)

    print("")
    print(f"更新完成：{found.get('case_id')}")
    print(f"Result：{found.get('result')}")
    print(f"Lifecycle：{found.get('lifecycle_status')} -> {found.get('next_expected_state')}")
    if path:
        print(f"Markdown：{path.relative_to(ROOT)}")
    if not changed:
        print("提示：本次没有新增 outcome 内容，只刷新了 lifecycle 字段。")


if __name__ == "__main__":
    main()
