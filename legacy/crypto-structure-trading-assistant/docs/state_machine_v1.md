# 状态机 v1

本文根据 `docs/project_plan_v1.md` 完善，用于定义 v1 需要遵守的五个状态机、状态优先级、进入条件、退出条件、失效条件、图面显示和对信号的影响。本文件不包含 Pine 代码。

## 总体原则

1. 状态机用于减少信号冲突，不用于预测未来。
2. Market Regime 决定市场背景。
3. Dow Structure 决定结构方向。
4. Breakout 决定突破质量和真假突破风险。
5. Signal 决定信号顺序和冷却。
6. Exit 决定风险警示和离场参考。
7. 结构失效优先级高于新增入场信号。
8. warning 不能直接改变为反向入场信号。
9. 状态切换必须基于 confirmed pivot、bar close confirmation 或明确过滤条件。
10. RANGE 状态默认压制 LONG / SHORT 主信号。
11. TRANSITION 状态只允许轻量观察，不允许高置信 LONG / SHORT 主信号。

## 状态机优先级

当多个状态机给出不同提示时，按以下顺序解释：

1. Exit State Machine
2. Dow Structure State Machine
3. Market Regime State Machine
4. Breakout State Machine
5. Signal State Machine

优先级说明：

- Exit 负责风险与离场，必须优先。
- Dow Structure 负责核心结构，不允许被单根动能信号覆盖。
- Market Regime 负责背景过滤。
- Breakout 负责局部事件。
- Signal 只在前面状态允许时输出参考。

## 1. Market Regime 行情状态机

### 状态名称

- neutral
- up_trend
- down_trend
- range
- transition
- exhaustion

### 进入条件

- neutral：结构、趋势和动能尚未形成清晰方向。
- up_trend：HH / HL 偏多，价格主要位于 EMA20 上方，EMA10 >= EMA20，MACD 不明显空头扩张。
- down_trend：LH / LL 偏空，价格主要位于 EMA20 下方，EMA10 <= EMA20，MACD 不明显多头扩张。
- range：价格反复穿越 EMA20，Bollinger Band 宽度收窄，MACD 靠近零轴，高低点结构不清晰。
- transition：原趋势结构失效，或价格、均线、MACD 与道氏结构发生分歧，新趋势尚未确认。
- exhaustion：趋势后期出现动能减弱、实体缩小、影线放大，或价格创新高 / 新低但动能没有同步增强。

### 退出条件

- neutral 在 confirmed swing 和趋势过滤形成方向后退出。
- up_trend 在多头结构失效或进入衰竭后退出。
- down_trend 在空头结构失效或进入衰竭后退出。
- range 在有效突破或新结构确认后退出。
- transition 在新方向结构确认后退出。
- exhaustion 在趋势恢复、结构失效或进入离场状态后退出。

### 失效条件

- up_trend：close 跌破最近 confirmed swing low。
- down_trend：close 突破最近 confirmed swing high。
- range：Breakout Score 达到有效突破阈值，且突破后不快速回到区间。
- transition：新方向结构无法确认，重新回到 range 或 neutral。
- exhaustion：动能恢复并进入 continuation。

### 图面显示

- Dashboard 显示 Regime。
- 主图可通过背景、状态文字或轻量标签提示 Regime。
- RANGE 和 TRANSITION 应避免过强视觉暗示。

### 对信号的影响

- up_trend 优先允许 LONG、PB-L、BO-L。
- down_trend 优先允许 SHORT、PB-S、BO-S。
- range 降低 LONG / SHORT 权重，重点观察 Range High / Range Low。
- transition 只允许轻量观察，例如 long_watch、short_watch、breakout_attempt 或 warning；不允许高置信 LONG / SHORT 主信号。
- exhaustion 优先输出 EXH-L / EXH-S 或等待 XL / XS。

## 2. Dow Structure 道氏结构状态机

### 状态名称

- no_structure
- bullish_structure
- bearish_structure
- bullish_invalidated
- bearish_invalidated
- transition_structure

### 进入条件

