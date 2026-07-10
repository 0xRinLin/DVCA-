# DVCA Signal Atlas 复盘路径

本文件用于截图复盘时快速判断当前案例属于哪条路径。

## 第一步：先判断是否是独立 TC

检查图上是否出现 `TC-L` 或 `TC-S`：

- 如果是 TC-L / TC-S，优先归为 `TrendContinuation`。
- 检查 EMA20 / EMA50 是否符合 `ctxUp` 或 `ctxDown`。
- 检查 TC 前是否有回踩或反抽 EMA20。
- 检查是否突破短高或跌破短低。
- 不要把 TC 当作背离反转。

案例字段建议：

- `pattern_type=TrendContinuation`
- `tc_present=Yes`
- `signal_chain=TC-L` 或 `TC-S`

## 第二步：再判断是否是 Zone 到 Entry

如果图上出现 L-ZONE 或 S-ZONE：

1. 找到两个 Pivot 点和背离线。
2. 记录背离代码 H / M / R。
3. 找到结构触发线 `bullTrigger` 或 `bearTrigger`。
4. 检查后续是否出现 LONG 或 SHORT。

多头路径：

- `L-ZONE`
- `C-L`
- `bullTrigger`
- `LONG`
- `PB-L`

空头路径：

- `S-ZONE`
- `C-S`
- `bearTrigger`
- `SHORT`
- `PB-S`

案例字段建议：

- Zone 到 Entry：`pattern_type=Reversal`
- Entry 到 PB：`pattern_type=Pullback`
- 出现正式突破：`trigger_break=Yes`
- 出现 PB：`pb_confirmed=Yes`

## 第三步：判断是否只是观察信号

以下信号通常不单独作为正式交易执行：

- `L-ZONE`
- `S-ZONE`
- `C-L`
- `C-S`
- `EXH-L`
- `EXH-S`
- `LATE-L`
- `LATE-S`
- `E-L`
- `E-S`

记录方式：

- 单独 Zone：`result=NoTrade` 或 `Unknown`
- 单独 EXH：`pattern_type=Exhaustion`，`result=NoTrade` 或 `Unknown`
- E-L / E-S 后失败：`pattern_type=FailedBreakout`，`result=Fail`
- LATE-L / LATE-S：记录为补确认，不要当作追单信号。

## 第四步：判断失败类型

多头失败常见路径：

- L-ZONE 后跌破 `bullLow - 0.05 ATR`
- L-ZONE 后超过 `maxSetupBars` 仍未突破
- 突破 `bullTrigger` 但只出现 E-L，没有 LONG
- LONG 后 PB-L 等待失败

空头失败常见路径：

- S-ZONE 后突破 `bearHigh + 0.05 ATR`
- S-ZONE 后超过 `maxSetupBars` 仍未跌破
- 跌破 `bearTrigger` 但只出现 E-S，没有 SHORT
- SHORT 后 PB-S 等待失败

案例字段建议：

- `pattern_type=FailedBreakout`
- `result=Fail`
- `notes` 写明失败点。

## 第五步：补齐结果统计字段

每个案例完成复盘后，至少补齐：

- `outcome_bars_10`
- `outcome_bars_20`
- `outcome_bars_50`
- `max_favorable_move`
- `max_adverse_move`
- `result`

如果后续 K 线不足，先填 `Unknown`，不要凭感觉提前判断。

