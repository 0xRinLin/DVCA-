# DVCA v1.5.1 线段形态说明

本文件基于 `indicator/dvca_v1_5_1.pine` 的真实代码逻辑编写，用于截图复盘和案例归档。

使用原则：

- 背离线不是进场线，只说明两个 Pivot 点之间的动能变化。
- 结构触发线才是 Zone 后的突破 / 破位观察线。
- EMA20 / EMA50 用来判断趋势背景，不是单独买卖信号。
- Keltner 用来辅助判断极值、支撑压力和可选盈亏比过滤。
- TC-L / TC-S 是趋势延续线段，不属于背离反转线段。
- PB-L / PB-S 必须发生在 LONG / SHORT 之后。
- EXH-L / EXH-S 是衰竭提醒，不是正式反向线段。
- LATE-L / LATE-S 是 Pivot 延迟确认后的补充，不应解释为追单线段。
- 当前 Pine 代码没有针对 BTC、ETH、SOL 等具体币种写独立逻辑；本文中 BTC / SOL 相关章节只作为按代码信号组合进行案例归档的线段类型，不代表源码内置币种规则。

## 多头背离线

### 对应代码逻辑

多头背离线来自 `newPL`，也就是 `ta.pivotlow(low, pL, pR)` 确认新的 Pivot Low 后的比较逻辑。代码把当前低点 `currPrice = pl` 与历史低点数组中的 `p1Price` 比较，要求两个低点间隔满足 `effMinBars <= barsBetween <= effMaxBars`，并且当前价格满足 `currPrice <= p1Price + atr[pR] * priceToleranceATR`。

背离由三项组成：`currHist > p1Hist` 记为 H，`currMacd > p1Macd` 记为 M，`currRSI > p1RSI` 记为 R。`divCount` 必须达到 `minDivCount`。当 Zone 通过评分、VPA、关键位和趋势过滤后，如果 `showDivLine` 开启，代码会用绿色线连接 `bestP1Index, bestP1Price` 和 `currIndex, currPrice`。

### 图上表现

图上表现为两个低点之间的绿色斜线，通常出现在 L-ZONE 附近。第二个低点可能接近前低，也可能略低于前低。

### 市场含义

它表示价格再次测试低点时，MACD Histogram、MACD Line 或 RSI 不再同步走弱，说明下跌动能出现减弱迹象。

### 常见有效形态

有效形态通常是第二个低点靠近 Donchian 低点、Keltner 下轨或前低区域，同时出现 H / M / R 中至少两项背离，并且配合强 VPA、假跌破收回或结构极值。

### 常见失败形态

失败形态通常是背离线出现后价格继续跌破 `bullLow - atr * 0.05`，或者 L-ZONE 成立后始终无法突破 `bullTrigger`。也可能出现突破，但只触发 E-L，未通过 LONG 的严格质量过滤。

### 需要配合的信号

需要配合 L-ZONE、C-L、LONG、PB-L、EXH-L、结构触发线、EMA20 / EMA50、Keltner 下轨、Donchian 低点、成交量、MACD 和 RSI。

### 截图复盘要点

截图需要保留两个 Pivot Low、绿色背离线、L-ZONE 标签、背离代码、结构触发线和后续是否出现 LONG。记录第二个低点是否靠近支撑，以及背离后 10 / 20 / 50 根 K 线是否止跌。

### 是否适合交易执行

不适合单独交易执行。多头背离线只是 Zone 的基础证据，正式执行需要等待 LONG 或后续 PB-L。

## 空头背离线

### 对应代码逻辑

空头背离线来自 `newPH`，也就是 `ta.pivothigh(high, pL, pR)` 确认新的 Pivot High 后的比较逻辑。代码把当前高点 `currPrice = ph` 与历史高点数组中的 `p1Price` 比较，要求两个高点间隔满足 `effMinBars <= barsBetween <= effMaxBars`，并且当前价格满足 `currPrice >= p1Price - atr[pR] * priceToleranceATR`。

背离由三项组成：`currHist < p1Hist` 记为 H，`currMacd < p1Macd` 记为 M，`currRSI < p1RSI` 记为 R。`divCount` 必须达到 `minDivCount`。当 Zone 通过评分、VPA、关键位和趋势过滤后，如果 `showDivLine` 开启，代码会用红色线连接 `bestP1Index, bestP1Price` 和 `currIndex, currPrice`。

### 图上表现

图上表现为两个高点之间的红色斜线，通常出现在 S-ZONE 附近。第二个高点可能接近前高，也可能略高于前高。

### 市场含义

它表示价格再次测试高点时，MACD Histogram、MACD Line 或 RSI 不再同步走强，说明上涨动能出现减弱迹象。

### 常见有效形态

有效形态通常是第二个高点靠近 Donchian 高点、Keltner 上轨或前高区域，同时出现 H / M / R 中至少两项背离，并且配合强 VPA、假突破收回或结构极值。

### 常见失败形态