- no_structure：confirmed swing 数量不足，或 HH / HL / LH / LL 无法形成有效序列。
- bullish_structure：形成 HH + HL，多头结构成立。
- bearish_structure：形成 LH + LL，空头结构成立。
- bullish_invalidated：上涨结构中 close 跌破最近 confirmed swing low。
- bearish_invalidated：下跌结构中 close 突破最近 confirmed swing high。
- transition_structure：原结构失效后，新方向结构尚未完整确认。

### 退出条件

- no_structure 在出现足够 confirmed swing 后退出。
- bullish_structure 在跌破结构失效位后退出。
- bearish_structure 在突破结构失效位后退出。
- bullish_invalidated 在形成 bearish_structure、transition_structure 或 no_structure 后退出。
- bearish_invalidated 在形成 bullish_structure、transition_structure 或 no_structure 后退出。
- transition_structure 在新方向结构确认或重新混乱后退出。

### 失效条件

- bullish_structure 的失效条件是 close 跌破最近 confirmed swing low。
- bearish_structure 的失效条件是 close 突破最近 confirmed swing high。
- transition_structure 的失效条件是无法形成新结构，回到 no_structure 或 range。

### 图面显示

- 主图显示 HH / HL / LH / LL。
- BOS / CHoCH 只在结构确认后显示。
- ZC-L / ZC-S 必须与结构转折或区域确认相关。

### 对信号的影响

- bullish_structure 支持 LONG、PB-L、BO-L。
- bearish_structure 支持 SHORT、PB-S、BO-S。
- bullish_invalidated 支持 XL。
- bearish_invalidated 支持 XS。
- no_structure 和 transition_structure 压制主信号，只允许轻量观察或等待确认。

## 3. Breakout 突破状态机

### 状态名称

- no_breakout
- breakout_attempt
- breakout_confirmed
- breakout_failed
- retest
- continuation

### 进入条件

- no_breakout：价格未接近或突破关键位。
- breakout_attempt：价格接近或盘中突破 confirmed high、confirmed low、range high 或 range low。
- breakout_confirmed：收盘突破关键位，突破距离超过 ATR buffer，Breakout Score >= 60。
- breakout_failed：突破后快速回到原区间，或 Breakout Score 降到弱突破区间。
- retest：有效突破后回踩或反抽原关键位。
- continuation：retest 后价格继续沿突破方向运行，且动能未明显反向。

### 退出条件

- no_breakout 在接近关键位后进入 breakout_attempt。
- breakout_attempt 在收盘确认后进入 breakout_confirmed，或失败后回到 no_breakout。
- breakout_confirmed 在回踩后进入 retest，延续后进入 continuation，失败后进入 breakout_failed。
- breakout_failed 在回到 range、transition 或新结构确认后退出。
- retest 在确认延续或失败后退出。
- continuation 在动能衰竭、结构失效或新关键位形成后退出。

### 失效条件

- BO-L 后 close 回到原 range high 下方。
- BO-S 后 close 回到原 range low 上方。
- 突破 K 线实体不足且后续无法延续。
- MACD 不再同向或快速转弱。
- Bollinger Band 未扩张且价格回到区间。

### 图面显示

- BO-L / BO-S 使用突破标签。
- Breakout Score 显示在 Dashboard。
- failed 状态可作为风险提示，不应过度占用图面。

### 对信号的影响

- breakout_confirmed 允许 BO-L / BO-S，但必须由 Breakout Score 和 bar close confirmation 共同确认。
- breakout_failed 支持 XL / XS 或假突破风险提示。
- retest 支持 PB-L / PB-S。
- continuation 支持趋势延续判断，但不应频繁重复主信号。

## 4. Signal 信号状态机

### 状态名称

- flat
- long_watch
- long_active
- long_exit
- short_watch
- short_active
- short_exit

### 进入条件

- flat：没有有效入场参考、观察参考或离场参考。
- long_watch：多头结构、行情状态或区域位置支持观察，但尚未满足 LONG、PB-L 或 BO-L；TRANSITION 中最多只能进入该观察状态。
- long_active：LONG、PB-L 或 BO-L 满足主参考条件。
- long_exit：XL 条件出现，或多头结构失效。
- short_watch：空头结构、行情状态或区域位置支持观察，但尚未满足 SHORT、PB-S 或 BO-S；TRANSITION 中最多只能进入该观察状态。
- short_active：SHORT、PB-S 或 BO-S 满足主参考条件。
- short_exit：XS 条件出现，或空头结构失效。

