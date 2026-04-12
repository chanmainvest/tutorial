<!-- 此文件需要翻译为简体中文 -->
<!-- This file needs translation to Simplified Chinese -->

# Week 46: Backtesting and Strategy Validation

---

## Reading Section

### a) Why This Is Important

Backtesting -- the process of testing an investment strategy on historical data to see how it would have performed -- is perhaps the most dangerous tool in the investor's toolkit. It is dangerous not because it is useless, but because it is seductive. A well-constructed backtest can make you rich. A poorly constructed one will make you confident while losing money, which is worse than losing money while knowing you are gambling.

The financial industry runs on backtests. Every new ETF, every factor strategy, every quantitative hedge fund, every robo-advisor algorithm was backtested before launch. The problem is that backtests are subject to a devastating array of biases, each of which makes historical performance look better than reality. Understanding these biases is essential because:

- **Backtests almost always overstate future performance**: Empirical research consistently finds that strategies perform 30-70% worse in live trading than in backtests. This is not a small discrepancy -- it is the difference between a strategy that "generates 15% returns" and one that actually generates 5-8%. The gap comes from biases that are easy to overlook and hard to correct.

- **Lookahead bias can make any strategy look brilliant**: If your backtest accidentally uses information that was not available at the time of the trade -- future earnings, data revisions, index membership changes -- it will show artificially superior returns. Lookahead bias is insidious because it often hides in data sources you trust. Companies report financial data with delays, databases get corrected retroactively, and index compositions change. Any of these can contaminate a backtest.

- **Survivorship bias inflates returns by excluding failures**: If your universe of securities includes only companies that survived to the present, you are excluding the bankruptcies, delistings, and mergers that a real investor would have experienced. This bias can add 1-3% per year to backtested returns. A strategy that appears to return 12% annually may truly return 9-10%.

- **Overfitting is the single most common cause of backtest failure**: Adding parameters, optimizing cutoff points, and fine-tuning entry/exit rules to maximize historical performance creates a model that is perfectly adapted to the past and useless for the future. A strategy with 20 optimized parameters fitted to 15 years of data has memorized historical noise, not discovered a persistent edge.

- **Transaction costs can eliminate an entire edge**: Many backtested strategies show attractive returns before costs but generate returns below a simple index fund after accounting for spreads, slippage, market impact, and commissions. Transaction cost modeling is the single most important -- and most frequently botched -- component of backtesting.

- **Walk-forward analysis is the gold standard for validation**: Simply splitting data into "training" and "testing" sets helps but is insufficient. Walk-forward analysis -- where you repeatedly train on a rolling window and test on the subsequent period -- mimics the experience of a live trader who must make decisions with only past data available. It is the closest a backtest can come to simulating reality.

This lesson will teach you how to build, evaluate, and criticize backtests so you can distinguish genuine edges from statistical mirages.

---

### b) What You Need to Know

#### 1. The Backtesting Framework

A backtest simulates what would have happened if you had followed a specific strategy in the past. The framework has several essential components.

```
BACKTESTING FRAMEWORK: CORE COMPONENTS

┌────────────────────────────────────────────────┐
│                                                │
│  1. STRATEGY DEFINITION                        │
│     - Entry rules (when to buy)                │
│     - Exit rules (when to sell)                │
│     - Position sizing (how much)               │
│     - Universe selection (which securities)     │
│     - Rebalancing frequency (how often)        │
│                                                │
│  2. DATA                                       │
│     - Price data (adjusted for splits/divs)    │
│     - Fundamental data (point-in-time)         │
│     - Universe data (index membership history) │
│     - Transaction cost estimates               │
│                                                │
│  3. EXECUTION SIMULATION                       │
│     - Order placement timing                   │
│     - Fill assumptions (what price?)           │
│     - Slippage model                           │
│     - Capacity constraints                     │
│                                                │
│  4. PERFORMANCE MEASUREMENT                    │
│     - Returns (total, excess, risk-adjusted)   │
│     - Drawdowns (max, duration, recovery)      │
│     - Turnover (trading frequency)             │
│     - Net-of-cost returns                      │
│                                                │
│  5. VALIDATION                                 │
│     - In-sample vs. out-of-sample              │
│     - Walk-forward analysis                    │
│     - Monte Carlo simulation                   │
│     - Sensitivity analysis                     │
│                                                │
└────────────────────────────────────────────────┘

TIMELINE OF A BACKTEST:

  Data Available
  ├──────────────────────────────────────────┤
  │  In-Sample (Training)  │  Out-of-Sample │
  │  2000 ──────── 2015    │  2015 ── 2025  │
  │                        │                │
  │  Develop and optimize  │  Test ONCE.    │
  │  strategy here.        │  No peeking.   │
  │  Iterate as needed.    │  No re-doing.  │
  └────────────────────────┴────────────────┘

  CRITICAL RULE: Once you look at out-of-sample
  results, that data is "used." You cannot go
  back, adjust your strategy, and re-test on
  the same out-of-sample period. That turns it
  into in-sample data.
```

```
BACKTESTING EXAMPLE: SIMPLE MOMENTUM STRATEGY

STRATEGY DEFINITION:
  Universe: S&P 500 stocks
  Signal: 12-month total return (momentum)
  Rule: Each month, buy the top 50 stocks by
        12-month return. Equal weight.
        Sell any holding that drops out of top 50.
  
STEP-BY-STEP BACKTEST (ONE MONTH):

  Date: January 31, 2015
  
  Step 1: Look up S&P 500 members AS OF Jan 2015
          (NOT current members -- this prevents
          survivorship bias)
  
  Step 2: For each member, calculate 12-month
          total return (Feb 2014 - Jan 2015)
          Using data available ON Jan 31, 2015
          (no future data)
  
  Step 3: Rank all stocks by 12-month return
  
  Step 4: Select top 50
  
  Step 5: Compare to current holdings from
          December 2014
  
  Step 6: Calculate trades needed:
          - Sell stocks that dropped out of top 50
          - Buy stocks that entered top 50
          - Rebalance to equal weight
  
  Step 7: Apply transaction costs:
          - Spread cost: 0.05% per trade
          - Market impact: 0.10% per trade
          - Total: 0.15% per trade
  
  Step 8: Calculate portfolio return for Feb 2015:
          Sum of (weight * return) for all 50 stocks
          Minus transaction costs on trades executed
  
  Step 9: Record portfolio value, return, turnover
  
  Step 10: Repeat for next month (Feb 28, 2015)

  Repeat Step 1-10 for every month in the
  backtest period. Aggregate into performance
  statistics.

MONTHLY TURNOVER CALCULATION:
  If 8 stocks dropped out and 8 new stocks entered:
  Turnover = 8/50 = 16% monthly
  Annual turnover = 16% * 12 = 192%
  
  With 0.15% cost per trade (buy + sell = 2 trades):
  Annual cost = 192% * 2 * 0.15% = 0.576%
  
  This is SIGNIFICANT. A strategy returning 12%
  gross returns only 11.4% net. If the benchmark
  returns 10%, the net alpha is only 1.4%, and
  much of that may be noise.
```

