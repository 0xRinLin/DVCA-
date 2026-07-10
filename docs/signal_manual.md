# DVCA v1.5.1 信号说明书

本文件基于 `indicator/dvca_v1_5_1.pine` 的真实代码逻辑编写，用于截图复盘和案例归档。

说明原则：

- L-ZONE / S-ZONE 是背离观察区，不是进场信号。
- C-L / C-S 是 Zone 在 LTF 模式下成立后的确认提示，不等于正式进场。
- E-L / E-S 是突破发生但严格进场条件未全部满足时的提前观察信号。
- LATE-L / LATE-S 是 Pivot 确认延迟导致的补确认，不是追单信号。
- LONG / SHORT 是代码定义的严格突破进场信号。
- PB-L / PB-S 是 LONG / SHORT 之后的回踩确认。
- TC-L / TC-S 是趋势延续信号，不依赖背离 Zone，不是背离反转。
- EXH-L / EXH-S 是趋势中衰竭提醒，不是正式反向进场。

默认模式下，`Auto` 会把 30m 及以上视为 HTF Context，把 30m 以下视为 LTF Execution；15m 及以上但低于 30m 会进入更严格的 LTF-C 参数。实际周期判断以代码中的 `timeframe.in_seconds()`、`autoHTFSeconds` 和 `ltfConfirmSeconds` 为准。

## L-ZONE

### 中文含义

多头背离观察区。它表示价格在 Pivot Low 附近出现符合评分要求的潜在多头背离区域。

### 代码触发逻辑

`bullZoneSignal` 在已确认的新 Pivot Low 上触发。代码会把当前低点与历史低点 Pivot 进行比较，要求两个 Pivot 间隔在 `effMinBars` 到 `effMaxBars` 之间，并且当前低点不能明显高于前低，价格容差由 `priceToleranceATR` 控制。

背离部分比较 MACD Histogram、MACD Line、RSI 三项：当前低点处这些指标高于前一个低点时分别记为 H、M、R 背离，背离数量必须达到 `minDivCount`。代码会生成类似 `HMR`、`HR`、`MR` 的背离代码。

过滤部分包括 VPA、关键位和趋势过滤：普通 Zone 默认需要强 VPA，强 VPA 来自吸收下影、努力无结果或假跌破收回；关键位可以来自 Donchian 低点、Keltner 下轨、假跌破或结构极值；如果处于干净下跌背景并启用反趋势过滤，反趋势多头 Zone 需要达到 `majorBottomOk`。

评分由背离数量、强 VPA、关键位、价格新低配合 Histogram 背离、Major Bottom 条件组成，分数必须达到 `effMinScore`。通过冷却、同一区间锁定和替换分数检查后，代码建立 `bullActive`，保存 `bullTrigger` 结构触发线，并画出 L-ZONE 标签。

### 市场含义

代码含义是：下跌后的某个已确认 Pivot Low 附近，价格低点与动能指标之间出现背离，同时具备 VPA 或关键支撑等过滤条件。它表示多头反转的观察区已经形成，但还没有完成结构突破。

### 是否可以作为进场信号

不可以作为正式进场信号。它只是观察区。代码在 L-ZONE 后还要等待 `bullTrigger` 被有效突破，并通过严格质量过滤后才会触发 LONG。

### 适合周期

可以在 LTF 和 HTF 模式下出现。默认 `Auto` 下，30m 及以上会被当作 HTF 背景，30m 以下会被当作 LTF 执行周期。复盘时建议同时记录 30m 背景和 15m / 5m 执行细节。

### 需要配合观察的内容

观察背离代码是 H、M、R 中哪几项；观察是否靠近 Donchian 支撑、Keltner 下轨或前低；观察 VPA 是吸收、努力无结果还是假跌破收回；观察绿色结构触发线 `bullTrigger` 与当前价格的距离。

### 常见失败情况

失败通常对应代码里的失效或过滤不足：Zone 出现后价格继续跌破 `bullLow - 0.05 * ATR`，等待超过 `maxSetupBars`，背离分数虽达标但处于强下跌背景，或后续突破触发线时无法满足量能、EMA、动能、风险或 RR 条件。

### 截图复盘要点

截图需要包含两个 Pivot Low、背离连线、L-ZONE 标签、结构触发线、EMA20 / EMA50、Keltner 下轨、成交量、MACD 和 RSI。重点记录 L-ZONE 到 LONG 之间等了多少根 K 线，以及是否先出现 E-L 或 LATE-L。

