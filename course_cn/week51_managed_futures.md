<!-- 此文件需要翻译为简体中文 -->
<!-- This file needs translation to Simplified Chinese -->

# Week 51: Managed Futures and Trend Following

## Reading Section

### a) Why This Is Important

If there is one strategy that every serious portfolio should consider, it is managed futures -- specifically, trend following. The reason is simple and profound: trend following is one of the very few strategies that has demonstrated consistent positive returns during major equity bear markets, while also generating positive returns on average during normal markets. This combination -- "crisis alpha" plus a positive long-run expected return -- makes it arguably the most powerful diversifier available to investors.

Most portfolio construction focuses on the correlation between asset classes: stocks and bonds, domestic and international, equities and commodities. But in major crises, correlations between traditional asset classes tend to spike toward 1.0 -- the very moment you need diversification the most, it fails. Trend following breaks this pattern. During the 2008 Global Financial Crisis, the average managed futures fund returned approximately +18% while the S&P 500 lost -37%. During the dot-com crash (2000-2002), during the European debt crisis, during COVID -- trend following strategies delivered positive or at least protective returns in each case.

Understanding why trend following works, how it is implemented, and how to access it at reasonable cost has become essential knowledge for any Level 5 investor. The strategy has moved from the exclusive domain of institutional investors and high-net-worth individuals to become accessible through low-minimum ETFs.

This lesson will explain the mechanics of trend following, the academic evidence behind time series momentum, the concept of crisis alpha, practical implementation options, and how to integrate managed futures into a multi-asset portfolio. By the end, you will understand why the largest and most sophisticated institutional investors in the world -- sovereign wealth funds, pension systems, and endowments -- allocate 10 to 20 percent of their portfolios to this strategy.

---

### b) What You Need to Know

#### What Are Managed Futures?

Managed futures is a broad category that encompasses any professionally managed investment strategy that trades futures contracts. Within this category, Commodity Trading Advisors (CTAs) are the most common structure. While "managed futures" technically includes many approaches (fundamental, quantitative, discretionary), the dominant strategy by far is systematic trend following.

```
Managed Futures Universe:

Managed Futures (CTA Industry)
  |
  +-- Systematic Strategies (~85% of industry AUM)
  |     |
  |     +-- Trend Following (~70% of systematic)
  |     |     Long-term trend (6-12 month lookback)
  |     |     Medium-term trend (1-6 month lookback)
  |     |     Short-term trend (days to weeks lookback)
  |     |
  |     +-- Counter-Trend / Mean Reversion (~10%)
  |     +-- Carry (~10%)
  |     +-- Pattern Recognition (~5%)
  |     +-- Machine Learning / Statistical (~5%)
  |
  +-- Discretionary Strategies (~15% of industry AUM)
        |
        +-- Global Macro (discretionary futures trading)
        +-- Fundamental (commodity specialists)

Industry AUM: ~$400 billion (as of 2024)
Number of CTAs: ~1,500 registered
Top 20 firms control ~60% of AUM
```

#### The Trend Following Concept

Trend following is based on a remarkably simple premise: assets that have been going up tend to continue going up, and assets that have been going down tend to continue going down. The strategy buys assets in uptrends and sells (shorts) assets in downtrends, holding positions until the trend reverses.

```
Core Trend Following Rules (Simplified):

1. TREND IDENTIFICATION
   Compute a moving average (e.g., 200-day) for each asset
   If price > moving average: UPTREND (go long)
   If price < moving average: DOWNTREND (go short)

2. POSITION SIZING
   Allocate risk equally across all markets
   Size each position inversely proportional to its volatility
   Target a specific portfolio-level volatility (e.g., 10-15%)

3. REBALANCING
   Update signals daily or weekly
   Adjust position sizes when volatility changes
   Exit positions when trend reverses

That is it. The elegance is in the simplicity.
The difficulty is in the discipline and execution.
```

```
Trend Following Signal: Moving Average Crossover

Price
  |
  |              **                     ***
  |            **  **                 **   **
  |          **      **             **       **
  |        **    B    ****     ****           **
  |      **           ----****----             **
  |    **         ----               ----        **
  |  **      ----                         ----    **
  | *   ----      S                            ----*  S
  |----                                             ----
  |___________________________________________________
                      Time

  * = Price
  ---- = 200-day Moving Average
  B = BUY signal (price crosses above MA)
  S = SELL/SHORT signal (price crosses below MA)

  In uptrends: LONG position, profits as price rises
  In downtrends: SHORT position, profits as price falls
  During whipsaws: Losses from false signals (the cost of the strategy)
```

More sophisticated trend following systems use multiple lookback periods and combine different signal types:

```
Multi-Signal Trend Following:

Signal Type         Lookback     Sensitivity   Whipsaw Risk
---------------------------------------------------------------
Short-term MA       10-50 days   High          High
Medium-term MA      50-100 days  Medium        Medium
Long-term MA        100-250 days Low           Low
Breakout (Donchian) 20-200 days  Varies        Medium
Exponential MA      Various      Adjustable    Medium
Time Series Mom     1-12 months  Low-Medium    Low

Most professional CTAs combine 3-5 signal types across
multiple lookback periods to smooth out signals and reduce
whipsaw costs. Signals are often weighted and averaged.

Example Composite Signal:
  Signal = 0.20 * Short_MA + 0.30 * Medium_MA
         + 0.30 * Long_MA  + 0.20 * Breakout

  If Signal > 0: Go LONG (proportional to signal strength)
  If Signal < 0: Go SHORT (proportional to signal strength)
  If Signal near 0: FLAT or reduced position
```

#### Time Series Momentum: The Academic Foundation

The academic foundation for trend following was formally established by Moskowitz, Ooi, and Pedersen in their landmark 2012 paper "Time Series Momentum." They documented that looking at an asset's own past returns (time series momentum) predicts future returns across virtually every asset class.

