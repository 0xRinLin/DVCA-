# DVCA Change Log

## 2026-07-21

- 原因：记录 `CASE-0016` 在 63818 扫低后的 V 型恢复与多周期延续，建立 Outcome13 分支。
- 改动：归档 BTCUSDT 00:50 的 LTF 与 HTF 截图；同批 SOL/ETH 截图未归档。
- 改动：更新案例正文、案例数据库、项目状态与 Changelog，状态为 `Outcome13Active / Upgraded / Breakout Extension Attempt`。
- 约束：主案例仍为 `Review20 / Outcome50 / Unknown`；不修改任何 Pine、Signal Manual 或 Line Patterns。

## 2026-07-08

- 原因：升级 Case Database，新增 Case Lifecycle 机制，避免案例入库后长期停留在 `Unknown`，并让每个案例都有明确的 10 / 20 / 50 根 K 线复盘节点。
- 改动：新增 `state`、`next_expected_state`、`lifecycle_status` 字段。
- 改动：新增 `scripts/review_case.py`，用于按 `CASE-0009` 这类编号复盘案例、更新 Outcome10 / Outcome20 / Outcome50、刷新 CSV 与案例 Markdown，并辅助计算 `result`。
- 改动：更新案例数据库脚本、标签字典、案例规则和 README。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-08 Trading Desk Report

- 原因：固定 `DVCA Trading Desk Report` 作为每日多周期盘面复盘格式，并把 7-8 两张 BTC 图纳入案例数据库。
- 改动：新增 `docs/trading_desk_report.md`、`templates/trading_desk_report_template.md`、`reports/trading_desk/2026-07-08_BTCUSDT_trading_desk_report.md`。
- 改动：新增 `CASE-0010`，用于记录 BTCUSDT `1D+30m` 的 `TransitionToTrendDown / Context Shift` Good Case。
- 改动：新增 `CASE-0011`，用于记录 BTCUSDT `5m+1m` 的 `TrendContinuation / TC-S` Good Case。
- 改动：新增研究问题 `research/questions/2026-07-08_BTC_Reversal_Readiness.md`。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-08 Trading Desk Follow-up

- 原因：根据本次 ChatGPT DVCA Trading Desk Report 更新案例库，记录 SOL 空头延续案例，并把 BTC 恢复失败观察作为既有案例 follow-up。
- 改动：新增 `CASE-0012`，记录 `SOLUSDT / MultiTF / TrendContinuation / TC-S` Good Case。
- 改动：在 `CASE-0009` 追加 BTC follow-up：5m `L-ZONE HMR95` 未突破 Trigger `62394`，1m 从 `TC-L` 转为 `TC-S`。
- 说明：SOL 截图未在本轮消息中提供明确文件路径，`CASE-0012` 的 `screenshot_path` 暂记为 Pending，后续收到图片后再补归档路径。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-08 BTC CASE-0009 Outcome10

- 原因：根据本次 BTC Trading Desk Report 更新既有 BTC Recovery / TC-S 案例，不新建独立 Case。
- 改动：在 `CASE-0009` 写入 Outcome10：5m `L-ZONE HMR95` 未突破 Trigger，1m 转为 `TC-S` 并跌破 `62100`，反弹失败，空头延续有效。
- 改动：`CASE-0009` 生命周期从 `Open / Outcome10` 推进为 `Review10 / Outcome20`。
- 说明：按用户要求，`result` 保持 `Unknown`，等待 Outcome20 / Outcome50 进一步确认。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-08 SOL CASE-0012 Follow-up

- 原因：根据 21:57 左右 SOLUSDT Trading Desk Report 更新既有 SOL TC-S 案例，不新建独立 Case。
- 改动：在 `CASE-0012` 追加 follow-up：15m / 5m 仍为 `Ctx=DN` 且 `Last=TC-S`，1m 出现 `L-ZONE HR85`，但尚未形成 `LONG / PB-L`。
- 改动：记录关键价位 `77.00-77.10`、`77.20-77.35`、`77.50-77.75`、`76.90`，并记录下一步观察 `L-ZONE Failed / TC-S Continuation` 或 `TrendDown→Recovery→Reversal Attempt`。
- 说明：`CASE-0012` 生命周期保持 `Open / Outcome10`，`result` 保持 `Unknown`。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-08 SOL CASE-0012 22:43 Follow-up

- 原因：根据 22:43 左右 SOLUSDT Trading Desk Report 更新既有 SOL TC-S 案例，不新建独立 Case。
- 改动：在 `CASE-0012` 追加 follow-up：前一段 `L-ZONE / TC-L` 反弹没有升级成 `LONG / PB-L`，随后演化为 `S-ZONE / C-S / TC-S`，定义为 `Weak Recovery Failed→TC-S Continuation`。
- 改动：记录关键价位 `77.20-77.35`、`77.05-77.10`、`76.85-76.90`、`76.58-76.70`、`76.30-76.00`，并保留 `Continue Down 或 EXH-L` 作为下一步观察。
- 说明：尚未写入 Outcome10；如果后续跌破 `76.58` 并继续下探，再更新 Outcome10。
- 说明：用户附图 `7-8-10.png` 画面显示 `BTCUSDT.P`，未归档为 SOL 截图。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-09 BTC CASE-0009 Follow-up

