# Crypto Structure Trading Assistant 项目整体方案 v1

版本：v1.0
日期：2026-07-01
项目类型：TradingView Pine Script v5 交易观察指标
项目名称：crypto-structure-trading-assistant

---

## 一、项目目标

本项目的目标是根据技术分析学习资料，开发一个 TradingView Pine Script v5 指标。

该指标不是自动交易机器人，也不是预测涨跌的黑箱系统，而是一个结构型交易观察工具，用来辅助判断：

1. 当前行情状态；
2. 道氏高低点结构；
3. 多空趋势方向；
4. 关键做多区和做空区；
5. 突破质量；
6. 回踩与反抽机会；
7. LONG / SHORT 参考信号；
8. 止损失效条件；
9. 止盈和离场参考。

本项目的核心原则是：

```text
先结构，后信号。
先顺势，后反转。
先观察，后交易。
先稳定，后复杂。
先文档，后代码。
```

---

## 二、项目定位

本项目最终产物是：

```text
TradingView Pine Script v5 indicator
```

不是：

```text
自动下单机器人
自动回测策略
无条件买卖点系统
高频交易系统
```

第一版只做 `indicator()`，不做 `strategy()`。

等观察指标稳定后，后续版本才考虑策略回测。

---

## 三、学习资料来源与核心思想

学习资料主要包括：

1. 技术分析核心原则；
2. 趋势判断；
3. 道氏理论；
4. 趋势线；
5. 趋势通道；
6. 均线；
7. 布林通道；
8. MACD；
9. 单根 K 线；
10. K 线组合；
11. 反转形态；
12. 中继形态；
13. 突破确认；
14. 止损止盈；
15. 盘感训练；
16. 实战检查清单。

学习资料的核心思想是：技术分析不是预测绝对结果，而是在价格图表中识别更高概率的方向、位置和交易条件。

因此，本项目不能把任何单一信号当成买卖命令，而应该建立一个综合判断系统。

---

## 四、资料内容的代码化分类

### 1. 可以直接量化的内容

这些内容可以直接写进 Pine Script：

```text
道氏高低点
HH / HL / LH / LL
均线排列
布林通道
MACD 状态
ATR 波动过滤
收盘突破
2% 突破规则
K线实体大小
突破后是否回到区间
```

### 2. 可以半量化的内容

这些内容可以转成评分、过滤器或 warning：

```text
K线组合
中继形态
反转雏形
趋势衰竭
假突破风险
```

### 3. 不适合直接自动化的内容

这些内容不应该直接做成买卖信号：

```text
盘感
主观画线
复杂头肩形
复杂 W / M 形态
圆弧形
完整楔形判断
```

盘感只能作为辅助提醒，不能替代客观规则。

---

## 五、指标整体架构

指标采用七层结构：

```text
行情状态层
↓
道氏结构层
↓
趋势过滤层
↓
区域判断层
↓
突破评分层
↓
信号输出层
↓
止损止盈辅助层
```

---

## 六、行情状态层

行情状态分为：

```text
UP_TREND      上升趋势
DOWN_TREND    下降趋势
RANGE         横盘震荡
TRANSITION    趋势切换中
EXHAUSTION    趋势衰竭
```

判断依据：

```text
Swing High / Swing Low
HH / HL / LH / LL
EMA 位置
MACD 动能
布林带宽
ATR 波动状态
```

---

## 七、道氏结构层

指标需要自动识别：

```text
HH = Higher High，更高高点
HL = Higher Low，更高低点
LH = Lower High，更低高点
LL = Lower Low，更低低点
```

结构判断：

```text
HH + HL = 多头结构
LH + LL = 空头结构
高低点混乱 = 震荡或过渡结构
```

关键变量：

```text
lastConfirmedHigh
lastConfirmedLow
lastBullishInvalidation
lastBearishInvalidation
```

结构失效规则：

```text
上涨结构中，如果 close 跌破最近 confirmed swing low，则上涨结构失效。

下跌结构中，如果 close 突破最近 confirmed swing high，则下跌结构失效。
```

---

## 八、趋势过滤层

使用以下工具过滤低质量信号：

```text
EMA 5 / 10 / 20 / 40 / 60
Bollinger Band 20, 2
MACD 12, 26, 9
ATR 14
```

多头过滤：

```text
close > EMA20
EMA10 >= EMA20
MACD 不明显空头扩张
close 位于布林中轨上方或重新收回中轨
```

空头过滤：

```text
close < EMA20
EMA10 <= EMA20
MACD 不明显多头扩张
close 位于布林中轨下方或重新跌破中轨
```

