# DVCA Case Lifecycle

本文件用于说明案例从入库到完成复盘的生命周期。该机制只管理案例数据库，不修改 DVCA Pine 指标，不改变 Signal Manual 和 Line Patterns 的解释。

## 设计原因

过去案例进入数据库后，如果结果仍是 `Unknown`，很容易忘记后续 10 / 20 / 50 根 K 线表现。Case Lifecycle 的目标是让每个案例都有明确的下一步，避免只收截图、不复盘结果。

## 新增字段

- `state`：案例当前所处的内部状态。
- `next_expected_state`：下一次应该记录的复盘节点。
- `lifecycle_status`：案例生命周期状态。

## lifecycle_status 定义

- `Open`：案例刚进入数据库，等待记录信号后 10 根 K 线表现。
- `Review10`：已经记录 Outcome10，等待记录 Outcome20。
- `Review20`：已经记录 Outcome20，等待记录 Outcome50。
- `Closed`：已经记录 Outcome50，或已手动关闭，不再继续等待。

## state 定义

- `SignalCaptured`：信号已捕获，尚未记录 Outcome10。
- `Outcome10Recorded`：已记录 Outcome10。
- `Outcome20Recorded`：已记录 Outcome20。
- `Outcome50Recorded`：已记录 Outcome50。
- `Closed`：案例已关闭。

## next_expected_state 定义

- `Outcome10`：下一步观察信号后 10 根 K 线表现。
- `Outcome20`：下一步观察信号后 20 根 K 线表现。
- `Outcome50`：下一步观察信号后 50 根 K 线表现。
- `None`：没有下一步复盘。

## 标准流程

```text
SignalCaptured
  ↓
Outcome10Recorded
  ↓
Outcome20Recorded
  ↓
Outcome50Recorded
  ↓
Closed
```

对应生命周期：

```text
Open
  ↓
Review10
  ↓
Review20
  ↓
Closed
```

## 复盘脚本

使用 `scripts/review_case.py` 复盘单个案例：

```bash
python3 scripts/review_case.py CASE-0009
```

脚本会显示当前案例是否已经记录 10 / 20 / 50 根 K 线表现，并在交互模式下询问是否已经达到对应 K 线数量。

也可以使用非交互方式更新：

```bash
python3 scripts/review_case.py CASE-0009 --bars 10 --outcome10 "10根K后继续下跌，TC-S 延续有效"
python3 scripts/review_case.py CASE-0009 --bars 20 --outcome20 "20根K后维持空头结构"
python3 scripts/review_case.py CASE-0009 --bars 50 --outcome50 "50根K后完成一段空头延续" --close
```

## Result 自动计算

如果没有手动传入 `--result`，脚本会根据 `Outcome10`、`Outcome20`、`Outcome50` 的文字自动推断 `result`。

- 出现 `成功`、`有效`、`顺向`、`继续跌`、`继续涨`、`延续` 等关键词，倾向 `Success`。
- 出现 `失败`、`反向`、`失效`、`止损`、`invalid` 等关键词，倾向 `Fail`。
- 出现 `过早`，倾向 `Early`。
- 出现 `过晚`，倾向 `Late`。
- 出现 `不交易`、`只观察`、`NoTrade`，倾向 `NoTrade`。
- 没有足够信息时保持 `Unknown`。

最终结果仍以截图和复盘事实为准。自动计算只是辅助，必要时可以用 `--result` 手动覆盖。
