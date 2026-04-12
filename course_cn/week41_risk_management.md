<!-- 此文件需要翻译为简体中文 -->
<!-- This file needs translation to Simplified Chinese -->

# Week 41: Portfolio Risk Management

---

## Reading Section

### a) Why This Is Important

Risk management is the single most important skill separating investors who survive from those who do not. It is not glamorous, it does not generate cocktail-party stories, and it rarely appears in headlines. But every catastrophic investment failure -- from Long-Term Capital Management to individual traders blowing up their accounts -- can be traced to a failure of risk management, not a failure of analysis.

Understanding risk management is critical because:

- **Position sizing determines your survival**: A brilliant trade thesis is worthless if you bet too much on it. The 2% rule, Kelly criterion, and other sizing frameworks exist because mathematically, even a strategy with 60% win rate will go bankrupt if positions are too large. Most retail investors have no systematic position sizing method at all, which means their survival is a matter of luck, not skill.
- **Stop-loss strategies protect capital from catastrophic draws**: Without a predefined exit plan, human psychology takes over. Investors hold losers hoping for recovery (loss aversion) and sell winners too early (disposition effect). A disciplined stop-loss strategy removes emotion from the most critical decision: when to exit a losing position.
- **Risk budgeting turns vague diversification into a precise framework**: Saying "do not put all your eggs in one basket" is useless advice without quantification. Risk budgeting allocates specific risk limits across asset classes, strategies, and time horizons. It answers the question: "How much can I afford to lose in each area before it threatens my overall financial plan?"
- **Scenario analysis prepares you for events the market says are impossible**: Markets consistently underestimate the probability of extreme events. Scenario analysis forces you to ask: "What happens to my portfolio if the S&P drops 40% in two months? What if interest rates spike 300 basis points? What if my largest holding goes to zero?" If you cannot answer these questions, you do not understand your portfolio.
- **Risk management is a process, not a product**: You cannot buy risk management. It is not an ETF, a hedge fund, or a software tool. It is a daily discipline of measuring, monitoring, and adjusting exposures. The best investors in the world -- Renaissance Technologies, Bridgewater, Citadel -- spend more time on risk management than on idea generation.

This lesson will teach you the core frameworks of professional risk management, adapted for individual investors. You will learn how to size positions, set stops, budget risk, run scenario analyses, and build a risk management process that protects your capital while allowing it to grow.

---

### b) What You Need to Know

#### 1. Position Sizing: The 2% Rule

Position sizing is the process of determining how many shares, contracts, or dollars to allocate to a single trade or investment. It is arguably the most impactful decision you make as an investor, yet most people give it almost no thought.

The 2% Rule states: never risk more than 2% of your total portfolio on any single trade.

```
THE 2% RULE -- MECHANICS

Portfolio value: $100,000
Maximum risk per trade: 2% = $2,000

EXAMPLE: Buying stock XYZ at $50 with a stop-loss at $45
  Risk per share: $50 - $45 = $5
  Maximum shares: $2,000 / $5 = 400 shares
  Position size: 400 x $50 = $20,000 (20% of portfolio)

  NOTE: The position SIZE is 20%, but the RISK is only 2%.
  These are different concepts.

EXAMPLE: Buying stock ABC at $200 with a stop-loss at $180
  Risk per share: $200 - $180 = $20
  Maximum shares: $2,000 / $20 = 100 shares
  Position size: 100 x $200 = $20,000 (20% of portfolio)

EXAMPLE: Buying stock DEF at $30 with a stop-loss at $27
  Risk per share: $30 - $27 = $3
  Maximum shares: $2,000 / $3 = 666 shares
  Position size: 666 x $30 = $19,980 (20% of portfolio)

KEY INSIGHT:
  The tighter your stop-loss, the more shares you can buy.
  The wider your stop-loss, the fewer shares you can buy.
  But the dollar risk stays constant at $2,000.
```

Why 2%? Because it ensures survival through losing streaks.

```
SURVIVAL ANALYSIS: WHY 2% WORKS

Starting portfolio: $100,000
Risk per trade: 2% ($2,000)

Consecutive       Portfolio      Cumulative
Losses            Value          Drawdown
────────────────────────────────────────────
  1               $98,000        -2.0%
  2               $96,040        -4.0%
  3               $94,119        -5.9%
  5               $90,392        -9.6%
 10               $81,707       -18.3%
 15               $73,857       -26.1%
 20               $66,761       -33.2%

After 20 CONSECUTIVE losses (extraordinarily rare
for any reasonable strategy), you still have 66.8%
of your capital. Recovery is entirely feasible.

COMPARE WITH 10% RISK PER TRADE:

Consecutive       Portfolio      Cumulative
Losses            Value          Drawdown
────────────────────────────────────────────
  1               $90,000       -10.0%
  2               $81,000       -19.0%
  3               $72,900       -27.1%
  5               $59,049       -41.0%
 10               $34,868       -65.1%
 15               $20,589       -79.4%
 20               $12,158       -87.8%

After 10 consecutive losses, you have lost 65%.
Recovery requires a 186% gain. Effectively impossible
for most strategies. You are financially destroyed.
```

```
POSITION SIZING DECISION TREE

     Start: What is my total portfolio value?
            |
            v
     Calculate: 2% of portfolio = MAX RISK PER TRADE
            |
            v
     Determine: Where is my stop-loss for this trade?
            |
            +--> Stop-loss set by technical analysis
            |    (support level, moving average, etc.)
            |
            +--> Stop-loss set by maximum acceptable
            |    loss (e.g., 10% below entry)
            |
            +--> Stop-loss set by volatility
                 (e.g., 2x ATR below entry)
            |
            v
     Calculate: Risk per share = Entry - Stop-loss
            |
            v
     Calculate: Shares = Max risk / Risk per share
            |
            v
     CHECK: Does position size exceed 25% of portfolio?
            |
       +--->YES: Reduce to 25% maximum position
       |         (your stop is probably too tight)
       |
       +--->NO: Proceed with calculated size
```

#### 2. The Kelly Criterion

The Kelly criterion is a mathematical formula for optimal bet sizing that maximizes long-term growth rate. It was developed by John Kelly at Bell Labs in 1956 and later adopted by gamblers and investors.

