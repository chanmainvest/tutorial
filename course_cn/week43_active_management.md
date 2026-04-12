<!-- 此文件需要翻译为简体中文 -->
<!-- This file needs translation to Simplified Chinese -->

# Week 43: Active Portfolio Management

---

## Reading Section

### a) Why This Is Important

Active management -- the attempt to outperform a benchmark through security selection, factor timing, or tactical allocation -- is the most debated topic in finance. Trillions of dollars in fees are at stake. The active management industry collects over $100 billion per year in fees from investors who believe their managers can beat the market. Understanding the tools for evaluating active management is critical for every investor, whether you manage your own money or hire someone to do it.

Understanding active management metrics is critical because:

- **You need to know if your manager (or you) are adding value**: Beating the market in a single year proves nothing. A monkey throwing darts at a stock page will beat the market roughly half the time. The metrics in this lesson -- alpha, information ratio, active share -- distinguish genuine skill from luck over meaningful time periods.
- **Most active managers underperform after fees**: The SPIVA (S&P Indices Versus Active) scorecard consistently shows that 80-90% of active large-cap managers underperform the S&P 500 over 15-year periods. If you are paying for active management, you need tools to evaluate whether your manager is in the skilled minority or the underperforming majority.
- **Understanding performance attribution reveals whether outperformance is genuine**: A manager who beat the benchmark by 3% might have done so through brilliant stock picking, or by simply overweighting a sector that happened to do well. Performance attribution decomposes returns into allocation decisions and selection decisions, revealing the true source of performance.
- **The Fundamental Law of Active Management connects skill, breadth, and performance**: This framework helps you understand why some strategies have higher potential than others, and why adding more independent bets can be more valuable than increasing the accuracy of each bet.
- **Active share predicts future performance better than past performance does**: Research shows that managers with truly differentiated portfolios (high active share) have a better chance of outperforming than closet indexers who charge active fees for index-like portfolios. Knowing how to measure active share protects you from paying fees for nothing.

This lesson will teach you the complete toolkit for evaluating active management: alpha, beta, tracking error, information ratio, active share, the Fundamental Law of Active Management, and multi-factor performance attribution.

---

### b) What You Need to Know

#### 1. Alpha and Beta: The Foundation

Alpha and beta are the two most fundamental concepts in active management evaluation. Beta measures market exposure. Alpha measures everything else -- the value added (or destroyed) by active decisions.

```
ALPHA AND BETA: DEFINITIONS

The Capital Asset Pricing Model (CAPM):
  E(Rp) = Rf + Beta x (Rm - Rf) + Alpha

Where:
  E(Rp) = Expected portfolio return
  Rf    = Risk-free rate
  Beta  = Sensitivity to market returns
  Rm    = Market return
  Alpha = Excess return not explained by market exposure

BETA: How much does the portfolio move with the market?
  Beta = 1.0: Moves exactly with the market
  Beta = 1.2: Moves 20% more than the market
  Beta = 0.8: Moves 20% less than the market
  Beta = 0.0: Unrelated to market movement
  
ALPHA: What return is left after accounting for beta?
  Alpha > 0: Manager added value beyond market exposure
  Alpha = 0: Manager's return is fully explained by beta
  Alpha < 0: Manager destroyed value relative to risk taken

EXAMPLE:
  Portfolio return:     +12%
  Risk-free rate:       4%
  Market return:        +10%
  Portfolio beta:       1.2

  Expected return = 4% + 1.2 x (10% - 4%) = 11.2%
  Alpha = 12% - 11.2% = +0.8%

  The portfolio returned 12%, but 11.2% was explained
  by market exposure (beta of 1.2). Only 0.8% was
  genuine value-added -- alpha.
```

```
ALPHA INTERPRETATION: CRITICAL NUANCES

IS ALPHA STATISTICALLY SIGNIFICANT?
  
  A +0.8% alpha might sound good, but is it real or luck?
  
  To determine significance, you need:
  - The t-statistic of alpha
  - t = alpha / standard error of alpha
  - t > 2.0 is statistically significant at 95% confidence
  
  ROUGH RULE OF THUMB:
  ┌─────────────────────────────────────────────────┐
  │  To have a significant alpha at 95% confidence: │
  │                                                 │
  │  Annual alpha    Years of data needed           │
  │  ───────────────────────────────────────────    │
  │  1%              ~16 years                      │
  │  2%              ~8 years                       │
  │  3%              ~5 years                       │
  │  5%              ~3 years                       │
  │                                                 │
  │  Most fund managers do not have 16 years of     │
  │  data. This is why proving 1% annual alpha      │
  │  is extraordinarily difficult statistically.    │
  └─────────────────────────────────────────────────┘

  IMPLICATION: Most observed alpha is consistent
  with randomness. A manager with 3 years of 2%
  annual alpha CANNOT be distinguished from luck.
  This does not mean there is no skill -- it means
  the evidence is insufficient to prove it.

ALPHA IS NET-OF-FEES:
  Gross alpha (before fees): +1.5%
  Management fee:            -1.0%
  Net alpha:                 +0.5%
  
  Many funds generate positive gross alpha but negative
  net alpha. The manager has skill, but not enough to
  overcome their fee. You, the investor, are worse off
  than indexing.
```

#### 2. Tracking Error

Tracking error measures how much a portfolio's returns deviate from its benchmark. It is the standard deviation of the difference between portfolio returns and benchmark returns.

```
TRACKING ERROR: DEFINITION AND CALCULATION

Tracking Error (TE) = StdDev(Rp - Rb)

Where:
  Rp = Portfolio return
  Rb = Benchmark return

EXAMPLE: Monthly returns over 12 months
  Month    Portfolio    Benchmark    Difference
  ─────────────────────────────────────────────
  Jan      +2.1%       +1.8%        +0.3%
  Feb      -1.5%       -1.2%        -0.3%
  Mar      +3.2%       +2.5%        +0.7%
  Apr      +0.8%       +1.1%        -0.3%
  May      -0.5%       -0.2%        -0.3%
  Jun      +1.9%       +1.5%        +0.4%
  Jul      +2.8%       +2.0%        +0.8%
  Aug      -2.1%       -1.8%        -0.3%
  Sep      +1.2%       +0.9%        +0.3%
  Oct      +0.5%       +0.4%        +0.1%
  Nov      +3.1%       +2.3%        +0.8%
  Dec      +1.5%       +1.2%        +0.3%
  ─────────────────────────────────────────────
  Average difference: +0.18% per month
  StdDev of differences: 0.40% per month
  Annualized TE: 0.40% x sqrt(12) = 1.39%

TRACKING ERROR INTERPRETATION:

  TE Range      Description            Portfolio Type
  ──────────────────────────────────────────────────────
  0%            Perfect index match    Index fund
  0.1-0.5%     Near-index             Enhanced index
  0.5-2%       Low active risk        Core active fund
  2-5%         Moderate active risk   Typical active fund
  5-10%        High active risk       Concentrated fund
  10-15%       Very high active risk  Hedge fund / 
                                      sector fund
  > 15%        Extreme active risk    Highly concentrated
                                      or leveraged
```