- 原因：根据 2026-07-09 11:03 左右 BTCUSDT 截图更新 `CASE-0009`，不新建独立 Case。
- 改动：归档 BTC 截图到 `screenshots/BTCUSDT/2026-07-09/2026-07-09_BTCUSDT_MultiTF_TC-S_WeakRecoveryFailed_followup.png`。
- 改动：在 `CASE-0009` 追加 follow-up：`Weak Recovery Failed→TC-S Continuation`，记录 `L-ZONE 尝试反弹→Trigger 未突破→TC-S→继续下压`。
- 改动：记录关键价位 `62,300-62,400`、`62,000-62,150`、`61,750-61,850`、`61,600-61,650`、`61,400`。
- 说明：`CASE-0009` 已处于 `Review20 / Outcome50`，未回退生命周期，`result` 保持 `Unknown`。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-09 SOL Observation

- 原因：根据 2026-07-09 11:03 左右 SOLUSDT 截图记录观察，不新建 Case。
- 改动：归档 SOL 截图到 `screenshots/SOLUSDT/2026-07-09/2026-07-09_SOLUSDT_1H_CTX_DN_observation.png`。
- 改动：新增 observation 文件 `research/observations/2026-07-09_SOL_1H_CTX_DN_observation.md`。
- 说明：SOL 1H 仍为 `Ctx=DN`，`77.50-77.80` 是关键反抽压力，未站上前不定义为多头反转。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-09 BTC CASE-0009 L-ZONE Recovery Watch

- 原因：根据 2026-07-09 11:26 左右 BTCUSDT 截图更新 `CASE-0009`，不新建独立 Case。
- 改动：归档 BTC 截图到 `screenshots/BTCUSDT/2026-07-09/2026-07-09_BTCUSDT_MultiTF_1m_L-ZONE_RecoveryWatch_followup.png`。
- 改动：在 `CASE-0009` 追加 follow-up：`TC-S Continuation→1m L-ZONE Recovery Watch`，记录 `TC-S 下跌→低位出现 1m L-ZONE HMR95→短线反弹→5m/15m 尚未确认多头`。
- 改动：记录关键价位 `62,300-62,400`、`62,000-62,150`、`61,880-61,920`、`61,750-61,800`、`61,400-61,600`。
- 说明：`CASE-0009` 继续保持 `Review20 / Outcome50`，`result` 保持 `Unknown`。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-09 BTC CASE-0009 Recovery Upgrade

- 原因：根据 2026-07-09 12:40 左右 BTCUSDT 截图更新 `CASE-0009`，不新建独立 Case。
- 改动：归档 BTC 截图到 `screenshots/BTCUSDT/2026-07-09/2026-07-09_BTCUSDT_MultiTF_RecoveryUpgrade_followup.png`。
- 改动：在 `CASE-0009` 更新 follow-up：`TC-S Continuation→L-ZONE Recovery→Recovery Upgrade`，记录 `TC-S 下跌→低位 L-ZONE / C-L→1m TC-L→5m Ctx 转 UP→反弹升级观察`。
- 改动：记录关键价位 `62,400-62,600`、`62,250-62,300`、`62,000-62,150`、`61,850-61,900`、`61,600-61,750`。
- 说明：`CASE-0009` `result` 保持 `Unknown`，Lifecycle 继续等待 `Outcome20 / Outcome50`；当前 1m 和 5m 修复明显增强，低位追空风险上升，但 15m 尚未完全翻多，未出现明确 `PB-L / LONG` 前不建议追多。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-09 BTC CASE-0009 TC-L Breakout / S-ZONE Pressure

- 原因：根据 2026-07-09 14:58 左右 BTCUSDT Trading Desk Report 更新 `CASE-0009`，不新建独立 Case。
- 改动：在 `CASE-0009` 追加 follow-up：`L-ZONE Recovery→TC-L Breakout→S-ZONE Pressure`，记录 `TC-S 下跌→低位 L-ZONE / C-L→1m TC-L→5m TC-L→15m TC-L→当前 5m 出现 S-ZONE HMR100`。
- 改动：记录关键价位 `63,000-63,200`、`62,800-62,900`、`62,500-62,600`、`62,300-62,400`、`62,000-62,150`。
- 说明：`CASE-0009` 继续保持 `Review20 / Outcome50`，`result` 保持 `Unknown`；当前进入压力区，不追高，等待回踩确认或 `S-ZONE` 失效信号。
- 说明：用户提供的截图路径 `/Users/linxiong/Desktop/截屏2026-07-09 14.58.23.png` 不存在，因此本次未归档截图。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-09 BTC CASE-0009 High Range Consolidation

- 原因：根据 2026-07-09 15:29 左右 BTCUSDT 截图更新 `CASE-0009`，不新建独立 Case。
- 改动：归档 BTC 截图到 `screenshots/BTCUSDT/2026-07-09/2026-07-09_BTCUSDT_MultiTF_HighRangeConsolidation_followup.png`。
- 改动：在 `CASE-0009` 追加 follow-up：`TC-L Breakout→S-ZONE Pressure→High Range Consolidation`，记录 `低位 L-ZONE / C-L→1m TC-L→5m TC-L→15m TC-L→价格接近 63,000→5m S-ZONE HMR100→当前高位横盘消化`。
- 改动：记录关键价位 `63,000-63,200`、`62,900-63,000`、`62,750-62,850`、`62,600-62,700`、`62,500-62,600`、`62,300-62,400`。
- 说明：`CASE-0009` 继续保持 `Review20 / Outcome50`，`result` 保持 `Unknown`；不追多，不主动空，等待回踩确认或 `63,000` 上方有效突破。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-09 BTC CASE-0009 Pullback L-ZONE / TC-L Resume