```
THE KELLY CRITERION

Full Kelly formula:
  f* = (bp - q) / b

Where:
  f* = fraction of capital to risk
  b  = odds received on the bet (reward-to-risk ratio)
  p  = probability of winning
  q  = probability of losing (1 - p)

EXAMPLE: Stock trade with 60% win rate, 1.5:1 reward/risk
  f* = (1.5 x 0.60 - 0.40) / 1.5
  f* = (0.90 - 0.40) / 1.5
  f* = 0.50 / 1.5
  f* = 0.333 (33.3% of capital)

KELLY FRACTION FOR COMMON SCENARIOS:

Win Rate    Reward:Risk    Full Kelly    Half Kelly
──────────────────────────────────────────────────────
  50%          1:1           0.0%          0.0%
  50%          2:1          16.7%          8.3%
  55%          1:1          10.0%          5.0%
  55%          1.5:1        18.3%          9.2%
  60%          1:1          20.0%         10.0%
  60%          1.5:1        33.3%         16.7%
  60%          2:1          40.0%         20.0%
  65%          1:1          30.0%         15.0%
  70%          1:1          40.0%         20.0%

CRITICAL WARNING:
  Full Kelly is EXTREMELY aggressive.
  It maximizes long-term growth but produces enormous
  drawdowns -- often 50-80% peak-to-trough.
  
  NEVER use full Kelly. Use HALF KELLY or less.
  Half Kelly achieves 75% of the growth rate with
  dramatically less drawdown.

  Even half Kelly is aggressive for most investors.
  Many professionals use quarter Kelly (f*/4).
```

```
KELLY VS. FIXED FRACTION: COMPARISON OVER TIME

Scenario: Strategy with 55% win rate, 1.5:1 reward/risk
Starting capital: $100,000 | 500 trades

                Full Kelly    Half Kelly    2% Fixed
                (18.3%)       (9.2%)        Fraction
──────────────────────────────────────────────────────
Final value     $2,450,000    $890,000      $340,000
Max drawdown    -72%          -42%          -24%
Worst streak    -62%          -35%          -18%
Recovery time   148 trades    62 trades     28 trades
Growth rate     6.3%/trade    4.7%/trade    2.5%/trade

KEY TAKEAWAY:
  Full Kelly has the highest terminal value but the
  drawdowns are psychologically unbearable. A 72%
  drawdown means watching $100,000 become $28,000
  before it recovers.

  Half Kelly is a strong compromise.
  
  The 2% fixed rule is the most conservative and the
  most survivable. For investors who cannot tolerate
  large drawdowns, it is the correct choice.
```

#### 3. Stop-Loss Strategies

A stop-loss is a predetermined price at which you will exit a losing position. It removes the most dangerous variable in investing: your emotions during a drawdown.

```
STOP-LOSS TYPES

1. FIXED PERCENTAGE STOP
   Exit if position declines X% from entry price.
   
   Entry: $100 | Stop: 10% below = $90
   
   Pros: Simple, easy to implement
   Cons: Does not account for stock volatility
         A volatile stock might trigger stops
         on normal fluctuations
   
   Best for: Long-term investors with broad positions

2. VOLATILITY-BASED STOP (ATR STOP)
   Exit if position declines by N x ATR below entry.
   ATR = Average True Range (measure of daily volatility)
   
   Entry: $100 | ATR: $3 | Multiplier: 2x
   Stop: $100 - (2 x $3) = $94
   
   Pros: Adapts to stock's normal movement patterns
         Volatile stocks get wider stops
         Calm stocks get tighter stops
   Cons: Requires ATR calculation
   
   Best for: Active traders, technical analysts

3. SUPPORT-BASED STOP
   Exit if position breaks below a key support level.
   
   Entry: $100 | Key support: $92 | Stop: $91
   (Just below support to avoid stop-hunting)
   
   Pros: Based on market structure, not arbitrary levels
   Cons: Requires chart reading skill
         Support levels are subjective
   
   Best for: Swing traders, technical traders

4. TRAILING STOP
   Stop-loss that moves up as the stock rises,
   but never moves down.
   
   Entry: $100 | Trailing stop: 15%
   Stock hits $120: Stop moves to $102
   Stock hits $140: Stop moves to $119
   Stock drops to $119: TRIGGERED -- exit
   
   Pros: Locks in profits as stock rises
         Never limits upside
   Cons: Can be stopped out by normal pullbacks
         in an uptrend
   
   Best for: Trend followers, momentum traders

5. TIME-BASED STOP
   Exit if the trade has not worked within N days/weeks.
   
   Example: "If this stock has not moved up 5% within
   30 days, I will exit regardless of price."
   
   Pros: Prevents capital from being tied up in
         dead money positions
   Cons: Good trades sometimes take time to develop
   
   Best for: Catalyst-driven trades, options trades
```

```
STOP-LOSS PLACEMENT DIAGRAM

Price
  |
  |  .....
  | .     ..        <-- Stock peaks at $115
  |.       ..
  |         .
  |          ..     <-- Current price: $108
  |           .
  |................ <-- Entry price: $100
  |
  |  ============= <-- RESISTANCE-TURNED-SUPPORT: $97
  |
  |  ------------- <-- STOP-LOSS PLACEMENT: $95
  |                    (below support to avoid
  |                     stop-hunting by market makers)
  |
  |  ============= <-- NEXT SUPPORT: $88
  |
  +---------------------------------------------> Time

STOP-HUNTING:
  Market makers and algorithms know where common
  stop-loss levels cluster (round numbers, obvious
  support levels). They may push prices briefly below
  these levels to trigger stops, then buy the shares
  at lower prices.
  
  DEFENSE: Place stops 1-3% below the obvious level,
  not exactly at it. Use mental stops (manual exit)
  instead of automatic stop orders for large positions.
```

#### 4. Risk Budgeting

Risk budgeting is the process of allocating a total portfolio risk budget across different investments, asset classes, or strategies. It answers the question: "How much risk am I willing to accept in each area?"

```
RISK BUDGETING FRAMEWORK

Step 1: Define total portfolio risk tolerance
  Maximum acceptable drawdown: 20%
  This is your TOTAL RISK BUDGET

Step 2: Allocate risk across asset classes
  ┌─────────────────────────────────────────────┐
  │           TOTAL RISK BUDGET: 20%            │
  │                                             │
  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
  │  │  Equities │  │  Bonds   │  │  Alts    │  │
  │  │  12%      │  │  4%      │  │  4%      │  │
  │  │  risk     │  │  risk    │  │  risk    │  │
  │  └──────────┘  └──────────┘  └──────────┘  │
  │                                             │
  │  Sum of component risks <= Total budget     │
  │  (accounting for correlations, sum can be   │
  │   higher because diversification reduces    │
  │   combined risk)                            │
  └─────────────────────────────────────────────┘

Step 3: Subdivide within each asset class
  Equities (12% risk budget):
    ┌─────────────────────────────────────────┐
    │  US Large Cap    5% risk    (42%)       │
    │  US Small Cap    3% risk    (25%)       │
    │  Int'l Dev       2% risk    (17%)       │
    │  Emerging Mkts   2% risk    (17%)       │
    └─────────────────────────────────────────┘

Step 4: Convert risk budget to position size
  To achieve 5% risk contribution from US Large Cap:
  - US Large Cap historical volatility: 16%
  - Position size = Risk budget / Volatility
  - Position size = 5% / 16% = 31.25% of portfolio
  
  To achieve 2% risk contribution from Emerging Mkts:
  - EM historical volatility: 22%
  - Position size = 2% / 22% = 9.1% of portfolio
```

