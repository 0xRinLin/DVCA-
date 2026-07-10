# DVCA 三级案例体系

本文件用于规定截图、候选案例、黄金案例的分层标准。核心原则是：不要把所有截图都录入数据库，只把值得研究的信号进入案例库。

## 总体结构

DVCA 研究资料分为三层：

- Level 1：Raw，原始截图。
- Level 2：Candidate，候选案例。
- Level 3：Gold，黄金案例。

这三层的目的不同，不能混用。

## Level 1：Raw 原始截图

Raw 是所有“看起来有意思”的截图存档层。

建议路径：

```text
screenshots/
├── BTCUSDT/
│   └── 2026-07-06/
│       ├── BTC_30m.png
│       ├── BTC_15m.png
│       ├── BTC_5m.png
│       └── BTC_1m_before.png
├── ETHUSDT/
└── SOLUSDT/
```

Raw 层规则：

- 可以多存。
- 不需要马上录入 `data/case_database.csv`。
- 不需要马上判断结果。
- 可以记录“before”和“after”截图。
- 只是发现现象，不等于完整案例。

适合进入 Raw 的内容：

- 看到一个加速段，但结果还没出来。
- 看到一个可能的 TC、EXH、Zone，但后续还没确认。
- 发现一个问题，例如“为什么没有 LONG？”
- 想稍后继续观察的结构。

## Level 2：Candidate 候选案例

Candidate 是进入数据库的研究案例。

路径：

```text
data/case_database.csv
cases/
```

进入 Candidate 的标准：

- 信号链已经相对完整。
- 或者失败已经明确。
- 或者现象特别漂亮，值得未来统计。
- 或者现象特别奇怪，值得研究。

录入方式：

```bash
python3 scripts/add_case.py ...
```

Candidate 必须至少填写：

- `symbol`
- `timeframe`
- `direction`
- `main_signal`
- `signal_chain`
- `pattern_type`
- `result`
- `screenshot_path`
- `notes`

## Level 3：Gold 黄金案例

Gold 是最标准、最教科书式的案例层。

路径：

```text
gold_cases/
├── BTC/
│   ├── LONG/
│   ├── PB/
│   ├── TC/
│   └── EXH/
├── ETH/
└── SOL/
```

Gold 层规则：

- 只放最有代表性的案例。
- 不追求数量。
- 必须能清楚说明一个信号或线段类型。
- 未来 Signal Atlas、升级路线和教学说明优先引用 Gold 案例。

适合进入 Gold 的内容：

- 标准 L-ZONE → LONG → PB-L。
- 标准 S-ZONE → SHORT → PB-S。
- 标准 TC-L / TC-S 趋势延续。
- 标准 EXH 后转 Zone 或反转。
- 非常清楚的失败案例。

## 什么截图不要直接录数据库

以下情况先放 Raw，不要直接录数据库：

- 只发现一个问题，结果还没出来。
- 加速段还在运行，未出现后续 30 根 K。
- 只是看起来像 EXH，但没有后续确认。
- 只是图形奇怪，还不知道是 TC、EXH、Zone 还是震荡。
- 没有截图 after 阶段，无法判断结果。

## 进入数据库的四类标准

只有满足下面任意一类，才进入 `case_database.csv`。

### 第一类：完整流程

例如：

```text
L-ZONE → LONG → PB-L
S-ZONE → SHORT → PB-S
EXH-L → L-ZONE → LONG
```

### 第二类：失败案例

失败案例非常重要，必须保留。

例如：

```text
LONG → Fail
SHORT → Fail
E-L → Fail
TC-L → Fail
```

### 第三类：特别漂亮

例如：

```text
BTC 连续 4 个 TC-L
SOL 标准 S-ZONE → SHORT → PB-S
```

### 第四类：特别奇怪

例如：

```text
BTC 趋势很强，但为什么没有 LONG？
SOL 出现 Zone，却迟迟没有 SHORT。
```

这类案例可以先建立 Research Question，再等收集到足够截图后录入 Candidate。

## 当前建议流程

1. 看到有意思的图，先保存到 `screenshots/`。
2. 如果只是问题，记录到 `research/questions/`。
3. 继续观察 after 截图。
4. 结果明确后，再决定是否进入 `case_database.csv`。
5. 最标准的案例，复制或引用到 `gold_cases/`。

