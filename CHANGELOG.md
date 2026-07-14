# Changelog

## 2026-07-14 — 高周期专项验证框架

- 将项目状态更新为迁移阶段完成、高周期专项验证进行中。
- 建立 `cases/high_timeframe_validation/` 案例生命周期目录和 HTF 案例模板。
- 建立独立的 `data/high_timeframe_validation/htf_case_database.csv`，未修改现有案例数据库。
- 建立高周期分类标准、人工复核工作表和初始汇总文档。
- 新增 `scripts/validate_htf_cases.py`，静态检查 Case ID、必填字段、截图、Outcome、分类、截图哈希和主代码引用。
- 当前样本数为 0；证据不足，不允许开始 v1.5.5 代码修改。
- 未修改任何 Pine Script 文件。

## 2026-07-14

- 初始化统一 DVCA 项目目录与 Git 仓库。
- 以原 `dvca-signal-study` 仓库为统一项目根；保留 `crypto-structure-trading-assistant` 早期资料和 `dvca128` 主版本说明，不嵌套复制自身或重复 Pine 代码。
- 根据主版本说明确认 DVCA v1.5.4 Decoupled Safety Patch 为正式基线。
- 将 v1.5.1、v1.5.4R 与 v1.6.6 作为历史版本/旁支归档。
- 建立根项目规则、项目状态、迁移报告、决策日志、已知问题与待确认问题。
- 未修改任何 Pine Script 逻辑，未开始 v1.5.5 开发。