```
RISK BUDGET ALLOCATION: PRACTICAL EXAMPLE

Portfolio: $500,000
Maximum drawdown tolerance: 15% ($75,000)

Asset Class       Risk     Allocation    Dollar      Max Expected
                  Budget   Weight        Amount      Loss
──────────────────────────────────────────────────────────────────
US Equities       6%       40%           $200,000    $30,000
Int'l Equities    3%       15%           $75,000     $15,000
US Bonds          2%       25%           $125,000    $10,000
Real Estate       2%       10%           $50,000     $10,000
Alternatives      2%       10%           $50,000     $10,000
──────────────────────────────────────────────────────────────────
TOTAL             15%      100%          $500,000    $75,000

Note: Individual risk budgets sum to 15%, which equals
the total budget. In practice, due to imperfect
correlations between asset classes, the actual portfolio
risk will be LESS than 15%. This provides a safety margin.

CORRELATION BENEFIT:
  If all assets were perfectly correlated:
    Portfolio risk = 15% (sum of parts)
  With typical correlations (0.3-0.6 average):
    Portfolio risk = ~10-12%
  The diversification benefit = 3-5% risk reduction
```

#### 5. Scenario Analysis

Scenario analysis is the process of constructing plausible future states of the world and estimating how your portfolio would perform in each. Unlike VaR and other statistical measures, scenario analysis does not rely on historical patterns repeating -- it forces you to imagine specific events and trace their consequences.

```
SCENARIO ANALYSIS FRAMEWORK

Step 1: Define scenarios (3-5 distinct scenarios)

  SCENARIO 1: BASE CASE (50% probability)
    GDP growth 2-3%, inflation 2-3%, rates stable
    S&P 500: +8-12%, Bonds: +3-5%
    
  SCENARIO 2: RECESSION (15% probability)
    GDP contracts 2-4%, unemployment rises to 6%+
    S&P 500: -25 to -35%, Bonds: +8-15%
    
  SCENARIO 3: STAGFLATION (10% probability)
    GDP growth 0-1%, inflation 5-7%, rates rise
    S&P 500: -15 to -25%, Bonds: -5 to -10%
    
  SCENARIO 4: BOOM (20% probability)
    GDP growth 4%+, earnings surge, rates stable
    S&P 500: +20-30%, Bonds: +1-3%
    
  SCENARIO 5: CRISIS (5% probability)
    Financial system stress, credit freeze
    S&P 500: -40 to -50%, Bonds: -5 to +20%
    (depends on nature of crisis)

Step 2: Estimate portfolio impact in each scenario

Step 3: Check -- is the worst case survivable?
  If NO: reduce risk until worst case is survivable
  If YES: is the expected return acceptable?
```

```
SCENARIO ANALYSIS: WORKED EXAMPLE

Portfolio: $400,000
  60% US Equities ($240,000)
  25% US Bonds ($100,000)
  10% REITs ($40,000)
  5% Gold ($20,000)

                  Equities  Bonds    REITs    Gold     PORTFOLIO
Scenario          Return    Return   Return   Return   Return
──────────────────────────────────────────────────────────────────
Base case (50%)   +10%      +4%      +8%      +2%      +7.7%
                  +$24,000  +$4,000  +$3,200  +$400    +$31,600

Recession (15%)   -30%      +12%     -25%     +15%     -16.5%
                  -$72,000  +$12,000 -$10,000 +$3,000  -$67,000

Stagflation (10%) -20%      -8%      -15%     +25%     -13.7%
                  -$48,000  -$8,000  -$6,000  +$5,000  -$57,000

Boom (20%)        +25%      +2%      +20%     -5%      +17.3%
                  +$60,000  +$2,000  +$8,000  -$1,000  +$69,000

Crisis (5%)       -45%      +5%      -40%     +30%     -27.1%
                  -$108,000 +$5,000  -$16,000 +$6,000  -$113,000

EXPECTED VALUE = Sum of (probability x return):
  = (0.50 x 7.7%) + (0.15 x -16.5%) + (0.10 x -13.7%)
    + (0.20 x 17.3%) + (0.05 x -27.1%)
  = 3.85% - 2.48% - 1.37% + 3.46% - 1.36%
  = +2.1% expected return

WORST CASE ANALYSIS:
  Crisis scenario: -27.1% = -$113,000
  Is this survivable? For a 45-year-old with
  a $120,000 salary and 20-year horizon: YES
  For a 68-year-old retiree depending on the
  portfolio for income: PROBABLY NOT

  If not survivable, reduce equity allocation
  until worst case is within tolerance.
```

#### 6. The Risk Management Process

Risk management is not something you do once and forget. It is a continuous process that must be integrated into your daily, weekly, and monthly investing routine.

```
THE RISK MANAGEMENT PROCESS

  ┌──────────────────────────────────────────────────────┐
  │                                                      │
  │     ┌──────────┐                                     │
  │     │ IDENTIFY  │  What risks does my portfolio      │
  │     │ RISKS     │  face? Market, credit, liquidity,  │
  │     └─────┬─────┘  concentration, currency, etc.     │
  │           │                                          │
  │           v                                          │
  │     ┌──────────┐                                     │
  │     │ MEASURE   │  How large are these risks?        │
  │     │ RISKS     │  Use volatility, VaR, stress       │
  │     └─────┬─────┘  tests, correlation analysis.      │
  │           │                                          │
  │           v                                          │
  │     ┌──────────┐                                     │
  │     │ SET       │  How much risk am I willing        │
  │     │ LIMITS    │  to take? Define position limits,  │
  │     └─────┬─────┘  drawdown limits, sector limits.   │
  │           │                                          │
  │           v                                          │
  │     ┌──────────┐                                     │
  │     │ MONITOR   │  Are my current exposures within   │
  │     │ EXPOSURES │  limits? Track positions daily.    │
  │     └─────┬─────┘  Check correlations monthly.      │
  │           │                                          │
  │           v                                          │
  │     ┌──────────┐                                     │
  │     │ ADJUST    │  When limits are breached or       │
  │     │ & RESPOND │  conditions change, rebalance,     │
  │     └─────┬─────┘  hedge, or reduce exposure.        │
  │           │                                          │
  │           v                                          │
  │     ┌──────────┐                                     │
  │     │ REVIEW    │  What worked? What did not?        │
  │     │ & LEARN   │  Update models and assumptions     │
  │     └─────┬─────┘  based on actual results.          │
  │           │                                          │
  │           └──────────> (back to IDENTIFY)             │
  │                                                      │
  └──────────────────────────────────────────────────────┘
```

