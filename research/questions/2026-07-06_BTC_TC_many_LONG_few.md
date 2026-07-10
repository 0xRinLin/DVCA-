# BTC 在趋势行情里为什么 TC-L 很多，但 LONG 很少？

## 基本信息

- 日期：2026-07-06
- 品种：BTCUSDT
- 相关周期：1m / 5m / 15m / 30m
- 当前状态：Open
- 问题类型：TrendContinuation vs Reversal

## 问题描述

BTC 在趋势行情里经常出现 TC-L / TC-S，但 LONG / SHORT 相对较少。

这说明当前 DVCA v1.5.1 在 BTC 的趋势段中，可能更容易识别“趋势延续”，而不是“背离反转后的严格突破”。

## 暂时不能下结论的原因

单张图只能说明发现了一个现象，不能说明这个现象稳定存在。

当前还不知道：

- 是 BTC 本身趋势段回踩浅，导致 TC 更多。
- 是 Pivot 背离条件较严格，导致 L-ZONE / S-ZONE 少。
- 是 Zone 出现了，但没有通过 LONG / SHORT 的严格突破过滤。
- 是时间周期太小，1m 加速段还没完成后续结构。

## 需要收集的案例

建议至少收集：

- BTCUSDT 30m TC-L / TC-S 案例 10 个。
- BTCUSDT 15m TC-L / TC-S 案例 10 个。
- BTCUSDT 出现 L-ZONE / S-ZONE 但没有 LONG / SHORT 的案例 10 个。
- BTCUSDT 标准 LONG / SHORT 案例 5 个。

## 关联截图

先放 Raw，不急着录入数据库：

```text
screenshots/BTCUSDT/2026-07-06/
```

建议保存：

```text
BTC_1m_before.png
BTC_1m_after.png
BTC_5m_context.png
BTC_15m_context.png
BTC_30m_context.png
```

## 可能的案例归类

- 如果最终形成 TC-S 并继续跌：`TrendContinuation`
- 如果最终形成 EXH-L → L-ZONE → LONG：`Reversal`
- 如果最终只是震荡：不录数据库
- 如果出现 E-L / E-S 后失败：`FailedBreakout`

## 后续动作

1. 保存 before / after 截图。
2. 不急着录入 `case_database.csv`。
3. 等 30-80 根 K 后判断结果。
4. 如果形成完整信号链，再用 `scripts/add_case.py` 录入 Candidate。
5. 累积足够样本后，在 `research/findings/` 写阶段性发现。

