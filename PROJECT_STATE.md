# DVCA 项目状态

最后更新：2026-07-21（Asia/Shanghai）

## 当前阶段

迁移阶段完成，正在进行高周期专项验证框架建设，尚未开始v1.5.5开发。

高周期专项已建立独立案例目录、模板、专项 CSV、分类标准、人工复核工作表、初始汇总和静态检查脚本。当前样本数为 0，尚未形成任何代码问题结论。

## 基线状态

- 当前主版本基线已确认为 **DVCA v1.5.4**。`legacy/dvca128/DVCA_v1_5_4_MASTER_NOTES.md` 记录了主版本选择；唯一正式代码保存为 `indicator/current/dvca_v1_5_4.pine`。
- v1.5.4 主文件共 1499 行，代码声明为 `DVCA v1.5.4 Decoupled Safety Patch`；正式副本必须与 legacy 源文件保持哈希一致。
- 完整的 v1.5.1 保存于 `indicator/dvca_v1_5_1.pine`，共 1075 行，作为本仓库历史研究基准；为避免重复，不再复制到 archive 或嵌套 legacy。
- `legacy/crypto-structure-trading-assistant/pine/crypto_structure_trading_assistant_v1.pine` 只有 5 行，是“正式实现尚未开始”的占位文件，不是可运行基线。
- v1.5.4R Conservative 共 1506 行，是保守测试旁支，不替代主版本，归档于 `indicator/archive/v1_5_x/`。
- v1.6.6 Visible Adaptive 共 944 行，按主版本说明属于不再继续的 1.6.x 历史实验路线，归档于 `indicator/archive/v1_6_x/`，不得自动恢复为主版本。
- 当前不得直接编写或生成 v1.5.5 正式代码。

### 最新研究观察

- `CASE-0016` 在 2026-07-21 00:50 更新为 `1H/30m/15m/5m/1m 全部 UP`：价格在 63818 扫低后完成 V 型恢复，30m 收复 65084.6 Trigger，并推进至 65409-65417；新分支为 `Outcome13Active / Upgraded / Recovery Continuation / Breakout Extension Attempt`。当前位于 1H Trigger 65589.7 下方，执行保持 No-Chase，主案例仍为 `Review20 / Outcome50 / Unknown`。
- `CASE-0016` 在 2026-07-20 13:13 更新为 `1H FLAT / 30m FLAT / 15m FLAT / 5m DN / 1m DN`：失守 64439-64406 与 64239-64170，当前测试 64013-63996；Outcome11 更新为 `Outcome11BearishBreakdown`，新分支进入 `Outcome12Active / Multi-Level Support Failure`。方向偏空但 1m/5m 已超卖，执行保持等待反弹拒绝或 63996 破位回测，禁止低位追空。
- `CASE-0016` 在 2026-07-19 20:52 更新为 `15m DN / 5m DN / 1m FLAT`：低周期反弹仅为 Countertrend Repair，Current Recovery Branch 由 Outcome10Active 转为 `Outcome10AtRisk`；当前截图未包含 30m/1H，其 15:10 状态明确标记为过期参考。
- `CASE-0016` 在 2026-07-19 15:10 更新为 `HTF UP / LTF Pullback`：1H/30m/15m 保持 UP，1m/5m 转 DN 并出现 TC-S；Current Recovery Branch 保持 `Outcome10Active`，等待低周期 UP + TC-L/PB-L 再确认。
- BTCUSDT 30m 人工常规多头背离的后续方向已验证：价格依次收复 64078、64170、64438，并扩展至 64800-64900；研究状态更新为 `False Negative / Bullish Follow-Through Confirmed / Regression Test Required`，具体根因仍需 v1.5.4 复现。
- 新增 BTCUSDT 30m 常规多头背离漏报观察：DVCA 1.5.1 截图中人工可见价格 Lower Low 与 MACD Higher Low，但未打印背离事件。
- 该样本分类为 `False Negative / NeedsCodeTrace / ExcludedPendingReproduction`；当前只确认视觉事件与指标输出不一致，Pivot 配对错误仍是待验证假设。
- 已建立 Divergence Detection Accuracy 核查要求：记录全部价格/MACD Pivot、位移容差、多历史 Pivot 配对、阈值结果和精确 suppression reason；检测事件必须与 Context/交易门控分离。
- 普通历史案例 `CASE-0016` 已记录 Outcome10：恢复分支失败，随后 1H/30m/15m/5m/1m 全部转为 DN，空头延续阶段有效。
- `CASE-0016` 已记录 Outcome20：原始空头方向有利并到达 62800-62600 延伸区；第二次低周期修复使 5m 转 UP/TC-L，当前 1m 在首次回踩中为 FLAT，案例进入 Review20 并等待 Outcome50。
- `CASE-0016` 的 Current Recovery Branch 已升级为 Strong Recovery：1H/30m/15m/5m 全部转 UP，原 Bearish Continuation 在方向层失效；1m 处于 Full MTF Bullish Alignment 后的首次 FLAT 回踩，分支状态为 Outcome10Active。
- `CASE-0016` 的首次回踩随后守住 64000：5m 出现 L-ZONE HMR95，1m 以 TC-L 从 FLAT 返回 UP，五周期多头对齐恢复；分支仍为 Outcome10Active，主案例继续等待 Outcome50。
- `CASE-0016` 在 22:31 交易至 64150 上方，五周期仍为 UP，5m/15m 动能扩张；当前仅记录为 `64150 Breakout Attempt`，因尚无收盘、站稳或成功回测证据，Breakout Confirmation 继续 Pending，执行保持 No-Chase。
- 截图运行 DVCA 1.5.1，不符合 v1.5.4 高周期专项准入条件；已标记为 `ExcludedPendingReproduction`。
- `DN-PENDING` 仅作为待验证研究建议，不是当前代码已实现状态，也未触发 v1.5.5 开发。

