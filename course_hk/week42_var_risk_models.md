<!-- 此檔案需要翻譯為香港繁體中文 -->
<!-- This file needs translation to HK Traditional Chinese -->

# Week 42: Value at Risk and Risk Models

---

## Reading Section

### a) Why This Is Important

Last week we covered the conceptual framework of risk management -- position sizing, stop-losses, risk budgeting, and scenario analysis. This week we put numbers on those concepts. Value at Risk (VaR), Conditional Value at Risk (CVaR), stress testing, and factor risk models are the quantitative tools that institutional investors use every single day to measure, monitor, and manage portfolio risk.

Understanding these tools is critical because:

- **VaR is the industry standard for risk measurement**: Every major bank, hedge fund, pension fund, and insurance company calculates VaR daily. If you want to understand how professionals think about risk, you need to understand VaR. When someone says "our daily VaR is $5 million at the 95% confidence level," they are communicating a specific, quantitative statement about portfolio risk.
- **VaR has well-known limitations that caused real-world disasters**: The 2008 financial crisis exposed critical weaknesses in VaR models. Banks that relied solely on VaR were blindsided by losses that their models said were virtually impossible. Understanding these limitations -- and the tools that address them, like CVaR and stress testing -- is essential for any serious investor.
- **Factor risk models decompose portfolio risk into understandable components**: Rather than viewing your portfolio as a black box with some aggregate risk number, factor models tell you: "40% of your risk comes from your exposure to the overall market, 25% comes from your tilt toward growth stocks, 15% comes from your sector concentration in technology, and 20% comes from stock-specific risk." This decomposition is enormously valuable for understanding WHERE your risk is coming from and whether that is where you WANT it.
- **Stress testing prepares you for events that VaR says cannot happen**: VaR answers the question "What is my worst-case loss on a normal day?" Stress testing answers "What happens when the world goes crazy?" Both questions need answers.
- **These tools are increasingly accessible to individual investors**: Portfolio analytics platforms now offer VaR calculations, factor decompositions, and stress testing to retail investors. Understanding the theory helps you use these tools correctly and interpret their output wisely.

This lesson will teach you how VaR is calculated (three methods), what CVaR adds, how stress testing works, what factor risk models reveal, and -- critically -- where all of these tools fail.

---

### b) What You Need to Know

#### 1. Value at Risk (VaR): The Concept

Value at Risk answers a simple question: "What is the maximum loss I should expect over a given time period, at a given confidence level, under normal market conditions?"

```
VaR DEFINITION

"There is a X% chance that the portfolio will not lose
 more than $Y over the next N days."

THREE PARAMETERS:
  1. Confidence level (typically 95% or 99%)
  2. Time horizon (typically 1 day or 10 days)
  3. Dollar amount (the VaR number itself)

EXAMPLE:
  "1-day 95% VaR = $50,000"
  
  This means:
  - Over any given day
  - There is a 95% probability
  - That the portfolio will not lose more than $50,000
  
  Equivalently:
  - On 1 day out of 20 (5% of trading days)
  - Losses may EXCEED $50,000
  - VaR says NOTHING about how much they exceed it

VISUAL INTERPRETATION:

  Probability
  |
  |     ___________
  |    /           \
  |   /             \
  |  /               \
  | /    95% of      \
  |/    outcomes      \
  |    within here     \
  +-----|---------|---------|---> Portfolio Return
    -$50k    $0       +$80k
        ^
        |
    VaR = $50,000 loss
    (5% of outcomes are
     worse than this)
```

```
VaR AT DIFFERENT CONFIDENCE LEVELS

Portfolio: $1,000,000 in S&P 500 index
Annual volatility: 16%
Daily volatility: 16% / sqrt(252) = 1.01%

         Confidence    Z-Score    1-Day VaR
         ──────────────────────────────────
           90%          1.28      $12,900
           95%          1.65      $16,600
           99%          2.33      $23,500
           99.9%        3.09      $31,200

INTERPRETATION:
  At 95%: We expect to lose more than $16,600
          on about 1 day per month (5% of 20 days)
          
  At 99%: We expect to lose more than $23,500
          on about 2-3 days per year (1% of 252 days)
          
  At 99.9%: We expect to lose more than $31,200
            on about 1 day every 4 years

SCALING VaR ACROSS TIME HORIZONS:
  N-day VaR = 1-day VaR x sqrt(N)
  
  1-day 95% VaR:  $16,600
  5-day 95% VaR:  $16,600 x sqrt(5)  = $37,100
  10-day 95% VaR: $16,600 x sqrt(10) = $52,500
  
  WARNING: Square root scaling assumes returns are
  independent and identically distributed. In reality,
  market crashes cluster (volatility clustering), making
  multi-day VaR larger than the square-root formula suggests.
```

#### 2. Parametric VaR (Variance-Covariance Method)

The simplest VaR method assumes returns follow a normal distribution. It uses only the mean and standard deviation of returns plus the correlations between portfolio components.

```
PARAMETRIC VaR CALCULATION

For a single asset:
  VaR = Portfolio Value x Z-score x sigma x sqrt(T)

Where:
  Z-score: 1.65 for 95%, 2.33 for 99%
  sigma: daily standard deviation of returns
  T: time horizon in days

EXAMPLE: Single stock portfolio
  Portfolio: $200,000 in AAPL
  AAPL daily volatility (sigma): 1.8%
  
  1-day 95% VaR = $200,000 x 1.65 x 0.018
               = $5,940

For a two-asset portfolio:
  Portfolio sigma = sqrt(w1^2*s1^2 + w2^2*s2^2
                        + 2*w1*w2*s1*s2*rho)

Where:
  w1, w2 = portfolio weights
  s1, s2 = asset standard deviations
  rho = correlation between assets

EXAMPLE: Two-stock portfolio
  $120,000 in AAPL (60%), daily vol = 1.8%
  $80,000 in JNJ (40%), daily vol = 1.0%
  Correlation = 0.35

  Portfolio sigma = sqrt(0.6^2 x 0.018^2 + 0.4^2 x 0.01^2
                        + 2 x 0.6 x 0.4 x 0.018 x 0.01 x 0.35)
                 = sqrt(0.0001166 + 0.0000160 + 0.0000302)
                 = sqrt(0.0001628)
                 = 0.01276  (1.276%)

  1-day 95% VaR = $200,000 x 1.65 x 0.01276
               = $4,211

  NOTE: VaR for the two-stock portfolio ($4,211) is LESS
  than VaR for AAPL alone at the same total value ($5,940).
  This is the diversification benefit in action.
```

