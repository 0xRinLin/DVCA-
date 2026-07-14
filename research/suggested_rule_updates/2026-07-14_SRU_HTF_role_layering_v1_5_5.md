# Suggested Rule Update：HTF Role Layering for v1.5.5

## 基本信息

- 日期：2026-07-14
- 状态：Pending Evidence
- 最少案例要求：30 个相关案例
- 当前证据状态：观察支持，但统计不足
- 禁止动作：不得直接修改 Pine、Signal Manual、Line Patterns。

## 建议更新方向

不要通过整体放宽阈值解决 30min / 1H 信号少的问题。

建议将高周期职责改为：

```text
1H = 背景状态 / 风险区 / 方向许可
30min = 结构确认 / 转折候选 / 趋势延续空间
15min / 5min = LONG / SHORT / PB 执行确认
1min = 精细入场和止损管理
```

## 候选规则

### SRU-HTF-01：1H 背景优先

1H 默认输出背景状态，不追求频繁 LONG / SHORT。

候选输出：

- BULL
- BEAR
- RANGE
- TRANSITION
- Zone Watch
- Zone Valid
- Risk State

### SRU-HTF-02：30min 结构优先

30min 优先确认结构转折、FT / PB 候选、失效位和趋势延续空间。

### SRU-HTF-03：三时间字段

每个结构 / 信号记录：

- `originBar`
- `confirmedBar`
- `executableBar`

统计时使用 `executableBar`。

### SRU-HTF-04：候选状态链

新增内部状态链：

```text
WATCH -> CANDIDATE -> CONFIRMED -> EXECUTABLE -> INVALID / EXPIRED
```

候选状态不等同于入场信号。

### SRU-HTF-05：周期自适应参数

至少分成三组参数：

- 1min / 5min：执行参数
- 15min / 30min：结构参数
- 1H 及以上：背景参数

需要验证的项目：

- Pivot 确认长度
- Zone 有效期
- PB 等待窗口
- 成交量阈值
- ATR 距离
- 冷却时间
- 趋势确认强度

## 暂不允许的修改

- 不直接降低阈值。
- 不直接缩短所有周期 Pivot 参数。
- 不直接增加 1H LONG / SHORT 标签。
- 不把候选状态画成执行标签。
- 不用单一标的结果代表 BTC / ETH / SOL 全部市场。

## 进入正式规则更新的条件

满足以下条件后才可从 Suggested Rule Update 升级为正式规则：

1. 至少 30 个相关案例。
2. 覆盖 BTC、ETH、SOL。
3. 覆盖 30min 和 1H。
4. 统计 originBar / confirmedBar / executableBar 延迟。
5. 证明 1H 背景覆盖率改善而 RANGE 噪音没有显著上升。
6. 证明 30min 结构确认延迟减少至少 1 根 K 线。
7. 图面密度不高于 v1.5.4 明显水平。

## 当前处理

保持 Pending，不直接进入代码。


## Evidence Update：CASE-0015 HTF Breakout Study

- 日期：2026-07-14 20:48 UTC+8
- 案例：`CASE-0015`
- 类型：Gold Case / Outcome50PendingHTFClose

### 观察

15m 与 30m 已经转为 UP 并出现突破延伸，但 1H 仍显示 FLAT，同时 Last 仍为 `A-S HMR100`。价格已经收复主要均线，说明当前状态可能不是空头延续，而是 recovery state 尚未在 HTF close 前被正式确认。

### 对 SRU 的支持

该案例支持以下候选规则继续观察：

1. HTF 需要 `RECOVERY-L` / `UP-PENDING` 中间状态。
2. `A-S HMR100` 不应覆盖 recovery state。
3. HMR100 Pattern Score 不能直接转译为执行方向。
4. HTF 状态评估必须区分当前 K 线未收盘与已收盘。
5. 执行层应输出 No Chase，而不是在极端延伸位置追多。

### 状态

仍为 Pending Evidence，等待更多案例和 CASE-0015 Outcome50。

