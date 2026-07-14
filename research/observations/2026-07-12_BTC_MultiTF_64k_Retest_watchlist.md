# BTCUSDT Watchlist Observation：64k Retest Conflict

## 基本信息

- 日期：2026-07-12
- 截图时间：20:24（UTC+8）
- 标的：BTCUSDT
- 周期：15m / 5m / 1m
- 案例状态：Watchlist only
- 截图路径：`screenshots/BTCUSDT/2026-07-12/2026-07-12_BTCUSDT_MultiTF_64k_Retest_Conflict_watchlist.png`

## 多周期状态

- 15m：`FLAT`，修复进行中。
- 5m：`UP`，最新信号为 `TC-L`，前一个 `C-S` 已失效。
- 1m：`UP`，加速后出现 `S-ZONE / C-S`，当前为短线回调。

## 周期冲突

- 1m 出现空头警示。
- 5m 仍保持多头结构。
- 当前不将 1m `S-ZONE / C-S` 单独解释为 5m 反转，也不在压力区追多。

## 关键价位

- `64,110-64,170`：关键压力区。
- `64,000-63,980`：第一回测支撑与当前核心争夺区。
- `63,940-63,900`：下一层支撑区。

## 决策

- 不追价。
- 如果回测 `64,000-63,980` 后守住，等待回踩做多确认。
- 如果 5m 跌破关键结构，再按空头破位路径重新评估。

## 后续观察

- 下一复盘节点：价格回测 `64,000-63,980` 后的 Outcome10。
- 观察重点：5m 多头结构是否保持，1m 是否重新恢复 `TC-L`，或转为有效 `TC-S`。
- 当前只作为 Watchlist observation，不进入 `data/case_database.csv`，不计入 CASE-0009 的正式 Outcome。


## Outcome50 Upgrade

- 升级日期：2026-07-13 10:01（UTC+8）
- 已升级为正式案例：`CASE-0013`
- 最终分类：Failed Breakout / Bull Trap
- 结论：20:24 的跨周期冲突没有立即给出做空执行信号；22:54 的上破也不能直接视为 confirmed breakout。Outcome50 显示价格未能守住 `64150-64170`，随后跌破 `63900 / 63596`，15m / 5m / 1m 转为 `DN`，最新有效信号为 `TC-S`。
- 研究价值：用于完善 breakout confirmation filter：高周期收盘、持续 K 线、成功回踩、不能快速收回突破位下方，以及成交量/价格接受度延续。
