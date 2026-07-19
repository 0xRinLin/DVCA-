# DVCA 案例复盘：CASE-0016

## 基本信息

- 案例编号：CASE-0016
- 日期：2026-07-16
- 截图时间：20:47 UTC+8
- 交易品种：BTCUSDT
- 交易所：Binance
- 截图指标版本：DVCA 1.5.1
- 当前项目基线：DVCA v1.5.4
- 周期：1H / 30m / 15m / 5m / 1m
- 方向观察：SHORT
- 主信号：TC-S / Full MTF Recovery / 64150 Breakout Attempt
- 模式：BearishTransitionRecoveryFailure
- 结果：Unknown
- 暂定评级：Good Case candidate
- 研究标签：HTF_DN_PENDING / TC_S_TREND_CONFIRMATION

## 证据边界

- 本案例截图右侧 HUD 明确显示 `DVCA 1.5.1`，因此属于历史版本研究证据。
- 当前正式主版本是 `indicator/current/dvca_v1_5_4.pine`；本案例不能直接用于认定 v1.5.4 存在高周期状态滞后。
- `DN-PENDING` 是基于本案例提出的候选研究状态，不是 DVCA v1.5.1 或 v1.5.4 已实现的正式状态。
- 若要进入 v1.5.4 高周期专项数据库，必须使用 v1.5.4 在同类行情上重新截图并完成人工逐根 K 线复核。

## 截图路径

- 5m / 15m / 1m：`screenshots/BTCUSDT/2026-07-16/2026-07-16_BTCUSDT_MultiTF_TC-S_BearishTransition_2047.png`
- 30m / 1H：`screenshots/BTCUSDT/2026-07-16/2026-07-16_BTCUSDT_30m_1H_DN-PENDING_2047.png`
- 中间恢复分支 5m / 15m / 1m：`screenshots/BTCUSDT/2026-07-16/2026-07-16_BTCUSDT_BearishContinuationFailure_LTF_2229.png`
- 中间恢复分支 30m / 1H：`screenshots/BTCUSDT/2026-07-16/2026-07-16_BTCUSDT_BearishContinuationFailure_HTF_2230.png`
- Outcome10 5m / 15m / 1m：`screenshots/BTCUSDT/2026-07-17/2026-07-17_BTCUSDT_MultiTF_RecoveryFailure_TC-S_Outcome10_1228.png`
- Outcome10 30m / 1H：`screenshots/BTCUSDT/2026-07-17/2026-07-17_BTCUSDT_30m_1H_BearishAlignment_Outcome10_1228.png`
- Outcome20 Active 30m / 1H（16:07）：`screenshots/BTCUSDT/2026-07-17/2026-07-17_BTCUSDT_30m_1H_BearishReconfirmation_1607.png`
- Outcome20 Active 30m / 1H（16:08）：`screenshots/BTCUSDT/2026-07-17/2026-07-17_BTCUSDT_30m_1H_ExtensionZoneReached_1608.png`
- Outcome20 5m / 15m / 1m（19:10）：`screenshots/BTCUSDT/2026-07-17/2026-07-17_BTCUSDT_MultiTF_FirstPullbackAfter5mUP_1910.png`
- Outcome20 30m / 1H（19:10）：`screenshots/BTCUSDT/2026-07-17/2026-07-17_BTCUSDT_30m_1H_SecondRepair_HTF_1910.png`
- Full MTF Recovery 5m / 15m / 1m（21:07）：`screenshots/BTCUSDT/2026-07-18/2026-07-18_BTCUSDT_MultiTF_FullRecovery_FirstPullback_2107.png`
- First Pullback LTF Detail（21:07）：`screenshots/BTCUSDT/2026-07-18/2026-07-18_BTCUSDT_MultiTF_FirstPullback_LTF_Detail_2107.png`
- Full MTF Recovery 30m / 1H（21:12）：`screenshots/BTCUSDT/2026-07-18/2026-07-18_BTCUSDT_30m_1H_FullRecovery_HTF_2112.png`
- First Pullback Held 5m / 15m / 1m（22:04）：`screenshots/BTCUSDT/2026-07-18/2026-07-18_BTCUSDT_MultiTF_FirstPullbackHeld_LTFReconfirmation_2204.png`
- Full MTF Recovery 30m / 1H（22:04）：`screenshots/BTCUSDT/2026-07-18/2026-07-18_BTCUSDT_30m_1H_FullMTFRecovery_2204.png`
- 64150 Breakout Attempt 5m / 15m / 1m（22:31）：`screenshots/BTCUSDT/2026-07-18/2026-07-18_BTCUSDT_MultiTF_64150_BreakoutAttempt_2231.png`
- 64150 Breakout Attempt 30m / 1H（22:31）：`screenshots/BTCUSDT/2026-07-18/2026-07-18_BTCUSDT_30m_1H_64150_BreakoutAttempt_2231.png`

## Case Lifecycle

- 当前状态：Outcome20Recorded
- 下一步预期：Outcome50
- 生命周期状态：Review20
- Outcome10：Recovery Branch Failed / Bearish Continuation Active
- Outcome20：Favorable for original SHORT direction / 62800-62600 extension reached / Second Low-Level Repair Active
- Outcome50：Pending
- Current Recovery Branch：Outcome10Active / Strong Recovery / HTF Upgrade Confirmed
- 最终结果：Unknown
- 最终评级：Pending，Outcome 未完成前不晋升为 Good Case

## 初始多周期状态表（2026-07-16 20:47 UTC+8）

