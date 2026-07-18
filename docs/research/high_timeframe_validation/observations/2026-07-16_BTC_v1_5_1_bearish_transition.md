# BTC v1.5.1 多周期空头转折观察

## 记录信息

- 日期：2026-07-16
- 时间：20:47 UTC+8
- 标的：BTCUSDT
- 对应普通案例：`CASE-0016`
- 截图指标版本：DVCA 1.5.1
- 当前正式基线：DVCA v1.5.4
- 专项准入状态：ExcludedPendingReproduction

## 观察现象

- 30m、15m、5m、1m 已显示 `Ctx=DN`，并由 TC-S 延续。
- 1H 仍显示 `Ctx=FLAT`，最新事件为 `A-S HMR95`，动能偏空。
- 该差异提出一个待验证问题：1H 是否需要在 FLAT 与 DN 之间显示 `DN-PENDING`，还是现有表现只是合理的高周期收盘确认延迟。

## 证据限制

- 截图运行的是 DVCA 1.5.1，不能据此判断 v1.5.4 存在相同问题。
- 缺少趋势启动、结构变化和各信号真实可见时间的逐根 K 线标注。
- Outcome10、Outcome20 已完成历史版本跟踪；Outcome50 尚未完成。
- 因此本观察不写入 `data/high_timeframe_validation/htf_case_database.csv`，不计入正式专项样本数。

## v1.5.4 复现验收标准

1. 使用 `indicator/current/dvca_v1_5_4.pine` 对同类行情重新截图。
2. 同时保留 1H、30m、15m，并统一截图时间与时区。
3. 记录 30m 首次转 DN、15m 首次 TC-S 和 1H 状态切换的真实确认时间。
4. 区分正常高周期收盘等待、Zone pivot 显示偏移与机制性状态滞后。
5. 完成 Outcome10/20/50 后再判断是否需要 `DN-PENDING` 候选状态。

## 当前结论

这是一个高价值的历史版本观察，但不是 v1.5.4 缺陷证据。当前只保留 `HTF_DN_PENDING` 与 `TC_S_TREND_CONFIRMATION` 研究标签，不启动 v1.5.5 代码修改。

## Outcome10 历史版本跟踪（2026-07-17 12:28 UTC+8）

- 价格先从 63780 支撑反弹，收复 64150 与 64500，并使 1m / 5m 转 UP。
- 反弹在 64750-64800 附近受阻，随后跌破 64500-64430、64300、64150-64000 和 63780。
- 最新截图中 1H、30m、15m、5m、1m 全部为 DN；恢复分支记为 Failed，空头延续记为 Active。
- 这说明 v1.5.1 图中的 `FLAT → 候选 DN-PENDING → DN` 路径已出现，但版本限制不变：不得据此确认 v1.5.4 存在同样的机制或需要代码修改。
- 下一步仍是用 v1.5.4 复现，并记录 1H 从 FLAT 切换到 DN 的真实确认时间。

## Outcome20 Active 历史版本跟踪（2026-07-17 16:07 UTC+8）

- 价格进一步跌破 63200 与 63000，到达 `62800-62600` 延伸观察区。
- 1m / 5m 出现 L-ZONE HMR100，1m 一度从 DN 转为 FLAT，但修复未能收复 `62950-63080`。
- 1m 随后重新出现 TC-S 并回到 DN，五周期 DN 对齐恢复，低周期修复分支记为 Failed。
- 当前阶段分类为 `Bearish Reconfirmation above Core Low`，但因价格接近 `62800-62745` 支撑，执行仍是 No-Chase。
- 本节尚未完成完整 Outcome20，只作为中间路径记录；最终结果继续保持 Unknown。
- 版本限制不变：截图运行 DVCA 1.5.1，不能计入 v1.5.4 正式专项样本。

## Outcome20 历史版本结论（2026-07-17 19:10 UTC+8）

- 原始 SHORT 方向为 Favorable，价格已经到达 `62800-62600` 延伸观察区。
- 62800 再次守住后出现第二次低周期修复：1m 转 UP，随后 5m 从 DN 经 FLAT 转为 UP，并出现 TC-L。
- 反弹至 63150 附近后，1m 出现 S-ZONE / C-S 并回到 FLAT；这是 5m 转 UP 后的首次回踩，不是正式 SHORT。
- 高周期仍为 1H/30m/15m DN，5m UP 与高周期形成冲突；空头背景继续保留，但执行周期暂停追空。
- Outcome20 正式记录为 `Favorable for original SHORT direction / Second Low-Level Repair Active`，生命周期推进到 Review20，最终 Result 仍为 Unknown。
- 该记录继续属于 DVCA 1.5.1 历史观察，不计入 v1.5.4 正式专项样本。

## Full MTF Recovery 历史版本跟踪（2026-07-18 21:07-21:12 UTC+8）

- 62850 附近支撑有效后，价格依次收复 63000、63500、63780 和 64000。
- 5m、15m、30m、1H 依次转为 UP；15m/5m 最新 TC-L，说明第二次低周期修复已经升级为高周期方向确认。
- 1H/30m Context 已为 UP，但 Last 仍显示 A-S HMR95/100，继续形成 Context 与 Last 的陈旧信号冲突观察。
- 1m 当前为 FLAT、Last TC-L，属于 Full MTF Bullish Alignment 后的首次回踩；恢复分支先记为 Outcome10Active，不提前判定成功。
- 原 Bearish Continuation 在 5m/15m/30m/1H 方向层失效，但主案例仍等待 Outcome50 才能形成最终结论。
- 版本限制不变：这是 DVCA 1.5.1 历史证据，不计入 v1.5.4 正式专项样本。
