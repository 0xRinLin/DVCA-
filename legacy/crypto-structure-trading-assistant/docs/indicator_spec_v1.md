# 指标规格 v1

本文根据 `docs/project_plan_v1.md` 完善，用于定义 Crypto Structure Trading Assistant 的指标定位、模块边界、状态输出和实现约束。本文件不包含 Pine 代码。

## 1. 指标名称

Crypto Structure Trading Assistant

项目目录名称：

```text
crypto-structure-trading-assistant
```

目标脚本文件：

```text
pine/crypto_structure_trading_assistant_v1.pine
```

## 2. 指标定位

本指标是 TradingView Pine Script v5 结构型交易观察辅助工具，主要用于加密货币市场。

本指标用于辅助观察：

- 当前行情状态
- 道氏结构
- 多空趋势方向
- L-ZONE / S-ZONE
- Range High / Range Low
- Breakout Score
- LONG / SHORT 参考信号
- PB / BO 机会
- EXH 衰竭警示
- XL / XS 离场参考
- 结构失效位置

本指标不是：

- 自动下单机器人
- 自动回测策略
- 无条件买卖点系统
- 高频交易系统
- 黑箱预测系统

## 3. 支持市场

优先支持：

- BTC
- ETH
- SOL

可扩展支持：

- 其他高流动性加密货币交易对

不优先支持：

- 低流动性小币种
- 极端插针频繁且成交深度不足的交易对
- 数据源质量不稳定的交易对

## 4. 支持周期

优先周期：

- 15m
- 1h
- 4h
- 1D

周期使用原则：

- 15m 更容易出现噪声，需要更严格的 ATR buffer 和信号冷却。
- 1h 是主要观察周期，适合大多数结构与信号验证。
- 4h 更适合判断趋势背景和重要区域。
- 1D 更适合判断大方向，不应期待高频信号。

## 5. 必须包含的模块

### 输入参数模块

用于集中管理周期、长度、阈值、显示开关和信号冷却参数。

必须覆盖：

- EMA 长度
- Bollinger Band 长度与倍数
- MACD 参数
- ATR 长度
- ATR buffer 倍数
- pivot 确认参数
- Breakout Score 阈值
- 信号冷却周期
- Dashboard 显示开关
- 标签和区域显示开关

### EMA 模块

必须包含：

- EMA 5
- EMA 10
- EMA 20
- EMA 40
- EMA 60

用途：

- 判断趋势过滤
- 判断价格相对中短期均线位置
- 辅助 L-ZONE / S-ZONE
- 辅助 PB-L / PB-S

### Bollinger Band 模块

默认参数：

- 长度 20
- 倍数 2

用途：

- 判断波动扩张或收缩
- 辅助识别震荡
- 辅助判断价格是否接近上轨 / 下轨
- 辅助 EXH-L / EXH-S

### MACD 模块

默认参数：

- 12
- 26
- 9

用途：

- 判断动能方向
- 判断动能扩张或减弱
- 过滤低质量 LONG / SHORT
- 辅助 Breakout Score
- 辅助 EXH-L / EXH-S

使用限制：

- 不把 MACD 金叉或死叉单独作为买卖命令。

### ATR 模块

默认参数：

- ATR 14

用途：

- 构造 ATR buffer
- 过滤噪声突破
- 判断高波动插针风险
- 辅助 Stop Zone

### Swing High / Swing Low 模块

用途：

- 识别 confirmed swing high
- 识别 confirmed swing low
- 作为 HH / HL / LH / LL 的基础
- 作为结构失效位的基础

规则：

- 必须使用 confirmed pivots。
- 不允许使用未确认 pivot 触发主信号。
- 结构判断必须等待 pivot 确认。

### HH / HL / LH / LL 模块

用途：

- 识别道氏结构
- 判断多头结构、空头结构、震荡或过渡结构
- 支持 BOS / CHoCH
- 支持结构失效判断

### Dow Structure 道氏结构模块

必须输出：

- no_structure
- bullish_structure
- bearish_structure
- bullish_invalidated
- bearish_invalidated
- transition_structure

结构失效：

- 上涨结构中，close 跌破最近 confirmed swing low，视为上涨结构失效。
- 下跌结构中，close 突破最近 confirmed swing high，视为下跌结构失效。

### Market Regime 行情状态模块

必须输出：

- UP_TREND
- DOWN_TREND
- RANGE
- TRANSITION
- EXHAUSTION

用途：

- 过滤交易方向
- 降低震荡区信号密度
- 判断是否只观察而不触发主信号

### L-ZONE / S-ZONE 区域模块

区域必须服务于结构，而不是装饰。

L-ZONE 用于：

- 多头结构中的回踩观察
- PB-L
- LONG 位置过滤

S-ZONE 用于：

- 空头结构中的反抽观察
- PB-S
- SHORT 位置过滤

### Breakout Score 突破评分模块

评分范围：

- 0 - 30：弱突破，假突破风险高
- 31 - 60：普通突破
- 61 - 80：有效突破
- 81 - 100：强突破

默认规则：

- Breakout Score >= 60 才允许 BO-L / BO-S。

评分因素：

- 收盘突破关键位
- 突破距离超过 ATR buffer
- BTC / ETH 60m 可参考 2% 原则
- 突破 K 线实体放大
- MACD 同向扩张
- Bollinger Band 宽度扩大
- 突破后没有快速回到原区间

### Entry Signals 入场参考信号模块

必须保留：

