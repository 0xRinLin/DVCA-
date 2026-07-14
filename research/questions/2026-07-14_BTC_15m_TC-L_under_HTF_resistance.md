# BTC 15m TC-L 能否突破 HTF 压力并升级为反转？

## 基本信息

- 日期：2026-07-14
- 品种：BTCUSDT.P / Binance
- 指标：DVCA 1.5.1
- 关联案例：`CASE-0015`
- 关联主题：`research/questions/2026-07-14_DVCA_HTF_execution_signal_lag.md`
- 状态：Outcome20Recorded / Outcome50PendingHTFConfirmation
- 改进标签：CounterTrendSignalDowngrade

## 问题

15m `L-ZONE → TC-L` 能否升级为确认反转，还是会在 30m / 1H 压力下失败？

## 当前证据

| 周期 | DVCA 状态 | 复盘含义 |
| --- | --- | --- |
| 1H | `Ctx=DN`, `Last=A-S HMR100` | 高周期偏空，对低周期多头执行构成降级条件 |
| 30m | `Ctx=FLAT`, `Last=A-L HMR100` | 出现修复 / 多头 Zone 观察，但未建立稳定多头背景 |
| 15m | `Ctx=UP`, `Last=TC-L` | 低位 L-ZONE 后的多头延续，但不是正式 LONG |
| 5m | `Ctx=UP`, `S-ZONE HMR100` visible | 反弹延续中已出现短周期压力观察 |
| 1m | TC-L / short-term mixed events | 只用于观察节奏，不覆盖 HTF 背景 |

## 代码语义边界

- `A-S / A-L` 是 HTF Zone 名称，不是严格 `SHORT / LONG`。
- `TC-L` 是趋势延续信号，不是背离反转信号。
- 因此本问题不统计“标签方向是否看对”，而是统计“15m TC-L 在 HTF 冲突中是否升级为可执行反转”。

## 当前假设

```text
Pattern 可以保留
→ Context Alignment 为 Countertrend / Conflict
→ Execution Score 降级
→ 未出现 LONG / PB-L 前保持 NoTrade
```

当 1H 仍为 `DN`、30m 只是 `FLAT`时，15m `TC-L` 应被视为高价值观察信号，但交易执行评级应降级。

## 验证计划

1. 从 2026-07-14 19:23-19:27 UTC+8 后开始，按 15m 周期记录 Outcome10。
2. 记录 30m 是否从 `FLAT` 转向稳定 `UP`。
3. 记录 15m 是否出现正式 `LONG / PB-L`，而不只是继续出现 `TC-L`。
4. 记录价格是否突破、接受并成功回踩 30m / 1H 压力。
5. 如反弹失败，记录首个可识别的 15m 转弱事件与确认延迟。

## Outcome10 分类候选

- `ConfirmedReversal`：30m 背景升级，15m 出现正式多头确认，突破后能保持结构。
- `CounterTrendBounceFailed`：15m TC-L 无法突破 HTF 压力，并重新出现空头确认。
- `NoTradeConflictPersists`：10 根 15m K 后仍为高低周期冲突，无可执行确认。

## 当前结论

- 案例状态：Outcome10Recorded。
- Outcome10：1m 临时转 DN 后支撑守住，重新收复 62800 并恢复 `UP / TC-L`；随后放量突破 62920 和 63000。
- Finding：`S-ZONE` 的局部延伸警告有效，但没有结构跟随的趋势空已失效；结构收复后的 `TC-L` 是更可靠的延续确认。
- 执行状态：Outcome20Active / NoChase_WaitRetest。
- 优先观察：62920-62850 回测；持续运行在 62800 下方视为失效。
- 下一步：Outcome20。
- 本文只建立研究假设与验证标准，不修改 Pine、Signal Manual 或 Line Patterns。


## Outcome20 / HTF Breakout Study（2026-07-14 20:48 UTC+8）

- 关联案例：`CASE-0015`。
- 价格：约 `63780`。
- 15m：Context UP，Latest TC-L，RSI 约 84.9，极端延伸。
- 30m：Context UP，Latest A-L HMR100，B score 100，RSI 约 80，突破确认但过度延伸。
- 1H：Context FLAT，Latest A-S HMR100，B score 95，RSI 约 70，价格已收复主要均线，但当前 K 线可能仍未收盘。

### 新增审计问题

1. 1H 是否在收盘后转为 UP？
2. `FLAT` 是否是合理的收盘确认延迟，而不是状态错误？
3. `A-S HMR100` 是否错误覆盖 recovery state？
4. HTF 是否应显示 `UP-PENDING` 作为中间状态？
5. 反趋势 `HMR100` 是否容易误导执行？

### 候选状态链

```text
FLAT -> RECOVERY-L -> UP-PENDING -> UP-CONFIRMED
```

### 当前执行结论

不追 `63780`，已有多单管理利润，等待 `63500-63300`、`63250-63000`、`62900-62700` 回踩区。

### 研究评级

升级为 Gold Case。Outcome50 需要等待 HTF close 后确认。

## 21:00 High-Level Extension

- 价格突破 `63000 / 63250`后放量加速，在 `63500` 上方得到接受并测试 `63800`。
- 15m / 5m 仍为 `UP / TC-L`，但 RSI 约 `79.4 / 75.8`，进入强势但过度延伸阶段。
- 1m 仍为 `UP`，最新 `S-ZONE HMR100 / S invalid`，RSI 约 `70.6`，MACD Histogram 转负，只确认短线动能减速。
- 当前不追多，也不在多头结构未破坏时仅凭 1m 警告做空。
- 下一步：等待 21:00 的 1H K 线收盘后确认 HTF 状态，再记录 Outcome50。