#### 2. Lookahead Bias

Lookahead bias occurs when a backtest uses information that was not available at the time of the simulated trade. It is the most insidious bias because it can hide in perfectly reasonable-looking data.

```
LOOKAHEAD BIAS: SOURCES AND EXAMPLES

SOURCE 1: FINANCIAL DATA REVISIONS

  GDP is initially reported as "advance estimate,"
  then revised in "second estimate" and "third estimate."

  Advance GDP (reported Jan 30): +2.5%
  Second estimate (Feb 28):      +2.8%
  Third estimate (Mar 30):       +2.2%

  If your backtest uses the FINAL GDP figure on
  Jan 30 (the date of the advance release), you
  are using data that was not available until
  March 30. This is lookahead bias.

  CORRECT: Use real-time (vintage) data -- the
  number that was actually available on each date.

SOURCE 2: EARNINGS REPORTING DELAYS

  Company reports Q4 earnings on February 15.
  Many databases assign Q4 data to December 31.
  
  If your backtest uses Q4 earnings to make a
  trade on January 2, you are trading on data
  that will not exist for 6 weeks.

  ┌──────────────────────────────────────────────┐
  │  TIMELINE:                                   │
  │                                              │
  │  Dec 31          Jan 2           Feb 15      │
  │  (fiscal Q4      (your trade)   (earnings    │
  │   end date)                      reported)   │
  │                                              │
  │  Database says: Q4 EPS = $2.50 on Dec 31    │
  │  Reality: $2.50 was NOT known until Feb 15  │
  │                                              │
  │  Your backtest bought on Jan 2 using         │
  │  earnings that would not be reported for     │
  │  6 more weeks. LOOKAHEAD BIAS.               │
  └──────────────────────────────────────────────┘

  CORRECT: Use a lag of 60-90 days after fiscal
  quarter end before using fundamental data.
  Or use a point-in-time database that records
  exactly when each data point became available.

SOURCE 3: INDEX MEMBERSHIP CHANGES

  Tesla was added to the S&P 500 on Dec 21, 2020.
  If your backtest of "S&P 500 stocks" in 2019
  includes Tesla, you have lookahead bias.
  Tesla was NOT in the S&P 500 in 2019.

  CORRECT: Use historical index constituent
  lists. The S&P 500 of 2019 included different
  companies than the S&P 500 of 2024.

SOURCE 4: PRICE ADJUSTMENTS

  Stock split 4:1 on August 1, 2020.
  Pre-split price: $400. Post-split: $100.
  Databases retroactively adjust all pre-split
  prices by dividing by 4.

  If your backtest uses a $50 stop-loss on a
  pre-split price of $100 (adjusted), the ACTUAL
  price the investor saw was $400. A $50 stop
  would not have been triggered on the real $400.

  CORRECT: Be aware of split-adjusted vs. actual
  prices. Use split-adjusted for return calculations,
  actual prices for order-level simulation.

SOURCE 5: DIVIDEND ADJUSTMENTS

  Total return data includes dividends reinvested.
  But dividends are not known in advance.
  Special dividends, dividend cuts, and ex-dates
  are forward-looking information.

  CORRECT: Use dividend data only AFTER the
  ex-dividend date, which is when the market
  price adjusts.
```

#### 3. Survivorship Bias in Backtesting

```
SURVIVORSHIP BIAS: THE SILENT RETURN INFLATOR

WHAT IT IS:
  Your backtest universe includes only securities
  that survived to the present. Dead companies --
  bankruptcies, delistings, acquisitions at low
  prices -- are excluded.

MAGNITUDE OF THE BIAS:

  Asset Class       Estimated Annual Bias
  ──────────────────────────────────────────
  US large-cap stocks     0.5 - 1.0%
  US small-cap stocks     1.0 - 3.0%
  International stocks    1.0 - 2.0%
  Mutual funds            1.0 - 2.0%
  Hedge funds             3.0 - 5.0%
  Venture capital         5.0 - 10.0%

EXAMPLE: SMALL-CAP VALUE STRATEGY

  You backtest a small-cap value strategy from
  2000 to 2020 using a CURRENT database of stocks.

  What you INCLUDE:
  - All companies that exist today and were
    small and cheap at some point during 2000-2020
  - Companies that survived and thrived

  What you EXCLUDE:
  - Companies that went bankrupt (return = -100%)
  - Companies that were delisted for fraud
  - Companies acquired at distressed prices
  - Companies that merged and ceased to exist

  THE SURVIVORS were small and cheap AND recovered.
  THE FAILURES were small and cheap AND died.

  Your backtest only sees the recoveries, not
  the deaths. Result: backtested return is
  artificially high.

  ┌──────────────────────────────────────────────┐
  │  BACKTEST WITH SURVIVORSHIP BIAS:            │
  │                                              │
  │  Small-cap value return: 14.2% per year      │
  │  Looks great! Beats the market by 4%.        │
  │                                              │
  │  BACKTEST WITHOUT SURVIVORSHIP BIAS:         │
  │                                              │
  │  Small-cap value return: 11.8% per year      │
  │  Still good, but 2.4% less impressive.       │
  │  The excess return is 1.6%, not 4%.          │
  │  After transaction costs: maybe 0.5%.        │
  │  Barely worth the effort.                    │
  └──────────────────────────────────────────────┘

HOW TO FIX SURVIVORSHIP BIAS:
  1. Use a survivorship-bias-free database
     (CRSP, Compustat with delisting returns)
  2. Include delisting returns (what happened
     when the stock was removed)
  3. Use historical index constituents, not
     current constituents
  4. Track what happened to stocks that left
     the universe
```

#### 4. Overfitting

Overfitting is the process of creating a model so tightly fitted to historical data that it captures noise rather than signal. It is the most common cause of backtest failure.

