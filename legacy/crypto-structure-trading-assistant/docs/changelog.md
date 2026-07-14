# 变更记录

## v0.3.5

- 根据项目方向升级，进入 Research Validation Phase。
- 更新 `docs/project_plan_v1.md`，将路线从“直接进入 v0.4 Pine”调整为“先验证、后实现”。
- 新增 `docs/validation_plan.md`。
- 明确 v0.3.5 阶段需要冻结核心规则设计，收集至少 100 个标准化案例。
- 明确需要统计 LONG、SHORT、PB、BO、EXH、XL、XS 等信号表现。
- 明确 Breakout Score 默认阈值需要通过 55、60、65、70 等分档统计验证。
- 明确 v0.4 Pine 基础版必须等待 Research Report 和统计结论后再进入。
- 更新 README 的版本路线和当前阶段说明。
- 更新 AGENTS.md，加入 Research Validation 前置规则。
- 更新 `prompts/05_write_pine.md`，防止绕过验证直接写 Pine。
- 更新 `docs/test_plan_v1.md`，明确 TradingView 测试前置条件。
- 本次未写 Pine Script 正式代码。

## v0.3.1

- 根据方案优先规则，更新 `docs/project_plan_v1.md` 的项目文件结构。
- 新增 `docs/playbook/` 实战手册目录。
- 新增多周期观察手册。
- 新增多头 Setup 手册。
- 新增空头 Setup 手册。
- 新增趋势日观察手册。
- 新增反转日观察手册。
- 新增执行检查清单。
- 本次只新增和完善中文文档，未写 Pine Script 正式代码。

## v0.3.0

- 进入状态机确认版，重点检查信号互斥、状态约束和测试验收标准。
- 明确 LONG / SHORT、PB-L / PB-S、BO-L / BO-S 的互斥要求。
- 明确 RANGE 状态默认压制 LONG / SHORT。
- 明确 TRANSITION 状态只允许轻量观察，不允许高置信 LONG / SHORT 主信号。
- 明确 BO-L / BO-S 必须由 Breakout Score 决定，默认阈值为 60。
- 补充 bar close confirmation 对结构、突破和失效信号的要求。
- 补充状态机冲突处理规则和测试计划中的 v0.3 验收项。
- 未修改 docs/project_plan_v1.md。
- 未修改 Pine Script，占位文件仍未开始正式实现。

## v0.2.0

- 根据 `docs/project_plan_v1.md` 完善所有中文规则文档。
- 完善学习资料摘要与代码化分类。
- 完善指标规格文档，补充模块职责、状态边界和 Dashboard 规则。
- 完善信号规则文档，补充信号优先级、互斥原则、冷却原则和验收标准。
- 完善状态机文档，补充状态机优先级、冲突处理和状态验收标准。
- 完善视觉设计文档，补充视觉层级、密度控制和图面验收标准。
- 完善测试计划文档，补充状态机冲突检查、测试记录要求和通过标准。
- 未修改 Pine Script，占位文件仍未开始正式实现。

## v0.1.0

- 初始化项目结构。
- 新增 docs/project_plan_v1.md，并将其设为项目最高优先级方案文件。
- 新增 AGENTS.md 项目规则。
- 新增 README.md。
- 新增学习资料摘要文档。
- 新增指标规格文档。
- 新增信号规则文档。
- 新增状态机文档。
- 新增视觉设计文档。
- 新增测试计划文档。
- 明确项目默认语言为中文。
- Pine Script 正式实现尚未开始。
