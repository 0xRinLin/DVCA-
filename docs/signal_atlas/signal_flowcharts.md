# DVCA v1.5.1 信号流程图

本文件用流程图描述 DVCA v1.5.1 的主要信号路径。图中所有节点都对应当前 Pine 代码中的实际逻辑。

## 总览流程

```mermaid
flowchart TD
    A["K线确认 barstate.isconfirmed"] --> B{"出现 Pivot Low 或 Pivot High"}
    B -- "Pivot Low" --> C["多头背离 / L-ZONE / EXH-L 检查"]
    B -- "Pivot High" --> D["空头背离 / S-ZONE / EXH-S 检查"]
    B -- "无 Pivot" --> E["独立 TC 检查"]
    C --> F["bullActive 或 EXH-L"]
    D --> G["bearActive 或 EXH-S"]
    F --> H["L-ZONE -> LONG -> PB-L"]
    G --> I["S-ZONE -> SHORT -> PB-S"]
    E --> J["TC-L / TC-S"]
```

## L-ZONE 到 LONG

```mermaid
flowchart TD
    A["newPL"] --> B["比较历史 Pivot Low"]
    B --> C{"H/M/R 背离数量达标"}
    C -- "否" --> X["无 L-ZONE"]
    C -- "是" --> D{"VPA 过滤通过"}
    D -- "否" --> X
    D -- "是" --> E{"关键位或结构极值通过"}
    E -- "否" --> X
    E -- "是" --> F{"趋势过滤通过"}
    F -- "否" --> X
    F -- "是" --> G{"score >= effMinScore"}
    G -- "否" --> X
    G -- "是" --> H["L-ZONE + C-L"]
    H --> I["保存 bullTrigger"]
    I --> J{"已突破且距离触发线不远"}
    J -- "是" --> K["LATE-L"]
    J -- "否" --> L["等待突破"]
    L --> M{"close > bullTrigger + ATR buffer"}
    M -- "否" --> L
    M -- "是" --> N{"strictOk"}
    N -- "是" --> O["LONG"]
    N -- "否" --> P["E-L 或继续等待"]
```

## S-ZONE 到 SHORT

```mermaid
flowchart TD
    A["newPH"] --> B["比较历史 Pivot High"]
    B --> C{"H/M/R 背离数量达标"}
    C -- "否" --> X["无 S-ZONE"]
    C -- "是" --> D{"VPA 过滤通过"}
    D -- "否" --> X
    D -- "是" --> E{"关键位或结构极值通过"}
    E -- "否" --> X
    E -- "是" --> F{"趋势过滤通过"}
    F -- "否" --> X
    F -- "是" --> G{"score >= effMinScore"}
    G -- "否" --> X
    G -- "是" --> H["S-ZONE + C-S"]
    H --> I["保存 bearTrigger"]
    I --> J{"已跌破且距离触发线不远"}
    J -- "是" --> K["LATE-S"]
    J -- "否" --> L["等待跌破"]
    L --> M{"close < bearTrigger - ATR buffer"}
    M -- "否" --> L
    M -- "是" --> N{"strictOk"}
    N -- "是" --> O["SHORT"]
    N -- "否" --> P["E-S 或继续等待"]
```

## LONG 到 PB-L

```mermaid
flowchart TD
    A["LONG"] --> B["waitBullPB = true"]
    B --> C["记录 bullRetestLevel = bullTrigger"]
    C --> D{"等待 minRetestBars"}
    D -- "否" --> B
    D -- "是" --> E{"回撤深度达标"}
    E -- "否" --> B
    E -- "是" --> F{"触及触发线或 EMA20"}
    F -- "否" --> B
    F -- "是" --> G{"收阳 + 动能确认"}
    G -- "是" --> H["PB-L"]
    G -- "否" --> B
    B --> I{"失败或超时"}
    I -- "是" --> J["结束 PB 等待"]
```

## SHORT 到 PB-S

```mermaid
flowchart TD
    A["SHORT"] --> B["waitBearPB = true"]
    B --> C["记录 bearRetestLevel = bearTrigger"]
    C --> D{"等待 minRetestBars"}
    D -- "否" --> B
    D -- "是" --> E{"反抽深度达标"}
    E -- "否" --> B
    E -- "是" --> F{"触及触发线或 EMA20"}
    F -- "否" --> B
    F -- "是" --> G{"收阴 + 动能确认"}
    G -- "是" --> H["PB-S"]
    G -- "否" --> B
    B --> I{"失败或超时"}
    I -- "是" --> J["结束 PB 等待"]
```

## TC-L 趋势延续

```mermaid
flowchart TD
    A["LTF confirmed bar"] --> B{"ctxUp 成立"}
    B -- "否" --> X["无 TC-L"]
    B -- "是" --> C{"回踩 EMA20 附近后收回"}
    C -- "否" --> X
    C -- "是" --> D{"突破最近短高 + ATR buffer"}
    D -- "否" --> X
    D -- "是" --> E{"MACD-H 上升 + RSI > 50 且上升"}
    E -- "否" --> X
    E -- "是" --> F{"成交量达标 + 冷却通过"}
    F -- "否" --> X
    F -- "是" --> G["TC-L"]
```

## TC-S 趋势延续

```mermaid
flowchart TD
    A["LTF confirmed bar"] --> B{"ctxDown 成立"}
    B -- "否" --> X["无 TC-S"]
    B -- "是" --> C{"反抽 EMA20 附近后跌回"}
    C -- "否" --> X
    C -- "是" --> D{"跌破最近短低 - ATR buffer"}
    D -- "否" --> X
    D -- "是" --> E{"MACD-H 下降 + RSI < 50 且下降"}
    E -- "否" --> X
    E -- "是" --> F{"成交量达标 + 冷却通过"}
    F -- "否" --> X
    F -- "是" --> G["TC-S"]
```

## EXH-L / EXH-S 衰竭提醒

```mermaid
flowchart TD
    A["新 Pivot Low / High"] --> B{"LTF 且 useExhaustion"}
    B -- "否" --> X["无 EXH"]
    B -- "是" --> C{"趋势背景与衰竭方向一致"}
    C -- "否" --> X
    C -- "是" --> D{"背离数量达标"}
    D -- "否" --> X
    D -- "是" --> E{"exhStrong"}
    E -- "否" --> X
    E -- "是" --> F{"exhExtreme"}
    F -- "否" --> X
    F -- "是" --> G{"exhScore 达标 + 冷却通过"}
    G -- "否" --> X
    G -- "是, Low" --> H["EXH-L"]
    G -- "是, High" --> I["EXH-S"]
```