```
OVERFITTING: HOW TO RECOGNIZE AND AVOID IT

THE FUNDAMENTAL PROBLEM:

  Historical data = Signal + Noise

  Signal: Persistent, exploitable patterns
  Noise: Random fluctuations specific to that period

  A simple model captures mostly signal.
  A complex model captures signal AND noise.

  ┌──────────────────────────────────────────────┐
  │  NUMBER OF PARAMETERS vs. PERFORMANCE        │
  │                                              │
  │  In-Sample                                   │
  │  Performance    *                             │
  │      |       *  *  *  *  *  *  *  *          │
  │      |     *                                  │
  │      |   *                                    │
  │      | *                                      │
  │      |*                                       │
  │      └────────────────────────────────────    │
  │      1   3   5   7   9  11  13  15  17       │
  │              Number of Parameters             │
  │                                              │
  │  Out-of-Sample                               │
  │  Performance                                  │
  │      |   *  *                                 │
  │      | *      *  *                            │
  │      |*          *                            │
  │      |              *                         │
  │      |                *                       │
  │      |                  *  *  *  *  *         │
  │      └────────────────────────────────────    │
  │      1   3   5   7   9  11  13  15  17       │
  │              Number of Parameters             │
  │                                              │
  │  SWEET SPOT: 3-5 parameters for most         │
  │  financial models. Beyond that, you are       │
  │  fitting noise.                               │
  └──────────────────────────────────────────────┘

SIGNS OF OVERFITTING:

  1. Strategy has many rules and parameters
     "Buy when RSI < 30 AND MACD crosses above
     signal AND volume is 1.5x average AND
     it is a Tuesday AND price is above 200-day
     MA but below 50-day MA AND..."
     
     Every additional condition was likely added
     to improve historical performance. Each one
     reduces future reliability.

  2. Performance is dramatically better in-sample
     than out-of-sample.
     
     In-sample Sharpe: 2.5
     Out-of-sample Sharpe: 0.3
     
     This is textbook overfitting.

  3. Strategy works only in a specific time period
     or market regime.
     
     "Works great 2010-2020 but not 2000-2010."
     The model fit the regime-specific features
     of 2010-2020, not universal market dynamics.

  4. Small changes in parameters cause large
     changes in results.
     
     Lookback of 11 months: Sharpe 1.8
     Lookback of 12 months: Sharpe 0.4
     Lookback of 13 months: Sharpe 1.5
     
     A genuine effect should be robust to small
     parameter changes. Sharp sensitivity to
     parameters indicates overfitting.

  5. Strategy requires precise timing.
     
     "Rebalance on the 3rd Wednesday of each
     month at 2:47 PM for best results."
     
     A genuine edge should not depend on the
     specific minute you trade.

HOW TO PREVENT OVERFITTING:

  RULE 1: Fewer parameters is better.
    Minimum observations per parameter: 50:1
    60 months of data -> max 1 parameter
    300 months of data -> max 6 parameters

  RULE 2: Every parameter needs economic justification.
    WHY is a 12-month lookback better than 6 or 18?
    If you cannot explain it, you found noise.

  RULE 3: Test parameter stability.
    If the optimal parameter is 12, the strategy
    should also work well with 10 or 14.
    Plot performance vs. parameter value.
    It should be a smooth curve, not spiky.

  RULE 4: Use regularization.
    Penalize model complexity mathematically.
    AIC, BIC, LASSO, Ridge regression.
    These techniques automatically balance fit
    against complexity.

  RULE 5: Cross-validate.
    Do not rely on a single train/test split.
    Use k-fold cross-validation or walk-forward
    analysis (see below).
```

#### 5. In-Sample vs. Out-of-Sample Testing

```
IN-SAMPLE vs. OUT-OF-SAMPLE

IN-SAMPLE (training):
  The data used to develop and optimize the strategy.
  Performance on this data is UNRELIABLE because
  the strategy was designed to fit it.

OUT-OF-SAMPLE (testing):
  Data the strategy has NEVER seen.
  Performance on this data is the best estimate
  of future performance.

THE SIMPLE SPLIT:

  ┌───────────────────────────┬────────────────┐
  │   IN-SAMPLE (70%)        │   OOS (30%)    │
  │   2000 ──────── 2017     │  2017 ── 2025  │
  │                          │                │
  │   Develop strategy.      │  Test once.    │
  │   Optimize parameters.   │  Report this.  │
  └──────────────────────────┴────────────────┘

PROBLEMS WITH A SIMPLE SPLIT:

  1. One test is not enough. Your out-of-sample
     period could be unusual (e.g., all bull market
     or dominated by COVID crash).

  2. You might unconsciously peek. If you look at
     out-of-sample results, go back and "improve"
     the strategy, then re-test, you have turned
     out-of-sample into in-sample.

  3. Sample period selection can be gamed. Choosing
     where to split can itself introduce bias.

EXPECTED PERFORMANCE DECAY:

  ┌──────────────────────────────────────────────┐
  │  TYPICAL PERFORMANCE DEGRADATION             │
  │                                              │
  │  In-sample Sharpe ratio:        2.0          │
  │  Out-of-sample Sharpe ratio:    1.0 - 1.3   │
  │  Live trading Sharpe ratio:     0.5 - 0.8   │
  │                                              │
  │  RULE OF THUMB:                              │
  │  Expect live performance to be 30-60% worse  │
  │  than in-sample performance.                 │
  │                                              │
  │  If in-sample Sharpe < 1.5, the strategy     │
  │  is unlikely to survive live trading.        │
  └──────────────────────────────────────────────┘
```

#### 6. Walk-Forward Analysis

Walk-forward analysis is the gold standard for backtesting validation. It simulates how a strategy would be managed in real time.

