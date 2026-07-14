# 测试计划 v1

本文根据 `docs/project_plan_v1.md` 完善，用于定义后续 Pine Script 实现后的测试项目、测试市场、测试周期、测试场景和验收标准。本文件不包含 Pine 代码。

## 测试目标

测试目标不是证明信号一定盈利，而是验证指标是否符合项目方案：

1. Pine v5 能稳定编译。
2. 不使用未来数据。
3. 使用 confirmed pivot。
4. 避免 repaint。
5. 信号不过密。
6. 状态机不冲突。
7. 图面不拥挤。
8. Dashboard 与主图一致。
9. alertcondition 清晰可用。
10. 所有主信号都有失效条件。
11. RANGE 默认压制 LONG / SHORT。
12. TRANSITION 只允许轻量观察，不输出高置信主信号。

## 前置条件

本测试计划用于 Pine 实现后的 TradingView 测试。

在进入 Pine 实现和执行本测试计划前，需要先完成 v0.3.5 Research Validation：

- 完成 `docs/validation_plan.md` 中定义的标准化案例验证。
- 完成核心信号统计。
- 完成 Breakout Score 阈值验证。
- 确认 Research Report 允许进入 v0.4。

## 1. Pine v5 编译测试

检查项目：

- 是否能在 TradingView 以 Pine Script v5 编译。
- 是否存在 undeclared identifier。
- 是否存在 line continuation 错误。
- 是否存在类型不匹配。
- 是否存在变量初始化顺序问题。
- 是否使用 `indicator()`。
- 是否没有使用 `strategy()`。
- overlay 是否为 true。

验收标准：

- 无编译错误。
- 无明显运行时报错。
- v1 仍保持观察指标定位。

## 2. repaint 测试

检查项目：

- 信号是否依赖未来数据。
- 历史信号是否在新 K 线出现后异常移动或消失。
- 结构标签是否在 pivot 未确认前提前出现。
- 主信号是否尽量基于 bar close confirmation。
- BO-L / BO-S 是否必须经过收盘确认，而不是盘中临时突破直接确认。

验收标准：

- 不使用未来函数逻辑。
- 不因未确认 pivot 提前输出主信号。
- 允许实时 K 线内状态变化，但收盘确认后应稳定。
- 依赖结构、突破和失效的信号，必须在收盘确认后才作为正式输出。

## 3. confirmed pivot 测试

检查项目：

- Swing High / Swing Low 是否使用 confirmed pivot。
- HH / HL / LH / LL 是否只基于确认后的 pivot。
- BOS / CHoCH 是否基于确认结构。
- LONG / SHORT 是否不依赖未确认结构。

验收标准：

- confirmed pivot 前不输出依赖结构的主信号。
- 结构失效位来自最近 confirmed swing。

## 4. lookahead_on 检查

检查项目：

- 不得使用 lookahead_on。
- 如果后续加入多周期数据，必须避免未来数据。
- 多周期状态不得提前引用未确认的高周期结果。

验收标准：

- 全项目无 lookahead_on。
- 多周期扩展前必须先更新方案和测试标准。

## 5. label / line / box 超限检查

检查项目：

- 标签数量是否可控。
- 区域数量是否可控。
- 线段和 box 是否有删除、复用或数量限制方案。
- 长时间历史数据加载后是否稳定。

验收标准：

- 不触发 TradingView 对 label / line / box 的限制。
- 图面不会因为历史数据过长而失控。
- 默认显示模式下图面保持清楚。

## 6. Dashboard 检查

检查项目：

- Regime 是否显示。
- Structure 是否显示。
- Momentum 是否显示。
- Volatility 是否显示。
- Breakout Score 是否显示。
- Trade Bias 是否显示。
- Risk State 是否显示。
- Dashboard 是否与主图标签一致。

验收标准：

- Dashboard 字段齐全。
- 字段内容不互相冲突。
- 风险状态优先显示。
- 不遮挡主要价格区域。

## 7. alertcondition 检查

检查项目：

- LONG 是否支持警报。
- SHORT 是否支持警报。
- PB-L 是否支持警报。
- PB-S 是否支持警报。
- BO-L 是否支持警报。
- BO-S 是否支持警报。
- EXH-L 是否支持警报。
- EXH-S 是否支持警报。
- XL 是否支持警报。
- XS 是否支持警报。