```
TRACKING ERROR: WHAT IT REVEALS

TRACKING ERROR AS A RISK BUDGET FOR ACTIVE DECISIONS:

  Total portfolio risk = Benchmark risk + Active risk
  
  If benchmark volatility = 16%
  and tracking error = 4%
  
  Portfolio volatility = approx sqrt(16^2 + 4^2)
                       = approx 16.5%
  
  The active decisions add only 0.5% to total volatility
  but can significantly impact returns (positively or
  negatively).

WHY TRACKING ERROR MATTERS:

  High TE:
    ┌──────────────────────────────────────────────┐
    │  Portfolio differs significantly from benchmark │
    │  + Can generate large alpha (positive or negative)│
    │  + Truly active management                       │
    │  - Higher risk of large underperformance         │
    │  - May not match benchmark in any given period   │
    └──────────────────────────────────────────────┘

  Low TE:
    ┌──────────────────────────────────────────────┐
    │  Portfolio closely tracks benchmark              │
    │  + Returns predictably near benchmark            │
    │  + Low risk of large underperformance            │
    │  - Limited ability to generate alpha             │
    │  - May be a "closet indexer" charging active fees│
    └──────────────────────────────────────────────┘
    
  CLOSET INDEXER WARNING:
  If TE < 2% and the fund charges 0.8%+ in fees,
  the manager is effectively charging active fees
  to deliver near-index returns. This is the worst
  outcome for investors: paying for active management
  but getting passive results minus fees.
```

#### 3. Information Ratio

The information ratio combines alpha and tracking error into a single measure of risk-adjusted active performance. It answers: "How much alpha did the manager generate per unit of active risk taken?"

```
INFORMATION RATIO: DEFINITION

  IR = Alpha / Tracking Error

  IR = (Portfolio return - Benchmark return) / TE

INTERPRETATION:
  IR > 0.5:   Very good (top quartile active manager)
  IR > 0.75:  Excellent (top decile)
  IR > 1.0:   Exceptional (extremely rare, sustained)
  IR = 0:     No value added
  IR < 0:     Value destroyed (worse than index)

EXAMPLE:
  Manager A: Alpha = 2%, TE = 6%   -> IR = 0.33
  Manager B: Alpha = 1%, TE = 2%   -> IR = 0.50
  Manager C: Alpha = 3%, TE = 8%   -> IR = 0.38
  
  Manager B has the highest IR despite the lowest alpha.
  Per unit of active risk, Manager B is the most efficient.
  
  KEY INSIGHT: IR measures the EFFICIENCY of active
  management, not the magnitude. A high IR means the
  manager is generating alpha without taking excessive
  active risk.

COMPARING MANAGERS USING IR:

  ┌──────────────────────────────────────────────────┐
  │  Manager     Alpha   TE      IR      Assessment  │
  │──────────────────────────────────────────────────│
  │  Fund A      +3.0%   12%     0.25    Inefficient │
  │  Fund B      +1.5%   3%      0.50    Efficient   │
  │  Fund C      +2.0%   5%      0.40    Moderate    │
  │  Fund D      -0.5%   2%     -0.25    Destroying  │
  │  Fund E      +0.8%   8%      0.10    Not worth it│
  │  Index Fund   0.0%   0%      N/A     Baseline    │
  └──────────────────────────────────────────────────┘
  
  Fund B is the best choice: modest alpha but very
  consistent, with low tracking error.
  
  Fund A has the highest alpha but also the most risk.
  Fund E takes significant active risk for negligible alpha.
  Fund D is actively destroying value.
```

```
IR AND THE INFORMATION COEFFICIENT:

  The IR can be decomposed:
  
  IR = IC x sqrt(BR)
  
  Where:
    IC = Information Coefficient (correlation between
         forecasts and actual outcomes, a measure of SKILL)
    BR = Breadth (number of independent bets per year)
  
  This is the FUNDAMENTAL LAW OF ACTIVE MANAGEMENT.
  We will cover it in detail in section 5.
  
  PREVIEW:
    A manager with modest skill (IC = 0.05)
    making many independent bets (BR = 100)
    can achieve: IR = 0.05 x sqrt(100) = 0.50
    
    A manager with higher skill (IC = 0.10)
    making few bets (BR = 25)
    achieves: IR = 0.10 x sqrt(25) = 0.50
    
    SAME IR, different approach.
    Skill and breadth are substitutes.
```

#### 4. Active Share

Active share measures how different a portfolio is from its benchmark. It is the percentage of the portfolio that differs from the benchmark holdings.

```
ACTIVE SHARE: DEFINITION AND CALCULATION

Active Share = (1/2) x Sum of |Wp,i - Wb,i|
               for all securities i

Where:
  Wp,i = Weight of security i in the portfolio
  Wb,i = Weight of security i in the benchmark

EXAMPLE:
  Security    Portfolio Weight    Benchmark Weight    |Difference|
  ─────────────────────────────────────────────────────────────
  AAPL        8%                  7%                  1%
  MSFT        6%                  6%                  0%
  GOOG        0%                  4%                  4%
  AMZN        10%                 3%                  7%
  NVDA        12%                 5%                  7%
  META        0%                  2%                  2%
  JPM         4%                  2%                  2%
  XYZ Corp    5%                  0%                  5%
  (other)     55%                 71%                 --
  Sum of |diff| for all positions:                    52%
  Active Share = 52% / 2 = 26%
  
  NOTE: This is a simplified example. In practice,
  the sum is over ALL securities in both the portfolio
  and the benchmark (potentially thousands).

ACTIVE SHARE CATEGORIES:

  Active Share    Category              Implication
  ────────────────────────────────────────────────────
  0-20%           Closet indexer        Paying active fees
                                        for passive returns
  
  20-40%          Factor bet            Mild tilt but
                                        mostly indexing
  
  40-60%          Moderately active     Some differentiation
  
  60-80%          Distinctly active     Meaningfully different
                                        from benchmark
  
  80-100%         Highly active         Very different portfolio
                                        (stock picker or
                                         concentrated fund)
```