| 周期 | 图上 Context | 最新信号 | 动能/位置 | 研究判断 |
| --- | --- | --- | --- | --- |
| 1H | FLAT | A-S HMR95 | RSI 约 35.6，动能偏空 | 高周期尚未正式转 DN；候选观察为 DN-PENDING |
| 30m | DN / B100 | A-S HMR100 | RSI 约 30.8，MACD 为负 | 核心结构已经转弱 |
| 15m | DN / B100 | TC-S | RSI 约 33.9 | 空头执行环境已形成 |
| 5m | DN | TC-S | RSI 约 49.8 | 执行周期保持空头延续 |
| 1m | DN / S95 | TC-S | RSI 约 36.7 | 精细周期跟随下跌，但正接近支撑 |

## 当前市场结构

```text
延伸上涨
→ S-ZONE / C-S / LATE-S 风险警告
→ 高点降低
→ 跌破 64500
→ 跌破 64100 / 64000
→ 30m / 15m / 5m / 1m 转为 DN
→ 多周期 TC-S 延续
→ 测试 63800-63780 支撑
```

- 30m 以下周期的空头转折已经一致，说明这不再只是 1m 的局部回踩。
- 1H 仍显示 `FLAT`，因此“1H 趋势空确认”尚未完成。
- 当前价格已接近支撑，方向判断偏空不等于此处具备良好追空盈亏比。

## 信号链

- 观察区/风险信号：S-ZONE / A-S HMR95-100。
- Zone 确认提示：C-S。
- 延迟补确认：LATE-S，只记录转弱补确认，不作为追单信号。
- 趋势延续：30m 以下多个周期转 DN 后出现 TC-S。
- 正式执行信号：截图未确认独立 `SHORT` 或 `PB-S`。
- 当前分类：`MTF bearish transition below 1H / TC-S continuation / no chase into support`。

## 关键价位与失效条件

- 当前支撑：`63800-63780`。
- 下一支撑观察区：`63500-63300`。
- 第一反抽压力：`64050-64150`。
- 核心压力区：`64300-64500`。
- 空头延续失效观察：重新站回 `64150`，并在 5m / 15m 形成更高低点结构。
- 更强失效证据：重新收复 `64300-64500`，且 30m 不再保持 DN。

## 多头与空头交易计划

### 空头计划

- 当前动作：等待，不直接在 `63800-63780` 支撑附近追空。
- 入场触发：反抽 `64050-64150` 后无法站稳，5m / 1m 形成更低高点，并重新出现 TC-S、SHORT 或 PB-S 之一。
- 止损原则：放在反抽确认高点上方；仅凭当前截图无法可靠给出精确止损价。
- 目标观察：先看 `63800-63780`，有效跌破并回抽不回后再看 `63500-63300`。
- 无效条件：持续站回 `64150` 并形成更高低点；若进一步收复 `64300-64500`，空头转折假设明显减弱。

### 多头计划

- 当前动作：禁止仅因接近支撑或 RSI 偏低而逆势做多。
- 入场触发：至少收复 `64150`，形成 5m 更高低点，并使 15m 空头延续结构失效。
- 止损原则：放在确认后的更高低点下方；当前截图不足以确定精确位置。
- 目标观察：`64300-64500` 压力区。
- 无效条件：反抽无法站稳 `64050-64150`，随后再度跌破 `63800-63780`。

## 评分

- 信号方向评分：`8/10`。30m、15m、5m、1m 同向 DN，TC-S 延续一致。
- 当前位置评分：`4/10`。价格正测试支撑，追空位置不佳。
- 多周期一致性评分：`7/10`。30m 以下一致，但 1H 仍是 FLAT。
- 当前交易评分：`5/10`。方向明确、执行位置欠佳，需等待反抽确认。
- 研究价值评分：`8/10`。适合验证 1H `FLAT` 到潜在 `DN` 之间是否需要过渡状态。

## Outcome 剧本

### Outcome10

- 空头延续：跌破 `63800-63780`，反抽不能收回，向 `63500-63300` 推进。
- 反抽修复：守住 `63800-63780` 并收复 `64150`，但尚不足以确认高周期反转。
- 震荡：价格在 `63780-64150` 内整理，保持 NoTrade。

### Outcome20

- 观察 30m 是否继续保持 DN。
- 观察 1H 是否从 FLAT 进入正式 DN，或重新恢复到非空头结构。
- 记录反抽是否产生 SHORT / PB-S，避免只统计 TC-S 标签数量。

### Outcome50

- 判断这次转弱属于完整趋势反转、有限回调还是假跌破。
- 完成最大顺向空间、最大反向回撤和最终案例评级。
- 只有 Outcome50 与人工复核完成后，才决定是否将本案例晋升为 Good Case。

## 指标改进建议

1. 研究 `FLAT → DN-PENDING → DN` 的过渡展示，但不得基于单一 v1.5.1 案例直接改代码。
2. 分离 `HTF Context`、`Last Zone Event` 与 `LTF Execution Signal`，避免把 A-S 高分误读成正式追空授权。
3. 在 TC-S 方向正确但贴近支撑时增加位置/延伸惩罚或 `No-Chase` 提示。
4. 使用 v1.5.4 复现同类样本，核对 1H/30m 状态切换是否仍存在相同现象。

## Follow-up 要求

- 以 15m 为主计时，补充信号后 10、20、50 根 K 线截图。
- Outcome10 截图必须覆盖 `63800-63780` 的最终处理结果。
- Outcome20 需同时保留 1H / 30m / 15m，确认高周期状态是否切换。
- 复现时使用 DVCA v1.5.4，并记录 Zone 的 pivot 位置与真实确认时间。

## 中间 Follow-up（2026-07-16 22:30 UTC+8）

- 价格：约 `64740`。
- 截图：
  - `screenshots/BTCUSDT/2026-07-16/2026-07-16_BTCUSDT_BearishContinuationFailure_LTF_2229.png`
  - `screenshots/BTCUSDT/2026-07-16/2026-07-16_BTCUSDT_BearishContinuationFailure_HTF_2230.png`
- 阶段状态：Bearish Continuation Failed。
- Recovery Branch：SignalCaptured。
- Result：Unknown。