```
RISK MANAGEMENT CHECKLIST: INDIVIDUAL INVESTOR

DAILY (5 minutes):
  [ ] Check portfolio value and daily P&L
  [ ] Check if any positions are near stop-loss levels
  [ ] Check major market indicators (S&P, VIX, 10Y yield)
  [ ] Check for breaking news on held positions

WEEKLY (30 minutes):
  [ ] Review all open positions and their status
  [ ] Check position sizes vs. risk limits
  [ ] Review sector and geographic concentration
  [ ] Check correlation of recent returns
  [ ] Verify stop-losses are current and appropriate

MONTHLY (2 hours):
  [ ] Calculate portfolio risk metrics (volatility,
      max drawdown, Sharpe ratio)
  [ ] Run scenario analysis on current portfolio
  [ ] Review risk budget allocation vs. targets
  [ ] Assess whether any positions should be trimmed
      or added to
  [ ] Compare realized risk to expected risk
  [ ] Document any risk events and lessons learned

QUARTERLY (4 hours):
  [ ] Full portfolio risk review
  [ ] Re-run correlation analysis (correlations change)
  [ ] Update scenario analysis with new assumptions
  [ ] Review and update risk budget allocations
  [ ] Stress test against historically extreme events
  [ ] Review whether the overall risk level is
      appropriate for your current life situation
```

#### 7. Concentration Risk

One of the most dangerous and underappreciated risks for individual investors is concentration -- having too much of the portfolio in a single stock, sector, or asset class.

```
CONCENTRATION RISK GUIDELINES

MAXIMUM POSITION SIZES (as % of total portfolio):

  Single stock:           5-10%
  Single sector:         20-25%
  Single country:        30-40%  (ex. home country)
  Single asset class:    50-60%
  Single strategy:       30-40%
  
  EXCEPTIONS:
  Employer stock:        Maximum 10%
  (You already have income risk from your employer.
   Adding portfolio risk doubles down on one company.)
  
  Your home:             Maximum 40% of net worth
  (Hard to diversify, but recognized as unavoidable)

CONCENTRATION WARNING SIGNS:

  ┌───────────────────────────────────────────────┐
  │  RED FLAGS:                                   │
  │                                               │
  │  > 20% in one stock (excluding home)          │
  │  > 40% in one sector                          │
  │  > 70% in one country                         │
  │  > 80% in one asset class                     │
  │  > 50% in correlated positions                │
  │  Your employer stock exceeds 15%              │
  │  One position's daily P&L dominates the       │
  │    entire portfolio's daily P&L               │
  └───────────────────────────────────────────────┘

REAL-WORLD DISASTERS FROM CONCENTRATION:

  Enron employees: 62% of 401k in Enron stock
    Result: $2 billion in retirement savings lost
    
  Bear Stearns employees: Stock went from $170 to $2
    Many employees had majority of net worth in stock
    
  Tech workers in 2000-2002: Large RSU/option holdings
    NASDAQ dropped 78%. Many lost 90%+ of net worth.
```

#### 8. Correlation and the Illusion of Diversification

Diversification only works when assets are not highly correlated. During crises, correlations tend to increase -- precisely when diversification is needed most.

```
CORRELATION BEHAVIOR IN DIFFERENT MARKETS

             Normal Market          Crisis Market
             Correlations           Correlations
─────────────────────────────────────────────────────
Stocks/Bonds   -0.2 to +0.3         -0.5 to +0.6
                                     (can flip either way)

US/Int'l        +0.5 to +0.7         +0.8 to +0.95
Stocks                               (convergence)

Large/Small     +0.7 to +0.8         +0.90 to +0.98
Cap                                  (convergence)

Stocks/Gold     -0.1 to +0.1         -0.3 to +0.5
                                     (unreliable)

Stocks/REITs    +0.5 to +0.7         +0.8 to +0.95
                                     (convergence)

KEY INSIGHT: During crises, most "diversified"
portfolios turn out to be far less diversified than
expected. The only reliable diversifiers are:

1. Cash (always uncorrelated, but zero real return)
2. Long-dated US Treasuries (usually negative
   correlation in equity crashes, but NOT guaranteed)
3. Managed futures/trend following (historically
   negative correlation in equity crashes)
4. Long volatility (by design, profits from crashes)

THE DIVERSIFICATION ILLUSION:

   Calm markets:                Crisis:
   ┌────┐ ┌────┐ ┌────┐        ┌────────────────┐
   │ US │ │Int'l│ │ EM │        │                │
   │+8% │ │+6% │ │+10%│        │  ALL: -30%     │
   │    │ │    │ │    │        │  to -45%       │
   └────┘ └────┘ └────┘        │                │
   "Diversified!"              └────────────────┘
                               "Where did my
                                diversification go?"
```

#### 9. Drawdown Management

Drawdowns -- peak-to-trough declines in portfolio value -- are the most psychologically painful aspect of investing. Understanding drawdown math is essential because the recovery math is asymmetric.

```
DRAWDOWN AND RECOVERY: THE ASYMMETRY PROBLEM

Drawdown    Required Recovery     Recovery Time
            to Break Even         (at 10%/year)
─────────────────────────────────────────────────
  -5%         +5.3%                6 months
 -10%        +11.1%                1.1 years
 -15%        +17.6%                1.7 years
 -20%        +25.0%                2.3 years
 -25%        +33.3%                3.0 years
 -30%        +42.9%                3.7 years
 -40%        +66.7%                5.4 years
 -50%       +100.0%                7.3 years
 -60%       +150.0%               10.0 years
 -75%       +300.0%               15.0 years
 -90%       +900.0%               25.0 years

KEY INSIGHT:
  A 50% loss requires a 100% gain to recover.
  A 75% loss requires a 300% gain.
  
  This is why risk management focuses on avoiding
  large drawdowns. Once you are down 50%+, the math
  of recovery works against you so severely that
  many investors never recover within their lifetime.

MAXIMUM DRAWDOWN GUIDELINES BY INVESTOR TYPE:

  Conservative (retiree, near retirement):    10-15%
  Moderate (mid-career, balanced risk):       15-25%
  Aggressive (young, high income, long horizon): 25-35%
  Very aggressive (speculative allocation):   35-50%
  
  No investor should accept a maximum drawdown
  greater than 50% on their total portfolio.
```

#### 10. Risk as Process: Building Your Risk Framework

```
BUILDING A PERSONAL RISK MANAGEMENT FRAMEWORK

STEP 1: KNOW YOUR RISK CAPACITY
  ┌─────────────────────────────────────────────┐
  │  FINANCIAL CAPACITY:                        │
  │  - Time horizon: _____ years                │
  │  - Income stability: high / medium / low    │
  │  - Emergency fund: _____ months of expenses │
  │  - Portfolio as % of net worth: _____%      │
  │  - Dependents: _____                        │
  │                                             │
  │  EMOTIONAL CAPACITY:                        │
  │  - Can I sleep with a 20% drawdown?  Y/N   │
  │  - Can I sleep with a 30% drawdown?  Y/N   │
  │  - Have I experienced a bear market? Y/N    │
  │  - Did I panic-sell in past drawdowns? Y/N  │
  │                                             │
  │  YOUR RISK CAPACITY = minimum of financial  │
  │  and emotional capacity. If you can afford  │
  │  a 30% drawdown but cannot sleep through    │
  │  it, your capacity is lower than 30%.       │
  └─────────────────────────────────────────────┘

STEP 2: SET SPECIFIC LIMITS (write them down)
  Maximum portfolio drawdown: _____%
  Maximum single position risk: _____%
  Maximum sector concentration: _____%
  Maximum correlated exposure: _____%
  Minimum cash/liquidity reserve: _____%

STEP 3: IMPLEMENT SYSTEMS
  - Set stop-losses on all active positions
  - Set calendar reminders for weekly/monthly reviews
  - Use a spreadsheet or portfolio tracker
  - Write down your rules and review them when
    emotions run high

STEP 4: REVIEW AND ADAPT
  - Quarterly: Are my limits still appropriate?
  - After major events: What did I learn?
  - Annually: Has my risk capacity changed?
```

