# SKYHYNIXUSDT Finding：A-L、HUD Last 与 TC-S Extended 审计

## 基本信息

- 日期：2026-07-13
- 品种：SKYHYNIXUSDT
- 周期：1H / 30m / 15m / 5m / 1m
- 关联案例：`CASE-0014`
- 当前状态：InReview
- 证据：DVCA v1.5.1 Pine 源码与 2026-07-13 两张 SKYHYNIXUSDT 截图

## 事件摘要

```text
HTF consolidation near 1475
→ high-volume breakdown
→ loss of 1405
→ loss of 1355
→ waterfall decline to 1292
→ repeated TC-S
→ 1H / 30m Last displays A-L HMR95 / HMR100 while Ctx remains DN
```

`TC-S` 对下跌方向的识别正确，但价格在大幅 ATR 位移后已进入延伸阶段。此时“方向正确”不等于“仍可新开市价空单”。

## Finding 1：A-L 的精确代码语义

`A-L` 不是独立的进场触发器。它是多头 Pivot Zone 通过 HTF 有效参数后，HUD 对该 Zone 使用的名称：

- Auto 模式下，30m 及以上进入 `isHTFMode`。
- HTF 默认使用 Pivot Left/Right `5/5`、最小间隔 `18`、最大间隔 `260`、最低分 `90`、冷却 `96`根 K。
- `HMR` 由 `f_code()` 生成，表示 Histogram、MACD Line、RSI 三项背离均成立。
- `95 / 100` 是背离数量、VPA、关键位、新低及 Major Bottom 等项目相加后的 Zone 评分，不是成功率或下单分数。
- Zone 成立时会设置 `bullActive=true`，HTF HUD 显示 `Act=B score`。
- `LONG / E-L / PB-L / TC-L` 的执行状态机均限制在 `isLTFMode`，因此 HTF `A-L` 本身不会直接发出正式 `LONG`。

## Finding 2：HTF 反趋势过滤缺口

多头 Zone 的空头背景过滤由以下条件开启：

```text
cleanBearCtx = isLTFMode and useTrendAwareFilter and ctxDown
```

因为条件明确要求 `isLTFMode`，HTF 模式下 `cleanBearCtx` 恒为 false。这意味着：

- 1H / 30m `Ctx=DN` 时，HTF `A-L` 不受 `counterTrendNeedsMajor` 的反趋势限制。
- 当前没有“HTF 趋势罚分”或“Crash 中禁止高分反向执行解读”。
- SKYHYNIX 截图中 `Ctx=DN` 与 `Last=A-L HMR95/100` 并存，符合当前代码，不是面板计算崩溃；问题在于语义未分层，容易被误读为做多授权。

## Finding 3：Last 是事件覆盖，不是当前优先级结论

`lastSignal` 是全局单一字符串。Zone、EXH、LONG/SHORT、E-L/E-S、PB 和 TC 在各自触发时直接对其赋值。

- 同一根 K 线上如果有多个事件，后执行的代码覆盖先执行的值。
- HUD `Last` 只显示这个字符串，没有分开 `Trend Signal`、`Countertrend Warning` 和 `Execution State`。
- HTF 不执行 LTF Entry / PB / TC 状态机，因此最近一次 HTF `A-L` 可以持续显示为 Last，即使当前价格仍在崩跌。

结论：`Last=A-L` 只能读为“最近记录的 HTF 多头 Zone 事件”，不能读为“当前首选交易方向”。

## Finding 4：超卖与反向执行边界

- A-L 评分不使用 RSI 绝对超卖阈值；RSI 只是通过 Pivot 背离参与 `HMR` 组合。
- HTF `A-L` 不是可执行 LONG，因此 RSI 7-10 与 A-L 同时出现不构成代码层的正式买入授权。
- LTF 正式 LONG 仍需要 Trigger 突破、量能、EMA20 恢复、动能、风险和可选 RR 条件。
- 但在强空背景中，`bullScore >= majorScore` 可以使 `ctxOk` 通过。因此 2.0 仍需要对 Crash / Extended 背景增加更明确的反趋势执行限制。

## Finding 5：显示开关不改变信号优先级

`showZoneSignal`、`showConfirmSignal`、`showEntrySignal`、`showTCSignal`、`showExhSignal` 等开关只出现在 `plotshape()` 或绘图语句。`hudMode` 只决定 table 是否显示。

代码级结论：

- 关闭某类标签不会阻止该信号的状态计算。
- 显示开关不会改变 `lastSignal` 赋值顺序。
- `showStructureLine` / `showDivLine` 仅控制 line 对象创建，不改变 Zone 是否成立。

## Finding 6：TC-S 没有阶段分类

当前 `TC-S` 要求：

- `Ctx=DN`，EMA20 < EMA50，价格在 EMA50 下方。
- 回看区间内曾反抽接近 EMA20。
- 收盘跌破短期低点加 buffer。
- MACD Histogram 继续走弱，RSI < 50 且继续下降。
- 量能达到均量倍数与冷却条件。

但当前不检查：

- 当前价格距离 EMA20 / EMA50 的最大 ATR 位移。
- RSI 是否已处于极端超卖。
- 连续空头扩张 K 线数。
- 自结构破位起已经过的 K 线数。
- 成交量高潮或抛售衰竭风险。

因此该案例支持新增 TC-S Phase：`Early / Mature / Extended`。`Extended` 应只保留方向警示，降级或禁止新市价追空授权。

## DVCA 2.0 候选改进

1. 分离 `Trend Signal`、`Countertrend Warning`、`Execution State`。
2. 新增 `EXTENDED / CRASH / NO CHASE` 状态。
3. 对 HTF DN 中的 A-L 和 HTF UP 中的 A-S 施加趋势罚分或强制降级。
4. 将 RSI 极值、EMA/ATR 位移、连续扩张 K、破位后时间和 Volume Climax 纳入 TC Phase。
5. `Last` 分解为至少三个字段：`Trend Last`、`Warning Last`、`Execution Last`。
6. 为显示开关建立回归测试，验证不同显示组合下的原始信号序列一致。

## 执行结论

- 不在 `1292-1295` 附近追空。
- 不因 RSI 超卖或 `A-L HMR95/100` 单独做多。
- 等待底部确认，或等待 `1306-1325`、更理想的 `1360-1375` 反抽失败后再评估顺势空。
- Outcome10 / Outcome20 / Outcome50 从新日内低点开始记录。

## Outcome20 更新

- 2026-07-13 17:18 UTC+8，价格跌破 `1285`后到达约 `1240`，再反弹至约 `1282`。
- 1m 已转 `UP / TC-L`，但 15m 仍为 `DN / L-ZONE HMR100 / B invalid`，因此只确认短线反弹，不确认 15m 反转。
- `1295-1305` 是下一个反弹升级确认区。
- 跨市场比较见 `research/findings/2026-07-13_Cross_Market_Pattern_vs_Execution_Quality.md`。
