# DVCA 案例复盘：CASE-0015

## 基本信息

- 案例编号：CASE-0015
- 用户请求编号：CASE-0010（已被 2026-07-08 BTC Context Shift 案例占用，本次不覆盖）
- 日期：2026-07-14
- 截图时间：19:23-19:27 UTC+8
- 交易品种：BTCUSDT.P
- 交易所：Binance
- 指标：DVCA 1.5.1
- 周期：1m / 5m / 15m / 30m / 1H
- 方向观察：LONG
- 主信号：15m TC-L after L-ZONE
- 模式：CounterTrendReversalAttempt
- 结果：Unknown（Outcome10 Favorable，等待 Outcome20）
- 初始评级：Research A- / Trade C
- 改进标签：CounterTrendSignalDowngrade

## 截图路径

- LTF：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_15m_TC-L_LTF_1923.png`
- 1H Context：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_1H_AS_HMR100_Context_1925.png`
- MTF：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_30m_AL_15m_TCL_1927.png`
- Outcome10：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_TC-L_Outcome10_2027.png`
- Outcome20 HTF Study：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_HTF_Breakout_Study_2048.png`
- Outcome20 High-Level Extension：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_HighLevel_Extension_2100.png`
- Outcome10 Sequence - Pullback Active：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_PullbackActive_2202.png`
- Outcome10 Sequence - Deep Pullback：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_DeepPullback_2205.png`
- Outcome10 Sequence - Pullback Recovery：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_PullbackRecovery_LATE-L_2218.png`
- Outcome10 Sequence - HTF State Lag：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_30m_1H_HTF_StateLag_2218.png`
- Outcome10 Sequence - Breakout Retest：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_BreakoutRetest_2258.png`
- Outcome10 Sequence - HTF Extension：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_30m_1H_BreakoutExtension_2307.png`
- Outcome10 Favorable LTF：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_Outcome10_Favorable_2346.png`
- Outcome10 Context / Last Conflict：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_30m_1H_Outcome10_ContextLastConflict_2346.png`

## Case Lifecycle

- 当前状态：Outcome10Recorded
- 下一步预期：Outcome20After2026-07-15_00:27_UTC+8
- 生命周期状态：Review10
- 执行状态：NoChase
- 当前评级：Good Case candidate / Gold Case candidate

## 多周期背景

### 1H

- `Ctx=DN`，高周期背景仍偏空。
- `Last=A-S HMR100`，记录的是 HTF 空头 Zone / 背离事件，不是本次 15m 反弹已失效的单独证明。
- 价格仍处于高周期压力下，因此低周期多头信号需降级处理。

### 30m

- `Ctx=FLAT`，市场从下跌进入修复 / 震荡阶段。
- `Last=A-L HMR100`，表示 HTF 多头 Zone / 背离观察事件。
- 30m 尚未建立明确多头趋势背景，不能单凭 `A-L HMR100` 定义反转完成。

### 15m

- `Ctx=UP`，低位 `L-ZONE` 后出现 `TC-L`。
- 15m 已形成多头反弹延续，但 `TC-L` 是趋势延续标签，不等于严格突破 `LONG`。
- 当前需验证反弹能否突破并接受 30m / 1H 压力。

### 5m

- `Ctx=UP`，价格保持在短周期均线结构上方。
- 截图中出现 `S-ZONE HMR100`，说明反弹过程中同时出现上方压力观察。
- 5m 不能单独解决 1H DN 与 15m UP 之间的冲突。

### 1m

- 反弹后仍可见 `TC-L`，但短周期中同时出现 Zone / 压力事件。
- 1m 只用于观察反弹节奏和确认细化，不用于覆盖 30m / 1H 背景。

## 信号链

```text
HTF bearish
→ 1H A-S HMR100
→ 30m A-L HMR100 / Recovery / FLAT
→ 15m L-ZONE
→ 15m TC-L bullish rebound
→ wait for confirmation beneath 30m / 1H resistance
```

## 冲突定义

```text
1H：A-S HMR100 / Ctx DN
30m：A-L HMR100 / Ctx FLAT
15m：TC-L / Ctx UP
```

- 1H 与 30m 的 `A-S / A-L` 都是 HTF Zone 事件，不是正式 `SHORT / LONG`。
- 15m `TC-L` 说明反弹延续，但它不是背离反转已确认的证明。
- 当前的研究价值正是跟踪低周期 `TC-L` 能否在 HTF 压力下升级。