震荡过滤：

```text
价格反复穿越 EMA20
布林带宽收窄
MACD 靠近零轴
高低点结构不清晰
```

---

## 九、区域判断层

指标必须画区域，而不是只画箭头。

核心区域：

```text
L-ZONE = 潜在做多区
S-ZONE = 潜在做空区
Range High = 震荡上沿
Range Low = 震荡下沿
Stop Zone = 结构失效区
Target Zone = 目标参考区
```

区域作用：

```text
L-ZONE 用于观察回踩做多。
S-ZONE 用于观察反抽做空。
Range High / Range Low 用于判断突破。
Stop Zone 用于判断信号失效。
Target Zone 用于辅助止盈。
```

---

## 十、突破评分层

突破不能只用简单的 `close > high` 或 `close < low` 判断。

应使用 Breakout Score。

突破评分因素：

```text
收盘突破关键位
突破距离超过 ATR buffer
BTC / ETH 60m 可参考 2% 原则
突破 K 线实体放大
MACD 同向扩张
布林带宽扩大
突破后没有快速回到原区间
```

评分解释：

```text
0 - 30：弱突破，假突破风险高
31 - 60：普通突破
61 - 80：有效突破
81 - 100：强突破
```

默认：

```text
Breakout Score >= 60 才允许 BO-L / BO-S 信号。
```

---

## 十一、信号输出层

第一版保留以下信号：

```text
LONG
SHORT
PB-L
PB-S
BO-L
BO-S
EXH-L
EXH-S
XL
XS
```

### LONG

含义：多头入场参考。

条件：

```text
Market Regime 为 UP_TREND 或 TRANSITION_TO_UP
道氏结构偏多
close > EMA20
EMA10 >= EMA20
MACD 不明显空头扩张
价格靠近 L-ZONE 或完成有效向上突破
未处于强震荡过滤状态
满足信号冷却周期
```

### SHORT

含义：空头入场参考。

条件：

```text
Market Regime 为 DOWN_TREND 或 TRANSITION_TO_DOWN
道氏结构偏空
close < EMA20
EMA10 <= EMA20
MACD 不明显多头扩张
价格靠近 S-ZONE 或完成有效向下跌破
未处于强震荡过滤状态
满足信号冷却周期
```

### PB-L

含义：上升趋势中的回踩做多观察。

条件：

```text
上升趋势中
价格回踩 EMA20、布林中轨或 L-ZONE
没有跌破最近 confirmed swing low
出现重新转强 K 线
MACD 不明显转空
```

### PB-S

含义：下降趋势中的反抽做空观察。

条件：

```text
下降趋势中
价格反抽 EMA20、布林中轨或 S-ZONE
没有突破最近 confirmed swing high
出现重新转弱 K 线
MACD 不明显转多
```

### BO-L

含义：向上有效突破。

条件：

```text
close 突破最近 confirmed high 或 range high
突破距离超过 ATR buffer
Breakout Score >= 默认阈值
MACD 同向
突破 K 线实体放大
```

### BO-S

含义：向下有效跌破。

条件：

```text
close 跌破最近 confirmed low 或 range low
跌破距离超过 ATR buffer
Breakout Score >= 默认阈值
MACD 同向
跌破 K 线实体放大
```

### EXH-L

含义：多头衰竭警示。

出现条件：

```text
上涨趋势后期
价格接近上方阻力或布林上轨
出现长上影线或实体缩小
MACD 动能减弱
价格创新高但动能没有同步增强
```

EXH-L 不是做空信号，只是多头减仓或警惕信号。

### EXH-S

含义：空头衰竭警示。

出现条件：

```text
下跌趋势后期
价格接近下方支撑或布林下轨
出现长下影线或实体缩小
MACD 空头动能减弱
价格创新低但动能没有同步增强
```

EXH-S 不是做多信号，只是空头减仓或警惕信号。

### XL

含义：多单离场参考。

条件：

```text
多头结构失效
close 跌破最近 confirmed swing low
close 跌破 EMA20 且 MACD 转弱
出现 EXH-L 后价格无法继续新高
突破失败并回到原区间
```

### XS

含义：空单离场参考。

条件：

```text
空头结构失效
close 突破最近 confirmed swing high
close 突破 EMA20 且 MACD 转强
出现 EXH-S 后价格无法继续新低
跌破失败并回到原区间
```

---

## 十二、状态机设计

项目必须包含五个状态机：