### Previous

```text
1H FLAT
30m / 15m / 5m / 1m DN
TC-S
Price tested 63780 support
```

### 阶段路径

```text
63780 support held
Price reclaimed 64150
Price reclaimed 64500
1m and 5m changed to UP
15m, 30m and 1H returned/remained FLAT
Bearish continuation failed
```

### Intermediate MTF

| 周期 | 状态 |
| --- | --- |
| 1H | FLAT，A-S HMR95 |
| 30m | FLAT，A-S HMR100 |
| 15m | FLAT，latest TC-S |
| 5m | UP，latest TC-L |
| 1m | UP，latest TC-L，S invalid |

### 阶段解释

这是 `LTF bullish recovery inside HTF transition`，不是已经确认的 HTF uptrend。

- 不追 `64850-65000` 阻力区。
- 原 TC-S / Bearish Continuation 在本阶段失效。
- Recovery Branch 进入 `SignalCaptured`，等待后续验证是否升级为 HTF recovery 或再次失败。

### 阶段关键价位

- Resistance：`64850-65000`
- Support：`64600-64500`
- Next：`64350-64250`
- Core：`64150-64000`
- Failure：below `63780`

### 阶段结论

63780 支撑守住并连续收复 64150 / 64500 后，1m 与 5m 切换为 UP，说明原 30m 以下的 Bearish Continuation 在这一阶段失败。但 15m、30m、1H 仍为 FLAT 或 transition，因此不能提前判定为 HTF 多头趋势确认；该恢复分支继续等待后续结果。

## Outcome10 Resolution（2026-07-17 12:28 UTC+8）

### 数据读取说明

- 图表十字光标位于历史 K 线上，顶部 OHLC 属于光标选中的历史柱，不代表当前价格。
- 当前价格约 `63341.4`，取自实时买卖报价与右侧价格轴标签。
- 本节只使用用户提供并能在截图中核验的最新 HUD、MACD、RSI 和价位信息。

### 最新多周期状态

| 周期 | Context / 状态 | 最新信号 | MACD / Histogram | RSI / MA |
| --- | --- | --- | --- | --- |
| 1H | DN / B95 / Trig 60758.3 | A-S HMR95 | -269.9 / -194.3 / -75.6 | 32.65 / 41.25 |
| 30m | DN / B100 / Trig 64438.9 | A-S HMR100 | -220.7 / -183.5 / -37.2 | 31.75 / 36.08 |
| 15m | DN / B invalid | TC-S | -148.7 / -140.8 / -8.0 | 31.90 / 36.93 |
| 5m | DN / S95 / Trig 63358.0 / B invalid | TC-S | -62.5 / -42.9 / -19.6 | 34.67 / 44.17 |
| 1m | DN / S invalid | TC-S | -43.5 / -42.5 / -1.0 | 34.34 / 33.49 |

### 实际路径

```text
63780 支撑初次守住
→ 收复 64150
→ 收复 64500
→ 1m / 5m 转 UP
→ 64750-64800 附近受阻
→ 首次回踩 64500
→ 64500-64430 支撑失败
→ 跌破 64300
→ 跌破 64150-64000
→ 跌破 63780 核心支撑
→ 30m / 1H 转 DN
→ 五周期空头对齐
→ 当前价格约 63341
```

### Outcome10 判定

- Recovery Branch：`Failed`。短线收复 64150 和 64500 后，未能守住 64500-64430，最终跌破 63780。
- Bearish Continuation：`Active`。确认依据为 63780 跌破，以及 30m / 1H 均转 DN。
- 原始 CASE-0016 空头方向：Favorable / Direction Validated at Outcome10。
- 最终 Result：仍为 Unknown，等待 Outcome20 和 Outcome50；不得把 Outcome10 方向验证提前写成最终 Good Case。

### 最新关键价位

- 第一压力：`63400-63500`。
- 优先空头设置区：`63500-63620`。
- 核心压力：`63770-63900`。
- 强压力：`64050-64200`。
- 当前支撑：`63300-63200`。
- 下一观察：`63000`。
- 延伸观察：`62800-62600`。

### 最新执行计划

- 不在约 `63341` 追空；15m、30m、1H RSI 已接近低位，位置风险高。
- 优先等待反抽 `63500-63620` 或 `63770-63900` 后出现空头拒绝，再评估顺势空。
- 破位空必须等待 `63200` 跌破并反抽失败，不能只凭瞬间下破执行。
- 五个周期都保持 DN 时，多头尚未确认。
- 逆势多至少需要 1m 转 UP，并出现 TC-L 或 PB-L，同时 5m 不再创出新低。
- 精确止损应依据反抽确认高点或结构低点设置；当前截图不足以给出统一固定止损价。

### 研究结论

1. 2026-07-16 的 `DN-PENDING` 候选观察在 v1.5.1 后续图中最终演化为 1H `DN`，但这仍不是 v1.5.4 的验证结果。
2. 恢复分支先转强再失败，说明单次 LTF 收复不能覆盖 30m / 1H 的后续确认；需要持续守住关键结构。
3. TC-S 的方向确认与执行位置必须分开：五周期空头对齐不等于接近支撑时可以追空。
4. Outcome20 应重点检查 `63200` 是否有效跌破，以及反抽 `63500-63620` 是否形成拒绝。

## 当前结论

Outcome10 已确认恢复分支失败，`1H/30m/15m/5m/1m` 全部转为 DN，CASE-0016 的空头方向得到阶段验证。当前价格约 63341，正靠近 `63300-63200` 支撑，执行仍是等待反抽拒绝或 63200 破位回测，禁止低位追空；最终结果与案例评级继续等待 Outcome20/50。

## Outcome20 Active Follow-up（2026-07-17 16:07 UTC+8）

### 数据读取说明

