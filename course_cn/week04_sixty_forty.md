<function_calls>
<invoke name="view">
<parameter name="path">C:\Users\hevan\AppData\Local\Temp\tmphzp4lwst.md</parameter>
</invoke>
</function_calls>
<function_response>
# Week 10, Lesson 4: Backtesting a Simple Momentum Strategy

## Overview

In this lesson, we build and backtest a straightforward momentum strategy.

**Host:** Horace
**Format:** Monologue with screen share

---

## Script

**Horace:** Last week, we talked about how momentum works conceptually — assets that have gone up recently tend to keep going up, at least for a while.

Today, let's actually test that idea. We're going to build a simple momentum strategy from scratch and backtest it on historical data.

[VISUAL: Screen share — Python notebook open]

Here's the setup:
- We'll use a universe of large-cap stocks in the S&P 500.
- Every month, we'll rank them by 12-month return (excluding the most recent month — that's standard practice).
- We'll go long the top 20% and short the bottom 20%.
- We'll hold for one month and then rebalance.

Let's write the code.

[CUT TO: Code typing sequence]

```python
import pandas as pd
import numpy as np

# Load monthly return data
returns = pd.read_csv("sp500_monthly_returns.csv", index_col=0, parse_dates=True)

# Rank stocks each month by 12-1 momentum
lookback = 12
skip = 1

momentum_scores = returns.shift(skip).rolling(lookback).sum()

# Long top quintile, short bottom quintile
def get_quintile_portfolio(scores):
    ranked = scores.rank(pct=True)
    long_mask = ranked >= 0.8
    short_mask = ranked <= 0.2
    long_weights = long_mask / long_mask.sum()
    short_weights = short_mask / short_mask.sum()
    return long_weights - short_weights

monthly_weights = momentum_scores.apply(get_quintile_portfolio, axis=1)

# Portfolio returns
portfolio_returns = (monthly_weights.shift(1) * returns).sum(axis=1)
```

[VISUAL: Code appears line by line]

OK, so what did we just do?

We loaded historical monthly returns for S&P 500 stocks. We calculated momentum as the cumulative return over the past 12 months, but we skip the most recent month because short-term reversal is well-documented — the very last month can actually go against you.

Then we sorted stocks into quintiles — top 20% go long, bottom 20% go short.

[ANIMATION: animation/week10_momentum_ranking.py]

Let's look at the results.

```python
cumulative = (1 + portfolio_returns).cumprod()
cumulative.plot(title="Momentum Strategy Cumulative Return")
```

[VISUAL: Equity curve chart appears]

You can see the strategy has a nice upward slope over time — which confirms the momentum premium is real.

But here's where it gets interesting. Let's calculate some performance stats.

```python
sharpe = portfolio_returns.mean() / portfolio_returns.std() * np.sqrt(12)
max_dd = (cumulative / cumulative.cummax() - 1).min()

print(f"Annualized Sharpe Ratio: {sharpe:.2f}")
print(f"Max Drawdown: {max_dd:.2%}")
```

**Horace:** A Sharpe ratio around 0.5 to 0.7 is typical for a simple momentum strategy. And you'll notice the max drawdown can be quite severe — momentum strategies are notorious for sudden crashes. In 2009, after the financial crisis, momentum had one of its worst crashes ever. Stocks that had been going down kept getting shorted, then when the market reversed hard, those shorts got crushed.

[VISUAL: Drawdown chart showing 2009 crash]

This is called a momentum crash, and it's a real risk you need to account for.

A few ways to manage it:
- Volatility scaling: reduce position size when volatility is high
- Crash protection: cut exposure when the broad market is in a downtrend
- Diversification across asset classes, not just equities

[ANIMATION: animation/week10_momentum_crash_overlay.py]

Let's also check what this strategy looks like broken down by sector.

```python
sector_returns = portfolio_returns.groupby(sector_map, axis=1).sum()
sector_returns.cumplot()
```

**Horace:** You'll often find that momentum tends to concentrate in a few hot sectors — tech, energy, consumer discretionary — depending on the market environment. That's actually one of the critiques of momentum: it can become very sector-concentrated.

