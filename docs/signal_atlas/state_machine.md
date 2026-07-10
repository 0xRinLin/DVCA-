# DVCA v1.5.1 状态机

本文件描述 DVCA v1.5.1 中真实存在的状态变量和状态切换。所有内容基于 `indicator/dvca_v1_5_1.pine`。

## 核心状态变量

- `bullActive`：多头 Zone 已经成立，等待向上突破 `bullTrigger`。
- `bearActive`：空头 Zone 已经成立，等待向下跌破 `bearTrigger`。
- `waitBullPB`：LONG 已经出现，等待多头回踩确认 PB-L。
- `waitBearPB`：SHORT 已经出现，等待空头反抽确认 PB-S。
- `lastBullZoneIndex` / `lastBearZoneIndex`：记录同方向 Zone 冷却。
- `lastBullExhIndex` / `lastBearExhIndex`：记录同方向 EXH 冷却。
- `lastTCLongIndex` / `lastTCShortIndex`：记录同方向 TC 冷却。

## 多头反转状态机

```mermaid
flowchart TD
    A["等待新 Pivot Low"] --> B["newPL 已确认"]
    B --> C["比较历史 Pivot Low"]
    C --> D{"背离数量 >= minDivCount"}
    D -- "否" --> Z["不生成 L-ZONE"]
    D -- "是" --> E{"VPA / 关键位 / 趋势过滤 / 分数通过"}
    E -- "否" --> Z
    E -- "是" --> F["bullZoneSignal = true"]
    F --> G["bullActive = true"]
    G --> H["保存 bullTrigger / bullLow / bullScore"]
    H --> I{"确认时已经突破且距离不远"}
    I -- "是" --> J["bullLateSignal = true"]
    I -- "否" --> K["等待突破 bullTrigger"]
    K --> L{"超过 maxSetupBars"}
    L -- "是" --> M["bullActive = false, B expired"]
    L -- "否" --> N{"跌破 bullLow - 0.05 ATR"}
    N -- "是" --> O["bullActive = false, B invalid"]
    N -- "否" --> P{"close > bullTrigger + buffer"}
    P -- "否" --> K
    P -- "是" --> Q{"strictOk 通过"}
    Q -- "否, riskOk 且未发 E-L" --> R["bullEarlySignal = true"]
    Q -- "否" --> K
    Q -- "是" --> S["longSignal = true"]
    S --> T["bullActive = false"]
    T --> U["waitBullPB = true"]
```

### 多头状态说明

- `L-ZONE` 出现后，代码进入 `bullActive`。
- `bullActive` 期间只观察突破、过期或失效。
- `LONG` 出现后，多头反转状态结束，转入 `waitBullPB`。
- `E-L` 只表示突破发生但严格条件不足，不会结束 `bullActive`。
- `LATE-L` 是 Zone 被确认时价格已经突破触发线的补确认，不等同于 LONG。

## 空头反转状态机

```mermaid
flowchart TD
    A["等待新 Pivot High"] --> B["newPH 已确认"]
    B --> C["比较历史 Pivot High"]
    C --> D{"背离数量 >= minDivCount"}
    D -- "否" --> Z["不生成 S-ZONE"]
    D -- "是" --> E{"VPA / 关键位 / 趋势过滤 / 分数通过"}
    E -- "否" --> Z
    E -- "是" --> F["bearZoneSignal = true"]
    F --> G["bearActive = true"]
    G --> H["保存 bearTrigger / bearHigh / bearScore"]
    H --> I{"确认时已经跌破且距离不远"}
    I -- "是" --> J["bearLateSignal = true"]
    I -- "否" --> K["等待跌破 bearTrigger"]
    K --> L{"超过 maxSetupBars"}
    L -- "是" --> M["bearActive = false, S expired"]
    L -- "否" --> N{"突破 bearHigh + 0.05 ATR"}
    N -- "是" --> O["bearActive = false, S invalid"]
    N -- "否" --> P{"close < bearTrigger - buffer"}
    P -- "否" --> K
    P -- "是" --> Q{"strictOk 通过"}
    Q -- "否, riskOk 且未发 E-S" --> R["bearEarlySignal = true"]
    Q -- "否" --> K
    Q -- "是" --> S["shortSignal = true"]
    S --> T["bearActive = false"]
    T --> U["waitBearPB = true"]
```