```
PARAMETRIC VaR: STRENGTHS AND WEAKNESSES

STRENGTHS:
  + Fast to compute (closed-form formula)
  + Easy to understand and explain
  + Only needs means, variances, and correlations
  + Works well for linear instruments (stocks, bonds)
  + Additive across components (can decompose VaR)

WEAKNESSES:
  - Assumes normal distribution of returns
  - Real returns have FAT TAILS (extreme events
    are much more common than normal distribution predicts)
  - Does not handle options well (non-linear payoffs)
  - Assumes constant volatility and correlations
  - Underestimates risk during market stress

NORMAL DISTRIBUTION vs. REALITY:

  Normal distribution predicts:
    > 3 sigma event: once every 740 days (3 years)
    > 4 sigma event: once every 31,560 days (126 years)
    > 5 sigma event: once every 3.5 million days (never)
  
  Actual stock market:
    > 3 sigma event: once every 100-200 days
    > 4 sigma event: once every 2-5 years
    > 5 sigma event: once every 10-20 years
  
  CONCLUSION: Fat tails make parametric VaR dangerously
  optimistic about tail risk. The 2008 crisis produced
  events that a normal distribution said should happen
  once in the lifetime of the universe.
```

#### 3. Historical Simulation VaR

Instead of assuming a distribution, historical simulation uses actual past returns to estimate VaR. It takes your current portfolio and applies historical daily returns to see what would have happened.

```
HISTORICAL SIMULATION VaR: METHOD

Step 1: Collect N days of historical returns
  (typically 250-1000 trading days)

Step 2: Apply each day's returns to current portfolio
  For day i: Hypothetical P&L = Sum of
    (position_j x return_j_on_day_i)
    for all positions j

Step 3: Sort the hypothetical P&L from worst to best

Step 4: VaR = the loss at the Xth percentile
  For 95% VaR with 500 observations:
    VaR = 25th worst day (5% x 500)
  For 99% VaR with 500 observations:
    VaR = 5th worst day (1% x 500)

EXAMPLE: 500 days of data, sorted P&L
  Day rank    P&L           Cumulative %
  ────────────────────────────────────────
  1 (worst)   -$48,200      0.2%
  2           -$41,500      0.4%
  3           -$38,700      0.6%
  4           -$35,100      0.8%
  5           -$32,800      1.0%  <-- 99% VaR
  ...
  24          -$19,400      4.8%
  25          -$18,200      5.0%  <-- 95% VaR
  26          -$17,800      5.2%
  ...
  250         +$500         50.0% (median)
  ...
  500 (best)  +$52,300      100.0%
  
  95% VaR = $18,200
  99% VaR = $32,800
```

```
HISTORICAL SIMULATION: STRENGTHS AND WEAKNESSES

STRENGTHS:
  + No distribution assumption (captures fat tails)
  + Captures actual correlations (including non-linear)
  + Naturally incorporates skewness and kurtosis
  + Handles options and non-linear instruments
  + Intuitive: "what would have happened"

WEAKNESSES:
  - Assumes history repeats (future = past)
  - Limited by available data (cannot model events
    worse than the worst day in your sample)
  - Sample period matters enormously:
    ┌─────────────────────────────────────────────┐
    │  Using 2015-2019 data: Low VaR              │
    │  (calm market, no crisis in sample)         │
    │                                             │
    │  Using 2007-2009 data: High VaR             │
    │  (crisis in sample)                         │
    │                                             │
    │  SAME PORTFOLIO, VERY DIFFERENT VaR         │
    │  depending on which history you choose      │
    └─────────────────────────────────────────────┘
  - Ghost effects: old extreme events drop out of
    the sample window, causing VaR to suddenly drop
    even with no portfolio change
  - Equal weighting of all historical days (a day
    from 3 years ago has same weight as yesterday)
```

#### 4. Monte Carlo VaR

Monte Carlo simulation generates thousands of random scenarios based on assumed statistical properties of asset returns, then calculates VaR from the simulated distribution.

```
MONTE CARLO VaR: METHOD

Step 1: Estimate return distribution parameters
  - Mean returns for each asset
  - Volatilities for each asset
  - Correlation matrix between assets
  - (Optional) Fat tail parameters, skewness

Step 2: Generate N random scenarios (N = 10,000+)
  For each scenario:
    - Draw correlated random returns for all assets
    - Calculate portfolio P&L
  
Step 3: Sort the N portfolio P&L values

Step 4: VaR = loss at the Xth percentile
  For 95% VaR with 10,000 scenarios:
    VaR = 500th worst scenario

CONCEPTUAL DIAGRAM:

  Generate 10,000 random portfolio returns:
  
  Scenario 1:   AAPL -2.1%, JNJ +0.3%  -> P&L: -$2,280
  Scenario 2:   AAPL +1.5%, JNJ +0.8%  -> P&L: +$2,440
  Scenario 3:   AAPL -0.3%, JNJ -0.5%  -> P&L: -$760
  ...
  Scenario 10000: AAPL +0.7%, JNJ -0.2% -> P&L: +$680
  
  Sort all 10,000 P&L values:
  
       Frequency
       |
       |        ___________
       |       /           \
       |      /             \
       |     /               \
       |    /                 \
       |   /                   \
       |  /     10,000          \
       | / simulated outcomes    \__
  _____|/                          \____
  ─────|──────────|─────────────────────> P&L
       ^          $0
       |
  500th worst = 95% VaR
```

```
MONTE CARLO VaR: STRENGTHS AND WEAKNESSES

STRENGTHS:
  + Highly flexible (any distribution assumption)
  + Can model fat tails, skewness, regime changes
  + Handles options and non-linear instruments well
  + Can generate as many scenarios as needed
  + Can incorporate complex dependencies
  + Can model time-varying volatility (GARCH)

WEAKNESSES:
  - Computationally intensive (slow for large portfolios)
  - Model risk: garbage in, garbage out
    (results depend on assumed distributions)
  - Requires careful calibration of parameters
  - Can give false precision (10,000 scenarios sounds
    scientific, but if the model is wrong, all 10,000
    scenarios are wrong)
  - Convergence: need enough scenarios for stable results

COMPARISON OF THREE VaR METHODS:

Feature          Parametric   Historical   Monte Carlo
─────────────────────────────────────────────────────────
Speed            Fast         Medium       Slow
Distribution     Normal only  No assumption Flexible
Fat tails        No           Yes          If modeled
Non-linear       No           Yes          Yes
Transparency     High         High         Medium
Data needed      Stats only   Full history  Parameters
Model risk       Medium       Low          High
Best for         Stocks/bonds All assets   Options/
                                           complex
```

#### 5. Conditional Value at Risk (CVaR / Expected Shortfall)

CVaR, also called Expected Shortfall, answers the question that VaR ignores: "When losses exceed VaR, how bad do they get?"