```
Time Series Momentum (TSMOM) Evidence:

Asset Class         Markets Tested   Premium   Sharpe Ratio
---------------------------------------------------------------
Equity Indices      12 markets       7.3%      0.52
Bond Futures        10 markets       3.8%      0.41
Currency Forwards   9 markets        4.2%      0.45
Commodity Futures   27 markets       5.1%      0.47
ALL COMBINED        58 markets       5.1%      0.76*

*Diversified portfolio Sharpe ratio is HIGHER than any single
 asset class because trends are relatively uncorrelated across markets.

Key Findings:
  1. TSMOM is positive and significant in EVERY asset class
  2. Works across multiple lookback periods (1, 3, 6, 12 months)
  3. Persists after transaction costs
  4. NOT explained by traditional risk factors
  5. Has existed for over 100 years (out-of-sample confirmation)
```

Why does time series momentum work? Several explanations have been proposed:

```
Why Trends Exist in Financial Markets:

1. BEHAVIORAL EXPLANATIONS
   a) Anchoring: Investors anchor to old prices and underreact
      to new information. Prices adjust slowly to fundamentals.
   b) Herding: Investors follow each other, creating momentum
   c) Disposition Effect: Investors sell winners too early
      and hold losers too long, slowing trend development
   d) Confirmation Bias: Once a trend forms, investors seek
      information confirming the trend and ignore contradictions

2. INSTITUTIONAL EXPLANATIONS
   a) Central Bank Policy: Interest rate cycles create
      multi-year trends in bonds and currencies
   b) Risk Management: Stop-losses force selling into declines,
      exacerbating trends
   c) Index Rebalancing: Mechanical buying/selling by passive
      funds creates trend persistence
   d) Margin Calls: Forced liquidation during stress extends
      downward trends

3. FUNDAMENTAL EXPLANATIONS
   a) Business Cycles: Economic expansions and contractions
      create multi-quarter trends in corporate earnings
   b) Commodity Super Cycles: Supply/demand imbalances take
      years to resolve, creating extended trends
   c) Regime Changes: Shifts in monetary policy, regulation,
      or geopolitics create structural breaks that
      manifest as trends

KEY INSIGHT: Trends are not random or irrational.
They reflect the slow, uneven process by which markets
incorporate information and adjust to new realities.
```

#### Crisis Alpha: Why Trend Following Profits in Crashes

The most valuable property of trend following is its behavior during major crises. This property, dubbed "crisis alpha" by Kathryn Kaminski in her influential research, arises mechanically from how trend following works.

```
Crisis Alpha Mechanism:

Phase 1: THE BUILD-UP (Months Before Crisis)
  Markets are calm or rising
  Trend following is modestly profitable (long equities)
  No crisis protection visible

Phase 2: THE INITIAL SHOCK (First Days/Weeks)
  Markets drop sharply
  Trend following systems LOSE money initially
  Long equity positions face losses
  This is the "whipsaw cost" of trend following

Phase 3: THE TREND DEVELOPS (Weeks to Months)
  Decline continues and accelerates
  Trend signals flip from LONG to SHORT
  Trend following systems now SHORT equities
  Simultaneously: LONG bonds (flight to safety trend)
  Simultaneously: SHORT commodities (demand destruction)

Phase 4: THE CRISIS DEEPENS (Months)
  Multiple sustained trends across asset classes
  Trend following is HIGHLY profitable
  Short equities + Long bonds + Short commodities + Long USD
  All trends reinforcing each other

Phase 5: THE RECOVERY (Bottom and Reversal)
  Markets bottom and reverse
  Trend following LOSES some profits on reversal
  Systems slowly flip from SHORT back to LONG
  Net result: Large positive return over the full crisis cycle

KEY INSIGHT: Trend following LOSES during sudden, short shocks
but PROFITS during extended, sustained crises.
The net effect over a full crisis is almost always positive.
```

```
Trend Following Performance During Major Crises:

Event                       S&P 500    Trend Following*   Bonds
                            Return     Return (est.)      Return
----------------------------------------------------------------------
Black Monday (Oct 1987)     -20.5%     +11.2%             +4.5%
Asian Crisis (1997-98)       -6.2%     +12.4%             +8.2%
LTCM / Russia (1998)        -19.3%     +18.1%             +5.7%
Dot-com Crash (2000-02)     -47.4%     +28.4%             +22.3%
GFC (2007-09)               -56.8%     +18.3%             +14.0%
European Debt (2011)        -19.4%     +5.1%              +7.8%
COVID Crash (Feb-Mar 2020)  -33.9%     -3.2%              +3.2%
2022 Bear Market            -25.4%     +23.7%             -13.0%

*Approximate, based on SG Trend Index or similar benchmarks

Key observations:
  1. Trend following was POSITIVE in 6 out of 8 major crises
  2. The two "failures" (COVID, Eurozone) were SMALL losses
  3. The 2022 result is remarkable: trend following profited
     while BOTH stocks AND bonds lost money
  4. Long-duration crises (dot-com, GFC) produce the best results
  5. Short, sharp shocks (COVID) produce the worst results
```

Why does trend following perform differently in 2022 vs. COVID?

```
COVID (Feb-Mar 2020) vs. 2022 Bear Market: A Study in Contrast

COVID:
  - Duration: ~5 weeks of decline
  - Speed: Fastest 30% decline in history
  - Reversal: Sharp V-shaped recovery
  - Trend following had NO TIME to flip short
  - Result: Small loss (-3.2%)

2022:
  - Duration: ~10 months of decline
  - Speed: Gradual, grinding decline
  - Bond market also trended down (rising rates)
  - Commodities trended UP (energy crisis)
  - Trend following had PLENTY OF TIME to establish shorts
  - Result: Large profit (+23.7%)

  Lesson: Trend following needs TIME for trends to develop.
  Short, sharp shocks are the enemy. Extended moves are the friend.
  This is why trend following provides the BEST crisis protection
  during the WORST crises (which tend to be extended).
```