[VISUAL: Sector breakdown bar chart]

One more thing I want to show you — transaction costs.

```python
turnover = monthly_weights.diff().abs().sum(axis=1)
cost_per_trade = 0.001  # 10 bps per side
transaction_costs = turnover * cost_per_trade
net_returns = portfolio_returns - transaction_costs

net_sharpe = net_returns.mean() / net_returns.std() * np.sqrt(12)
print(f"Net Sharpe after costs: {net_sharpe:.2f}")
```

**Horace:** Momentum strategies have high turnover — you're replacing 20% of your portfolio every month. That adds up. After realistic transaction costs, your Sharpe ratio might drop from 0.6 to 0.4. Still positive, but not as impressive. And for smaller accounts, slippage makes this worse.

[VISUAL: Table comparing gross vs net performance]

So what's the takeaway here?

Momentum works. The academic evidence is solid — it's been documented across asset classes, time periods, and geographies. But it's not easy to harvest:
- It crashes at the worst times
- Transaction costs eat into returns
- Concentration risk is real

This is why most practitioners combine momentum with other factors — value, quality, low volatility — to build a more robust portfolio.

[ANIMATION: animation/week10_multi_factor_combination.py]

Next week, we'll look at how to combine momentum with a value factor to smooth out some of these rough edges.

---

## Key Concepts

- **12-1 momentum**: 12-month lookback, skip most recent month
- **Quintile portfolio**: Long top 20%, short bottom 20%
- **Momentum crash**: Sharp reversal that hurts momentum strategies
- **Transaction costs**: High turnover reduces net returns
- **Factor combination**: Combining momentum with value improves stability

---

## Visuals Needed

| Timestamp | Visual |
|-----------|--------|
| 0:30 | Python notebook setup |
| 2:00 | Momentum ranking animation |
| 4:00 | Equity curve chart |
| 6:00 | Drawdown chart — 2009 crash |
| 8:00 | Sector breakdown bar chart |
| 10:00 | Gross vs net performance table |

</parameter>
</invoke>
</function_calls>

# 第10周，第4课：回测一个简单的动量策略

## 概述

本课中，我们将构建并回测一个简单的动量策略。

**主持人：** 陳馬
**形式：** 独白配屏幕共享

---

## 脚本

**陳馬：** 上周，我们从概念上讨论了动量是如何运作的——近期上涨的资产往往会继续上涨，至少在一段时间内如此。

今天，我们就来实际验证这个想法。我们将从零开始构建一个简单的动量策略，并用历史数据对其进行回测。

[VISUAL: Screen share — Python notebook open]

这是我们的设置：
- 我们将使用标普500中大盘股的股票池。
- 每个月，我们按12个月的收益对它们进行排名（排除最近一个月——这是标准做法）。
- 我们做多排名前20%的股票，做空排名后20%的股票。
- 持有一个月后再平衡。

下面来写代码。

[CUT TO: Code typing sequence]

```python
import pandas as pd
import numpy as np

# 加载月度收益数据
returns = pd.read_csv("sp500_monthly_returns.csv", index_col=0, parse_dates=True)

# 每月按12-1动量对股票排名
lookback = 12
skip = 1

momentum_scores = returns.shift(skip).rolling(lookback).sum()

# 做多最高五分位，做空最低五分位
def get_quintile_portfolio(scores):
    ranked = scores.rank(pct=True)
    long_mask = ranked >= 0.8
    short_mask = ranked <= 0.2
    long_weights = long_mask / long_mask.sum()
    short_weights = short_mask / short_mask.sum()
    return long_weights - short_weights

monthly_weights = momentum_scores.apply(get_quintile_portfolio, axis=1)

# 投资组合收益
portfolio_returns = (monthly_weights.shift(1) * returns).sum(axis=1)
```

[VISUAL: Code appears line by line]

好，我们刚才做了什么？

我们加载了标普500股票的历史月度收益数据。我们将动量定义为过去12个月的累计收益，但跳过了最近一个月——因为短期反转效应有充分的文献记录，最后那个月实际上可能对你不利。