- 截图时间范围：2026-07-17 16:07:23-16:07:32 UTC+8。
- 截图价格范围：`62824.2-62830.4`；本次记录参考价约 `62830`。
- 图表十字光标位于历史 K 线上，顶部 OHLC 属于选中的历史柱；当前价格取自实时买卖报价与右侧价格轴。
- 屏幕边缘裁切或标签重叠的数值不作估算。
- 两张归档截图均展示 30m / 1H；15m / 5m / 1m 状态与数值按本次用户报告归档，不能当作两张图片直接显示的字段。

### 最新多周期状态

| 周期 | Context / 状态 | 最新信号 | 结构备注 |
| --- | --- | --- | --- |
| 1H | DN / B95 / Trig 60758.3 | A-S HMR95 | 高周期保持空头，RSI 接近低位 |
| 30m | DN / B100 / Trig 64438.9 | A-S HMR100 | 核心结构保持空头 |
| 15m | DN / B invalid | TC-S | 空头延续仍有效 |
| 5m | DN / B100 / Trig 63078.4 / B invalid | L-ZONE HMR100 | 低位修复观察区未升级为正式多头 |
| 1m | DN / S invalid | TC-S | FLAT 修复结束后重新转 DN |

### 最新可见指标

| 周期 | MACD / Signal / Histogram | RSI / MA |
| --- | --- | --- |
| 1H | -407.7 / -300.0 / -106.7 | 28.70 / 35.73 |
| 30m | MACD 主线被裁切 / -293.2 / -47.4 | 28.66 / 30.96 |
| 15m | -232.1 / -231.9 / -0.2 | 30.86 / 第二标签被裁切 |
| 5m | -64.3 / -85.7 / +11.4 | 41.08 / 40.84 |
| 1m | -19.0 / -18.5 / -0.5 | 47.38 / 41.35 |

### 最新可见均线

- 1H：`63976.3 / 63964.4 / 63680.5 / 63602.7`。
- 30m：`64020.1 / 63985.6 / 63700.1 / 63329.6`。
- 15m：`64033.0 / 63815.5 / 63092.2`。
- 5m：`63627.8 / 63301.5 / 63048.4`。
- 1m：`62994.1 / 62883.7 / 62855.3 / 62835.7`。

### 后续路径

```text
跌破 63200
→ 跌破 63000
→ 进入 62800-62600 延伸观察区
→ 1m / 5m 出现 L-ZONE HMR100
→ 1m 从 DN 转为 FLAT
→ 低位修复至 62900 附近
→ 未能收复 62950-63080
→ 1m 再次出现 TC-S
→ 1m 从 FLAT 返回 DN
→ 五周期 DN 对齐恢复
→ 当前价格约 62830
```

### 分支状态

- Recovery Branch：`Outcome10Failed`，保持不变。
- Bearish Continuation：`Active`；`62800-62600` 延伸目标区已经到达。
- Low-Level Repair Branch：此前为 Active，本次确认为 `Failed`。
- 修复失败确认：1m `FLAT → DN`，同时最新信号重新变为 TC-S。
- Current Execution Branch：`Active / Bearish Reconfirmation above Core Low`。
- Lifecycle：仍为 `Outcome10Recorded / Review10`，本节仅为 Outcome20 Active 跟踪，尚未达到完整 20 根 15m K 线。
- 最终 Result：`Unknown`。

### 最新关键价位

- 即时压力：`62835-62885`。
- 第一压力：`62950-63000`。
- 方向测试区：`63048-63080`。
- 下一压力：`63200-63330`。
- 核心压力：`63500-63630`。
- 当前支撑：`62800-62745`。
- 核心支撑：`62650-62600`。
- 延伸观察：`62400-62200`。
- 深层参考：`62000-61865`。

### 最新执行计划

- 不在 `62800` 支撑附近直接追空。
- 优先等待反抽 `62950-63080` 后出现空头拒绝，再评估顺势空。
- 次级计划是等待 `63200-63330` 的反抽拒绝。
- 破位空只在 `62600` 跌破并完成失败回测后评估。
- 五周期仍为 DN 时，多头尚未确认。
- 逆势多至少需要 1m 从 FLAT 转 UP，并出现 TC-L 或 PB-L；单独 L-ZONE HMR100 不构成正式多头进场。
- 具体止损必须放在实际反抽确认高点或结构失效位之外，当前截图不足以给出统一固定止损价。

### 本阶段结论

价格已经跌破 63200 和 63000，并到达 `62800-62600` 延伸观察区。1m / 5m 的 L-ZONE HMR100 只形成短暂低位修复，未能收复 `62950-63080`，随后 1m 重新出现 TC-S 并从 FLAT 返回 DN。当前属于核心低点上方的空头再确认，但位置已贴近支撑，方向有效不等于可以追空；继续等待完整 Outcome20。

## Outcome20 Resolution：5m 转 UP 后首次回踩（2026-07-17 19:10 UTC+8）

### 数据读取说明

- 截图时间范围：2026-07-17 19:10:02-19:10:12 UTC+8；当前参考价约 `63075`。
- 图表十字光标位于历史 K 线上，顶部 OHLC 属于选中的历史柱；当前价格取自实时买卖报价与右侧价格轴。
- 本次截图覆盖 1H、30m、15m、5m、1m；30m 一条 MACD 数值被水平标记遮挡，不作估算。
- 从 Outcome10 的 2026-07-17 12:28 到本次截图已超过 20 根 15m K 线，因此本次正式记录 Outcome20。

### Outcome20 多周期状态

| 周期 | Context / 状态 | 最新信号 | 结构解释 |
| --- | --- | --- | --- |
| 1H | DN / B95 / Trig 60758.3 | A-S HMR95 | 高周期空头背景未改变 |
| 30m | DN / B100 / Trig 64438.9 | A-S HMR100 | 核心空头结构未改变 |
| 15m | DN / B invalid | TC-S | 恢复尚未升级到 15m |
| 5m | UP / S expired | TC-L | 第二次低周期修复已进入执行周期 |
| 1m | FLAT / S100 / Trig 63133.2 / S invalid | S-ZONE HMR100 | 5m 转 UP 后的首次回踩，等待方向确认 |