#### Diversification Benefits

The correlation structure of managed futures relative to traditional assets is the primary reason for including them in a portfolio.

```
Correlation of Managed Futures to Traditional Assets:

                        All Periods    Bull Markets   Bear Markets
                        (Full Sample)  (Stocks Up)    (Stocks Down)
---------------------------------------------------------------------
S&P 500                  -0.05          +0.10          -0.35
US Aggregate Bonds       +0.15          +0.10          +0.25
60/40 Portfolio           0.00          +0.10          -0.20
Commodities              +0.10          +0.10          +0.05
Real Estate (REITs)       0.00          +0.05          -0.15
Hedge Funds (HFRI)       +0.20          +0.25          +0.10

KEY INSIGHT: Managed futures have NEAR-ZERO average correlation
to stocks and bonds. But the correlation is NEGATIVE during
bear markets -- exactly when you need diversification most.

This "conditional correlation" property is extremely rare.
Bonds provided it historically but FAILED in 2022 (positive
correlation during a bear market). Managed futures did NOT fail.
```

```
Portfolio Impact of Adding Managed Futures:

                     60/40        60/40 + 15%     Improvement
                     Portfolio    Managed Futures
-------------------------------------------------------------
Annual Return        8.5%         8.8%            +0.3%
Volatility           9.8%         8.2%            -1.6%
Sharpe Ratio         0.55         0.71            +0.16
Max Drawdown        -32.5%       -23.4%           +9.1%
Worst Year          -22.1%       -15.8%           +6.3%

  The improvement in risk-adjusted returns comes primarily from
  REDUCED DRAWDOWNS rather than increased returns.

  A 15% allocation to managed futures reduced the worst drawdown
  by nearly 10 percentage points while maintaining similar returns.

  This is the "free lunch" of diversification in action --
  adding an asset with near-zero or negative correlation
  improves the portfolio without proportionately reducing returns.
```

#### How Professional CTAs Construct Portfolios

Professional trend following CTAs typically trade 50 to 200 different futures markets across four major sectors: equities, bonds, currencies, and commodities.

```
Typical CTA Market Universe:

EQUITY INDICES (10-15 markets):
  S&P 500, Nasdaq 100, Russell 2000 (US)
  Euro Stoxx 50, DAX, FTSE 100 (Europe)
  Nikkei 225, Hang Seng, ASX 200 (Asia-Pacific)
  MSCI Emerging Markets, KOSPI (Korea)

BOND FUTURES (10-15 markets):
  US Treasuries: 2Y, 5Y, 10Y, 30Y
  German Bunds, UK Gilts, Japanese JGBs
  Australian, Canadian, Italian government bonds
  Eurodollar, Fed Funds, SOFR

CURRENCY FORWARDS (8-12 markets):
  EUR/USD, GBP/USD, JPY/USD, AUD/USD
  CAD/USD, CHF/USD, NZD/USD
  Emerging: BRL, MXN, ZAR, KRW

COMMODITIES (20-30 markets):
  Energy: Crude Oil (WTI, Brent), Natural Gas, Heating Oil, Gasoline
  Metals: Gold, Silver, Copper, Platinum, Palladium
  Grains: Corn, Wheat, Soybeans, Soybean Oil, Soybean Meal
  Softs: Sugar, Coffee, Cocoa, Cotton
  Livestock: Live Cattle, Lean Hogs

TOTAL: 50-80 markets for a diversified CTA
       Some trade 150+ markets

Sector Allocation (Risk-Weighted):
  Equities:     20-30%
  Bonds:        20-30%
  Currencies:   15-25%
  Commodities:  20-30%

  Typically equal-risk-weighted across sectors
  to avoid any single sector dominating the portfolio
```

```
CTA Risk Management Framework:

1. POSITION SIZING (Volatility Targeting)
   Each market position sized to contribute equal risk
   
   Position Size = (Target Risk per Market) / (Market Volatility)
   
   Example:
     Portfolio: $10 million
     Target vol: 12% annualized
     Number of markets: 60
     Risk per market: 12% / sqrt(60) = 1.55%
     
     If Crude Oil volatility = 30% annualized:
       Crude position = (1.55% * $10M) / (30% * Contract Value)
     
     If Gold volatility = 15% annualized:
       Gold position = (1.55% * $10M) / (15% * Contract Value)
     
     Result: Gold position is LARGER in notional terms because
     Gold is less volatile. Both contribute equal risk.

2. PORTFOLIO-LEVEL RISK CONTROLS
   Maximum portfolio leverage: typically 5-10x notional
   Maximum sector concentration: 30-40% of risk budget
   Maximum single market: 5-10% of risk budget
   Dynamic volatility scaling: reduce positions when
   portfolio vol exceeds target

3. STOP LOSSES
   Individual market stops: Typically 2-3x average true range
   Portfolio drawdown stops: Reduce risk at -10% to -15% drawdown
   Correlation-adjusted stops: Tighten stops when correlations rise

4. TAIL RISK MANAGEMENT
   Stress test against historical crises
   Monitor portfolio "long gamma" vs "short gamma" exposure
   Ensure the portfolio benefits from large, sustained moves
```

#### ETF Access to Managed Futures

Retail investors now have access to managed futures strategies through ETFs. The two most prominent are DBMF and KMLM.

