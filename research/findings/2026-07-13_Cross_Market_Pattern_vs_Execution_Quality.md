# Cross-Market Finding：Pattern Score 不等于 Execution Quality

## 基本信息

- 日期：2026-07-13
- 截图时间：17:18 UTC+8
- 关联案例：`CASE-0014` SKYHYNIXUSDT，`CASE-0013` BTCUSDT
- 研究状态：Finding Recorded
- 代码边界：本文只记录 v1.5.5 候选字段，不修改 DVCA v1.5.1 Pine 代码。

## 跨市场证据

### SKYHYNIXUSDT

```text
HTF 破位 / Crash Extension
→ 跌破 1285
→ 到达约 1240
→ 反弹至约 1282
→ 15m 仍 DN，L-ZONE HMR100 / B invalid
→ 1m UP / TC-L，但尚未升级为 15m 反转
```

`L-ZONE HMR100` 描述的是当前代码中的高分背离 / Zone 模式，不是做多执行质量 100，也不是成功率 100%。价格位于 Crash 后的反弹阶段，必须单独评估高周期趋势、所处位置和执行条件。

### BTCUSDT

```text
64150-64170 突破失败
→ 15m / 5m / 1m 转 DN
→ 重复 TC-S
→ 跌破 63000
→ 62600-62700 附近暂时稳定
→ 1m 出现 S-ZONE HMR85
```

BTC 的空头方向仍正确，但下跌已有明显位移。此时新出现的高分空头 Pattern 并不自动等于高质量市价追空机会。

## 共享结论

> 高 Pattern / HMR 分数只能评价模式本身，不能独立代表实际下单质量。

反趋势 `L-ZONE` 和趋势后段 `S-ZONE / TC-S` 都需要加入位置与延伸罚分。研究中必须区分：

1. 这个形态是否符合代码条件。
2. 它是否与当前趋势背景一致。
3. 它出现的位置是早期、中段还是过度延伸后。
4. 当前是否具备可执行的触发、风险和盈亏比条件。

## DVCA v1.5.5 候选字段

### Pattern Score

- 用途：保留当前 Zone / 背离 / 结构模式的原始质量评分。
- 边界：不得解释为成功率或执行授权。

### Context Alignment

- 用途：表示信号与 HTF / 当前 `Ctx` 的方向是否一致。
- 建议状态：`Aligned / Neutral / Countertrend / Conflict`。

### Location Score

- 用途：评估信号相对 EMA、Keltner、Donchian、触发线、支撑压力与 ATR 位移的位置。
- 罚分：过度远离均线、已连续扩张、靠近成交量高潮或进入反向支撑/压力。

### Execution Score

- 用途：在 Pattern、Context、Location、Trigger、Risk / Reward 和 Extension 评估之后，给出独立执行质量。
- 原则：不得直接复制 Pattern Score。

### Extension Status

- 建议状态：`Early / Mature / Extended / Climax`。
- 候选因子：EMA / ATR 距离、RSI 极值、连续扩张 K 线、破位后经过 K 线数、成交量高潮。

### No-Chase Flag

- 用途：在方向判断仍有效，但新开市价单的位置和风险已不合格时，明确输出 `true`。
- 不改变：不否定原趋势方向，只禁止追价执行。

## 当前执行结论

- SKY：短线反弹已出现，但未经 `1295-1305` 确认前，不定义为15m反转。
- BTC：空头延伸有效，但不把下跌后段的高分 `S-ZONE` 解释为新的追空授权。
- 两个市场都继续使用“方向判断”与“执行质量”分离的复盘方法。