## 当前信号

- 出现的标签：1H A-S HMR100 / 30m A-L HMR100 / 15m L-ZONE 后 TC-L
- 是否有背离线：Yes（HTF Zone 对应 Pivot 背离线）
- 是否有结构触发线：图上有 HTF Trigger 参考，但本次未记录为严格多头突破完成
- 是否突破触发线：No
- 是否出现 LONG/SHORT：No formal LONG / SHORT confirmation
- 是否出现 PB：No
- 是否出现 TC：Yes，15m TC-L
- 是否出现 EXH：No

## 研究问题

> 15m `L-ZONE → TC-L` 能否升级为确认反转，还是会在 30m / 1H 压力下失败？

## Outcome10 验证标准

- 计时周期：从初始截图后的 15m K 线计算 10 根。
- 反转升级证据：30m 从 `FLAT` 转向稳定 `UP`，价格突破并接受上方压力，且回踩不破反弹结构。
- 反弹失败证据：15m `TC-L` 后无法继续推进，15m 重新转弱，或 30m / 1H 压力下出现有效空头结构确认。
- 无交易证据：高低周期冲突持续，未出现正式 `LONG / PB-L`，也未出现明确的空头重新确认。

## Outcome10 Follow-up（2026-07-14 20:27 UTC+8）

- 价格：约 `63010`。
- 15m：`Ctx=UP`，最新 `TC-L`，RSI 约 `69.6`。
- 5m：`Ctx=UP`，最新 `TC-L`，RSI 约 `67.3`。
- 1m：`Ctx=UP`，最新 `TC-L`，RSI 约 `73`。

### 路径

```text
62850 附近受阻
→ 回踩 62760 附近
→ 1m 暂时转 DN
→ 支撑守住
→ 重新收复 62800
→ 1m 恢复 UP / TC-L
→ 放量突破 62920 与 63000
```

### 结论

- `S-ZONE` 对局部过度延伸给出了警告，但警告后的趋势空思路已被结构收复否定。
- 1m 支撑守住、重新转 `UP`并出现 `TC-L`，与 5m / 15m `UP + TC-L` 同步，是本次更可靠的多头延续确认。
- 这一结果支持 `CounterTrendSignalDowngrade`：Zone 警告不应在未有结构跟随时直接升级为反向执行。
- 本次只确认 LTF 反弹延续升级；初始记录的 30m / 1H 压力验证仍需等待 Outcome20。

### 执行边界

- 当前不在 `63010` 附近追多。
- 优先观察 `62920-62850` 回测是否守住。
- 失效条件：价格持续运行在 `62800` 下方。
- 案例评级：Good Case candidate。

## 结果

- 信号后 10 根 K 线：回踩 62760 附近后支撑守住，1m 从临时 DN 恢复为 UP / TC-L，随后放量突破 62920 与 63000；LTF 多头延续确认，等待 Outcome20 验证 HTF 压力。
- 信号后 20 根 K 线：等待 2026-07-15 00:27 UTC+8 后复盘。
- 信号后 50 根 K 线：尚未达到。
- 最大顺向空间：NA
- 最大反向回撤：NA
- 是否成功：Outcome10 方向验证为 Yes；最终 Result 保持 Unknown。

## 总结

- Outcome10 已确认 1m / 5m / 15m 同步 `UP + TC-L`，但仍不能据此确认 30m / 1H 反转完成。
- 该案例的交易评级为 C，因为 HTF 背景与 15m 信号冲突，且尚无严格 `LONG / PB-L`。
- 该案例的研究评级为 A-，因为它可用于验证 `CounterTrendSignalDowngrade`：反趋势 TC 应保留观察价值，但在高周期未同步前降级执行质量。
- 当前决策：`Outcome20Active / NoChase_WaitRetest`。


## Outcome10 形成过程：HTF Breakout Study（2026-07-14 20:48 UTC+8）