---

### c) Common Misconceptions

**Misconception 1: "Diversification is all the risk management I need."**

Diversification is necessary but far from sufficient. As we saw, correlations spike during crises, which means your "diversified" portfolio of US stocks, international stocks, REITs, and high-yield bonds may all decline 25-40% simultaneously. True risk management requires position sizing, stop-losses, risk budgeting, and scenario analysis in addition to diversification. Diversification is one tool in the toolbox, not the entire toolbox.

**Misconception 2: "Stop-losses guarantee I will not lose more than X%."**

Stop-loss orders become market orders once triggered, and in fast-moving markets, the execution price can be far below your stop price. This is called slippage. During the 2010 Flash Crash, many stop-loss orders were filled 20-40% below the stop price. During overnight gaps (stock opens 15% lower than the previous close due to bad earnings), your stop-loss at 10% below entry is irrelevant -- you will be filled at the open price. Stop-losses are risk management tools, not risk elimination tools.

**Misconception 3: "The Kelly criterion tells me exactly how much to bet."**

Kelly requires precise knowledge of your win rate and reward-to-risk ratio, which in investing are estimates, not known quantities. A small error in estimating your edge can lead to dramatically wrong position sizes. If you think your win rate is 60% but it is actually 50%, full Kelly will tell you to bet aggressively on what is actually a zero-edge strategy. This is why practitioners use half Kelly or less -- it provides a buffer against estimation error.

**Misconception 4: "Risk management reduces returns."**

In the short term, yes -- limiting position sizes means you capture less of your best ideas. But in the long term, risk management increases compound returns because it prevents the catastrophic drawdowns that destroy compounding. A strategy that returns 15% per year with a -60% max drawdown will underperform a strategy that returns 10% per year with a -20% max drawdown over a 20-year period, because the recovery time from -60% destroys several years of compounding.

**Misconception 5: "I do not need stop-losses on long-term investments."**

This depends on your definition of "long-term." If you have a 30-year horizon and are investing in broad index funds, position-level stop-losses may indeed be unnecessary because you are accepting interim drawdowns in exchange for long-term returns. But if "long-term" means holding individual stocks for years, stop-losses are critical. Enron, Bear Stearns, Lehman Brothers, and Wirecard were all long-term holdings for many investors who watched them go to zero. Individual stocks can go to zero; indexes generally do not.

**Misconception 6: "Risk equals volatility."**

Volatility is one measure of risk, but it is not risk itself. The true risks that destroy investors are permanent loss of capital, liquidity crises (unable to sell when you need to), concentration blowups, and behavioral mistakes (panic selling at the bottom). A stock that goes from $100 to $80 to $120 has high volatility but produced a positive outcome. A stock that goes from $100 to $95 to $90 to $0 has low volatility but destroyed your capital. Focus on the risks that actually destroy wealth, not just the ones that are easy to measure.

---

### d) Common Questions and Answers

**Q1: Should I use the 2% rule for long-term buy-and-hold investments?**

A: The 2% rule is primarily designed for active trading where stop-losses are used. For long-term buy-and-hold investments, the concept still applies but is adapted differently. Instead of defining risk as "distance to stop-loss," define risk as "maximum acceptable loss on this position." If you are willing to accept a 30% decline on a stock (holding through a bear market), then the 2% rule would size the position at 2% / 30% = 6.7% of your portfolio. This ensures that even if the stock drops 30%, your total portfolio impact is limited to 2%.

**Q2: How do I set a stop-loss on a stock that I own for dividend income?**

A: Dividend stocks present a dilemma because selling eliminates the income stream. Consider a "soft stop" approach: if the stock declines 20% from your purchase price, conduct a full review. Has the dividend been cut? Has the business fundamentally deteriorated? If yes, sell. If the dividend is secure and the business is sound, the decline may be a buying opportunity. However, set a "hard stop" at a level where the decline would indicate fundamental distress -- typically 30-40% below entry. If a dividend stock declines 40%, something is almost certainly wrong regardless of the dividend yield.

**Q3: How do I handle risk for options positions?**

A: For options, risk your premium. If you buy a call option for $3 per share ($300 total), your maximum risk is $300. Apply the 2% rule to the premium, not the underlying stock value. For sold options, risk is potentially much larger. For a sold put at a $50 strike, your maximum risk is $5,000 per contract (if stock goes to zero). Size sold options positions so that the maximum loss is within your 2% risk budget.

**Q4: How often should I rebalance to manage risk?**

A: Rebalancing frequency depends on how far your portfolio drifts from targets. Calendar-based rebalancing (quarterly or semi-annually) is simple but arbitrary. Threshold-based rebalancing (rebalance when any allocation drifts more than 5 percentage points from target) is more efficient. In practice, checking monthly and rebalancing when thresholds are breached is a reasonable compromise. Over-rebalancing incurs transaction costs and taxes; under-rebalancing allows risk drift.

**Q5: What is the biggest risk management mistake individual investors make?**

A: The single biggest mistake is not having a risk management plan at all. Most individual investors buy stocks or funds based on tips, articles, or recent performance, with no predefined exit strategy, no position sizing methodology, no risk budget, and no scenario analysis. They are flying blind. The second biggest mistake is having a plan but abandoning it during market stress -- selling everything after a 20% decline because "this time is different," when their plan said to hold through drawdowns.

**Q6: How do I account for risk in assets I cannot easily sell, like real estate or private investments?**

A: Illiquid assets should be included in your risk budget at their estimated value, with the additional recognition that you cannot quickly reduce the position if conditions deteriorate. This means illiquid assets should have a larger risk allocation to account for the inability to exit. If your real estate holding represents 30% of your net worth and you cannot sell it quickly, you should reduce risk in your liquid portfolio to compensate. Treat illiquidity as an additional risk factor, not just a minor inconvenience.

**Q7: Should my risk management approach change as I age?**

A: Absolutely. As your time horizon shortens, your capacity to recover from large drawdowns diminishes. A 30-year-old with a -40% drawdown has 30+ years to recover. A 65-year-old with a -40% drawdown may never recover within their spending lifetime. Gradually reduce your maximum drawdown tolerance as you age: 35-40% maximum in your 20s-30s, 25-30% in your 40s-50s, 15-20% in your 60s, and 10-15% in retirement. This translates directly into lower equity allocations and tighter stop-losses over time.

