# 信号规则 v1

本文根据 `docs/project_plan_v1.md` 完善，用于定义 Crypto Structure Trading Assistant 的信号含义、触发条件、失效条件、使用边界和优先级。本文件不包含 Pine 代码。

## 总体原则

1. 所有信号都是交易观察参考，不是自动买卖命令。
2. 所有主信号必须有明确失效条件。
3. LONG / SHORT 不能只由单一指标触发。
4. PB-L / PB-S 必须发生在已有趋势背景中。
5. BO-L / BO-S 必须通过 Breakout Score 过滤。
6. EXH-L / EXH-S 只是 warning，不允许作为反向开仓信号。
7. XL / XS 是离场参考，不是反手入场信号。
8. RANGE 状态中必须减少主信号。
9. 信号必须受冷却周期控制，避免过密。
10. confirmed pivot 未确认前，不允许输出依赖结构的主信号。
11. TRANSITION 状态中只允许轻量观察，不允许输出高置信 LONG / SHORT 主信号。
12. 依赖结构、突破或失效的信号，必须尽量基于 bar close confirmation。

## 信号优先级

当多个信号同时满足时，按以下顺序处理：

1. 结构失效类：XL / XS
2. 风险警示类：EXH-L / EXH-S
3. 有效突破类：BO-L / BO-S
4. 回踩反抽类：PB-L / PB-S
5. 主入场参考：LONG / SHORT

优先级说明：

- 离场和风险优先于新增入场。
- 反向信号不得在结构尚未转换时直接覆盖原方向。
- RANGE 状态中 BO-L / BO-S 的优先级高于普通 LONG / SHORT。

## 信号互斥原则

- LONG 与 SHORT 不应在同一根 K 线上同时出现。
- PB-L 与 PB-S 不应在同一结构状态下同时出现。
- BO-L 与 BO-S 不应在同一关键区间同时出现。
- EXH-L 可以与多头风险状态共存，但不能变成 SHORT。
- EXH-S 可以与空头风险状态共存，但不能变成 LONG。
- XL 出现时，不应同时输出新的 LONG。
- XS 出现时，不应同时输出新的 SHORT。
- RANGE 状态下默认压制 LONG / SHORT，只允许区间观察或等待有效突破。
- TRANSITION 状态下默认压制高置信 LONG / SHORT，只允许 long_watch、short_watch、breakout_attempt、warning 等轻量观察状态。

## 信号决策门槛

在输出任何主信号前，必须先通过以下门槛：

1. 结构门槛：必须有 confirmed pivot 支撑的 Dow Structure 或明确的有效突破。
2. 状态门槛：RANGE 默认等待，TRANSITION 默认只观察。
3. 收盘门槛：主信号优先使用 bar close confirmation，不用盘中临时突破直接确认。
4. 冲突门槛：如果同时存在离场、warning、入场条件，离场和 warning 优先。
5. 评分门槛：BO-L / BO-S 必须由 Breakout Score 决定，默认阈值为 60。
6. 冷却门槛：未满足冷却周期时，不重复输出同类主信号。

## LONG

含义：多头入场参考，用于提示当前环境更适合观察顺势做多机会。

触发条件：

- Market Regime 为 UP_TREND。
- Dow Structure 为 bullish_structure。
- close > EMA20。
- EMA10 >= EMA20。
- MACD 不明显空头扩张。
- close 位于 Bollinger Band 中轨上方，或重新收回中轨。
- 价格靠近 L-ZONE，或完成有效向上突破。
- 未处于强震荡过滤状态。
- 未处于 TRANSITION 状态。
- 最近没有同方向信号过密输出。
- 满足信号冷却周期。

失效条件：

- close 跌破最近 confirmed swing low。
- Dow Structure 进入 bullish_invalidated。
- close 跌破 EMA20 且 MACD 转弱。
- BO-L 失败并回到原区间。
- Market Regime 转为 DOWN_TREND。
- Market Regime 转为 RANGE 或 TRANSITION。
- 出现 XL。

是否允许作为主交易信号：允许作为主参考信号，但必须结合结构失效位、趋势过滤、区域位置和信号冷却。

是否只是 warning：不是 warning。

备注：

- LONG 不应在 RANGE 中频繁出现。
- LONG 不应在 TRANSITION 中作为高置信主信号出现。
- LONG 不能只因为 MACD 金叉或价格站上 EMA20 就触发。

## SHORT

含义：空头入场参考，用于提示当前环境更适合观察顺势做空机会。

触发条件：

