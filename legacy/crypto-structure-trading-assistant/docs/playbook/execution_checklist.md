# 执行检查清单

本文用于人工执行前、中、后的检查。本文件不包含 Pine 代码，不构成投资建议。

## 执行前

### 市场状态

- 当前 Regime 是什么？
- 是否为 RANGE？
- 是否为 TRANSITION？
- 是否存在 EXHAUSTION？
- Dashboard 与主图是否一致？

### 结构状态

- Dow Structure 是 bullish_structure、bearish_structure，还是 no_structure？
- 最近 confirmed swing high 在哪里？
- 最近 confirmed swing low 在哪里？
- 当前方向的结构失效位在哪里？
- 是否存在 BOS / CHoCH？

### 区域位置

- 价格是否接近 L-ZONE？
- 价格是否接近 S-ZONE？
- 价格是否接近 Range High / Range Low？
- 是否已经远离合理区域，存在追价风险？

### 信号确认

- LONG / SHORT 是否互斥？
- PB-L / PB-S 是否互斥？
- BO-L / BO-S 是否互斥？
- BO-L / BO-S 的 Breakout Score 是否 >= 60？
- 信号是否满足 bar close confirmation？
- 信号是否依赖 confirmed pivot？

### 风险检查

- 是否出现 EXH-L 或 EXH-S？
- 是否出现 XL 或 XS？
- warning 是否被误当成反向入场？
- 离场参考是否被误当成反手入场？
- 止损是否脱离入场依据？

## 执行中

- 如果价格触发结构失效位，优先处理风险。
- 如果突破失败并回到原区间，降低 BO 信号置信度。
- 如果进入 RANGE，减少主信号假设。
- 如果进入 TRANSITION，只保留轻量观察。
- 如果出现 EXH-L / EXH-S，不直接反向，先评估持仓风险。

## 执行后

- 记录交易对。
- 记录周期。
- 记录 Regime。
- 记录 Structure。
- 记录信号类型。
- 记录入场依据。
- 记录失效条件。
- 记录离场依据。
- 保存截图到 `screenshots/`。
- 复盘是否违反方案规则。

## 一票否决项

出现以下情况时，不应执行高置信主信号：

- 没有 confirmed pivot 支撑结构。
- RANGE 中普通 LONG / SHORT。
- TRANSITION 中高置信 LONG / SHORT。
- BO-L / BO-S 的 Breakout Score < 60。
- EXH-L 被当成 SHORT。
- EXH-S 被当成 LONG。
- XL 被当成 SHORT。
- XS 被当成 LONG。
- 止损位置无法解释。