验收标准：

- warning 与主交易参考信号在警报名称中区分。
- 离场参考与反向入场信号在警报名称中区分。
- 不出现同一根 K 线重复触发大量同类警报。

## 8. 信号过密检查

检查项目：

- 是否使用信号冷却周期。
- RANGE 状态下 LONG / SHORT 是否明显减少。
- 同方向信号是否避免连续密集出现。
- 同一区域内是否避免重复刷标签。
- 同一突破结构内是否避免重复 BO-L / BO-S。

验收标准：

- 图面不被信号覆盖。
- 强趋势中有必要提示，但不刷屏。
- 横盘震荡中以等待和区间为主。

## 9. 状态机冲突检查

检查项目：

- Market Regime 与 Dow Structure 是否冲突。
- Dow Structure 失效时是否优先触发 XL / XS。
- EXH-L 是否不会直接变成 SHORT。
- EXH-S 是否不会直接变成 LONG。
- Breakout failed 是否能压制原 BO 信号。
- Signal State 是否避免 LONG / SHORT 同时出现。
- PB-L / PB-S 是否互斥。
- BO-L / BO-S 是否互斥，并由 Breakout Score 决定。
- RANGE 是否默认压制 LONG / SHORT。
- TRANSITION 是否只进入 watch、warning 或 breakout_attempt，不进入高置信 active。
- XL / XS 是否只作为离场参考，不直接触发反向入场。

验收标准：

- 状态冲突有优先级。
- 离场风险优先于新增入场。
- warning 不直接反向开仓。
- RANGE 中 Trade Bias 以 WAIT 或区间观察为主。
- TRANSITION 中不输出高置信 LONG / SHORT。
- Breakout Score < 60 时不得输出 BO-L / BO-S。

## 10. 测试市场

必须测试：

- BTCUSDT 15m
- BTCUSDT 1h
- BTCUSDT 4h
- ETHUSDT 1h
- SOLUSDT 1h

建议扩展测试：

- ETHUSDT 4h
- SOLUSDT 4h
- BTCUSDT 1D

## 11. 测试周期

必须测试：

- 15m
- 1h
- 4h
- 1D

周期检查重点：

- 15m：噪声过滤和信号冷却。
- 1h：主信号和状态机稳定性。
- 4h：结构和区域清晰度。
- 1D：大周期趋势状态和低频信号。

## 12. 测试场景

必须覆盖：

- 强上涨趋势
- 强下跌趋势
- 横盘震荡
- 真突破
- 假突破
- 趋势反转
- 高波动插针

每个场景检查重点：

- 强上涨趋势：是否优先 LONG、PB-L、BO-L，且不会频繁 SHORT。
- 强下跌趋势：是否优先 SHORT、PB-S、BO-S，且不会频繁 LONG。
- 横盘震荡：是否减少主信号，突出 Range High / Range Low。
- 真突破：Breakout Score 是否达到有效区间，BO-L / BO-S 是否合理。
- 假突破：是否能进入 breakout_failed 或触发风险提示。
- 趋势反转：是否先出现结构失效，再逐步进入新方向观察。
- 过渡状态：是否只进入轻量观察，等待 confirmed swing 和 bar close confirmation。
- 高波动插针：ATR buffer 是否能过滤噪声。

## 13. 测试记录要求

每次测试应记录：

- 测试日期
- 脚本版本
- 交易对
- 周期
- 测试场景
- 是否通过编译
- 是否出现 repaint 风险
- 是否出现信号过密
- 是否出现图面拥挤
- 是否有 TradingView 报错
- 截图文件名

截图建议保存到：

```text
screenshots/
```

## 14. 通过标准

v1 进入正式观察版前，至少需要满足：

- Pine v5 编译通过。
- 无 lookahead_on。
- 主结构基于 confirmed pivot。
- 主要市场和周期图面稳定。
- Dashboard 与主图一致。
- LONG / SHORT 不在 RANGE 中频繁出现。
- LONG / SHORT 不在 TRANSITION 中作为高置信主信号出现。
- PB-L / PB-S 明确互斥。
- BO-L / BO-S 明确互斥，且 Breakout Score >= 60。
- EXH-L / EXH-S 明确只是 warning。
- XL / XS 明确只是离场参考。
- label / line / box 不超限。