```
ACTIVE SHARE AND PERFORMANCE: THE RESEARCH

Cremers & Petajisto (2009) landmark study found:

  ┌─────────────────────────────────────────────────────┐
  │  ACTIVE SHARE vs. FUTURE PERFORMANCE                │
  │                                                     │
  │  Funds with Active Share > 80%:                     │
  │    Average outperformance: +1.5% per year           │
  │    (before fees; modest after fees)                 │
  │                                                     │
  │  Funds with Active Share 20-60%:                    │
  │    Average outperformance: -0.3% per year           │
  │    (closet indexers underperform by their fee)      │
  │                                                     │
  │  Funds with Active Share < 20%:                     │
  │    Average outperformance: -1.0% per year           │
  │    (essentially index minus fees)                   │
  │                                                     │
  │  KEY INSIGHT:                                       │
  │  High active share is necessary but not sufficient  │
  │  for outperformance. You must be different AND      │
  │  right. Being different and wrong is disastrous.    │
  └─────────────────────────────────────────────────────┘

ACTIVE SHARE + TRACKING ERROR MATRIX:

                    Low TE              High TE
                    (<4%)               (>4%)
                ┌────────────────┬────────────────┐
  High Active   │ Diversified    │ Concentrated   │
  Share (>60%)  │ stock picker   │ stock picker   │
                │ BEST CATEGORY  │ High risk/     │
                │ for alpha      │ high reward    │
                ├────────────────┼────────────────┤
  Low Active    │ Closet         │ Factor bet     │
  Share (<60%)  │ indexer        │ (sector/style  │
                │ WORST CATEGORY │  rotation)     │
                │ fees for nothing│               │
                └────────────────┴────────────────┘

  The combination of HIGH active share and LOW tracking
  error identifies "diversified stock pickers" -- managers
  who pick many different stocks from the benchmark but
  whose overall portfolio risk is similar to the benchmark.
  Research shows this is the group most likely to outperform.
```

#### 5. The Fundamental Law of Active Management

The Fundamental Law, developed by Grinold and Kahn, provides a theoretical framework for understanding the drivers of active management performance.

```
THE FUNDAMENTAL LAW OF ACTIVE MANAGEMENT

  IR = IC x sqrt(BR)

Where:
  IR = Information Ratio (risk-adjusted alpha)
  IC = Information Coefficient (skill per bet)
  BR = Breadth (number of independent bets per year)

IC (INFORMATION COEFFICIENT):
  Measures the correlation between your forecasts and
  actual outcomes. Ranges from -1 to +1.
  
  IC = 0.00: No forecasting ability (random)
  IC = 0.05: Modest skill (typical active manager)
  IC = 0.10: Good skill (above-average manager)
  IC = 0.15: Excellent skill (top-tier manager)
  IC = 0.20: Exceptional skill (extremely rare)
  
  NOTE: Even IC = 0.05 represents meaningful skill.
  It means your forecasts are slightly better than
  random. Over many bets, this compounds.

BR (BREADTH):
  The number of INDEPENDENT investment decisions per year.
  
  KEY WORD: INDEPENDENT.
  Buying 50 tech stocks is NOT 50 independent bets.
  These stocks are highly correlated, so the effective
  breadth might be 5-10 independent bets, not 50.
  
  True breadth comes from:
  - Investing across uncorrelated sectors
  - Investing across different countries
  - Investing across different time horizons
  - Using different types of strategies
  
EXAMPLE CALCULATIONS:

  Stock picker (IC=0.05, BR=100):
    IR = 0.05 x sqrt(100) = 0.50     (Very good)
  
  Macro trader (IC=0.15, BR=10):
    IR = 0.15 x sqrt(10) = 0.47      (Good)
  
  Sector rotator (IC=0.08, BR=30):
    IR = 0.08 x sqrt(30) = 0.44      (Good)
  
  Concentrated fund (IC=0.10, BR=15):
    IR = 0.10 x sqrt(15) = 0.39      (Moderate)
```

```
FUNDAMENTAL LAW: IMPLICATIONS

IMPLICATION 1: BREADTH AND SKILL ARE SUBSTITUTES
  ┌─────────────────────────────────────────────────┐
  │  To achieve IR = 0.50:                          │
  │                                                 │
  │  IC = 0.05 needs BR = 100 (many bets, low skill)│
  │  IC = 0.10 needs BR = 25  (fewer bets, more skill)│
  │  IC = 0.25 needs BR = 4   (very few bets, very  │
  │                             high skill)          │
  │                                                 │
  │  If you have modest skill, make many bets.       │
  │  If you have high skill, you can concentrate.    │
  │  Most investors should assume modest skill and   │
  │  make many independent bets.                     │
  └─────────────────────────────────────────────────┘

IMPLICATION 2: DIVERSIFICATION HELPS EVEN SKILLED MANAGERS
  
  Skill (IC)      BR = 10    BR = 25    BR = 50    BR = 100
  ──────────────────────────────────────────────────────────
  IC = 0.05       0.16       0.25       0.35       0.50
  IC = 0.10       0.32       0.50       0.71       1.00
  IC = 0.15       0.47       0.75       1.06       1.50
  
  Doubling breadth is equivalent to multiplying skill
  by 1.41 (sqrt(2)). It is often easier to find more
  independent bets than to get significantly better
  at forecasting.

IMPLICATION 3: CORRELATION REDUCES EFFECTIVE BREADTH
  
  If you make 50 stock picks but they are all in tech:
    Average correlation between picks: 0.6
    Effective breadth = N / (1 + (N-1) x rho)
                      = 50 / (1 + 49 x 0.6)
                      = 50 / 30.4
                      = 1.6 independent bets
  
  50 correlated bets = 1.6 independent bets!
  
  LESSON: Diversification across uncorrelated
  opportunities is FAR more valuable than taking
  many correlated bets.
```

#### 6. Performance Attribution

Performance attribution decomposes a portfolio's return relative to its benchmark into specific decision categories. It answers: "WHERE did the outperformance or underperformance come from?"