## S-ZONE

### 中文含义

空头背离观察区。它表示价格在 Pivot High 附近出现符合评分要求的潜在空头背离区域。

### 代码触发逻辑

`bearZoneSignal` 在已确认的新 Pivot High 上触发。代码会把当前高点与历史高点 Pivot 进行比较，要求两个 Pivot 间隔在 `effMinBars` 到 `effMaxBars` 之间，并且当前高点不能明显低于前高，价格容差由 `priceToleranceATR` 控制。

背离部分比较 MACD Histogram、MACD Line、RSI 三项：当前高点处这些指标低于前一个高点时分别记为 H、M、R 背离，背离数量必须达到 `minDivCount`。

过滤部分包括 VPA、关键位和趋势过滤：普通 Zone 默认需要强 VPA，强 VPA 来自供应上影、努力无结果或假突破收回；关键位可以来自 Donchian 高点、Keltner 上轨、假突破或结构极值；如果处于干净上涨背景并启用反趋势过滤，反趋势空头 Zone 需要达到 `majorTopOk`。

评分由背离数量、强 VPA、关键位、价格新高配合 Histogram 背离、Major Top 条件组成，分数必须达到 `effMinScore`。通过冷却、同一区间锁定和替换分数检查后，代码建立 `bearActive`，保存 `bearTrigger` 结构触发线，并画出 S-ZONE 标签。

### 市场含义

代码含义是：上涨后的某个已确认 Pivot High 附近，价格高点与动能指标之间出现背离，同时具备 VPA 或关键压力等过滤条件。它表示空头反转的观察区已经形成，但还没有完成结构跌破。

### 是否可以作为进场信号

不可以作为正式进场信号。它只是观察区。代码在 S-ZONE 后还要等待 `bearTrigger` 被有效跌破，并通过严格质量过滤后才会触发 SHORT。

### 适合周期

可以在 LTF 和 HTF 模式下出现。默认 `Auto` 下，30m 及以上会被当作 HTF 背景，30m 以下会被当作 LTF 执行周期。复盘时建议同时记录 30m 背景和 15m / 5m 执行细节。

### 需要配合观察的内容

观察背离代码是 H、M、R 中哪几项；观察是否靠近 Donchian 压力、Keltner 上轨或前高；观察 VPA 是供应上影、努力无结果还是假突破收回；观察红色结构触发线 `bearTrigger` 与当前价格的距离。

### 常见失败情况

失败通常对应代码里的失效或过滤不足：Zone 出现后价格继续突破 `bearHigh + 0.05 * ATR`，等待超过 `maxSetupBars`，背离分数虽达标但处于强上涨背景，或后续跌破触发线时无法满足量能、EMA、动能、风险或 RR 条件。

### 截图复盘要点

截图需要包含两个 Pivot High、背离连线、S-ZONE 标签、结构触发线、EMA20 / EMA50、Keltner 上轨、成交量、MACD 和 RSI。重点记录 S-ZONE 到 SHORT 之间等了多少根 K 线，以及是否先出现 E-S 或 LATE-S。

## C-L

### 中文含义

多头 Zone 确认提示。它表示一个多头 Zone 已经在 LTF 模式下被代码接受。

### 代码触发逻辑

`bullConfirmSignal` 在 `bullZoneSignal` 成立时同步赋值为 `isLTFMode`。也就是说，只有当前周期属于 LTF Execution 时，L-ZONE 成立才会同时显示 C-L。

C-L 不单独计算新的背离，也不额外确认突破。它依附于 L-ZONE 的完整评分、VPA、关键位、趋势过滤、冷却和触发线建立逻辑。

### 市场含义

代码含义是：多头观察区已经在执行周期上正式确认，`bullActive` 已建立，后续可以观察是否突破 `bullTrigger`。

### 是否可以作为进场信号

不可以作为正式进场信号。C-L 只是 Zone 确认提示，不代表已经突破结构线。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下，它主要用于 30m 以下周期；15m 会使用 LTF-C 的更严格 Pivot、分数和冷却参数。

### 需要配合观察的内容

观察 C-L 是否与 L-ZONE 对应；观察 C-L 出现时价格距离 `bullTrigger` 多远；观察当前是否已经接近突破、是否有量能和动能转强。

### 常见失败情况

C-L 后价格没有突破结构线，或继续跌破 Zone 低点导致 `bullActive` 失效；也可能突破发生但严格条件不足，只给 E-L 而不给 LONG。

