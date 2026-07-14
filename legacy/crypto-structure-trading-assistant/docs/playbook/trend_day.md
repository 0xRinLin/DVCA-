# 趋势日观察手册

本文用于定义趋势行情中的观察重点。本文件不包含 Pine 代码。

## 趋势日特征

多头趋势日常见特征：

- Market Regime 为 UP_TREND。
- Dow Structure 为 bullish_structure。
- 回踩不破最近 confirmed swing low。
- 价格多次在 EMA20 或 L-ZONE 附近重新转强。
- BO-L 后没有快速回到原区间。

空头趋势日常见特征：

- Market Regime 为 DOWN_TREND。
- Dow Structure 为 bearish_structure。
- 反抽不破最近 confirmed swing high。
- 价格多次在 EMA20 或 S-ZONE 附近重新转弱。
- BO-S 后没有快速回到原区间。

## 多头趋势日策略

优先观察：

- PB-L
- BO-L
- LONG

风险观察：

- EXH-L
- XL

处理原则：

- 不因单根回落直接看空。
- 回踩只要不破 confirmed swing low，优先按趋势内调整处理。
- 追涨前必须检查是否远离 L-ZONE。
- 出现 EXH-L 后先减少激进多头假设。

## 空头趋势日策略

优先观察：

- PB-S
- BO-S
- SHORT

风险观察：

- EXH-S
- XS

处理原则：

- 不因单根反弹直接看多。
- 反抽只要不破 confirmed swing high，优先按趋势内调整处理。
- 追空前必须检查是否远离 S-ZONE。
- 出现 EXH-S 后先减少激进空头假设。

## 趋势日禁止事项

- 不逆势抢反转。
- 不把 warning 当反向开仓。
- 不在结构未失效前频繁切换方向。
- 不让止损脱离入场依据。

## 趋势日复盘重点

- 信号是否顺着主要结构。
- PB 和 BO 是否有明确失效条件。
- RANGE 是否被误判成趋势。
- EXH 是否及时提示风险。
- XL / XS 是否只作为离场参考。