```
WALK-FORWARD ANALYSIS

CONCEPT:
  Instead of one train/test split, perform MANY
  splits that roll forward through time.

  ┌──────────────────────────────────────────────┐
  │                                              │
  │  Period 1:                                   │
  │  Train: 2000-2004 | Test: 2005              │
  │  ████████████████ | ████                     │
  │                                              │
  │  Period 2:                                   │
  │  Train: 2001-2005 | Test: 2006              │
  │    ████████████████ | ████                   │
  │                                              │
  │  Period 3:                                   │
  │  Train: 2002-2006 | Test: 2007              │
  │      ████████████████ | ████                 │
  │                                              │
  │  Period 4:                                   │
  │  Train: 2003-2007 | Test: 2008              │
  │        ████████████████ | ████               │
  │                                              │
  │  ...continue through all available data...   │
  │                                              │
  │  Period 16:                                  │
  │  Train: 2015-2019 | Test: 2020              │
  │                      ████████████████ | ████ │
  │                                              │
  └──────────────────────────────────────────────┘

  At each period:
  1. Optimize strategy on training window
  2. Apply (without changes) to test window
  3. Record test window performance

  The AGGREGATE performance across all test
  windows is the walk-forward estimate of
  strategy quality.

ADVANTAGES:
  + Simulates live trading experience
  + Multiple out-of-sample tests, not just one
  + Strategy adapts to changing markets
  + Exposes regime-dependent strategies
  + Most realistic estimate of future performance

DISADVANTAGES:
  - Requires more data (need enough for many periods)
  - Computationally intensive (many optimizations)
  - Results depend on window length choices
  - Cannot fully prevent overfitting if you iterate
    on the walk-forward results themselves

WALK-FORWARD RESULTS INTERPRETATION:

  If walk-forward Sharpe > 0.5 consistently
  across all test periods: Potentially viable.

  If walk-forward Sharpe varies wildly between
  test periods: Strategy is regime-dependent.
  Proceed with extreme caution.

  If walk-forward Sharpe is negative in several
  periods: Strategy does not generalize. Reject.

  Walk-Forward          In-Sample     Assessment
  Sharpe                Sharpe
  ──────────────────────────────────────────────
  > 0.8                 > 1.5         Strong
  0.5 - 0.8             > 1.5         Moderate
  0.3 - 0.5             > 1.5         Weak
  < 0.3                 > 1.5         Overfit
  ~0 or negative        > 1.5         Pure noise
```

#### 7. Transaction Costs in Backtests

Transaction costs are frequently underestimated or omitted in backtests. Realistic cost modeling is the difference between a strategy that works on paper and one that works with real money.

```
TRANSACTION COSTS: THE STRATEGY KILLER

COMPONENTS OF TRANSACTION COST:

  1. SPREAD COST
     You buy at the ask, sell at the bid.
     Cost = half-spread per trade.
     
     Liquid large-cap: 0.01-0.03%
     Mid-cap: 0.05-0.15%
     Small-cap: 0.15-0.50%
     Micro-cap: 0.50-2.00%

  2. MARKET IMPACT
     Your trade moves the price against you.
     Depends on order size relative to volume.
     
     Small order (< 1% of daily volume): 0.05%
     Medium order (1-5% of volume): 0.10-0.30%
     Large order (> 5% of volume): 0.30-1.00%+

  3. SLIPPAGE
     Difference between intended price and actual fill.
     Caused by price movement during execution.
     
     Typical: 0.02-0.10%

  4. OPPORTUNITY COST
     Unfilled orders. Your limit order did not execute,
     and the stock moved away from you.
     Hard to model but real.

IMPACT ON DIFFERENT STRATEGIES:

  Strategy          Annual     Cost per   Net     Is It
                    Turnover   Trade      Annual  Worth
                    (%)        (%)        Cost    It?
  ──────────────────────────────────────────────────────
  Buy-and-hold      5%         0.10%      0.01%  Yes
  Annual rebalance  25%        0.10%      0.05%  Yes
  Quarterly factor  100%       0.15%      0.30%  Maybe
  Monthly momentum  200%       0.15%      0.60%  Risky
  Weekly mean rev.  500%       0.20%      2.00%  Unlikely
  Daily trading     2000%      0.10%      4.00%  HFT only
  Intraday scalp    5000%+     0.05%      5.00%+ No

EXAMPLE: TRANSACTION COSTS DESTROY ALPHA

  Strategy: Monthly momentum (top decile stocks)
  
  Gross return:  15.0% per year
  Benchmark:     10.0% per year
  Gross alpha:   5.0% per year
  
  Transaction costs:
  - Annual turnover: 200%
  - Cost per trade: 0.15% (spread + impact)
  - One-way trades: 200% * 2 = 400% of portfolio
  - Total cost: 400% * 0.15% = 0.60%
  
  Wait, that does not seem too bad. But let us
  use more realistic costs for the smaller stocks
  that momentum strategies tend to buy:
  
  - Cost per trade: 0.30% (small/mid-cap impact)
  - Total cost: 400% * 0.30% = 1.20%
  
  Hmm. Now add slippage:
  - Slippage: 0.10% per trade
  - Total: 400% * (0.30% + 0.10%) = 1.60%
  
  Net alpha: 5.0% - 1.60% = 3.40%
  
  But wait -- this assumes no capacity constraints.
  With $100M in the strategy, market impact doubles:
  - Total cost: 400% * 0.50% = 2.00%
  
  Net alpha: 5.0% - 2.00% = 3.00%
  
  And after management fees (1%) and performance
  fees (20% of alpha):
  - Fees: 1% + 20% * 3% = 1.60%
  - Investor net alpha: 3.00% - 1.60% = 1.40%
  
  From 5% gross alpha to 1.4% investor alpha.
  And we have not even discussed the risk that
  the gross alpha is overestimated due to other
  biases.

  ┌──────────────────────────────────────────────┐
  │  THE WATERFALL OF ALPHA DECAY:               │
  │                                              │
  │  Backtested alpha:         5.0%              │
  │  After survivorship bias:  4.2%              │
  │  After lookahead bias:     3.8%              │
  │  After transaction costs:  2.2%              │
  │  After slippage:           1.8%              │
  │  After management fees:    0.8%              │
  │  After performance fees:   0.5%              │
  │  After implementation:     0.2%              │
  │                                              │
  │  5% became 0.2%. And 0.2% is within the     │
  │  noise of random chance.                     │
  └──────────────────────────────────────────────┘
```

#### 8. When to Trust a Backtest