- 原因：根据 2026-07-09 16:53 左右 BTCUSDT 截图更新 `CASE-0009`，不新建独立 Case。
- 改动：归档 BTC 截图到 `screenshots/BTCUSDT/2026-07-09/2026-07-09_BTCUSDT_MultiTF_Pullback_LZONE_TC-L_Resume_followup.png`。
- 改动：在 `CASE-0009` 追加 follow-up：`S-ZONE Pressure→Pullback→L-ZONE Recovery→TC-L Resume`，记录 `低位 L-ZONE/C-L→TC-L 上涨→5m S-ZONE HMR100 高位压力→回踩→5m L-ZONE HR85→1m TC-L 恢复`。
- 改动：记录关键价位 `63,000-63,200`、`62,850-62,950`、`62,750-62,800`、`62,600-62,700`、`62,500-62,600`、`62,300-62,400`。
- 说明：`CASE-0009` 继续保持 `Review20 / Outcome50`，`result` 保持 `Unknown`；回踩暂时守住，但价格仍在压力区附近，不追多，等待站稳或二次回踩确认。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-10 BTC CASE-0009 30m UP / TC-L Continuation

- 原因：根据 2026-07-10 11:53 左右 BTCUSDT 截图更新 `CASE-0009`，不新建独立 Case。
- 改动：归档 BTC 截图到 `screenshots/BTCUSDT/2026-07-10/2026-07-10_BTCUSDT_MultiTF_30mUP_TC-L_SZONEPressure_followup.png`。
- 改动：在 `CASE-0009` 追加 follow-up：`L-ZONE Recovery→30m UP→TC-L Continuation→1m S-ZONE Pressure`，记录 `TC-S 下跌→低位 L-ZONE/C-L→1m TC-L→5m TC-L→15m TC-L→30m Ctx 转 UP→当前价格接近 64,000，1m 出现 S-ZONE HMR100 高位压力`。
- 改动：记录关键价位 `64,000-64,200`、`63,800-63,950`、`63,500-63,650`、`63,200-63,400`、`62,900-63,000`、`62,500-62,600`。
- 说明：`CASE-0009` 继续保持 `Review20 / Outcome50`，`result` 保持 `Unknown`；BTC 30m、15m、5m 均已明显转强，但 1m 出现 `S-ZONE HMR100`，不追高，等待回踩确认。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-10 SOL Observation

- 原因：根据 2026-07-10 11:53 左右 SOLUSDT 截图记录观察，不新建 Case。
- 改动：归档 SOL 截图到 `screenshots/SOLUSDT/2026-07-10/2026-07-10_SOLUSDT_30m_CTX_UP_observation.png`。
- 改动：新增 observation 文件 `research/observations/2026-07-10_SOL_30m_CTX_UP_observation.md`。
- 说明：SOL 30m `Ctx=UP`，低位 `L-ZONE` 后修复；`78.80-79.30` 为当前压力区，下一步观察 `78.30 / 78.00` 是否守住。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-10 BTC CASE-0009 / SOL 12:38 Follow-up

- 原因：根据 2026-07-10 12:38 左右组合截图更新 BTC 既有 `CASE-0009`，并补充 SOL 观察记录；用户本轮未提供结构化字段，因此按图面状态做保守 follow-up，不新建独立 Case。
- 改动：归档 BTC 截图到 `screenshots/BTCUSDT/2026-07-10/2026-07-10_BTCUSDT_MultiTF_30mUP_TC-L_1238_followup.png`。
- 改动：归档 SOL 截图到 `screenshots/SOLUSDT/2026-07-10/2026-07-10_SOLUSDT_30m_CTX_UP_1238_observation.png`。
- 改动：在 `CASE-0009` 追加 follow-up：`30m UP→TC-L Continuation→High S-ZONE Pressure Watch`，记录 BTC 仍不能按强空头处理，但 `64,000-64,200` 压力区附近不追多，等待回踩确认或有效突破。
- 改动：在 `research/observations/2026-07-10_SOL_30m_CTX_UP_observation.md` 追加 12:38 follow-up：SOL 30m 仍为 `Ctx=UP`，低位 `L-ZONE` 后修复延续，继续观察 `78.30 / 78.00` 回踩是否守住。
- 说明：`CASE-0009` 继续保持 `Review20 / Outcome50`，`result` 保持 `Unknown`。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-10 BTC CASE-0009 Breakout Extension / Momentum Push

