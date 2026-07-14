# Hypothesis：v1.5.5 HTF Accuracy Patch 应从周期职责分层开始

## 基本信息

- 日期：2026-07-14
- 状态：Hypothesis
- 关联问题：`research/questions/2026-07-14_DVCA_HTF_execution_signal_lag.md`
- 代码边界：本文不修改 DVCA Pine，不修改 Signal Manual，不修改 Line Patterns。

## 核心假设

DVCA v1.5.4 在 30min / 1H 上的主要问题不是单纯“信号太少”，而是：

```text
高周期职责不清
+ 确认链过长
+ Pivot 右侧确认带来的真实时间滞后
+ 同参数跨周期使用
+ Zone 到执行信号之间缺少候选状态
```

因此，v1.5.5 的修复方向不应是整体放宽阈值，而应是高周期职责分层。

## P0 假设

### 1H 职责

1H 应优先输出：

- BULL / BEAR / RANGE / TRANSITION
- Zone Watch / Zone Valid
- 趋势强度
- 结构确认方向
- 是否允许低周期做多或做空

1H 不应追求像 5min 那样频繁输出 LONG / SHORT。

### 30min 职责

30min 应优先输出：

- 结构转折候选
- 结构已确认
- FT / PB 候选与确认
- 趋势延续是否仍有空间
- 信号失效位

### 15min / 5min 职责

15min / 5min 应负责：

- LONG / SHORT
- PB-L / PB-S
- 实际进场确认

## 时间字段假设

未来所有结构或信号都应区分：

| 字段 | 含义 |
| --- | --- |
| `originBar` | 结构最初发生的位置 |
| `confirmedBar` | 条件真正确认的位置 |
| `executableBar` | 实际可以采取交易行动的位置 |

准确性评估必须以 `executableBar` 为准，不能以回画后的 Pivot 位置计算。

## 候选状态假设

建议验证内部状态链：

```text
WATCH
→ CANDIDATE
→ CONFIRMED
→ EXECUTABLE
→ INVALID / EXPIRED
```

这些状态用于提前记录线索，但不直接等同于 LONG / SHORT。

## 验证标准候选

| 验收项 | 建议标准 |
| --- | --- |
| 1H 背景覆盖率 | 有效行情中至少 80% K 线具备明确背景状态 |
| 1H 沉默区 | 不应连续长时间既无背景方向也无风险状态 |
| 30min 结构确认延迟 | 相比 v1.5.4 中位数减少至少 1 根 K 线 |
| LONG / SHORT 滞后 | 信号出现后仍应具备合理结构止损和至少 1.5R 潜力 |
| RANGE 误判 | 不得因增加信号而明显高于 v1.5.4 |
| 高低周期冲突 | 冲突信号必须降级或被禁止 |
| Pivot 真实性 | 回测以确认位置计算，不得用回画位置 |
| 标的兼容性 | BTC、ETH、SOL 分别验证，不能只针对 SOL 调参 |
| 图面密度 | 保持接近 v1.5.4，不重现 v1.6.x 噪音问题 |

## 当前结论

当前只是假设，不是最终规则。

只有当至少 30 个相关案例支持该方向后，才能进入 Suggested Rule Update 的正式评估。