---

---

## YouTube Script

**Week 41: Portfolio Risk Management**

[VISUAL: Title card -- "Portfolio Risk Management: How to Survive and Thrive"]

**Alex**: Today we are going to talk about the most important topic in all of investing, and I guarantee it is not what most people think.

**Sam**: Let me guess -- it is not about finding the next hot stock?

**Alex**: Not even close. It is about risk management. Every legendary investor -- Warren Buffett, Ray Dalio, Howard Marks, George Soros -- they all say the same thing. The first rule of investing is do not lose money. The second rule is do not forget rule one.

**Sam**: That sounds like a cliche, though. Everyone says "do not lose money." How do you actually do it?

**Alex**: That is exactly what we are going to cover. Risk management is a system -- a set of tools and processes that keep you in the game long enough for your good ideas to work. Let me start with the single most impactful concept: position sizing.

[VISUAL: "Position Sizing: The 2% Rule" slide]

**Alex**: Position sizing is deciding how much of your portfolio to put into any single investment. And here is the thing -- most retail investors do this completely wrong or do not do it at all.

**Sam**: What do they do instead?

**Alex**: They typically do one of three things. First, equal weighting -- just divide the portfolio into however many stocks they want to own. Ten stocks, ten percent each. Second, conviction weighting -- they put 30% into their best idea, 20% into the next, and so on. Third, and most common, random sizing -- they buy some number of shares that "feels right" with no methodology at all.

**Sam**: And those are all wrong?

**Alex**: They are all missing the key insight. Position sizing should be based on risk, not conviction or arbitrary allocation.

[ANIMATION: animation/week41_position_sizing.py -- Animated comparison of three portfolios over 100 trades. Portfolio A uses the 2% rule with consistent 2% risk per trade. Portfolio B uses aggressive 10% risk per trade. Portfolio C uses random sizing between 1-15%. The underlying strategy is identical with a 55% win rate and 1.5:1 reward-to-risk ratio. The animation shows all three portfolio equity curves simultaneously, with Portfolio B experiencing a devastating drawdown around trade 40 that nearly wipes it out, Portfolio C showing erratic volatile performance, and Portfolio A showing steady upward growth with manageable drawdowns. Running statistics show maximum drawdown, current drawdown, and total return for each.]

**Sam**: That is incredibly clear. Portfolio B -- the aggressive one -- nearly went to zero even though the underlying strategy was profitable.

**Alex**: Exactly. The strategy had a genuine edge. Fifty-five percent win rate, 1.5 to 1 reward-to-risk. That is a good strategy. But with 10% risk per trade, a normal losing streak was enough to nearly destroy the account. Portfolio A, using the 2% rule, captured the same edge but survived the drawdowns.

**Sam**: OK, walk me through the 2% rule mechanically.

**Alex**: Here is how it works. Take your total portfolio value. Calculate 2% of it -- that is your maximum risk per trade. Then determine where your stop-loss is. The distance between your entry price and your stop-loss, in dollars per share, is your risk per share. Divide your maximum risk by the risk per share, and you get the number of shares to buy.

[VISUAL: Step-by-step calculation example on screen]

**Alex**: Say your portfolio is $100,000. Two percent is $2,000 maximum risk. You want to buy a stock at $50 with a stop-loss at $45. That is $5 risk per share. Two thousand divided by five equals 400 shares. You would buy 400 shares at $50, which is a $20,000 position -- 20% of your portfolio.

**Sam**: Wait -- 20% in one stock? That seems aggressive.

**Alex**: But notice -- the POSITION is 20%, but the RISK is only 2%. If you are wrong and the stock hits your stop-loss at $45, you lose $2,000. Two percent of your portfolio. Completely survivable. The key distinction is between position size and risk. They are not the same thing.

**Sam**: What if I have a wider stop-loss?

**Alex**: Then you buy fewer shares. Same stock at $50, but your stop is at $40 -- that is $10 risk per share. Two thousand divided by ten equals 200 shares. Your position is now $10,000 -- only 10% of the portfolio. The wider the stop, the smaller the position. The risk stays constant.

[VISUAL: Table showing different stop distances and resulting position sizes]

**Sam**: That makes a lot of sense. The stop-loss determines the position size, not the other way around.

**Alex**: Exactly right. Now let me explain why 2% specifically. It is about surviving losing streaks.

**Sam**: How bad can losing streaks get?

**Alex**: Worse than you think. Even with a 60% win rate, there is about a 1% chance of losing 10 trades in a row over any 200-trade period. If you risk 2% per trade, ten consecutive losses takes you down about 18%. Painful, but totally recoverable. If you risk 10% per trade, ten consecutive losses takes you down 65%. You now need a 186% gain just to break even. You are effectively dead.

[VISUAL: Side-by-side drawdown comparison table]

**Sam**: OK, I am sold on the 2% rule. But I have heard of something called the Kelly criterion that supposedly tells you the mathematically optimal bet size. Is that better?

**Alex**: The Kelly criterion is fascinating and important, but dangerous in practice. Let me explain.

[VISUAL: Kelly criterion formula on screen]

**Alex**: The Kelly formula calculates the fraction of your capital that maximizes long-term growth rate, given your edge. It takes into account both your win rate and your reward-to-risk ratio. For a strategy with a 60% win rate and 1.5 to 1 payoff, Kelly says to risk 33% of your capital per trade.

**Sam**: Thirty-three percent? That is insanely aggressive.

**Alex**: It is. And here is the catch -- full Kelly is mathematically optimal for growth, but it produces drawdowns of 50-80% along the way. No human being can tolerate that. The standard practice is to use half Kelly, which gives you 75% of the growth rate with dramatically less drawdown. Or quarter Kelly for even more conservative sizing.

**Sam**: But there is another problem, right? You have to know your exact win rate and payoff ratio.

**Alex**: That is the fatal flaw. Kelly requires PRECISE inputs. In gambling, you know the odds exactly. In investing, you are estimating. If you think your win rate is 60% but it is really 50%, full Kelly will have you risking 33% per trade on a strategy with zero edge. You will blow up.

[VISUAL: Sensitivity analysis showing how small changes in estimated win rate dramatically change Kelly sizing]

**Alex**: This is why the 2% rule is safer for most investors. It does not require you to know your edge precisely. It simply limits the damage from any single trade. Use Kelly as a theoretical framework for thinking about bet sizing, but use the 2% rule as your practical daily tool.

**Sam**: Let me transition to stop-losses. You keep mentioning them as part of position sizing. What are the main types?

[VISUAL: "Stop-Loss Strategies" section header]

**Alex**: There are five main types, and each one has its place. First is the fixed percentage stop. You simply sell if the stock drops a certain percentage below your entry. Ten percent is common. Simple but inflexible -- it does not account for different stocks having different volatilities.

