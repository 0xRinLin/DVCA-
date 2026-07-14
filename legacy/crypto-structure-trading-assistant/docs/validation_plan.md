# Research Validation Plan

本文根据 `docs/project_plan_v1.md` 创建，用于定义 v0.3.5 Research Validation Phase 的验证目标、案例标准、统计口径和进入 Pine 开发前的通过标准。本文件不包含 Pine 代码。

## 阶段定位

v0.3.5 不是 Pine 开发阶段，而是 Research Validation 阶段。

本阶段目标是把当前 `indicator_spec`、`signal_rules`、`state_machine` 和 `playbook` 暂时冻结，用真实图表案例验证规则是否稳定、阈值是否合理、信号是否值得进入 Pine 实现。

## 核心判断

当前项目不应直接进入 v0.4 Pine 基础指标版。

原因：

1. 规则已经较完整，但缺少案例验证。
2. Breakout Score 默认阈值 60 还没有统计依据。
3. LONG / SHORT / PB / BO / EXH / XL / XS 的表现需要按市场和周期拆开验证。
4. 如果现在直接写 Pine，后续会因为规则和阈值反复变化而频繁重写。
5. 项目目标已经升级为有理论、有案例、有统计支撑的 DVCA 2.0，而不是只写一个能运行的指标。

## Research Freeze

验证期内默认冻结以下文件的核心设计：

- `docs/indicator_spec_v1.md`
- `docs/signal_rules_v1.md`
- `docs/state_machine_v1.md`
- `docs/visual_design_v1.md`
- `docs/playbook/`

冻结含义：

- 不轻易改变信号名称。
- 不轻易改变状态机名称。
- 不根据少数案例修改阈值。
- 不提前进入 Pine 实现。
- 所有规则调整都必须有案例或统计依据。

允许变更：

- 修正文档中的明显矛盾。
- 增加案例记录字段。
- 增加统计分类。
- 补充验证口径。

## 项目分层

当前项目体系升级为：

```text
DVCA Project
├── DVCA Research
├── DVCA Specification
├── DVCA Validation
├── DVCA Statistics
└── DVCA Pine
```

职责说明：

- DVCA Research：沉淀案例、图表、信号研究和交易观察经验。
- DVCA Specification：定义指标规格、信号规则、状态机和视觉设计。
- DVCA Validation：验证规则是否可靠。
- DVCA Statistics：统计不同信号、市场、周期和场景表现。
- DVCA Pine：把已验证的规则翻译成 Pine Script。

## 验证样本目标

第一轮最低目标：

```text
100 个标准化案例
```

建议样本分布：

- BTCUSDT：不少于 35 个案例。
- ETHUSDT：不少于 25 个案例。
- SOLUSDT：不少于 20 个案例。
- 其他高流动性交易对：不少于 20 个案例。

周期分布：

- 15m：不少于 20 个案例。
- 1h：不少于 40 个案例。
- 4h：不少于 30 个案例。
- 1D：不少于 10 个案例。

市场场景分布：

- 强上涨趋势
- 强下跌趋势
- 横盘震荡
- 真突破
- 假突破
- 趋势反转
- 高波动插针

## 案例记录字段

每个案例至少记录：

- case_id
- 日期
- 交易对
- 周期
- 市场场景
- Market Regime
- Dow Structure
- Breakout State
- Signal State
- Exit State
- 信号类型
- 是否在 RANGE
- 是否在 TRANSITION
- 是否使用 confirmed pivot
- 是否满足 bar close confirmation
- Breakout Score
- ATR buffer 是否通过
- MACD 状态
- Bollinger Band 状态
- L-ZONE / S-ZONE 位置
- 结构失效位
- 信号后最大有利波动
- 信号后最大不利波动
- 是否触发失效条件
- 是否出现 EXH
- 是否出现 XL / XS
- 结果分类
- 截图文件名
- 复盘备注

## 结果分类

建议使用以下结果标签：

- success：信号方向和结构延续一致。
- partial_success：方向正确，但空间不足或很快进入风险状态。
- failed：信号后较快触发失效条件。
- invalid_setup：不符合规则，不应计入有效信号。
- warning_only：只属于 EXH 或风险提示。
- exit_only：只属于 XL / XS 离场参考。

## 统计对象

必须统计：

- LONG 成功率
- SHORT 成功率
- PB-L 成功率
- PB-S 成功率
- BO-L 成功率
- BO-S 成功率
- EXH-L 后转化为 XL 的比例
- EXH-S 后转化为 XS 的比例
- XL 后是否继续下跌的比例
- XS 后是否继续上涨的比例
- RANGE 中主信号失败率
- TRANSITION 中主信号失败率
- Breakout Score 不同阈值的表现

## Breakout Score 阈值验证

需要重点比较：

- Breakout Score >= 55
- Breakout Score >= 60
- Breakout Score >= 65
- Breakout Score >= 70

统计目标：

- 成功率
- 失败率
- 样本数量
- 平均最大有利波动
- 平均最大不利波动
- 假突破比例
- 触发失效条件的速度

结论要求：

- 如果 60 的表现明显弱于 65 或 70，后续 Pine 默认阈值不得继续机械使用 60。
- 如果 70 样本太少，需要区分成功率与信号稀缺问题。
- 阈值调整必须写入 Research Report 后，再更新方案和规则文档。

## 市场差异统计

需要按交易对统计：

- BTC 中哪类信号表现最好。
- ETH 中哪类信号表现最好。
- SOL 中哪类信号表现最好。
- 不同币种是否需要不同阈值。
- 高波动币种是否需要更高 ATR buffer。

示例问题：

- BTC 是否更适合 BO 类信号？
- ETH 是否更适合 PB 类信号？
- SOL 是否更容易出现假突破？

## 周期差异统计

需要按周期统计：

- 15m 的噪声和失败率。
- 1h 的主信号稳定性。
- 4h 的结构可靠性。
- 1D 的信号稀缺性。

结论用途：

- 决定 Pine 默认周期提示。
- 决定不同周期是否需要不同信号冷却。
- 决定 ATR buffer 是否需要按周期调整。

## 进入 Pine 的条件

满足以下条件后，才建议进入 v0.4：

1. 完成至少 100 个标准化案例。
2. 每类核心信号至少有可讨论样本。
3. Breakout Score 默认阈值有统计依据。
4. RANGE 和 TRANSITION 的压制规则被案例验证。
5. EXH 只作为 warning 的规则被案例验证。
6. XL / XS 只作为离场参考的规则被案例验证。
7. 完成 Research Report。
8. 如果统计结论改变规则，先更新 `docs/project_plan_v1.md`。

## 不进入 Pine 的条件

出现以下情况时，不应进入 v0.4：

- Breakout Score 阈值仍无依据。
- LONG / SHORT 失败主要来自 RANGE 或 TRANSITION 未压制。
- PB / BO 信号定义在案例中频繁冲突。
- EXH 被误用为反向信号的问题没有解决。
- XL / XS 被误用为反手信号的问题没有解决。
- 样本数量不足，无法形成稳定判断。

## 输出物

v0.3.5 阶段应输出：

- 标准化案例记录。
- 统计表。
- 信号表现总结。
- 市场差异总结。
- 周期差异总结。
- Breakout Score 阈值报告。
- Research Report。
- 是否进入 v0.4 的结论。

## 当前结论

当前不建议直接进入 v0.4 Pine 基础指标版。

下一步应进入 v0.3.5 Research Validation Phase，先用案例和统计验证规则，再决定哪些内容值得翻译成 Pine Script。