```
BRINSON ATTRIBUTION MODEL

The Brinson model decomposes active return into:
  1. ALLOCATION EFFECT: Over/underweighting sectors
  2. SELECTION EFFECT: Picking stocks within sectors
  3. INTERACTION EFFECT: Combination of allocation + selection

FORMULAS:
  Allocation = Sum of (Wp,s - Wb,s) x (Rb,s - Rb)
  Selection  = Sum of Wb,s x (Rp,s - Rb,s)
  Interaction = Sum of (Wp,s - Wb,s) x (Rp,s - Rb,s)

Where:
  Wp,s = Portfolio weight in sector s
  Wb,s = Benchmark weight in sector s
  Rp,s = Portfolio return in sector s
  Rb,s = Benchmark return in sector s
  Rb   = Total benchmark return

ALLOCATION EFFECT:
  Did overweighting winners and underweighting
  losers add value?
  
  If you overweighted tech (+5% vs benchmark)
  and tech outperformed, allocation effect is positive.
  
SELECTION EFFECT:
  Did picking stocks within each sector add value?
  
  If your tech stocks returned 15% while the benchmark's
  tech stocks returned 12%, selection effect is positive.

INTERACTION EFFECT:
  The cross-product of allocation and selection.
  Positive when you overweighted sectors where you
  also picked well.
```

```
PERFORMANCE ATTRIBUTION: WORKED EXAMPLE

Portfolio vs. S&P 500, annual returns

Sector       Port    Bench   Port    Bench    Bench
             Weight  Weight  Return  Return   Sector
                                              Return
─────────────────────────────────────────────────────
Technology   30%     28%     +18%    +15%     +15%
Healthcare   15%     13%     +8%     +10%     +10%
Financials   12%     13%     +12%    +11%     +11%
Energy       3%      4%      -5%     -3%      -3%
Cons Disc    15%     10%     +14%    +9%      +9%
Cons Staples 5%      7%      +5%     +6%      +6%
Industrials  10%     10%     +11%    +10%     +10%
Other        10%     15%     +7%     +8%      +8%
─────────────────────────────────────────────────────
TOTAL        100%    100%    +12.2%  +10.5%

Total active return = +1.7%

ATTRIBUTION DECOMPOSITION:

ALLOCATION EFFECT:
  Tech:     (30%-28%) x (15%-10.5%) = +0.09%
  Health:   (15%-13%) x (10%-10.5%) = -0.01%
  Finance:  (12%-13%) x (11%-10.5%) = -0.005%
  Energy:   (3%-4%)   x (-3%-10.5%) = +0.135%
  ConsDis:  (15%-10%) x (9%-10.5%)  = -0.075%
  ConsStap: (5%-7%)   x (6%-10.5%)  = +0.09%
  Indust:   (10%-10%) x (10%-10.5%) = 0%
  Other:    (10%-15%) x (8%-10.5%)  = +0.125%
  ─────────────────────────────────────────
  TOTAL ALLOCATION EFFECT:             +0.37%

SELECTION EFFECT:
  Tech:     28% x (18%-15%) = +0.84%
  Health:   13% x (8%-10%)  = -0.26%
  Finance:  13% x (12%-11%) = +0.13%
  Energy:   4%  x (-5%--3%) = -0.08%
  ConsDis:  10% x (14%-9%)  = +0.50%
  ConsStap: 7%  x (5%-6%)   = -0.07%
  Indust:   10% x (11%-10%) = +0.10%
  Other:    15% x (7%-8%)   = -0.15%
  ─────────────────────────────────────────
  TOTAL SELECTION EFFECT:              +1.01%

INTERACTION EFFECT:
  (Remaining: 1.7% - 0.37% - 1.01% = +0.32%)

INTERPRETATION:
  ┌──────────────────────────────────────────────────┐
  │  Total outperformance:     +1.70%                │
  │                                                  │
  │  Allocation effect:        +0.37%  (22%)         │
  │  Selection effect:         +1.01%  (59%)         │
  │  Interaction effect:       +0.32%  (19%)         │
  │                                                  │
  │  CONCLUSION: Most of the outperformance came     │
  │  from stock SELECTION, not sector allocation.    │
  │  The manager is a stock picker, not a sector     │
  │  rotator. This is valuable information for       │
  │  evaluating whether the skill is sustainable.    │
  └──────────────────────────────────────────────────┘
```

#### 7. Multi-Factor Attribution

Modern performance attribution goes beyond the Brinson sector model to decompose returns by factor exposures.

```
MULTI-FACTOR ATTRIBUTION

Instead of sectors, decompose returns by factor:

  Portfolio return = Risk-free rate
                   + Market exposure
                   + Size exposure
                   + Value exposure
                   + Momentum exposure
                   + Quality exposure
                   + Alpha (residual)

EXAMPLE:
  Portfolio annual return:     +14.0%
  Risk-free rate:              +4.0%
  ───────────────────────────────────
  Excess return:               +10.0%

  Market (beta=1.1, mkt=+8%):  +8.8%
  Size (small cap tilt):        +0.5%
  Value (growth tilt):          -0.3%
  Momentum (momentum tilt):    +0.8%
  Quality (quality tilt):      +0.4%
  ───────────────────────────────────
  Factor-explained return:     +10.2%
  
  Residual alpha:              -0.2%

  INTERPRETATION:
  ┌────────────────────────────────────────────────┐
  │  This manager appears to have returned +14%,   │
  │  beating the market's +12%.                    │
  │                                                │
  │  But factor decomposition reveals:             │
  │  - Higher market beta explains most excess     │
  │  - Momentum and quality tilts added returns    │
  │  - After accounting for ALL factor exposures,  │
  │    the residual alpha is actually NEGATIVE     │
  │                                                │
  │  CONCLUSION: No genuine stock-picking skill.   │
  │  The "outperformance" is entirely explained    │
  │  by systematic factor exposures that could be  │
  │  replicated cheaply with factor ETFs.          │
  └────────────────────────────────────────────────┘
```