失败形态通常是背离线出现后价格继续突破 `bearHigh + atr * 0.05`，或者 S-ZONE 成立后始终无法跌破 `bearTrigger`。也可能出现破位，但只触发 E-S，未通过 SHORT 的严格质量过滤。

### 需要配合的信号

需要配合 S-ZONE、C-S、SHORT、PB-S、EXH-S、结构触发线、EMA20 / EMA50、Keltner 上轨、Donchian 高点、成交量、MACD 和 RSI。

### 截图复盘要点

截图需要保留两个 Pivot High、红色背离线、S-ZONE 标签、背离代码、结构触发线和后续是否出现 SHORT。记录第二个高点是否靠近压力，以及背离后 10 / 20 / 50 根 K 线是否滞涨。

### 是否适合交易执行

不适合单独交易执行。空头背离线只是 Zone 的基础证据，正式执行需要等待 SHORT 或后续 PB-S。

## 多头结构触发线

### 对应代码逻辑

多头结构触发线是 `bullTrigger`。L-ZONE 成立后，代码先计算保守触发线 `triggerConservative = f_highestBetween(pR, pR + bestBars, effMaxBars + pR)`，再计算快速触发线 `triggerFast = ltfRecentHigh`。LTF 模式下，`ltfBreakMode` 决定使用 Conservative、Fast 或 Hybrid。Hybrid 模式会在可用情况下选择更低的多头触发价。

正式 LONG 要求 `close > bullTrigger + atr * breakoutBufferATR`。如果 `showStructureLine` 开启，代码会从 Zone 当前 Pivot 位置向右画出绿色水平线。

### 图上表现

图上表现为 L-ZONE 之后的一条绿色水平线，通常位于当前价格上方或附近，代表多头需要突破的结构位置。

### 市场含义

它表示多头背离观察区之后，市场需要突破上方结构高点，才算从观察进入执行阶段。

### 常见有效形态

有效形态是 L-ZONE 后价格不再创新低，围绕触发线下方蓄势，随后收盘突破触发线并同步满足量能、EMA20、MACD Histogram、RSI 和风险过滤。

### 常见失败形态

失败形态是价格未突破触发线并超过 `maxSetupBars`，或先跌破 `bullLow - atr * 0.05` 导致多头结构失效。另一类失败是突破触发线但严格条件不够，只出现 E-L。

### 需要配合的信号

需要配合 L-ZONE、C-L、E-L、LATE-L、LONG、PB-L、成交量、EMA20、MACD Histogram 和 RSI。

### 截图复盘要点

截图要标出 L-ZONE、绿色背离线、`bullTrigger`、突破 K 线和突破后的走势。重点记录突破发生时距离 Zone 有多少根 K 线，以及是否出现 LATE-L 或 E-L。

### 是否适合交易执行

触发线本身不是交易信号。只有收盘突破并通过严格条件生成 LONG，才属于代码定义的正式多头执行信号。

## 空头结构触发线

### 对应代码逻辑

空头结构触发线是 `bearTrigger`。S-ZONE 成立后，代码先计算保守触发线 `triggerConservative = f_lowestBetween(pR, pR + bestBars, effMaxBars + pR)`，再计算快速触发线 `triggerFast = ltfRecentLow`。LTF 模式下，`ltfBreakMode` 决定使用 Conservative、Fast 或 Hybrid。Hybrid 模式会在可用情况下选择更高的空头触发价。

正式 SHORT 要求 `close < bearTrigger - atr * breakoutBufferATR`。如果 `showStructureLine` 开启，代码会从 Zone 当前 Pivot 位置向右画出红色水平线。

### 图上表现

图上表现为 S-ZONE 之后的一条红色水平线，通常位于当前价格下方或附近，代表空头需要跌破的结构位置。

### 市场含义

它表示空头背离观察区之后，市场需要跌破下方结构低点，才算从观察进入执行阶段。

### 常见有效形态

有效形态是 S-ZONE 后价格不再创新高，围绕触发线上方转弱，随后收盘跌破触发线并同步满足量能、EMA20、MACD Histogram、RSI 和风险过滤。

### 常见失败形态

失败形态是价格未跌破触发线并超过 `maxSetupBars`，或先突破 `bearHigh + atr * 0.05` 导致空头结构失效。另一类失败是跌破触发线但严格条件不够，只出现 E-S。

### 需要配合的信号

需要配合 S-ZONE、C-S、E-S、LATE-S、SHORT、PB-S、成交量、EMA20、MACD Histogram 和 RSI。

### 截图复盘要点

截图要标出 S-ZONE、红色背离线、`bearTrigger`、跌破 K 线和跌破后的走势。重点记录跌破发生时距离 Zone 有多少根 K 线，以及是否出现 LATE-S 或 E-S。

### 是否适合交易执行

触发线本身不是交易信号。只有收盘跌破并通过严格条件生成 SHORT，才属于代码定义的正式空头执行信号。

## EMA20 / EMA50 趋势线段

### 对应代码逻辑

