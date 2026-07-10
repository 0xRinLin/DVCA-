# DVCA Trading Desk Report

本文件固定 DVCA 每日盘面复盘报告格式。它用于把截图分析、市场状态、信号链、交易计划、场景推演和案例入库判断统一到同一个框架中。

该报告只用于复盘与研究，不修改 DVCA Pine 指标，不替代 `docs/signal_manual.md` 和 `docs/line_patterns.md`。

## 报告目标

- 先判断 Market State，再判断是否有交易信号。
- 先看多周期一致性，再看 1m 或 5m 的入场细节。
- 明确区分 Momentum Recovery 与 Trend Reversal。
- 明确区分观察、等待、顺势执行、逆势风险。
- 判断截图是否值得进入 Case Database。
- 从案例中提炼 DVCA 2.0 的研究问题，而不是凭感觉改指标。

## 固定结构

每份 Trading Desk Report 应包含以下部分：

1. 标的、分析时间、周期组合。
2. Market State。
3. Signal Chain。
4. 多周期一致性。
5. Trading Plan。
6. Scenario。
7. Risk Assessment。
8. Execution。
9. Case Database 判断。
10. 对 DVCA 指标的研究反馈。

## 核心判断原则

- `1D / 1H / 30m` 用于判断大背景。
- `15m / 5m` 用于判断执行方向。
- `1m` 只用于观察短线动能，不单独定义反转。
- `Momentum Recovery` 不是 `Trend Reversal`。
- `L-ZONE / S-ZONE` 是观察区，不是进场。
- `LONG / SHORT` 是严格突破或跌破信号。
- `PB-L / PB-S` 是突破后的回踩或反抽确认。
- `TC-L / TC-S` 是趋势延续，不是背离反转。
- `EXH-L / EXH-S` 是衰竭提醒，不是正式反向进场。

## 入库判断

Trading Desk Report 中的截图不一定全部进入数据库。只有满足以下条件时才录入 Case Database：

- 可以研究完整流程，例如 `S-ZONE→C-S→TC-S`。
- 可以研究状态切换，例如 `Transition→Trend Down`。
- 可以研究失败案例，例如 `LONG→Fail`。
- 可以研究纪律案例，例如 `1m 动能修复但高周期仍为空头`。
- 可以作为 Gold Case 或 Good Case 被 Signal Atlas 引用。

## 与 Case Lifecycle 的关系

Trading Desk Report 只完成当下判断。进入数据库后的案例，仍必须通过 Case Lifecycle 继续记录：

- Outcome10
- Outcome20
- Outcome50
- Result

也就是说，报告结论不是最终结果。最终 `Success / Fail / Early / Late / NoTrade / Unknown` 必须由后续 K 线表现决定。
