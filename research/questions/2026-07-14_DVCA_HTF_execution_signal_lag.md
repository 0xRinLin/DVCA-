# DVCA v1.5.4 在 30min / 1H 上为什么执行信号偏少且偏晚？

## 基本信息

- 日期：2026-07-14
- 相关标的：BTCUSDT / ETHUSDT / SOLUSDT
- 相关周期：30min / 1H / 15min / 5min / 1min
- 当前状态：Open
- 问题类型：HTF Signal Timeliness / Execution Quality
- 当前评级：部分通过，但高周期时效性不合格

## 问题描述

结合目前已经观察到的 BTC、ETH、SOL 多周期案例，DVCA v1.5.4 在 30min 和 1H 上出现两个相互关联但需要分开统计的问题：

1. 可执行信号偏少：LONG、SHORT、PB、TC 在高周期上不够及时。
2. 部分信号确认偏晚：TC-L / TC-S 往往在趋势已经运行一段距离后才出现。

这不是简单的“参数太严格”问题。更准确的方向是：

```text
1H 负责背景状态
30min 负责结构确认
15min / 5min 负责执行确认
1min 负责精细入场和止损管理
```

## 已观察到的现象

| 检查项 | 30min | 1H | 判断 |
| --- | ---: | ---: | --- |
| L-ZONE / S-ZONE | 偶尔出现 | 相对更常见 | 观察信号并非完全不足 |
| LONG / SHORT | 偏少 | 明显偏少 | 执行信号不足 |
| PB-L / PB-S | 偏少 | 很少形成完整链 | 候选容易过期或无法确认 |
| TC-L / TC-S | 趋势形成后才出现 | 往往已运行较远 | 延续信号偏晚 |
| EXH-L / EXH-S | 有时较晚 | 可能在趋势尾端才确认 | 警告价值下降 |
| 跨周期配合 | 30min 尚可作为结构层 | 1H 难以提供及时方向 | 高周期联动不足 |

## 研究问题

1. 30min / 1H 的执行信号偏少，究竟是信号设计问题，还是周期职责定位问题？
2. TC-L / TC-S 在高周期上确认偏晚，主要来自 Pivot 右侧确认、确认链过长，还是跨周期共用参数？
3. 1H 是否应该减少 LONG / SHORT 执行标签，转而提高 BULL / BEAR / RANGE / TRANSITION 背景覆盖率？
4. 30min 是否应该承担结构转折候选、FT/PB 候选、趋势延续空间判断，而不是强行承担精确入场？
5. Zone Watch 到 Executable 之间是否需要新增中间状态，避免早期线索沉默、最终确认又太晚？

## 暂时不能下结论的原因

当前判断来自多周期观察，但还没有形成足够数量的标准化统计。

不能直接得出以下结论：

- 直接降低阈值。
- 直接缩短 Pivot 参数。
- 直接增加 1H LONG / SHORT 标签。
- 直接把 v1.5.5 改成更敏感版本。

原因是这些做法可能重新引入 v1.6.x 类似问题：RANGE 噪音、标签过密、不同标的表现不一致。

## 需要收集的案例

建议至少收集：

- BTCUSDT 30min HTF 信号时效性案例 10 个。
- ETHUSDT 30min HTF 信号时效性案例 10 个。
- SOLUSDT 30min HTF 信号时效性案例 10 个。
- BTCUSDT 1H 背景状态覆盖案例 10 个。
- ETHUSDT 1H 背景状态覆盖案例 10 个。
- SOLUSDT 1H 背景状态覆盖案例 10 个。

每个案例必须记录：

- originBar
- confirmedBar
- executableBar
- 信号类型
- 是否处于 RANGE
- 是否高低周期冲突
- 信号出现后是否仍有至少 1.5R 潜力
- 是否因 Pivot 回画导致视觉提前

## 后续动作

1. 不修改 Pine。
2. 不修改 Signal Manual。
3. 不修改 Line Patterns。
4. 先建立 v1.5.5 HTF Accuracy Patch 研究候选。
5. 等至少 30 个相关案例后，再判断是否升级为正式规则修改。