```
WHEN TO TRUST (AND DISTRUST) A BACKTEST

TRUST A BACKTEST WHEN:

  ✓ It has an economic rationale
    WHY does this edge exist? WHO loses?
    "Value works because investors overpay for
    growth" -- clear rationale, identifiable
    behavioral bias.

  ✓ It uses few parameters
    A strategy with 1-3 parameters fitted on
    20+ years of data is less likely overfit.

  ✓ It survives walk-forward analysis
    Consistent performance across many test
    periods, not just one favorable window.

  ✓ It survives realistic transaction costs
    Returns are still attractive after spreads,
    impact, slippage, and fees.

  ✓ It works in multiple markets and time periods
    US and international. Pre-2000 and post-2000.
    Emerging and developed markets.

  ✓ It has been documented by independent researchers
    Academic papers, replicated by others.
    Not just the fund manager's internal research.

  ✓ The in-sample to out-of-sample decay is modest
    In-sample Sharpe 1.5, out-of-sample Sharpe 1.0
    is encouraging. In-sample 3.0, OOS 0.5 is not.

DISTRUST A BACKTEST WHEN:

  ✗ No economic rationale
    "We found that this works" without explaining
    WHY it should work or persist.

  ✗ Many parameters and rules
    "Buy when A AND B AND NOT C AND D > 2.5 AND..."
    More rules = more overfitting risk.

  ✗ Only tested on one period in one market
    US stocks 2010-2020. A ten-year bull market.
    How did it do in 2000-2002 or 2008?

  ✗ Transaction costs are ignored or unrealistic
    "Assuming zero transaction costs" or
    "0.01% per trade" for a small-cap strategy.

  ✗ Returns are too good
    Any strategy showing > 25% annual returns
    with low volatility should be presumed overfit
    until proven otherwise. The world's best
    investors earn 15-20%.

  ✗ Excessive curve-fitting of parameters
    "The optimal lookback is exactly 11.5 months."
    Real effects are robust to parameter choice.

  ✗ Data starts from an arbitrary, convenient date
    "Starting from March 2009..." (the market
    bottom). Convenient start dates inflate returns.

BACKTEST EVALUATION SCORECARD:

  Criterion                    Points (0-2)
  ──────────────────────────────────────────
  Economic rationale             /2
  Simplicity (< 5 params)       /2
  Walk-forward positive          /2
  Realistic costs deducted       /2
  Multiple markets tested        /2
  Independent replication        /2
  Modest in-to-OOS decay         /2
  20+ year sample period         /2
  Survivorship bias free         /2
  No lookahead bias              /2
  ──────────────────────────────────────────
  Total                          /20

  16-20: High confidence
  12-15: Moderate confidence, proceed with caution
  8-11:  Low confidence, probably overfit
  0-7:   Reject -- likely noise
```

---

### c) Common Misconceptions

**Misconception 1: "If a backtest shows good returns, the strategy works."**

Backtested returns are the UPPER BOUND of what a strategy can deliver. Every bias -- survivorship, lookahead, overfitting, understated costs -- works in the direction of inflating backtested performance. A strategy that shows 12% backtested returns may deliver 6-8% in live trading. A strategy that shows 6-8% backtested returns may deliver less than a passive index fund after all biases and costs are properly accounted for. The default assumption should be that a backtest is overstated until proven otherwise.

**Misconception 2: "I split my data into training and testing, so I am protected from overfitting."**

A single train-test split is better than nothing but far from sufficient. The test period may be unrepresentative (e.g., entirely within a bull market). You may unconsciously peek at the test results and adjust your strategy. And the specific split point can itself be optimized -- you may choose the split that gives the best test results. Walk-forward analysis with many rolling windows is a much stronger test. Even so, if you iterate on the walk-forward results themselves, you are overfitting to the walk-forward process.

**Misconception 3: "Zero-commission brokers mean transaction costs are negligible."**

Commission is a small fraction of total transaction cost. The spread, market impact, slippage, and opportunity cost of unfilled orders typically dwarf commissions. A strategy with 200% annual turnover trading mid-cap stocks faces 1-2% annual transaction costs even with zero commissions. For small-cap and micro-cap stocks, costs can be 3-5% or more. The shift to zero commissions has made it cheaper to execute individual trades but has NOT eliminated the core costs that destroy high-turnover strategies.

**Misconception 4: "More data always makes a backtest more reliable."**

Using 50 years of data sounds rigorous, but market structure has changed dramatically over that period. Decimalization (2001), the rise of electronic trading, the growth of passive investing, and changes in regulation have fundamentally altered market behavior. A strategy that worked from 1970-2000 may not work in the post-2000 electronic market. The right amount of data balances statistical power against regime relevance. For most strategies, 15-25 years of data -- covering multiple market cycles in a relatively consistent structural regime -- is the sweet spot.

**Misconception 5: "If a strategy has a high Sharpe ratio in the backtest, it will have a high Sharpe ratio live."**

Backtested Sharpe ratios almost always overstate live performance. The typical decay is 40-60%. A backtested Sharpe of 2.0 typically delivers a live Sharpe of 0.8-1.2. This means a backtested Sharpe below 1.5 is unlikely to deliver a live Sharpe above 0.5, which is borderline for practical use. Any backtested Sharpe above 3.0 should be viewed with extreme suspicion -- it almost certainly reflects overfitting, data errors, or unrealistic assumptions.

**Misconception 6: "Walk-forward analysis proves a strategy works."**

Walk-forward analysis is the best validation tool available, but it is not proof. A strategy can pass walk-forward analysis and still fail in live trading if market conditions change, if the strategy's edge gets arbitraged away by other participants who discover the same signal, or if the walk-forward process itself was iterated upon (making the walk-forward results effectively in-sample). Walk-forward analysis reduces confidence in bad strategies but does not guarantee confidence in strategies that pass.

---

### d) Common Questions and Answers

**Q1: What is the minimum amount of data I need for a reliable backtest?**

A: The absolute minimum is enough data to cover at least two full market cycles, including both bull and bear markets. For US equities, this typically means at least 15 years (e.g., 2007-2022 captures the financial crisis, recovery, COVID crash, and the 2022 drawdown). For monthly strategies, 15 years gives you 180 observations. For daily strategies, it gives you roughly 3,750 trading days. If your strategy depends on rare events (recessions, crises), you need more data to capture enough events -- ideally 25-30 years or more. For walk-forward analysis, you need even more data because each training window consumes 3-5 years.

**Q2: How should I model transaction costs in a backtest?**

A: At minimum, include the half-spread cost for each trade. For large-cap US stocks, use 0.03-0.05% per trade. For mid-cap, use 0.10-0.20%. For small-cap, use 0.25-0.50%. Add a market impact component that scales with order size relative to average daily volume: 0.05% for small orders, 0.10-0.20% for medium, and 0.30%+ for large. Add slippage of 0.02-0.05%. As a rough total, use 0.10% per trade for liquid large-caps and 0.50% for less liquid small-caps. These are conservatively estimated -- many real-world traders experience higher costs. It is always better to overestimate transaction costs than underestimate them.

**Q3: How do I avoid survivorship bias in a stock backtest?**

A: Use a database that includes delisted securities and their delisting returns. The CRSP database from the University of Chicago is the gold standard for US stocks and includes all delistings with their final returns. Compustat's Point-in-Time database provides fundamental data free of lookahead bias. If you cannot access these (they are expensive), at minimum ensure your data source includes delisted stocks. Many free data sources (Yahoo Finance, Google Finance) only include currently active securities. When you notice your universe has no bankrupt companies, you have survivorship bias.

**Q4: What is a realistic expectation for how much a strategy degrades from backtest to live trading?**