EMA20 对应 `emaFast = ta.ema(close, emaFastLen)`，EMA50 对应 `emaSlow = ta.ema(close, emaSlowLen)`。趋势背景由 `ctxUp` 和 `ctxDown` 判断。`ctxUp` 要求 EMA20 在 EMA50 上方，收盘在 EMA50 上方，并且 EMA50 相比 `trendSlopeLen` 前上升。`ctxDown` 要求 EMA20 在 EMA50 下方，收盘在 EMA50 下方，并且 EMA50 相比 `trendSlopeLen` 前下降。

严格进场中，LONG 默认要求 `close > emaFast`，SHORT 默认要求 `close < emaFast`。TC-L / TC-S、PB-L / PB-S 也会使用 EMA20 作为回踩或反抽参考。

### 图上表现

图上表现为 EMA20 快线和 EMA50 慢线。EMA20 在 EMA50 上方且 EMA50 上行时，背景偏多；EMA20 在 EMA50 下方且 EMA50 下行时，背景偏空。

### 市场含义

EMA20 / EMA50 用来判断当前信号处在趋势背景还是反转背景。它不是单独买卖信号，而是信号质量过滤和 TC 趋势延续的基础。

### 常见有效形态

有效的多头趋势线段通常是 EMA20 在 EMA50 上方，价格回踩 EMA20 后重新站上并突破短高。有效的空头趋势线段通常是 EMA20 在 EMA50 下方，价格反抽 EMA20 后重新跌下并跌破短低。

### 常见失败形态

失败形态通常是 EMA20 / EMA50 纠缠走平，价格反复穿越 EMA20，导致 TC 或 PB 信号容易被震荡噪音干扰。反趋势 Zone 在强趋势 EMA 背景下也容易过早。

### 需要配合的信号

需要配合 LONG、SHORT、PB-L、PB-S、TC-L、TC-S、EXH-L、EXH-S，以及 `ctxUp / ctxDown / strongUp / strongDown` 背景。

### 截图复盘要点

截图要打开 EMA 显示，记录信号出现时价格在 EMA20 和 EMA50 的哪一侧，EMA50 是否有斜率，回踩或反抽是否围绕 EMA20 展开。

### 是否适合交易执行

不适合单独交易执行。EMA20 / EMA50 是背景与过滤工具，执行仍应看 LONG、SHORT、PB 或 TC。

## Keltner 上下轨线段

### 对应代码逻辑

Keltner 由 `kcBasis = ta.ema(close, kcLen)`、`kcRange = ta.ema(ta.tr(true), kcLen)`、`kcUpper = kcBasis + kcRange * kcMult`、`kcLower = kcBasis - kcRange * kcMult` 计算。

多头 Zone 中，`nearKcSupport` 判断当前 Pivot Low 是否靠近 `kcLower[pR]`。空头 Zone 中，`nearKcResistance` 判断当前 Pivot High 是否靠近 `kcUpper[pR]`。EXH-L 用 `currPrice <= kcLower[pR] + atr[pR] * 0.60` 辅助判断下跌极值，EXH-S 用 `currPrice >= kcUpper[pR] - atr[pR] * 0.60` 辅助判断上涨极值。

### 图上表现

图上表现为 Keltner 上轨和下轨。价格靠近下轨时可能参与多头支撑或 EXH-L 极值判断；价格靠近上轨时可能参与空头压力或 EXH-S 极值判断。

### 市场含义

Keltner 在代码中不是独立信号，而是判断 Zone 是否靠近关键位、EXH 是否位于极值区域、LONG / SHORT 可选 RR 是否有空间的辅助线段。

### 常见有效形态

有效形态通常是 L-ZONE 或 EXH-L 发生在 Keltner 下轨附近，或 S-ZONE / EXH-S 发生在 Keltner 上轨附近，并且同时有背离、VPA 或假突破 / 假跌破。

### 常见失败形态

失败形态通常是强趋势中价格长时间贴着 Keltner 上轨或下轨运行，过早把通道边缘当作反转依据。震荡很窄时，Keltner 上下轨也可能离当前价格太近，突破后空间不足。

### 需要配合的信号

需要配合 L-ZONE、S-ZONE、EXH-L、EXH-S、LONG、SHORT、Donchian 高低点、VPA 和背离线。

### 截图复盘要点

截图要打开 Keltner 显示，记录 Zone / EXH 与上轨或下轨的距离，观察后续是否出现结构触发线突破或跌破。

### 是否适合交易执行

不适合单独交易执行。Keltner 是极值和支撑压力辅助，不是正式交易信号。

## Donchian 高低点结构

### 对应代码逻辑

Donchian 高低点由 `donHigh = ta.highest(high, donLen)` 和 `donLow = ta.lowest(low, donLen)` 计算。Pivot 处的前置 Donchian 参考为 `priorDonHighAtP2 = ta.highest(high, donLen)[pR + 1]` 和 `priorDonLowAtP2 = ta.lowest(low, donLen)[pR + 1]`。

多头支撑使用 `nearDonSupport = abs(currPrice - priorDonLowAtP2) <= atr[pR] * srNearATR`。空头压力使用 `nearDonResistance = abs(currPrice - priorDonHighAtP2) <= atr[pR] * srNearATR`。可选 RR 过滤中，LONG 会把 `donHigh[1]` 当作候选上方阻力，SHORT 会把 `donLow[1]` 当作候选下方支撑。