```
Managed Futures ETF Comparison:

DBMF (iMGP DBi Managed Futures Strategy ETF)
  Expense Ratio:   0.85%
  AUM:             ~$3 billion
  Inception:       May 2019
  Strategy:        Replicates the returns of the top 20 CTAs
                   using a factor-based approach
  Methodology:     Uses regression analysis to decompose CTA returns
                   into underlying risk factor exposures, then
                   replicates those exposures using liquid futures
  Markets Traded:  ~10-15 core futures contracts
  Leverage:        Typically 2-5x notional
  Key Feature:     Tracks CTA performance without CTA fees (2/20)
  Limitations:     Replication is imperfect; may lag during
                   rapid regime changes; limited market breadth

KMLM (KFA Mount Lucas Managed Futures Index Strategy ETF)
  Expense Ratio:   0.92%
  AUM:             ~$500 million
  Inception:       December 2020
  Strategy:        Tracks the KFA MLM Index, a rules-based
                   trend following strategy
  Methodology:     Equal-risk-weighted trend signals across
                   commodities, currencies, and bonds
  Markets Traded:  ~24 futures contracts
  Leverage:        Typically 3-6x notional
  Key Feature:     Pure, transparent trend following
  Limitations:     No equity index futures; higher expense ratio;
                   less diversified than multi-strategy CTAs

Other Options:
  WTMF (WisdomTree Managed Futures Strategy Fund)
    Expense: 0.65%, AUM: ~$300M, Inception: 2011
    Approach: Quantitative trend and carry
    Note: Longest track record among managed futures ETFs

  CTA (Simplify Managed Futures Strategy ETF)
    Expense: 0.75%, AUM: ~$200M, Inception: 2022
    Approach: Trend following with tail risk overlay
```

```
Performance Comparison (Annualized, 2022-2024):

                Return    Volatility   Sharpe    Max DD
------------------------------------------------------
DBMF             8.2%      12.5%       0.46     -12.3%
KMLM             6.5%      10.8%       0.37     -14.1%
WTMF             3.8%       7.2%       0.25      -8.5%
SG Trend Index   9.5%      13.2%       0.52     -10.8%
S&P 500          9.8%      17.5%       0.42     -25.4%
US Agg Bonds    -1.2%       7.8%      -0.41     -17.8%

Notes:
  - ETFs trail the SG Trend Index (institutional CTA benchmark)
    by 1-3% annually due to replication error and higher costs
  - Even so, managed futures ETFs provided UNCORRELATED positive
    returns during a period when bonds lost money
  - The 2022 result was transformative: managed futures ETFs
    were one of the only asset classes that made money
```

#### Implementation Considerations

```
Practical Considerations for Adding Managed Futures:

1. ALLOCATION SIZE
   Minimum meaningful: 5% of total portfolio
   Recommended range: 10-20% for serious diversification
   Maximum suggested: 25% (beyond this, vol drag becomes significant)

   Research (AQR, Man Group): 10-15% allocation provides
   the best risk-adjusted portfolio improvement

2. WHICH PRODUCT TO USE
   If choosing one: DBMF (broadest replication, largest AUM)
   If choosing two: DBMF + KMLM (complementary approaches)
   Advanced: Combine ETF with direct futures trading if
   account size permits ($500K+ recommended for direct futures)

3. TAX CONSIDERATIONS
   Managed futures ETFs use futures contracts, which receive
   favorable tax treatment under Section 1256:
     60% long-term capital gains
     40% short-term capital gains
   Regardless of holding period (the "60/40 rule")
   This makes managed futures ETFs MORE tax-efficient than
   equity factor ETFs with high turnover

4. REBALANCING
   Managed futures returns are UNCORRELATED to stocks/bonds
   This means the allocation will naturally drift
   After a stock crash: managed futures will be overweight (sell some)
   After a stock boom: managed futures will be underweight (buy more)
   Rebalancing INTO managed futures after a strong stock run
   is effectively buying crash insurance at a discount

5. BEHAVIORAL CHALLENGES
   Managed futures can underperform stocks for 2-3 years straight
   During bull markets, the allocation feels like dead weight
   Investors must understand they are paying for INSURANCE
   The "premium" is the opportunity cost during bull markets
   The "payout" comes during crises

6. COMBINATION WITH OTHER ALTERNATIVES
   Managed futures + volatility selling = complementary
   (Vol selling loses during crises when managed futures gain)
   Managed futures + factor tilts = low correlation
   Managed futures + real assets = diversified alternatives sleeve
```

#### Historical Context: Trend Following Across Centuries

One of the most compelling arguments for trend following is its longevity. Research by Lemperi`ere et al. (2014) and Hurst, Ooi, and Pedersen (2017) documented positive trend following returns going back to the 1800s.

```
Trend Following Across History:

Period              Markets Available    Trend Return   Notes
----------------------------------------------------------------------
1880-1920           Commodities, bonds   +5.2%         Pre-modern era
1920-1950           Stocks, commodities  +6.8%         Depression, WWII
1950-1970           Broad futures        +4.5%         Post-war calm
1970-2000           Global futures       +8.3%         High vol era
2000-2010           Global futures       +7.1%         Crisis-rich decade
2010-2020           Global futures       +2.8%         Low vol era
2020-2024           Global futures       +8.5%         Return to vol

Key Observations:
  1. Trend following has been profitable in EVERY multi-decade period
  2. Returns are HIGHER during volatile periods (1970s, 2000s, 2020s)
  3. Returns are LOWER during calm, low-volatility periods (2010s)
  4. The strategy has survived world wars, depressions, and
     fundamental changes in market structure
  5. The long history makes it one of the most robust strategies known
```

```
Why Trend Following Persists Over Centuries:

Unlike many anomalies that disappear after discovery,
trend following has persisted because:

1. It is HARD to execute psychologically
   Buying breakouts feels like chasing
   Holding through drawdowns requires iron discipline
   Shorting feels unnatural to most investors
   The strategy "feels wrong" most of the time

