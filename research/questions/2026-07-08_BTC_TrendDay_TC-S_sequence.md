# BTC Trend Day 中 TC-S 会连续出现几次？

## 基本信息

- 日期：2026-07-08
- 品种：BTCUSDT
- 相关周期：15m / 5m / 1m
- 当前状态：Open
- 问题类型：TrendContinuation / Trend Day / Discipline

## 问题

BTC 在 Trend Down 行情中，TC-S 是否会连续出现，并形成一路下跌的趋势延续结构？

进一步的问题是：当 15m 与 5m 都处于 `Ctx=DN`，但 1m 出现 MACD 动能缓和时，是否应该仍然避免逆势抄底？

## 当前观察

7-8 Daily Review 图中：

- 15m 最近有效信号为 `TC-S`。
- 15m HUD 显示 `Ctx=DN`。
- 5m 同样处于空头背景。
- 1m 出现动能缓和和小反弹，但没有 `L-ZONE`、`LONG` 或 `PB-L`。
- 当前状态更接近 `TrendContinuation`，不是 `Reversal`。

## 当前假设

- BTC Trend Day 中，TC-S 可能会连续出现。
- 1m 动能修复只是 Momentum Recovery，不等于 Trend Reversal。
- 高周期 15m 和执行周期 5m 同为 Down Context 时，不应因为 1m 短线止跌就做多。
- 更合理的执行方式是等待 5m 反抽 EMA20 后，再观察是否出现新的 `TC-S` 或 `PB-S`。

## 验证计划

至少收集：

- BTCUSDT 15m / 5m / 1m 多周期 TC-S 案例 30 个。
- 其中 15m 与 5m 同时 `Ctx=DN` 的案例至少 20 个。
- 记录 1m 是否出现 MACD 修复。
- 统计 1m 修复后是否真正形成 `L-ZONE→LONG`，还是继续下跌。
- 统计等待 5m 反抽后 TC-S / PB-S 的成功率。

## 当前关联案例

- `CASE-0009`：7-8 BTC MultiTF TC-S Trend Day，不逆势抄底案例。

## 可能的结论方向

如果样本支持该假设，后续 Playbook 可以加入：

```text
15m Ctx=DN + 5m Ctx=DN
且 1m 只有 MACD 修复、没有 L-ZONE/LONG/PB-L
=> 不定义为反转，不做多。
=> 等待 5m 反抽 EMA20 后的 TC-S / PB-S。
```

## 后续动作

1. 等待 `CASE-0009` 后续 20 / 50 根 K 线结果。
2. 补充 after 截图。
3. 更新 `case_database.csv` 中的结果字段。
4. 累积足够样本后，在 `research/findings/` 总结 Trend Day TC-S 规律。