A: Expect a 30-60% decline in risk-adjusted returns. If your backtest shows a Sharpe ratio of 2.0, plan for a live Sharpe of 0.8-1.4. If it shows annual alpha of 5%, plan for 2-3% live alpha. If it shows 12% annual returns, plan for 8-9% live returns. These degradation rates are averages; some strategies degrade more, some less. Strategies with fewer parameters, longer holding periods, and trading liquid securities tend to degrade less. Strategies with many parameters, high turnover, and illiquid securities tend to degrade more.

**Q5: Should I ever use a backtest to make investment decisions?**

A: Yes, but with appropriate skepticism. A well-constructed backtest -- one that uses survivorship-free data, avoids lookahead bias, includes realistic transaction costs, uses few parameters, and passes walk-forward analysis -- provides genuinely useful information about a strategy's characteristics. The key is to use the backtest to understand the strategy's behavior (when it works, when it fails, how much it drawdown) rather than to predict its exact future returns. Think of a backtest as a stress test, not a forecast. A strategy that fails a proper backtest is almost certainly bad. A strategy that passes is possibly good but needs live verification with small capital before scaling up.

**Q6: How can I tell if a fund manager's backtest is trustworthy?**

A: Ask pointed questions. What database did they use? Does it include delisted securities? Did they use point-in-time data or retroactively available data? How many parameters does the strategy have? What are the total transaction cost assumptions? Did they perform walk-forward analysis? What is the in-sample versus out-of-sample performance? How does the strategy perform in different market regimes (bull, bear, high volatility, low volatility)? A trustworthy manager will have clear, detailed answers. A manager who cannot answer these questions -- or who dismisses them as "technical details" -- is either careless or deliberately obscuring the weaknesses of their approach.

**Q7: What are the best free tools for backtesting?**

A: For Python users, `backtrader` and `zipline` are popular open-source backtesting frameworks. `QuantConnect` offers a cloud-based platform with free data for limited use. `Portfolio Visualizer` (portfoliovisualizer.com) provides simple backtesting of asset allocation strategies without coding. For options backtesting, `OptionStack` offers limited free access. The biggest challenge is data quality: free price data (Yahoo Finance) lacks delisting returns and has survivorship bias. Serious backtesting requires paid data (CRSP, Bloomberg, or similar), which costs hundreds to thousands of dollars per year. The gap between free and paid data quality is large, and using free data introduces biases that can invalidate your results.

---

---

## YouTube Script

**Week 46: Backtesting and Strategy Validation**

[VISUAL: Title card -- "The Backtest Trap: Why Most Strategies Fail in Real Life"]

**Alex**: Today we are going to talk about one of the most important -- and most treacherous -- tools in investing: backtesting. The practice of testing your strategy on historical data to see how it would have performed. And I need to warn you upfront: backtesting is incredibly seductive and incredibly dangerous.

**Sam**: Dangerous? I thought backtesting was just responsible due diligence. You want to see if a strategy worked before putting real money on it.

**Alex**: That is exactly why it is dangerous. The idea is completely sound. The execution is where investors lose fortunes. Here is the core problem: a backtest is a retrospective analysis of data you already have. It is like reading a mystery novel after someone told you who the murderer is. Everything looks obvious in hindsight.

**Sam**: So backtests are biased toward looking good?

**Alex**: Always. And not by a small amount. Research consistently shows that strategies perform 30-70% worse in live trading than in backtests. A strategy that shows a Sharpe ratio of 2.0 in the backtest typically delivers 0.8 to 1.2 live. A strategy showing 5% annual alpha often delivers 1-2%.

[VISUAL: Chart showing the "Alpha Waterfall" -- how backtested returns erode step by step]

[ANIMATION: animation/week46_backtest_pitfalls.py -- Animated demonstration of backtesting biases. The animation starts with a "clean" backtest showing an equity curve rising smoothly from $100,000 to $500,000 over 20 years. A counter in the corner shows the annualized return and Sharpe ratio. Then, one by one, biases are "turned on" and the equity curve adjusts in real time. First, survivorship bias is corrected: several stocks in the portfolio go bankrupt, and the equity curve drops. The annualized return decreases visibly. Second, lookahead bias is corrected: trades that used future information are removed, causing the curve to dip further. Third, transaction costs are added: each trade incurs a visible cost deduction, and the equity curve flattens. Fourth, slippage is added: fills worsen, and the curve drops further. Finally, the overfit parameters are replaced with simpler rules, and the curve drops to nearly match the benchmark. The final frame shows side-by-side: the "as presented" backtest versus the "corrected" backtest, with the gap between them highlighted and labeled "The Backtest Illusion."]

**Sam**: That animation is sobering. The strategy went from looking amazing to barely beating the index.

**Alex**: And that is a GOOD outcome. Many strategies go from "beating the index by 5%" to "underperforming the index by 2%" after corrections. Let me walk you through each bias so you can spot them.

[VISUAL: "Lookahead Bias" section header]

**Alex**: Lookahead bias is the most insidious. It occurs when your backtest uses information that was not available at the time of the trade. It sounds like an obvious mistake, but it hides in places you would never expect.

**Sam**: Like what?

**Alex**: Financial data revisions. GDP numbers are revised multiple times after the initial release. The "final" GDP figure for Q3 might not be available until three months after the quarter ends. If your backtest uses the final figure on the date of the initial release, you are using data from the future.

**Sam**: But databases just show the final number, right?

**Alex**: Exactly. Most databases show the revised, corrected, final figure with a timestamp of the original reporting date. Your backtest treats it as if the revised number was known on day one. This is a subtle but real form of lookahead bias.

**Alex**: Earnings data is even worse. A company's fiscal Q4 might end December 31, but they do not report earnings until February. Most databases assign Q4 data to December 31. If your backtest uses Q4 earnings data on January 2 to buy a stock, you are trading on information that would not exist for another 6 weeks.

[VISUAL: Timeline showing the gap between fiscal quarter end and earnings report date]

**Sam**: So how do you fix this?

**Alex**: Use point-in-time databases -- databases that record when each piece of information became available. Or impose a conservative lag: do not use quarterly data until 90 days after the fiscal quarter end. This ensures the data was definitely public before you trade on it.

**Alex**: Another sneaky source of lookahead bias is index membership. If you backtest a strategy on "S&P 500 stocks" using the CURRENT S&P 500 members, you are including Tesla in 2019, even though Tesla was not added until December 2020.

**Sam**: And Tesla's stock tripled in 2020. So including it retroactively would inflate returns.

**Alex**: Exactly. You need the HISTORICAL constituent list -- which companies were actually in the S&P 500 on each date. This is harder to obtain than you might think, which is why many amateur backtests get it wrong.