- Market Regime 为 DOWN_TREND。
- Dow Structure 为 bearish_structure。
- close < EMA20。
- EMA10 <= EMA20。
- MACD 不明显多头扩张。
- close 位于 Bollinger Band 中轨下方，或重新跌破中轨。
- 价格靠近 S-ZONE，或完成有效向下跌破。
- 未处于强震荡过滤状态。
- 未处于 TRANSITION 状态。
- 最近没有同方向信号过密输出。
- 满足信号冷却周期。

失效条件：

- close 突破最近 confirmed swing high。
- Dow Structure 进入 bearish_invalidated。
- close 突破 EMA20 且 MACD 转强。
- BO-S 失败并回到原区间。
- Market Regime 转为 UP_TREND。
- Market Regime 转为 RANGE 或 TRANSITION。
- 出现 XS。

是否允许作为主交易信号：允许作为主参考信号，但必须结合结构失效位、趋势过滤、区域位置和信号冷却。

是否只是 warning：不是 warning。

备注：

- SHORT 不应在 RANGE 中频繁出现。
- SHORT 不应在 TRANSITION 中作为高置信主信号出现。
- SHORT 不能只因为 MACD 死叉或价格跌破 EMA20 就触发。

## PB-L

含义：上升趋势中的回踩做多观察。

触发条件：

- Market Regime 为 UP_TREND。
- Dow Structure 为 bullish_structure。
- 价格回踩 EMA20、Bollinger Band 中轨或 L-ZONE。
- 回踩过程中没有跌破最近 confirmed swing low。
- 出现重新转强 K 线。
- MACD 不明显转空。
- 回踩后价格没有快速跌回弱势区。

失效条件：

- close 跌破最近 confirmed swing low。
- 回踩后不能重新转强。
- L-ZONE 被有效跌破。
- Market Regime 转为 RANGE、TRANSITION 或 DOWN_TREND。
- 出现 XL。

是否允许作为主交易信号：允许作为主参考信号，但它的定位是趋势内回踩机会，不是底部反转信号。

是否只是 warning：不是 warning。

备注：

- PB-L 必须依赖已有上升结构。
- 没有 confirmed bullish_structure 时，不应把普通下跌当成 PB-L。

## PB-S

含义：下降趋势中的反抽做空观察。

触发条件：

- Market Regime 为 DOWN_TREND。
- Dow Structure 为 bearish_structure。
- 价格反抽 EMA20、Bollinger Band 中轨或 S-ZONE。
- 反抽过程中没有突破最近 confirmed swing high。
- 出现重新转弱 K 线。
- MACD 不明显转多。
- 反抽后价格没有快速站回强势区。

失效条件：

- close 突破最近 confirmed swing high。
- 反抽后不能重新转弱。
- S-ZONE 被有效突破。
- Market Regime 转为 RANGE、TRANSITION 或 UP_TREND。
- 出现 XS。

是否允许作为主交易信号：允许作为主参考信号，但它的定位是趋势内反抽机会，不是顶部反转信号。

是否只是 warning：不是 warning。

备注：

- PB-S 必须依赖已有下降结构。
- 没有 confirmed bearish_structure 时，不应把普通上涨当成 PB-S。

## BO-L

含义：向上有效突破。

触发条件：

- close 突破最近 confirmed high 或 range high。
- 突破必须以 bar close confirmation 为主。
- 突破距离超过 ATR buffer。
- Breakout Score >= 默认阈值 60。
- MACD 同向或不明显背离。
- 突破 K 线实体放大。
- Bollinger Band 宽度扩张或开始扩张。
- 突破后没有快速回到原区间。

失效条件：

- 突破后 close 回到原 range high 下方。
- Breakout Score 降到 30 以下。
- MACD 动能快速转弱。
- 突破 K 线后连续无法延续。
- Market Regime 回到 RANGE。

是否允许作为主交易信号：允许作为主参考信号，但必须通过 Breakout Score 过滤。

是否只是 warning：不是 warning。

备注：

- BO-L 不能只由 `close > high` 类型条件触发。
- BO-L 后可进入 retest 或 continuation 观察。

## BO-S

含义：向下有效跌破。

触发条件：

- close 跌破最近 confirmed low 或 range low。
- 跌破必须以 bar close confirmation 为主。
- 跌破距离超过 ATR buffer。
- Breakout Score >= 默认阈值 60。
- MACD 同向或不明显背离。
- 跌破 K 线实体放大。
- Bollinger Band 宽度扩张或开始扩张。
- 跌破后没有快速回到原区间。

失效条件：

