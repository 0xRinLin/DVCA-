# Signal Atlas 与案例数据库映射

本文件说明如何把 Signal Atlas 中的状态路径填写到 `data/case_database.csv`。本文件不改变数据库结构，只说明已有字段的用法。

## 反转链条

### 多头反转

- `direction`：`LONG`
- `main_signal`：根据复盘重点填写 `L-ZONE`、`LONG` 或 `PB-L`
- `signal_chain`：`L-ZONE→LONG` 或 `L-ZONE→LONG→PB-L`
- `pattern_type`：`Reversal` 或 `Pullback`
- `trigger_break`：出现 LONG 时填 `Yes`
- `pb_confirmed`：出现 PB-L 时填 `Yes`，没有则填 `No` 或 `NA`
- `tc_present`：除非同图上出现 TC-L，否则填 `No`
- `exh_present`：若前面有 EXH-L，可填 `Yes`

### 空头反转

- `direction`：`SHORT`
- `main_signal`：根据复盘重点填写 `S-ZONE`、`SHORT` 或 `PB-S`
- `signal_chain`：`S-ZONE→SHORT` 或 `S-ZONE→SHORT→PB-S`
- `pattern_type`：`Reversal` 或 `Pullback`
- `trigger_break`：出现 SHORT 时填 `Yes`
- `pb_confirmed`：出现 PB-S 时填 `Yes`，没有则填 `No` 或 `NA`
- `tc_present`：除非同图上出现 TC-S，否则填 `No`
- `exh_present`：若前面有 EXH-S，可填 `Yes`

## 趋势延续链条

### TC-L

- `direction`：`LONG`
- `main_signal`：`TC-L`
- `signal_chain`：`TC-L`
- `pattern_type`：`TrendContinuation`
- `trigger_break`：`NA`
- `pb_confirmed`：`NA`
- `tc_present`：`Yes`
- `exh_present`：按图上是否有 EXH 填写

### TC-S

- `direction`：`SHORT`
- `main_signal`：`TC-S`
- `signal_chain`：`TC-S`
- `pattern_type`：`TrendContinuation`
- `trigger_break`：`NA`
- `pb_confirmed`：`NA`
- `tc_present`：`Yes`
- `exh_present`：按图上是否有 EXH 填写

## 衰竭提醒链条

### EXH-L

- `direction`：`LONG`
- `main_signal`：`EXH-L`
- `signal_chain`：`EXH-L`
- `pattern_type`：`Exhaustion`
- `trigger_break`：`NA`
- `pb_confirmed`：`NA`
- `tc_present`：`No`
- `exh_present`：`Yes`
- `result`：多数情况下先填 `NoTrade` 或 `Unknown`

如果 EXH-L 后出现 L-ZONE 和 LONG，可以写：

- `signal_chain`：`EXH-L→L-ZONE→LONG`
- `pattern_type`：`Reversal`
- `trigger_break`：`Yes`
- `exh_present`：`Yes`

### EXH-S

- `direction`：`SHORT`
- `main_signal`：`EXH-S`
- `signal_chain`：`EXH-S`
- `pattern_type`：`Exhaustion`
- `trigger_break`：`NA`
- `pb_confirmed`：`NA`
- `tc_present`：`No`
- `exh_present`：`Yes`
- `result`：多数情况下先填 `NoTrade` 或 `Unknown`

如果 EXH-S 后出现 S-ZONE 和 SHORT，可以写：

- `signal_chain`：`EXH-S→S-ZONE→SHORT`
- `pattern_type`：`Reversal`
- `trigger_break`：`Yes`
- `exh_present`：`Yes`

## 提前和延迟确认

### E-L / E-S

E-L / E-S 是突破或跌破发生，但严格进场条件不足。

- `main_signal`：`E-L` 或 `E-S`
- `pattern_type`：通常填 `FailedBreakout` 或 `Reversal`
- `trigger_break`：`Yes`
- `result`：如果后续快速反向，填 `Fail`；如果后续补出 LONG/SHORT，按最终链条调整。
- `notes`：记录缺少的严格条件，例如量能不足、未站上 EMA20、动能不足或风险不合格。

### LATE-L / LATE-S

LATE-L / LATE-S 是 Pivot 延迟确认后的补确认，不是追单信号。

- `main_signal`：`LATE-L` 或 `LATE-S`
- `pattern_type`：通常填 `Reversal`
- `trigger_break`：`Yes`
- `result`：未复盘前填 `Unknown`
- `notes`：记录确认时价格距离触发线是否过远。