```
FACTOR ATTRIBUTION DIAGRAM

  Total excess return: +10.0%
  
  ┌──────────────────────────────────────────────┐
  │ ████████████████████████████████████░░░░░░░  │
  │ Market                              Other    │
  │ +8.8%                              factors   │
  │ (88% of excess return)                       │
  └──────────────────────────────────────────────┘
  
  Zooming into "Other factors":
  ┌──────────────────────────────────────────────┐
  │ ████ ░░░ ████ ████ ▓▓▓▓                     │
  │ Size Val  Mom  Qual Alpha                    │
  │+0.5% -0.3% +0.8% +0.4% -0.2%              │
  └──────────────────────────────────────────────┘
  
  Most of the return is from MARKET EXPOSURE (beta).
  The factor tilts add modest amounts.
  True alpha (stock selection skill) is negligible.

WHAT THIS MEANS FOR INVESTORS:

  Before factor attribution:
    "This fund beat the market by 2%! Great manager!"
  
  After factor attribution:
    "This fund has beta of 1.1 and tilts toward
     momentum and quality. The market exposure and
     factor tilts explain 102% of excess return.
     There is no alpha. I could replicate this with
     a market ETF + factor ETFs for 0.1% in fees
     instead of 0.8%."
```

#### 8. Evaluating Active Managers: A Complete Framework

```
ACTIVE MANAGER EVALUATION CHECKLIST

STEP 1: BASIC PERFORMANCE METRICS
  [ ] Total return vs. benchmark (3, 5, 10 years)
  [ ] Alpha (net of fees)
  [ ] Is alpha statistically significant? (t-stat > 2)
  [ ] Maximum drawdown vs. benchmark drawdown
  [ ] Performance in up markets vs. down markets

STEP 2: RISK-ADJUSTED METRICS
  [ ] Tracking error (how much active risk?)
  [ ] Information ratio (alpha per unit of active risk)
  [ ] Sharpe ratio vs. benchmark Sharpe ratio
  [ ] Upside capture ratio vs. downside capture ratio

STEP 3: PORTFOLIO CHARACTERISTICS
  [ ] Active share (how different from benchmark?)
  [ ] Number of holdings (concentrated or diversified?)
  [ ] Sector concentrations
  [ ] Factor exposures (style tilts)
  [ ] Portfolio turnover (high turnover = high costs)

STEP 4: ATTRIBUTION ANALYSIS
  [ ] Is outperformance from allocation or selection?
  [ ] Is it from factor tilts or stock picking?
  [ ] Is the alpha coming from a few lucky positions
      or broad-based skill?

STEP 5: QUALITATIVE FACTORS
  [ ] Is the manager investing their own money?
  [ ] Has the process been consistent over time?
  [ ] Has the fund gotten too large for the strategy?
  [ ] Is the team stable?
  [ ] Are fees reasonable for the active share?

COMBINING METRICS INTO A SCORECARD:

  Metric               Red Flag          Green Flag
  ─────────────────────────────────────────────────
  Alpha (5yr, net)     < 0%              > 1%
  IR                   < 0               > 0.40
  Active Share         < 30%             > 60%
  TE                   < 2% with high    2-8%
                       fees
  Attribution          All from factors  Genuine
                                         selection alpha
  Turnover             > 100%            < 50%
  Manager ownership    $0                > $1M
  Fee reasonableness   1%+ for low AS    < 0.5% or
                                         performance-based
```

---

### c) Common Misconceptions

**Misconception 1: "A fund that beat the market last year is a good fund."**

One year of outperformance is statistically meaningless. With thousands of active funds, hundreds will beat the market in any given year by pure chance. The probability that last year's winners will repeat next year is only slightly better than 50/50. You need at minimum 5 years of consistent outperformance, and ideally 10+, to begin distinguishing skill from luck. Even then, factor attribution is essential -- was the outperformance from genuine stock picking or from factor tilts that happened to work?

**Misconception 2: "Low tracking error means low risk."**

Low tracking error means the portfolio closely tracks its benchmark. This does not mean the portfolio is low risk -- it means it has low ACTIVE risk (risk of deviating from the benchmark). If the benchmark drops 40%, a low-tracking-error portfolio will also drop approximately 40%. Low tracking error is desirable only if the benchmark's risk is appropriate for you. An S&P 500 index fund with zero tracking error still has significant market risk.

**Misconception 3: "High active share guarantees outperformance."**

High active share is necessary but not sufficient. It means the portfolio is different from the benchmark -- but being different can mean being different in a bad way. A manager who avoids the best-performing stocks has high active share and underperforms dramatically. The research shows that high active share gives managers the OPPORTUNITY to outperform, but they must also have genuine skill (positive IC). High active share without skill is a recipe for large underperformance.

**Misconception 4: "Alpha is the manager's return minus the benchmark's return."**

This is a simplified version that ignores risk. True alpha adjusts for the portfolio's beta (and potentially other factor exposures). A portfolio that returned 15% when the benchmark returned 12% might have zero alpha if the portfolio has a beta of 1.3. The excess return is fully explained by taking more market risk, not by skillful stock picking. Always calculate risk-adjusted alpha.

**Misconception 5: "More holdings means more diversification and therefore better."**

More holdings increase diversification of stock-specific risk, which reduces tracking error. But this comes at a cost. Each additional holding dilutes the impact of the manager's best ideas. If a manager has genuine skill in picking 20 stocks, adding 80 mediocre stocks to "diversify" will actually REDUCE alpha while reducing tracking error. The Fundamental Law tells us that what matters is INDEPENDENT bets, not just more bets. 50 correlated tech stocks provide almost no diversification benefit.

**Misconception 6: "Performance attribution proves why a manager outperformed."**

Attribution tells you where returns came from but does not tell you whether the source was intentional. A manager might have overweighted energy because of a bullish thesis, or because they inherited a position and never sold it. Attribution shows the WHAT, not the WHY. Always combine attribution with qualitative understanding of the manager's process.

---

### d) Common Questions and Answers

**Q1: How do I calculate alpha and tracking error for my own portfolio?**

A: Download your portfolio's monthly returns and the benchmark's monthly returns for at least 36 months. Subtract the benchmark return from the portfolio return each month. The average of these differences (annualized) is approximately your alpha. The standard deviation of these differences (annualized by multiplying by sqrt(12)) is your tracking error. For true risk-adjusted alpha, regress your excess returns against the benchmark excess returns; the intercept of the regression is alpha and the slope is beta.

**Q2: What is a reasonable fee for active management given these metrics?**

A: The fee should be less than the expected gross alpha. If a manager has historically generated 2% gross alpha with an IR of 0.50, a fee of 0.8% leaves you with 1.2% net alpha -- reasonable. But if the gross alpha is only 1% and the fee is 0.8%, you are paying 80% of the value-added as fees and keeping only 0.2%. As a rough rule, fees should be no more than one-third to one-half of gross alpha. If you cannot estimate gross alpha, check active share. If active share is below 40%, the manager is a closet indexer and almost no fee is justified -- just buy an index fund.