**Sam**: A volatile biotech stock might routinely swing 10% in a week.

**Alex**: Exactly. That is why the second type -- the volatility-based stop -- is often better. You use the stock's Average True Range, or ATR, which measures its normal daily movement. A typical stop is set at 2 times ATR below the entry price. So a calm utility stock with a $0.50 ATR gets a $1 stop, while a volatile tech stock with a $5 ATR gets a $10 stop.

[VISUAL: Two stocks side by side showing different ATR values and resulting stop placement]

**Sam**: The stop adjusts to the stock's natural movement. I like that.

**Alex**: Third is the support-based stop. You identify a key support level on the chart and place your stop just below it. If the stock breaks support, the technical picture has changed and you exit. This requires chart-reading ability but is probably the most widely used method among professional traders.

**Sam**: What about trailing stops?

**Alex**: That is number four. A trailing stop moves up as the stock rises but never moves down. If you set a 15% trailing stop on a stock you bought at $100, and it goes to $140, your stop is now at $119. If the stock then drops to $119, you are sold out with a 19% gain instead of riding it back down.

[ANIMATION: animation/week41_trailing_stop.py -- Animated chart showing a stock price rising from $100 to $160 over several months with pullbacks along the way. A trailing stop line (15% below peak) is shown moving up alongside the price. The animation pauses at key moments to highlight how the stop adjusts: it rises when the stock makes new highs but stays flat during pullbacks. Eventually the stock reverses and crosses the trailing stop line, triggering a sell. Annotations show the entry price, the highest price reached, the trailing stop level, and the final gain captured.]

**Sam**: That is elegant. You never cap your upside, but you protect against major reversals.

**Alex**: The final type is the time-based stop. You exit if the trade has not worked within a certain number of days or weeks. This is especially useful for catalyst-driven trades. If you bought before an earnings report expecting a breakout and nothing happened after two weeks, exit and deploy your capital elsewhere.

**Sam**: Let us move to risk budgeting. How do I think about my total portfolio risk?

[VISUAL: "Risk Budgeting" section header]

**Alex**: Risk budgeting starts with one number: your maximum acceptable drawdown. What is the largest peak-to-trough decline you can tolerate -- financially AND emotionally?

**Sam**: How do I figure that out?

**Alex**: Financially, it depends on your time horizon and income. If you are 30 years old with a stable job, you can probably tolerate a 30% drawdown because you have decades to recover and ongoing income to invest. If you are 65 and retired, a 30% drawdown might force you to sell at the bottom because you need the money for living expenses.

**Sam**: And the emotional side?

**Alex**: Here is a brutal truth. Most people overestimate their emotional risk tolerance. In a survey, everyone says they can handle a 20% decline. But when their $500,000 portfolio drops to $400,000, they cannot sleep. They check their phone at 3 AM. They argue with their spouse. They eventually panic-sell at the bottom. If you have never experienced a real bear market, be conservative in estimating your emotional capacity. Use a maximum drawdown that is 10 percentage points below what you think you can handle.

[VISUAL: Risk capacity assessment framework]

**Alex**: Once you have your maximum drawdown, you allocate it across asset classes. This is your risk budget. If your total budget is 20%, you might allocate 12% to equities, 4% to bonds, and 4% to alternatives. Then you size your positions within each bucket so that the worst-case loss for each bucket stays within its allocation.

**Sam**: How do I translate a risk budget into actual position sizes?

**Alex**: Divide the risk budget by the asset's expected volatility. If you allocate 5% of risk to US large cap stocks, and US large cap has roughly 16% historical volatility, your position size should be about 5% divided by 16%, which is 31% of your portfolio. For emerging markets with 22% volatility and a 2% risk allocation, the position would be 2% divided by 22%, about 9% of the portfolio.

[VISUAL: Risk budget allocation table with calculations]

**Sam**: So riskier assets automatically get smaller allocations?

**Alex**: Exactly. And that is the beauty of risk budgeting versus naive allocation. If you simply allocate 30% to US stocks and 10% to emerging markets, you might think the EM position is small. But EM is far more volatile, so it might actually contribute MORE risk than the larger US position. Risk budgeting ensures each position contributes proportionally to your overall risk.

**Sam**: Let us talk about scenario analysis. I hear professional investors talk about this a lot.

[VISUAL: "Scenario Analysis" section header]

**Alex**: Scenario analysis is one of the most powerful tools in risk management because it forces you to think about specific future states of the world, not just historical patterns. Here is how it works.

**Alex**: Step one, define three to five plausible scenarios. A base case -- the most likely outcome. An optimistic case. A pessimistic case. And one or two extreme cases.

**Sam**: Give me an example.

**Alex**: For a typical balanced portfolio right now, I would model: Base case, economy grows 2-3%, stocks up 8-12%, bonds up 3-5%. Recession, GDP contracts, stocks down 25-35%, bonds up 8-15%. Stagflation, low growth with high inflation, stocks down 15-25%, bonds also down 5-10% because rising rates hurt bond prices. A boom, GDP growth 4%+, stocks up 20-30%. And a financial crisis, credit freeze, stocks down 40-50%.

[VISUAL: Scenario matrix with descriptions]

**Sam**: Then you apply each scenario to your actual portfolio?

**Alex**: Exactly. Take every position in your portfolio and estimate how it would perform in each scenario. Then calculate the total portfolio impact. The critical question is: in the worst case, is the loss survivable?

**Sam**: And if it is not?

**Alex**: Then you reduce risk until it is. That might mean reducing equity allocation, adding hedges, or increasing cash. The whole point of scenario analysis is to confront uncomfortable possibilities BEFORE they happen, when you can still make rational decisions. Once the crisis is happening, emotions take over.

[ANIMATION: animation/week41_scenario_analysis.py -- Interactive scenario analysis visualization. Shows a sample portfolio with 60% stocks, 25% bonds, 10% REITs, 5% gold. Five scenarios are displayed as columns: base case, recession, stagflation, boom, and crisis. For each scenario, animated bars show the return of each asset class and the total portfolio return. The worst-case scenario is highlighted in red, with an annotation showing the dollar loss and the number of years needed to recover at the expected return rate. The animation then shows the portfolio being adjusted -- reducing stocks to 45%, adding 15% to short-term bonds -- and the scenarios recalculate, showing the worst case improving significantly.]

**Sam**: That really drives the point home. You can see exactly how each change affects your worst case.

**Alex**: And notice something important. When we reduced stocks from 60% to 45%, the base case return dropped -- from about 7.7% to about 6.2%. Risk management has a cost. But the worst case improved from a 27% loss to about an 18% loss. That is the tradeoff, and it is a tradeoff every investor needs to make consciously.

**Sam**: You have been building toward something. You keep saying risk management is a process. What does that mean?

[VISUAL: "Risk Management as a Process" section header]

