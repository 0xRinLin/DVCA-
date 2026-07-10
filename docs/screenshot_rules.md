# 截图规则

## Raw 截图原则

- 不是所有截图都要录入数据库。
- 所有觉得有意思但结果还没出来的图，先作为 Raw 截图保存到 `screenshots/`。
- Raw 截图可以不填写 `case_id`。
- 只有当信号链完整、失败明确、特别漂亮或特别奇怪时，才升级为 Candidate 案例并录入数据库。

推荐 Raw 路径：

```text
screenshots/BTCUSDT/2026-07-06/BTC_1m_before.png
screenshots/BTCUSDT/2026-07-06/BTC_1m_after.png
```

## 截图内容规则

- 每次至少截图 30m 和 15m。
- 重要案例补充 1H 和 5m。
- 截图必须包含信号出现前 80-150 根 K 线。
- 截图必须包含信号出现后 30-80 根 K 线。
- 尽量保留成交量、MACD、RSI、结构线和背离线。
- 文件名格式：

```text
YYYY-MM-DD_SYMBOL_TIMEFRAME_SIGNAL_RESULT.png
```

示例：

```text
2026-07-05_BTCUSDT_30m_LONG_success.png
```

## Before / After 规则

如果当前只是发现一个问题，例如 1m 加速后不知道会继续跌还是反转，应先保存 before 图，等待后续 30-80 根 K 后再保存 after 图。

示例：

```text
BTC_1m_before.png
BTC_1m_after.png
```

只有 after 图能说明结果时，再考虑录入 `data/case_database.csv`。