## Evidence Update：CASE-0015 Pullback Role Classification

- 日期：2026-07-14 22:02-22:05 UTC+8
- 案例：`CASE-0015`
- 状态：`Outcome50DeepPullback / HTFResolutionPending`

### 观察

价格在 64000 附近受阻后，1m 先从 `UP` 转为 `FLAT`，随后跌破 63800 与 63600 并转为 `DN / TC-S`。同期 15m / 5m 仍为 `UP / TC-L`，说明相同的 `TC-S` 在不同 HTF 背景下承担不同角色。

### 候选角色分类

```text
LTF TC-S + HTF UP = PULLBACK-S
LTF TC-S + HTF DN = TREND-S
```

候选显示字段：

```text
HTF Trend
LTF Phase
LTF State
Execution
```

在 22:02 的状态中，建议显示：

```text
HTF Trend: UP
LTF Phase: PULLBACK
LTF State: FLAT
Execution: WAIT
```

### 边界

- `PULLBACK-S / TREND-S` 是 v1.5.5 研究候选分类，不是 DVCA v1.5.1 的现有标签。
- 不改变 `TC-S` 的代码触发逻辑，只建议增加 HTF 角色解释层。
- 当前证据只有单个 Gold Case，仍不足以进入正式规则或 Pine 实现。

## Outcome50 Validation：Pullback Recovery / HTF State Lag

- 日期：2026-07-14 22:18 UTC+8
- 案例：`CASE-0015`
- 标签：`MTF_PULLBACK_RECOVERY`、`HTF_STATE_LAG`

### 验证结果

```text
HTF UP
→ LTF FLAT
→ LTF DN / TC-S
→ support held near 63550
→ no loss of 63300 / 63250
→ reclaim Trigger near 63787
→ LTF UP
→ LATE-L HR85
```

该路径支持：HTF 为 `UP` 时，LTF `TC-S` 应先解释为 `PULLBACK-S`。只有 HTF 同步转 `DN`，才升级为 `TREND-S`。

### HTF 状态滞后证据

- 30m 已为 `UP / A-L HMR100 / B100`。
- 15m / 5m 均为 `UP / TC-L`。
- 1H 价格已在主要均线上方、RSI 约 68.6，但仍为 `FLAT / A-S HMR100 / B95`。

因此继续建议增加：

```text
FLAT → RECOVERY-L → UP-PENDING → UP-CONFIRMED
```

### LATE-L 执行边界

- 本例 `LATE-L HR85` 的方向正确。
- Trigger 收复已经先发生，`LATE-L` 后出现，执行确认存在延迟。
- 这支持保留 `LATE-L` 为补确认 / 复盘标签，不将其升级为追单授权。

### 状态

本条由 Pending Observation 升级为 Single Gold Case Validation；仍需达到最少案例门槛后，才能修改 Pine。

## Post-Close Validation：Breakout Retest / HTF Transition

- 日期：2026-07-14 22:58-23:07 UTC+8
- 案例：`CASE-0015`
- 状态：`BreakoutRetestActive / NoChase`

### 观察

- 22:58：15m 为 `UP / TC-L`；5m 与 1m 为 `UP / L-ZONE HMR95`，Trigger 分别约 64086 与 64010。
- 价格完成 Pullback Recovery 后重新测试 64000，但尚处在 64100-64250 压力区附近。
- 23:07：30m 与 1H HUD 均显示 `Ctx=UP`，价格约 64177。

### 对候选状态链的支持

```text
FLAT
→ RECOVERY-L
→ UP-PENDING
→ UP-CONFIRMED
```

本次后续图说明此前的 1H `FLAT` 可以被视为恢复与确认之间的过渡状态候选，而不是永久停留状态。

### 执行边界

- `Ctx=UP` 解决方向确认问题，不自动解决高位执行质量问题。
- 5m / 1m `L-ZONE HMR95` 是观察区，不是正式 `LONG`。
- 突破测试阶段仍应输出 `NoChase`，等待 64010-64090 的有效接受或 63920-63850 回踩确认。