- 价格：约 `63780`。
- 截图：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_HTF_Breakout_Study_2048.png`。
- 案例评级：Gold Case candidate。
- 生命周期：Outcome10Active。

### 多周期状态

| 周期 | 状态 | 观察 |
| --- | --- | --- |
| 15m | Context UP / Latest TC-L | RSI 约 84.9，极端延伸 |
| 30m | Context UP / Latest A-L HMR100 | B score 100，RSI 约 80，Breakout confirmed 但过度延伸 |
| 1H | Context FLAT / Latest A-S HMR100 | B score 95，RSI 约 70，价格收复主要均线，但当前 K 线可能仍未收盘 |

### Audit Questions

1. 1H 是否在 K 线收盘后从 `FLAT` 切换为 `UP`？
2. 当前 `FLAT` 是否是合理的 close-confirmation delay？
3. `A-S HMR100` 是否错误覆盖了 recovery state？
4. HTF 是否应该在最终确认前显示 `UP-PENDING`？
5. `HMR100` 的反趋势评分是否会误导执行？

### Candidate State

```text
FLAT
-> RECOVERY-L
-> UP-PENDING
-> UP-CONFIRMED
```

### Execution

- 不在 `63780` 附近追多。
- 已有多单以利润管理为主。
- 优先等待回踩区：
  - `63500-63300`
  - `63250-63000`
  - `62900-62700`

### 阶段结论

15m / 30m 的多头恢复和突破已经成立，但 1H 仍处于 HTF close confirmation 的等待区。当前结果不能直接关闭为 Success，也不能把 `A-S HMR100` 解读为追空授权。本阶段为 Outcome10 形成过程，研究价值在于暴露 HTF recovery state、close-confirmation delay、反趋势 HMR100 评分与执行风险之间的关系。

## 20:48 阶段状态

- 当前状态：Outcome10Active。
- 下一步预期：Outcome10 正式确认。
- 生命周期状态：Open。
- 结果：Unknown。

## Outcome10 形成过程：High-Level Extension（2026-07-14 21:00 UTC+8）

- 价格：约 `63803`。
- 截图：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_HighLevel_Extension_2100.png`。
- 证据边界：本张图直接展示 15m / 5m / 1m；1H 状态必须等待 21:00 K 线收盘后使用 HTF 图另行确认。

### 多周期状态

| 周期 | 状态 | 观察 |
| --- | --- | --- |
| 15m | `UP / TC-L` | RSI 约 `79.4`，已处于极端延伸区 |
| 5m | `UP / TC-L` | RSI 约 `75.8`，趋势强但已延伸 |
| 1m | `UP / S-ZONE HMR100 / S invalid` | RSI 约 `70.6`，MACD Histogram 转负，动能开始减速 |

### 结构路径

```text
突破 63000
→ 突破 63250
→ 放量加速
→ 价格在 63500 上方得到接受
→ 测试 63800
→ LTF 动能开始减速
```

### Finding

- 15m / 5m `TC-L` 仍确认多头延续方向，但 RSI 和价格位置显示已进入过度延伸阶段。
- 1m `S-ZONE HMR100` 与 MACD Histogram 转负提示动能减速，但 `S invalid` 与尚未破坏的多头结构不支持立即做空。
- 该阶段应将“趋势方向仍多”与“新开多单执行质量已降低”分开记录。

### Execution

- 已有多单：管理利润，不在动能减速阶段扩大风险。
- 空仓：不在 `63800-64000` 附近追多。
- 反向做空：未跌破 `63250` 并完成 bearish retest 前，不建立空头执行资格。

### Next

- 等待 21:00 的 1H K 线收盘后确认 HTF 状态。
- 当前保持 `Result=Unknown`，不在 HTF 收盘前提前关闭为 Success。
- 下一生命周期节点：`Outcome10Recorded`。

## Outcome10 形成过程：Pullback Active（2026-07-14 22:02 UTC+8）

- 价格：约 `63715`。
- 截图：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_PullbackActive_2202.png`。

### 多周期状态

| 周期 | 状态 | 观察 |
| --- | --- | --- |
| 15m | `UP / TC-L` | RSI 约 `69`，高周期多头结构仍完整 |
| 5m | `UP / TC-L` | RSI 约 `57`，MACD Histogram 转负，回踩进行中 |
| 1m | `FLAT / S-ZONE HMR100 / S invalid` | RSI 约 `42`，MACD 为负，短周期从 UP 降为 FLAT |

### 状态路径

```text
64000 附近受阻
→ 跌破 63800
→ 1m UP 转 FLAT
→ 15m / 5m 仍保持 UP
→ LTF Pullback Active
```

### Display Study

```text
HTF Trend: UP
LTF Phase: PULLBACK
LTF State: FLAT
Execution: WAIT
```

### 关键价位

- 重新收复：`63780-63850`
- 第一支撑：`63650-63600`
- 下一支撑：`63450-63380`
- 核心结构：`63300-63250`

### 结论

- 1m 动能转弱，但尚未出现可执行的空头趋势确认。
- 图中没有 `PB-L`，因此也没有形成回踩多头执行信号。
- 该阶段记录为 `Outcome10PullbackActive / WAIT`，不因 1m 压力警告提前关闭案例。

## Outcome10 形成过程：Deep Pullback（2026-07-14 22:05 UTC+8）

- 价格：约 `63590`。
- 截图：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_DeepPullback_2205.png`。

