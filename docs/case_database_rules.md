# DVCA 案例数据库使用规则

本文件用于规定 `data/case_database.csv` 的填写方式。所有统计都必须基于这个 CSV，不允许为了让指标看起来更好而修改结果。

DVCA 项目采用 Raw / Candidate / Gold 三级案例体系。原始截图先放 `screenshots/`，不要求每张图都进入数据库。只有进入 Candidate 层的案例，才写入 `data/case_database.csv`。

## 基本规则

- Raw 原始截图不需要 `case_id`。
- 每个 Candidate 案例必须对应一个 `case_id`。
- 每个 Candidate 案例至少应该有一张截图路径。
- 每个案例必须记录 `symbol`、`timeframe`、`main_signal`、`signal_chain`、`result`。
- 每个案例都必须带有 Case Lifecycle 字段：`state`、`next_expected_state`、`lifecycle_status`。
- 不确定的字段填 `Unknown` 或 `NA`，不要乱填。
- 如果某个字段不适用于当前案例，例如没有 Zone 分数，可以填 `NA`。
- 如果某个字段暂时看不清，例如行情背景，可以填 `Unknown`。
- 所有统计必须基于 `data/case_database.csv`。
- 所有 Candidate 案例报告必须能追溯到截图路径和案例 Markdown 文件路径。
- 不完整、结果未知、只是发现问题的截图，先放 Raw 或 `research/questions/`，不要急着入库。

## 进入数据库的标准

只有满足下面任意一类，才进入 `case_database.csv`。

### 完整流程

例如：

- `L-ZONE→LONG→PB-L`
- `S-ZONE→SHORT→PB-S`
- `EXH-L→L-ZONE→LONG`

### 失败案例

例如：

- `LONG→Fail`
- `SHORT→Fail`
- `E-L→Fail`
- `TC-L→Fail`

### 特别漂亮

例如：

- BTC 连续多个 TC-L。
- SOL 标准 Zone 到 SHORT/LONG 再到 PB。

### 特别奇怪

例如：

- BTC 趋势很强但 LONG 很少。
- Zone 出现后长期没有正式突破。

这类情况也可以先进入 `research/questions/`，等结果明确后再入库。

## result 定义

- `Success`：信号后按预期方向走出有效空间。
- `Fail`：信号后快速反向或触发失效。
- `Early`：方向对但信号过早。
- `Late`：方向对但信号过晚。
- `NoTrade`：只观察不交易。
- `Unknown`：暂时无法判断。

## Case Lifecycle 定义

Case Lifecycle 用于管理案例从入库到完成复盘的过程。详细说明见 `docs/case_lifecycle.md`。

- `Open`：案例已入库，等待记录信号后 10 根 K 线表现。
- `Review10`：已记录 10 根 K 线表现，等待 20 根 K 线表现。
- `Review20`：已记录 20 根 K 线表现，等待 50 根 K 线表现。
- `Closed`：已记录 50 根 K 线表现，或已手动关闭。

对应的 `state`：

- `SignalCaptured`：信号已捕获，等待 Outcome10。
- `Outcome10Recorded`：已记录 Outcome10。
- `Outcome20Recorded`：已记录 Outcome20。
- `Outcome50Recorded`：已记录 Outcome50。
- `Closed`：案例已关闭。

对应的 `next_expected_state`：

- `Outcome10`
- `Outcome20`
- `Outcome50`
- `None`

## 必填字段

以下字段每个案例都应尽量填写：

- `case_id`
- `date`
- `symbol`
- `timeframe`
- `direction`
- `main_signal`
- `signal_chain`
- `pattern_type`
- `result`
- `state`
- `next_expected_state`
- `lifecycle_status`
- `screenshot_path`
- `case_file_path`

## 字段填写原则

- `case_id`：自动生成，例如 `CASE-0001`。
- `date`：信号出现日期，建议使用 `YYYY-MM-DD`。
- `symbol`：交易品种，例如 `BTCUSDT`、`ETHUSDT`、`SOLUSDT`。
- `timeframe`：截图周期，例如 `1H`、`30m`、`15m`、`5m`。
- `direction`：只填 `LONG` 或 `SHORT`，无法判断时填 `Unknown`。
- `main_signal`：主信号，例如 `LONG`、`SHORT`、`PB-L`、`TC-S`。
- `signal_chain`：信号链，例如 `L-ZONE→LONG→PB-L`。
- `pattern_type`：线段类型，例如 `Reversal`、`Pullback`、`TrendContinuation`、`Exhaustion`、`FailedBreakout`。
- `market_context`：行情背景，例如 `TrendUp`、`TrendDown`、`Range`、`Expansion`、`Climax`、`Unknown`。
- `ema_context`：EMA 背景，例如 `AboveEMA50`、`BelowEMA50`、`EMAFlat`、`EMACross`、`Unknown`。
- `divergence_code`：背离代码，例如 `H`、`M`、`R`、`HM`、`HR`、`MR`、`HMR`、`None`。
- `vpa_type`：量价类型，例如 `VA`、`VS`、`VR`、`VF`、`VE`、`None`、`Unknown`。
- `zone_score`：Zone 分数；没有 Zone 时填 `NA`。
- `trigger_break`：是否突破或跌破触发线，填 `Yes`、`No` 或 `NA`。
- `pb_confirmed`：是否出现 PB 确认，填 `Yes`、`No` 或 `NA`。
- `tc_present`：是否出现 TC，填 `Yes` 或 `No`。
- `exh_present`：是否出现 EXH，填 `Yes` 或 `No`。
- `state`：案例状态，例如 `SignalCaptured`、`Outcome10Recorded`、`Outcome20Recorded`、`Outcome50Recorded`、`Closed`。
- `next_expected_state`：下一步要观察的复盘节点，例如 `Outcome10`、`Outcome20`、`Outcome50`、`None`。
- `lifecycle_status`：生命周期状态，例如 `Open`、`Review10`、`Review20`、`Closed`。
- `outcome_bars_10`、`outcome_bars_20`、`outcome_bars_50`：记录信号后 10 / 20 / 50 根 K 线表现。
- `max_favorable_move`：最大顺向空间。
- `max_adverse_move`：最大反向回撤。
- `notes`：补充说明，不确定的判断也写在这里。

## 禁止事项

- 不允许为了提高成功率而删除失败案例。
- 不允许为了让指标看起来更好而修改 `result`。
- 不允许用主观感觉覆盖截图事实。
- 不允许把 L-ZONE / S-ZONE 当作正式进场结果统计。
- 不允许把 EXH-L / EXH-S 当作正式反向进场结果统计。
- 不允许跳过 Outcome10 / Outcome20 / Outcome50 就凭感觉关闭案例。
