# BTC 30m 常规多头背离漏报观察

## 记录信息

- 日期：2026-07-19
- 时间：12:22 UTC+8
- 标的：BTCUSDT.P（Binance）
- 主观察周期：30m
- 辅助周期：1H
- 截图指标版本：DVCA 1.5.1
- 当前正式基线：DVCA v1.5.4
- 问题分类：`False Negative / NeedsCodeTrace`
- 专项准入状态：`ExcludedPendingReproduction`
- 截图：`screenshots/BTCUSDT/2026-07-19/2026-07-19_BTCUSDT_30m_DIV-L_false-negative_1222.png`
- 截图 SHA-256：`c28e89d5a090430f16ff488af6d4fce56d1a38ab0173773315512f1960d607ca`

## 问题陈述

30m 图中可人工识别出常规多头背离，但 DVCA 1.5.1 没有打印对应背离事件。人工观察到的结构为：

- 价格 Pivot A 到 Pivot C 形成更低低点（Lower Low）。
- MACD 对应低点形成更高低点（Higher Low）。
- MACD 空头柱在转正前持续收缩。
- 随后价格以放量方式重新站上均线组。

因此，本截图将“视觉常规多头背离存在、指标未打印事件”记录为历史版本漏报样本。它不证明 v1.5.4 存在相同缺陷，也不证明具体根因已经确认。

## 当前根因假设

优先假设是多低点簇中的 Pivot 配对不正确：引擎可能只比较最近的相邻微型 Pivot，没有回看最后一个具有结构意义的有效 Pivot。

仍需排查的替代原因：

1. 价格 Pivot 与振荡器 Pivot 必须同柱，缺少可配置的位移容差。
2. `minBars`、`maxBars`、价格差值或振荡器差值阈值未通过。
3. 背离事件已被检测，但被趋势或 Context 交易门控直接抑制。
4. 右侧 Pivot 确认后没有按确认偏移回填事件标记。
5. 显示逻辑或事件优先级覆盖了已检测的背离。

## 必须增加的诊断记录

后续候选版本只在获得明确开发授权后实现；诊断至少应输出：

1. 每一个已确认价格 Pivot Low 的 bar index、价格和确认时间。
2. 每个价格 Pivot bar 上采样的 MACD 值。
3. 独立检测到的每一个 MACD Pivot Low。
4. 价格 Pivot 与振荡器 Pivot 的 bar displacement，以及配置的容差结果。
5. 当前 Pivot 与多个历史有效 Pivot 的逐一比较结果，而非只比较一个前点。
6. `minBars`、`maxBars`、`priceDelta`、`oscillatorDelta` 和各阈值是否通过。
7. 每一个被拒绝背离的精确 suppression reason。
8. 背离检测结果与趋势、Context、结构和执行门控的独立状态。
9. Pivot 右侧确认时间、事件归属 bar 和回填偏移。
10. 显示开关开启或关闭时，底层检测状态是否完全一致。

## 期望事件语义

- `DIV-L-WARN`：候选或已检测的常规多头背离观察事件，不代表进场。
- `DIV-L-CONFIRMED`：右侧 Pivot 完成确认后的背离事件，可按已确认 Pivot bar 回填。
- `LONG`：只有后续结构触发和执行条件成立时才能出现；不得由背离事件自动生成。
- 当 Context 阻止交易时，应保留 `DIV-L-WARN` 或 `DIV-L-CONFIRMED`，只压制执行资格，不应删除研究事件。

## v1.5.4 复现与验收标准

1. 使用 `indicator/current/dvca_v1_5_4.pine` 在同一历史区间复现，并固定交易所、标的、周期和时区。
2. 导出全部价格 Pivot、MACD 采样点、独立 MACD Pivot 和候选配对。
3. 确认人工标记的 Pivot A/C 是否属于当前代码允许的有效 Pivot。
4. 若配对被拒绝，必须得到唯一、可读且可复查的拒绝原因。
5. 若背离成立，候选阶段显示 `DIV-L-WARN`，右侧确认后显示 `DIV-L-CONFIRMED`。
6. Context 或趋势门控只能改变执行评分和 LONG 资格，不能抹除背离事件。
7. 回填只发生在已确认右侧 Pivot 后，并明确标注确认延迟，避免被解释为实时无延迟信号。
8. 隐藏标签或切换显示选项不得改变 Pivot、候选、确认、失效或拒绝状态。
9. 同一低点簇不得重复打印等价事件，也不得通过无限回看制造事后最优配对。
10. 完成 BTC、ETH、SOL 的多低点簇样本验证后，才允许形成 v1.5.5 修改提案。

## 当前结论

该截图是 DVCA 1.5.1 的高价值背离漏报观察，支持建立独立的 Divergence Detection Accuracy 专项。当前只确认“视觉事件与指标输出不一致”，根因仍为待验证假设；不修改正式 Pine，不自动生成 LONG，也不计入 v1.5.4 正式样本或交易案例胜率。