- 原因：根据 2026-07-10 16:17 左右 BTCUSDT 截图更新既有 `CASE-0009`，不新建独立 Case。
- 改动：归档 BTC 截图到 `screenshots/BTCUSDT/2026-07-10/2026-07-10_BTCUSDT_MultiTF_BreakoutExtension_MomentumPush_followup.png`。
- 改动：在 `CASE-0009` 追加 follow-up：`L-ZONE Recovery→TC-L Continuation→Breakout Extension→Momentum Push`，记录 `低位 L-ZONE/C-L→1m TC-L→5m TC-L→15m TC-L→突破 64,000→当前冲到 64,200 附近`。
- 改动：记录关键价位 `64,300-64,500`、`64,150-64,250`、`64,000-64,100`、`63,800-63,950`、`63,500-63,650`、`63,200-63,400`。
- 说明：`CASE-0009` 继续保持 `Review20 / Outcome50`，`result` 保持 `Unknown`；当前属于多头突破延续，但 1m 已急拉，不追多，等待 `64,000` 或 `63,850` 回踩确认。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-12 BTC CASE-0009 EXH-L Bounce / Weak Recovery

- 原因：根据 2026-07-12 12:20 左右 BTCUSDT 截图更新既有 `CASE-0009`，不新建独立 Case。
- 改动：归档 BTC 截图到 `screenshots/BTCUSDT/2026-07-12/2026-07-12_BTCUSDT_MultiTF_EXH-L_TC-L_SZONE_WeakRecovery_followup.png`。
- 改动：在 `CASE-0009` 追加 follow-up：`15m EXH-L Bounce→5m TC-L Weak Recovery→1m S-ZONE Pullback`，记录 `15m 下跌后出现 EXH-L HMR95→1m/5m 反弹修复→5m Last=TC-L→1m 反弹到 S-ZONE HMR100→从压力区回落`。
- 改动：记录关键价位 `64,220-64,300`、`64,150-64,220`、`64,080-64,120`、`63,950-64,000`、`63,800-63,900`、`63,650-63,750`。
- 说明：`CASE-0009` 继续保持 `Review20 / Outcome50`，`result` 保持 `Unknown`；当前是 15m 下跌后的弱修复，重点观察 `64,000` 是否守住以及 `64,150-64,220` 反抽是否失败。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-12 BTC CASE-0009 TC-L Recovery / 64k Retest

- 原因：根据 2026-07-12 19:36 左右 BTCUSDT 截图更新既有 `CASE-0009`，不新建独立 Case。
- 改动：归档 BTC 截图到 `screenshots/BTCUSDT/2026-07-12/2026-07-12_BTCUSDT_MultiTF_EXH-L_TC-L_64k_Retest_followup.png`。
- 改动：在 `CASE-0009` 追加 follow-up：`15m EXH-L Bounce→1m TC-L Recovery→64k Retest`，记录 `15m EXH-L HMR95→1m L-ZONE/C-L 止跌→1m 多次 TC-L 反弹→5m 回到均线组→重新测试 64,000`。
- 改动：记录关键价位 `64,150-64,220`、`64,000-64,080`、`63,900-63,950`、`63,750-63,850`、`63,650-63,700`、`64,300-64,500`。
- 说明：`CASE-0009` 继续保持 `Review20 / Outcome50`，`result` 保持 `Unknown`；5m 仍为 `FLAT`，不追多，观察 `64,000` 是否站稳，或在站不上且 1m 转 `TC-S` 时按反抽失败处理。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-12 BTC 64k Retest Conflict Watchlist

- 原因：根据 2026-07-12 20:24（UTC+8）BTCUSDT 15m / 5m / 1m 状态记录周期冲突；用户明确标记为 `Watchlist only`。
- 改动：从网页存档附带资源中提取原始 PNG，归档到 `screenshots/BTCUSDT/2026-07-12/2026-07-12_BTCUSDT_MultiTF_64k_Retest_Conflict_watchlist.png`。
- 改动：新增 `research/observations/2026-07-12_BTC_MultiTF_64k_Retest_watchlist.md`，记录 15m `FLAT`、5m `UP / TC-L`、1m `UP / S-ZONE / C-S` 的周期冲突。
- 改动：记录压力 `64,110-64,170`，支撑 `64,000-63,980` 与 `63,940-63,900`，并将回测 `64,000-63,980` 后的 10 根 K 线表现设为下一观察节点。
- 说明：本条不进入 `data/case_database.csv`，不新建 Case，不更新 CASE-0009 的正式 Outcome。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-13 SKYHYNIX CASE-0014 Crash Extension / Panel Conflict

- 原因：根据 2026-07-13 11:09-11:10（UTC+8）SKYHYNIXUSDT 多周期截图，归档 HTF 盘整破位、瀑布下跌、延伸阶段 `TC-S` 与 `A-L HMR95/100` 面板冲突。
- 改动：新增 `CASE-0014`，分类为 `HTF Breakdown / Crash Extension / Panel Signal Conflict`，状态为 `SignalCaptured / Open / Outcome10`，评级为 Gold Case candidate。
- 改动：归档两张截图到 `screenshots/SKYHYNIXUSDT/2026-07-13/`。
- 改动：新增 `research/findings/2026-07-13_SKYHYNIX_A-L_Last_TC-S_Extension_audit.md`，完成 `A-L` 语义、HUD `Last` 覆盖、HTF 反趋势过滤、显示开关与 `TC-S` 阶段分类审计。
- 说明：`A-L` 是 HTF Zone 观察标签，不是 `LONG`；当前 HTF 模式不应用 `cleanBearCtx`，HUD `Last` 也不区分趋势信号与反趋势警告。
- 说明：`EXTENDED / CRASH / NO CHASE`、HTF 趋势罚分和 TC Early/Mature/Extended 被记录为 DVCA 2.0 候选设计，未冒充为 v1.5.1 已实现逻辑。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-13 BTC CASE-0013 Failed Breakout / Bull Trap Outcome50