```
CVaR vs. VaR: THE CRITICAL DIFFERENCE

VaR tells you: "I will not lose more than $X with Y% confidence"
CVaR tells you: "When I DO lose more than VaR, my AVERAGE loss is $Z"

VISUAL:

  Probability
  |
  |     ___________
  |    /           \
  |   /             \
  |  /    95% of     \
  | /    outcomes     \
  |/                   \
  |                     \___
  +────|──────────────|──────|─────> Loss
       0            VaR    CVaR
                   $50k   $78k
       
       ├──── 95% ────┤ 5% │
       
  VaR = $50,000:  "95% of the time, losses stay below $50k"
  CVaR = $78,000: "When losses exceed $50k (the worst 5%),
                   the AVERAGE loss is $78,000"

WHY CVaR IS BETTER:

  Consider two portfolios:
  
  Portfolio A:                Portfolio B:
  95% VaR = $50,000          95% VaR = $50,000
  Worst 5% losses:           Worst 5% losses:
    -$52,000                   -$55,000
    -$55,000                   -$70,000
    -$58,000                   -$95,000
    -$60,000                   -$120,000
    -$65,000                   -$500,000
  CVaR = $58,000              CVaR = $168,000
  
  SAME VaR. Vastly different tail risk.
  VaR cannot distinguish them. CVaR can.
  Portfolio B has hidden catastrophic risk.
```

```
CVaR CALCULATION (HISTORICAL METHOD)

Using the sorted P&L from historical simulation:
500 observations, 95% confidence level

The worst 5% = worst 25 observations

  Rank    P&L
  ──────────────
  1       -$48,200
  2       -$41,500
  3       -$38,700
  4       -$35,100
  5       -$32,800
  6       -$31,200
  7       -$29,500
  8       -$28,100
  9       -$27,000
  10      -$26,200
  ...
  25      -$18,200  <-- This is VaR (95th percentile)
  
  CVaR = Average of ranks 1-25
       = (-$48,200 + -$41,500 + ... + -$18,200) / 25
       = -$29,800

  95% VaR = $18,200 (boundary of worst 5%)
  95% CVaR = $29,800 (average of worst 5%)

  CVaR is 64% larger than VaR in this example.
  This is typical -- CVaR is usually 1.3x to 2.5x VaR
  depending on how fat the tails are.
```

#### 6. Stress Testing

Stress testing goes beyond statistical models to ask: "What happens to my portfolio if a specific extreme event occurs?" Unlike VaR, stress tests are not constrained by historical probabilities or statistical distributions.

```
STRESS TESTING FRAMEWORK

TYPE 1: HISTORICAL STRESS TESTS
  Apply actual historical crisis returns to current portfolio

  ┌────────────────────────────────────────────────────────┐
  │  Event                    S&P    10Y     Credit  Gold  │
  │                           500    Bond    Spreads       │
  │────────────────────────────────────────────────────────│
  │  Black Monday 1987        -20%   +5%     +100bp  +3%  │
  │  LTCM Crisis 1998         -19%   +8%     +200bp  +2%  │
  │  Tech Crash 2000-02       -49%   +20%    +300bp  +5%  │
  │  GFC 2008-09              -57%   +25%    +600bp  +25% │
  │  COVID Crash 2020         -34%   +5%     +400bp  +5%  │
  │  2022 Rate Shock          -25%   -15%    +150bp  -1%  │
  └────────────────────────────────────────────────────────┘

  Apply to current portfolio to estimate impact.

TYPE 2: HYPOTHETICAL STRESS TESTS
  Design plausible future scenarios not seen in history

  Example hypothetical scenarios:
  - China invades Taiwan (supply chain collapse)
  - US sovereign debt downgrade (Treasury selloff)
  - AI bubble burst (tech sector -60%)
  - Global pandemic worse than COVID
  - Simultaneous stock AND bond crash (-30% / -15%)

TYPE 3: SENSITIVITY ANALYSIS (Factor Shocks)
  Change one risk factor at a time and measure impact

  Interest rates: +100bp, +200bp, +300bp
  S&P 500: -10%, -20%, -30%, -40%
  VIX: 25, 35, 50, 80
  Credit spreads: +100bp, +200bp, +400bp
  USD: +10%, -10%
```

```
STRESS TEST: WORKED EXAMPLE

Portfolio: $600,000
  40% US Equities       ($240,000)
  20% Int'l Equities    ($120,000)
  25% US Agg Bonds      ($150,000)
  10% REITs             ($60,000)
  5%  Gold              ($30,000)

STRESS TEST: 2008-STYLE FINANCIAL CRISIS

Asset Class       Crisis Return    Dollar Impact
──────────────────────────────────────────────────
US Equities       -50%             -$120,000
Int'l Equities    -55%             -$66,000
US Agg Bonds      +8%              +$12,000
REITs             -65%             -$39,000
Gold              +25%             +$7,500
──────────────────────────────────────────────────
TOTAL                              -$205,500
Portfolio drawdown:                -34.3%

STRESS TEST: 2022-STYLE RATE SHOCK

Asset Class       Crisis Return    Dollar Impact
──────────────────────────────────────────────────
US Equities       -25%             -$60,000
Int'l Equities    -20%             -$24,000
US Agg Bonds      -13%             -$19,500
REITs             -30%             -$18,000
Gold              -2%              -$600
──────────────────────────────────────────────────
TOTAL                              -$122,100
Portfolio drawdown:                -20.4%

NOTE: The 2022 scenario is worse for bonds but better
for equities. The 2008 scenario is worse for equities.
A truly robust portfolio should survive BOTH.

STRESS TEST: HYPOTHETICAL WORST CASE
(Simultaneous equity crash + rate spike + credit crisis)

Asset Class       Crisis Return    Dollar Impact
──────────────────────────────────────────────────
US Equities       -45%             -$108,000
Int'l Equities    -50%             -$60,000
US Agg Bonds      -10%             -$15,000
REITs             -55%             -$33,000
Gold              +15%             +$4,500
──────────────────────────────────────────────────
TOTAL                              -$211,500
Portfolio drawdown:                -35.3%

Is -35% survivable? Depends on investor.
If not: increase bond allocation, add TIPS, add cash.
```

#### 7. Factor Risk Models

Factor risk models decompose portfolio risk into systematic (factor) risk and idiosyncratic (stock-specific) risk. They answer the question: "Where is my risk coming from?"

