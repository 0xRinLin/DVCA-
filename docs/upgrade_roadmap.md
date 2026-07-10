# DVCA 升级路线

## 阶段一：冻结 v1.5.1，建立案例库

- 固定 `indicator/dvca_v1_5_1.pine` 作为研究基准版本。
- 不在当前版本上频繁修改指标代码。
- 优先收集不同币种、不同周期、不同市场状态下的截图案例。

## 阶段二：统计 BTC、ETH、SOL 的信号表现

- 统计 BTCUSDT、ETHUSDT、SOLUSDT 的信号有效率。
- 按周期记录 1H、30m、15m、5m 的表现差异。
- 区分反转、延续、回踩、衰竭等不同信号类型。

## 阶段三：找出 TC、LONG、PB、EXH 的误判原因

- 分析 TC 信号在趋势延续和假突破中的表现。
- 分析 LONG/SHORT 是否过早或过晚。
- 分析 PB 信号是否需要更严格的趋势过滤。
- 分析 EXH 信号是否更适合作为减仓或观察信号。

## 阶段四：设计 DVCA 2.0，不在 1.5.x 上盲目堆功能

- 先完成案例统计，再决定新版本结构。
- 避免在 v1.5.x 上不断叠加零散过滤条件。
- 将有效规则整理成独立模块，为 DVCA 2.0 做准备。

## 阶段五：引入 Market Regime Engine

DVCA 2.0 可考虑引入市场状态引擎，用于识别：

- Trend
- Range
- Expansion
- Climax

## 阶段六：重新统一 Reversal Entry、Trend Entry、Pullback Entry

- 重新定义 Reversal Entry。
- 重新定义 Trend Entry。
- 重新定义 Pullback Entry。
- 让不同信号在不同市场状态下拥有明确职责。

