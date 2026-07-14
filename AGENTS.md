# DVCA Project Instructions

## 1. Project Purpose

本项目用于 DVCA 加密货币交易指标的长期开发、TradingView 图表分析、
交易执行研究、案例复盘和准确性验证。

主要目标：

1. 维护和迭代 DVCA Pine Script 指标。
2. 分析 BTC、ETH、SOL 等加密货币的多周期结构。
3. 建立 1H、30m、15m、5m、1m 多周期交易体系。
4. 记录有效信号、失败信号及 Outcome10、Outcome20、Outcome50。
5. 将研究结论转化为可验证、可执行的开发任务。

## 2. Language

默认使用中文。

代码变量、函数、文件名可以使用英文。
所有研究结论、任务说明和验收报告优先使用中文。

## 3. Source of Truth

正式文件优先级：

1. AGENTS.md
2. PROJECT_STATE.md
3. docs/decisions/decision_log.md
4. docs/specifications/
5. indicator/current/
6. docs/research/
7. cases/ 和 data/
8. legacy/

legacy/ 只作为迁移参考，不是当前正式版本。

不得在没有核对正式文件的情况下，直接使用 legacy/ 中的结论或代码。

## 4. Current Baseline

当前主版本基线为 DVCA v1.5.4。

v1.6.x 属于历史实验路线，不得自动恢复为主版本。

下一版本方向暂定为 v1.5.5 Accuracy Patch，但在完成专项验证之前，
不得直接修改或生成 v1.5.5 正式代码。

当前首先需要验证：

- 1H 和 30m 信号是否属于合理稀疏；
- 是否存在机制性滞后；
- Zone、结构确认和执行信号之间的延迟来源；
- 高周期与低周期信号是否一致；
- RANGE 和 TRANSITION 是否正确压制趋势信号。

## 5. Pine Script Rules

每次修改、修复或升级 Pine Script：

1. 必须提供完整、可直接复制到 TradingView 运行的代码。
2. 不得只提供局部补丁或替换片段。
3. 必须保留清楚的版本号。
4. 必须写明修改说明。
5. 必须写明兼容性说明。
6. 修改前必须检查旧版本逻辑。
7. 优先基于 v1.5.4 小步升级。
8. 不进行无必要的大规模重构。
9. 显示开关不得改变底层状态机。
10. 不得因为隐藏标签而改变候选、确认、失效或退出逻辑。

未经明确任务授权，不得修改 indicator/current/ 中的正式版本。

开发候选版本必须先保存到 indicator/candidates/。

通过验收后才能晋升到 indicator/current/。

## 6. Multi-Timeframe Framework

默认周期职责：

- 1H：市场背景、主要趋势和大级别风险。
- 30m：核心结构、趋势延续和潜在转折。
- 15m：执行环境和确认。
- 5m：主要执行触发。
- 1m：精细入场、加速确认和风险管理。

1m 不得单独决定交易方向。

低周期信号和高周期方向冲突时：

- 降低信号评分；
- 不作为高置信度交易；
- 明确标记冲突原因。

## 7. Signal Semantics

- L-ZONE、S-ZONE：观察区，不等于立即进场。
- LONG、SHORT、PB-L、PB-S：主要执行信号。
- EXH-L、EXH-S：衰竭警告，不直接等于反向入场。
- RANGE：压制趋势型 LONG 和 SHORT。
- TRANSITION：不开高置信度仓位。

必须区分：

- 信号出现；
- 信号确认；
- 信号失效；
- 信号过期。

必须记录：

- 已确认结构点；
- 结构确认时间；
- FT/PB 候选状态；
- FT/PB 确认状态；
- FT/PB 失效状态；
- FT/PB 过期状态。

## 8. Screenshot Analysis

分析 TradingView 截图时必须输出：

1. 多周期状态表。
2. 当前市场结构。
3. 信号链。
4. 支撑、阻力、触发线和失效位。
5. 多头与空头交易计划。
6. 入场、止损、目标和无效条件。
7. 信号评分和交易评分。
8. Outcome10、Outcome20、Outcome50 剧本。
9. 是否值得创建案例。
10. Follow-up 要求。
11. 给 Codex 的开发记录。
12. 最终结论：可操作、等待确认或禁止追单。

无法从截图准确读取的价格不得伪造。

## 9. Case Lifecycle

案例必须至少记录：

- Case ID
- 交易标的
- 周期
- 截图时间
- 市场状态
- 主要信号
- 信号链
- 入场触发条件
- 失效条件
- Outcome10
- Outcome20
- Outcome50
- 最终结果
- 案例评级
- 指标改进建议

案例评级：

- Gold Case
- Good Case
- Normal Case
- Failed Case

不得在 Outcome 数据尚未完成时提前认定最终案例评级。

## 10. Development Workflow

每个开发任务必须遵循：

1. 阅读 AGENTS.md。
2. 阅读 PROJECT_STATE.md。
3. 检查 decision_log.md。
4. 检查 current 主代码。
5. 检查相关研究和案例。
6. 写出问题归因。
7. 写出拟修改范围。
8. 写出验收标准。
9. 修改候选版本。
10. 执行静态检查和人工检查。
11. 更新 CHANGELOG.md。
12. 更新 PROJECT_STATE.md。
13. 更新任务状态。

不得绕过验证直接宣称问题已解决。

## 11. Safety and Trading Accuracy

不得因为图上出现 LONG 或 SHORT 标签就直接建议进场。

必须检查：

- 趋势；
- 结构；
- 位置；
- 成交量；
- 背离；
- 触发线；
- 多周期一致性；
- 信号是否过早；
- 是否属于震荡误判；
- 是否已经错过最佳入场；
- 止损距离；
- 盈亏比。

默认优先风险控制和避免追单。

## 12. File Protection

不得删除：

- legacy/
- indicator/archive/
- 原始截图；
- 已完成案例；
- 原始数据库。

迁移和整理时优先复制，不直接移动或覆盖。

发现冲突时应生成迁移报告，不得自行猜测哪一个版本正确。