### 图上表现

图上表现为近期区间的高点和低点结构。代码没有单独画 Donchian 线，但复盘时可以用价格图上的最近高低点区域观察。

### 市场含义

Donchian 结构用于判断 Zone 是否靠近近期关键支撑或压力，也用于判断突破后是否有足够空间。

### 常见有效形态

有效形态通常是 L-ZONE 发生在近期 Donchian 低点附近，S-ZONE 发生在近期 Donchian 高点附近，并且后续价格突破或跌破对应结构触发线。

### 常见失败形态

失败形态通常是 Donchian 高低点只是短期噪音，大周期方向仍很强，Zone 出现后价格继续沿原方向运行。另一个失败形态是突破后很快遇到 Donchian 反向结构，空间不足。

### 需要配合的信号

需要配合 L-ZONE、S-ZONE、LONG、SHORT、Keltner、EMA20 / EMA50、VPA 和 RR 过滤。

### 截图复盘要点

截图需要包含足够多 K 线，最好能看到 `donLen` 对应的近期高低点区域。记录信号发生时是否靠近 Donchian 高点或低点。

### 是否适合交易执行

不适合单独交易执行。Donchian 是结构参考，正式交易仍需要 LONG、SHORT、PB 或 TC。

## L-ZONE 到 LONG 的线段

### 对应代码逻辑

这条线段从 `bullZoneSignal` 开始，到 `longSignal` 结束。L-ZONE 成立后，代码设置 `bullActive = true`，保存 `bullLow`、`bullTrigger`、`bullScore` 和 `bullInfo`。之后只有在 LTF 模式下，结构未过期、未失效，并且收盘突破 `bullTrigger + atr * breakoutBufferATR` 时，才进入 LONG 检查。

LONG 需要 `strictOk` 成立，包括量能过滤、站上 EMA20、MACD Histogram 和 RSI 同向上升、强空头背景下的上下文过滤、风险距离过滤，以及可选 RR 过滤。

### 图上表现

图上表现为 L-ZONE 出现在低点附近，随后价格向上接近绿色结构触发线，最终在某根 K 线收盘突破并显示 LONG。

### 市场含义

它表示市场从多头背离观察区进入正式多头突破。代码不把 L-ZONE 当作进场，而是等结构突破确认。

### 常见有效形态

有效形态是 L-ZONE 后价格不再创新低，突破触发线时有量能，收盘站上 EMA20，MACD Histogram 和 RSI 同步回升，风险距离不过大。

### 常见失败形态

失败形态是 L-ZONE 后价格继续破低，或突破等待超过 `maxSetupBars`。另一类是突破触发线时质量不足，只出现 E-L，没有出现 LONG。

### 需要配合的信号

需要配合 C-L、E-L、LATE-L、LONG、PB-L、背离线、结构触发线、EMA20、成交量、MACD Histogram 和 RSI。

### 截图复盘要点

截图需要从 L-ZONE 前的第一个 Pivot Low 开始，保留到 LONG 后至少 30 根 K 线。记录 Zone 分数、背离代码、触发线位置、LONG 当根量能和后续是否出现 PB-L。

### 是否适合交易执行

只有 LONG 这一端适合按代码定义作为正式执行信号。L-ZONE 到 LONG 的过程适合观察和等待。

## S-ZONE 到 SHORT 的线段

### 对应代码逻辑

这条线段从 `bearZoneSignal` 开始，到 `shortSignal` 结束。S-ZONE 成立后，代码设置 `bearActive = true`，保存 `bearHigh`、`bearTrigger`、`bearScore` 和 `bearInfo`。之后只有在 LTF 模式下，结构未过期、未失效，并且收盘跌破 `bearTrigger - atr * breakoutBufferATR` 时，才进入 SHORT 检查。

SHORT 需要 `strictOk` 成立，包括量能过滤、跌破 EMA20、MACD Histogram 和 RSI 同向下降、强多头背景下的上下文过滤、风险距离过滤，以及可选 RR 过滤。

### 图上表现

图上表现为 S-ZONE 出现在高点附近，随后价格向下接近红色结构触发线，最终在某根 K 线收盘跌破并显示 SHORT。

### 市场含义

它表示市场从空头背离观察区进入正式空头破位。代码不把 S-ZONE 当作进场，而是等结构跌破确认。

### 常见有效形态

有效形态是 S-ZONE 后价格不再创新高，跌破触发线时有量能，收盘跌破 EMA20，MACD Histogram 和 RSI 同步走弱，风险距离不过大。

### 常见失败形态

失败形态是 S-ZONE 后价格继续破高，或跌破等待超过 `maxSetupBars`。另一类是跌破触发线时质量不足，只出现 E-S，没有出现 SHORT。

### 需要配合的信号

需要配合 C-S、E-S、LATE-S、SHORT、PB-S、背离线、结构触发线、EMA20、成交量、MACD Histogram 和 RSI。