然后我们将股票分成五分位——排名前20%做多头头寸，排名后20%做空头头寸。

[ANIMATION: animation/week10_momentum_ranking.py]

来看看结果。

```python
cumulative = (1 + portfolio_returns).cumprod()
cumulative.plot(title="动量策略累计收益")
```

[VISUAL: Equity curve chart appears]

可以看到该策略随时间呈现出良好的上升趋势——这证实了动量溢价确实存在。

但有趣的地方来了。我们来计算一些绩效统计数据。

```python
sharpe = portfolio_returns.mean() / portfolio_returns.std() * np.sqrt(12)
max_dd = (cumulative / cumulative.cummax() - 1).min()

print(f"年化夏普比率: {sharpe:.2f}")
print(f"最大回撤: {max_dd:.2%}")
```

**陳馬：** 对于一个简单的动量策略，夏普比率在0.5到0.7之间是比较典型的。你还会注意到最大回撤可能相当严重——动量策略以突然崩溃而著称。2009年金融危机后，动量经历了有史以来最惨烈的崩溃之一。持续下跌的股票被不断做空，而当市场急剧反转时，这些空头头寸就被打爆了。

[VISUAL: Drawdown chart showing 2009 crash]

这就是所谓的动量崩溃，是你必须认真对待的真实风险。

几种管理方法：
- 波动性缩放：当波动性较高时缩减仓位规模
- 崩溃保护：当大盘处于下跌趋势时削减敞口
- 跨资产类别进行分散投资，而不仅限于股票

[ANIMATION: animation/week10_momentum_crash_overlay.py]

我们再来看看这个策略按板块分解的情况。

```python
sector_returns = portfolio_returns.groupby(sector_map, axis=1).sum()
sector_returns.cumplot()
```

**陳馬：** 你会经常发现，动量往往集中在少数热门板块中——科技、能源、非必需消费品——具体取决于市场环境。这实际上也是对动量的一个批评：它可能造成非常高的板块集中度。

[VISUAL: Sector breakdown bar chart]

还有一件事我想展示给大家看——交易成本。

```python
turnover = monthly_weights.diff().abs().sum(axis=1)
cost_per_trade = 0.001  # 每边10个基点
transaction_costs = turnover * cost_per_trade
net_returns = portfolio_returns - transaction_costs

net_sharpe = net_returns.mean() / net_returns.std() * np.sqrt(12)
print(f"扣除成本后的净夏普比率: {net_sharpe:.2f}")
```

**陳馬：** 动量策略的换手率很高——每个月要替换20%的投资组合。这会积少成多。扣除合理的交易成本后，你的夏普比率可能从0.6降至0.4。虽然仍然为正，但就没那么亮眼了。对于规模较小的账户，滑点会让情况更糟。

[VISUAL: Table comparing gross vs net performance]

那么，我们得出什么结论？

动量是有效的。学术证据非常充分——它已经在多种资产类别、不同时间段和不同地域中得到验证。但要从中获益并不容易：
- 它往往在最糟糕的时候崩溃
- 交易成本侵蚀收益
- 集中度风险是真实存在的

这就是为什么大多数从业者会将动量与其他因子结合——价值、质量、低波动性——来构建更稳健的投资组合。

[ANIMATION: animation/week10_multi_factor_combination.py]

下周，我们将探讨如何将动量与价值因子结合，以平滑掉一些粗糙的棱角。

---

## 核心概念

- **12-1动量**：12个月回望期，跳过最近一个月
- **五分位投资组合**：做多前20%，做空后20%
- **动量崩溃**：急剧反转对动量策略造成重创
- **交易成本**：高换手率降低净收益
- **因子组合**：将动量与价值结合可提升稳健性

---

## 所需视觉素材

| 时间戳 | 视觉素材 |
|--------|----------|
| 0:30 | Python笔记本设置 |
| 2:00 | 动量排名动画 |
| 4:00 | 净值曲线图 |
| 6:00 | 回撤图——2009年崩溃 |
| 8:00 | 板块分解柱状图 |
| 10:00 | 毛收益与净收益对比表 |