```
FACTOR RISK MODEL: CONCEPTUAL STRUCTURE

Total portfolio risk = Factor risk + Specific risk

FACTOR RISK: Risk from exposure to common factors
  that affect many stocks simultaneously.
  
  Common factors:
  ┌─────────────────────────────────────────────────┐
  │  MARKET        Overall market movement          │
  │  SIZE          Small cap vs. large cap          │
  │  VALUE         Value vs. growth                 │
  │  MOMENTUM      Recent winners vs. losers        │
  │  QUALITY       Profitable vs. unprofitable      │
  │  VOLATILITY    Low vol vs. high vol             │
  │  SECTOR        Industry exposure                │
  │  COUNTRY       Geographic exposure              │
  │  INTEREST RATE Sensitivity to rate changes      │
  │  CREDIT        Sensitivity to credit conditions │
  └─────────────────────────────────────────────────┘

SPECIFIC RISK: Risk unique to individual stocks
  (earnings surprises, management changes, lawsuits, etc.)
  
  Specific risk can be diversified away with enough
  positions. Factor risk cannot.

RISK DECOMPOSITION DIAGRAM:

  Total Portfolio Risk: 100%
  ┌──────────────────────────────────────────────┐
  │                                              │
  │  Factor Risk: 75%              Specific: 25% │
  │  ┌────────────────────────┐    ┌───────────┐ │
  │  │ Market    40%          │    │ Stock A 5% │ │
  │  │ Growth    15%          │    │ Stock B 4% │ │
  │  │ Tech sect 10%         │    │ Stock C 3% │ │
  │  │ Momentum   5%          │    │ ...        │ │
  │  │ Other      5%          │    │ Stock N 2% │ │
  │  └────────────────────────┘    └───────────┘ │
  │                                              │
  └──────────────────────────────────────────────┘
```

```
FACTOR RISK DECOMPOSITION: EXAMPLE

Portfolio: 15 stocks, heavily weighted in tech growth

FACTOR EXPOSURES (BETAS):
  Market beta:     1.15  (15% more market risk than index)
  Size factor:    -0.20  (tilted toward large cap)
  Value factor:   -0.45  (heavily tilted toward growth)
  Momentum:       +0.30  (tilted toward recent winners)
  Tech sector:    +0.35  (overweight technology)
  
RISK CONTRIBUTION BY FACTOR:

  Factor           Exposure    Factor Vol    Risk
                   (Beta)      (Annual)      Contribution
  ────────────────────────────────────────────────────────
  Market            1.15        16%          42%
  Value (growth)   -0.45        10%          18%
  Tech sector       0.35        12%          14%
  Momentum          0.30         8%           8%
  Size             -0.20         6%           3%
  Other factors     various     various       5%
  ────────────────────────────────────────────────────────
  TOTAL FACTOR RISK                          90%
  Specific risk                              10%
  ────────────────────────────────────────────────────────
  TOTAL                                     100%

INTERPRETATION:
  This portfolio's risk is 90% driven by factors and
  only 10% by individual stock selection.
  
  The largest risk is MARKET exposure (42%), followed
  by GROWTH tilt (18%) and TECH concentration (14%).
  
  ACTION ITEMS:
  - If you want less risk, reduce market beta (add bonds)
  - If you want less factor concentration, balance
    growth with some value exposure
  - The tech overweight contributes 14% of risk;
    consider diversifying sectors
  - Specific risk is low (10%), meaning diversification
    across 15 stocks has done its job
```

#### 8. Limitations of VaR and Risk Models

No discussion of risk models is complete without a thorough understanding of their limitations. These limitations have caused real-world catastrophes.

```
CRITICAL LIMITATIONS OF VaR

LIMITATION 1: VaR SAYS NOTHING ABOUT TAIL LOSSES
  VaR: "95% of the time, losses will not exceed $50,000"
  
  But what about the other 5%?
  Could be -$55,000 or -$5,000,000
  VaR treats both the same.
  
  SOLUTION: Use CVaR (Expected Shortfall) to measure
  the average loss in the tail.

LIMITATION 2: VaR ASSUMES "NORMAL" CONDITIONS
  VaR is calibrated to normal market behavior.
  During crises, volatilities spike, correlations
  change, liquidity evaporates, and the rules change.
  
  The worst days in market history all look like this:
  
  VaR said:    "Worst case is -3%"
  Reality:     "-12% in one day"
  Explanation: "That was a 9-sigma event"
  Translation: "Our model was wrong"
  
  SOLUTION: Supplement VaR with stress tests that
  do not rely on normal-market assumptions.

LIMITATION 3: VaR CREATES FALSE CONFIDENCE
  ┌─────────────────────────────────────────────┐
  │                                             │
  │  "Our VaR is only $5 million, so we can     │
  │   increase leverage."                       │
  │                                             │
  │  This reasoning CAUSED the 2008 crisis.     │
  │  Banks used low VaR numbers to justify      │
  │  extreme leverage. When VaR models broke    │
  │  down during the crisis, losses were        │
  │  10-50x the VaR estimate.                   │
  │                                             │
  │  RULE: VaR is a MINIMUM risk estimate,      │
  │  not a maximum. Actual losses can and will  │
  │  exceed VaR regularly.                      │
  │                                             │
  └─────────────────────────────────────────────┘

LIMITATION 4: CORRELATION BREAKDOWN
  VaR models assume correlations are stable.
  During crises, correlations spike toward 1.0.
  
  Normal market:          Crisis:
  Stock A ── 0.3 ── Stock B   Stock A ── 0.9 ── Stock B
  Stock A ── 0.2 ── Stock C   Stock A ── 0.85── Stock C
  
  Diversification benefit disappears precisely when
  you need it most. VaR understates crisis-period risk.

LIMITATION 5: LIQUIDITY RISK IS INVISIBLE TO VaR
  VaR assumes you can sell at current market prices.
  During crises, bid-ask spreads widen 5-10x, some
  assets become completely illiquid.
  
  Your VaR might say: "Sell $1M of bonds at -2% loss"
  Reality during crisis: "Cannot sell bonds at any price"
  
  SOLUTION: Apply liquidity adjustments to VaR.
  Add extra risk for illiquid positions.

LIMITATION 6: MODEL RISK
  Every VaR model is wrong. The question is how wrong.
  
  Parametric VaR: wrong because returns are not normal
  Historical VaR: wrong because the future is not the past
  Monte Carlo VaR: wrong because the model is misspecified
  
  Using VaR without understanding its limitations
  is worse than not using VaR at all, because it
  creates an illusion of precision.
```

```
THE "COBRA EFFECT" OF VaR

Named after a real historical event in colonial India
where a bounty on cobras led to cobra FARMING, making
the problem worse.

VaR can create perverse incentives:

1. VaR-CONSTRAINED TRADERS:
   Traders with VaR limits may restructure portfolios
   to minimize REPORTED VaR while taking on the same
   or MORE actual risk.
   
   Example: Selling deep out-of-the-money options
   has very low VaR (small daily move expected)
   but enormous tail risk (catastrophic if exercised).
   
   VaR says: "Low risk"
   Reality: "Picking up pennies in front of steamrollers"

2. PROCYCLICALITY:
   In calm markets: VaR is low -> take more risk
   In volatile markets: VaR rises -> forced to sell
   
   This creates a feedback loop:
   ┌──────────────────────────────────────────┐
   │  Market drops                            │
   │     ↓                                    │
   │  Volatility rises                        │
   │     ↓                                    │
   │  VaR increases                           │
   │     ↓                                    │
   │  Risk limits breached                    │
   │     ↓                                    │
   │  Forced selling to reduce VaR            │
   │     ↓                                    │
   │  Market drops further                    │
   │     ↓                                    │
   │  REPEAT                                  │
   └──────────────────────────────────────────┘
   
   VaR-based risk management can AMPLIFY crashes.
```