### 空头状态说明

- `S-ZONE` 出现后，代码进入 `bearActive`。
- `bearActive` 期间只观察跌破、过期或失效。
- `SHORT` 出现后，空头反转状态结束，转入 `waitBearPB`。
- `E-S` 只表示跌破发生但严格条件不足，不会结束 `bearActive`。
- `LATE-S` 是 Zone 被确认时价格已经跌破触发线的补确认，不等同于 SHORT。

## PB 状态机

```mermaid
flowchart TD
    A["LONG"] --> B["waitBullPB = true"]
    B --> C{"等待 >= minRetestBars"}
    C -- "否" --> B
    C -- "是" --> D{"超过 maxRetestBars"}
    D -- "是" --> E["waitBullPB = false"]
    D -- "否" --> F{"回踩失败"}
    F -- "是" --> G["PB-L fail, waitBullPB = false"]
    F -- "否" --> H{"回踩深度 + 触发线/EMA20 + 阳线 + 动能"}
    H -- "是" --> I["bullPBSignal = true"]
    H -- "否" --> B

    J["SHORT"] --> K["waitBearPB = true"]
    K --> L{"等待 >= minRetestBars"}
    L -- "否" --> K
    L -- "是" --> M{"超过 maxRetestBars"}
    M -- "是" --> N["waitBearPB = false"]
    M -- "否" --> O{"反抽失败"}
    O -- "是" --> P["PB-S fail, waitBearPB = false"]
    O -- "否" --> Q{"反抽深度 + 触发线/EMA20 + 阴线 + 动能"}
    Q -- "是" --> R["bearPBSignal = true"]
    Q -- "否" --> K
```

### PB 状态说明

- PB-L 只能来自 LONG 后的 `waitBullPB`。
- PB-S 只能来自 SHORT 后的 `waitBearPB`。
- 代码不允许没有 LONG/SHORT 就直接出现 PB-L/PB-S。
- PB 等待会因为失败条件或超过 `maxRetestBars` 结束。

## TC 独立状态机

```mermaid
flowchart TD
    A["每根 confirmed bar"] --> B{"useTrendContinuation 且 isLTFMode"}
    B -- "否" --> Z["不检查 TC"]
    B -- "是" --> C{"TC 冷却通过"}
    C -- "否" --> Z
    C -- "是" --> D{"EMA 趋势背景成立"}
    D -- "否" --> Z
    D -- "是" --> E{"回踩/反抽 EMA20 成立"}
    E -- "否" --> Z
    E -- "是" --> F{"突破短高/跌破短低"}
    F -- "否" --> Z
    F -- "是" --> G{"动能 + 量能 + 背景过滤"}
    G -- "否" --> Z
    G -- "是, 多头" --> H["tcLongSignal = true"]
    G -- "是, 空头" --> I["tcShortSignal = true"]
```

### TC 状态说明

- TC-L / TC-S 不依赖 L-ZONE / S-ZONE。
- TC-L 要求 `not longSignal`，TC-S 要求 `not shortSignal`，避免同一根和正式突破信号重叠。
- TC 是趋势延续路径，不是背离反转路径。

## EXH 独立提醒

```mermaid
flowchart TD
    A["确认新 Pivot"] --> B{"useExhaustion 且 isLTFMode"}
    B -- "否" --> Z["不检查 EXH"]
    B -- "是" --> C{"趋势背景符合衰竭方向"}
    C -- "否" --> Z
    C -- "是" --> D{"背离数量和时间/价格条件通过"}
    D -- "否" --> Z
    D -- "是" --> E{"exhStrong + exhExtreme + 分数通过"}
    E -- "否" --> Z
    E -- "是, Pivot Low" --> F["bullExhSignal = true"]
    E -- "是, Pivot High" --> G["bearExhSignal = true"]
```

### EXH 状态说明

- EXH-L / EXH-S 是提醒，不会设置 `bullActive` 或 `bearActive`。
- EXH 不会直接生成 LONG / SHORT。
- EXH 后是否转化为 Zone 或 Entry，需要在案例库中通过 `signal_chain` 记录。