- 原因：根据 2026-07-12 20:24 初始截图、2026-07-12 22:54 突破跟踪、2026-07-13 10:01 Outcome50 截图，将原 BTC 64k Retest Conflict watchlist 升级为正式 Good Case。
- 改动：新增 `cases/failed_signals/CASE-0013_BTCUSDT_MultiTF_FailedBreakout_BullTrap.md`，分类为 `FailedBreakout / Bull Trap`。
- 改动：归档 Breakout 截图到 `screenshots/BTCUSDT/2026-07-12/2026-07-12_BTCUSDT_MultiTF_64150_Breakout_Outcome20.png`，归档 Outcome50 截图到 `screenshots/BTCUSDT/2026-07-13/2026-07-13_BTCUSDT_MultiTF_FailedBreakout_BullTrap_Outcome50.png`。
- 改动：在 `data/case_database.csv` 新增 `CASE-0013`，`result=Fail`，`state=Outcome50Recorded`，`lifecycle_status=Closed`。
- 改动：更新 `research/observations/2026-07-12_BTC_MultiTF_64k_Retest_watchlist.md`，补充 Outcome50 Upgrade 指向 `CASE-0013`。
- 结论：向上突破最终确认失败，形成明确 `Failed Breakout / Bull Trap`；后续执行不追空，等待 `63,500-63,635` 或 `63,690-63,800` 反抽失败确认。
- 保护：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-13 Cross-Market Follow-up：SKY Outcome20 / BTC Outcome50 Extension

- 原因：根据 2026-07-13 17:18（UTC+8）SKYHYNIXUSDT 与 BTCUSDT 跨市场截图，验证 Pattern/HMR 高分与实际执行质量必须分开评估。
- 改动：`CASE-0014` 更新为 `Outcome20Recorded / Review20 / Outcome50`，记录跌至约 1240 后反弹至约 1282，但15m尚未反转。
- 改动：`CASE-0013` 保持 `Fail / Outcome50Recorded / Closed`，追加跌破 63000 并在 62600-62700 附近暂稳的 Outcome50 延伸证据。
- 改动：新增 `research/findings/2026-07-13_Cross_Market_Pattern_vs_Execution_Quality.md`，归档 v1.5.5 候选字段 `Pattern Score`、`Context Alignment`、`Location Score`、`Execution Score`、`Extension Status`、`No-Chase Flag`。
- 边界：本次只更新案例、截图、研究文档与数据库；不修改 Pine、Signal Manual 或 Line Patterns。

## 2026-07-14 BTC Counter-Trend TC-L / HTF Conflict

- 原因：归档 BTCUSDT.P 在 1H `DN / A-S HMR100`、30m `FLAT / A-L HMR100`、15m `UP / TC-L` 之间的多周期冲突，验证 15m 反弹是否能升级为确认反转。
- 编号：用户请求 `CASE-0010`，但该编号已被 2026-07-08 BTC Context Shift 案例占用；为避免覆盖，本次分配 `CASE-0015`。
- 改动：新增 `CASE-0015`，分类为 `CounterTrendReversalAttempt`，状态为 `SignalCaptured / Open / Outcome10`，执行状态为 `NoTrade_WaitConfirmation`。
- 改动：归档 1m / 5m / 15m / 30m / 1H 三张截图到 `screenshots/BTCUSDT/2026-07-14/`。
- 改动：新增 `research/questions/2026-07-14_BTC_15m_TC-L_under_HTF_resistance.md`，并关联 HTF 执行信号时效性研究。
- 评级：Research A- / Trade C；ImprovementTag=`CounterTrendSignalDowngrade`。
- 边界：本次不修改 Pine、Signal Manual 或 Line Patterns。

## 2026-07-14 BTC CASE-0015 Outcome10 Recovery Follow-up

- 原因：根据 2026-07-14 20:27（UTC+8）BTCUSDT.P 多周期截图，记录 15m / 5m / 1m 重新同步 `UP + TC-L` 后的 Outcome10。
- 改动：`CASE-0015` 从 `SignalCaptured / Open / Outcome10` 推进为 `Outcome10Recorded / Review10 / Outcome20`。
- 改动：归档截图 `screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_TC-L_Outcome10_2027.png`。
- Finding：`S-ZONE` 对局部过度延伸给出警告，但基于该警告的趋势空已被支撑与结构收复否定；收复后的 `TC-L` 是更可靠的延续确认。
- 执行：不在约 63010 追多，优先等待 62920-62850 回测；持续运行在 62800 下方为失效条件。
- 评级：Good Case candidate，Result 保持 Unknown，继续等待 Outcome20。
- 边界：本次不修改 Pine、Signal Manual 或 Line Patterns。

## 2026-07-14 BTC CASE-0015 Outcome20 High-Level Extension

