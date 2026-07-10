# DVCA 标签系统

本文件说明 Phase 2 案例数据库中的标签如何使用。所有标签应优先参考 `data/tag_dictionary.csv`。

## 标签用途

- `Symbol`：用于区分 BTCUSDT、ETHUSDT、SOLUSDT 等交易品种。
- `Timeframe`：用于区分 1H、30m、15m、5m 等周期。
- `Direction`：用于记录案例方向，只填 `LONG`、`SHORT` 或 `Unknown`。
- `Signal`：用于记录主信号和信号链。
- `Pattern`：用于归类线段类型。
- `MarketContext`：用于记录行情背景。
- `EMAContext`：用于记录 EMA20 / EMA50 背景。
- `Result`：用于统计信号结果。
- `LifecycleStatus`：用于记录案例复盘进度。
- `CaseState`：用于记录案例内部状态。
- `NextExpectedState`：用于记录下一次应该复盘的节点。

## 如何判断 pattern_type

- `Reversal`：从 L-ZONE / S-ZONE 发展到 LONG / SHORT 的反转链条，例如 `L-ZONE→LONG`。
- `Pullback`：LONG / SHORT 后继续出现 PB-L / PB-S，例如 `LONG→PB-L` 或 `SHORT→PB-S`。
- `TrendContinuation`：主信号是 TC-L 或 TC-S，不依赖背离 Zone。
- `Exhaustion`：主信号是 EXH-L 或 EXH-S，只作为衰竭提醒。
- `FailedBreakout`：突破或跌破触发线后失败，或者只出现 E-L / E-S 后快速反向。
- `TransitionToTrendDown`：高周期或执行周期从震荡、转弱状态过渡为空头趋势背景，常见表现是 `Context Shift→TC-S`。
- `TransitionToTrendUp`：高周期或执行周期从震荡、转强状态过渡为多头趋势背景，常见表现是 `Context Shift→TC-L`。

## 如何判断 market_context

- `TrendUp`：EMA20 在 EMA50 上方，价格大多在 EMA50 上方，EMA50 有上行倾向。
- `TrendDown`：EMA20 在 EMA50 下方，价格大多在 EMA50 下方，EMA50 有下行倾向。
- `Range`：价格围绕 EMA20 / EMA50 来回穿越，结构没有清晰方向。
- `Expansion`：价格出现明显放量突破、跌破或大实体扩张。
- `Climax`：价格急涨或急跌后出现 EXH、背离、长影线或明显衰竭。
- `Unknown`：截图信息不足，暂时无法判断。

## 如何判断 ema_context

- `AboveEMA50`：信号出现时价格主要位于 EMA50 上方。
- `BelowEMA50`：信号出现时价格主要位于 EMA50 下方。
- `EMAFlat`：EMA20 / EMA50 走平、纠缠或方向不清。
- `EMACross`：EMA20 与 EMA50 发生交叉，或接近交叉。
- `Unknown`：截图中没有显示 EMA，或无法判断。

## 如何记录 signal_chain

`signal_chain` 用箭头连接同一案例中的信号过程。常见写法：

- `L-ZONE→LONG`
- `L-ZONE→LONG→PB-L`
- `S-ZONE→SHORT`
- `S-ZONE→SHORT→PB-S`
- `TC-L`
- `TC-S`
- `EXH-L→L-ZONE→LONG`
- `EXH-S→S-ZONE→SHORT`
- `E-L→Fail`
- `E-S→Fail`
- `LATE-L→LONG`
- `LATE-S→SHORT`

如果只观察不交易，可以写：

- `L-ZONE`
- `S-ZONE`
- `EXH-L`
- `EXH-S`

## BTC 常见 TC 多、LONG 少时如何标记

当前 Pine 代码没有 BTC 专属逻辑。BTC 出现 TC 多、LONG 少时，应按实际信号标记，而不是假设 BTC 有特殊规则。

建议填写：

- `symbol`：`BTCUSDT`
- `main_signal`：`TC-L` 或 `TC-S`
- `signal_chain`：`TC-L` 或 `TC-S`
- `pattern_type`：`TrendContinuation`
- `market_context`：根据图形填写 `TrendUp`、`TrendDown` 或 `Range`
- `ema_context`：根据 EMA50 位置填写
- `tc_present`：`Yes`
- `trigger_break`：如果不是 Zone 后突破，填 `NA`
- `pb_confirmed`：没有 PB 时填 `NA` 或 `No`

如果 BTC 出现 L-ZONE / S-ZONE 但没有 LONG / SHORT，应把 `result` 视情况填为 `NoTrade`、`Fail`、`Early` 或 `Unknown`，不要把 Zone 当作正式进场。

## SOL 常见 Zone→SHORT/LONG→PB 时如何标记

当前 Pine 代码没有 SOL 专属逻辑。SOL 出现完整 Zone 到 Entry 再到 PB 的案例时，应按通用代码链条记录。

多头案例建议填写：

- `symbol`：`SOLUSDT`
- `direction`：`LONG`
- `main_signal`：如果复盘重点是进场，填 `LONG`；如果重点是回踩确认，填 `PB-L`
- `signal_chain`：`L-ZONE→LONG→PB-L`
- `pattern_type`：`Pullback`
- `trigger_break`：`Yes`
- `pb_confirmed`：`Yes`
- `tc_present`：按图上是否出现 TC 填 `Yes` 或 `No`
- `exh_present`：按图上是否出现 EXH 填 `Yes` 或 `No`

空头案例建议填写：

- `symbol`：`SOLUSDT`
- `direction`：`SHORT`
- `main_signal`：如果复盘重点是进场，填 `SHORT`；如果重点是回踩确认，填 `PB-S`
- `signal_chain`：`S-ZONE→SHORT→PB-S`
- `pattern_type`：`Pullback`
- `trigger_break`：`Yes`
- `pb_confirmed`：`Yes`
- `tc_present`：按图上是否出现 TC 填 `Yes` 或 `No`
- `exh_present`：按图上是否出现 EXH 填 `Yes` 或 `No`

## 不确定时的处理

- 不确定行情背景：填 `Unknown`。
- 没有 Zone 分数：填 `NA`。
- 没有背离：填 `None`。
- 没有 VPA 类型：填 `None`。
- 截图缺少后续 K 线：结果填 `Unknown`，并在 `notes` 说明。
- 还没到 10 根 K：`lifecycle_status` 保持 `Open`。
- 已记录 10 根 K、还没到 20 根 K：`lifecycle_status` 填 `Review10`。
- 已记录 20 根 K、还没到 50 根 K：`lifecycle_status` 填 `Review20`。
- 已记录 50 根 K 或手动结束复盘：`lifecycle_status` 填 `Closed`。