**Q3: How long should I give a manager before judging their performance?**

A: At minimum, a full market cycle (typically 5-7 years, encompassing both bull and bear markets). Three years is the absolute minimum for any statistical reliability. Firing a manager after one bad year is usually a mistake, as even skilled managers underperform 30-40% of the time due to normal variance. However, you should fire a manager immediately if there are non-performance concerns: style drift, loss of key personnel, regulatory issues, or violations of stated investment guidelines.

**Q4: Is it better to have one concentrated manager or multiple diversified managers?**

A: Multiple managers reduce manager-specific risk but can create "di-worsification" -- the combined portfolio may look like an expensive index fund. The key metric is the active share of the COMBINED portfolio of managers. If you hire five active managers and their combined portfolio has active share below 30%, you have achieved index-like results at active management prices. Better approaches include: one high-conviction manager plus an index fund for the remainder, or multiple managers with uncorrelated styles (one value, one growth, one international).

**Q5: Does the Fundamental Law work in practice?**

A: The Fundamental Law is a useful conceptual framework, but it has limitations in practice. The assumption that all bets are independent is almost never true. Stock picks within the same sector are correlated, reducing effective breadth. The Information Coefficient is assumed to be constant across all bets, but in reality, some bets are better than others. Despite these limitations, the core insight is robust: diversify your active bets across uncorrelated opportunities and focus on having at least modest skill per bet.

**Q6: What should I look for in performance attribution?**

A: Look for consistency and intentionality. Good signs: selection alpha across multiple sectors (broad skill, not one lucky pick), consistent allocation effect (the manager has genuine macro/sector views), and alpha that does not disappear when factor exposures are accounted for. Bad signs: all alpha from one sector or one stock (concentrated luck), allocation alpha from one sector that happened to rally (unintentional exposure), and alpha that is fully explained by factor tilts (no genuine stock-picking skill).

**Q7: How do I know if I am a closet indexer in my own portfolio?**

A: Calculate your active share relative to a broad index like the S&P 500 or total market index. If more than 60% of your portfolio is in index funds or ETFs, and your individual stock picks collectively represent less than 30% of the portfolio, your active share is low. This is not necessarily bad -- it means your costs are low and your risk is benchmark-like. But if you are spending significant time researching individual stocks for only 10% of your portfolio, the effort may not be worth the potential impact.

---

---

## YouTube Script

**Week 43: Active Portfolio Management**

[VISUAL: Title card -- "Alpha, Beta, and the Art of Active Management"]

**Alex**: Today we tackle one of the most contentious topics in finance: does active management work? And how do you measure whether it is working?

**Sam**: This is the "stock picking versus index funds" debate?

**Alex**: It goes much deeper than that. We are going to cover the precise tools that professionals use to evaluate active management -- alpha, tracking error, information ratio, active share, the Fundamental Law of Active Management, and performance attribution.

**Sam**: Why do these matter for regular investors?

**Alex**: Because the active management industry collects over $100 billion a year in fees. If you own any actively managed fund, or if you pick individual stocks yourself, you need to know whether that activity is adding value or destroying it.

[VISUAL: SPIVA scorecard statistics]

**Sam**: And the statistics are not encouraging for active managers, right?

**Alex**: The SPIVA scorecard consistently shows that over 15-year periods, roughly 85-90% of US large-cap active managers underperform the S&P 500. But -- and this is important -- some managers DO outperform consistently. The tools we are learning today help you identify which ones.

**Sam**: Let us start at the beginning. Alpha and beta.

[VISUAL: "Alpha and Beta" section header]

**Alex**: Beta measures how much your portfolio moves with the market. A beta of 1 means your portfolio moves in lockstep with the market. Beta of 1.2 means you move 20% more -- you are up more in bull markets and down more in bear markets. Beta of 0.8 means you move 20% less.

**Sam**: And alpha?

**Alex**: Alpha is the return that is left over after you account for beta. Here is a critical example. A portfolio returns 15% in a year when the market returns 10%. Most people would say the manager outperformed by 5%. But if the portfolio has a beta of 1.3, the expected return based purely on market exposure was 4% plus 1.3 times 6%, which equals 11.8%.

[VISUAL: Alpha calculation worked through step by step]

**Sam**: So the manager's alpha is only 15% minus 11.8%, which is 3.2%, not 5%.

**Alex**: Exactly. And that is a generous example. Many managers who appear to beat the market have simply taken more market risk -- higher beta. Their alpha, after adjusting for risk, is zero or negative.

**Sam**: How do I know if alpha is real or just luck?

**Alex**: This is the hardest question in finance. The answer requires statistical significance testing. For a 1% annual alpha to be statistically significant at 95% confidence, you typically need about 16 years of data. For 2% alpha, about 8 years. For 3%, about 5 years.

[ANIMATION: animation/week43_alpha_significance.py -- Animated simulation showing 100 fund managers with zero true alpha (they are all coin flippers). Each manager runs for 1, 3, 5, 10, and 20 years. At each time horizon, the animation shows how many managers appear to have "significant" alpha. After 1 year, about 40-45 managers show positive alpha. After 3 years, about 30. After 5 years, about 20. After 10 years, about 10-12. After 20 years, about 5 managers still show positive alpha even though NONE of them have genuine skill. The point is made visually: even with zero skill, some managers will always look good by pure luck, and longer track records are needed to distinguish skill from luck.]

**Sam**: That is sobering. Even with NO skill, some managers will always appear to outperform just by chance.

**Alex**: And here is the cruel corollary. The fund industry has thousands of managers. If 5% of zero-skill managers appear to outperform over 10 years, and you have 5,000 managers, that is 250 managers who look skilled but are not. Separating the truly skilled from the lucky is extremely difficult.

**Sam**: Is it even possible?

**Alex**: Yes, but you need multiple tools, not just returns. That is where tracking error and information ratio come in.

[VISUAL: "Tracking Error and Information Ratio" section header]

**Alex**: Tracking error measures how much your portfolio's returns deviate from the benchmark. It is the standard deviation of the return difference. A tracking error of zero means you are an index fund. A tracking error of 5% means your monthly returns typically differ from the benchmark by about 1.4% in any given month.

**Sam**: And that tells me how active the manager is?

