# Gold Case Candidate：CASE-0015 BTC HTF Breakout Recovery

## 基本信息

- 候选类型：BTC / TC / HTF Recovery
- 对应案例：CASE-0015
- 日期：2026-07-14
- 品种：BTCUSDT.P
- 交易所：Binance
- 指标：DVCA 1.5.1
- 主信号：15m / 5m TC-L
- 当前结果：Unknown（Outcome10 Favorable）
- 生命周期：Outcome10Recorded / Review10
- 下一步：Outcome20 after 2026-07-15 00:27 UTC+8
- 暂定评级：Good Case candidate / Gold Case candidate
- 完整案例：`cases/CASE-0015_BTCUSDT.P_MultiTF_15m_TC-L_HTF_A-S-A-L_Conflict.md`

## 核心信号链

```text
1H DN / A-S HMR100
→ 30m FLAT / A-L HMR100
→ 15m L-ZONE / TC-L
→ 1m 结构回收 / TC-L
→ 5m / 15m 同步 UP / TC-L
→ 突破 63000 / 63250
→ 放量加速并接受 63500
→ 测试 63800
→ LTF 过度延伸 / 动能减速
→ 1m UP 转 FLAT / Pullback Active
→ 跌破 63800 / 63600
→ 1m DN / TC-S / Deep Pullback
→ 63550 附近支撑守住
→ 收复 63787 Trigger
→ 1m 返回 UP / LATE-L HR85
→ Pullback Recovery Confirmed
```

## Gold 候选原因

- 完整记录了 HTF 偏空、低周期修复、结构收复、TC-L 同步、放量突破与过度延伸的演化。
- 能清楚说明 `S-ZONE` 警告不等于反向执行，以及结构收复后 `TC-L` 的延续确认价值。
- 能区分趋势方向、过度延伸警告和实际执行质量。
- 暴露了 1H close-confirmation delay、`UP-PENDING` 候选状态和反趋势 HMR100 显示优先级问题。

## 关键截图

- Initial LTF：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_15m_TC-L_LTF_1923.png`
- Initial HTF：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_30m_AL_15m_TCL_1927.png`
- Outcome10：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_TC-L_Outcome10_2027.png`
- Outcome10 HTF Study：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_HTF_Breakout_Study_2048.png`
- Outcome10 Extension：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_HighLevel_Extension_2100.png`
- Outcome10 Pullback Active：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_PullbackActive_2202.png`
- Outcome10 Deep Pullback：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_DeepPullback_2205.png`
- Outcome10 Recovery：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_PullbackRecovery_LATE-L_2218.png`
- Outcome10 HTF：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_30m_1H_HTF_StateLag_2218.png`
- Outcome10 Breakout Retest：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_BreakoutRetest_2258.png`
- Outcome10 HTF Extension：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_30m_1H_BreakoutExtension_2307.png`
- Outcome10 Favorable LTF：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_Outcome10_Favorable_2346.png`
- Outcome10 Context / Last Conflict：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_30m_1H_Outcome10_ContextLastConflict_2346.png`

## 执行原则

- 已有多单以利润管理为主。
- 不在 `63800-64000` 过度延伸区追多。
- 不因 1m `S-ZONE HMR100` 和动能减速直接做空。
- 只有跌破 `63250` 并完成 bearish retest，才重新评估空头执行。
- 15m / 5m 仍为 `UP` 时，1m `TC-S` 只归类为候选 `PULLBACK-S`；不得当作 `TREND-S`。

## 待验证项

- 21:00 的 1H K 线收盘后，Context 是否从 `FLAT` 升级为 `UP`。
- 1H `A-S HMR100` 是否仍覆盖 recovery state。
- 深度回踩后，`63500-63450` 与 `63300-63200` 是否守住。
- HTF 是否同步转 `DN`；未同步前保持 `PULLBACK-S` 研究分类。
- Outcome10 已确认主信号方向 Favorable；1m `LATE-L` 单独记录为执行确认偏晚，最终 Result 仍为 Unknown。
- 继续将 1H `FLAT / A-S HMR100` 与已收复结构之间的差异作为 `HTF_STATE_LAG` 研究问题，不再阻止本案例关闭。

## Outcome10 Validation

```text
Pullback Recovery Confirmed
→ retest 64000
→ 5m / 1m L-ZONE HMR95
→ Trigger 64010-64090 test
→ 30m / 1H Ctx UP
→ HTF Breakout Extension
```

- 22:58 跟踪状态：`BreakoutRetestActive / NoChase`。
- 23:07 HTF 图显示 30m / 1H 均为 `Ctx=UP`，为此前 `HTF_STATE_LAG` 提供后续状态转换证据。
- 23:46 最新观察价约 64770，62920-63160、63500 与 64400 均已突破并有量能确认。
- 当前记录为 `Outcome10Recorded / Review10`，不能提前写成 Outcome20 / Outcome50 或最终 Success。
- 单独 `L-ZONE` 仍不解释为正式进场信号；高位 `S-ZONE / C-S` 先作为风险警告。