- 原因：根据 2026-07-14 21:00（UTC+8）BTCUSDT.P 15m / 5m / 1m 截图，记录突破 63000 / 63250、放量加速、63500 上方接受与 63800 测试后的动能减速。
- 并行更新处理：保留已存在的 20:48 Outcome20 / HTF Breakout Study，本次作为同一 Outcome20 的 High-Level Extension，不重复新建案例。
- 改动：`CASE-0015` 保持 `Outcome20Recorded / Review20 / Unknown`，下一步统一为 `Outcome50PendingHTFConfirmation`。
- 改动：归档 `screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_HighLevel_Extension_2100.png`。
- 改动：将 `CASE-0015` 正式归入 `gold_cases/BTC/TC/`，并更新 Signal Atlas 案例映射。
- 执行：已有多单管理利润；不在 63800-64000 追多；未跌破 63250 并完成 bearish retest 前不做空。
- 证据边界：21:00 截图未直接展示 1H，因此 HTF 状态保持待收盘确认，不提前判定。
- 边界：本次不修改 Pine、Signal Manual 或 Line Patterns。

## 2026-07-14 BTC CASE-0015 Outcome50 Pullback Active / Deep Pullback

- 原因：根据 2026-07-14 22:02 与 22:05（UTC+8）BTCUSDT.P 多周期截图，记录 64000 附近受阻后从 LTF 动能减弱到 1m `DN / TC-S` 的连续回踩过程。
- 改动：归档 `2026-07-14_BTCUSDT_MultiTF_PullbackActive_2202.png` 与 `2026-07-14_BTCUSDT_MultiTF_DeepPullback_2205.png`。
- 改动：`CASE-0015` 更新为 `Outcome50DeepPullback / Review20 / Outcome50HTFResolution`，`Result` 保持 `Unknown`。
- 研究结论：15m / 5m 仍为 `UP / TC-L` 时，1m `TC-S` 只确认低周期回踩空，不确认 HTF 趋势空。
- 候选分类：`LTF TC-S + HTF UP = PULLBACK-S`；`LTF TC-S + HTF DN = TREND-S`。该分类仅写入 Suggested Rule Update，不修改 v1.5.1 代码语义。
- 关键价位：反抽 `63640-63700`；支撑 `63500-63450`；下一观察 `63390-63300`；核心结构 `63250-63200`。
- 边界：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-14 BTC CASE-0015 Outcome50 Pullback Recovery

- 原因：根据 2026-07-14 22:18（UTC+8）BTCUSDT.P LTF 与 HTF 截图，完成 `CASE-0015` 的 Outcome50 复盘。
- 去重：两张 LTF 附件哈希相同，只归档一份；另归档一张 30m / 1H HTF 图。
- 结果：63550 附近支撑守住，未跌破 63300 / 63250；1m 收复约 63787 Trigger，从 `DN / TC-S` 恢复为 `UP / LATE-L HR85`。
- 生命周期：`Outcome50Recorded / Closed`；主信号结果：`Success`；Gold Case 保留。
- Finding：HTF `UP` 背景下的 LTF `TC-S` 被验证为 `PULLBACK-S`；`LATE-L` 方向正确但执行偏晚。
- 研究：新增 `MTF_PULLBACK_RECOVERY`、`HTF_STATE_LAG` 标签，并继续观察 `FLAT → RECOVERY-L → UP-PENDING → UP-CONFIRMED` 候选状态链。
- 边界：未修改 `indicator/dvca_v1_5_1.pine`、`docs/signal_manual.md`、`docs/line_patterns.md`。

## 2026-07-14 BTC CASE-0015 Post-Close Breakout Retest

- 原因：根据 2026-07-14 22:58 与 23:07（UTC+8）BTCUSDT.P 截图，为已关闭的 `CASE-0015` 增加突破回测与 HTF 延伸证据。
- 改动：归档 `2026-07-14_BTCUSDT_MultiTF_BreakoutRetest_2258.png` 和 `2026-07-14_BTCUSDT_30m_1H_BreakoutExtension_2307.png`。
- 状态：主案例保持 `Outcome50Recorded / Closed / Success`；关闭后跟踪状态为 `BreakoutRetestActive / NoChase`。
- 关键位：Trigger `64010-64090`；压力 `64100-64250`；支撑 `63920-63850`；核心恢复支撑 `63820-63780`。
- 研究：23:07 图中 30m / 1H 均为 `Ctx=UP`，为 `FLAT → RECOVERY-L → UP-PENDING → UP-CONFIRMED` 候选状态链提供后续证据。
- 边界：5m / 1m `L-ZONE HMR95` 仍是观察区，不等于正式 `LONG`；未修改 Pine、Signal Manual 或 Line Patterns。

## 2026-07-14 BTC CASE-0015 Lifecycle Correction / Outcome10