### 多周期状态

| 周期 | 状态 | 观察 |
| --- | --- | --- |
| 15m | `UP / TC-L` | RSI 约 `64`，趋势仍多但动能减弱 |
| 5m | `UP / TC-L` | RSI 约 `53`，MACD Histogram 为负 |
| 1m | `DN / TC-S` | RSI 约 `35`，MACD 负向扩张，低周期回踩空确认 |

### 状态路径

```text
64000 附近受阻
→ 1m 动能减弱
→ 1m UP 转 FLAT
→ 跌破 63800
→ 跌破 63600
→ 1m FLAT 转 DN
→ 1m TC-S
```

### 研究分类

```text
LTF TC-S + HTF UP = PULLBACK-S
LTF TC-S + HTF DN = TREND-S
```

- `PULLBACK-S / TREND-S` 是本案例提出的研究分类，不是 DVCA v1.5.1 的原始标签。
- 当前 15m / 5m 仍为 `UP`，所以 1m `TC-S` 只确认低周期回踩空，不能解释为 HTF 趋势空。

### 关键价位

- 反抽压力：`63640-63700`
- 第一支撑：`63500-63450`
- 下一支撑：`63390-63300`
- 核心结构：`63250-63200`

### 回踩阶段结论

- 低周期回踩已从 `FLAT` 升级为 `DN / TC-S`，状态记为 `Outcome10DeepPullbackWatch`。
- 高周期趋势空尚未确认；只有 HTF 同步转 `DN` 后，研究分类才可从 `PULLBACK-S` 升级为 `TREND-S`。
- `Result` 保持 `Unknown`，等待回踩止稳或 HTF 结构破坏后再确定 `Success / Fail / Late / NoTrade`。
- 生命周期仍在 Outcome10 观察窗口内，不能提前推进到 Outcome20 / Outcome50。

## Outcome10 形成过程：Pullback Recovery（2026-07-14 22:18 UTC+8）

- 价格：约 `63829`。
- LTF 截图：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_PullbackRecovery_LATE-L_2218.png`。
- HTF 截图：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_30m_1H_HTF_StateLag_2218.png`。
- 标签：`MTF_PULLBACK_RECOVERY`、`HTF_STATE_LAG`。

### 多周期状态

| 周期 | 状态 | 观察 |
| --- | --- | --- |
| 1H | `FLAT / A-S HMR100 / B95` | RSI 约 `68.6`；价格已在主要均线上方，存在 HTF 状态滞后候选 |
| 30m | `UP / A-L HMR100 / B100` | RSI 约 `76`；多头恢复确认，但位置已过度延伸 |
| 15m | `UP / TC-L` | RSI 约 `72.8`；主信号方向延续 |
| 5m | `UP / TC-L` | RSI 约 `64.5`；低周期回踩已恢复 |
| 1m | `UP / LATE-L HR85` | Trigger 约 `63787`，RSI 约 `56.5`；此前 `DN / TC-S` 回踩被收复 |

### 完整路径

```text
HTF UP
→ LTF FLAT
→ LTF DN / TC-S
→ 63550 附近支撑守住
→ 未跌破 63300 / 63250
→ LTF 收复约 63787 Trigger
→ LTF 返回 UP
→ LATE-L HR85
```

### 研究结论

1. HTF 为 `UP` 时出现的 LTF `TC-S`，本案例验证为回踩阶段，而不是 HTF 趋势空。
2. 1m `LATE-L` 的方向正确，但由于 Pivot 确认延迟，执行确认偏晚，不应用作追单授权。
3. 1H 在结构收复、价格站上主要均线且动能偏多时仍显示 `FLAT / A-S HMR100`，继续支持 HTF state lag 审计。
4. 候选 HTF 状态链继续保留：`FLAT → RECOVERY-L → UP-PENDING → UP-CONFIRMED`。