### 最新可见指标

| 周期 | MACD / Signal / Histogram | RSI / MA |
| --- | --- | --- |
| 1H | -372.1 / -342.0 / -30.1 | 36.82 / 31.95 |
| 30m | 主线被水平标记遮挡 / -320.1 / +47.9 | 41.11 / 32.52 |
| 15m | -51.6 / -111.5 / +59.6 | 49.23 / 41.75 |
| 5m | 51.9 / 57.1 / -5.2 | 55.23 / 61.72 |
| 1m | -10.9 / -10.3 / -0.6 | 34.37 / 47.80 |

### 最新可见均线

- 1H：`63912.4 / 63873.9 / 63671.2 / 63465.2`。
- 30m：`63928.0 / 63904.6 / 63621.9 / 63186.6`。
- 15m：`63914.6 / 63639.3 / 63298.8 / 63041.2`。
- 5m：`63424.0 / 63056.9 / 63016.4`。
- 1m：`63114.7 / 63103.0 / 63057.0 / 63011.7`。

### Outcome20 路径

```text
跌破 63200 / 63000
→ 进入 62800-62600 延伸区
→ 第一次低周期修复失败
→ 62800 再次守住
→ 第二次低周期修复
→ 1m 转 UP
→ 收复 62900 / 63000
→ 5m DN → FLAT → UP
→ 5m 最新 TC-L
→ 反弹至 63150 附近
→ 1m S-ZONE / C-S
→ 1m UP → FLAT
→ 当前首次回踩约 63075
```

### 分支与生命周期判定

- Recovery Branch：`Outcome10Failed`，历史判定保持不变。
- Bearish Continuation：`Active at HTF / Execution Timeframe Paused`。1H、30m、15m 仍为 DN，但 5m 已转 UP，不允许把高周期空头背景直接转换成当前追空授权。
- First Low-Level Repair：`Failed`。
- Second Low-Level Repair：`Active / Countertrend Recovery`。
- 当前事件：`First Pullback after 5m UP`。
- Outcome20：原始 SHORT 方向为 Favorable，价格已经到达 `62800-62600` 延伸区；当前第二次低周期修复尚未完成，不能据此关闭案例。
- Lifecycle：`Outcome20Recorded / Review20 / Outcome50`。
- 最终 Result：`Unknown`。

### 关键价位

- 即时支撑：`63060-63040`。
- 第二支撑：`63020-63000`。
- 深回踩支撑：`62950-62900`。
- 恢复核心支撑：`62825-62800`。
- 低位核心支撑：`62650-62600`。
- 即时压力：`63103-63115`。
- Trigger 压力：`63133-63150`。
- 下一压力：`63186-63205`。
- 核心压力：`63298-63350`。
- 强压力：`63420-63470`。

### 当前执行计划

- 1m 保持 FLAT 时不进场。
- 多头只在 `63060-63040` 或 `63020-63000` 守住，且 1m 返回 UP 并出现 TC-L / PB-L 后评估。
- 突破多必须收复 `63150` 并完成成功回测；恢复升级还需收复 `63205`，同时 15m 退出 DN。
- 5m 保持 UP 时不主动做空；1m 的 S-ZONE 只作为压力警告，不是 SHORT。
- 空头执行至少需要跌破 `63000`、回测失败，并由 1m TC-S / PB-S 确认。
- HTF 在图上确认 Context 改变前仍按 DN 记录。

### Outcome20 结论

原始空头方向在 Outcome20 阶段得到进一步验证，价格到达 `62800-62600` 延伸区；但 62800 再次守住后，第二次低周期修复使 5m 从 DN 经 FLAT 转为 UP，并出现 TC-L。当前 1m 在 63150 附近出现 S-ZONE / C-S 后回到 FLAT，属于 5m 转 UP 后的首次回踩。此时最合理的执行是等待 1m 确认，而不是在高周期 DN 与 5m UP 冲突时追空或追多。案例继续等待 Outcome50。

## Current Recovery Branch：Full MTF Recovery First Pullback（2026-07-18 21:07-21:12 UTC+8）

### 数据完整性

- 1m / 5m / 15m 数据取自 21:07 截图，当前价格约 `64109.5`。
- 30m / 1H 数据取自 21:12 补充截图，当前价格约 `64020.9`。
- 历史十字光标 OHLC 不作为当前价格；两次截图之间不反推任何指标数值。
- 1H 慢速蓝色均线标签被重叠遮挡，不作估算。

### 当前多周期状态

| 周期 | Context / DVCA | 最新信号 | 当前解释 |
| --- | --- | --- | --- |
| 1H | UP / B95 / Trig 60758.3 | A-S HMR95 | HTF 已升级为 UP，但 Last 仍保留历史反向警告 |
| 30m | UP / B100 / Trig 64438.9 | A-S HMR100 | 结构已转 UP，Last 与 Context 存在陈旧信号冲突 |
| 15m | UP / B expired | TC-L | 多头恢复已扩展到执行环境 |
| 5m | UP / S invalid | TC-L | 主要执行周期保持多头 |
| 1m | FLAT / B expired | TC-L | 全周期转强后的首次回踩，暂不执行 |

### 当前可见指标

| 周期 | MACD / Signal / Histogram | RSI / MA |
| --- | --- | --- |
| 1H | 86.1 / 75.8 / +10.3 | 55.32 / 56.25 |
| 30m | 52.6 / 50.2 / +2.4 | 54.22 / 57.30 |
| 15m | 45.1 / 28.3 / +16.7 | 61.41 / 60.04 |
| 5m | 41.3 / 39.3 / +2.0 | 56.63 / 72.79 |
| 1m | -5.7 / 5.4 / -11.1 | 38.32 / 50.77 |