```text
Market Regime State Machine
Dow Structure State Machine
Breakout State Machine
Signal State Machine
Exit State Machine
```

### 1. Market Regime State Machine

状态：

```text
neutral
up_trend
down_trend
range
transition
exhaustion
```

用途：

```text
决定当前市场背景。
过滤不适合的交易方向。
减少震荡区假信号。
```

### 2. Dow Structure State Machine

状态：

```text
no_structure
bullish_structure
bearish_structure
bullish_invalidated
bearish_invalidated
transition_structure
```

用途：

```text
判断趋势结构是否成立。
判断结构是否失效。
决定 BOS / CHoCH / ZC-L / ZC-S。
```

### 3. Breakout State Machine

状态：

```text
no_breakout
breakout_attempt
breakout_confirmed
breakout_failed
retest
continuation
```

用途：

```text
判断真突破、假突破、突破后回抽和突破后延续。
```

### 4. Signal State Machine

状态：

```text
flat
long_watch
long_active
long_exit
short_watch
short_active
short_exit
```

用途：

```text
避免重复信号。
让 LONG / SHORT / PB / BO / XL / XS 有顺序。
```

### 5. Exit State Machine

状态：

```text
no_exit
warning
partial_exit
full_exit
```

用途：

```text
辅助止盈和离场。
避免过早离场或无规则持仓。
```

---

## 十三、视觉设计

主图显示：

```text
EMA 5 / 10 / 20 / 40 / 60
Bollinger 上轨 / 中轨 / 下轨
Swing High / Swing Low
HH / HL / LH / LL
L-ZONE / S-ZONE
BOS / CHoCH
LONG / SHORT
PB-L / PB-S
BO-L / BO-S
EXH-L / EXH-S
XL / XS
```

Dashboard 显示：

```text
Regime
Structure
Momentum
Volatility
Breakout Score
Trade Bias
Risk State
```

视觉语言：

```text
绿色 = 多头
红色 = 空头
黄色 = 观察 / 警示
灰色 = 震荡 / 等待
蓝色 = 突破
紫色 = 衰竭
```

---

## 十四、项目文件结构

项目结构：

```text
crypto-structure-trading-assistant/
├── AGENTS.md
├── README.md
├── docs/
│   ├── project_plan_v1.md
│   ├── source_summary.md
│   ├── indicator_spec_v1.md
│   ├── signal_rules_v1.md
│   ├── state_machine_v1.md
│   ├── visual_design_v1.md
│   ├── test_plan_v1.md
│   ├── validation_plan.md
│   ├── changelog.md
│   └── playbook/
│       ├── multi_timeframe_playbook.md
│       ├── long_setup.md
│       ├── short_setup.md
│       ├── trend_day.md
│       ├── reversal_day.md
│       └── execution_checklist.md
├── pine/
│   ├── crypto_structure_trading_assistant_v1.pine
│   └── archive/
├── screenshots/
│   └── README.md
└── prompts/
    ├── 01_build_project.md
    ├── 02_write_spec.md
    ├── 03_write_state_machine.md
    ├── 04_write_pine.md
    ├── 05_self_check.md
    └── 06_fix_errors.md
```

---

## 十五、版本路线

当前项目路线升级为：

```text
DVCA Specification
↓
DVCA Validation
↓
DVCA Statistics
↓
DVCA Research Report
↓
DVCA Pine
```

说明：

```text
v0.1 - v0.3 属于 Specification 阶段。
v0.3.5 属于 Research Validation 阶段。
v0.4 以后才允许进入 Pine 开发阶段。
```

在 v0.3.5 验证完成前，不建议直接进入 v0.4。

### v0.1：项目文档版

目标：

```text
创建项目结构。
写入 AGENTS.md。
写入 README.md。
保存 project_plan_v1.md。
整理 source_summary.md。
```

不写 Pine 代码。

### v0.2：规则文档版

目标：

```text
完善 indicator_spec_v1.md。
完善 signal_rules_v1.md。
完善 visual_design_v1.md。
完善 test_plan_v1.md。
```

不写 Pine 代码。

### v0.3：状态机版

目标：

```text
完善 state_machine_v1.md。
明确 Market Regime、Dow Structure、Breakout、Signal、Exit 五个状态机。
```

不写 Pine 代码。

### v0.3.5：Research Validation Phase

目标：

```text
冻结 indicator_spec、signal_rules、state_machine 的核心设计。
建立 validation_plan.md。
收集至少 100 个标准化案例。
统计 LONG、SHORT、PB、BO、EXH、XL、XS 等信号表现。
验证 Breakout Score 默认阈值是否合理。
验证不同市场和周期下的信号差异。
形成 Research Report 后，再决定是否进入 Pine 基础实现。
```