### 恢复阶段判定

- 主信号 `15m L-ZONE → TC-L`：方向验证成功。
- Pullback 分类：`PULLBACK-S` 得到恢复路径验证，没有升级成 `TREND-S`。
- `LATE-L`：方向正确、执行偏晚；按说明书边界不作为追单信号。
- 案例状态：`Outcome10Active`。
- 阶段结果：方向 Favorable，但最终 Result 保持 Unknown。
- 评级：Good Case candidate / Gold Case candidate。

## Outcome10 形成过程：Breakout Retest Active（2026-07-14 22:58 UTC+8）

- 价格：约 `64030`。
- 截图：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_BreakoutRetest_2258.png`。
- 案例生命周期：`Outcome10Active`。
- 跟踪状态：`BreakoutRetestActive`。

### 多周期状态

| 周期 | 状态 | 观察 |
| --- | --- | --- |
| 15m | `UP / TC-L` | RSI 约 `76.7`，趋势延续但已延伸 |
| 5m | `UP / L-ZONE HMR95 / B95` | Trigger 约 `64086`，RSI 约 `63.8` |
| 1m | `UP / L-ZONE HMR95 / B95 / S invalid` | Trigger 约 `64010`，RSI 约 `59` |

### 路径

```text
64000 附近受阻
→ LTF UP → FLAT → DN
→ TC-S pullback
→ 63550 附近支撑守住
→ LTF 返回 UP
→ 收复 63787
→ 重新测试 64000
→ Breakout Test Active
```

### 关键价位

- Trigger 区：`64010-64090`
- 压力区：`64100-64250`
- 第一支撑：`63920-63850`
- 核心恢复支撑：`63820-63780`

### 分类与执行

- Pullback 已恢复，当前进入突破测试阶段。
- 5m / 1m `L-ZONE HMR95` 仍是观察区，不等同正式 `LONG`。
- 当前分类：`BreakoutRetestActive / NoChase`。
- 本段是 Outcome10 的突破测试过程，不提前写入最终 Success。

## Outcome10 形成过程：HTF Extension（2026-07-14 23:07 UTC+8）

- 截图：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_30m_1H_BreakoutExtension_2307.png`。
- 图上价格约 `64177`，30m 与 1H HUD 均显示 `Ctx=UP`。
- 该截图为 22:58 Breakout Test 后的延伸证据，支持 HTF 从恢复阶段转向多头确认。
- 位置已明显延伸，继续保留 `NoChase`，不把方向确认等同于当前执行质量。

## Outcome10 Recorded（2026-07-14 23:46 UTC+8）

- 用户请求编号：CASE-0010；项目实际编号：`CASE-0015`。`CASE-0010` 已被 2026-07-08 Context Shift 案例占用，不覆盖。
- 初始价格区域：约 `62700-62900`。
- 最新观察价格：约 `64770`。
- 主信号：`15m L-ZONE → TC-L`。
- Outcome10：Favorable。
- Direction Validated：Yes。
- Current Execution：`NoChase`。
- LTF 截图：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_Outcome10_Favorable_2346.png`。
- HTF 截图：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_30m_1H_Outcome10_ContextLastConflict_2346.png`。

### Breakout Confirmation

- `62920-63160` 压力簇已突破。
- `63500` 区域已突破。
- `64400` 区域已突破。
- Volume Confirmation：Yes。

### MTF State

| 周期 | 当前状态 |
| --- | --- |
| 5m | 强势 `UP`，但已过度延伸 |
| 15m | `UP / TC-L`，RSI 超买 |
| 30m | 结构突破，`Last` 仍为 `A-L HMR100` |
| 1H | `Ctx=UP`，`Last` 仍为 `A-S HMR100` |

### 顶部风险提示

- 低周期出现 `S-ZONE` 与 `C-S`。
- 在当前高位，它们先作为风险警告，不直接构成反向执行授权。
- 当前执行保持 `NoChase`。

### 改进标签

- `HTFSignalLag`
- `StaleLastSignal`
- `ContextLastConflict`
- `CounterSignalAsRiskWarning`

### Lifecycle

- 当前状态：`Outcome10Recorded`。
- 生命周期状态：`Review10`。
- 结果：`Unknown`，Outcome10 为 Favorable。
- 暂定评级：Good Case candidate / Gold Case candidate。
- 下一次复盘：2026-07-15 00:27 UTC+8 之后记录 Outcome20。