- LONG
- SHORT
- PB-L
- PB-S
- BO-L
- BO-S

使用原则：

- 所有入场参考信号必须有失效条件。
- 主信号必须经过 Market Regime、Dow Structure、趋势过滤和冷却周期过滤。
- RANGE 中不得频繁输出 LONG / SHORT。
- TRANSITION 中不得输出高置信 LONG / SHORT，只允许轻量观察状态。
- 依赖结构、突破或失效的主信号，优先基于 bar close confirmation。

### Exit Signals 离场参考信号模块

必须保留：

- EXH-L
- EXH-S
- XL
- XS

使用原则：

- EXH-L / EXH-S 是 warning，不是反向开仓信号。
- XL / XS 是离场参考，不是反向入场命令。
- 离场信号优先级高于新增同向入场信号。

### Dashboard 状态面板模块

必须显示：

- Regime
- Structure
- Momentum
- Volatility
- Breakout Score
- Trade Bias
- Risk State

Dashboard 必须与主图状态一致，不应显示与主图信号冲突的结论。

### Alertcondition 警报模块

后续实现必须支持以下信号警报：

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

warning 与主交易参考信号必须在警报文本中区分。

## 6. Market Regime 行情状态

### UP_TREND

含义：上升趋势。

典型条件：

- 道氏结构偏多。
- 价格主要位于 EMA20 上方。
- EMA10 >= EMA20。
- MACD 不明显空头扩张。
- 回踩不破最近 confirmed swing low。

允许优先观察：

- LONG
- PB-L
- BO-L

### DOWN_TREND

含义：下降趋势。

典型条件：

- 道氏结构偏空。
- 价格主要位于 EMA20 下方。
- EMA10 <= EMA20。
- MACD 不明显多头扩张。
- 反抽不破最近 confirmed swing high。

允许优先观察：

- SHORT
- PB-S
- BO-S

### RANGE

含义：横盘震荡。

典型条件：

- 价格反复穿越 EMA20。
- Bollinger Band 宽度收窄。
- MACD 靠近零轴。
- 高低点结构不清晰。

处理原则：

- 减少 LONG / SHORT。
- 重点观察 Range High / Range Low。
- 等待有效突破或结构转向。
- 默认 Trade Bias 应偏向 WAIT。

### TRANSITION

含义：趋势切换中。

典型条件：

- 原趋势结构失效。
- 新方向结构尚未完整确认。
- 价格与均线、MACD、道氏结构出现分歧。

处理原则：

- 只允许轻量观察。
- 不允许高置信 LONG / SHORT 主信号。
- 优先等待 confirmed swing 和突破确认。
- Dashboard 的 Trade Bias 应偏向 WAIT、WATCH 或 RISK，而不是强 LONG / SHORT。

### EXHAUSTION

含义：趋势衰竭。

典型条件：

- 趋势后期价格接近关键阻力或支撑。
- K 线实体缩小或影线变长。
- MACD 动能减弱。
- 价格创新高或新低但动能未同步增强。

处理原则：

- 输出 EXH-L / EXH-S。
- 不直接反向开仓。
- 结合 XL / XS 判断离场参考。

## 7. Dow Structure 道氏结构状态

必须识别：

- HH：Higher High，更高高点
- HL：Higher Low，更高低点
- LH：Lower High，更低高点
- LL：Lower Low，更低低点

结构解释：

- HH + HL = 多头结构
- LH + LL = 空头结构
- 高低点混乱 = 震荡或过渡结构

关键结构变量：

- lastConfirmedHigh
- lastConfirmedLow
- lastBullishInvalidation
- lastBearishInvalidation

失效边界：

- 多头结构的核心失效位是最近 confirmed swing low。
- 空头结构的核心失效位是最近 confirmed swing high。

## 8. 信号列表

入场参考：

- LONG
- SHORT
- PB-L
- PB-S
- BO-L
- BO-S

风险与离场参考：

- EXH-L
- EXH-S
- XL
- XS

信号输出原则：

- 不在未确认结构上输出主信号。
- 不在强震荡状态下密集输出主信号。
- 不在 TRANSITION 状态下输出高置信 LONG / SHORT。
- 不把 warning 当成反向信号。
- 不把离场信号当成反手信号。
- BO-L / BO-S 必须由 Breakout Score 决定，默认阈值为 60。
- 主信号优先基于 bar close confirmation。

## 9. Dashboard 状态面板内容

Dashboard 字段含义：

- Regime：当前行情状态。
- Structure：当前道氏结构。
- Momentum：MACD 与价格动能状态。
- Volatility：Bollinger Band 和 ATR 代表的波动状态。
- Breakout Score：突破质量评分。
- Trade Bias：当前观察偏向，多头、空头、等待或风险。
- Risk State：结构失效、衰竭、假突破或正常。

Dashboard 显示优先级：

1. 结构失效和风险状态优先。
2. Market Regime 次之。
3. Breakout Score 和 Trade Bias 再次之。
4. 不显示与主图信号矛盾的结论。

## 10. v1 不做 strategy 的说明

v1 版本只使用 `indicator()`，不使用 `strategy()`。

不做 strategy 的原因：

- 当前项目目标是观察结构，不是自动回测。
- 信号规则仍需通过图面和人工复盘验证。
- 结构、状态机和视觉语言需要先稳定。
- 过早回测容易把观察工具误用成机械交易系统。

后续只有在 v1 观察指标稳定后，才考虑策略回测版本。