### 截图复盘要点

截图需要从 S-ZONE 前的第一个 Pivot High 开始，保留到 SHORT 后至少 30 根 K 线。记录 Zone 分数、背离代码、触发线位置、SHORT 当根量能和后续是否出现 PB-S。

### 是否适合交易执行

只有 SHORT 这一端适合按代码定义作为正式执行信号。S-ZONE 到 SHORT 的过程适合观察和等待。

## LONG 到 PB-L 的线段

### 对应代码逻辑

LONG 出现后，代码设置 `waitBullPB = true`，保存 `bullRetestLevel = bullTrigger`、`bullBreakIndex`、`bullBreakLow` 和 `bullPostBreakHigh`。PB-L 只能在 LONG 之后检查。

PB-L 要求突破后至少等待 `minRetestBars`，不能超过 `maxRetestBars`。回踩深度需要满足 `bullPostBreakHigh - low >= atr * pbMinPullbackATR`，除非该参数为 0。有效回踩可以触及 `bullRetestLevel + atr * retestToleranceATR` 后收在触发线上方，也可以在允许 EMA 回踩时触及 EMA20 容差范围后收在 EMA20 上方。最后要求阳线，并且在启用动能确认时 `macdHist >= macdHist[1]`。

### 图上表现

图上表现为 LONG 后价格先向上运行，再回踩绿色触发线或 EMA20，然后重新收强并显示 PB-L。

### 市场含义

它表示多头突破后的二次确认。代码把它作为突破后回踩承接，而不是原始反转信号。

### 常见有效形态

有效形态是 LONG 后先拉开一定空间，再回踩触发线或 EMA20，回踩 K 线不跌破失败线，随后以阳线和动能稳定收回。

### 常见失败形态

失败形态是 LONG 后没有足够回踩，导致没有 PB-L；或回踩过深，收盘跌破 `bullRetestLevel - atr * retestFailATR` 或跌破 `bullBreakLow`，导致 PB-L 等待失败。

### 需要配合的信号

需要配合 LONG、PB-L、EMA20、结构触发线、MACD Histogram、成交量和后续趋势延续信号 TC-L。

### 截图复盘要点

截图要包含 LONG、突破后最高点、回踩最低点、PB-L 标签、EMA20 和触发线。记录从 LONG 到 PB-L 间隔了几根 K 线，以及 PB-L 后 10 / 20 / 50 根 K 线表现。

### 是否适合交易执行

适合按突破后回踩确认进行执行观察。它必须建立在已经出现 LONG 的前提下。

## SHORT 到 PB-S 的线段

### 对应代码逻辑

SHORT 出现后，代码设置 `waitBearPB = true`，保存 `bearRetestLevel = bearTrigger`、`bearBreakIndex`、`bearBreakHigh` 和 `bearPostBreakLow`。PB-S 只能在 SHORT 之后检查。

PB-S 要求跌破后至少等待 `minRetestBars`，不能超过 `maxRetestBars`。反抽深度需要满足 `high - bearPostBreakLow >= atr * pbMinPullbackATR`，除非该参数为 0。有效反抽可以触及 `bearRetestLevel - atr * retestToleranceATR` 后收在触发线下方，也可以在允许 EMA 回踩时触及 EMA20 容差范围后收在 EMA20 下方。最后要求阴线，并且在启用动能确认时 `macdHist <= macdHist[1]`。

### 图上表现

图上表现为 SHORT 后价格先向下运行，再反抽红色触发线或 EMA20，然后重新收弱并显示 PB-S。

### 市场含义

它表示空头跌破后的二次确认。代码把它作为跌破后反抽压制，而不是原始反转信号。

### 常见有效形态

有效形态是 SHORT 后先跌出一定空间，再反抽触发线或 EMA20，反抽 K 线不突破失败线，随后以阴线和动能稳定转弱。

### 常见失败形态

失败形态是 SHORT 后没有足够反抽，导致没有 PB-S；或反抽过深，收盘突破 `bearRetestLevel + atr * retestFailATR` 或突破 `bearBreakHigh`，导致 PB-S 等待失败。

### 需要配合的信号

需要配合 SHORT、PB-S、EMA20、结构触发线、MACD Histogram、成交量和后续趋势延续信号 TC-S。

### 截图复盘要点

截图要包含 SHORT、跌破后最低点、反抽最高点、PB-S 标签、EMA20 和触发线。记录从 SHORT 到 PB-S 间隔了几根 K 线，以及 PB-S 后 10 / 20 / 50 根 K 线表现。

### 是否适合交易执行

适合按跌破后反抽确认进行执行观察。它必须建立在已经出现 SHORT 的前提下。

## TC-L 趋势延续线段

### 对应代码逻辑

TC-L 来自 `tcLongSignal`，与 L-ZONE 背离逻辑无关。它要求 `useTrendContinuation` 开启、当前为 LTF 模式、同方向冷却结束，并且同一根没有触发 LONG。