**Alex**: It tells you how much active RISK the manager is taking. And that is important because it is one thing to outperform by 2% with 3% tracking error -- that means the active bets were efficient. It is quite another to outperform by 2% with 12% tracking error -- that means the active bets were large and sloppy, and you just happened to get lucky.

**Sam**: So the ratio of alpha to tracking error matters.

**Alex**: That is exactly the information ratio. IR equals alpha divided by tracking error. It measures how much return you get per unit of active risk. Think of it as the Sharpe ratio for active management.

[VISUAL: Information ratio calculation and interpretation scale]

**Alex**: An IR above 0.5 is very good -- top quartile among active managers. Above 0.75 is excellent. Above 1.0 is exceptional and almost impossible to sustain over long periods.

**Sam**: What is a typical IR?

**Alex**: The median active manager has an IR near zero -- their alpha is negligible after fees. The top quartile has an IR around 0.3-0.5. Top decile is 0.5-0.8. If someone claims a sustained IR above 1.0, they are either Warren Buffett, Renaissance Technologies, or lying.

[VISUAL: Distribution of information ratios across active managers]

**Sam**: I want to understand active share. I have heard it mentioned as a way to identify closet indexers.

[VISUAL: "Active Share" section header]

**Alex**: Active share measures how different your portfolio is from the benchmark, position by position. It is calculated by summing the absolute differences between your portfolio weights and the benchmark weights for every security, then dividing by two.

**Sam**: Give me an example.

**Alex**: Say the benchmark has 7% in Apple, and your fund has 10% in Apple. That is a 3% difference. The benchmark has 4% in Google, and your fund has zero. That is a 4% difference. You do this for every stock in both the portfolio and the benchmark, sum up all the absolute differences, and divide by two. If your active share is 80%, it means 80% of your portfolio differs from the benchmark.

[VISUAL: Active share calculation example with several stocks]

**Sam**: What does research say about active share and performance?

**Alex**: The landmark Cremers and Petajisto study from 2009 divided funds into categories based on active share. Funds with active share above 80% -- truly differentiated portfolios -- outperformed their benchmarks by about 1.5% per year before fees. Funds with active share below 40% -- closet indexers -- underperformed by about the amount of their fee. They were charging for active management but delivering index-like returns.

**Sam**: So if you are going to be active, be REALLY active?

**Alex**: Yes, but with a caveat. High active share is necessary but not sufficient. Being different from the benchmark is only valuable if you are different in the RIGHT way. A manager who avoids the 10 best-performing stocks has high active share and terrible returns. You need high active share AND skill.

[ANIMATION: animation/week43_active_share.py -- Animated scatter plot comparing active share (x-axis) to future 5-year alpha (y-axis) for 500 simulated funds. The animation builds up over time, showing four quadrants: low active share with negative alpha (closet indexers, bottom left), low active share with small positive alpha (enhanced indexers, top left), high active share with negative alpha (unskilled stock pickers, bottom right), and high active share with positive alpha (skilled stock pickers, top right). The best-performing funds cluster in the top right, confirming that high active share is necessary for significant outperformance. But the bottom right quadrant also has many funds, showing that high active share without skill leads to large underperformance. A text annotation summarizes: "High active share gives you the opportunity to outperform -- and the risk of underperforming significantly."]

**Sam**: So the key combination is high active share plus genuine skill.

**Alex**: Exactly. And there is an even more useful matrix. Plot active share against tracking error. Funds with high active share but low tracking error are "diversified stock pickers" -- they pick many different stocks but the overall portfolio risk is similar to the benchmark. Research shows this is the category most likely to outperform. Funds with low active share and low tracking error are closet indexers. Funds with high active share and high tracking error are concentrated bets -- they can outperform hugely or underperform hugely.

[VISUAL: Active share vs. tracking error 2x2 matrix]

**Sam**: Now I want to understand the Fundamental Law. This sounds like it ties everything together.

[VISUAL: "The Fundamental Law of Active Management" section header]

**Alex**: The Fundamental Law, developed by Grinold and Kahn, is one of the most elegant frameworks in finance. It says: Information Ratio equals the Information Coefficient times the square root of Breadth. IR equals IC times square root of BR.

**Sam**: Break those components down.

**Alex**: The Information Coefficient, IC, measures your skill per bet. It is the correlation between your forecasts and actual outcomes. An IC of zero means your predictions are random. An IC of 0.05 means you have a very slight edge -- your predictions are slightly better than chance. An IC of 0.10 is quite good. An IC of 0.15 is exceptional.

**Sam**: Those sound really small.

**Alex**: They are. Even the best investors in the world have ICs in the 0.05 to 0.15 range. Nobody consistently predicts stock returns with high accuracy. But even a tiny edge, compounded over many bets, produces significant alpha.

**Sam**: And that is where breadth comes in.

**Alex**: Breadth, BR, is the number of independent bets per year. The key word is INDEPENDENT. If you buy 50 tech stocks, those are not 50 independent bets -- they are highly correlated. The effective breadth might be only 5-10.

[VISUAL: Formula with examples at different IC and BR combinations]

**Alex**: Here is the magic. A manager with modest skill -- IC of 0.05 -- making 100 independent bets achieves an IR of 0.05 times the square root of 100, which equals 0.50. That is a very good IR. A manager with twice the skill -- IC of 0.10 -- making only 25 bets achieves 0.10 times the square root of 25, which equals 0.50. Same IR, completely different approach.

**Sam**: So skill and breadth are substitutes.

**Alex**: Exactly. If you have modest forecasting ability -- which is what most investors have -- you should make MANY independent bets. Diversify across sectors, countries, and styles. Each bet on its own will not be impressively profitable, but the cumulative effect of many small edges is a strong information ratio.

**Sam**: And if you are Warren Buffett with higher skill per bet?

**Alex**: Then you can concentrate -- make fewer, larger bets and still achieve a strong IR. But most people overestimate their IC. They think they are Buffett when they are actually average. The safe strategy is to assume modest skill and diversify.

[VISUAL: Table showing IC/BR combinations and resulting IR]

**Sam**: This has a practical implication for me. I should spread my stock picks across different sectors and countries, not concentrate in what I know best?

**Alex**: Unless what you know best truly gives you an edge. But here is a reality check: if you pick 50 stocks all in the tech sector, your effective breadth is not 50. Because those stocks are correlated at about 0.5-0.7 with each other, your effective breadth is more like 5-8 independent bets. You have done a lot of research for very little diversification benefit.

