# DVCA 首次迁移审计报告

审计日期：2026-07-14（Asia/Shanghai）

## 1. 审计范围与结论

本次只进行项目盘点、文件分类、冲突识别和基线确认；未修改 Pine Script，未删除、移动或覆盖任何旧资料。

合并到 GitHub 关联仓库后的布局：

- 原 `dvca-signal-study` 内容保留在仓库根，不再嵌套复制自身；
- `legacy/crypto-structure-trading-assistant/`

早期审计确认两个来源的非 Git 文件数量分别为 101 和 27。随后发现 `/Users/linxiong/Documents/dvca128/` 中的主版本资料。为避免向 GitHub 推送重复内容，`dvca128` 只在 `legacy/` 保存主版本说明，三份代码分别在 `indicator/current/` 与 `indicator/archive/` 保留唯一规范副本。

## 2. 当前文件清单

### 2.1 文件类型汇总

| 类型 | 数量 |
|---|---:|
| Markdown | 85 |
| PNG 截图 | 32 |
| CSV | 4 |
| Python 脚本 | 5 |
| Pine Script | 5（legacy 4，current/archive 为原样副本） |
| `.gitignore` | 1 |
| legacy 原始资料合计 | 132 |

### 2.2 主要资料

- DVCA 研究项目：15 个普通案例文件、Gold 目录中 2 个案例文件、32 张截图、研究问题/观察/发现/假设、5 个 Python 脚本、案例模板及统计数据。
- Crypto Structure Trading Assistant：项目计划、指标规格、状态机、信号规则、验证计划、执行手册、提示词和一个 Pine 占位文件。
- `dvca128`：主版本说明保存在 legacy；v1.5.4、v1.5.4R、v1.6.6 代码分别保存在 current/archive，避免重复。
- 正式 `indicator/` 已完成主版本和历史分支的原样复制；`cases/`、`data/`、`scripts/` 尚未晋升 legacy 内容。

## 3. Pine Script 清单

| 路径 | 文件名 | 代码声明 | 行数 | 重复判断 | 正式版本可能性 |
|---|---|---|---:|---|---|
| `indicator/dvca_v1_5_1.pine` | `dvca_v1_5_1.pine` | Pine v5；指标名 `DVCA v1.5.1 Small Readable Labels` | 1075 | 只保留根目录历史副本 | 历史研究基准，不能认定为 v1.5.4 |
| `legacy/crypto-structure-trading-assistant/pine/crypto_structure_trading_assistant_v1.pine` | `crypto_structure_trading_assistant_v1.pine` | Pine v5；正文声明正式实现尚未开始 | 5 | 非重复 | 不是正式实现，仅为占位文件 |
| `indicator/current/dvca_v1_5_4.pine` | `dvca_v1_5_4.pine` | Pine v5；指标名 `DVCA v1.5.4 Decoupled Safety Patch` | 1499 | 唯一 current 副本 | 主版本说明明确指定为正式主版本 |
| `indicator/archive/v1_5_x/DVCA_v1_5_4R_Conservative.pine` | `DVCA_v1_5_4R_Conservative.pine` | Pine v5；指标名 `DVCA v1.5.4R Conservative` | 1506 | 唯一 archive 副本 | 保守测试旁支，不替代主版本 |
| `indicator/archive/v1_6_x/DVCA_v1_6_6_Visible_Adaptive.pine` | `DVCA_v1_6_6_Visible_Adaptive.pine` | Pine v5；指标名 `DVCA v1.6.6 Visible Adaptive` | 944 | 唯一 archive 副本 | 1.6.x 历史实验路线，不得晋升 |

### v1.5.4 识别结果

初始两个项目中没有 v1.5.4；补充搜索在 `/Users/linxiong/Documents/dvca128/` 找到两份 v1.5.4 代码和主版本说明。`DVCA_v1_5_4_MASTER_NOTES.md` 明确写明主版本是 `DVCA_v1_5_4_Decoupled_Safety_Patch.pine`，并说明 v1.5.4R 只是保守测试旁支。因此已将主文件逐字节复制为 `indicator/current/dvca_v1_5_4.pine`，没有修改代码。