核心条件包括：`tcCtxLong = ctxUp and emaFast > emaSlow and close > emaSlow`；最近 `tcPullbackLookback` 内最低价触及 `emaFast + atr * tcEmaToleranceATR` 且当前收盘在 EMA20 上方；当前收盘突破过去 `tcBreakLookback` 根前高加 `atr * breakoutBufferATR`；MACD Histogram 上升，RSI 大于 50 且上升；成交量大于等于 `volMa * tcVolMult`；如果启用 `tcRequireHTFBias`，不能有相反的 `ctxDown`。

### 图上表现

图上表现为 EMA20 在 EMA50 上方，价格回踩 EMA20 附近后重新向上，突破短期高点并显示 TC-L。

### 市场含义

它表示已有上升趋势中的回踩后再突破，是趋势延续，不是背离反转。

### 常见有效形态

有效形态是 EMA50 上行、EMA20 在 EMA50 上方，价格回踩 EMA20 但不破坏趋势，随后放量突破短高，同时 RSI 在 50 上方继续走强。

### 常见失败形态

失败形态是趋势已经进入末端，回踩只是横盘噪音，或者突破短高后马上跌回。上方 Donchian 或 Keltner 压力太近时，后续空间也可能不足。

### 需要配合的信号

需要配合 EMA20 / EMA50、成交量、MACD Histogram、RSI、Donchian 高点、Keltner 上轨和后续是否出现 PB-L。

### 截图复盘要点

截图要保留 TC-L 前的回踩段、EMA20 / EMA50、短高突破位置、成交量和后续走势。重点区分 TC-L 与 LONG：TC-L 不需要前置 L-ZONE。

### 是否适合交易执行

适合趋势延续类执行观察。它不是反转信号，也不应按背离反转逻辑复盘。

## TC-S 趋势延续线段

### 对应代码逻辑

TC-S 来自 `tcShortSignal`，与 S-ZONE 背离逻辑无关。它要求 `useTrendContinuation` 开启、当前为 LTF 模式、同方向冷却结束，并且同一根没有触发 SHORT。

核心条件包括：`tcCtxShort = ctxDown and emaFast < emaSlow and close < emaSlow`；最近 `tcPullbackLookback` 内最高价触及 `emaFast - atr * tcEmaToleranceATR` 且当前收盘在 EMA20 下方；当前收盘跌破过去 `tcBreakLookback` 根前低减 `atr * breakoutBufferATR`；MACD Histogram 下降，RSI 小于 50 且下降；成交量大于等于 `volMa * tcVolMult`；如果启用 `tcRequireHTFBias`，不能有相反的 `ctxUp`。

### 图上表现

图上表现为 EMA20 在 EMA50 下方，价格反抽 EMA20 附近后重新向下，跌破短期低点并显示 TC-S。

### 市场含义

它表示已有下降趋势中的反抽后再破位，是趋势延续，不是背离反转。

### 常见有效形态

有效形态是 EMA50 下行、EMA20 在 EMA50 下方，价格反抽 EMA20 但不破坏趋势，随后放量跌破短低，同时 RSI 在 50 下方继续走弱。

### 常见失败形态

失败形态是趋势已经进入末端，反抽只是横盘噪音，或者跌破短低后马上收回。下方 Donchian 或 Keltner 支撑太近时，后续空间也可能不足。

### 需要配合的信号

需要配合 EMA20 / EMA50、成交量、MACD Histogram、RSI、Donchian 低点、Keltner 下轨和后续是否出现 PB-S。

### 截图复盘要点

截图要保留 TC-S 前的反抽段、EMA20 / EMA50、短低跌破位置、成交量和后续走势。重点区分 TC-S 与 SHORT：TC-S 不需要前置 S-ZONE。

### 是否适合交易执行

适合趋势延续类执行观察。它不是反转信号，也不应按背离反转逻辑复盘。

## EXH-L 衰竭线段

### 对应代码逻辑

EXH-L 来自 `bullExhSignal`。它只在 `useExhaustion` 开启、当前为 LTF 模式、确认新 Pivot Low 时检查。基础条件和多头背离使用同一组 Pivot Low 比较，但 EXH 有单独评分。

代码要求处于下跌背景：Pivot 处 EMA20 低于 EMA50，或收盘低于 EMA50。两个低点间隔和价格容差仍需有效，H / M / R 背离数量达到 `minDivCount`。`exhStrong` 来自三重背离、假跌破、靠近支撑，或缩量二次测试加努力无结果。`exhExtreme` 默认要求靠近支撑、接近 Keltner 下轨、假跌破或三重背离。评分达到 `exhMinScore`，干净下跌背景下还要达到 `trendExhMinScore`。

### 图上表现

图上表现为下跌背景中的低点区域出现 EXH-L 标签，通常靠近支撑、Keltner 下轨或新低区域。

### 市场含义

它表示下跌过程中的衰竭提醒，说明继续下跌时动能或量价行为出现减弱，但还没有确认反转。

### 常见有效形态

有效形态是下跌趋势中价格打出新低或接近下轨，同时出现多项背离、假跌破、缩量二次测试或努力无结果，后续再形成 L-ZONE、LONG 或至少止跌横盘。