#### 9. Putting It All Together: A Complete Risk Measurement Framework

```
COMPREHENSIVE RISK MEASUREMENT APPROACH

Do not rely on any single measure. Use ALL of these:

  ┌──────────────────────────────────────────────────────┐
  │  MEASURE        PURPOSE         WHAT IT CATCHES      │
  │──────────────────────────────────────────────────────│
  │  VaR (95%)      Daily risk      Normal daily losses  │
  │  VaR (99%)      Tail risk       Rare but plausible   │
  │  CVaR           Tail severity   How bad the bad gets │
  │  Stress tests   Extreme events  Model-free scenarios │
  │  Factor decomp  Risk sources    Where risk comes from│
  │  Concentration  Single names    Idiosyncratic risk   │
  │  Correlation    Diversification Hidden dependencies  │
  │  Drawdown       Cumulative loss Sustained declines   │
  │  Liquidity      Exit ability    Can you sell?         │
  └──────────────────────────────────────────────────────┘

RISK DASHBOARD (what professionals monitor daily):

  ┌─────────────────────────────────────┐
  │  RISK DASHBOARD - April 12, 2026   │
  │                                     │
  │  Portfolio Value:    $500,000        │
  │  Daily P&L:          -$2,100        │
  │                                     │
  │  1-Day 95% VaR:     $8,200         │
  │  1-Day 99% VaR:     $14,500        │
  │  10-Day 95% VaR:    $25,900        │
  │  95% CVaR:          $18,600        │
  │                                     │
  │  Portfolio Vol:      14.2% (ann)    │
  │  Market Beta:        0.85           │
  │  Sharpe Ratio:       1.12           │
  │                                     │
  │  Max Drawdown (YTD): -6.3%         │
  │  Current Drawdown:   -2.1%         │
  │                                     │
  │  Largest Position:   AAPL (7.2%)   │
  │  Largest Sector:     Tech (28.1%)  │
  │                                     │
  │  STRESS TEST RESULTS:              │
  │  2008-style crisis: -31.2%         │
  │  Rate shock +300bp: -18.7%         │
  │  Tech crash -50%:   -22.4%         │
  │                                     │
  │  ALERTS: None                       │
  └─────────────────────────────────────┘
```

---

### c) Common Misconceptions

**Misconception 1: "VaR tells me my maximum possible loss."**

VaR tells you the loss that will be exceeded a certain percentage of the time. It is a threshold, not a ceiling. If your 95% VaR is $50,000, you should expect to lose MORE than $50,000 about once a month (one day in twenty). VaR says nothing about how much more. Your actual loss could be $55,000 or $500,000. This is why CVaR exists -- it measures the average loss when VaR is exceeded.

**Misconception 2: "A lower VaR always means a safer portfolio."**

A portfolio can have low VaR but extreme tail risk. Selling deep out-of-the-money put options has very low VaR because the daily expected loss is tiny. But the tail risk is catastrophic -- the position can lose 10-50 times its VaR in a single day. This is exactly the risk profile that destroyed Long-Term Capital Management, AIG, and numerous hedge funds. Low VaR with high CVaR is a major warning sign.

**Misconception 3: "Historical VaR captures all the risks because it uses real data."**

Historical VaR can only capture events that occurred in your data window. If your window is 2015-2019, it does not contain a financial crisis. Your VaR will dramatically understate the risk of crisis-type events. Even a 20-year window may not contain the specific type of crisis that hits next. Historical simulation is useful but must be supplemented with hypothetical stress tests.

**Misconception 4: "Monte Carlo simulation gives accurate results because it runs thousands of scenarios."**

Running 10,000 scenarios sounds impressive, but if the underlying model is wrong, all 10,000 scenarios are wrong. Monte Carlo is only as good as the assumptions about return distributions, correlations, and volatilities that you feed into it. Garbage in, garbage out -- but with 10,000 rows of garbage instead of one. The precision of the output far exceeds the accuracy of the inputs.

**Misconception 5: "Factor risk models capture all sources of risk."**