## 4. 重复文件清单

### 4.1 跨项目同名文件

| 文件名 | 情况 |
|---|---|
| `AGENTS.md` | 两份规则不同：研究项目固定 v1.5.1；早期项目要求先完成 Research Validation。不得互相覆盖。统一规则由仓库根 `AGENTS.md` 管理。 |
| `README.md` | 两份分别描述不同项目阶段和用途，应作为迁移来源保留，正式 README 需另行整合。 |
| `case_database.csv` | 两份字段结构和数据量不同，属于实质冲突，不能按同名覆盖。 |

### 4.2 完全相同内容

发现两张路径和命名不同、SHA-1 完全相同的截图：

- `screenshots/BTCUSDT/2026-07-10/2026-07-10_BTCUSDT_MultiTF_30mUP_TC-L_1238_followup.png`
- `screenshots/SOLUSDT/2026-07-10/2026-07-10_SOLUSDT_30m_CTX_UP_1238_observation.png`

这可能是误分类或重复引用。迁移前需人工查看图片内容并确认标的；本次不删除任一文件。

## 5. 冲突文件与冲突结论

### 5.1 版本基线沿革（已厘清）

- 早期根 AGENTS、README 和多份说明将 v1.5.1 定义为当时的研究基准。
- 2026-07-14 的研究问题与假设开始按 v1.5.4 讨论高周期滞后，并提出 v1.5.5 候选方向。
- `dvca128` 的主版本说明确认 v1.5.4 Decoupled Safety Patch 为主版本、v1.5.4R 为测试旁支；同时找到 v1.6.6 历史源码。

结论：正式基线可确认为 v1.5.4；v1.5.1、v1.5.4R 和 v1.6.6 分别作为旧研究基准、保守旁支和历史实验归档。尚需按案例逐份标注实际运行版本。

### 5.2 案例数据库冲突

| 来源 | 数据行 | 列数 | 特点 |
|---|---:|---:|---|
| `data/case_database.csv` | 持续维护 | 29 | 现有正式研究数据库，包含方向、信号链、Outcome10/20/50、截图和案例路径 |
| `legacy/crypto-structure-trading-assistant/data/case_database.csv` | 1 | 20 | 使用 ParentCase、FollowUpDate、NextExpectedState、KeyLevels 等另一套字段 |

两者存在同类概念但列名和语义不完全一致。建议先制定统一 schema，再把第二份的一条 CASE-0009 作为待合并记录处理，不能简单追加或覆盖。

### 5.3 源仓库状态风险

早期审计时，`dvca-signal-study` 曾包含已修改和未跟踪资料。当前统一仓库直接沿用并继续该 Git 历史，不再维护一份嵌套 legacy 自身副本。

## 6. 缺失文件清单

按目标结构和验收标准，目前至少缺少或尚未建立：

- v1.5.1 到 v1.5.4 的逐版本变更记录和 TradingView 最终编译/运行验收记录。
- `docs/project/project_charter.md`、`docs/project/version_policy.md`。
- `docs/specifications/` 下的正式规格文件。
- `docs/signals/` 下的正式信号文档。
- `docs/playbook/` 下的正式执行文档。
- `docs/codex/TASKS.md`、`ACCEPTANCE_CRITERIA.md`、`PROMPT_LIBRARY.md`、`COMPLETED_TASKS.md`。
- 正式 `data/case_database.csv` 及统一字段规范。
- `data/case_index.csv`、`signal_dictionary.csv`、`tag_dictionary.csv`、`statistics_summary.md` 的正式版本或迁移决定。
- `scripts/new_case.py`、`validate_case_database.py`、`validate_project.py`、`generate_research_summary.py`。
- 统一截图命名和按 Case ID 关联的清单。
- 建议的聊天摘要文件。

“缺失”表示目标结构尚未具备，不代表应立即新建空壳或从 legacy 直接覆盖。