### 常见失败形态

失败形态是强下跌趋势中连续出现 EXH-L，但价格仍沿 EMA 下方继续下行。另一个失败形态是只有 EXH-L，没有后续结构触发线突破。

### 需要配合的信号

需要配合 L-ZONE、C-L、LONG、PB-L、多头背离线、Keltner 下轨、Donchian 低点、EMA20 / EMA50 和 VPA。

### 截图复盘要点

截图要保留 EXH-L 前的下跌段、Pivot Low、Keltner 下轨、背离指标和后续是否出现 L-ZONE 或 LONG。记录 EXH-L 后 10 / 20 / 50 根 K 线是否止跌。

### 是否适合交易执行

不适合作为正式反向执行。EXH-L 是衰竭提醒，不是 LONG。

## EXH-S 衰竭线段

### 对应代码逻辑

EXH-S 来自 `bearExhSignal`。它只在 `useExhaustion` 开启、当前为 LTF 模式、确认新 Pivot High 时检查。基础条件和空头背离使用同一组 Pivot High 比较，但 EXH 有单独评分。

代码要求处于上涨背景：Pivot 处 EMA20 高于 EMA50，或收盘高于 EMA50。两个高点间隔和价格容差仍需有效，H / M / R 背离数量达到 `minDivCount`。`exhStrong` 来自三重背离、假突破、靠近压力，或缩量二次测试加努力无结果。`exhExtreme` 默认要求靠近压力、接近 Keltner 上轨、假突破或三重背离。评分达到 `exhMinScore`，干净上涨背景下还要达到 `trendExhMinScore`。

### 图上表现

图上表现为上涨背景中的高点区域出现 EXH-S 标签，通常靠近压力、Keltner 上轨或新高区域。

### 市场含义

它表示上涨过程中的衰竭提醒，说明继续上涨时动能或量价行为出现减弱，但还没有确认反转。

### 常见有效形态

有效形态是上涨趋势中价格打出新高或接近上轨，同时出现多项背离、假突破、缩量二次测试或努力无结果，后续再形成 S-ZONE、SHORT 或至少滞涨横盘。

### 常见失败形态

失败形态是强上涨趋势中连续出现 EXH-S，但价格仍沿 EMA 上方继续上行。另一个失败形态是只有 EXH-S，没有后续结构触发线跌破。

### 需要配合的信号

需要配合 S-ZONE、C-S、SHORT、PB-S、空头背离线、Keltner 上轨、Donchian 高点、EMA20 / EMA50 和 VPA。

### 截图复盘要点

截图要保留 EXH-S 前的上涨段、Pivot High、Keltner 上轨、背离指标和后续是否出现 S-ZONE 或 SHORT。记录 EXH-S 后 10 / 20 / 50 根 K 线是否滞涨。

### 是否适合交易执行

不适合作为正式反向执行。EXH-S 是衰竭提醒，不是 SHORT。

## 假突破 / 假跌破线段

### 对应代码逻辑

假突破 / 假跌破主要由 `vpaVF` 表示，属于强 VPA 的一类。

多头假跌破：当前 Pivot Low 低于前一个低点，并且 Pivot 当根收盘回到前低上方，或在 `fakeBreakWindow` 窗口内出现收盘重新站回前低上方。代码为 `useVPA and currPrice < p1Price and (close[pR] > p1Price or f_anyCloseAboveAfter(pR, fakeBreakWindow, p1Price))`。

空头假突破：当前 Pivot High 高于前一个高点，并且 Pivot 当根收盘回到前高下方，或在 `fakeBreakWindow` 窗口内出现收盘重新跌回前高下方。代码为 `useVPA and currPrice > p1Price and (close[pR] < p1Price or f_anyCloseBelowAfter(pR, fakeBreakWindow, p1Price))`。

### 图上表现

多头图上表现为刺破前低后收回。空头图上表现为刺破前高后收回。它通常出现在背离线第二个 Pivot 点附近。

### 市场含义

代码含义是价格短暂突破前低或前高，但没有被收盘确认接受，因此作为强 VPA 证据参与 Zone 和 EXH 判断。

### 常见有效形态

有效形态是刺破前低或前高后快速收回，同时出现 H / M / R 背离，并且靠近 Donchian 或 Keltner 关键位。

### 常见失败形态

失败形态是假突破收回后又再次真实突破，或假跌破收回后没有突破 `bullTrigger`，假突破收回后没有跌破 `bearTrigger`。

### 需要配合的信号

需要配合 L-ZONE、S-ZONE、EXH-L、EXH-S、结构触发线、背离线、Donchian 高低点、Keltner 和成交量。

### 截图复盘要点

截图要标出前一个 Pivot 价位、刺破位置、收回 K 线、背离指标、Zone 标签和后续结构触发线。记录收回发生在 Pivot 当根还是 `fakeBreakWindow` 内。

### 是否适合交易执行

不适合单独交易执行。它是 Zone / EXH 的增强证据，不是正式进场信号。

## BTC 常见 TC 多、LONG 少的线段类型