### 退出条件

- watch 状态在条件消失后回到 flat。
- active 状态在离场信号出现后进入 exit。
- exit 完成后回到 flat。
- exit 后若形成相反方向结构，只能先进入相反方向 watch。

### 失效条件

- long_active 中 close 跌破最近 confirmed swing low。
- short_active 中 close 突破最近 confirmed swing high。
- 信号冷却周期未满足时，不允许重复进入 active。
- RANGE 状态下 active 信号必须更严格。
- TRANSITION 状态下不允许进入 long_active 或 short_active，除非方案文件未来明确改为允许。

### 图面显示

- 主图显示 LONG / SHORT / PB-L / PB-S / BO-L / BO-S / XL / XS。
- Dashboard 显示 Trade Bias 和 Risk State。
- 同一方向重复信号应被抑制。

### 对信号的影响

- 控制信号顺序。
- 避免 LONG 和 SHORT 同时出现。
- 避免 active 状态内重复刷同类信号。
- exit 状态优先于新增入场信号。

## 5. Exit 离场状态机

### 状态名称

- no_exit
- warning
- partial_exit
- full_exit

### 进入条件

- no_exit：没有离场或衰竭迹象。
- warning：出现 EXH-L 或 EXH-S。
- partial_exit：趋势仍未完全失效，但动能减弱、突破失败、价格接近 Target Zone 或出现衰竭迹象。
- full_exit：结构失效，XL 或 XS 条件成立。

### 退出条件

- warning 后趋势恢复并继续延续，回到 no_exit。
- warning 后风险扩大，进入 partial_exit。
- partial_exit 后结构恢复，回到 no_exit 或 warning。
- partial_exit 后结构失效，进入 full_exit。
- full_exit 后 Signal State 回到 flat。

### 失效条件

- EXH-L 后价格继续创新高且 MACD 动能增强。
- EXH-S 后价格继续创新低且 MACD 空头动能增强。
- partial_exit 后价格重新进入 continuation。
- full_exit 后不得维持原 active 状态。

### 图面显示

- EXH-L / EXH-S 使用警示视觉。
- XL / XS 使用明确离场标签。
- Risk State 在 Dashboard 中优先显示。

### 对信号的影响

- warning 不直接反向开仓。
- partial_exit 提醒减仓或保护利润。
- full_exit 优先于新增同向入场。
- full_exit 后必须等待新结构或新状态。

## 状态冲突处理

常见冲突处理规则：

- Market Regime 为 UP_TREND，但 Dow Structure 失效：优先按结构失效处理，禁止新增 LONG。
- Market Regime 为 DOWN_TREND，但 Dow Structure 失效：优先按结构失效处理，禁止新增 SHORT。
- Breakout confirmed，但 Breakout Score 后续快速下降：进入 breakout_failed。
- EXH-L 出现但多头结构未失效：只提示 warning，不输出 SHORT。
- EXH-S 出现但空头结构未失效：只提示 warning，不输出 LONG。
- RANGE 中突破未确认：不输出 BO-L / BO-S，只进入 breakout_attempt。
- TRANSITION 中结构未确认：不输出高置信 LONG / SHORT，只允许 watch、warning 或 breakout_attempt。
- TRANSITION 中出现单向动能增强：仍需等待 confirmed swing、bar close confirmation 和状态退出后再输出主信号。
- BO-L 与 BO-S 同时满足局部条件：视为冲突，不输出突破主信号，回到 breakout_attempt 或 range 观察。

## 状态验收标准

后续实现完成后，状态机需要满足：

- 状态名称稳定。
- 状态切换有清晰依据。
- 状态之间不互相矛盾。
- 图面显示与 Dashboard 一致。
- 信号必须受状态约束。
- 离场状态优先于新增入场状态。
- 震荡状态能明显减少信号。