- 原因：用户明确指定本轮应按 15m K 线计为 `Outcome10Recorded`，下一次 Outcome20 在 2026-07-15 00:27 UTC+8 后；因此纠正此前过早推进到 Outcome20 / Outcome50 的生命周期标记。
- 编号：用户仍称 `CASE-0010`，但项目中的 `CASE-0010` 已属于 2026-07-08 BTC Context Shift；本轮继续更新实际对应的 `CASE-0015`，不覆盖旧案例。
- 改动：`CASE-0015` 修正为 `Outcome10Recorded / Review10 / Unknown`，Outcome10 结果为 Favorable，Direction Validated=Yes。
- 改动：初始区域约 62700-62900，最新观察价格约 64770；62920-63160、63500、64400 已突破并有量能确认。
- 改动：归档 23:46 LTF 与 30m/1H 两张截图，记录 5m/15m 强势但延伸、30m/1H Context 与 Last 冲突。
- 暂定评级：Good Case candidate / Gold Case candidate；当前执行 `NoChase`。
- 改进标签：`HTFSignalLag`、`StaleLastSignal`、`ContextLastConflict`、`CounterSignalAsRiskWarning`。
- 边界：未修改 Pine、Signal Manual 或 Line Patterns。

## 2026-07-20 BTC CASE-0016 Multi-Level Support Failure

- 原因：根据 2026-07-20 13:13（UTC+8）BTCUSDT 五周期截图，记录多级支撑失守及 1H 从 UP 降为 FLAT。
- 路径：64539-64584 收复失败 → 跌破 64439-64406 → 5m DN/TC-S → 跌破 64239-64170 → 测试 64013-63996。
- 分支：`Outcome11BearishBreakdown`；新增 `Outcome12Active / Multi-Level Support Failure`。
- 生命周期：主案例保持 `Outcome20Recorded / Review20 / Outcome50 / Unknown`。
- 执行：方向偏空但 1m/5m 超卖，不在约 64080 追空；等待 64170-64266 或 64380-64445 反弹拒绝，或 63996 跌破后的失败回测。
- 保护：未修改任何 Pine Script、Signal Manual 或 Line Patterns。

## 2026-07-16 BTC CASE-0016 MTF Bearish Transition

- 原因：根据 2026-07-16 20:47（UTC+8）BTCUSDT 多周期截图，记录 30m/15m/5m/1m 同步转 DN、1H 仍为 FLAT 的空头转折。
- 改动：新增 `CASE-0016`，状态为 `SignalCaptured / Open / Outcome10`，Result 保持 Unknown，暂定为 Good Case candidate。
- 改动：归档两张原始截图到 `screenshots/BTCUSDT/2026-07-16/`，记录支撑 `63800-63780`、下一支撑 `63500-63300`、压力 `64050-64150` 与核心压力 `64300-64500`。
- 执行：不在支撑附近追空；优先等待反抽失败和 5m/1m 空头确认；无结构收复前不做逆势多。
- 版本边界：截图运行 DVCA 1.5.1；`DN-PENDING` 是研究建议，不是代码现有状态。本案例不计入 v1.5.4 高周期正式样本，需复现。
- 保护：未修改任何 Pine Script、Signal Manual 或 Line Patterns。

## 2026-07-19 BTC CASE-0016 15m Bearish Downgrade

- 原因：记录 20:52 截图中的 15m 降级、5m 空头延续与 1m 逆势修复。
- 数据边界：当前仅有 1m/5m/15m；30m/1H 的 15:10 状态标记为 `STALE / NOT CURRENT`。
- 状态：`15m DN / 5m DN / 1m FLAT`；Current Recovery Branch=`Outcome10AtRisk`。
- 生命周期：主案例保持 `Outcome20Recorded / Review20 / Outcome50 / Unknown`。
- 保护：未修改任何 Pine Script、Signal Manual 或 Line Patterns。

## 2026-07-17 BTC CASE-0016 Outcome10 Recovery Failure

- 原因：根据 2026-07-17 12:28（UTC+8）BTCUSDT 多周期截图，记录 63780 初次守住后的恢复最终失败，以及五周期重新转为空头对齐。
- 路径：收复 64150/64500 → 64750-64800 受阻 → 64500-64430 失守 → 跌破 64300、64150-64000 与 63780 → 当前约 63341。
- 生命周期：`Outcome10Recorded / Review10 / Outcome20`；Recovery Branch=Failed，Bearish Continuation=Active，Result 保持 Unknown。
- 执行：不在 `63300-63200` 支撑附近追空；优先等待 `63500-63620` 或 `63770-63900` 反抽拒绝，或 63200 跌破后的失败回测。
- 版本边界：截图继续运行 DVCA 1.5.1；本记录不计入 v1.5.4 正式专项样本，不据此修改代码。
- 保护：未修改任何 Pine Script、Signal Manual 或 Line Patterns。

## 2026-07-17 BTC CASE-0016 Failed Low-Level Repair

- 原因：根据 2026-07-17 16:07-16:08（UTC+8）BTCUSDT 跟踪截图，记录价格进入 62800-62600 延伸区后的低周期修复失败。
- 路径：跌破 63200/63000 → 1m/5m L-ZONE HMR100 → 1m DN 转 FLAT → 未收复 62950-63080 → 1m TC-S → FLAT 返回 DN。
- 分支：Low-Level Repair=Failed；Bearish Continuation=Active；Current Execution Branch=Bearish Reconfirmation above Core Low。
- 生命周期：保持 `Outcome10Recorded / Review10 / Outcome20`，本次只标记 Outcome20 Active，Result 继续为 Unknown。
- 执行：不在 62800 附近追空；等待反抽拒绝或 62600 跌破后的失败回测。
- 版本边界：截图运行 DVCA 1.5.1，不计入 v1.5.4 正式专项样本。
- 保护：未修改任何 Pine Script、Signal Manual 或 Line Patterns。