### 对应代码逻辑

当前源码没有任何 BTC 专属判断，也没有按 `syminfo.ticker` 做分支。因此本节不是代码内置规则，而是用于复盘 BTC 案例时的归档类型：当 BTC 图上 TC-L / TC-S 多，而 LONG / SHORT 少时，通常意味着代码更多满足趋势延续条件，而较少满足背离 Zone 到严格突破的完整链条。

TC 多的代码条件来自 `tcLongSignal / tcShortSignal`：EMA20 / EMA50 趋势背景明确，价格回踩或反抽 EMA20，随后突破短高或跌破短低，并且 MACD Histogram、RSI、成交量满足要求。LONG / SHORT 少的代码原因可能是没有形成符合 `minDivCount`、VPA、关键位、评分和冷却要求的 Zone，或 Zone 后没有通过严格突破过滤。

### 图上表现

图上通常表现为价格沿 EMA20 / EMA50 单边推进，回踩浅、结构连续，TC-L 或 TC-S 在趋势中段出现。相对而言，明显的双 Pivot 背离、L-ZONE / S-ZONE 和后续严格 LONG / SHORT 链条较少。

### 市场含义

按代码解释，这类图不是“没有机会”，而是机会更多来自趋势延续，而不是背离反转。它强调顺着 EMA 背景做回踩后突破，而不是等待 Zone 反转。

### 常见有效形态

有效形态是 EMA50 有清晰斜率，EMA20 与 EMA50 排列明确，价格多次靠近 EMA20 后继续突破短高或跌破短低，成交量和动能配合。

### 常见失败形态

失败形态是趋势后段仍连续出现 TC，但价格已经靠近 Keltner 边界或 Donchian 反向结构，突破短高 / 短低后空间不足。另一种失败是 EMA 走平时 TC 变成震荡噪音。

### 需要配合的信号

需要配合 TC-L、TC-S、EMA20 / EMA50、成交量、MACD Histogram、RSI、Donchian 高低点和 Keltner 上下轨。若出现 EXH-L / EXH-S，需要记录趋势是否可能衰竭。

### 截图复盘要点

BTC 案例截图要标注 TC 出现前的回踩或反抽，记录是否有 L-ZONE / S-ZONE 缺失，以及 LONG / SHORT 少的原因是没有 Zone，还是 Zone 后未通过严格突破条件。

### 是否适合交易执行

适合按 TC 趋势延续逻辑观察执行，不适合强行套用背离反转逻辑。是否交易仍以 TC-L / TC-S 的实际触发条件为准。

## SOL 常见 Zone 到 SHORT/LONG 到 PB 的线段类型

### 对应代码逻辑

当前源码没有任何 SOL 专属判断，也没有按 `syminfo.ticker` 做分支。因此本节不是代码内置规则，而是用于复盘 SOL 案例时的归档类型：当 SOL 图上经常出现 Zone 到 SHORT / LONG，再到 PB 的完整链条时，应按通用代码逻辑记录。

多头链条是 `bullZoneSignal -> longSignal -> bullPBSignal`。空头链条是 `bearZoneSignal -> shortSignal -> bearPBSignal`。Zone 需要 Pivot 背离、VPA、关键位和评分通过；LONG / SHORT 需要结构触发线突破或跌破并通过严格过滤；PB-L / PB-S 必须发生在 LONG / SHORT 之后，并满足回踩深度、触发线或 EMA20 回踩、K 线方向和动能确认。

### 图上表现

图上表现为先出现 L-ZONE 或 S-ZONE，随后价格突破绿色触发线出现 LONG，或跌破红色触发线出现 SHORT。突破后价格回踩触发线或 EMA20，再出现 PB-L 或 PB-S。

### 市场含义

按代码解释，这类线段是从反转观察到结构确认，再到回踩确认的完整流程。它比单独 Zone 更完整，也比单独 PB 更有前后文。

### 常见有效形态

有效形态是 Zone 发生在 Donchian 或 Keltner 关键位附近，背离和 VPA 明确，LONG / SHORT 当根突破质量足够，随后 PB 回踩不破失败线，并用阳线或阴线重新确认方向。

### 常见失败形态

失败形态是 Zone 成立后没有突破触发线，或者突破后很快回到触发线内。另一类失败是 LONG / SHORT 出现后 PB 回踩过深，触发 PB fail 条件。

### 需要配合的信号

需要配合 L-ZONE、S-ZONE、LONG、SHORT、PB-L、PB-S、结构触发线、背离线、EMA20、Keltner、Donchian、成交量、MACD Histogram 和 RSI。

### 截图复盘要点

SOL 案例截图要完整覆盖 Zone 前两个 Pivot、结构触发线、LONG / SHORT 当根、PB 回踩段和后续 10 / 20 / 50 根 K 线。记录这条链条是多头还是空头，PB 是触发线回踩还是 EMA20 浅回踩。

### 是否适合交易执行

适合按完整链条做案例复盘。真正执行点以 LONG / SHORT 或 PB-L / PB-S 的代码触发为准，不能把 Zone 本身当作进场。
