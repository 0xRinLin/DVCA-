# Changelog

## 2026-07-17 — CASE-0016 低周期修复失败与空头再确认

- 归档 BTCUSDT 16:07-16:08（UTC+8）的两张 30m / 1H 跟踪截图。
- 价格跌破 63200 与 63000 后进入 62800-62600 延伸观察区；1m / 5m L-ZONE HMR100 只形成短暂修复。
- 1m 未能配合价格收复 62950-63080，随后重新出现 TC-S 并从 FLAT 返回 DN；低周期修复分支记为 Failed。
- `CASE-0016` 继续保持 `Outcome10Recorded / Review10 / Outcome20`，本次仅为 Outcome20 Active 跟踪，Result 仍为 Unknown。
- 执行继续为 No-Chase：不在 62800 支撑附近追空，等待 62950-63080 或 63200-63330 反抽拒绝，或 62600 跌破后的失败回测。
- 截图运行 DVCA 1.5.1，不计入 v1.5.4 正式高周期专项样本；未修改任何 Pine Script。

## 2026-07-17 — CASE-0016 Outcome10 恢复失败与空头延续

- 归档 BTCUSDT 12:28（UTC+8）的 LTF 与 HTF 两张跟踪截图。
- `CASE-0016` 推进为 `Outcome10Recorded / Review10 / Outcome20`；恢复分支为 Failed，原始空头方向阶段验证为 Favorable，最终 Result 仍为 Unknown。
- 最新五周期均为 DN；63780 核心支撑已失守，30m / 1H 已完成空头对齐。
- 执行仍为 NoChase：不在约 63341 和 `63300-63200` 支撑附近追空，等待反抽拒绝或 63200 破位回测。
- 版本边界不变：截图为 DVCA 1.5.1，不计入 v1.5.4 正式高周期专项样本。
- 未修改任何 Pine Script，未生成 v1.5.5 候选代码。

## 2026-07-16 — BTC 多周期空头转折历史观察

- 新增 `CASE-0016`，记录 BTCUSDT 在 30m/15m/5m/1m 同步转 DN、1H 仍为 FLAT 时的 TC-S 延续。
- 归档 5m/15m/1m 与 30m/1H 两张原始截图，案例保持 `SignalCaptured / Open / Unknown`。
- 当前评级只记录为 `Good Case candidate`，Outcome10/20/50 尚未完成，不提前给出最终评级。
- 截图指标为 DVCA 1.5.1；新增高周期观察文档并标记 `ExcludedPendingReproduction`，不计入 v1.5.4 正式专项样本。
- `DN-PENDING` 只作为研究建议；未修改任何 Pine Script，未生成 v1.5.5 候选代码。

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
