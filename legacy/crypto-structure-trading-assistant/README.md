# Crypto Structure Trading Assistant

这是一个 TradingView Pine Script v5 结构型交易观察指标项目，主要用于加密货币市场。

## 项目目的

本项目用于开发一个交易观察辅助指标，帮助观察：

- Market Regime 行情状态
- Dow Structure 道氏结构
- Swing High / Swing Low
- HH / HL / LH / LL
- L-ZONE / S-ZONE
- Breakout Score 突破质量
- 回踩与反抽机会
- LONG / SHORT 参考信号
- 离场参考信号
- 风险边界与失效条件

## 重要说明

本项目不是自动交易机器人。

本项目不是投资建议。

本项目采用方案驱动开发。

当前项目路线已经升级为研究验证驱动开发。进入 Pine 实现前，需要先完成 Research Validation，用案例和统计验证核心规则。

最高优先级方案文件是：

docs/project_plan_v1.md

任何重大变更都必须先更新 docs/project_plan_v1.md。

## 适用市场

- BTC
- ETH
- SOL
- 其他高流动性加密货币交易对

## 适用周期

- 15m
- 1h
- 4h
- 1D

## 版本路线

- v0.1：项目文档版
- v0.2：规则文档版
- v0.3：状态机文档版
- v0.3.5：Research Validation Phase
- v0.4：Pine 基础指标版，需在验证完成后进入
- v0.5：结构识别版
- v0.6：交易信号版
- v0.7：准确性过滤版
- v1.0：正式观察版

## 当前阶段

当前建议阶段是 v0.3.5 Research Validation Phase。

本阶段不急于写 Pine，而是先收集标准化案例，统计 LONG、SHORT、PB、BO、EXH、XL、XS 等规则表现，验证 Breakout Score 阈值和不同市场、周期的信号差异。