要求：

```text
不写 Pine 代码。
不急于修改规则参数。
不根据少量案例推翻状态机。
以案例数据库和统计结果驱动后续实现。
```

### v0.4：Pine 基础版

目标：

```text
写第一版 Pine Script v5。
包含 EMA、Bollinger、MACD、ATR、Swing High / Low、Dashboard。
```

进入条件：

```text
v0.3.5 Research Validation 完成。
至少 100 个标准化案例完成记录。
关键阈值有统计依据。
Research Report 已确认哪些规则可以进入 Pine。
```

暂时不追求复杂买卖信号。

### v0.5：结构识别版

新增：

```text
HH / HL / LH / LL
BOS
CHoCH
Market Regime
L-ZONE / S-ZONE
```

### v0.6：交易信号版

新增：

```text
LONG
SHORT
PB-L
PB-S
BO-L
BO-S
EXH-L
EXH-S
XL
XS
```

### v0.7：准确性过滤版

新增：

```text
ATR buffer
假突破过滤
信号冷却周期
震荡过滤
bar close confirmation
no repaint 检查
```

### v1.0：正式观察版

目标：

```text
图面稳定
信号不过密
结构判断清楚
适合 BTC / ETH / SOL
适合 15m / 1h / 4h / 1D
```

---

## 十六、测试计划

必须测试：

```text
Pine v5 是否能编译
是否有 undeclared identifier
是否有 line continuation 错误
是否有 repaint 风险
是否使用 confirmed pivot
是否避免 lookahead_on
是否信号过密
是否 label / line / box 超限
Dashboard 是否正常
alertcondition 是否正常
```

测试市场：

```text
BTCUSDT 15m
BTCUSDT 1h
BTCUSDT 4h
ETHUSDT 1h
SOLUSDT 1h
```

测试场景：

```text
强上涨趋势
强下跌趋势
横盘震荡
真突破
假突破
趋势反转
高波动插针
```

---

## 十七、Codex 使用原则

不能一次性让 Codex 完成全部任务。

正确顺序：

```text
第一步：初始化项目结构
第二步：保存 project_plan_v1.md
第三步：完善规则文档
第四步：完善状态机文档
第五步：进入 Research Validation
第六步：收集标准化案例
第七步：完成统计分析
第八步：输出 Research Report
第九步：再写 Pine Script
第十步：TradingView 编译
第十一步：根据报错修完整代码
第十二步：记录 changelog
第十三步：小版本迭代
```

每次让 Codex 修改代码时，必须要求：

```text
输出完整 Pine Script 文件。
不要只输出 patch。
不要只输出替换片段。
```

---

## 十八、重要开发纪律

1. 不要用未确认 pivot 发信号。
2. 不要在震荡区频繁报 LONG / SHORT。
3. 不要把 MACD 金叉死叉当买卖命令。
4. 不要过早做反转。
5. 不要让图面太乱。
6. 不要让止损脱离入场依据。
7. 不要第一版就做 strategy 回测。
8. 不要用大重构解决小问题。
9. 每个版本只解决一类问题。
10. 所有信号必须有失效条件。
11. 在 Research Validation 完成前，不要急于进入 Pine 实现。
12. 规则阈值优先由案例统计验证，而不是只凭主观判断确定。

---

## 十九、最终成品目标

最终指标应该能回答：

```text
当前是上涨、下跌、震荡还是过渡？
当前结构是多头、空头还是混乱？
价格是否接近 L-ZONE / S-ZONE？
突破是真突破还是假突破风险？
现在适合 LONG、SHORT、等待、减仓还是离场？
如果进场，结构失效在哪里？
如果持仓，哪里应该减仓或退出？
```

最终项目应该包含：

```text
完整项目说明
完整指标规格
完整信号规则
完整状态机
完整视觉设计
完整测试计划
完整验证计划
完整执行手册
完整研究报告
完整统计记录
完整 Pine Script 指标
每次修改记录
历史版本归档
测试截图
```

---

## 二十、项目总原则

```text
先文档，后代码。
先结构，后信号。
先顺势，后反转。
先观察，后交易。
先稳定，后复杂。
先验证，后实现。
```

本项目第一阶段的目标不是写出最复杂的指标，也不是尽快写出 Pine，而是写出一个结构清楚、信号稳定、经过案例验证、可以长期迭代的交易观察系统。
