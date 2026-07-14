# 空头 Setup 手册

本文用于定义 SHORT、PB-S、BO-S 的人工观察流程。本文件不包含 Pine 代码。

## 适用背景

优先适用：

- Market Regime 为 DOWN_TREND。
- Dow Structure 为 bearish_structure。
- 价格位于 EMA20 下方或重新跌破 EMA20。
- EMA10 <= EMA20。
- MACD 不明显多头扩张。

谨慎适用：

- Market Regime 为 RANGE：默认等待，不追普通 SHORT。
- Market Regime 为 TRANSITION：只允许轻量观察，不做高置信 SHORT。
- 出现 EXH-S：先检查风险，不急于新增空头。

## SHORT 条件

1. bearish_structure 已确认。
2. close < EMA20。
3. EMA10 <= EMA20。
4. MACD 不明显多头扩张。
5. 价格靠近 S-ZONE，或 BO-S 已确认。
6. 未处于强震荡过滤状态。
7. 满足信号冷却周期。
8. 已确认空头结构失效位。

## PB-S 条件

1. 下降趋势中。
2. 反抽 EMA20、Bollinger Band 中轨或 S-ZONE。
3. 没有突破最近 confirmed swing high。
4. 出现重新转弱 K 线。
5. MACD 不明显转多。

## BO-S 条件

1. close 跌破最近 confirmed low 或 range low。
2. 跌破以 bar close confirmation 为主。
3. 跌破距离超过 ATR buffer。
4. Breakout Score >= 60。
5. MACD 同向或不明显背离。
6. 跌破 K 线实体放大。
7. 跌破后没有快速回到原区间。

## 失效条件

- close 突破最近 confirmed swing high。
- Dow Structure 进入 bearish_invalidated。
- close 突破 EMA20 且 MACD 转强。
- BO-S 失败并回到原区间。
- Market Regime 转为 RANGE、TRANSITION 或 UP_TREND。
- 出现 XS。

## 执行前检查

- 当前不是高置信 TRANSITION。
- 当前不是强 RANGE。
- EXH-S 没有明显扩大。
- 结构失效位清楚。
- 入场位置不是远离 S-ZONE 的追空。
- 目标区和风险区都能在图上解释。

## 禁止事项

- 不因 MACD 死叉单独做 SHORT。
- 不因价格刚跌破 EMA20 单独做 SHORT。
- 不在未确认 pivot 前依赖结构信号。
- 不把 EXH-L 直接当成 SHORT。
- 不把 XL 直接当成 SHORT。