### 截图复盘要点

截图要同时保留 L-ZONE 的 Pivot 标签和 C-L 的确认位置。重点记录 C-L 是不是明显晚于 Pivot 低点，以及确认后价格是否围绕触发线蓄势。

## C-S

### 中文含义

空头 Zone 确认提示。它表示一个空头 Zone 已经在 LTF 模式下被代码接受。

### 代码触发逻辑

`bearConfirmSignal` 在 `bearZoneSignal` 成立时同步赋值为 `isLTFMode`。也就是说，只有当前周期属于 LTF Execution 时，S-ZONE 成立才会同时显示 C-S。

C-S 不单独计算新的背离，也不额外确认跌破。它依附于 S-ZONE 的完整评分、VPA、关键位、趋势过滤、冷却和触发线建立逻辑。

### 市场含义

代码含义是：空头观察区已经在执行周期上正式确认，`bearActive` 已建立，后续可以观察是否跌破 `bearTrigger`。

### 是否可以作为进场信号

不可以作为正式进场信号。C-S 只是 Zone 确认提示，不代表已经跌破结构线。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下，它主要用于 30m 以下周期；15m 会使用 LTF-C 的更严格 Pivot、分数和冷却参数。

### 需要配合观察的内容

观察 C-S 是否与 S-ZONE 对应；观察 C-S 出现时价格距离 `bearTrigger` 多远；观察当前是否已经接近跌破、是否有量能和动能转弱。

### 常见失败情况

C-S 后价格没有跌破结构线，或继续突破 Zone 高点导致 `bearActive` 失效；也可能跌破发生但严格条件不足，只给 E-S 而不给 SHORT。

### 截图复盘要点

截图要同时保留 S-ZONE 的 Pivot 标签和 C-S 的确认位置。重点记录 C-S 是不是明显晚于 Pivot 高点，以及确认后价格是否围绕触发线蓄势。

## E-L

### 中文含义

多头提前观察信号。它表示多头结构突破已经发生，但严格 LONG 条件没有全部通过。

### 代码触发逻辑

`bullEarlySignal` 只在 `bullActive` 已存在、当前为 LTF 模式、价格向上突破 `bullTrigger + ATR * breakoutBufferATR` 后才可能触发。

代码先检查正式 LONG 的严格条件：量能、站上 EMA20、MACD Histogram 与 RSI 同向回升、强空头背景下的上下文过滤、风险距离、可选 RR 过滤。若 `strictOk` 不成立，但 `enableEarlySignal` 开启、该 Zone 尚未发过 E-L、且 `riskOk` 成立，就触发 E-L。

### 市场含义

代码含义是：价格已经尝试向上突破多头触发线，但突破质量不足以被定义为严格 LONG。它是执行观察信号，不是 Zone 本身。

### 是否可以作为进场信号

不作为正式进场信号。E-L 代表严格进场失败后的提前观察，需要等待后续是否重新满足 LONG、形成 PB-L，或被失效。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下主要用于 30m 以下执行周期。

### 需要配合观察的内容

重点看 E-L 缺少哪项严格条件：成交量是否不足、是否未站上 EMA20、MACD Histogram 和 RSI 是否未同步回升、风险是否过大、是否仍处于强空头背景。

### 常见失败情况

常见失败是突破没有量、突破后马上跌回触发线下方，或价格距离止损过远导致风险结构不好。代码层面，后续若跌破 `bullLow - 0.05 * ATR`，该多头结构会失效。

### 截图复盘要点

截图要保留 E-L 当根 K 线、`bullTrigger`、成交量、EMA20、MACD Histogram 和 RSI。复盘时记录 E-L 后是否补出 LONG，还是形成假突破。

## E-S

### 中文含义

空头提前观察信号。它表示空头结构跌破已经发生，但严格 SHORT 条件没有全部通过。

### 代码触发逻辑

`bearEarlySignal` 只在 `bearActive` 已存在、当前为 LTF 模式、价格向下跌破 `bearTrigger - ATR * breakoutBufferATR` 后才可能触发。

代码先检查正式 SHORT 的严格条件：量能、跌破 EMA20、MACD Histogram 与 RSI 同向走弱、强多头背景下的上下文过滤、风险距离、可选 RR 过滤。若 `strictOk` 不成立，但 `enableEarlySignal` 开启、该 Zone 尚未发过 E-S、且 `riskOk` 成立，就触发 E-S。

### 市场含义

