# 多头 Setup 手册

本文用于定义 LONG、PB-L、BO-L 的人工观察流程。本文件不包含 Pine 代码。

## 适用背景

优先适用：

- Market Regime 为 UP_TREND。
- Dow Structure 为 bullish_structure。
- 价格位于 EMA20 上方或重新收回 EMA20。
- EMA10 >= EMA20。
- MACD 不明显空头扩张。

谨慎适用：

- Market Regime 为 RANGE：默认等待，不追普通 LONG。
- Market Regime 为 TRANSITION：只允许轻量观察，不做高置信 LONG。
- 出现 EXH-L：先检查风险，不急于新增多头。

## LONG 条件

1. bullish_structure 已确认。
2. close > EMA20。
3. EMA10 >= EMA20。
4. MACD 不明显空头扩张。
5. 价格靠近 L-ZONE，或 BO-L 已确认。
6. 未处于强震荡过滤状态。
7. 满足信号冷却周期。
8. 已确认多头结构失效位。

## PB-L 条件

1. 上升趋势中。
2. 回踩 EMA20、Bollinger Band 中轨或 L-ZONE。
3. 没有跌破最近 confirmed swing low。
4. 出现重新转强 K 线。
5. MACD 不明显转空。

## BO-L 条件

1. close 突破最近 confirmed high 或 range high。
2. 突破以 bar close confirmation 为主。
3. 突破距离超过 ATR buffer。
4. Breakout Score >= 60。
5. MACD 同向或不明显背离。
6. 突破 K 线实体放大。
7. 突破后没有快速回到原区间。

## 失效条件

- close 跌破最近 confirmed swing low。
- Dow Structure 进入 bullish_invalidated。
- close 跌破 EMA20 且 MACD 转弱。
- BO-L 失败并回到原区间。
- Market Regime 转为 RANGE、TRANSITION 或 DOWN_TREND。
- 出现 XL。

## 执行前检查

- 当前不是高置信 TRANSITION。
- 当前不是强 RANGE。
- EXH-L 没有明显扩大。
- 结构失效位清楚。
- 入场位置不是远离 L-ZONE 的追涨。
- 目标区和风险区都能在图上解释。

## 禁止事项

- 不因 MACD 金叉单独做 LONG。
- 不因价格刚站上 EMA20 单独做 LONG。
- 不在未确认 pivot 前依赖结构信号。
- 不把 EXH-S 直接当成 LONG。
- 不把 XS 直接当成 LONG。
