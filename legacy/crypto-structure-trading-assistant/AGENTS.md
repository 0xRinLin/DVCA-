# AGENTS.md

## 项目名称

Crypto Structure Trading Assistant

## 默认语言

本项目默认使用中文。

所有项目文档、说明、注释、变更记录、测试记录、提示词，默认使用中文。

以下内容可以保留英文：

- Pine Script 代码本身
- 文件名
- 变量名
- 函数名
- TradingView 固定术语
- EMA、MACD、ATR、Bollinger Band、Swing High、Swing Low 等技术名词
- LONG、SHORT、PB-L、PB-S、BO-L、BO-S、EXH-L、EXH-S、XL、XS 等信号名称

## 最高优先级方案文件

本项目最高优先级方案文件是：

docs/project_plan_v1.md

所有重要项目变更都必须先更新 docs/project_plan_v1.md。

如果用户需求与 docs/project_plan_v1.md 冲突，不要直接改代码。必须先说明该需求需要更新项目方案。

## 项目目标

开发一个 TradingView Pine Script v5 指标，名称为 Crypto Structure Trading Assistant。

该指标是结构型交易观察辅助工具，不是自动交易机器人，也不是黑箱预测系统。

## 开发原则

1. 先方案，后代码。
2. 先文档，后实现。
3. 先结构，后信号。
4. 先顺势，后反转。
5. 先观察，后交易。
6. 先稳定，后复杂。
7. 所有信号必须有失效条件。
8. 不更新 docs/project_plan_v1.md，不允许改变项目方向。
9. 项目默认中文输出。
10. 在 Research Validation 完成前，不要进入 Pine 正式实现。
11. 规则阈值应优先由案例统计验证，而不是只凭主观判断确定。

## Pine Script 规则

- 使用 Pine Script v5。
- v1 版本必须使用 indicator()，不要使用 strategy()。
- overlay = true。
- 不要使用 lookahead_on。
- 使用 confirmed pivots。
- 避免 repaint。
- 尽量使用 bar close confirmation。
- 使用 ATR buffer 过滤噪声。
- 避免信号过密。
- 避免 label / line / box 超限。
- 代码结构要模块化、可读。
- 代码注释优先使用中文。

## 必须保留的视觉语言

除非先更新 docs/project_plan_v1.md，否则必须保留以下标签和概念：

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

## 目标模块

项目最终需要包含：

1. 输入参数模块
2. EMA 模块
3. Bollinger Band 模块
4. MACD 模块
5. ATR 模块
6. Swing High / Swing Low 模块
7. HH / HL / LH / LL 模块
8. Dow Structure 道氏结构模块
9. Market Regime 行情状态模块
10. L-ZONE / S-ZONE 区域模块
11. Breakout Score 突破评分模块
12. Entry Signals 入场参考信号模块
13. Exit Signals 离场参考信号模块
14. Dashboard 状态面板模块
15. Alertcondition 警报模块

## 变更控制

在修改任何重要功能、信号、状态机、视觉设计或版本路线之前，必须：

1. 更新 docs/project_plan_v1.md。
2. 更新受影响的 docs 文件。
3. 在方案和文档一致后，再修改 Pine Script。
4. 更新 docs/changelog.md。

## Research Validation 规则

当前项目在 v0.3.5 阶段必须先进行 Research Validation。

进入 Pine 实现前，需要：

1. 完成 `docs/validation_plan.md` 中定义的标准化案例验证。
2. 收集至少 100 个案例。
3. 统计 LONG、SHORT、PB、BO、EXH、XL、XS 等信号表现。
4. 验证 Breakout Score 阈值。
5. 输出 Research Report。
6. 如统计结论改变方案，先更新 `docs/project_plan_v1.md`。

## 输出要求

修改 Pine Script 时，必须输出完整的新 Pine Script 文件。

不要只输出 patch。
不要只输出替换片段。
不要在没有方案依据的情况下进行大重构。
