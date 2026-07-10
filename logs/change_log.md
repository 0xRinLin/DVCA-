# DVCA Change Log

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