### 当前可见均线

- 1H：`63932.1 / 63905.5 / 63902.7 / 慢速蓝线不可独立读取`。
- 30m：`63992.1 / 63901.4 / 63895.2 / 63894.8`。
- 15m：`64034.7 / 63968.8 / 63888.9 / 63888.0`。
- 5m：`64094.6 / 64039.4 / 63999.5 / 63928.4`。
- 1m：`64146.8 / 64130.3 / 64094.5 / 64051.2`。

### 状态路径

```text
62850 附近形成支撑
→ 收复 63000
→ 收复 63500
→ 收复 63780
→ 收复 64000
→ 5m 转 UP
→ 15m 转 UP
→ 30m 转 UP
→ 1H 转 UP
→ 推进至 64180-64220
→ 1m 转 FLAT
→ 首次回踩 64050-64000
```

### 分支状态

- Historical Recovery：`Outcome10Failed`，保留历史结论。
- First Low-Level Repair：`Failed`。
- Second Low-Level Repair：此前 Active，本次后续升级为 Full MTF Recovery。
- Previous Bearish Continuation：`Invalidated at 5m / 15m / 30m / 1H directional layers`。
- Current Recovery Branch：`Outcome10Active / Strong Recovery / HTF Upgrade Confirmed`。
- 当前事件：`First Pullback after Full MTF Bullish Alignment`。
- 主案例生命周期仍为 `Outcome20Recorded / Review20 / Outcome50`；分支 Outcome10 不覆盖主案例生命周期。
- 最终 Result：`Unknown`。

### 关键价位

- 即时压力：`64095-64150`。
- 第一压力：`64180-64220`。
- 下一压力：`64300`。
- 30m HUD Trigger 参考：`64438.9`。
- 即时支撑：`64050-64000`。
- 核心均线支撑：`63930-63890`。
- 趋势防守：`63780-63730`。
- 深层支撑：`63565`。
- HTF 结构参考：`62970.3`。

### 执行计划

- 1m 保持 FLAT 时不直接入场。
- 多头只在 1m 重新确认 UP，并出现 TC-L 或 PB-L 后评估。
- 优先多头观察区为 `64050-64000` 与 `63930-63890`。
- 1H / 30m / 15m / 5m 同为 UP 时，不主动逆势做空。
- 空头至少需要跌破 `63890`、在 `64000` 附近回测失败、1m 转 DN，并出现 TC-S 或 PB-S。

### 当前结论

这次恢复已经从低周期修复升级为 1H、30m、15m、5m 的方向一致转强，原 Bearish Continuation 在这些方向层被否定。1m 当前转为 FLAT，属于 Full MTF Bullish Alignment 后的首次回踩；因此恢复方向得到明显强化，但执行必须等待 1m 再确认。Current Recovery Branch 先记为 Outcome10Active，主案例继续等待 Outcome50，最终结果不提前判定。

## Current Recovery Branch Follow-up：First Pullback Held / LTF Reconfirmation Completed（2026-07-18 22:04 UTC+8）

### 数据完整性

- 五个周期数据均来自同一次 22:04 截图，当前价格约 `64093.8`。
- 当前价格读取自实时报价与右侧价格轴；历史十字光标 OHLC 不作为当前值。

### 当前多周期状态

| 周期 | Context / DVCA | 最新信号 | 当前解释 |
| --- | --- | --- | --- |
| 1H | UP / B95 / Trig 60758.3 | A-S HMR95 | 高周期恢复保持有效，Last 仍是历史反向警告 |
| 30m | UP / B100 / Trig 64438.9 | A-S HMR100 | 方向保持 UP，Context 与 Last 的陈旧信号冲突仍存在 |
| 15m | UP / B expired | TC-L | 执行环境保持多头 |
| 5m | UP / B95 / Trig 64237.7 | L-ZONE HMR95 | 回踩观察区形成并守住，不单独作为进场信号 |
| 1m | UP / B expired | TC-L | 从 FLAT 返回 UP，低周期再确认完成 |

### 当前可见指标

| 周期 | MACD / Signal / Histogram | RSI / MA |
| --- | --- | --- |
| 1H | 91.6 / 79.7 / +11.9 | 58.75 / 56.82 |
| 30m | 54.9 / 51.8 / +3.1 | 58.84 / 57.63 |
| 15m | 30.3 / 28.1 / +2.2 | 57.52 / 59.38 |
| 5m | 2.2 / 2.3 / -0.1 | 56.39 / 49.33 |
| 1m | 18.4 / 13.9 / +4.5 | 62.83 / 61.16 |

### 当前可见均线

- 1H：`63952.7 / 63912.5 / 63910.4 / 63724.0`。
- 30m：`64008.9 / 63909.8 / 63905.2 / 63902.8`。
- 15m：`64035.1 / 63977.9 / 63898.7 / 63894.3`。
- 5m：`64052.2 / 64033.6 / 64003.6 / 63937.8`。
- 1m：`64064.3 / 64053.5 / 64052.0 / 64041.9`。

### 新增状态路径

```text
Full MTF Bullish Alignment
→ 推进至 64180-64220
→ 1m 转 FLAT
→ 回踩 64000
→ 64000 支撑守住
→ 5m L-ZONE HMR95
→ 1m TC-L
→ 1m 返回 UP
→ 五周期多头对齐恢复
```

### 关键价位与执行