## 2026-07-17 BTC CASE-0016 Outcome20 / Second Low-Level Repair

- 原因：根据 2026-07-17 19:10（UTC+8）BTCUSDT 全周期截图，记录 62800 再次守住后的第二次低周期修复，以及 5m 转 UP 后的首次回踩。
- 生命周期：`Outcome20Recorded / Review20 / Outcome50`；原始 SHORT 方向 Favorable，最终 Result 继续为 Unknown。
- 路径：第二次修复 → 1m UP → 收复 62900/63000 → 5m DN→FLAT→UP / TC-L → 63150 附近 1m S-ZONE/C-S → 1m FLAT。
- 执行：高周期仍 DN，但 5m 空头执行暂停；等待 1m 回踩确认，不把 S-ZONE 当作 SHORT。
- 版本边界：截图运行 DVCA 1.5.1，不计入 v1.5.4 正式专项样本。
- 保护：未修改任何 Pine Script、Signal Manual 或 Line Patterns。

## 2026-07-18 BTC CASE-0016 Full MTF Recovery First Pullback

- 原因：根据 2026-07-18 21:07-21:12（UTC+8）BTCUSDT 五周期截图，记录第二次修复升级为 Full MTF Recovery。
- 路径：62850 支撑 → 收复 63000/63500/63780/64000 → 5m/15m/30m/1H 转 UP → 1m FLAT 首次回踩。
- 分支：Previous Bearish Continuation 在方向层失效；Current Recovery Branch=`Outcome10Active / Strong Recovery / HTF Upgrade Confirmed`。
- 生命周期：主案例仍为 `Outcome20Recorded / Review20 / Outcome50 / Unknown`。
- 执行：1m FLAT 时等待，不追多；四个较高周期 UP 时不主动逆势做空。
- 保护：未修改任何 Pine Script、Signal Manual 或 Line Patterns。

## 2026-07-18 BTC CASE-0016 First Pullback Held / LTF Reconfirmation

- 原因：根据 2026-07-18 22:04（UTC+8）BTCUSDT 同步五周期截图，记录 Full MTF Recovery 后的首次回踩结果。
- 路径：回踩 64000 守住 → 5m L-ZONE HMR95 → 1m TC-L → 1m FLAT 返回 UP → 五周期多头对齐恢复。
- 分支：`Outcome10Active / Strong Recovery / HTF Upgrade Confirmed / First Pullback Held / LTF Reconfirmation Completed`。
- 生命周期：主案例保持 `Outcome20Recorded / Review20 / Outcome50 / Unknown`。
- 执行：结构确认但不在 64130-64150 压力附近追多；等待回踩或突破回测。
- 保护：未修改任何 Pine Script、Signal Manual 或 Line Patterns。

## 2026-07-18 BTC CASE-0016 64150 Breakout Attempt

- 原因：根据 2026-07-18 22:31（UTC+8）BTCUSDT 两张近同步五周期截图，记录首次回踩守住后的突破尝试。
- 路径：Full MTF UP → First Pullback Held → 1m TC-L → 5m/15m/30m 动能扩张 → 价格交易至 64150 上方。
- 分类：`64150 Breakout Attempt / Breakout Confirmation Pending`；尚无收盘、站稳或成功回测确认。
- 分支：`Outcome10Active / Strong Recovery / Full MTF UP / First Pullback Held / LTF Reconfirmation Completed`。
- 生命周期：主案例保持 `Outcome20Recorded / Review20 / Outcome50 / Unknown`。
- 执行：No-Chase；等待 64120-64095 回测确认，或 64237.7 突破后的成功回测。
- 保护：未修改任何 Pine Script、Signal Manual 或 Line Patterns。

## 2026-07-19 BTC 30m 常规多头背离漏报观察

- 原因：记录 30m 价格 Lower Low、MACD Higher Low 但 DVCA 1.5.1 未打印背离事件的历史样本。
- 分类：`False Negative / NeedsCodeTrace / ExcludedPendingReproduction`。
- 归因边界：视觉背离已人工确认；Pivot 配对、容差、阈值或门控中的具体根因尚未确认。
- 预期事件：候选 `DIV-L-WARN`，右侧 Pivot 确认后 `DIV-L-CONFIRMED`；不自动生成 LONG。
- 验证：先在 v1.5.4 重放并记录全部 Pivot、配对、阈值和 suppression reason。
- 保护：未修改任何 Pine Script、Signal Manual 或 Line Patterns；未写入正式案例数据库。

## 2026-07-19 BTC CASE-0016 HTF UP / LTF Pullback Follow-up

- 原因：记录 15:10 五周期截图中的高周期多头结构与低周期空头回调。
- 状态：1H/30m/15m UP，1m/5m DN；分支为 `Outcome10Active / LTF Pullback inside HTF UP`。
- 背离：30m 视觉多头背离后续已收复 64078、64170、64438 并扩展至 64800-64900，更新为 `Bullish Follow-Through Confirmed / Regression Test Required`。
- 生命周期：主案例保持 `Outcome20Recorded / Review20 / Outcome50 / Unknown`。
- 保护：未修改任何 Pine Script、Signal Manual 或 Line Patterns。
