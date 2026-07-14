# 05_write_pine

用途：根据方案和 docs 文件生成完整 Pine Script v5 指标。

使用边界：

- 写代码前先确认 `docs/project_plan_v1.md`、规格文档、信号规则和状态机文档一致。
- 写代码前先确认 v0.3.5 Research Validation 已完成。
- 写代码前先确认 `docs/validation_plan.md` 的验证结论允许进入 v0.4。
- 必须输出完整 Pine Script 文件。
- 不输出零散 patch 或替换片段。
- v1 使用 `indicator()`，不使用 `strategy()`。