## 新增关联案例

- `CASE-0015`：BTCUSDT.P，1H `DN / A-S HMR100`、30m `FLAT / A-L HMR100`、15m `UP / TC-L`。
- 研究用途：验证 HTF 与 15m 冲突时，反趋势 TC 是否应降级执行评分。
- 专项问题：`research/questions/2026-07-14_BTC_15m_TC-L_under_HTF_resistance.md`。


## Evidence Update：CASE-0016 Bearish Continuation Failure（2026-07-16）

- 案例：`CASE-0016`
- 时间：2026-07-16 22:30 UTC+8
- 类型：Failed Continuation / Recovery Branch SignalCaptured

### 观察

原路径为 `1H FLAT + 30m/15m/5m/1m DN + TC-S`，价格测试 `63780` 支撑。Outcome10 中，`63780` 支撑守住，价格收复 `64150` 与 `64500`，1m / 5m 转为 UP，而 15m / 30m / 1H 返回或保持 FLAT。

### 对研究问题的意义

该案例支持继续研究 HTF transition 中的双分支状态：

```text
Bearish Continuation Attempt -> Failed Continuation
Recovery Branch -> SignalCaptured
```

它说明 1H / 30m 仍为 FLAT 时，低周期 DN / TC-S 可以快速失败；如果没有 Recovery Branch 状态，系统容易把短线空头延续误读为高周期趋势确认。

### 后续观察

等待 Outcome20 / Outcome50，重点观察：

- 64850-65000 阻力区是否拒绝价格。
- 64600-64500 是否转为有效支撑。
- 64150-64000 核心区是否守住。
- 跌回 63780 下方是否重新恢复空头延续。

## Evidence Update：Recovery Branch Failed（2026-07-17）

- 案例：`CASE-0016`
- 时间：2026-07-17 12:28 UTC+8
- 类型：Recovery Failure / Bearish Continuation Reactivated

### 后续路径

恢复分支收复 64150 与 64500 后，在 64750-64800 附近受阻；随后依次失守 64500-64430、64300、64150-64000 和 63780。最新截图中 1H、30m、15m、5m、1m 全部为 DN。

### 对研究问题的意义

1. 低周期从 DN 恢复到 UP 只能建立恢复分支，不能在高周期尚未确认时直接定义反转完成。
2. 关键结构重新失守后，恢复分支应明确标记为 Failed，并恢复 Bearish Continuation 的活动状态。
3. Context 的方向确认与执行位置仍须分离；五周期 DN 时若价格已靠近支撑且 RSI 偏低，依然应显示 No-Chase。
4. 本证据来自 DVCA 1.5.1，只能用于形成 v1.5.4 复现问题，不能直接作为 v1.5.5 修改依据。

### 下一步

- Outcome20 检查 63200 是否有效跌破及 63500-63620 反抽是否被拒绝。
- 使用 v1.5.4 复现同类 `FLAT → DN-PENDING → DN` 路径，记录真实确认时间。

## Evidence Update：Failed Low-Level Repair（2026-07-17 16:07）

- 案例：`CASE-0016`
- 类型：Low-Level Repair Failed / Bearish Reconfirmation

价格跌破 63200 与 63000 后进入 `62800-62600` 区域，1m / 5m 出现 L-ZONE HMR100。1m 一度进入 FLAT，但未能收复 `62950-63080`，随后重新出现 TC-S 并返回 DN。

该路径进一步说明：

1. 空头背景中的高分 L-ZONE 只能建立修复观察分支，不能自动覆盖 HTF DN。
2. 低周期修复失败应由结构收复失败与 Context 返回 DN 共同确认，不能只看单个 TC-S 标签。
3. Bearish Reconfirmation 与追空授权必须分离；接近 62800 支撑时仍应维持 No-Chase。
4. 本记录尚未达到完整 Outcome20，继续等待后续 K 线。
