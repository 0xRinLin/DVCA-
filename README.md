# DVCA Signal Study

本项目用于研究和复盘 TradingView 指标 DVCA v1.5.1。

项目用途包括：

- 固定 DVCA v1.5.1 作为当前研究基准版本。
- 建立完整的 DVCA 信号说明书，所有解释都基于当前 Pine Script 代码逻辑。
- 通过截图记录 BTC、ETH、SOL 等币种在不同周期下的信号表现。
- 建立案例库，对有效信号、失败信号、趋势延续、反转和衰竭形态进行分类归档。
- 通过真实案例统计，为后续是否升级到 DVCA 2.0 提供依据。

当前阶段的核心原则是：先记录、先复盘、先统计，再决定是否修改指标逻辑。

## Phase 2：案例数据库系统

Phase 2 用于建立 DVCA 案例记录、标签系统和统计脚本。所有案例都记录在 `data/case_database.csv` 中，所有统计都基于该文件生成。

### 新增案例

使用 `scripts/add_case.py` 新增案例。脚本会自动生成 `case_id`，写入 CSV，并创建对应的 Markdown 案例文件。

```bash
python scripts/add_case.py --date 2026-07-05 --symbol BTCUSDT --timeframe 30m --direction LONG --main_signal TC-L --signal_chain "TC-L" --pattern_type TrendContinuation --market_context TrendUp --ema_context AboveEMA50 --result Success --screenshot_path "screenshots/BTCUSDT/example.png" --notes "BTC趋势延续案例"
```

### 查询案例

使用 `scripts/show_cases.py` 查询案例，可按 symbol、timeframe、main_signal、pattern_type、result 过滤。

```bash
python scripts/show_cases.py --symbol BTCUSDT
python scripts/show_cases.py --main_signal TC-L --result Fail
python scripts/show_cases.py --pattern_type Pullback
```

### 统计案例

使用 `scripts/analyze_statistics.py` 统计案例数量、信号成功率、品种表现、PB 对比和 TC 表现。统计结果会输出到终端，并写入 `data/statistics_summary.md`。

```bash
python scripts/analyze_statistics.py
```

### 生成案例报告

使用 `scripts/generate_case_report.py` 根据 `case_id` 生成或更新案例 Markdown 报告。

```bash
python scripts/generate_case_report.py --case_id CASE-0001
```

### 复盘案例生命周期

Case Lifecycle 用来跟踪案例是否已经完成 10 / 20 / 50 根 K 线复盘。使用 `scripts/review_case.py` 输入案例编号，脚本会提醒当前案例下一步该看什么，并更新 CSV 与对应 Markdown。

```bash
python scripts/review_case.py CASE-0009
python scripts/review_case.py CASE-0009 --bars 10 --outcome10 "10根K后继续下跌，TC-S 延续有效"
python scripts/review_case.py CASE-0009 --bars 50 --outcome50 "50根K后空头延续完成" --close
```

生命周期状态为：

- `Open`：等待 Outcome10。
- `Review10`：等待 Outcome20。
- `Review20`：等待 Outcome50。
- `Closed`：复盘完成或手动关闭。

### 推荐工作流

1. 保存截图到 `screenshots/` 对应品种目录。
2. 判断这只是 Raw 截图、Candidate 案例，还是 Gold 案例。
3. 只有 Candidate 才用 `add_case.py` 新增案例。
4. 用 `show_cases.py` 检查案例是否写入正确。
5. 用 `review_case.py` 在 10 / 20 / 50 根 K 后更新复盘结果。
6. 用 `analyze_statistics.py` 更新统计结果。
7. 用 `generate_case_report.py` 生成或刷新复盘报告。

## Phase 3：Signal Atlas 与研究问题

Phase 3 用于把 DVCA 研究从“收集截图”升级为“围绕问题做交易研究”。

### 三级案例体系

项目采用 Raw / Candidate / Gold 三层结构：

- `screenshots/`：Raw 原始截图。所有有意思但尚未完成的图先放这里，不急着入库。
- `data/case_database.csv` + `cases/`：Candidate 候选案例。只有完整流程、明确失败、特别漂亮或特别奇怪的信号才进入数据库。
- `gold_cases/`：Gold 黄金案例。只保存最标准、最有代表性的案例，未来 Signal Atlas 和升级研究优先引用这里。

详细规则见：

```text
docs/case_selection_framework.md
```

### Research Questions

如果你发现的是一个问题，而不是完整案例，先写入：

```text
research/questions/
```

例如：

```text
research/questions/2026-07-06_BTC_TC_many_LONG_few.md
```

研究路径：

1. 在 `questions/` 记录问题。
2. 在 `screenshots/` 保存 before / after 图。
3. 收集 20-30 个相关 Candidate 案例。
4. 在 `findings/` 总结阶段性发现。
5. 在 `conclusions/` 写最终结论，再决定是否修改 DVCA。

### 重要原则

不要把所有截图都录入数据库。Raw 是观察，Candidate 是研究样本，Gold 是高价值教材。

## Trading Desk Report

`DVCA Trading Desk Report` 是每日多周期盘面复盘的固定格式，用于统一记录：

- Market State
- Signal Chain
- 多周期一致性
- Trading Plan
- Scenario
- Risk Assessment
- Execution
- 是否值得入库
- 对 DVCA 2.0 的研究反馈

格式说明见：

```text
docs/trading_desk_report.md
```

模板见：

```text
templates/trading_desk_report_template.md
```

正式报告归档在：

```text
reports/trading_desk/
```