代码含义是：价格已经尝试向下跌破空头触发线，但跌破质量不足以被定义为严格 SHORT。它是执行观察信号，不是 Zone 本身。

### 是否可以作为进场信号

不作为正式进场信号。E-S 代表严格进场失败后的提前观察，需要等待后续是否重新满足 SHORT、形成 PB-S，或被失效。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下主要用于 30m 以下执行周期。

### 需要配合观察的内容

重点看 E-S 缺少哪项严格条件：成交量是否不足、是否未跌破 EMA20、MACD Histogram 和 RSI 是否未同步走弱、风险是否过大、是否仍处于强多头背景。

### 常见失败情况

常见失败是跌破没有量、跌破后马上收回触发线上方，或价格距离止损过远导致风险结构不好。代码层面，后续若突破 `bearHigh + 0.05 * ATR`，该空头结构会失效。

### 截图复盘要点

截图要保留 E-S 当根 K 线、`bearTrigger`、成交量、EMA20、MACD Histogram 和 RSI。复盘时记录 E-S 后是否补出 SHORT，还是形成假跌破。

## LATE-L

### 中文含义

多头延迟补确认。它表示 Pivot Low 被确认时，价格已经向上突破了多头触发线。

### 代码触发逻辑

`bullLateSignal` 只在 L-ZONE 刚刚成立、`lateEntryEnabled` 开启、当前为 LTF 模式时检查。

触发条件包括：当前收盘价已经高于 `bullTrigger + ATR * breakoutBufferATR`；当前价格距离触发线不超过 `lateMaxDistanceATR * ATR`；从 Pivot 低点到当前确认时刻的距离不超过 `pR + lateLookbackBars`；MACD Histogram 上升且 RSI 上升；若要求突破量能，则成交量要达到 `volMa * breakoutVolMult`。

### 市场含义

代码含义是：因为 Pivot 需要右侧 K 线确认，等 L-ZONE 被识别出来时，价格可能已经完成突破。LATE-L 用来标记这种“发现时已经突破但还离触发线不远”的补确认。

### 是否可以作为进场信号

不作为追单信号。它不是 LONG，也不会像 LONG 一样建立回踩等待状态。复盘时应把它视为延迟确认提示。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下主要用于 30m 以下周期，尤其是 Pivot 确认延迟容易影响读图的位置。

### 需要配合观察的内容

观察 LATE-L 出现时价格距离 `bullTrigger` 的 ATR 距离；观察是否仍在触发线附近；观察量能、MACD Histogram 和 RSI 是否确实同步转强。

### 常见失败情况

如果 LATE-L 出现时价格已经离触发线太远，虽然代码用 `lateMaxDistanceATR` 做了限制，但实盘复盘仍可能发现盈亏比变差。另一个失败场景是突破后很快跌回触发线下方。

### 截图复盘要点

截图要保留 Pivot Low、L-ZONE、LATE-L、触发线和当前价格与触发线的距离。重点记录 LATE-L 后是否继续走出 LONG 方向，还是变成延迟假突破。

## LATE-S

### 中文含义

空头延迟补确认。它表示 Pivot High 被确认时，价格已经向下跌破了空头触发线。

### 代码触发逻辑

`bearLateSignal` 只在 S-ZONE 刚刚成立、`lateEntryEnabled` 开启、当前为 LTF 模式时检查。

触发条件包括：当前收盘价已经低于 `bearTrigger - ATR * breakoutBufferATR`；当前价格距离触发线不超过 `lateMaxDistanceATR * ATR`；从 Pivot 高点到当前确认时刻的距离不超过 `pR + lateLookbackBars`；MACD Histogram 下降且 RSI 下降；若要求突破量能，则成交量要达到 `volMa * breakoutVolMult`。

### 市场含义

代码含义是：因为 Pivot 需要右侧 K 线确认，等 S-ZONE 被识别出来时，价格可能已经完成跌破。LATE-S 用来标记这种“发现时已经跌破但还离触发线不远”的补确认。

### 是否可以作为进场信号

不作为追单信号。它不是 SHORT，也不会像 SHORT 一样建立回踩等待状态。复盘时应把它视为延迟确认提示。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下主要用于 30m 以下周期，尤其是 Pivot 确认延迟容易影响读图的位置。

### 需要配合观察的内容

观察 LATE-S 出现时价格距离 `bearTrigger` 的 ATR 距离；观察是否仍在触发线附近；观察量能、MACD Histogram 和 RSI 是否确实同步转弱。