## 当前研究任务

首先验证高周期信号属于合理稀疏还是机制性滞后，重点包括：

1. 1H、30m 的背景/结构职责与执行职责是否混用。
2. Zone、结构确认和执行信号之间的延迟来源。
3. 高周期与低周期信号的一致性。
4. RANGE、TRANSITION 对趋势信号的压制是否正确。
5. 在不引入 v1.6.x 式噪音的前提下，是否有必要形成 v1.5.5 Accuracy Patch。
6. 复现 30m 常规背离漏报，确认是 Pivot 配对、位移容差、阈值拒绝、事件门控还是显示优先级造成。

### 高周期专项框架状态

- 专项任务：`RES-HTF-001`
- 当前阶段：框架完成，等待收集和人工复核样本
- 案例模板：`cases/high_timeframe_validation/templates/htf_case_template.md`
- 专项数据库：`data/high_timeframe_validation/htf_case_database.csv`
- 分类规则：`docs/research/high_timeframe_validation/classification_rules.md`
- 人工工作表：`docs/research/high_timeframe_validation/review_workbook.md`
- 汇总：`docs/research/high_timeframe_validation/summary.md`
- 静态检查：`scripts/validate_htf_cases.py`
- 结论限制：当前证据不足，不允许开始 v1.5.5 代码修改。

## 数据与案例状态

- `data/case_database.csv`：现有正式研究数据库；高周期专项使用独立的 `data/high_timeframe_validation/htf_case_database.csv`，不修改或合并原数据库。
- `legacy/crypto-structure-trading-assistant/data/case_database.csv`：1 条数据记录（加表头共 2 行），20 列，字段结构不同，不能直接覆盖或拼接。
- 发现 16 个普通案例 Markdown、3 个 Gold 案例 Markdown（另有 1 个 Gold README）以及 56 张截图。
- 案例、截图和数据库尚未晋升到正式目录，必须先确定映射、字段规范和 Case ID 去重规则。

## 保护状态

- 本次审计未修改任何 Pine Script；current/archive 文件均为原文件的逐字节复制。
- 本次审计未删除、移动或覆盖任何 `legacy/` 文件。
- `dvca-signal-study` 本身就是当前 Git 仓库根目录，因此没有再嵌套复制到 `legacy/`。
- `dvca128` 的主版本说明保存在 `legacy/dvca128/`；三份 Pine 代码只在 `indicator/current|archive/` 保留规范副本，避免重复内容。
- `crypto-structure-trading-assistant` 作为不同的早期资料来源保存在 `legacy/`。

## 下一步

1. 提供 BTC、ETH、SOL 的 1H、30m、15m 配套截图及统一时区时间轴。
2. 按模板创建首批 active 案例，不从文件名猜测截图内容。
3. 人工标记客观趋势起点、结构确认和信号真实可见时间。
4. 完成 Outcome10/20/50 后再移动到 completed 并形成最终分类。
5. 继续保持 current Pine 不变；多案例证据充分前不进入 v1.5.5 设计。
