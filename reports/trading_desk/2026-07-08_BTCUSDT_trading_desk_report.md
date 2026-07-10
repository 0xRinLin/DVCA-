# DVCA Trading Desk Report

**标的：BTCUSDT Perpetual**
**分析时间：2026-07-08 17:17 左右（截图时间，UTC+8）**
**周期：1D → 30m → 5m → 1m**

## 一、Market State（市场状态）

| 周期 | 当前状态 | 判断 |
| --- | --- | --- |
| 1D | 回落中，但长期结构未完全破坏 | 偏多转弱 |
| 30m | Ctx = DN，跌破短期均线 | Transition → Trend Down |
| 5m | TC-S 主导 | 空头延续 |
| 1m | TC-S 后小幅反抽 | 空头中的弱修复 |

**综合状态：**

```text
Higher Timeframe：Transition → Down
Execution Timeframe：Trend Down
Entry Timeframe：Momentum Recovery（不是反转）
```

**结论：当前不是多头行情，而是空头主导行情。**

## 二、Signal Chain（信号链）

根据两张图，信号链整理为：

```text
S-ZONE
    ↓
C-S
    ↓
TC-S
    ↓
跌破EMA20
    ↓
跌破EMA50
    ↓
加速下跌
    ↓
1m出现动能缓和
```

注意这里没有出现：

- `LONG`
- `PB-L`
- Trigger 向上突破
- 15m `Ctx = UP`

因此：DVCA 不定义为反转。

## 三、多周期一致性

### 30m

- 最近一次有效状态已经转弱。
- 价格跌破 EMA20，并开始靠近 EMA50。
- MACD 死叉并向零轴下方扩展。
- RSI 接近弱势区域。
- 作用：决定今天不主动找多。

### 5m

- TC-S 连续出现。
- EMA 空头排列。
- 反弹无法站稳 EMA20。
- 每次反弹都形成更低高点。

这说明：空头节奏保持完整，没有出现趋势反转结构。

### 1m

- MACD 红柱开始缩短。
- 有小反弹。
- 但价格仍被 EMA20 压制。

这是 `Momentum Recovery`，不是 `Trend Reversal`。

## 四、交易计划（Trading Plan）

### 可以

等待：

```text
5m
反抽
↓
EMA20
↓
重新出现TC-S
```

这是目前最符合 DVCA 的顺势空机会。

### 不建议

不要：

```text
因为1m止跌
↓
立即做多
```

原因：15m 与 5m 都没有支持多头。

## 五、Scenario（未来三种剧本）

### 剧本 A（概率最高：约 60%）

```text
反抽EMA20
↓
再次TC-S
↓
继续测试新低
```

**策略：**等待反抽，不追空，等确认后再考虑顺势空。

### 剧本 B（约 30%）

```text
横盘整理
↓
形成震荡区
↓
等待15m选择方向
```

**策略：**观望，不开新仓。

### 剧本 C（约 10%）

```text
快速收复EMA20
↓
15m出现L-ZONE
↓
LONG
↓
PB-L
```

**策略：**只有出现完整反转链，才重新考虑多单。

## 六、风险评估

| 风险 | 评级 |
| --- | --- |
| 追空风险 | ★★★☆☆（已有一段跌幅，盈亏比下降） |
| 抄底风险 | ★★★★★（高周期未确认反转） |
| 顺势交易质量 | ★★★★☆ |
| 逆势交易质量 | ★☆☆☆☆ |

## 七、执行计划（Execution）

### 如果空仓

继续等待。不追空，也不抄底。

等待：

- 5m 反抽。
- EMA20 附近再次出现 TC-S / PB-S。

### 如果已经有空单

继续持有。

关注：

- 是否出现 EXH-L。
- 是否出现 1m、5m 同时的强反转结构。

若没有，则保持顺势思路。

### 如果已经有多单

降低风险。因为当前多周期没有给出继续持有多单的优势。

## 八、是否值得录入数据库？

### 图1（30m + 1D）

已录入：`CASE-0010`

```text
Pattern：TransitionToTrendDown
Main Signal：Context Shift
Rating：Good Case
```

价值：研究 30m 如何从震荡或转弱状态过渡为空头背景。

截图路径：

```text
screenshots/BTCUSDT/2026-07-08/2026-07-08_BTCUSDT_1D_30m_ContextShift_Good_unknown.png
```

### 图2（5m + 1m）

已录入：`CASE-0011`

```text
Pattern：TrendContinuation
Main Signal：TC-S
Rating：Good Case
```

价值：研究 `1m 动能修复 ≠ 趋势反转`。

截图路径：

```text
screenshots/BTCUSDT/2026-07-08/2026-07-08_BTCUSDT_5m_1m_TC-S_MomentumRecovery_Good_unknown.png
```

## 九、今天给 DVCA 指标的反馈

这两张图提出一个值得继续研究的问题：

**现在 DVCA 能较好识别空头延续，但对于什么时候空头真正结束的定义还不够清晰。**

当前 DVCA 比较擅长回答：

- 什么时候不要抄底。
- 什么时候继续顺势。

但对于下面这个问题，还需要更明确的规则：

```text
什么时候可以结束空头思维，开始准备 LONG？
```

后续 DVCA 2.0 可以研究 `Reversal Readiness` 模块，而不是只依赖单个 `L-ZONE` 或 `LONG` 信号。

可以纳入的观察项：

- 15m 是否重新站回 EMA20 / EMA50。
- 是否出现高质量 L-ZONE，例如 HMR 高分。
- MACD 是否完成底背离并重新金叉。
- 是否出现 Trigger 突破并收盘确认。

目标不是提前抄底，而是清楚知道距离满足做多条件还差哪几项。
