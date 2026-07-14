# DVCA

DVCA 是用于加密货币多周期结构研究、TradingView Pine Script 指标维护、案例复盘及 Outcome10/20/50 验证的统一项目仓库。

## 当前状态

- 正式基线：`indicator/current/dvca_v1_5_4.pine`
- 当前阶段：迁移与基线审计
- 当前研究：验证 1H/30m 信号属于合理稀疏还是机制性滞后
- 开发限制：专项验证完成前，不生成 v1.5.5 正式代码

开始任何工作前，请依次阅读：

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `docs/decisions/decision_log.md`
4. `docs/project/migration_report.md`

`legacy/` 保存迁移前原始资料，只作为参考，不是正式版本来源。未经核对，不得直接覆盖 current、正式文档或数据库。