- 跌破后 close 回到原 range low 上方。
- Breakout Score 降到 30 以下。
- MACD 空头动能快速转弱。
- 跌破 K 线后连续无法延续。
- Market Regime 回到 RANGE。

是否允许作为主交易信号：允许作为主参考信号，但必须通过 Breakout Score 过滤。

是否只是 warning：不是 warning。

备注：

- BO-S 不能只由 `close < low` 类型条件触发。
- BO-S 后可进入 retest 或 continuation 观察。

## EXH-L

含义：多头衰竭警示，用于提示多头趋势后期风险上升。

触发条件：

- Market Regime 为 UP_TREND 或 EXHAUSTION。
- 价格接近上方阻力、Target Zone 或 Bollinger Band 上轨。
- 出现长上影线、实体缩小或连续上攻乏力。
- MACD 动能减弱。
- 价格创新高但动能没有同步增强。

失效条件：

- 价格继续有效上行。
- MACD 动能重新增强。
- BO-L 后进入 continuation。
- 新高后没有出现回落确认。

是否允许作为主交易信号：不允许作为主交易信号。

是否只是 warning：是 warning。

备注：

- EXH-L 不是 SHORT。
- EXH-L 可以提示减仓、保护利润或等待 XL，但不能单独反向。

## EXH-S

含义：空头衰竭警示，用于提示空头趋势后期风险上升。

触发条件：

- Market Regime 为 DOWN_TREND 或 EXHAUSTION。
- 价格接近下方支撑、Target Zone 或 Bollinger Band 下轨。
- 出现长下影线、实体缩小或连续下跌乏力。
- MACD 空头动能减弱。
- 价格创新低但动能没有同步增强。

失效条件：

- 价格继续有效下跌。
- MACD 空头动能重新增强。
- BO-S 后进入 continuation。
- 新低后没有出现反弹确认。

是否允许作为主交易信号：不允许作为主交易信号。

是否只是 warning：是 warning。

备注：

- EXH-S 不是 LONG。
- EXH-S 可以提示减仓、保护利润或等待 XS，但不能单独反向。

## XL

含义：多单离场参考。

触发条件：

- 多头结构失效。
- close 跌破最近 confirmed swing low。
- close 跌破 EMA20 且 MACD 转弱。
- 出现 EXH-L 后价格无法继续新高。
- BO-L 失败并回到原区间。
- Signal State 从 long_active 转向 long_exit。

失效条件：

- 多头结构恢复。
- 价格重新站回 EMA20 上方且 MACD 转强。
- Breakout State 重新进入 continuation。
- 新 confirmed swing 重新建立 bullish_structure。

是否允许作为主交易信号：不作为入场主信号，只作为离场参考。

是否只是 warning：不是 warning，是离场参考信号。

备注：

- XL 不等于 SHORT。
- XL 出现后，如果要转为空头观察，必须等待空头结构或有效跌破确认。

## XS

含义：空单离场参考。

触发条件：

- 空头结构失效。
- close 突破最近 confirmed swing high。
- close 突破 EMA20 且 MACD 转强。
- 出现 EXH-S 后价格无法继续新低。
- BO-S 失败并回到原区间。
- Signal State 从 short_active 转向 short_exit。

失效条件：

- 空头结构恢复。
- 价格重新跌回 EMA20 下方且 MACD 转弱。
- Breakout State 重新进入 continuation。
- 新 confirmed swing 重新建立 bearish_structure。

是否允许作为主交易信号：不作为入场主信号，只作为离场参考。

是否只是 warning：不是 warning，是离场参考信号。

备注：

- XS 不等于 LONG。
- XS 出现后，如果要转为多头观察，必须等待多头结构或有效突破确认。

## 信号冷却原则

后续实现必须设置冷却机制：

- 同方向 LONG / SHORT 不应连续密集出现。
- PB-L / PB-S 在同一回踩或反抽段内不应重复刷屏。
- BO-L / BO-S 在同一突破结构内只保留关键提示。
- EXH-L / EXH-S 可重复提醒，但必须限制频率。
- XL / XS 出现后，应等待新结构或新状态再允许新的同向入场。

## 信号验收标准

后续实现完成后，信号需要满足：

- 每个信号都有触发依据。
- 每个主信号都有失效条件。
- warning 与主信号清晰区分。
- 离场参考与反手入场清晰区分。
- RANGE 状态下信号明显减少。
- TRANSITION 状态下只允许轻量观察，不输出高置信 LONG / SHORT。
- 强趋势中信号不应完全缺失。
- 假突破场景中 BO-L / BO-S 能被过滤或快速失效。