**Sam**: Let us move to performance attribution. How do I figure out WHERE my returns came from?

[VISUAL: "Performance Attribution" section header]

**Alex**: Performance attribution decomposes your active return -- the difference between your portfolio and the benchmark -- into specific sources. The classic Brinson model splits it into allocation effect and selection effect.

**Sam**: What is the difference?

**Alex**: Allocation effect measures whether you added value by over- or underweighting sectors. If you overweighted technology and technology outperformed the market, your allocation effect in tech is positive. Selection effect measures whether you picked good stocks within each sector. If your tech stocks returned 18% while the benchmark's tech stocks returned 15%, your selection effect in tech is positive.

[VISUAL: Attribution example with sector-by-sector breakdown]

**Alex**: Let me walk through a real example. Say your portfolio returned 12.2% and the benchmark returned 10.5%. That is 1.7% outperformance. Attribution decomposes this as: 0.37% from sector allocation, 1.01% from stock selection, and 0.32% from the interaction between the two.

**Sam**: So most of the outperformance came from picking good stocks, not from overweighting the right sectors.

**Alex**: Exactly. And that distinction matters. Sector allocation is hard to repeat -- it requires macro forecasting, which is notoriously difficult. Stock selection tends to be more repeatable because it is based on company-level analysis. A manager whose outperformance comes primarily from selection is more likely to continue outperforming than one whose outperformance comes from a lucky sector bet.

**Sam**: What about factor attribution?

**Alex**: Factor attribution goes even deeper. Instead of asking "did the manager pick good stocks in tech?", it asks "is the outperformance explained by the manager's tilt toward growth stocks, or momentum stocks, or small caps?" This is crucial because factor tilts can be replicated cheaply with ETFs.

[ANIMATION: animation/week43_factor_attribution.py -- Animated waterfall chart showing a manager's 14% total return being decomposed step by step. The animation starts with the full 14% bar. First, the risk-free rate of 4% is separated out. Then market exposure (beta of 1.1 contributing 8.8%) is peeled away. Then size, value, momentum, and quality factor exposures are separated one by one, each showing their contribution. What remains at the end is the residual alpha -- in this case, approximately -0.2%. The animation emphasizes that the impressive-looking 14% total return and 2% "outperformance" versus the 12% market return is entirely explained by factor exposures. There is no genuine stock-picking alpha.]

**Sam**: That is devastating. The manager looked like a 2% outperformer, but after factor attribution, they actually have slightly negative alpha?

**Alex**: This is incredibly common. Studies show that a large majority of active fund "alpha" is actually factor exposure in disguise. The manager tilts toward momentum, or quality, or small caps, and when those factors perform well, the fund outperforms. When those factors reverse, the fund underperforms. The manager has no genuine stock-picking skill -- they are just a factor bet dressed up as active management.

**Sam**: And I could replicate that factor bet with cheap ETFs.

**Alex**: For about 0.1% in fees instead of 0.8% or 1.0%. This is one of the most important insights from modern finance: much of what the active management industry sells as "alpha" is actually "beta in disguise" -- systematic factor exposure that can be obtained far more cheaply.

**Sam**: So how do I use all of this practically?

[VISUAL: "Putting It All Together" section header]

**Alex**: Here is my framework for evaluating any active manager -- including yourself if you pick individual stocks.

**Alex**: Step one: look at alpha net of fees over at least 5 years, ideally 10. Is it positive? Is it statistically significant?

**Sam**: Most managers will fail at this step.

**Alex**: Correct. Step two: check the information ratio. An IR below 0.3 is not worth paying for. You can get similar results with an index fund and zero active risk.

**Alex**: Step three: check active share. If it is below 40%, you have a closet indexer. Do not pay active management fees for index-like returns.

**Alex**: Step four: run factor attribution. Is the alpha explained by factor tilts, or is there genuine residual stock-picking alpha? If it is all factor tilts, buy factor ETFs instead.

**Alex**: Step five: look at performance attribution. Is the alpha coming from broad-based stock selection across sectors, or from one or two lucky bets?

[VISUAL: Five-step evaluation framework as a flowchart]

**Sam**: If a manager passes all five steps, is it a good investment?

**Alex**: It is a CANDIDATE for investment. You still need to assess qualitative factors: is the manager investing their own money alongside clients? Has the process been consistent? Has the fund grown too large for its strategy? Are key personnel stable? But passing the quantitative tests is a prerequisite.

**Sam**: What percentage of active managers pass all five tests?

**Alex**: Generously? Maybe 5-10%. More realistically, 3-5%. The vast majority of active managers either have no alpha, are closet indexers, or have alpha that is fully explained by factor exposures.

**Sam**: So the default should be index funds?

**Alex**: For most investors, yes. The evidence overwhelmingly supports passive investing for the majority of a portfolio. BUT -- and this is important -- the fact that most active managers fail does not mean ALL active management is worthless. The small minority of genuinely skilled managers can add meaningful value. The tools we learned today help you identify them.

**Sam**: Let me summarize. Alpha measures value-added after adjusting for risk. Tracking error measures active risk. Information ratio is alpha per unit of tracking error. Active share measures portfolio differentiation. The Fundamental Law says IR equals skill times the square root of breadth. Performance attribution decomposes returns into allocation and selection. Factor attribution reveals whether alpha is genuine or just factor exposure.

**Alex**: Perfect. And the overarching message: be skeptical but not cynical. Most active management destroys value after fees. But the tools exist to separate the wheat from the chaff. Use them.

**Sam**: This has completely changed how I will evaluate fund managers -- and my own stock picks.

**Alex**: That is the goal. And do not forget to apply these tools to yourself. If you are spending 10 hours a week researching stocks and your portfolio has an information ratio near zero, your time might be better spent elsewhere. Index the core of your portfolio and concentrate your active bets where you have a genuine informational edge.

[VISUAL: "Next week: Market Microstructure"]

**Alex**: Next week we go inside the machine. We will learn about bid-ask spreads, market makers, order types, price impact, slippage, implementation shortfall, and dark pools. This is the plumbing of financial markets -- and understanding it can save you significant money on every trade you make.

**Sam**: From measuring performance to executing trades efficiently.

**Alex**: Exactly. All the alpha in the world does not help if you give it back in transaction costs. See you next week.

**Sam**: Thanks, Alex.

[VISUAL: End card with channel subscribe prompt and links to previous videos]