[VISUAL: "Survivorship Bias" section header]

**Alex**: Survivorship bias is conceptually simple: your data includes only the winners because the losers have disappeared. But the magnitude of the problem is larger than most people realize.

**Sam**: Give me a concrete example.

**Alex**: You want to backtest a small-cap value strategy. You pull a list of all US stocks from your database and filter for small, cheap ones. But your database only includes companies that CURRENTLY exist. Companies that went bankrupt in 2008, 2015, or 2020 are not in the database. They are gone.

**Sam**: And those bankrupt companies were probably small and cheap right before they died.

**Alex**: Right. Your strategy would have bought many of those companies. Some of the "small and cheap" stocks in your backtest recovered and tripled. In reality, some of them went to zero. You see only the ones that survived. The estimated magnitude of survivorship bias in small-cap value backtests is 1.5-3% per year.

**Sam**: So a strategy showing 14% returns might really deliver 11% after correcting for this bias.

**Alex**: And that 11% -- before transaction costs, before taxes, before fees -- is suddenly much less impressive than the 14% in the marketing materials.

[VISUAL: Side-by-side equity curves -- with survivorship bias (smooth, upward) and without (rougher, lower)]

**Alex**: Survivorship bias affects mutual fund analysis even more. When you look at "10-year mutual fund performance," you are seeing only the funds that survived 10 years. Funds that performed so badly they were closed or merged are excluded. This inflates the apparent average return by 1-2% per year and makes active management look more competitive with passive indexing than it actually is.

**Sam**: So the statistic that "40% of active funds beat their benchmark" might be even worse than it sounds.

**Alex**: Correct. When you include dead funds, the percentage that beat their benchmark drops further. The true long-run success rate of active management, after survivorship bias correction, is closer to 10-15% over 15-year periods.

[VISUAL: "Overfitting" section header]

**Sam**: Let us talk about overfitting. This comes up a lot in machine learning discussions, but how does it apply to investment strategies?

**Alex**: Imagine you are designing a momentum strategy. You need to choose a lookback period -- how many months of past returns do you look at? You test 1 month, 2 months, 3 months, all the way to 24 months. You find that 11 months gives the highest return.

**Sam**: Great, use 11 months.

**Alex**: But WHY 11 months? Is there an economic reason why 11 is better than 10 or 12? Almost certainly not. The reason 11 months looks best is random -- it happens to align with the specific fluctuations in your historical data. If you run the same test on a different time period, the "optimal" lookback might be 7 months, or 14 months, or something completely different.

**Sam**: So choosing 11 months is overfitting to the specific historical data.

**Alex**: Exactly. And it gets worse the more parameters you optimize. If you also optimize the number of stocks to hold, the rebalancing frequency, the sector constraints, and the volatility filter, you have five parameters, each tested over multiple values. The total number of combinations is enormous, and the chance that the "best" combination is genuinely the best -- rather than randomly the best in this specific data -- is very small.

**Sam**: How many parameters is too many?

**Alex**: A useful rule: you need at least 50 independent observations per parameter. With 15 years of monthly data (180 observations), you can responsibly optimize at most 3 parameters. With 5 years (60 observations), you can optimize maybe 1 parameter. A strategy with 10 optimized parameters on 5 years of data is guaranteed to be overfit.

[VISUAL: Table showing data length vs. maximum parameters with 50:1 rule]

**Alex**: Here is a simple diagnostic. If changing a parameter slightly causes a dramatic change in performance, the strategy is overfit. A genuine effect should be robust -- if 11 months works, then 10 and 12 months should also work reasonably well. If 11 months shows a Sharpe of 2.0 but 10 months shows 0.5 and 12 months shows 0.3, that 11-month result is noise.

**Sam**: That makes intuitive sense. A real pattern would not depend on such precise calibration.

**Alex**: Right. Think of it this way: the real world is messy. Any genuine edge in financial markets must be robust to imprecise implementation. If your strategy requires perfectly calibrated parameters to work, it will not survive the imprecision of real-world trading.

[VISUAL: "Walk-Forward Analysis" section header]

**Sam**: So how do we properly validate a strategy?

**Alex**: Walk-forward analysis. Instead of one split into training and testing, you do many. You take a 5-year training window, optimize your strategy, then test it on the next year. Then you roll the window forward by one year and repeat. Over a 20-year period, you get 15 separate out-of-sample tests.

**Sam**: So it is like simulating what a real trader would do -- only looking at past data to make future decisions.

**Alex**: Exactly. And the key feature is that you get MULTIPLE out-of-sample tests, not just one. If the strategy works in 12 out of 15 test periods, that is much more convincing than one test period that happened to be favorable.

**Sam**: What if it works in 8 out of 15?

**Alex**: Then the strategy is regime-dependent -- it works in some market conditions and fails in others. That is useful information, but it means you need to identify which regime favors the strategy and whether you can identify regime changes in real time. If you cannot, the strategy is impractical.

[VISUAL: Walk-forward timeline showing rolling training and test windows]

**Alex**: Walk-forward analysis also reveals the realistic Sharpe ratio you should expect. If the in-sample Sharpe is 2.0 and the walk-forward Sharpe is 1.0, you know the strategy has genuine alpha but the backtest overstates it by 2x. If the in-sample Sharpe is 2.0 and the walk-forward Sharpe is 0.2, the strategy is overfit and the "alpha" is an illusion.

**Sam**: Now let us talk about transaction costs. You mentioned they can destroy a strategy.

[VISUAL: "Transaction Costs" section header]

**Alex**: Transaction costs are the reality check that separates paper profits from real profits. Many beautiful strategies exist only in a world of zero transaction costs.

**Sam**: But we have zero commissions now. Are costs not negligible?

**Alex**: Commissions were never the main cost. The spread, market impact, and slippage are the big ones. When you buy a stock, you pay the ask price, which is above the midpoint. When you sell, you get the bid price, which is below the midpoint. That is the spread cost, and it happens on EVERY trade.

**Alex**: Then there is market impact. If you are buying 10,000 shares and the daily volume is 50,000, your buying pushes the price up against you. The bigger your order relative to volume, the more you move the price. This can easily cost 0.10-0.30% per trade for medium-sized orders.

**Sam**: And this gets worse for small-cap stocks with lower volume.

**Alex**: Much worse. A small-cap stock trading 20,000 shares per day with a spread of 0.50% and high impact costs can cost 0.50-1.00% per trade. If your strategy trades this stock 4 times per year, that is 2-4% in annual costs just from this one holding.