2. It REQUIRES institutional infrastructure
   Trading 50-100 futures markets simultaneously
   Managing margin and leverage across asset classes
   Operating 24/7 across global time zones
   Few individuals can replicate this

3. It PROFITS from others' behavioral mistakes
   As long as humans anchor, herd, and panic,
   trends will exist in financial markets
   AI and algorithmic trading may reduce this over time
   But so far, the evidence does not support significant decay

4. It SERVES a structural economic function
   Trend followers provide liquidity during crises
   They SHORT stocks when everyone else is selling
   This sounds paradoxical but trend followers' shorts
   ABSORB selling pressure, providing liquidity to forced sellers
   The premium is compensation for this service
```

#### Common Trend Following Challenges

```
When Trend Following Struggles:

1. WHIPSAW / CHOPPY MARKETS
   Trendless, range-bound markets generate false signals
   Each false signal costs money (buy high, sell low)
   Extended sideways periods can produce 15-25% drawdowns
   Example: 2011-2013 was difficult for most CTAs

2. SHARP V-SHAPED REVERSALS
   Trend following needs TIME to establish positions
   Quick crashes followed by quick recoveries = losses
   Example: COVID crash (Feb-Mar 2020) was too fast
   to flip from long to short to long again

3. CROWDED POSITIONS
   When too many trend followers are in the same trades,
   reversals become amplified
   Example: If everyone is long crude oil on trend,
   a reversal triggers mass selling, overshooting

4. LOW VOLATILITY ENVIRONMENTS
   Trend signals are weaker when volatility is low
   Position sizes are LARGER (inverse vol sizing)
   but trends are SMALLER and less reliable
   The 2010s "low vol" era was the worst decade for CTAs

5. INTEREST RATE REVERSALS
   Bond trends can reverse quickly when central banks pivot
   The 2013 "Taper Tantrum" hurt many CTAs
   Bonds are typically a large allocation in CTA portfolios
