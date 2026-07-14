# 反转日观察手册

本文用于定义趋势切换和反转观察流程。本文件不包含 Pine 代码。

## 核心原则

反转不能提前假设，必须先观察结构失效。

项目原则：

1. 先结构失效，再讨论反向机会。
2. 先 TRANSITION，再确认新趋势。
3. EXH-L / EXH-S 只是 warning。
4. XL / XS 只是离场参考。
5. 反向主信号必须等待新结构或有效突破确认。

## 多头转弱流程

观察顺序：

1. UP_TREND 后期出现 EXH-L。
2. 价格无法继续新高。
3. close 跌破 EMA20 且 MACD 转弱。
4. close 跌破最近 confirmed swing low。
5. Dow Structure 进入 bullish_invalidated。
6. Signal State 进入 long_exit。
7. 等待 bearish_structure 或 BO-S，再考虑 SHORT 观察。

禁止：

- EXH-L 出现后立刻做 SHORT。
- XL 出现后立刻反手 SHORT。
- 未确认 LH / LL 前假设下降趋势成立。

## 空头转强流程

观察顺序：

1. DOWN_TREND 后期出现 EXH-S。
2. 价格无法继续新低。
3. close 突破 EMA20 且 MACD 转强。
4. close 突破最近 confirmed swing high。
5. Dow Structure 进入 bearish_invalidated。
6. Signal State 进入 short_exit。
7. 等待 bullish_structure 或 BO-L，再考虑 LONG 观察。

禁止：

- EXH-S 出现后立刻做 LONG。
- XS 出现后立刻反手 LONG。
- 未确认 HH / HL 前假设上升趋势成立。

## TRANSITION 状态处理

TRANSITION 中只允许：

- long_watch
- short_watch
- breakout_attempt
- warning
- WAIT

TRANSITION 中不允许：

- 高置信 LONG
- 高置信 SHORT
- 直接反手
- 忽略结构失效位

## 反转日复盘重点

- 是否先出现旧结构失效。
- 是否等待 confirmed pivot。
- 是否使用 bar close confirmation。
- 是否把 warning 误用为反向信号。
- 是否把 XL / XS 误用为反手信号。