Factor models capture systematic risk -- the risk from exposure to known factors like market, size, value, and momentum. But they miss event risk (a specific company's CEO being arrested), liquidity risk (an asset becoming impossible to sell), and structural risk (an entire market closing, as happened with Russian stocks in 2022). Factor models are a powerful lens but not a complete picture.

**Misconception 6: "Stress testing is only for institutions."**

Individual investors can and should run simple stress tests. Take your current portfolio and ask: "What happens if the stock market drops 40%? What happens if interest rates rise 3%? What happens if my largest holding goes to zero?" You do not need a Bloomberg terminal. You need a spreadsheet and an honest assessment of each position's sensitivity to extreme moves. If the worst case is unsurvivable, reduce risk now, before the event occurs.

---

### d) Common Questions and Answers

**Q1: What confidence level and time horizon should I use for VaR?**

A: For daily monitoring, 95% 1-day VaR is standard. It gives you a practical sense of your daily risk. For risk budgeting and limit-setting, 99% 10-day VaR is more common because it captures more severe events over a longer horizon. Banks are required by regulators to use 99% 10-day VaR for capital calculations. As an individual investor, 95% 1-day VaR is sufficient for monitoring, but always supplement with CVaR and stress tests.

**Q2: How many days of historical data should I use for historical simulation VaR?**

A: At minimum, 250 trading days (one year). Ideally, 500-1000 days (2-4 years). Using less than 250 days produces unstable estimates. Using more than 1000 days includes very old data that may not be relevant to current market conditions. Some practitioners use exponentially weighted data, where recent observations get more weight than older ones, to balance recency with sample size.

**Q3: Can I calculate VaR for my personal portfolio?**

A: Yes. The simplest approach is to calculate the daily volatility of your portfolio's historical returns and multiply by the appropriate z-score. If your portfolio's daily standard deviation is 0.8%, your 95% 1-day VaR is 0.8% x 1.65 = 1.32% of portfolio value. On a $300,000 portfolio, that is $3,960. Many portfolio analytics tools (Portfolio Visualizer, Morningstar, some brokerage platforms) provide VaR calculations automatically.

**Q4: What is the difference between VaR and maximum drawdown?**

A: VaR measures the worst expected loss on a single day (or short period) at a given confidence level. Maximum drawdown measures the largest peak-to-trough decline over a given period, which can span weeks or months. A portfolio can have low daily VaR but a large maximum drawdown if it experiences many consecutive small losses. For long-term investors, maximum drawdown is often a more meaningful risk measure because it captures the cumulative impact of sustained declines.

**Q5: How do banks use VaR for regulation?**

A: Under Basel III regulations, banks must hold capital equal to at least 3 times their 99% 10-day VaR. This is meant to ensure banks have enough capital to survive extreme events. After 2008, regulators added Stressed VaR (VaR calculated using crisis-period data) and the Fundamental Review of the Trading Book (FRTB) framework, which replaces VaR with Expected Shortfall (CVaR) as the primary risk measure. The shift to CVaR reflects the recognition that VaR's blindness to tail severity was a major contributor to the crisis.

**Q6: How do I stress test a portfolio with options?**

A: Options stress testing requires repricing options under each stress scenario using an options pricing model (Black-Scholes or similar). You cannot simply apply percentage moves to option values because options have non-linear payoffs. If you own a call option and the stock drops 30%, the option might lose 60%, 80%, or 100% depending on its strike price and time to expiration. Most brokerage platforms with options trading offer a "what-if" or "theoretical" tool that reprices your options under different scenarios. Use these tools.

**Q7: Why did regulators shift from VaR to CVaR after the financial crisis?**

A: VaR's fundamental flaw is that it ignores the severity of tail losses. Two portfolios can have identical VaR but dramatically different tail risk. Before 2008, banks optimized their portfolios to minimize VaR, which led them to take on positions with enormous tail risk but low day-to-day risk (like mortgage-backed securities). CVaR penalizes tail severity, so portfolios optimized for CVaR are more robust to extreme events. The shift from VaR to CVaR in regulation is one of the most important post-crisis reforms.

---

---

## YouTube Script

**Week 42: Value at Risk and Risk Models**

[VISUAL: Title card -- "VaR, CVaR, and Risk Models: Quantifying Portfolio Risk"]

**Alex**: Last week we covered the conceptual foundations of risk management. This week we are going to put numbers on everything. We are going to learn how institutions measure risk, where those measurements fail, and how to build a complete risk framework.

**Sam**: This is the quantitative side -- the math behind risk management.

**Alex**: Right. And the centerpiece of institutional risk measurement is Value at Risk, or VaR. It is the most widely used risk metric in finance.

**Sam**: I have heard the term but never really understood what it means.

[VISUAL: VaR definition with bell curve diagram]

**Alex**: VaR answers one specific question: "What is the maximum loss I should expect on a normal day, at a given confidence level?" For example, "there is a 95% probability that the portfolio will not lose more than $50,000 in a single day." That is a 95% 1-day VaR of $50,000.

**Sam**: So on 95 out of 100 days, losses will be less than $50,000?

**Alex**: Exactly. But here is the critical nuance that most people miss. VaR says NOTHING about what happens on the other 5 days. The loss could be $55,000 or $5 million. VaR only tells you about the boundary -- the 95th percentile. It is a fence, not a wall.

**Sam**: That seems like a pretty big gap. How do you know what happens beyond the fence?

**Alex**: That is exactly the right question, and it is what led to the 2008 crisis. But we will get there. First, let me explain the three ways VaR is calculated, because the method matters a lot.

[VISUAL: "Three Methods of Calculating VaR" overview slide]

**Alex**: Method one is parametric VaR, also called the variance-covariance method. It is the simplest. You assume that returns follow a normal distribution -- the classic bell curve. Then VaR is just a formula.

**Sam**: What is the formula?

**Alex**: VaR equals your portfolio value times the z-score times the portfolio's daily standard deviation. For 95% confidence, the z-score is 1.65. For 99%, it is 2.33. If your portfolio is $500,000 and the daily standard deviation is 1%, your 95% VaR is $500,000 times 1.65 times 0.01, which equals $8,250.

[VISUAL: Step-by-step parametric VaR calculation]

**Sam**: That seems straightforward. What is the catch?

**Alex**: The catch is the assumption of normality. Real stock market returns have fat tails -- extreme events happen far more often than a normal distribution predicts. A normal distribution says a 4-sigma event should happen once every 126 years. In reality, it happens every 2-5 years. A 5-sigma event should theoretically happen once in 3.5 million years. The stock market has had several in just the last few decades.

[ANIMATION: animation/week42_fat_tails.py -- Animated overlay of the normal distribution (bell curve) and the actual distribution of S&P 500 daily returns from 1950 to 2025. The animation starts with both distributions overlapping at the center, looking nearly identical. Then it zooms into the left tail (losses), where the actual distribution dramatically exceeds the normal distribution. Annotations appear pointing to specific extreme days: Black Monday 1987 (-22.6%), COVID crash March 2020 (-12%), Flash Crash 2010 (-9%), and several other events. A counter tallies the number of actual events beyond 3, 4, and 5 standard deviations compared to what the normal distribution predicts. The difference is striking: hundreds of events where the normal model predicted single digits.]

**Sam**: That is shocking. The fat tails are dramatically thicker than the normal distribution predicts. So parametric VaR, which assumes normality, systematically underestimates the probability of extreme losses?

**Alex**: Precisely. Parametric VaR works fine for measuring the risk of ordinary daily movements. But it fails catastrophically at measuring tail risk -- the very risk that can destroy your portfolio.

**Sam**: What is method two?

**Alex**: Historical simulation. Instead of assuming a distribution, you take actual historical data. You collect hundreds of past daily returns for your portfolio's assets. Then you apply each historical day's returns to your current portfolio and ask, "What would my P&L have been?" You sort all the hypothetical P&L values from worst to best, and VaR is just the loss at the 5th percentile.

[VISUAL: Sorted histogram of historical simulation results with VaR marked]

**Sam**: That seems much better. No assumptions about normality.

**Alex**: It has advantages. It captures fat tails because they are in the actual data. It captures the actual correlations between assets. And it handles non-linear instruments like options better than parametric VaR.

**Sam**: But there is a catch here too.

**Alex**: Two catches. First, it assumes the future will look like the past. If your historical window is 2015-2019 -- a calm bull market -- your VaR will be low because there were no crises in that period. But that does not mean crises will not happen going forward.

**Sam**: Cherry-picking the sample period.

**Alex**: It does not even require intentional cherry-picking. Any fixed window automatically excludes some historical events. The second catch is the ghost effect. When an extreme day rolls off the end of your data window, VaR can drop overnight even though nothing about your portfolio changed. On January 1st of a new year, the worst day from four years ago might fall out of your 1000-day window, and suddenly your VaR looks 20% lower.

[VISUAL: Timeline showing data window shifting and extreme events falling off]

**Sam**: That is unsettling. What about the third method?

**Alex**: Monte Carlo simulation. This is the most sophisticated approach. You build a mathematical model of how your assets behave -- their expected returns, volatilities, correlations, and importantly, the shape of the return distribution including fat tails. Then you generate thousands of random scenarios from this model and calculate VaR from the simulated distribution.

[ANIMATION: animation/week42_monte_carlo.py -- Animated Monte Carlo simulation for a two-asset portfolio. The animation begins with 100 random return pairs being generated and plotted on a scatter plot, showing the correlation structure between the two assets. This scales up rapidly to 1,000, then 5,000, then 10,000 scenarios. A histogram of total portfolio returns builds up on the side as scenarios accumulate. The 95th percentile loss is marked and labeled as VaR. A convergence chart in the corner shows how the VaR estimate stabilizes as more scenarios are added, starting volatile with few scenarios and settling to a stable value by 10,000. The final frame compares the Monte Carlo VaR to the parametric VaR, showing the Monte Carlo estimate is larger due to the fat-tailed distribution used in the simulation.]

**Sam**: So Monte Carlo can model fat tails if you tell it to?

**Alex**: Exactly. You can use Student's t-distribution or other fat-tailed distributions instead of the normal distribution. You can model time-varying volatility. You can model regime changes. Monte Carlo is as good as the model you put into it.

**Sam**: And that is also its weakness -- it is only as good as the model.

**Alex**: Right. If your model is wrong, running 10,000 scenarios of a wrong model just gives you 10,000 wrong answers. This is called model risk. The output looks precise and scientific -- four decimal places, thousands of scenarios -- but the precision is meaningless if the underlying assumptions are flawed.

[VISUAL: Comparison table of three VaR methods -- strengths and weaknesses]

**Sam**: OK, so all three VaR methods have limitations. What do we do about it?

**Alex**: This is where CVaR -- Conditional Value at Risk, also called Expected Shortfall -- comes in. CVaR answers the question that VaR ignores: "When losses exceed VaR, how bad do they get?"

[VISUAL: Bell curve diagram showing VaR boundary and CVaR region in the tail]

**Alex**: VaR tells you the boundary of the worst 5% of outcomes. CVaR tells you the AVERAGE loss within that worst 5%. If your 95% VaR is $50,000, your CVaR might be $78,000. That means when you have a really bad day -- worse than VaR -- the average loss is about $78,000, not $50,000.

**Sam**: Why is that distinction important?

**Alex**: Because two portfolios can have identical VaR but completely different CVaR. Imagine Portfolio A and Portfolio B both have a 95% VaR of $50,000. But Portfolio A's worst days are clustered around $55,000-$65,000, while Portfolio B's worst days include occasional losses of $200,000 or even $500,000. Portfolio A's CVaR might be $58,000. Portfolio B's CVaR might be $168,000.

**Sam**: Same VaR, totally different risk.

**Alex**: Exactly. And this is not a theoretical concern. Before 2008, many banks had portfolios with moderate VaR but extreme CVaR. They were selling insurance on rare events -- credit default swaps, deep out-of-the-money options -- which had small daily risk but catastrophic tail risk. VaR could not see the difference. CVaR can.

**Sam**: Is that why regulators switched from VaR to CVaR after the crisis?

**Alex**: Precisely. The Basel Committee, which sets global banking regulations, introduced the Fundamental Review of the Trading Book, which replaces VaR with Expected Shortfall as the primary risk measure. CVaR penalizes tail severity, so banks can no longer hide tail risk behind low VaR numbers.

[VISUAL: VaR vs. CVaR for two portfolios with identical VaR but different tail risk]

**Sam**: Let us talk about stress testing. You mentioned this last week as a complement to statistical models.

[VISUAL: "Stress Testing" section header]

**Alex**: Stress testing is fundamentally different from VaR and CVaR. Those are statistical -- they ask, "What is the probability distribution of losses?" Stress testing is scenario-based -- it asks, "What happens if THIS specific thing occurs?"

**Sam**: Give me examples of stress scenarios.

**Alex**: There are three types. First, historical stress tests. You take actual past crises and apply them to your current portfolio. What would have happened to my portfolio during the 2008 financial crisis? During the COVID crash? During the 2022 rate shock?

**Sam**: But my portfolio is different from what I would have held during those periods.

**Alex**: That is exactly the point. You apply those historical market moves to your CURRENT portfolio. You know that during the 2008 crisis, the S&P 500 fell 57%, international stocks fell 55%, US bonds rose 8%, REITs fell 65%, and gold rose 25%. Apply those moves to whatever you are holding today.

[VISUAL: Historical stress test applied to a sample portfolio]

**Alex**: Second type: hypothetical stress tests. You design scenarios that have not happened but are plausible. What if China invades Taiwan and global supply chains collapse? What if the US government defaults on its debt? What if AI causes a technology sector crash of 60%?

**Sam**: Those sound extreme.

**Alex**: They are extreme. That is the point. You are testing the limits of your portfolio's resilience. If a plausible extreme scenario would destroy your portfolio, you need to know that before it happens, not after.

**Sam**: And the third type?

**Alex**: Sensitivity analysis or factor shocks. You change one risk factor at a time and measure the impact. What happens if interest rates rise 200 basis points? What happens if the S&P drops 30%? What happens if the VIX spikes to 60? This gives you a factor-by-factor understanding of your portfolio's vulnerabilities.

[ANIMATION: animation/week42_stress_test.py -- Interactive stress test dashboard animation. A sample portfolio is displayed: 40% US equities, 20% international equities, 25% bonds, 10% REITs, 5% gold. Five stress scenarios appear as tabs: 2008 crisis, COVID crash, 2022 rate shock, stagflation, and tech bubble burst. When each tab is selected, the portfolio bars animate to show the impact of each scenario on each asset class, with the total portfolio loss prominently displayed. The worst scenario (2008 crisis) is highlighted with a red warning, showing a -34% total portfolio loss. The animation then shows the portfolio being rebalanced -- reducing equities, adding more bonds and gold -- and the stress test results recalculate in real-time, showing improvement in the worst-case scenario.]

**Sam**: That is really powerful. You can see exactly how portfolio changes affect your worst-case outcomes.

**Alex**: And notice that the 2008 scenario and the 2022 scenario stress different parts of the portfolio. In 2008, stocks were devastated but bonds were a safe haven. In 2022, BOTH stocks and bonds fell because rising interest rates hurt both. A portfolio that survived 2008 might not survive a repeat of 2022, and vice versa. Good stress testing uses multiple scenarios.

**Sam**: Let us move to factor risk models. What are those?

[VISUAL: "Factor Risk Models" section header]

**Alex**: Factor risk models decompose your portfolio's total risk into components. Instead of saying "my portfolio has 14% volatility," a factor model says "6% of that volatility comes from market exposure, 3% comes from your tilt toward growth stocks, 2% comes from tech sector concentration, and 3% comes from individual stock selection."

**Sam**: So it tells you WHERE your risk is coming from?

**Alex**: Exactly. And that is incredibly valuable because it tells you whether your risk is intentional or accidental. If you are a growth investor and 25% of your risk comes from your growth factor exposure, that is intentional -- you chose to tilt toward growth. But if 15% of your risk comes from an unintended concentration in technology, that might be accidental, and you might want to fix it.

[VISUAL: Factor risk decomposition pie chart for a sample portfolio]

**Alex**: The major risk factors in equity markets are market (overall market direction), size (small vs. large cap), value (value vs. growth), momentum (recent winners vs. losers), quality (profitable vs. unprofitable companies), and low volatility (calm vs. volatile stocks). Then there are sector factors and country factors.

**Sam**: How does this help me practically?

**Alex**: Let me give you a concrete example. Say you have 15 stocks and your factor model tells you: market exposure contributes 42% of your risk, growth tilt contributes 18%, tech sector contributes 14%, and momentum contributes 8%. The remaining 18% is stock-specific.

**Sam**: That sounds like a typical growth-oriented tech portfolio.

**Alex**: It is. And the factor model reveals something important. If the market drops 20%, you can expect to lose about 23% because your market beta is 1.15. If growth stocks specifically underperform value by 10%, you will lose an additional 4.5% from your growth tilt. If the tech sector drops relative to the market, there is another hit. Your risks are stacked.

**Sam**: And those risks are correlated. They could all hit at once.

**Alex**: Which is exactly what happened in 2022. The market dropped, growth underperformed value dramatically, and tech was one of the worst-performing sectors. A portfolio with heavy market, growth, and tech factor exposure got hit three different ways simultaneously.

[VISUAL: Factor exposure diagram showing how multiple factor risks can stack]

**Sam**: So factor models help you avoid unintentional risk concentration across factors?

**Alex**: Precisely. If you want to take growth risk, do it knowingly and limit it. If you want tech exposure, size it appropriately. Factor models turn a vague sense of "I think I am diversified" into a precise measurement of where your risk actually sits.

**Sam**: Let us come back to the limitations we keep hinting at. VaR failed spectacularly in 2008. What happened?

[VISUAL: "When Risk Models Fail" section header]

**Alex**: The 2008 crisis is the definitive case study of VaR failure. Let me walk through what went wrong.

**Alex**: Before the crisis, banks held enormous portfolios of mortgage-backed securities. Their VaR models used historical data from a period when housing prices had never declined nationwide. The models showed low risk because the historical data contained no housing crashes.

**Sam**: So the models literally could not imagine the scenario that occurred?

**Alex**: Correct. And it was worse than that. VaR created a false sense of security that encouraged banks to take MORE risk. "Our VaR is only $50 million, so we can lever up further." The low VaR number was used to justify 30-to-1 leverage. When the crisis hit and losses exceeded VaR by 10 to 50 times, the leverage amplified those losses into existential threats.

[VISUAL: Pre-crisis bank leverage ratios and VaR estimates vs. actual losses]

**Alex**: There is also the procyclicality problem. When markets are calm, VaR is low, which encourages risk-taking. When markets become volatile, VaR rises, which forces selling. The forced selling makes markets more volatile, which raises VaR further, which forces more selling. VaR-based risk management can amplify market crashes instead of preventing them.

**Sam**: It is a feedback loop -- the same kind we saw with volatility products.

**Alex**: Exactly. And there is one more subtle problem called the cobra effect. When traders are given VaR limits, they find ways to minimize reported VaR while taking on enormous tail risk. Selling deep out-of-the-money options has very low VaR because the daily expected loss is tiny. But the tail risk is catastrophic. VaR cannot see it.

**Sam**: So VaR is actually dangerous if it is your only risk measure?

**Alex**: It is potentially more dangerous than having no risk measure at all, because it creates an illusion of safety. That is why the modern approach uses VaR as one tool among many: VaR for daily risk monitoring, CVaR for tail severity, stress tests for extreme scenarios, factor models for risk decomposition, and concentration analysis for single-name risk.

[VISUAL: Complete risk measurement framework showing all tools and their purposes]

**Sam**: How should an individual investor use all of this?

**Alex**: Here is my practical recommendation. First, calculate your portfolio's VaR using a free tool like Portfolio Visualizer. This gives you a baseline daily risk number. Second, understand that your actual worst-case loss is probably 2-3 times your VaR -- that is a rough CVaR estimate. Third, run simple stress tests in a spreadsheet. Take your positions and apply 2008-style returns, 2020-style returns, and 2022-style returns. If any scenario produces a loss you cannot tolerate, reduce risk. Fourth, check your factor exposures. Most brokerages now show you this. Are you unintentionally concentrated in growth, tech, or momentum?

**Sam**: That is manageable. VaR for daily monitoring, stress tests for extreme scenarios, and factor analysis for understanding risk sources.

**Alex**: And always remember: every model is wrong. The goal is not to predict the future perfectly. The goal is to be approximately right about the range of outcomes, prepare for the worst plausible case, and have a plan for when the models fail -- because they will fail.

**Sam**: Let me summarize. VaR measures the maximum expected loss at a given confidence level. Three methods: parametric (simple, assumes normality), historical simulation (uses real data, limited by history), and Monte Carlo (flexible, limited by model quality). CVaR measures the average loss in the tail. Stress testing measures the impact of specific extreme scenarios. Factor models decompose risk into systematic components. And no single tool is sufficient -- you need all of them, plus healthy skepticism.

**Alex**: Perfect. And if you remember nothing else from today, remember this: the models that failed in 2008 were not stupid. They were built by brilliant people with PhDs. They failed because they assumed the future would look like the recent past, and it did not. The same models might fail again, in a different way. Risk management is not about having the right model. It is about knowing that every model is wrong and planning accordingly.

**Sam**: That is a humbling thought.

**Alex**: It should be. Humility is the most important risk management tool of all. If you think your model has captured all the risks, you are the most dangerous person in the room.

[VISUAL: "Next week: Active Portfolio Management"]

**Alex**: Next week we shift gears from risk to return. We will cover alpha, beta, tracking error, information ratio, active share, and performance attribution -- the tools for understanding whether active management is actually adding value.

**Sam**: From measuring risk to measuring skill.

**Alex**: Exactly. And spoiler alert -- most active managers do not have as much skill as they think they do. The tools we will learn next week help you tell the difference.

**Sam**: Looking forward to it. Thanks, Alex.

**Alex**: Thank you, Sam. Remember -- the model is always wrong. Plan for it. See you next week.

[VISUAL: End card with channel subscribe prompt and links to previous videos]