**Alex**: This is the most important part of today's lesson. Risk management is not a one-time activity. It is not something you do when you set up your portfolio and then forget about. It is an ongoing cycle of identifying risks, measuring them, setting limits, monitoring your positions, adjusting when necessary, and reviewing what worked and what did not.

**Sam**: Walk me through what this looks like in practice for a regular investor.

**Alex**: Daily, which should take about five minutes: check your portfolio value, check if any positions are near stop-loss levels, and glance at the VIX and major market indicators. Weekly, about 30 minutes: review all open positions, verify position sizes are within risk limits, and check concentration. Monthly, about two hours: calculate your portfolio risk metrics, run a quick scenario analysis, review your risk budget, and document any lessons learned.

**Sam**: And quarterly?

**Alex**: Quarterly is your deep review. Four hours of serious work. Re-run your full scenario analysis with updated assumptions. Check whether correlations have changed -- they do change over time. Review whether your overall risk level is still appropriate for your life situation. A lot can change in three months -- a new job, a new baby, a big expense coming up.

[VISUAL: Risk management checklist organized by daily/weekly/monthly/quarterly]

**Sam**: Let me ask about something that is really relevant right now -- concentration risk. A lot of people have portfolios dominated by tech stocks.

**Alex**: Concentration risk is one of the most dangerous forms of risk because it feels good when it works. If you put 40% of your portfolio in Nvidia and it triples, you are a genius. But if Nvidia drops 60% -- which it absolutely can, and has in the past -- you have just lost 24% of your entire portfolio from a single stock.

**Sam**: What are the guidelines?

**Alex**: No single stock should be more than 5-10% of your total portfolio. No single sector should exceed 20-25%. And here is one people forget -- employer stock should be capped at 10%, because you already have income concentration risk with your employer. If you work at a tech company and own their stock, a single bad event can cost you both your job and your savings simultaneously.

**Sam**: That is what happened at Enron, right?

**Alex**: Enron employees had 62% of their 401k in Enron stock. When the company went to zero, they lost both their jobs and their retirement savings. The same pattern repeated at Bear Stearns, Lehman Brothers, and dozens of smaller companies. It is a mistake that gets made over and over.

[VISUAL: Historical examples of concentration risk disasters]

**Sam**: What about the correlation trap? You mentioned earlier that diversification can fail.

**Alex**: This is crucial. Most people think they are diversified because they own US stocks, international stocks, REITs, and maybe some corporate bonds. In calm markets, these assets have moderate correlations -- they do not all move together. But in a crisis, correlations spike toward one. Suddenly everything drops together.

**Sam**: So what actually provides real diversification in a crisis?

**Alex**: The reliable crisis diversifiers are cash, long-dated US Treasuries -- though even these are not guaranteed -- managed futures strategies that profit from trends in either direction, and long volatility positions. Everything else -- international stocks, REITs, corporate bonds, commodities -- tends to correlate heavily with US stocks during severe stress.

[VISUAL: Correlation matrix showing normal vs. crisis values]

**Sam**: Let us talk about drawdown management. You mentioned the asymmetry problem.

**Alex**: This is math everyone needs to understand. Losses and gains are not symmetrical. If you lose 10%, you need an 11% gain to recover. That is manageable. But if you lose 50%, you need a 100% gain to recover. At typical stock market returns of 8-10% per year, that takes seven years. If you lose 75%, you need a 300% gain -- fifteen years at 10% per year.

[VISUAL: Drawdown recovery table with years to recover]

**Sam**: So the entire point of risk management is to keep drawdowns small enough that recovery is feasible.

**Alex**: That is exactly right. The most successful long-term investors are not the ones with the highest returns -- they are the ones who avoid catastrophic drawdowns. Warren Buffett has never had a single year where Berkshire's book value dropped more than about 9%. His secret is not stock picking genius, though he has that too. It is the relentless focus on avoiding permanent loss of capital.

**Sam**: Let me summarize what I have learned today.

[VISUAL: Summary slide]

**Sam**: First, position sizing using the 2% rule -- never risk more than 2% of your portfolio on a single trade. Second, the Kelly criterion is mathematically optimal but too aggressive in practice -- use half Kelly or less, or just stick with the 2% rule. Third, stop-losses protect capital, and there are five main types depending on your trading style. Fourth, risk budgeting allocates a total risk tolerance across asset classes. Fifth, scenario analysis prepares you for specific futures. And sixth, risk management is an ongoing process, not a one-time setup.

**Alex**: Perfect summary. And here is one last thought. The best trade you will ever make is the one you do not make because your risk management told you the position was too large or the risk/reward was not there. You will never see that trade in your performance report, but it might be the one that saved your portfolio.

**Sam**: It is hard to appreciate avoiding a loss you never experienced.

**Alex**: That is why risk management is so hard psychologically. It is like paying for fire insurance. Every year you do not have a fire, the insurance feels like a waste. But the year your house burns down, it is the best money you ever spent. The goal is to still be investing five, ten, twenty years from now. And the only way to guarantee that is to manage your risk today.

**Sam**: This has been eye-opening. I think most investors, myself included, spend too much time researching stocks and not enough time thinking about how much to bet and when to exit.

**Alex**: And that is the dirty secret of the investment industry. The financial media, the newsletters, the YouTube channels -- they focus almost entirely on WHAT to buy. Nobody wants to hear about position sizing and drawdown management. But that is where the real edge is. The what-to-buy question matters, but the how-much-to-buy and when-to-sell questions matter more.

[VISUAL: Key takeaways bullet list]

**Alex**: Before we close, let me leave you with five rules of risk management that I want you to write down.

**Sam**: Go ahead.

**Alex**: Rule one: never risk more than 2% of your portfolio on a single trade. Rule two: always have a predetermined exit point before you enter a trade. Rule three: diversification is not enough -- you need position limits, sector limits, and correlation awareness. Rule four: plan for the worst case and make sure it is survivable. Rule five: risk management is a daily process, not a product you can buy.

**Sam**: Simple rules but incredibly hard to follow when emotions kick in.

**Alex**: That is why you write them down, review them regularly, and build systems that enforce them automatically. Stop-loss orders enforce rule two. Position sizing calculators enforce rule one. Calendar reminders enforce rule five. The goal is to make risk management automatic so you do not have to rely on willpower during a market panic.

[VISUAL: "Next week: Value at Risk and Risk Models"]

**Alex**: Next week, we are going to dive into the quantitative side of risk management -- Value at Risk, Conditional Value at Risk, stress testing, and factor risk models. We will put numbers on everything we discussed today.

**Sam**: So today was the conceptual framework, and next week is the math.

**Alex**: Exactly. You need both. The concepts tell you what to do. The models tell you how much.

**Sam**: Looking forward to it. Thanks, Alex.

**Alex**: Thank you, Sam. Remember -- the first rule is do not lose money. Everything else is secondary. See you next week.

[VISUAL: End card with channel subscribe prompt and links to previous videos]