### 常见失败情况

如果 LATE-S 出现时价格已经离触发线太远，虽然代码用 `lateMaxDistanceATR` 做了限制，但实盘复盘仍可能发现盈亏比变差。另一个失败场景是跌破后很快收回触发线上方。

### 截图复盘要点

截图要保留 Pivot High、S-ZONE、LATE-S、触发线和当前价格与触发线的距离。重点记录 LATE-S 后是否继续走出 SHORT 方向，还是变成延迟假跌破。

## LONG

### 中文含义

严格多头突破信号。它是代码定义的正式多头进场信号。

### 代码触发逻辑

`longSignal` 只在 `bullActive` 已存在、当前为 LTF 模式、结构未过期且未失效时触发。价格必须收盘突破 `bullTrigger + ATR * breakoutBufferATR`。

突破后，代码要求 `strictOk` 成立：若启用量能过滤，成交量必须大于等于 `volMa * breakoutVolMult`；若启用 EMA 恢复，收盘必须站上 EMA20；若启用动能过滤，MACD Histogram 必须上升且 RSI 必须上升；若启用严格进场且处于强空头背景，则需要 Zone 分数达到 `majorScore` 或收盘站上 EMA20；风险必须大于最小跳动且不超过 `maxRiskATR * ATR`；如果启用 RR 过滤，最近上方阻力需要满足最小盈亏比。

触发 LONG 后，代码关闭 `bullActive`，进入 `waitBullPB` 状态，保存回踩观察位 `bullRetestLevel = bullTrigger`。

### 市场含义

代码含义是：多头背离观察区之后，价格完成向上结构突破，并且突破质量、动能、风险条件通过。

### 是否可以作为进场信号

可以。LONG 是当前代码中正式的严格多头突破进场信号。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下主要用于 30m 以下执行周期。30m 及以上默认更偏背景观察，不触发 LONG。

### 需要配合观察的内容

观察 LONG 对应的前置 L-ZONE、C-L、触发线、成交量、EMA20、MACD Histogram、RSI、止损位置 `bullLow - ATR * atrStopBuffer`，以及是否开启 RR 过滤。

### 常见失败情况

常见失败包括突破后立即跌回触发线下方、突破量能不足但参数关闭导致过滤较松、强空头趋势中反弹突破失败、止损距离过大或上方阻力过近。

### 截图复盘要点

截图必须包含 L-ZONE 到 LONG 的完整路径，包括背离线、结构触发线、LONG 当根 K 线和后续 10 / 20 / 50 根 K 线表现。记录 LONG 后是否出现 PB-L。

## SHORT

### 中文含义

严格空头跌破信号。它是代码定义的正式空头进场信号。

### 代码触发逻辑

`shortSignal` 只在 `bearActive` 已存在、当前为 LTF 模式、结构未过期且未失效时触发。价格必须收盘跌破 `bearTrigger - ATR * breakoutBufferATR`。

跌破后，代码要求 `strictOk` 成立：若启用量能过滤，成交量必须大于等于 `volMa * breakoutVolMult`；若启用 EMA 恢复，收盘必须跌破 EMA20；若启用动能过滤，MACD Histogram 必须下降且 RSI 必须下降；若启用严格进场且处于强多头背景，则需要 Zone 分数达到 `majorScore` 或收盘跌破 EMA20；风险必须大于最小跳动且不超过 `maxRiskATR * ATR`；如果启用 RR 过滤，最近下方支撑需要满足最小盈亏比。

触发 SHORT 后，代码关闭 `bearActive`，进入 `waitBearPB` 状态，保存回踩观察位 `bearRetestLevel = bearTrigger`。

### 市场含义

代码含义是：空头背离观察区之后，价格完成向下结构跌破，并且跌破质量、动能、风险条件通过。

### 是否可以作为进场信号

可以。SHORT 是当前代码中正式的严格空头跌破进场信号。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下主要用于 30m 以下执行周期。30m 及以上默认更偏背景观察，不触发 SHORT。

### 需要配合观察的内容

观察 SHORT 对应的前置 S-ZONE、C-S、触发线、成交量、EMA20、MACD Histogram、RSI、止损位置 `bearHigh + ATR * atrStopBuffer`，以及是否开启 RR 过滤。

### 常见失败情况

常见失败包括跌破后立即收回触发线上方、跌破量能不足但参数关闭导致过滤较松、强多头趋势中回落跌破失败、止损距离过大或下方支撑过近。

