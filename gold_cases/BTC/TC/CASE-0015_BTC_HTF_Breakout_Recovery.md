# Gold Case：CASE-0015 BTC HTF Breakout Recovery

## 基本信息

- Gold 类型：BTC / TC / HTF Recovery
- 对应案例：CASE-0015
- 日期：2026-07-14
- 品种：BTCUSDT.P
- 交易所：Binance
- 指标：DVCA 1.5.1
- 主信号：15m / 5m TC-L
- 当前结果：Unknown
- 生命周期：Outcome20Recorded / Review20
- 下一步：Outcome50PendingHTFConfirmation
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
→ 等待 1H 收盘确认
```

## Gold 标记原因

- 完整记录了 HTF 偏空、低周期修复、结构收复、TC-L 同步、放量突破与过度延伸的演化。
- 能清楚说明 `S-ZONE` 警告不等于反向执行，以及结构收复后 `TC-L` 的延续确认价值。
- 能区分趋势方向、过度延伸警告和实际执行质量。
- 暴露了 1H close-confirmation delay、`UP-PENDING` 候选状态和反趋势 HMR100 显示优先级问题。

## 关键截图

- Initial LTF：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_15m_TC-L_LTF_1923.png`
- Initial HTF：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_30m_AL_15m_TCL_1927.png`
- Outcome10：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_TC-L_Outcome10_2027.png`
- Outcome20 HTF Study：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_HTF_Breakout_Study_2048.png`
- Outcome20 Extension：`screenshots/BTCUSDT/2026-07-14/2026-07-14_BTCUSDT_MultiTF_HighLevel_Extension_2100.png`

## 执行原则

- 已有多单以利润管理为主。
- 不在 `63800-64000` 过度延伸区追多。
- 不因 1m `S-ZONE HMR100` 和动能减速直接做空。
- 只有跌破 `63250` 并完成 bearish retest，才重新评估空头执行。

## 待验证项

- 21:00 的 1H K 线收盘后，Context 是否从 `FLAT` 升级为 `UP`。
- 1H `A-S HMR100` 是否仍覆盖 recovery state。
- 高位动能减速后，回踩是否保持 `63500 / 63250`结构。
- Outcome50 确认后，再决定最终 `Success / Late / NoTrade / Fail`。