```

---

### c) Common Misconceptions

**Misconception 1: "Trend following is just momentum investing."**

While trend following uses momentum signals, it differs from the equity momentum factor in several important ways. First, trend following uses *time series* momentum (an asset's own past returns) while the equity momentum factor uses *cross-sectional* momentum (ranking stocks relative to each other). Second, trend following applies across all asset classes -- bonds, currencies, commodities, and equities -- not just stocks. Third, trend following takes both long AND short positions, while most equity momentum strategies are long-only. These differences give trend following its unique crisis alpha property, which equity momentum does not share (momentum crashes during equity market reversals).

**Misconception 2: "Managed futures are too risky because they use leverage."**

While CTAs use notional leverage of 5-10x, this is misleading. Leverage in futures is fundamentally different from leverage in stocks. A CTA positions each market to contribute a small amount of risk, and the total portfolio volatility is typically targeted at 10-15% -- similar to or less than equity market volatility. The high notional leverage exists because futures require only small margin deposits. A trend following strategy with 10% target volatility is actually LESS risky than a 100% stock portfolio (which has 15-20% volatility) despite using 5x notional leverage.

**Misconception 3: "Trend following is a market timing strategy."**

Trend following does not attempt to predict market tops or bottoms. It does not try to "time" the market in the conventional sense. Instead, it reacts to price trends after they have already begun. A trend follower will always miss the top and the bottom. The profit comes from capturing the middle portion of sustained trends. This reactive, rather than predictive, approach is what gives the strategy its robustness -- it does not need to be right about the future, only patient enough to ride existing trends.

**Misconception 4: "Managed futures ETFs provide the same returns as institutional CTAs."**

Managed futures ETFs trail institutional CTAs by approximately 1 to 3 percent annually. The replication approach used by products like DBMF introduces tracking error. The limited number of markets traded by ETFs (10 to 25) versus institutional CTAs (50 to 200) reduces diversification. And the ETF expense ratio (0.85 to 0.95%) adds cost. However, institutional CTAs charge 2% management fee plus 20% performance fee, so the net-of-fee difference is much smaller. For most retail investors, ETFs are the more cost-effective access point.

**Misconception 5: "If trend following works, why is not everyone doing it?"**

Several reasons prevent universal adoption. First, trend following has extended periods of underperformance that most investors cannot tolerate -- the 2010s saw many institutional investors reduce or eliminate their managed futures allocation, right before the strategy delivered stellar 2022 returns. Second, the strategy feels psychologically uncomfortable: buying after prices have already risen and selling after prices have already fallen violates most people's instinct to buy low and sell high. Third, the strategy requires genuine diversification across many markets, which is operationally complex. And fourth, many investors evaluate strategies based on calendar-year returns rather than crisis-period returns, which makes trend following look mediocre during long bull markets.

**Misconception 6: "Trend following cannot work in efficient markets."**

The Efficient Market Hypothesis in its strong form implies that trends should not exist. But decades of evidence show they do. Markets are not perfectly efficient -- they are *adaptively* efficient. Information is incorporated slowly and unevenly due to behavioral biases, institutional constraints, and the complexity of the real economy. Central bank policy creates multi-year interest rate trends. Commodity supply-demand imbalances take years to resolve. Geopolitical shifts create currency trends. These are not market inefficiencies to be arbitraged away -- they are fundamental economic processes that manifest as price trends.

---

### d) Common Questions and Answers

**Q1: How much should I allocate to managed futures in my portfolio?**

A1: Academic research and industry practice suggest 10 to 20 percent for meaningful diversification benefit. The exact amount depends on your risk tolerance and investment horizon. At 5 percent, the impact on portfolio risk is noticeable but modest. At 10 percent, you get substantial drawdown reduction. At 15 to 20 percent, the impact is significant -- potentially reducing maximum drawdown by 25 to 35 percent relative to a traditional 60/40 portfolio. I would not recommend going above 25 percent unless you have deep experience with the strategy and can tolerate extended periods of underperformance during equity bull markets.

**Q2: Should I use DBMF or KMLM, or both?**

A2: If you are allocating to only one product, DBMF is the better choice due to its larger AUM, broader market coverage (including equity index futures, which KMLM excludes), and longer live track record. If you are allocating enough to split between two products, using both DBMF and KMLM provides strategy diversification -- DBMF uses CTA replication while KMLM uses direct trend following, and they will differ in their exposures at any given time. For a 10 percent managed futures allocation, I would suggest 7 percent DBMF and 3 percent KMLM.

**Q3: What should I expect from managed futures during a bull market?**

A3: During sustained equity bull markets, managed futures will typically generate modest positive returns (3 to 6 percent annually) from trends in bonds, currencies, and commodities, combined with long equity positions. However, this will significantly lag the equity market during strong up years. In a year when the S&P 500 returns 25 percent, managed futures might return 5 to 8 percent. This underperformance is the "insurance premium" you pay. The "payout" comes during bear markets, when managed futures can generate 10 to 25 percent while equities lose 20 to 50 percent. You must evaluate the strategy over a full market cycle, not individual calendar years.

**Q4: Can I replicate a trend following strategy on my own?**

A4: In principle, yes. The core strategy -- moving average crossover signals with inverse volatility position sizing -- is not complex. However, practical implementation requires trading futures across many markets, managing margin, monitoring positions across global time zones, and maintaining iron discipline to execute signals without second-guessing. You need a minimum account size of roughly $200,000 to $500,000 to diversify across enough markets. For most individual investors, managed futures ETFs are more practical, even with their imperfect replication and fees.

**Q5: Why did managed futures do so well in 2022?**

A5: 2022 was nearly ideal for trend following. Interest rates rose steadily throughout the year, creating strong short-bond positions. Commodities -- especially energy -- trended sharply higher due to the Russia-Ukraine conflict. The US dollar strengthened consistently. And equities declined gradually over months, giving trend following systems time to establish short positions. Critically, both stocks AND bonds trended downward simultaneously, which normally devastates a 60/40 portfolio but creates opportunities for a strategy that can go short both. Managed futures were one of the only strategies that made money in 2022 precisely because they can profit from downtrends.

**Q6: What is the worst-case scenario for managed futures?**

A6: The worst-case scenario is an extended period of low volatility and trendless markets across all asset classes simultaneously. The 2014-2017 period was close to this: major central banks coordinated to suppress volatility, bond yields were stable, currencies were range-bound, and commodities meandered. Trend following strategies generated near-zero or slightly negative returns for several years. While not catastrophic, the opportunity cost versus equities (which were rallying strongly) was substantial and caused many investors to abandon the strategy. The maximum drawdown for professional CTA indices has been approximately 15 to 20 percent, which is significant but far less than equity drawdowns.

**Q7: How does trend following interact with other portfolio strategies like factor investing or options income?**

A7: Trend following is highly complementary to both. Factor investing tends to have modest positive correlation to the equity market (long-only factor ETFs go down when stocks go down, though possibly less). Options income strategies (selling puts, covered calls) are exposed to equity downside risk. Trend following provides a natural hedge against exactly these scenarios because it flips short during extended equity declines. The combination of factor tilts (long-term equity premium capture), options income (short-term premium harvesting), and trend following (crisis protection) creates a portfolio with multiple return drivers and built-in hedging.

**Q8: Is trend following capacity-constrained? Will it stop working if too much money flows in?**

A8: This is a legitimate concern but less pressing than it appears. The global futures market is enormous -- daily turnover in major futures contracts exceeds hundreds of billions of dollars. The entire CTA industry manages approximately $400 billion, which is small relative to the markets it trades. However, crowding in specific markets or specific trend signals can cause problems. If every CTA uses the same 200-day moving average on crude oil, their simultaneous entry and exit creates self-fulfilling and then self-defeating dynamics. Professional CTAs mitigate this by using diverse signal sets, staggering entry/exit points, and trading less liquid markets that smaller competitors cannot access.

---

## YouTube Script

[VISUAL: Channel intro animation with trend charts across multiple markets -- stocks, bonds, commodities, currencies]

**Alex:** Welcome to Week 51. Today we are covering one of the most important topics in the entire course: managed futures and trend following. This strategy has been responsible for some of the most consistent portfolio protection during market crises, and it is now accessible to retail investors through ETFs.

**Sam:** I have been looking forward to this one. Managed futures always seemed mysterious to me -- like a black box that hedge funds use. Can we demystify it?

[VISUAL: Title card "Managed Futures: Demystified"]

**Alex:** Absolutely. And the surprise is how simple the core concept is. At its heart, trend following -- which accounts for about 70 percent of the managed futures industry -- does one thing: it buys assets that are going up and sells assets that are going down.

**Sam:** That is it? That sounds almost too simple.

**Alex:** The elegance IS the simplicity. A basic trend following system might use a 200-day moving average. When the price is above the 200-day average, you go long. When it is below, you go short. Apply this across 50 to 100 different futures markets -- stocks, bonds, commodities, currencies -- size each position by inverse volatility so that each market contributes equal risk, and you have a professional-grade trend following strategy.

[ANIMATION: animation/week51_trend_following.py -- Animated price chart showing a trend developing over time. A moving average line follows the price. Green arrows appear when buy signals trigger (price crosses above MA), red arrows when sell/short signals trigger (price crosses below MA). Profit and loss accumulates on a running total below the chart.]

**Sam:** If it is that simple, why does not everyone do it?

**Alex:** Two reasons. First, it is operationally complex even though the concept is simple. You need to trade futures across dozens of markets, manage leverage and margin, and operate around the clock across global time zones. Second -- and this is the bigger barrier -- it is psychologically brutal. Buying something that has already gone up feels like chasing. Holding through a 15 percent drawdown while the S&P is ripping higher requires iron discipline. Most people cannot do it.

[VISUAL: Title card "Time Series Momentum: The Academic Evidence"]

**Sam:** Let us talk about the academic foundation. Is there serious research behind this?

**Alex:** Extensive research. The landmark paper was by Moskowitz, Ooi, and Pedersen at AQR Capital Management in 2012. They studied 58 different futures markets across equities, bonds, currencies, and commodities, going back decades. They found that time series momentum -- an asset's own past returns predicting its future returns -- was positive and statistically significant in every single asset class.

**Sam:** Every asset class?

**Alex:** Every one. Equities, bonds, currencies, commodities. The effect was robust across multiple lookback periods from one month to twelve months. It persisted after transaction costs. And it was NOT explained by traditional risk factors. This is not some fragile anomaly -- it is one of the most robust patterns in financial markets.

[VISUAL: Table showing TSMOM returns across asset classes with Sharpe ratios]

**Sam:** Why do trends exist? It seems like markets should be efficient enough to eliminate predictable patterns.

**Alex:** Markets are adaptively efficient, not perfectly efficient. Several forces create trends. First, behavioral biases: investors anchor to old prices and underreact to new information, so prices adjust to new realities slowly rather than instantly. Second, institutional factors: central bank interest rate cycles create multi-year trends in bonds and currencies. Stop-losses and margin calls force selling during declines, extending downward trends. Third, real economic forces: commodity supply-demand imbalances take years to resolve, business cycles create multi-quarter earnings trends, and geopolitical shifts create currency movements that play out over months or years.

[ANIMATION: animation/week51_trend_following.py -- Animated diagram showing the behavioral cycle: new information arrives -> slow initial reaction (anchoring) -> gradual price adjustment -> herding amplifies the move -> overshoot -> eventual mean reversion. The animation highlights how trend following captures the middle portion of this cycle.]

**Sam:** Now let us talk about what I think is the most compelling feature: crisis alpha. What happens to trend following during market crashes?

[VISUAL: Title card "Crisis Alpha: The Ultimate Portfolio Insurance"]

**Alex:** Crisis alpha is the term coined by Kathryn Kaminski to describe trend following's remarkable property of generating positive returns during major market dislocations. Let me walk you through the mechanism.

**Sam:** Please.

**Alex:** When a crisis begins, there is typically a sudden initial shock -- think of the market dropping 5 percent in a few days. At this point, trend following systems are usually still long equities, so they LOSE money. This is the cost phase.

**Sam:** That does not sound like crisis protection.

**Alex:** Patience. As the decline continues -- say over several weeks -- the trend signals start to flip. Moving averages cross, breakout signals trigger. The systems move from long to flat to short. Simultaneously, other trends emerge: bonds rally as investors flee to safety, certain commodities sell off, the dollar may strengthen. The trend following system goes long bonds, short equities, short certain commodities.

[VISUAL: Timeline showing the five phases of crisis alpha: initial shock, signal flip, trend development, crisis deepening, recovery]

**Sam:** So the system needs time to adapt.

**Alex:** Exactly. And this is the key insight. The longer and more sustained the crisis, the more profitable trend following becomes. During the 2008 financial crisis, which played out over 18 months, trend following strategies returned approximately 18 percent while the S&P 500 lost 57 percent. During the dot-com crash, which lasted nearly three years, trend following returned about 28 percent cumulatively.

**Sam:** What about COVID? That was a crash but also a very quick recovery.

**Alex:** COVID is the perfect counter-example. The crash from peak to trough happened in just five weeks -- the fastest 30 percent decline in stock market history. Trend following systems barely had time to flip from long to short before the market reversed sharply upward. The result: managed futures lost about 3 percent during COVID, which is essentially flat. Not a disaster, but not the crisis alpha we saw in 2008.

[VISUAL: Side-by-side comparison charts of trend following vs S&P 500 during GFC 2008 and COVID 2020]

**Sam:** So trend following protects against long, grinding bear markets but not flash crashes.

**Alex:** That is the right way to think about it. And here is the important corollary: the truly dangerous bear markets -- the ones that destroy retirement portfolios and force people to sell at the bottom -- are almost always the extended ones. The GFC. The dot-com crash. These lasted months to years and caused 40 to 60 percent losses. Quick crashes with quick recoveries, like COVID, are traumatic but not financially devastating if you stay invested. Trend following provides the most protection precisely when you need it most.

**Sam:** What about 2022? I heard that was a standout year for managed futures.

[VISUAL: Title card "2022: Trend Following's Finest Hour"]

**Alex:** 2022 may have been the most important year in the history of trend following, in terms of proving its value to the investing world. Here is why: in 2022, stocks fell 25 percent, and bonds -- which are supposed to protect you during stock declines -- also fell, losing about 13 percent. The traditional 60/40 portfolio had its worst year in decades. Meanwhile, trend following strategies returned approximately 24 percent.

**Sam:** Positive 24 percent while both stocks and bonds lost money? How?

**Alex:** Multiple sustained trends across asset classes, all in the same direction. Interest rates rose steadily throughout the year as the Federal Reserve hiked aggressively. This created a strong, persistent short-bond trend. Energy commodities spiked due to the Russia-Ukraine conflict. The US dollar strengthened against nearly every other currency. And equities declined gradually over many months, giving trend following systems plenty of time to establish short positions. The key word is "gradually" -- these were not sudden shocks but sustained, multi-month trends.

[ANIMATION: animation/week51_trend_following.py -- Animated portfolio simulation showing positions across asset classes during 2022: short bonds building over time, long energy commodities, long USD, short equities. Each position's contribution to the overall return is shown as a stacking bar chart that grows throughout the year.]

**Sam:** So 2022 was the year that proved trend following works when nothing else does.

**Alex:** Precisely. And it vindicated the investors who maintained their managed futures allocation through the difficult 2010s, when trend following underperformed and many institutions abandoned it. The lesson is clear: crisis protection strategies only work if you hold them through the calm periods too. You cannot time when the crisis will come.

**Sam:** Let us talk about practical implementation. How can a regular investor access this?

[VISUAL: Title card "Implementation: ETFs and Beyond"]

**Alex:** The two most prominent options are DBMF and KMLM. DBMF, from iMGP, uses a factor-based approach to replicate the returns of the top 20 CTAs. It has the largest AUM at about 3 billion dollars and the broadest market coverage. KMLM, from KFA Mount Lucas, tracks a rules-based trend following index across commodities, currencies, and bonds. Both charge around 85 to 95 basis points, which sounds expensive but is far cheaper than the traditional CTA fee structure of 2 percent management fee plus 20 percent performance fee.

**Sam:** Which one should someone choose?

**Alex:** If picking one, I would lean toward DBMF because it includes equity index futures in its replication, while KMLM does not. This means DBMF can go short equity indexes during a bear market, which is a significant component of crisis alpha. If you have enough allocation to split between two products -- say, a 10 percent allocation to managed futures -- I would do 7 percent in DBMF and 3 percent in KMLM to get strategy diversification.

**Sam:** What is a reasonable allocation?

**Alex:** Research from AQR, Man Group, and other leading quant firms consistently points to 10 to 15 percent as the sweet spot. At this level, you get meaningful drawdown reduction -- potentially shaving 8 to 10 percentage points off the worst drawdown -- while maintaining strong portfolio returns. Below 5 percent, the impact is too small to matter. Above 20 percent, you start to feel significant drag during bull markets.

[VISUAL: Chart showing the efficient frontier with and without managed futures, demonstrating the improvement in risk-return trade-off]

**Sam:** What about behavioral challenges? You mentioned that trend following feels uncomfortable.

**Alex:** This might be the most important practical consideration. During a strong equity bull market -- like 2013 or 2019, when the S&P 500 returned 30-plus percent -- your managed futures allocation might return 3 to 5 percent. Every quarterly statement, you will see this allocation dragging on your total portfolio return. The temptation to eliminate it and go all-in on equities is enormous.

**Sam:** How do you stay disciplined?

**Alex:** Three things. First, mentally reframe the allocation as insurance. You do not cancel your homeowner's insurance because your house did not burn down last year. Second, look at your portfolio's risk metrics, not just returns. The Sharpe ratio, maximum drawdown, and volatility of the portfolio WITH managed futures is better than without, even if the raw return is slightly lower in bull markets. Third, remember 2008 and 2022. Those are the years that define long-term wealth. If managed futures reduce your drawdown from 50 percent to 30 percent in the next crisis, you need a 43 percent gain to recover from 30 percent versus a 100 percent gain from 50 percent. That difference compounds over a lifetime.

[VISUAL: Recovery math comparison: 30% drawdown needs 43% to recover vs 50% drawdown needs 100% to recover]

**Sam:** Let us talk about the long-term picture. Has trend following always worked?

**Alex:** Remarkably, yes. Research going back to the 1800s shows positive trend following returns across every multi-decade period. The strategy has survived world wars, the Great Depression, multiple financial crises, the transition from floor trading to electronic markets, and the rise of algorithmic trading. It has been profitable for over 100 years.

**Sam:** Why has it not been arbitraged away in all that time?

**Alex:** Because the barriers to implementation are structural and psychological, not informational. Everyone *knows* that trends exist. But executing a trend following strategy requires trading dozens of markets simultaneously, managing leverage, operating globally, and maintaining discipline through inevitable drawdowns. Most investors -- including most professionals -- cannot do this consistently. Additionally, trend following profits from behavioral biases that are deeply wired into human psychology: anchoring, herding, loss aversion. As long as humans are involved in markets, trends will exist.

[ANIMATION: animation/week51_trend_following.py -- Historical timeline animation showing trend following returns by decade from the 1880s to 2020s, with major historical events marked. The visual shows that the strategy has been consistently profitable across radically different market regimes and eras.]

**Sam:** How does managed futures fit with everything else we have learned in this course?

**Alex:** That is the perfect segue to next week's integration lesson, but I will preview it. Think of your portfolio as having multiple layers. The core is your market exposure -- stocks and bonds. Factor tilts add a modest return premium with controlled tracking error. Options strategies provide income and tail hedging. And managed futures provide the ultimate diversifier -- a strategy that is genuinely uncorrelated to everything else and provides positive returns during the crises that threaten the rest of your portfolio.

**Sam:** So managed futures is the portfolio's insurance policy?

**Alex:** Insurance policy with a positive expected return. Most insurance costs money -- you pay premiums and hope to never collect. Managed futures, historically, have generated positive returns on average while ALSO providing crisis protection. It is not a free lunch -- you endure periods of underperformance as the cost -- but over a full market cycle, it adds value on both the return and risk dimensions.

**Sam:** This has been incredibly insightful. I feel like managed futures is the missing piece that most portfolios lack.

**Alex:** It absolutely is. The largest, most sophisticated institutional investors -- Norwegian Government Pension Fund, Yale Endowment, Australian super funds -- have been allocating to managed futures for decades. It is only recently that retail investors have gained access through ETFs. Take advantage of it.

**Sam:** Next week is the grand finale. We bring everything together.

**Alex:** Week 52: Portfolio Integration -- putting all 52 weeks of learning into a single, coherent investment framework. See you then.

[VISUAL: End card with lesson summary, ETF comparison table, and recommended readings]

---
