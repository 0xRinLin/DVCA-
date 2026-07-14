# DVCA 案例复盘：CASE-0014

## 基本信息
- 案例编号：CASE-0014
- 日期：2026-07-13
- 交易品种：SKYHYNIXUSDT
- 周期：MultiTF
- 方向：SHORT
- 主信号：TC-S / A-L HMR95-100
- 结果：Unknown

## Case Lifecycle
- 当前状态：Outcome20Recorded
- 下一步预期：Outcome50
- 生命周期状态：Review20

## 信号链
- 信号链：HTF consolidation near 1475→breakdown→loss 1405→loss 1355→waterfall to 1292→repeated TC-S→A-L HMR95/100 panel conflict
- 线段类型：HTFBreakdownCrashExtension

## 大周期背景
- 行情背景：Expansion→Climax / CrashDown

## EMA背景
- EMA背景：BelowEMA50

## 背离与VPA
- 背离代码：HMR
- VPA类型：HighVolumeWaterfall / VolumeClimaxRisk
- Zone分数：95-100 (A-L warning)

## 触发与确认
- 是否突破/跌破触发线：Yes
- 是否PB确认：No
- 是否出现TC：Yes
- 是否出现EXH：No

## Outcome10 / Outcome20 / Outcome50
- Outcome10：已达到 10 根K；结果待补充
- Outcome20：价格跌破1285，一度到达约1240，随后反弹至约1282。短线反弹确认，但15m仍为DN，L-ZONE HMR100且B invalid，未形成15m反转；1295-1305为下一确认区。
- Outcome50：Unknown

## 空间与回撤
- 最大顺向空间：约52点（1292至1240）
- 最大反向回撤：NA

## 截图路径
- screenshots/SKYHYNIXUSDT/2026-07-13/2026-07-13_SKYHYNIXUSDT_MultiTF_TC-S_CrashExtension_1109.png; screenshots/SKYHYNIXUSDT/2026-07-13/2026-07-13_SKYHYNIXUSDT_HTF_A-L_PanelConflict_1110.png; screenshots/SKYHYNIXUSDT/2026-07-13/2026-07-13_SKYHYNIXUSDT_MultiTF_Outcome20_Rebound_1718.png

## 复盘结论
Rating=Gold Case candidate。Case Type=HTF Breakdown / Crash Extension / Panel Signal Conflict。Capture A=2026-07-13 11:09 UTC+8，reported price≈1294.86；reported 15m/5m/1m 均为 DN，最新 TC-S，RSI 约 13/27/30.6。Capture B=2026-07-13 11:10 UTC+8，price≈1291.93；1H/30m/5m 均为 DN，1H RSI≈7.1，30m RSI≈9.8，5m RSI≈26.4。结构为高周期 1475 附近盘整→放量破位→失守 1405→失守 1355→瀑布下跌至 1292。1H Last=A-L HMR95、30m Last=A-L HMR100，与 DN Context 和价格崩跌形成面板冲突。TC-S 方向正确但当前阶段已过度延伸，禁止在 1292-1295 附近追空，也禁止仅凭 RSI 超卖做多；等待确认底部或反抽失败。优先观察 1306-1325，较理想反抽区 1360-1375。Next=新日内低点后的 Outcome10 / Outcome20 / Outcome50。

Review note: Outcome20：15m DN / L-ZONE HMR100 / B invalid；5m FLAT / TC-S / S85；1m UP / TC-L / B expired。高Pattern/HMR分数不等于高执行质量，等待1295-1305确认或Outcome50。

## Outcome20 市场状态

- Capture：2026-07-13 17:18 UTC+8。
- 价格：约 `1282.45`。
- 15m：`DN`，最新 `L-ZONE HMR100`，`B invalid`，RSI 约 `47.5`。
- 5m：`FLAT`，最新 `TC-S`，`S85`，RSI 约 `68`。
- 1m：`UP`，最新 `TC-L`，`B expired`，RSI 约 `76.5`。
- 路径：跌破 `1285` → 到达约 `1240` → 反弹至约 `1282`。
- 结论：1m 短线反弹成立，但 15m 仍未反转；`1295-1305` 是反弹能否升级的关键确认区。
- 执行：不因 `L-ZONE HMR100` 直接做多，也不在瀑布下跌后的低位追空。

## 截图证据边界

- 用户提供的初始 Capture A 状态文本覆盖 15m / 5m / 1m。
- 初始附带截图以 1H / 30m / 5m 为主，因此初始 15m / 1m 数值作为用户报告字段归档。
- Outcome20 附带截图可直接观察 15m / 5m / 1m 面板状态。

## 代码审计结论

- `A-L` 是 HTF 模式下的多头 Zone / 背离观察标签，不是 `LONG`。
- `HMR` 表示 MACD Histogram、MACD Line 和 RSI 三项均构成多头背离；`95 / 100` 是 Zone 评分，不是进场概率。
- HTF 模式下 `cleanBearCtx` 不生效，所以 `Ctx=DN` 中仍可生成高分 `A-L`，当前没有 HTF 趋势罚分。
- HUD `Last` 只是单一 `lastSignal` 字符串，新事件按代码执行顺序覆盖旧值，没有趋势信号与反趋势警告的独立优先级通道。
- 显示开关只控制标签、线和 HUD 绘制，不参与 `lastSignal`、Zone、TC 或 Entry 触发条件。
- `TC-S` 当前没有 Early / Mature / Extended 阶段分类，也没有距离 EMA/ATR 上限、RSI 极值下限、连续扩张 K 线、破位后经过 K 线数或成交量高潮风险过滤。

## 开发任务归档

- 将 `Trend Signal` 与 `Countertrend Warning` 分开显示和保存。
- 对 HTF `Ctx=DN` 中的 `A-L` 引入趋势罚分或警告降级。
- 为 `TC-S` 增加 Early / Mature / Extended 阶段判定。
- 引入 `Pattern Score`、`Context Alignment`、`Location Score`、`Execution Score`、`Extension Status` 与 `No-Chase Flag` 作为 v1.5.5 研究候选字段。
- 以案例统计验证后再决定是否实装，不回填修改 v1.5.1。