- 即时压力：`64130-64150`；第一压力：`64180-64220`。
- 5m Trigger 参考：`64237.7`；下一压力：`64300`；30m Trigger 参考：`64438.9`。
- 即时支撑：`64065-64040`；次级支撑：`64035-64000`。
- 核心支撑：`63980-63900`；趋势防守：`63780-63720`。
- 多头结构已确认，但当前位置接近压力，不追多；优先等待 `64065-64040` 或 `64035-64000` 回踩，且 1m 保持 UP 或再次出现 TC-L / PB-L。
- 突破多要求站稳 `64150` 并成功回测；空头在五周期均为 UP 时不成立。
- 空头至少需要跌破 `64000`、回测失败、1m 转 DN 并出现 TC-S / PB-S；进一步确认还需 5m 转 FLAT 或 DN。

### 分支结论

- Current Recovery Branch：`Outcome10Active / Strong Recovery / HTF Upgrade Confirmed`。
- Full MTF Bullish Alignment：`Confirmed`。
- First Pullback：`Held`。
- LTF Reconfirmation：`Completed`，信号为 `1m TC-L`。
- 主案例仍保持 `Outcome20Recorded / Review20 / Outcome50 / Unknown`，等待后续 Outcome50，不提前关闭。

## Current Recovery Branch Follow-up：64150 Breakout Attempt（2026-07-18 22:31 UTC+8）

### 数据完整性

- 22:30:59 与 22:31:05 两张截图相隔约 6 秒，作为同一市场快照使用。
- 当前价格约 `64159.9-64160.0`，读取自实时报价与右侧价格轴；历史十字光标 OHLC 不作为当前数据。
- 本次只记录突破尝试，不把盘中越过 64150 解释为已经收盘、站稳或回测确认。

### 当前多周期状态

| 周期 | Context / DVCA | 最新信号 | 当前解释 |
| --- | --- | --- | --- |
| 1H | UP / B95 / Trig 60758.3 | A-S HMR95 | 高周期保持 UP，Last 仍是历史反向警告 |
| 30m | UP / B100 / Trig 64438.9 | A-S HMR100 | 动能扩张，但 64438.9 仍是上方触发参考 |
| 15m | UP / B100 / Trig 64237.7 | L-ZONE HMR100 | 回踩观察区后恢复推进，尚未突破触发线 |
| 5m | UP / B95 / Trig 64237.7 | L-ZONE HMR95 | 首次回踩守住后的推进延续 |
| 1m | UP / B expired | TC-L | 低周期多头再确认仍有效 |

### 当前可见指标

| 周期 | MACD / Signal / Histogram | RSI / MA |
| --- | --- | --- |
| 1H | 96.8 / 80.8 / +16.1 | 61.16 / 56.99 |
| 30m | 63.6 / 54.8 / +8.8 | 62.52 / 58.26 |
| 15m | 42.2 / 32.9 / +9.2 | 62.52 / 60.59 |
| 5m | 23.8 / 13.6 / +10.2 | 63.03 / 54.08 |
| 1m | 14.5 / 12.8 / +1.7 | 66.83 / 57.39 |

### 当前可见均线

- 1H：`63959.0 / 63915.1 / 63911.7 / 63724.6`。
- 30m：`64028.8 / 63921.6 / 63908.9 / 63908.2`。
- 15m：`64059.9 / 63992.9 / 63909.5 / 63899.8`。
- 5m：`64088.5 / 64054.5 / 64018.0 / 63949.1`。
- 1m：`64121.6 / 64097.1 / 64080.5 / 64059.6`。

### 新增状态路径

```text
Full MTF UP
→ First Pullback Held
→ 5m L-ZONE HMR95
→ 15m L-ZONE HMR100
→ 1m TC-L
→ 5m / 15m / 30m 动能扩张
→ 价格交易至 64150 上方
→ 64150 Breakout Attempt
→ Breakout Confirmation Pending
```

### 突破分类

- 截图时价格位于 `64150` 上方。
- 尚未确认该周期收盘站稳、后续持续接受或成功回测。
- 因此只能记录为 `Breakout Attempt`，不能记录为 `Confirmed Breakout`。

### 关键价位

- 突破观察区：`64130-64160`。
- 即时压力：`64180-64220`。
- 5m / 15m Trigger：`64237.7`。
- 下一压力：`64280-64320`。
- 30m Trigger：`64438.9`。
- 即时支撑：`64120-64095`。
- 次级支撑：`64080-64055`。
- 核心支撑：`64030-64000`。
- HTF 均线支撑：`63960-63900`。
- 趋势防守：`63780-63720`。

### 执行计划

- 当前不追多，也不把突破尝试提前判定为正式突破。
- 优先多头观察：回测 `64120-64095` 守住，且 1m 保持 UP 或再次出现 TC-L / PB-L。
- 备选多头观察：突破 `64237.7` 后成功回测，再观察 `64300 / 64438.9`。
- 五周期仍为 UP 时不确认空头；假突破空头至少需要跌破 `64095`、回测 `64120-64150` 失败、1m 转 DN，并出现 TC-S / PB-S。

### 分支结论

- Current Recovery Branch：`Outcome10Active / Strong Recovery / HTF Upgrade Confirmed`。
- Full MTF Bullish Alignment：`Confirmed`。
- First Pullback：`Held`。
- LTF Reconfirmation：`Completed`。
- Current Event：`64150 Breakout Attempt`。
- Breakout Confirmation：`Pending`。
- 主案例仍保持 `Outcome20Recorded / Review20 / Outcome50 / Unknown`。

## 2026-07-19 15:10 Follow-up：HTF UP / LTF Pullback

### 数据完整性

- `15:10:33` 截图用于 1m / 5m / 15m，`15:10:39` 截图用于 30m / 1H。
- 实时报价为 Bid `64662.4`、Ask `64662.5`；历史十字光标 OHLC 不作为当前价格。
- `15:10:45` 截图只包含 SOL / ETH，未纳入本案例。

### 当前多周期状态

