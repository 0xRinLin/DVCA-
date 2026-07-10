# 为什么 BTC 在趋势行情中 TC-L 远多于 LONG？

## 基本信息

- 日期：2026-07-07
- 品种：BTCUSDT
- 相关周期：5m / 15m / 30m
- 当前状态：Open
- 问题类型：TrendContinuation vs Reversal Entry

## 问题

为什么 BTC 在趋势行情中 TC-L 远多于 LONG？

今天的 DVCA Daily Review 中，多张 BTC 图都显示出 TC 类型的趋势延续结构，但并没有同等数量的 LONG。这个现象需要单独研究，不能直接解释为指标缺陷，也不能马上修改 DVCA 参数。

## 当前假设

- LONG 属于 Reversal Entry。
- TC-L 属于 Trend Continuation。
- BTC 在趋势行情中，价格更常沿 EMA20 / EMA50 延续，形成回踩后突破短高的 TC-L。
- LONG 需要先出现 L-ZONE，再突破结构触发线，并通过严格进场过滤，因此天然比 TC-L 少。
- 如果 BTC 趋势段回踩浅、Pivot 背离少，或者没有足够的 VPA / Zone 分数，LONG 的出现频率会低于 TC-L。

## 验证计划

至少收集 100 个 BTC 案例，覆盖：

- BTCUSDT 5m
- BTCUSDT 15m
- BTCUSDT 30m

统计内容：

- TC-L 出现频率。
- LONG 出现频率。
- TC-L 成功率。
- LONG 成功率。
- TC-L 对应的大周期状态。
- LONG 对应的大周期状态。
- TC-L 出现时的 EMA 背景。
- LONG 出现前是否有 L-ZONE、C-L、E-L 或 LATE-L。
- BTC 趋势行情中是否经常出现 TC-L 但没有 L-ZONE。

## 当前关联案例

- `CASE-0003`：BTC_TrendRecovery_TC-L，Candidate。
- `CASE-0004`：BTC_Gold_TC-L，Gold。
- `CASE-0005`：BTC_LateTrend_TC-L，Candidate。
- `CASE-0006`：BTC_HTF_Trend_LTF_TC，Gold。

## 当前不下结论的原因

目前只有少量 Daily Review 图，样本不足。需要等 after 图确认结果，并继续收集足够多的 BTC 5m、15m、30m 案例。

## 后续动作

1. 保存每个 TC-L 的 before / after 截图。
2. 每个完整或失败案例进入 `data/case_database.csv`。
3. Gold 案例同步到 `gold_cases/BTC/TC/`。
4. 达到 100 个样本后，在 `research/findings/` 写阶段性发现。
5. 再决定是否需要在 DVCA 2.0 中调整 Reversal Entry 与 Trend Entry 的关系。

