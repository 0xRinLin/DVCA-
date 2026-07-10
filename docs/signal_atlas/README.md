# DVCA Signal Atlas

本目录用于建立 DVCA v1.5.1 的状态机、信号流程图和案例归档映射。

本阶段只新增文档，不修改 `indicator/dvca_v1_5_1.pine`，不修改 `data/case_database.csv` 的字段结构。

## 文档索引

- `state_machine.md`：DVCA v1.5.1 的核心状态机，包括多头反转、空头反转、PB、TC 和 EXH。
- `signal_flowcharts.md`：从 Pivot 到 Zone、从 Zone 到 LONG/SHORT、从 LONG/SHORT 到 PB，以及 TC/EXH 的流程图。
- `case_mapping.md`：Signal Atlas 与案例数据库字段的对应关系，用于截图复盘和 `case_database.csv` 填写。
- `review_paths.md`：复盘时按路径阅读信号的顺序，帮助判断一个截图应该归到哪类案例。

## 代码依据

Signal Atlas 的核心依据来自 `indicator/dvca_v1_5_1.pine`：

- Pivot 背离与 Zone：`newPL`、`newPH`、`bullZoneSignal`、`bearZoneSignal`
- 活跃状态：`bullActive`、`bearActive`
- 结构触发线：`bullTrigger`、`bearTrigger`
- 正式突破信号：`longSignal`、`shortSignal`
- 回踩确认状态：`waitBullPB`、`waitBearPB`
- PB 确认：`bullPBSignal`、`bearPBSignal`
- 趋势延续：`tcLongSignal`、`tcShortSignal`
- 衰竭提醒：`bullExhSignal`、`bearExhSignal`
- 延迟确认：`bullLateSignal`、`bearLateSignal`

## 阅读顺序

1. 先读 `state_machine.md`，理解代码中的状态如何切换。
2. 再读 `signal_flowcharts.md`，理解每个信号链条的触发路径。
3. 记录案例时读 `case_mapping.md`，把信号链映射到案例数据库字段。
4. 截图复盘时读 `review_paths.md`，按路径检查当前截图属于反转、回踩、趋势延续还是衰竭。

## 重要原则

- L-ZONE / S-ZONE 是观察区，不是进场信号。
- C-L / C-S 是 LTF 模式下 Zone 成立后的确认提示，不是正式进场。
- LONG / SHORT 是 Zone 后的严格突破信号。
- PB-L / PB-S 必须发生在 LONG / SHORT 之后。
- TC-L / TC-S 是独立的趋势延续分支，不依赖背离 Zone。
- EXH-L / EXH-S 是衰竭提醒，不是正式反向进场。
- LATE-L / LATE-S 是 Pivot 延迟确认后的补确认，不应解释为追单信号。