## 7. 建议正式目录与迁移映射

| legacy 来源 | 建议目标 | 处理方式 |
|---|---|---|
| `dvca-signal-study/indicator/dvca_v1_5_1.pine` | `indicator/archive/v1_5_x/` | 已原样复制归档，保持原文件名和内容 |
| `dvca128/...Decoupled_Safety_Patch.pine` | `indicator/current/dvca_v1_5_4.pine` | 已根据主版本说明确认并原样复制 |
| `dvca128/...v1_5_4R_Conservative.pine` | `indicator/archive/v1_5_x/` | 已作为保守测试旁支原样归档 |
| `dvca128/...v1_6_6_Visible_Adaptive.pine` | `indicator/archive/v1_6_x/` | 已作为 1.6.x 历史实验原样归档 |
| `crypto-structure-trading-assistant/pine/...v1.pine` | `indicator/experiments/` 或仅留 legacy | 占位文件价值有限，建议只保留 legacy，除非需记录早期路线 |
| `dvca-signal-study/docs/signal_manual.md` | `docs/signals/signal_manual.md` | 核对与最终基线版本一致后复制 |
| `dvca-signal-study/docs/signal_atlas/*` | `docs/signals/` | 整理命名后复制，不覆盖正式文件 |
| 两项目状态机、规则、规格文档 | `docs/specifications/` | 逐份对照，注明适用版本后晋升 |
| 两项目 playbook 文档 | `docs/playbook/` | 对同主题文件先做差异审查 |
| `dvca-signal-study/research/*` | `docs/research/` | 保留日期和研究层级，复制后维护索引 |
| `dvca-signal-study/cases/*` | `cases/active|completed|failed_signals|good_cases/` | 依据 Outcome 完整度和评级逐案分类 |
| `dvca-signal-study/gold_cases/*` | `cases/gold_cases/` | 核对是否达到最终评级条件后复制 |
| `dvca-signal-study/screenshots/*` | `assets/screenshots/` | 保留原件；建立 Case ID 映射并处理疑似误分类副本 |
| 两份 `case_database.csv` | `data/case_database.csv` | 先确定统一 schema，再做可审计的字段映射与合并 |
| `dvca-signal-study/logs/case_index.csv` | `data/case_index.csv` | 核对 Case ID 唯一性和路径后复制 |
| `dvca-signal-study/data/tag_dictionary.csv` | `data/tag_dictionary.csv` | 审查字段后复制 |
| `dvca-signal-study/scripts/*.py` | `scripts/` | 先检查硬编码路径和目标 schema，再复制/改造 |
| `dvca-signal-study/templates/case_template.md` | `cases/templates/case_template.md` | 与统一 schema 对齐后复制 |

## 8. 需要人工确认的事项

1. v1.5.4 在 TradingView 最后一次人工编译/运行验收的日期和结果是什么？
2. v1.6.6 的最终否决案例证据是否需要整理为决策摘要？
3. v1.5.1 到 v1.5.4 的逐版本变更记录是否仍在聊天或其他备份中？
4. 两份 CASE-0009 数据是否描述同一案例；若是，应合并字段还是建立 follow-up 子记录？
5. 两张哈希相同但分别命名为 BTCUSDT 与 SOLUSDT 的截图，哪个标的/路径正确？
6. 77 条数据库记录中，哪些已有完整 Outcome10/20/50，哪些仍属 active？
7. Gold Case 是否已满足“不提前评级”的新规则，还是需要重新审核？
8. 正式数据库采用哪套字段，并如何保留 ParentCase/FollowUpDate/KeyLevels 等信息？

## 9. 建议执行顺序

1. 确定统一案例数据库 schema。
2. 解决 CASE-0009 与重复截图问题。
3. 按映射表以“复制、核验、记录”的方式逐类晋升资料。
4. 建立高周期专项验证任务和验收标准。
5. 运行项目验证并创建首次 Git 迁移基线提交。

v1.5.4 基线已经确认，但在专项验证和验收范围批准前，仍不应开始 v1.5.5 开发。