[VISUAL: Cost breakdown for a hypothetical trade in a large-cap vs. small-cap stock]

**Alex**: Let me show you the full impact with a real example. Take a monthly momentum strategy. It turns over 200% of the portfolio per year. That means the equivalent of the entire portfolio is bought and sold twice.

**Sam**: So every dollar in the portfolio is traded about 4 times per year -- 2 buys and 2 sells.

**Alex**: Right. At 0.15% per trade for large-caps, that is 4 times 0.15% equals 0.60% annual cost. Seems manageable. But the stocks momentum strategies buy tend to be mid- and small-caps with higher costs. At 0.30% per trade, costs become 1.20% per year. Add slippage and opportunity cost, and you are at 1.50-2.00%.

**Sam**: And if the strategy's gross alpha is 3%, half to two-thirds of it is eaten by costs.

**Alex**: And that is the good scenario. Many strategies have gross alpha of 1-2%, which is entirely consumed by transaction costs. The strategy looks great on paper and loses money in practice.

[VISUAL: "Alpha Waterfall" showing how gross alpha erodes through each cost layer]

**Sam**: So how do I know when to trust a backtest?

[VISUAL: "When to Trust a Backtest" section header]

**Alex**: I use a scorecard approach. There are about ten criteria that a good backtest should meet. I grade each one on a 0-2 scale.

**Sam**: Give me the top five.

**Alex**: First: does the strategy have an economic rationale? Not just "it works" but WHY does it work? Who is on the losing side of this trade? If you cannot identify the loser, you might BE the loser.

**Alex**: Second: simplicity. Strategies with 1-3 parameters are more likely genuine than strategies with 10-20 parameters. Every extra parameter is an opportunity for overfitting.

**Alex**: Third: walk-forward performance. Does it deliver positive, consistent returns across multiple out-of-sample test periods? If it only works in certain periods, it is regime-dependent at best.

**Alex**: Fourth: transaction costs. Does the strategy survive after realistic costs? If costs consume more than 50% of gross alpha, the strategy is fragile -- small changes in market conditions could push it underwater.

**Alex**: Fifth: multiple markets. Does it work in the US AND Europe AND Japan? A pattern that appears only in one country during one time period is probably data-mined. A pattern that appears across multiple countries and time periods is more likely genuine.

**Sam**: What is the strongest sign that a backtest is overfit?

**Alex**: Performance that is too good. If someone shows you a backtest with a Sharpe ratio above 3.0, assume overfitting until proven otherwise. The best investors in the world -- Warren Buffett, Jim Simons, Ray Dalio -- have live Sharpe ratios of 0.7 to 2.5. A backtest showing Sharpe 4.0 is claiming to be better than the best investors who ever lived. Possible but extremely unlikely.

[VISUAL: Spectrum of Sharpe ratios -- market average (0.4), good active manager (0.7), great hedge fund (1.5), suspicious backtest (3.0+)]

**Sam**: What about new retail investors who want to test a simple idea? Like "buy stocks after they drop 20%."

**Alex**: Great example. Let us walk through how you would test that responsibly. First, define the strategy precisely. "Buy stocks in the S&P 500 after a 20% decline from their 52-week high. Hold for 6 months. Equal weight."

**Sam**: Simple. Two parameters: the drawdown threshold and the holding period.

**Alex**: Good. Now, get survivorship-free data. Make sure you include stocks that were in the S&P 500 at each point in time, not just current members. Include companies that were later removed due to bankruptcy or merger.

**Sam**: What about transaction costs?

**Alex**: Use 0.10% per trade as a baseline. That covers spread and small impact for large-cap stocks. Your turnover depends on how many stocks trigger the 20% decline rule, but it is probably moderate.

**Alex**: Split the data. Use 2000-2015 to develop and confirm the strategy, then test on 2015-2025. Better yet, run walk-forward analysis with 5-year training windows.

**Sam**: And what would I probably find?

**Alex**: You would probably find that buying large dips works on average -- stocks that decline 20% tend to recover more often than not -- but with enormous variance. Some 20% declines become 50% declines. The strategy underperforms dramatically during bear markets (2008, 2020 briefly, 2022) because EVERYTHING is declining 20%, and you are buying everything, and much of it keeps falling.

**Sam**: So the average looks okay but the distribution of outcomes is wide.

**Alex**: And that is the key insight. Backtests show you the average outcome, but you live through a single path. The average may be positive while many individual paths are painful. Understanding the DISTRIBUTION of outcomes -- not just the average -- is essential for deciding whether you can actually follow a strategy through its worst periods.

[VISUAL: Distribution of outcomes for the "buy the dip" strategy, showing the fat tail of losses]

**Sam**: One more question. If backtests are so unreliable, how do professional quants use them?

**Alex**: Professionals treat backtests as the BEGINNING of research, not the end. A backtest is a hypothesis test: "Is this pattern real enough to investigate further?" If it passes the backtest with all biases corrected, they move to paper trading -- running the strategy in real time with no money. If it works in paper trading for 6-12 months, they allocate a small amount of capital. If it works with real money for another 6-12 months, they gradually increase the allocation. At every stage, they compare live performance to backtested expectations.

**Sam**: So the backtest is just step one of a multi-step validation process.

**Alex**: Exactly. And most strategies fail at each successive stage. Out of 100 backtested ideas, maybe 20 survive bias correction. Of those 20, maybe 5 work in paper trading. Of those 5, maybe 2 work with real money. And of those 2, maybe 1 continues to work after 3 years. The attrition rate is enormous, which is why genuine alpha is so rare and so valuable.

**Sam**: That is a sobering conversion rate. One percent.

**Alex**: And that is at professional firms with teams of PhDs, institutional data, and decades of experience. For individual investors running backtests on free data with retail tools, the success rate is even lower. Which is why, for most investors, the best use of backtesting knowledge is EVALUATING other people's claims rather than building your own strategies. When your financial advisor shows you a beautifully smooth equity curve, you now know to ask: "Is this survivorship-free? Point-in-time data? How many parameters? Walk-forward tested? After realistic costs?"

[VISUAL: "The Backtest Validation Checklist" -- 10 questions to ask about any backtest]

**Sam**: Thanks, Alex. Next week, we move to a very different topic -- tail risk hedging. How do you protect your portfolio against rare but catastrophic events?

**Alex**: Right. Tail risk is where everything we have learned about statistics, correlations, and strategy testing meets the real world of market crashes. It is a lesson that every investor needs but hopes they never have to use.

[VISUAL: End card -- "Next Week: Tail Risk Hedging"]
