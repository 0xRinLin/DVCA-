# 高周期专项验证分类标准

## 1. 使用原则

- 分类对象是完整案例证据，不是单个标签或单张截图。
- 单个案例只能获得暂定分类；代码问题必须由多个独立案例重复支持。
- 必须先独立判断客观结构，再查看 DVCA 标签和状态。
- 必须区分 pivot 极值位置、pivot 确认时间、Zone 真实可见时间、结构确认时间和执行信号时间。
- 30m/1H 在 v1.5.4 Auto 模式中属于 HTF Context；缺少 LONG/SHORT 本身不自动等于缺陷。
- 无法从截图或数据确认的价格、时间或 K 线数填 `Unknown`/`NA`，不得猜测。

## 2. 合法分类值

数据库 `final_classification` 只允许：

- `PENDING`
- `A_REASONABLE_SPARSE`
- `B_ACCEPTABLE_DELAY`
- `C_MECHANICAL_LAG`
- `D_OVER_FILTERING`
- `E_RANGE_PROTECTION_EFFECTIVE`

`PENDING` 表示证据不足或 Outcome 尚未完成。若一个案例同时体现多种现象，选择主要分类，并在 `suspected_issue` 和人工备注中记录次要现象。

## 3. A：合理稀疏

至少满足：

- 没有在震荡中产生大量误信号；
- 执行信号仍处于可交易阶段；
- 高周期信号可以作为方向或结构确认；
- 15m 或 5m 仍有合理执行机会；
- 延迟主要来自高周期 K 线本身，而非重复确认。

不得仅因信号数量少归入 A；必须证明稀疏没有破坏背景或执行价值。

## 4. B：可接受延迟

至少满足：

- 信号晚于趋势启动；
- 但仍能覆盖趋势中段；
- 止损和盈亏比仍合理；
- 没有明显错过主要行情。

必须记录延迟 K 线数、执行时趋势完成比例和盈亏比人工判断依据。

## 5. C：机制性滞后

可能包括：

- 多个条件串联重复确认同一事实；
- Zone、结构确认、趋势过滤重复等待；
- 执行信号出现时趋势已接近结束；
- 多数样本错过主要价格移动；
- 1H、30m 均无法提供有效背景或执行价值；
- 低周期早已完成结构转折，高周期仍长期保持旧状态。

归入 C 前必须排除正常的高周期收盘等待和 `offset=-pR` 造成的视觉错觉，并需要多个案例支持。

## 6. D：过滤过严

可能包括：

- 明确趋势中长期没有任何主要信号；
- 合理 Zone 被状态过滤持续压制；
- 成交量、趋势、结构条件必须同时达到极端值；
- BTC、ETH、SOL 多个标的重复出现同类漏信号。

必须指出具体受阻环节和跨案例重复证据；不能仅根据代码参数值推断。

## 7. E：震荡保护有效

至少满足：

- RANGE 中没有产生大量错误 LONG 或 SHORT；
- 放宽条件可能明显增加假信号；
- 当前稀疏主要来自必要的震荡过滤。

若 RANGE/TRANSITION 状态本身判断错误，不得归入 E，应保持 `PENDING` 或根据多案例证据归入 C/D。

## 8. 疑似问题值

数据库 `suspected_issue` 允许：

- `UNDETERMINED`
- `NONE`
- `NORMAL_HTF_DELAY`
- `PIVOT_VISUAL_DELAY`
- `OVER_FILTERING`
- `SIGNAL_CHAIN_LAG`
- `HTF_LTF_MISMATCH`
- `RANGE_SUPPRESSION`
- `TRANSITION_SUPPRESSION`
- `ZONE_WITHOUT_EXECUTION`
- `OTHER`

`suspected_issue` 不是代码缺陷结论。`requires_code_change` 在多案例证据和 Outcome 未完成前应保持 `Unknown`。

## 9. 多案例门槛

- 不得根据单个案例确认代码问题。
- 必须覆盖 BTC、ETH、SOL，并分别包含 1H、30m、15m 对照证据。
- 必须覆盖上涨、下跌、震荡、趋势转折、假突破/失败信号等市场类型。
- 汇总结论必须报告每类样本数、中位延迟、最大延迟、Outcome 完成度和证据质量。
- 样本不足时只能记录观察，不允许进入 v1.5.5 代码修改。