### 截图复盘要点

截图必须包含 S-ZONE 到 SHORT 的完整路径，包括背离线、结构触发线、SHORT 当根 K 线和后续 10 / 20 / 50 根 K 线表现。记录 SHORT 后是否出现 PB-S。

## PB-L

### 中文含义

多头突破后的回踩确认。它表示 LONG 之后，价格回踩触发线或 EMA20 并重新收强。

### 代码触发逻辑

`bullPBSignal` 只会在 LONG 触发后进入 `waitBullPB` 状态时检查。代码要求突破后至少等待 `minRetestBars`，且不能超过 `maxRetestBars`。

回踩深度需要满足 `bullPostBreakHigh - low >= ATR * pbMinPullbackATR`，除非最小回撤参数被设为 0。有效回踩可以是触碰 `bullRetestLevel + ATR * retestToleranceATR` 后收在 `bullRetestLevel` 上方，也可以是在允许 EMA 回踩时触碰 EMA20 容差范围后收在 EMA20 上方。最后还要求阳线收盘，并且在启用 PB 动能确认时 MACD Histogram 不低于前一根。

如果价格收盘跌破 `bullRetestLevel - ATR * retestFailATR` 或跌破 LONG 当根低点 `bullBreakLow`，PB-L 等待失败。

### 市场含义

代码含义是：多头突破后并没有直接追涨，而是等待市场回踩突破位或 EMA20，并出现重新承接。

### 是否可以作为进场信号

可以作为突破后的回踩确认信号。它不是原始反转信号，而是 LONG 之后的二次确认。

### 适合周期

只在 LTF 模式下、且已经出现 LONG 后才可能出现。默认 `Auto` 下主要用于 30m 以下执行周期。

### 需要配合观察的内容

观察 LONG 的触发线、回踩是否真的有足够深度、是否回踩到突破位或 EMA20、回踩 K 线是否收阳、MACD Histogram 是否停止走弱。

### 常见失败情况

常见失败是突破后没有足够回踩直接走远，导致没有 PB-L；或回踩过深，收盘跌破回踩失败线；也可能回踩到位但动能没有恢复。

### 截图复盘要点

截图要包含 LONG、突破后的最高点、回踩低点、PB-L 标签、EMA20 和触发线。记录 PB-L 后 10 / 20 / 50 根 K 线是否延续。

## PB-S

### 中文含义

空头跌破后的回踩确认。它表示 SHORT 之后，价格反抽触发线或 EMA20 并重新收弱。

### 代码触发逻辑

`bearPBSignal` 只会在 SHORT 触发后进入 `waitBearPB` 状态时检查。代码要求跌破后至少等待 `minRetestBars`，且不能超过 `maxRetestBars`。

回踩深度需要满足 `high - bearPostBreakLow >= ATR * pbMinPullbackATR`，除非最小回撤参数被设为 0。有效回踩可以是触碰 `bearRetestLevel - ATR * retestToleranceATR` 后收在 `bearRetestLevel` 下方，也可以是在允许 EMA 回踩时触碰 EMA20 容差范围后收在 EMA20 下方。最后还要求阴线收盘，并且在启用 PB 动能确认时 MACD Histogram 不高于前一根。

如果价格收盘突破 `bearRetestLevel + ATR * retestFailATR` 或突破 SHORT 当根高点 `bearBreakHigh`，PB-S 等待失败。

### 市场含义

代码含义是：空头跌破后并没有直接追空，而是等待市场反抽跌破位或 EMA20，并出现重新压制。

### 是否可以作为进场信号

可以作为跌破后的回踩确认信号。它不是原始反转信号，而是 SHORT 之后的二次确认。

### 适合周期

只在 LTF 模式下、且已经出现 SHORT 后才可能出现。默认 `Auto` 下主要用于 30m 以下执行周期。

### 需要配合观察的内容

观察 SHORT 的触发线、反抽是否真的有足够深度、是否回踩到跌破位或 EMA20、回踩 K 线是否收阴、MACD Histogram 是否停止走强。

### 常见失败情况

常见失败是跌破后没有足够反抽直接走远，导致没有 PB-S；或反抽过深，收盘突破回踩失败线；也可能反抽到位但动能没有恢复。

### 截图复盘要点

截图要包含 SHORT、跌破后的最低点、反抽高点、PB-S 标签、EMA20 和触发线。记录 PB-S 后 10 / 20 / 50 根 K 线是否延续。

## TC-L