## BTC TC 多、LONG 少的记录方式

当前代码没有 BTC 专属逻辑。如果 BTC 案例中 TC 多、LONG 少，应按实际信号记录：

- TC 案例：`main_signal=TC-L/TC-S`，`pattern_type=TrendContinuation`，`tc_present=Yes`
- 只有 Zone 没有 LONG/SHORT：`main_signal=L-ZONE/S-ZONE`，`result=NoTrade/Unknown/Fail`
- 不要把 BTC 的 TC 归为背离反转。
- 不要因为 BTC 上 LONG 少就修改信号定义。

### 当前 Gold Case 引用

以下案例用于 Signal Atlas 中说明 BTC 的 TC 趋势延续路径：

- `CASE-0004`：BTC_Gold_TC-L，Gold。路径：`gold_cases/BTC/TC/CASE-0004_BTC_Gold_TC-L.md`。
- `CASE-0006`：BTC_HTF_Trend_LTF_TC，Gold。路径：`gold_cases/BTC/TC/CASE-0006_BTC_HTF_Trend_LTF_TC.md`。

这两个案例只用于说明 TC-L 的趋势延续行为，不应解释为 LONG 较少的最终结论。最终结论需要等待 `research/questions/2026-07-07_BTC_TC_vs_LONG.md` 中的 100 个 BTC 样本验证。

## SOL Zone 到 Entry 到 PB 的记录方式

当前代码没有 SOL 专属逻辑。如果 SOL 案例出现完整链条，应按通用链条记录：

- 多头：`signal_chain=L-ZONE→LONG→PB-L`
- 空头：`signal_chain=S-ZONE→SHORT→PB-S`
- `pattern_type=Pullback`
- `trigger_break=Yes`
- `pb_confirmed=Yes`
- `main_signal` 可根据复盘重点填 `LONG/SHORT` 或 `PB-L/PB-S`

## 结果字段建议

- `Success`：信号后按预期方向走出有效空间。
- `Fail`：信号后快速反向或触发失效。
- `Early`：方向对但信号过早。
- `Late`：方向对但信号过晚。
- `NoTrade`：只观察不交易，例如单独 EXH 或单独 Zone。
- `Unknown`：截图后续不足，暂时无法判断。


## HTF Breakout / Recovery Pending Gold Case Candidate

以下案例用于 Signal Atlas 中说明高周期恢复状态、反趋势 HMR100 评分和执行风险分离：

- `CASE-0015`：BTCUSDT.P HTF Breakout Recovery，Good Case candidate / Gold Case candidate。路径：`gold_cases/BTC/TC/CASE-0015_BTC_HTF_Breakout_Recovery.md`。
  - 完整案例：`cases/CASE-0015_BTCUSDT.P_MultiTF_15m_TC-L_HTF_A-S-A-L_Conflict.md`。
  - 重点：15m / 30m 恢复并突破，21:00 前 1H 仍等待收盘确认；1m 高位动能减速不等于反向执行。
  - 候选状态链：`FLAT -> RECOVERY-L -> UP-PENDING -> UP-CONFIRMED`。
  - 执行原则：不追 `63800-64000`；未跌破 `63250` 并完成 bearish retest 前不做空；HMR100 不等于执行授权。
  - Outcome10 形成路径：`LTF UP -> FLAT -> DN / TC-S`，但 15m / 5m 仍为 `UP / TC-L`，因此暂归类为 `PULLBACK-S`，不是 `TREND-S`。
  - 候选角色规则：`LTF TC-S + HTF UP = PULLBACK-S`；`LTF TC-S + HTF DN = TREND-S`。
  - Outcome10：63550 附近支撑守住，未跌破 63300 / 63250；1m 收复约 63787 Trigger 后恢复 `UP / LATE-L HR85`，验证此前 `TC-S` 属于 `PULLBACK-S`。
  - 当前结果：`Unknown / Outcome10Recorded / Review10 / Favorable`；标签：`MTF_PULLBACK_RECOVERY`、`HTF_STATE_LAG`。
  - 形成过程：价格重新测试 64000，5m / 1m 进入 `L-ZONE HMR95 / BreakoutRetestActive`；随后 30m / 1H 均显示 `Ctx=UP`。执行仍为 `NoChase`。
  - 下一步：2026-07-15 00:27 UTC+8 后记录 Outcome20。

该引用只用于 Atlas 研究映射，不改变 Signal Manual 原则。