| 周期 | Context / DVCA | 最新信号 | 当前解释 |
| --- | --- | --- | --- |
| 1H | UP / B95 / Trig 60758.3 | A-S HMR95 | 高周期多头结构仍在，但 MACD 柱转负、动能减弱 |
| 30m | UP / B100 / Trig 64438.9 | A-S HMR95 | 已确认历史背离后的多头跟随，当前动能回落 |
| 15m | UP / B100 / Trig 64237.7 | L-ZONE HMR100 | 执行环境仍为 UP，回踩尚未升级为结构转空 |
| 5m | DN / S invalid | TC-S | 低周期回调已确认，尚无多头再进入信号 |
| 1m | DN / B invalid | TC-S | 短线空头回调持续，不能单独据此定义 HTF 反转 |

### 当前可见指标

| 周期 | MACD / Signal / Histogram | RSI / MA |
| --- | --- | --- |
| 1H | 184.8 / 204.6 / -19.8 | 64.81 / 72.12 |
| 30m | 69.1 / 101.1 / -32.1 | 55.70 / 64.25 |
| 15m | -0.9 / 7.1 / -8.0 | 46.52 / 49.59 |
| 5m | -7.2 / -3.5 / -3.7 | 42.48 / 48.33 |
| 1m | -7.5 / -5.5 / -1.9 | 32.24 / 41.29 |

### 当前可见均线

- 1H：`64536.7 / 64271.9 / 64117.7 / 63864.6`。
- 30m：`64660.7 / 64453.2 / 64254.6 / 64105.7`。
- 15m：`64699.3 / 64627.8 / 64446.8 / 64245.5`。
- 5m：`64689.2 / 64699.2 / 64680.6 / 64562.7`。
- 1m：`64681.0 / 64689.6 / 64694.1 / 64700.2`。

### 新增状态路径

```text
30m visual DIV-L false negative
-> bullish follow-through confirmed
-> reclaim 64078 / 64170 / 64438
-> extension toward 64800-64900
-> 5m S-ZONE / C-S
-> 1m and 5m TC-S
-> 1m and 5m changed to DN
-> LTF Pullback inside HTF UP
```

### 关键价位

- 即时压力：`64680-64700`；恢复确认参考：`64700-64730`；主要压力：`64800-64900`。
- 第一支撑：`64628-64560`；第二支撑：`64453-64438`；核心支撑：`64255-64238`。
- HTF 防守：`64170-64078`；深层防守约 `63865`。

### 执行与分支结论

- 1m 与 5m 同为 DN 时不执行多头；多头再进入至少需要 1m / 5m 返回 UP，并出现 TC-L 或 PB-L。
- 不在 `64628-64560` 支撑区直接追空；回调空头只有在支撑跌破并回测失败后才具备继续观察资格。
- 结构性空头升级需要跌破 `64238`、15m 转为 FLAT 或 DN，并且回收失败。
- Current Recovery Branch：`Outcome10Active / LTF Pullback inside HTF UP`。
- 30m 背离检测：`False Negative / Visual Divergence Confirmed / Bullish Follow-Through Confirmed / Regression Test Required`。
- 主案例保持 `Outcome20Recorded / Review20 / Outcome50 / Unknown`，不因本次分支观察提前关闭。

## 2026-07-19 20:52 Follow-up：15m Bearish Downgrade / 1m Countertrend Repair

### 数据边界

- 当前截图只包含 1m、5m、15m；实时报价 Bid `64400.7`、Ask `64400.8`。
- 30m 与 1H 未出现在当前截图中。其最后观察时间为 15:10，只保留为 `STALE / NOT CURRENT`，不参与当前多周期确认。
- 历史十字光标 OHLC 不作为当前 K 线数据。

### 当前可验证状态

| 周期 | Context / DVCA | 最新信号 | 当前解释 |
| --- | --- | --- | --- |
| 15m | DN / B expired | TC-S | 由此前状态降级为 DN，执行环境转空 |
| 5m | DN / S invalid | TC-S | 空头状态延续，但短线动能有所修复 |
| 1m | FLAT / B invalid | L-ZONE HMR100 | 约 64280-64300 反弹后的逆势修复，不是多头反转确认 |

### 当前可见指标

| 周期 | MACD / Signal / Histogram | RSI / MA |
| --- | --- | --- |
| 15m | -77.2 / -58.5 / -18.7 | 38.69 / 28.45 |
| 5m | -50.5 / -53.2 / +2.7 | 46.08 / 35.14 |
| 1m | +6.3 / +4.7 / +1.6 | 58.55 / 51.98 |

### 状态路径

```text
15m previous state
-> 15m DN / TC-S
-> 5m remains DN / TC-S
-> break 64520-64480 and 64453-64438
-> rebound from 64280-64300
-> 1m FLAT / L-ZONE HMR100
-> bearish context with countertrend repair
```

### 关键价位

- 压力：`64417-64480`、`64498-64507`、`64550-64580`、`64628`。
- 支撑：`64376-64365`、`64307-64280`、`64255-64238`、`64170-64078`、约 `63966`。

### 执行与分支结论

- 15m 与 5m 同为 DN 时不直接做多；1m FLAT 或 MACD 柱转正不构成反转确认。
- 优先空头观察：价格在 `64417-64507` 内受阻，随后 1m 转 DN，并出现 TC-S 或 PB-S。
- 延续空头观察：跌破 `64307` 后，回测 `64307-64365` 失败。
- 多头修复至少需要收复 `64480-64507`、1m 转 UP 并出现 TC-L；更高质量确认还要求 5m 脱离 DN 并收复 `64550-64580`。
- Current Recovery Branch：`Outcome10AtRisk / 15m FLAT-to-DN / 1m Countertrend Repair`。
- 30m 背离漏报案例保持 `False Negative / Bullish Follow-Through Confirmed / Regression Test Required`。
- 主案例仍保持 `Outcome20Recorded / Review20 / Outcome50 / Unknown`。