### 中文含义

多头趋势延续信号。它表示已有上升趋势中的回踩后再突破。

### 代码触发逻辑

`tcLongSignal` 与背离 Zone 无关。它只在 `useTrendContinuation` 开启、当前为 LTF 模式、同方向冷却结束、且本根没有触发 LONG 时检查。

趋势背景要求 `ctxUp` 成立：EMA20 在 EMA50 上方，收盘在 EMA50 上方，且 EMA50 相比 `trendSlopeLen` 前向上。回踩条件要求最近 `tcPullbackLookback` 内低点触及 EMA20 加 ATR 容差范围，并且当前收盘重新站上 EMA20。突破条件要求当前收盘高于过去 `tcBreakLookback` 根前高加 `breakoutBufferATR * ATR`。动能要求 MACD Histogram 上升、RSI 大于 50 且 RSI 上升。量能要求成交量大于等于 `volMa * tcVolMult`。如果启用 `tcRequireHTFBias`，还要求没有相反的 `ctxDown` 背景。

### 市场含义

代码含义是：价格已经处于上升趋势，经过一次靠近 EMA20 的回踩后，再次放量并带动能突破短期高点。

### 是否可以作为进场信号

可以作为趋势延续类进场观察信号。它不是背离反转，也不要求先出现 L-ZONE 或 LONG。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下主要用于 30m 以下执行周期。

### 需要配合观察的内容

观察 EMA20 / EMA50 多头排列、EMA50 斜率、回踩是否靠近 EMA20、突破是否越过最近高点、RSI 是否在 50 上方、量能是否达到阈值。

### 常见失败情况

常见失败是趋势已经进入末端但仍触发延续，回踩只是横盘噪音，突破短高后马上回落，或上方压力太近。代码没有要求先出现背离，因此复盘时要单独判断它是否处于趋势中段还是末端。

### 截图复盘要点

截图要包含 EMA20 / EMA50、回踩段、突破短高的位置、TC-L 标签、成交量、MACD Histogram 和 RSI。重点区分 TC-L 与 LONG：TC-L 来自趋势延续，LONG 来自 Zone 后结构突破。

## TC-S

### 中文含义

空头趋势延续信号。它表示已有下降趋势中的反抽后再跌破。

### 代码触发逻辑

`tcShortSignal` 与背离 Zone 无关。它只在 `useTrendContinuation` 开启、当前为 LTF 模式、同方向冷却结束、且本根没有触发 SHORT 时检查。

趋势背景要求 `ctxDown` 成立：EMA20 在 EMA50 下方，收盘在 EMA50 下方，且 EMA50 相比 `trendSlopeLen` 前向下。反抽条件要求最近 `tcPullbackLookback` 内高点触及 EMA20 减 ATR 容差范围，并且当前收盘重新跌破 EMA20。跌破条件要求当前收盘低于过去 `tcBreakLookback` 根前低减 `breakoutBufferATR * ATR`。动能要求 MACD Histogram 下降、RSI 小于 50 且 RSI 下降。量能要求成交量大于等于 `volMa * tcVolMult`。如果启用 `tcRequireHTFBias`，还要求没有相反的 `ctxUp` 背景。

### 市场含义

代码含义是：价格已经处于下降趋势，经过一次靠近 EMA20 的反抽后，再次放量并带动能跌破短期低点。

### 是否可以作为进场信号

可以作为趋势延续类进场观察信号。它不是背离反转，也不要求先出现 S-ZONE 或 SHORT。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下主要用于 30m 以下执行周期。

### 需要配合观察的内容

观察 EMA20 / EMA50 空头排列、EMA50 斜率、反抽是否靠近 EMA20、跌破是否越过最近低点、RSI 是否在 50 下方、量能是否达到阈值。

### 常见失败情况

常见失败是趋势已经进入末端但仍触发延续，反抽只是横盘噪音，跌破短低后马上收回，或下方支撑太近。代码没有要求先出现背离，因此复盘时要单独判断它是否处于趋势中段还是末端。

### 截图复盘要点

截图要包含 EMA20 / EMA50、反抽段、跌破短低的位置、TC-S 标签、成交量、MACD Histogram 和 RSI。重点区分 TC-S 与 SHORT：TC-S 来自趋势延续，SHORT 来自 Zone 后结构跌破。

## EXH-L

### 中文含义

下跌衰竭提醒。它表示下降背景中的低点附近出现多头方向的衰竭迹象。

### 代码触发逻辑

