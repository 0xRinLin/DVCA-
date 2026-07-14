# 视觉设计 v1

本文根据 `docs/project_plan_v1.md` 完善，用于定义主图元素、Dashboard、标签、颜色、层级、密度控制和图面验收标准。本文件不包含 Pine 代码。

## 设计目标

视觉设计服务于结构观察，而不是制造买卖冲动。

核心目标：

1. 让用户先看到行情状态。
2. 让用户看清道氏结构。
3. 让用户知道关键区域在哪里。
4. 让用户区分主信号、warning 和离场参考。
5. 避免图面拥挤。
6. 避免标签刷屏。

## 1. 主图显示元素

### 趋势与波动元素

主图需要显示：

- EMA 5
- EMA 10
- EMA 20
- EMA 40
- EMA 60
- Bollinger Band 上轨
- Bollinger Band 中轨
- Bollinger Band 下轨

显示原则：

- EMA20 是核心趋势参考。
- EMA5 / EMA10 用于短期动能辅助。
- EMA40 / EMA60 用于中期背景辅助。
- Bollinger Band 用于波动、震荡和衰竭判断。
- 均线和布林带不能抢占信号与结构标签的视觉层级。

### 结构元素

主图需要显示：

- Swing High
- Swing Low
- HH
- HL
- LH
- LL
- BOS
- CHoCH
- ZC-L
- ZC-S

显示原则：

- Swing 与 HH / HL / LH / LL 只基于 confirmed pivot。
- BOS / CHoCH 必须基于结构确认。
- ZC-L / ZC-S 必须与结构转折或区域确认相关。
- 结构标签应简洁，不应每根 K 线都显示。

### 区域元素

主图需要显示：

- L-ZONE
- S-ZONE
- Range High
- Range Low
- Stop Zone
- Target Zone

区域作用：

- L-ZONE 用于观察回踩做多。
- S-ZONE 用于观察反抽做空。
- Range High / Range Low 用于判断突破。
- Stop Zone 用于判断结构失效。
- Target Zone 用于辅助止盈。

显示原则：

- 区域优先于密集箭头。
- 区域透明度要适中，不能遮挡 K 线。
- Stop Zone 和 Target Zone 应清晰但克制。

### 信号元素

主图需要显示：

- LONG
- SHORT
- PB-L
- PB-S
- BO-L
- BO-S
- EXH-L
- EXH-S
- XL
- XS

显示原则：

- LONG / SHORT 是主参考信号。
- PB-L / PB-S 是趋势内回踩或反抽观察。
- BO-L / BO-S 是有效突破或跌破。
- EXH-L / EXH-S 是 warning。
- XL / XS 是离场参考。
- warning 和离场参考必须与入场参考视觉区分。

## 2. Dashboard 显示元素

Dashboard 必须显示：

- Regime
- Structure
- Momentum
- Volatility
- Breakout Score
- Trade Bias
- Risk State

字段说明：

- Regime：UP_TREND、DOWN_TREND、RANGE、TRANSITION、EXHAUSTION。
- Structure：bullish_structure、bearish_structure、no_structure、invalidated 或 transition。
- Momentum：MACD 动能方向和强弱。
- Volatility：Bollinger Band 与 ATR 表示的波动状态。
- Breakout Score：0 - 100 的突破质量评分。
- Trade Bias：LONG、SHORT、WAIT、RISK 或 EXIT。
- Risk State：normal、warning、partial_exit、full_exit、fake_breakout 风险等。

Dashboard 规则：

- 必须与主图信号一致。
- 不能显示与当前结构相反的强烈偏向。
- 风险状态优先显示。
- 字段数量保持精简，不做说明书式堆叠。

## 3. 标签名称

必须保留以下标签或概念：

- L-ZONE
- S-ZONE
- ZC-L
- ZC-S
- LONG
- SHORT
- PB-L
- PB-S
- BO-L
- BO-S
- EXH-L
- EXH-S
- XL
- XS
- HH
- HL
- LH
- LL
- BOS
- CHoCH

标签命名原则：

- 信号名称保持简短。
- 不把中文长句放进主图标签。
- 说明性文字放在文档或 Dashboard 中，不堆在 K 线上。

## 4. 颜色含义

颜色规则：

- 绿色 = 多头
- 红色 = 空头
- 黄色 = 观察 / 警示
- 灰色 = 震荡 / 等待
- 蓝色 = 突破
- 紫色 = 衰竭

使用原则：

- 多头结构和 LONG 相关元素使用绿色系。
- 空头结构和 SHORT 相关元素使用红色系。
- PB-L / PB-S 可使用观察色或方向色的弱化版本。
- BO-L / BO-S 使用蓝色与方向色结合。
- EXH-L / EXH-S 使用紫色或黄色警示。
- RANGE 和 WAIT 使用灰色。
- 不使用过多高饱和颜色。

## 5. 视觉层级

建议视觉优先级：

1. K 线和价格本身
2. 关键区域：L-ZONE / S-ZONE / Range High / Range Low
3. 结构标签：HH / HL / LH / LL / BOS / CHoCH
4. 主信号：LONG / SHORT / BO-L / BO-S
5. 回踩反抽：PB-L / PB-S
6. 风险与离场：EXH-L / EXH-S / XL / XS
7. 均线和 Bollinger Band
8. Dashboard

说明：

- 区域和结构应帮助用户理解信号来源。
- 信号不应遮挡结构关键点。
- Dashboard 不应遮挡主图主要价格区域。

## 6. 信号密度控制原则

必须控制：

- 同方向信号冷却。
- 同一区域内重复提示。
- 同一突破结构内重复 BO-L / BO-S。
- RANGE 状态下 LONG / SHORT 过密。
- EXH-L / EXH-S warning 过密。
- XL / XS 与反向主信号同时出现。

密度控制要求：

- 信号宁可少，不可乱。
- 主信号必须有结构依据。
- 区域显示优先于箭头堆叠。
- 同一段趋势中，重复标签应尽量压缩。

## 7. 图面不过度拥挤的原则

必须避免：

- 每根 K 线都显示标签。
- 多种标签重叠。
- label / line / box 接近 TradingView 限制。
- Dashboard 信息过多。
- 区域透明度过低导致遮挡价格。
- 颜色过多导致用户无法区分重点。

建议方式：

- 使用显示开关控制模块。
- 默认只显示核心结构、区域、主信号和 Dashboard。
- 可选显示更多调试类信息。
- 对历史区域和标签进行数量管理。

## 8. 视觉验收标准

后续实现完成后，图面需要满足：

- 一眼能看出 Regime 和 Structure。
- L-ZONE / S-ZONE 清晰但不遮挡价格。
- LONG / SHORT 与 EXH / XL / XS 能明显区分。
- RANGE 中信号明显减少。
- 强趋势中结构标签和主信号不混乱。
- Dashboard 字段与主图状态一致。
- 长时间加载历史数据后不出现标签或区域超限。