`bullExhSignal` 只在 `useExhaustion` 开启、当前为 LTF 模式、已确认新 Pivot Low 时检查。它与 L-ZONE 使用同一组 Pivot Low 比较和背离基础，但有单独的 EXH 评分。

基础条件包括：处于下跌背景，定义为 Pivot 处 EMA20 低于 EMA50，或收盘低于 EMA50；两个低点间隔有效；当前低点满足价格容差；H / M / R 背离数量达到 `minDivCount`。

强度条件 `exhStrong` 来自三重背离、假跌破、靠近支撑，或缩量二次测试加努力无结果。极值条件 `exhExtreme` 在默认开启时要求靠近支撑、接近 Keltner 下轨、假跌破或三重背离。评分由背离数量、下跌背景、价格新低、缩量二次测试、努力无结果、靠近支撑组成，并需要达到 `exhMinScore`；如果是干净下跌背景，则需要达到 `trendExhMinScore`。同方向还受 `exhCooldownBars` 冷却限制。

### 市场含义

代码含义是：下跌趋势或弱势背景中，价格继续打低但动能和量价行为显示下跌可能开始衰竭。

### 是否可以作为进场信号

不作为正式反向进场信号。EXH-L 是衰竭提醒，不等于 LONG。后续仍需观察是否形成 L-ZONE、C-L、LONG 或 PB-L。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下主要用于 30m 以下周期。

### 需要配合观察的内容

观察是否在下跌背景中，是否靠近支撑或 Keltner 下轨，是否有 H / M / R 背离，是否是假跌破或缩量二次测试，后续是否能突破结构触发线。

### 常见失败情况

常见失败是强趋势下多次出现衰竭但价格继续下行；或者只有衰竭提醒，没有后续结构突破。EXH-L 的代码目标是提醒下跌衰竭，不负责确认反转。

### 截图复盘要点

截图要保留 EXH-L 对应的 Pivot Low、下跌背景、支撑 / Keltner 下轨、背离指标和后续是否出现 L-ZONE 或 LONG。记录 EXH-L 后 10 / 20 / 50 根 K 线是否止跌。

## EXH-S

### 中文含义

上涨衰竭提醒。它表示上涨背景中的高点附近出现空头方向的衰竭迹象。

### 代码触发逻辑

`bearExhSignal` 只在 `useExhaustion` 开启、当前为 LTF 模式、已确认新 Pivot High 时检查。它与 S-ZONE 使用同一组 Pivot High 比较和背离基础，但有单独的 EXH 评分。

基础条件包括：处于上涨背景，定义为 Pivot 处 EMA20 高于 EMA50，或收盘高于 EMA50；两个高点间隔有效；当前高点满足价格容差；H / M / R 背离数量达到 `minDivCount`。

强度条件 `exhStrong` 来自三重背离、假突破、靠近压力，或缩量二次测试加努力无结果。极值条件 `exhExtreme` 在默认开启时要求靠近压力、接近 Keltner 上轨、假突破或三重背离。评分由背离数量、上涨背景、价格新高、缩量二次测试、努力无结果、靠近压力组成，并需要达到 `exhMinScore`；如果是干净上涨背景，则需要达到 `trendExhMinScore`。同方向还受 `exhCooldownBars` 冷却限制。

### 市场含义

代码含义是：上涨趋势或强势背景中，价格继续冲高但动能和量价行为显示上涨可能开始衰竭。

### 是否可以作为进场信号

不作为正式反向进场信号。EXH-S 是衰竭提醒，不等于 SHORT。后续仍需观察是否形成 S-ZONE、C-S、SHORT 或 PB-S。

### 适合周期

只在 LTF 模式下出现。默认 `Auto` 下主要用于 30m 以下周期。

### 需要配合观察的内容

观察是否在上涨背景中，是否靠近压力或 Keltner 上轨，是否有 H / M / R 背离，是否是假突破或缩量二次测试，后续是否能跌破结构触发线。

### 常见失败情况

常见失败是强趋势下多次出现衰竭但价格继续上行；或者只有衰竭提醒，没有后续结构跌破。EXH-S 的代码目标是提醒上涨衰竭，不负责确认反转。

### 截图复盘要点

截图要保留 EXH-S 对应的 Pivot High、上涨背景、压力 / Keltner 上轨、背离指标和后续是否出现 S-ZONE 或 SHORT。记录 EXH-S 后 10 / 20 / 50 根 K 线是否滞涨。
