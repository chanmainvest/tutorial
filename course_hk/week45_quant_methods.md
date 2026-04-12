<!-- 此檔案需要翻譯為香港繁體中文 -->
<!-- This file needs translation to HK Traditional Chinese -->

# Week 45: Quantitative Methods for Investors

---

## Reading Section

### a) Why This Is Important

Behind every investment decision lies a number, a relationship, or a pattern that someone claims to have discovered. Fund managers say their strategy "generates alpha." Financial advisors show charts proving that their method "works." Bloggers proclaim that gold prices predict stock market crashes, or that the January effect guarantees profits. But how do you know if any of these claims are real?

Quantitative methods -- the application of statistical and mathematical tools to financial data -- are the investor's defense against being fooled by randomness, sold on spurious patterns, and misled by well-intentioned but statistically illiterate analysis. Understanding these tools is critical because:

- **Most claimed patterns in financial data are false**: With thousands of researchers testing millions of combinations of variables, many "discoveries" are statistical noise that masqueraded as signal. The practice of p-hacking -- running analysis after analysis until something passes the significance threshold -- produces a steady stream of published "findings" that fail to replicate. The replication crisis in finance is severe: studies suggest that at least 50% of published anomalies in financial journals do not hold up out of sample.

- **Linear regression is the workhorse of factor analysis**: When someone says "value stocks outperform growth stocks," they are implicitly describing a regression result. When your fund manager claims to generate 3% alpha per year, that claim is based on a regression of fund returns against benchmark returns. If you cannot interpret a regression -- understand its coefficients, assess its significance, and evaluate its limitations -- you cannot critically evaluate these claims.

- **R-squared is the most misunderstood statistic in finance**: Investors routinely confuse R-squared (the percentage of variance explained by a model) with predictive power or quality of fit. An R-squared of 0.90 does not mean a model is good. An R-squared of 0.05 does not mean a model is useless. Understanding what R-squared does and does not tell you prevents costly misinterpretation.

- **Time series behavior determines which strategies can work**: Financial data is ordered in time, and its behavior over time -- whether it trends, reverts to a mean, or wanders randomly -- determines which strategies are viable. If a stock price follows a random walk, then mean-reversion strategies cannot work. If it trends, then momentum strategies have an edge. Understanding stationarity, autocorrelation, and mean reversion is fundamental to strategy selection.

- **Correlation is not causation, and everyone knows this, and nobody acts on it**: Every investor has heard that correlation does not imply causation. Yet every day, investment decisions are made on the basis of observed correlations treated as causal relationships. Understanding the difference -- and the specific mechanisms by which correlations mislead -- is essential to avoiding costly errors.

- **Statistical pitfalls can cost you your entire investment thesis**: Survivorship bias, look-ahead bias, multiple comparisons, data snooping, overfitting, small sample sizes -- each of these can make a worthless strategy look brilliant on paper. A single statistical mistake can cause you to deploy real capital on a strategy that never had a genuine edge.

This lesson will equip you with the statistical toolkit needed to separate genuine investment insights from statistical mirages.

---

### b) What You Need to Know

#### 1. Linear Regression for Factor Analysis

Linear regression is the foundation of nearly all empirical finance. At its core, regression asks: "How does one variable (the dependent variable) change when another variable (the independent variable) changes?"

```
LINEAR REGRESSION: THE BASICS

THE MODEL:
  Y = a + b * X + error

  Y = dependent variable (what you are trying to explain)
  X = independent variable (the explanatory factor)
  a = intercept (value of Y when X is zero)
  b = slope (how much Y changes for a one-unit change in X)
  error = what the model cannot explain (residual)

EXAMPLE: CAPM REGRESSION

  Fund Return = Alpha + Beta * Market Return + Error

  Y = Fund monthly return
  X = Market monthly return (e.g., S&P 500)
  a = Alpha (excess return not explained by market)
  b = Beta (sensitivity to the market)

  If regression yields:
    Alpha = 0.25% per month (3% annualized)
    Beta = 1.15

  Interpretation:
  - For every 1% the market moves, this fund moves 1.15%
  - The fund generates 0.25% per month ABOVE what
    its market exposure would predict
  - This alpha is the "skill" of the manager (if real)

VISUAL REPRESENTATION:

  Fund
  Return
  (%)
   8 |                               *
   6 |                         *  *
   4 |                   *  *
   2 |             *  * /
   0 |-------*--*-/--------------------
  -2 |     * /  *
  -4 |   * /
  -6 | * /
  -8 |/  *
     |________________________________
     -8  -6  -4  -2   0   2   4   6   8
              Market Return (%)

  The line is the regression line.
  The slope = beta = 1.15
  The intercept = alpha = 0.25%
  Points above the line = positive residuals
  Points below the line = negative residuals
```

```
MULTIPLE REGRESSION: FAMA-FRENCH FACTORS

Single regression uses ONE factor. Multiple regression
uses SEVERAL factors simultaneously:

  Return = Alpha + b1*Market + b2*Size + b3*Value + Error

FAMA-FRENCH THREE-FACTOR MODEL:

  Ri - Rf = ai + bi*(Rm-Rf) + si*SMB + hi*HML + ei

  Where:
  Ri - Rf  = Fund excess return (above risk-free rate)
  Rm - Rf  = Market excess return
  SMB      = Small Minus Big (small-cap premium)
  HML      = High Minus Low (value premium)
  ai       = Alpha (true skill after adjusting for factors)
  bi,si,hi = Factor loadings (sensitivities)

EXAMPLE OUTPUT:

  Factor       Coefficient   t-stat   p-value
  ──────────────────────────────────────────────
  Alpha        0.15%/mo      1.8      0.072
  Market       1.05          28.3     0.000
  SMB (Size)   0.35          4.2      0.000
  HML (Value)  0.22          2.9      0.004

  Interpretation:
  - Manager has beta of 1.05 (slightly above market)
  - Tilts toward small caps (SMB loading = 0.35)
  - Tilts toward value stocks (HML loading = 0.22)
  - Alpha of 0.15%/month is NOT statistically significant
    (p-value = 0.072 > 0.05 threshold)

  CONCLUSION: This manager's returns are EXPLAINED by
  exposure to market, size, and value factors. There
  is no statistically significant evidence of skill.
  The "alpha" from a single-factor model was actually
  compensation for taking size and value risk.

  ┌──────────────────────────────────────────────┐
  │  WHY THIS MATTERS:                           │
  │  Many "alpha-generating" managers are simply  │
  │  taking factor exposures that can be obtained │
  │  cheaply through index funds. You should not  │
  │  pay 1-2% fees for factor exposure you can    │
  │  get for 0.05-0.20%.                          │
  └──────────────────────────────────────────────┘
```

#### 2. R-Squared and Statistical Significance

R-squared and p-values are the two most commonly cited statistics in financial research. Both are routinely misunderstood.

```
R-SQUARED (COEFFICIENT OF DETERMINATION)

DEFINITION:
  R-squared = 1 - (Sum of Squared Residuals / Total Sum of Squares)

  In plain language:
  "What fraction of the variation in Y is explained by X?"

  R-squared = 0.00: X explains nothing about Y
  R-squared = 1.00: X explains everything about Y
  R-squared = 0.65: X explains 65% of Y's variation

EXAMPLE:

  Model: Fund Return = Alpha + Beta * Market Return

  R-squared = 0.85

  Meaning: 85% of this fund's return variation is
  explained by market movements. 15% comes from
  stock selection, sector bets, or randomness.

  ┌────────────────────────────────────────┐
  │  TOTAL VARIATION IN FUND RETURNS       │
  │                                        │
  │  ████████████████████████████████████  │
  │  ████████████████████░░░░░░░░░░░░░░░  │
  │  ▲                    ▲                │
  │  Explained by         Unexplained      │
  │  market (85%)         (15%)            │
  └────────────────────────────────────────┘

COMMON R-SQUARED VALUES IN FINANCE:

  Model                                 Typical R-sq
  ──────────────────────────────────────────────────
  S&P 500 index fund vs. S&P 500       0.999
  Large-cap active fund vs. S&P 500    0.85-0.95
  Hedge fund vs. S&P 500               0.30-0.70
  Individual stock vs. S&P 500         0.10-0.50
  Stock returns vs. GDP growth         0.03-0.08
  Monthly return predictions            0.01-0.05
  Daily return predictions              0.00-0.02

THE R-SQUARED TRAP:

  TRAP 1: "High R-squared = good model"
    A stock's regression on the market with R-sq = 0.92
    does NOT mean you can predict the stock's returns.
    It means the stock moves WITH the market.
    The 8% unexplained variance can still be huge.

  TRAP 2: "Low R-squared = useless model"
    A model predicting monthly returns with R-sq = 0.02
    seems pathetically weak. But 2% predictability in
    financial returns is ENORMOUSLY valuable.

    If you can predict 2% of return variance consistently,
    you can make billions of dollars in the markets.
    Renaissance Technologies allegedly operates with
    predictive R-squared values of 0.01-0.05.

  TRAP 3: "R-squared can only go up"
    Adding more variables to a model ALWAYS increases
    R-squared. This does NOT mean the model is better.
    Use adjusted R-squared, which penalizes for the
    number of variables:
    
    Adjusted R-sq = 1 - [(1-R-sq)(n-1)/(n-k-1)]
    
    Where n = observations, k = number of variables
```

```
STATISTICAL SIGNIFICANCE AND P-VALUES

THE P-VALUE:
  "If the true effect were ZERO, what is the probability
  of observing a result as extreme as what we found?"

  p-value = 0.05 means: There is a 5% chance of seeing
  this result if there were truly no effect.

  Convention:
  p < 0.05  -> "Statistically significant" (reject null)
  p >= 0.05 -> "Not significant" (fail to reject null)

THE T-STATISTIC:
  t-stat = coefficient / standard error

  Rule of thumb:
  |t-stat| > 2.0  -> approximately significant at 5% level
  |t-stat| > 2.6  -> approximately significant at 1% level
  |t-stat| > 3.3  -> approximately significant at 0.1% level

  Higher t-stat = more confident the coefficient is real

EXAMPLE: IS THIS FUND'S ALPHA REAL?

  Regression result: Alpha = 0.30% per month

  Scenario A: t-stat = 0.8, p-value = 0.42
    NOT significant. Alpha could easily be zero.
    We cannot distinguish 0.30% from noise.
    DO NOT pay high fees for this "alpha."

  Scenario B: t-stat = 2.5, p-value = 0.014
    Significant at 5% level. Fairly confident alpha
    is not zero. But could still be overstated.
    Consider the fund, but verify out of sample.

  Scenario C: t-stat = 4.2, p-value = 0.0001
    Highly significant. Very unlikely to be zero.
    Strong evidence of genuine skill.
    But still check: is the track record long enough?
    Are there hidden risks? Survivorship bias?

CRITICAL WARNING:
  ┌──────────────────────────────────────────────┐
  │  STATISTICAL SIGNIFICANCE != PRACTICAL       │
  │  SIGNIFICANCE                                │
  │                                              │
  │  With enough data, even a tiny, meaningless  │
  │  effect becomes "statistically significant." │
  │                                              │
  │  A fund with alpha = 0.01% per month         │
  │  (0.12%/year) with t-stat = 3.5 is           │
  │  statistically significant but practically   │
  │  meaningless. After fees, the alpha is gone.  │
  │                                              │
  │  Always ask: Is the effect LARGE ENOUGH       │
  │  to matter after fees and costs?              │
  └──────────────────────────────────────────────┘
```

#### 3. Time Series Basics: Stationarity and Autocorrelation

Financial data is ordered in time. This temporal structure has profound implications for analysis and strategy design.

```
STATIONARITY

DEFINITION:
  A time series is stationary if its statistical
  properties (mean, variance, autocorrelation) do not
  change over time.

STATIONARY SERIES:
  ┌──────────────────────────────────────────────┐
  │           *   *       *     *                 │
  │   *    *     * *   *    *      *    *         │
  │ ----*----------*---*------*-----*----- mean   │
  │    *  *     *    *     *    *      *          │
  │        *            *        *               │
  └──────────────────────────────────────────────┘
  Properties stay constant. Fluctuates around a
  fixed mean. Good for statistical analysis.

NON-STATIONARY SERIES (trending):
  ┌──────────────────────────────────────────────┐
  │                                         *    │
  │                                      *   *   │
  │                                *  *          │
  │                          *  *                │
  │                    *  *                      │
  │              *  *                            │
  │        *  *                                  │
  │  *  *                                        │
  └──────────────────────────────────────────────┘
  Mean changes over time. Standard regression
  produces SPURIOUS results on trending data.

NON-STATIONARY SERIES (random walk):
  ┌──────────────────────────────────────────────┐
  │        *                                     │
  │       * *                               *    │
  │      *   *                             * *   │
  │  *  *     *                *  *       *      │
  │ * *        *    *       * *    *    *         │
  │             *  * *   * *        * *          │
  │              *    * *                        │
  │                    *                         │
  └──────────────────────────────────────────────┘
  Wanders without returning to any mean.
  Stock prices are approximately random walks.
  Each step is independent of previous steps.

WHY STATIONARITY MATTERS:

  STOCK PRICES are non-stationary (random walk-ish).
  STOCK RETURNS are approximately stationary.

  WRONG: Regress stock PRICE on GDP level.
    Both trend upward over time.
    You will find a "significant" relationship
    that is entirely spurious.
    R-squared will be very high (0.90+) and
    completely meaningless.

  RIGHT: Regress stock RETURNS on GDP GROWTH.
    Both are (approximately) stationary.
    Any relationship found is more likely genuine.

  RULE: Always work with RETURNS (or changes),
  not LEVELS, when doing regression analysis
  on financial data.
```

```
AUTOCORRELATION

DEFINITION:
  Autocorrelation measures how much a time series
  is correlated with its own past values.

  Autocorrelation at lag k =
    Correlation between Y(t) and Y(t-k)

INTERPRETATION:

  Positive autocorrelation (momentum):
    If today's return is positive, tomorrow's return
    is more likely to be positive.
    
    + + + + - - - - + + + + - - - -
    (Runs of same sign)

  Negative autocorrelation (mean reversion):
    If today's return is positive, tomorrow's return
    is more likely to be negative.
    
    + - + - + - + - + - + - + - + -
    (Alternating signs)

  Zero autocorrelation (random walk):
    Today's return tells you nothing about tomorrow.
    
    + - - + + - + - - - + + - + - +
    (No pattern)

AUTOCORRELATION IN FINANCIAL MARKETS:

  Asset/Timeframe          Autocorrelation  Implication
  ──────────────────────────────────────────────────────
  Daily stock returns      ~0 to slightly   Approx random
                           negative         walk
  Monthly stock returns    Slightly         Weak short-term
                           positive         momentum
  1-year stock returns     Negative at      Long-term mean
                           3-5 year lags    reversion
  Daily bond returns       Slightly         Weak momentum
                           positive
  Currency returns         Mixed            Varies by pair
  Commodity returns        Positive at      Momentum in
                           medium term      trends

  KEY INSIGHT:
  - Short-term (days): Markets are nearly random
  - Medium-term (3-12 months): Weak momentum exists
  - Long-term (3-5 years): Mean reversion appears

  This pattern supports both momentum strategies
  (medium horizon) and value/mean-reversion strategies
  (long horizon), and neither contradicts efficient
  markets at short horizons.

LJUNG-BOX TEST:
  Tests whether a set of autocorrelations are jointly
  zero (i.e., whether ANY predictability exists).
  
  p-value < 0.05: Significant autocorrelation exists
  p-value > 0.05: No significant autocorrelation
  
  Most daily stock return series fail to reject the
  null of zero autocorrelation. They are approximately
  random walks at the daily frequency.
```

#### 4. Mean Reversion Testing

Mean reversion -- the tendency of a variable to return to its average over time -- is one of the most important concepts in finance and the basis for many investment strategies.

```
MEAN REVERSION

CONCEPT:
  If a variable tends to return to its long-term
  average, it exhibits mean reversion.

  ┌──────────────────────────────────────────────┐
  │                                              │
  │      *                          *            │
  │     * *                        * *           │
  │    *   *            *         *   *          │
  │ --*-----*----*-----*-*-------*-----*--- mean │
  │          *  * *   *   *     *       *        │
  │           *    * *     *   *         *       │
  │                 *       * *           *      │
  │                          *                   │
  └──────────────────────────────────────────────┘
  
  Mean reverting: Variable oscillates around a
  stable mean and tends to return when displaced.

WHAT MEAN REVERTS IN FINANCE:

  Strong evidence of mean reversion:
  - Valuation ratios (P/E, P/B, CAPE)
  - Interest rate spreads (credit, term)
  - Volatility (VIX, realized vol)
  - Currency relative to purchasing power parity
  - Profit margins (sector-level, economy-wide)

  Weak or no evidence of mean reversion:
  - Stock PRICES (approximately random walk)
  - GDP levels (trending upward)
  - Technological disruption effects

  ┌──────────────────────────────────────────────┐
  │  CRITICAL DISTINCTION:                       │
  │                                              │
  │  Stock PRICES do NOT mean revert.            │
  │  Stock VALUATIONS do mean revert.            │
  │                                              │
  │  A stock at $100 does NOT tend to return     │
  │  to $100 after falling to $50.               │
  │                                              │
  │  But a stock with P/E of 40 does tend to     │
  │  return toward a P/E of 15-20 over time      │
  │  (through price decline or earnings growth). │
  └──────────────────────────────────────────────┘

TESTING FOR MEAN REVERSION:

METHOD 1: AUGMENTED DICKEY-FULLER (ADF) TEST
  Tests whether a time series has a unit root
  (i.e., is a random walk).

  Null hypothesis: Series has a unit root (no mean reversion)
  Alternative: Series is stationary (mean reverting)

  If p-value < 0.05: Reject null -> evidence of mean reversion
  If p-value > 0.05: Fail to reject -> no evidence

  Typical results:
    Stock prices: p = 0.80 (NOT mean reverting)
    Stock returns: p = 0.001 (stationary)
    CAPE ratio: p = 0.04 (weakly mean reverting)
    VIX: p = 0.001 (strongly mean reverting)

METHOD 2: VARIANCE RATIO TEST
  If returns are random walk:
    Variance of k-period returns = k * Variance of 1-period returns

  If variance ratio < 1: Mean reversion (returns "cancel out")
  If variance ratio > 1: Momentum (returns "build up")
  If variance ratio = 1: Random walk

  Typical variance ratios for S&P 500:
    2-day vs. 1-day:   ~1.00 (random at short horizon)
    1-month vs. 1-week: ~0.98 (slight mean reversion)
    1-year vs. 1-month: ~0.95 (moderate mean reversion)
    5-year vs. 1-year:  ~0.80 (meaningful mean reversion)

METHOD 3: HALF-LIFE OF MEAN REVERSION
  How long does it take for a deviation from the
  mean to be reduced by half?

  Short half-life (days/weeks): Fast mean reversion,
    tradable with short-term strategies
  Long half-life (years): Slow mean reversion,
    relevant for long-term asset allocation
  Infinite half-life: No mean reversion (random walk)

  Typical half-lives:
    VIX:                ~2-4 weeks
    Interest rate spreads: ~3-6 months
    CAPE ratio:         ~3-7 years
    Currency PPP:       ~3-5 years
```

#### 5. Common Statistical Pitfalls

These are the errors that cause investors to deploy real capital on strategies that never had a genuine edge.

```
PITFALL 1: P-HACKING (DATA SNOOPING)

DEFINITION:
  Running many tests on the same data until one
  produces a "significant" result by chance.

EXAMPLE:
  You test 100 different "signals" for predicting
  stock returns. By chance alone, 5 will be
  "significant" at the 5% level (0.05 * 100 = 5).

  These 5 "significant" signals are false positives.
  They look real but are purely random.

  ┌──────────────────────────────────────────────┐
  │  WHAT THE RESEARCHER REPORTS:                │
  │                                              │
  │  "We found that the ratio of CEO surname     │
  │  length to company name length predicts      │
  │  stock returns with t-stat = 2.3 (p = 0.02)"│
  │                                              │
  │  WHAT ACTUALLY HAPPENED:                     │
  │                                              │
  │  They tested 200 variables. This was the     │
  │  one that happened to be "significant."      │
  │  The other 199 failures are never reported.  │
  │  This is the FILE DRAWER PROBLEM.            │
  └──────────────────────────────────────────────┘

HOW TO DETECT P-HACKING:
  - Does the paper test only ONE hypothesis?
    Suspicious if "we tested only this one thing"
  - Is there an economic rationale for the signal?
    If not, it is likely data-mined.
  - Does it replicate out of sample?
  - Apply Bonferroni correction or similar:
    Required p-value = 0.05 / number of tests
    100 tests -> need p < 0.0005 to be credible

PITFALL 2: MULTIPLE COMPARISONS

  Related to p-hacking but more subtle.

  EXAMPLE: Backtesting factor strategies
  
  You test these factors for US stocks 1990-2020:
  - Price/Earnings (4 variants)
  - Price/Book (3 variants)
  - Momentum (6 variants: different lookbacks)
  - Quality metrics (5 variants)
  - Low volatility (3 variants)
  - Size (2 variants)
  - Dividend yield (3 variants)
  - Technical signals (10 variants)
  ─────────────────────────────────
  Total: 36 independent tests

  At 5% significance: 36 * 0.05 = 1.8 expected
  false positives. Nearly 2 "significant" factors
  that are actually noise.

  BONFERRONI CORRECTION:
    Required p-value = 0.05 / 36 = 0.0014
    Required t-stat approximately 3.2

  HARVEY, LIU, AND ZHU (2016):
    In finance, the threshold for a new factor should be
    t-stat > 3.0, not the traditional 2.0, because of
    the massive number of factors already tested across
    all published research.

PITFALL 3: OVERFITTING

  Building a model so complex that it fits the noise
  in historical data, not the signal.

  IN-SAMPLE vs. OUT-OF-SAMPLE:
  
  ┌──────────────────────────────────────────────┐
  │  IN-SAMPLE (training data):                  │
  │                                              │
  │  Simple model:  * *  * *  * *                │
  │                /  \ / \ / \                  │
  │  Good fit but  not perfect. R-sq = 0.65      │
  │                                              │
  │  Complex model: ****************************  │
  │  Hits every point perfectly. R-sq = 0.99     │
  │                                              │
  │  OUT-OF-SAMPLE (new data):                   │
  │                                              │
  │  Simple model:  Still works. R-sq = 0.55     │
  │  Complex model: Falls apart. R-sq = 0.10    │
  │                                              │
  │  The complex model memorized the noise.      │
  │  The simple model captured the signal.       │
  └──────────────────────────────────────────────┘

  RULE OF THUMB (DEGREES OF FREEDOM):
    Minimum observations per parameter:
    10:1 is bare minimum
    20:1 is reasonable
    50:1 is good

    If you have 60 months of data and a model
    with 10 parameters, you have 6:1 ratio.
    This is almost certainly overfit.
```

```
PITFALL 4: SURVIVORSHIP BIAS

  Analyzing only the data that "survived" -- ignoring
  the data that was removed due to failure.

  MUTUAL FUND EXAMPLE:
    You study fund returns from 2000-2020.
    Your database has 3,000 funds.
    But 2,000 funds that existed in 2000 have since
    closed (most due to poor performance).
    
    Your analysis includes only the 3,000 survivors.
    Average return appears higher than reality because
    the failures are excluded.

    True average annual return: 7.5%
    Survivorship-biased average: 9.2%
    Bias: +1.7% per year

  STOCK INDEX EXAMPLE:
    "S&P 500 stocks returned 10% per year since 1990."
    But the current S&P 500 constituents are DIFFERENT
    from the 1990 constituents. Failed companies were
    removed. Winners were added. Using CURRENT members
    retroactively overstates historical returns.

  HEDGE FUND EXAMPLE:
    Hedge fund databases are self-reported and voluntary.
    Funds that perform badly stop reporting.
    This creates survivorship bias estimated at
    3-5% per year in hedge fund databases.

    ┌──────────────────────────────────────────┐
    │  "Hedge funds returned 12% per year"     │
    │                                          │
    │  After survivorship bias: ~8% per year   │
    │  After fees (2/20): ~5% per year         │
    │  After backfill bias: ~4% per year       │
    │  Risk-adjusted: Worse than index funds   │
    └──────────────────────────────────────────┘

PITFALL 5: SMALL SAMPLE SIZE

  Financial data has far fewer independent
  observations than people realize.

  "I backtested 30 years of data!"
  
  30 years of DAILY data = 7,500 observations.
  Sounds like a lot. But:
  
  - Daily returns are not independent
    (autocorrelation, clustering)
  - Different market regimes reduce effective
    sample size (maybe 4-6 truly independent
    market environments in 30 years)
  - Monthly data: 360 observations
  - Annual recessions: maybe 4-5 in sample
  - Crashes: 2-3 major events
  
  For strategies that depend on rare events
  (crashes, regime changes), 30 years gives you
  only 2-5 observations of the relevant event.
  
  Standard error scales with 1/sqrt(n).
  With only 5 crash observations, your estimate
  of crash behavior has a standard error of
  1/sqrt(5) = 45% of the true value.
  Essentially meaningless precision.
```

#### 6. Correlation vs. Causation

```
CORRELATION vs. CAUSATION

CORRELATION:
  Two variables tend to move together.
  Says nothing about WHY.

CAUSATION:
  One variable CAUSES changes in the other.
  Requires a mechanism, not just co-movement.

TYPES OF SPURIOUS CORRELATION:

1. COINCIDENCE (pure randomness)
   "The number of films Nicolas Cage appeared in
   correlates with swimming pool drownings."
   Correlation: r = 0.87
   Causation: None. Random coincidence.

2. CONFOUNDING VARIABLE (common cause)
   "Ice cream sales correlate with drowning deaths."
   
   Ice cream sales ←─── HEAT ───→ Drowning deaths
                    (confounding variable)
   
   Heat causes both. Ice cream does not cause drowning.
   
   FINANCIAL EXAMPLE:
   "Countries with more McDonald's have higher GDPs."
   
   McDonald's ←── DEVELOPMENT ──→ GDP
   
   Both are caused by economic development.
   Opening more McDonald's will not raise GDP.

3. REVERSE CAUSATION
   "Companies that advertise more have higher revenues."
   
   Maybe advertising causes revenue.
   Or maybe high revenue enables advertising spending.
   Or both.
   
   FINANCIAL EXAMPLE:
   "High P/E stocks have faster earnings growth."
   Maybe high P/E reflects EXPECTED future growth
   (the market anticipates growth and bids up price).
   The high P/E did not CAUSE the growth.

4. DATA MINING (ex-post pattern fitting)
   "Super Bowl winner (NFC vs. AFC) predicts
   stock market direction."
   
   This "worked" for decades by coincidence.
   It has no mechanism. It has since stopped working.

CORRELATION IN FINANCE - PRACTICAL CONCERNS:

  UNSTABLE CORRELATIONS:
  ┌──────────────────────────────────────────────┐
  │  Stock-Bond Correlation Over Time:           │
  │                                              │
  │  1960-2000: Positive (+0.2 to +0.5)         │
  │  2000-2020: Negative (-0.3 to -0.1)         │
  │  2022:      Positive again (+0.3)            │
  │                                              │
  │  If you built a portfolio assuming negative   │
  │  stock-bond correlation, 2022 was painful.   │
  │  Correlations CHANGE over time.              │
  └──────────────────────────────────────────────┘

  CRISIS CORRELATIONS:
  During market crises, correlations among risky
  assets spike toward 1.0. The diversification you
  thought you had disappears exactly when you need
  it most.

  Normal times:  Stock-Commodity corr = 0.15
  Crisis (2008): Stock-Commodity corr = 0.85

  This is the "correlation breakdown" problem.
  Diversification benefits are overstated by
  average correlation figures because averages
  include calm periods when you do not need
  diversification.
```

#### 7. Practical Tools

```
PRACTICAL QUANTITATIVE TOOLS FOR INVESTORS

TOOL 1: PYTHON + STATSMODELS
  Most common platform for financial analysis.
  
  Key functions:
  - OLS regression: sm.OLS(y, X).fit()
  - ADF test: adfuller(series)
  - Autocorrelation: acf(series, nlags=20)
  - Variance ratio: manual calculation

TOOL 2: EXCEL / GOOGLE SHEETS
  For simple regression and correlation:
  - LINEST() function for regression
  - CORREL() for correlation
  - RSQ() for R-squared
  - T.TEST() for significance testing
  
  Limitation: Cannot handle complex time series
  analysis, bootstrapping, or rolling regressions.

TOOL 3: KEY LIBRARIES FOR PYTHON

  import pandas as pd          # Data manipulation
  import numpy as np           # Numerical computing
  import statsmodels.api as sm # Regression, time series
  from scipy import stats      # Statistical tests
  import matplotlib.pyplot as plt  # Visualization

PRACTICAL CHECKLIST FOR EVALUATING CLAIMS:

  1. What is the sample period and size?
     [ ] At least 20 years of monthly data?
     [ ] Multiple market cycles included?

  2. Is the data clean?
     [ ] Survivorship bias addressed?
     [ ] Look-ahead bias eliminated?
     [ ] Total return (including dividends)?

  3. Is the analysis appropriate?
     [ ] Stationary variables used?
     [ ] Appropriate significance tests?
     [ ] Multiple comparisons adjusted for?

  4. Is it economically sensible?
     [ ] Does the effect have a logical mechanism?
     [ ] Is the magnitude plausible?
     [ ] Why would the effect persist?

  5. Does it replicate?
     [ ] Out-of-sample test performed?
     [ ] Different time periods?
     [ ] Different markets/geographies?
     [ ] Transaction costs deducted?

  If ANY of these fail, treat the claim with
  extreme skepticism.
```

---

### c) Common Misconceptions

**Misconception 1: "A high R-squared means the model is good and predictive."**

R-squared measures how much variation is explained by the model on the data it was fitted to. It says nothing about out-of-sample predictive power. A model with 50 parameters fitted to 60 data points can achieve R-squared of 0.99 while having zero predictive ability. Conversely, a model with R-squared of 0.02 that genuinely predicts 2% of return variance is extraordinarily valuable. In finance, R-squared should be used to understand how much of a fund's returns are attributable to factor exposures, not to assess whether a model will predict the future.

**Misconception 2: "If a correlation is statistically significant, the relationship is real and useful."**

Statistical significance tells you that an observed correlation is unlikely to have occurred by chance alone. It does not tell you that the correlation is stable over time, that it will persist in the future, or that it reflects a causal relationship you can exploit. A correlation between two variables computed over 50 years of data may be driven by a specific sub-period, may be caused by a third variable, or may have already been arbitraged away by other investors who noticed it earlier. Significant correlations in financial data are common; reliably profitable correlations are rare.

**Misconception 3: "More data always leads to better analysis."**

More data helps only if the data is relevant and the underlying process is stable. Using 100 years of stock market data to calibrate a model sounds rigorous, but if the market's structure has fundamentally changed -- as it did with the shift from physical trading floors to electronic markets, or the rise of passive investing -- old data may be more misleading than helpful. Using data from 1930 to predict behavior in 2025 assumes a stable data-generating process that almost certainly does not exist. The right amount of data is enough to cover multiple market cycles while remaining in a reasonably consistent structural regime.

**Misconception 4: "If a strategy worked in a backtest, it should work going forward."**

Backtests are subject to at least a dozen biases including survivorship bias, look-ahead bias, overfitting, data snooping, and transaction cost underestimation. The gap between backtested performance and live performance is consistently negative -- strategies perform worse live than in backtests. A responsible evaluation of a backtested strategy requires out-of-sample testing, realistic transaction costs, slippage estimates, and a credible economic rationale for why the edge exists and why it has not been arbitraged away.

**Misconception 5: "Correlation between two assets is a fixed number."**

Correlations are not constants -- they are summary statistics of a particular sample period that change dramatically over time. Stock-bond correlations have been positive for decades, negative for decades, and then positive again. Correlations among equity markets spike during crises, precisely when diversification is most needed. Any portfolio construction or risk management built on the assumption of stable correlations will eventually fail when correlations shift.

**Misconception 6: "I found a pattern that works, so I should trade on it."**

Finding a pattern in data is the easiest part of quantitative investing. The hard part is determining whether the pattern is real or spurious. Before trading on any pattern, you must answer: Does it have a logical economic mechanism? Does it survive out-of-sample testing? Does it survive after transaction costs? Would it survive if other investors discovered it? Has it been documented in academic literature (if so, it may have already been arbitraged)? If any answer is "no," the pattern is likely noise.

---

### d) Common Questions and Answers

**Q1: How many observations do I need for a reliable regression?**

A: The minimum depends on the number of parameters in your model. A conservative rule is 50 observations per parameter. For a single-factor regression, 50 monthly observations (about 4 years) is a bare minimum, and 120 (10 years) is much better. For a five-factor model, you want at least 250 monthly observations (20+ years). These minimums assume stationary data with reasonably stable relationships. For non-stationary data or unstable relationships, no sample size is sufficient -- you need to fix the data issues first. Remember that the effective sample size may be smaller than the number of observations due to autocorrelation and regime changes.

**Q2: What is the difference between the Sharpe ratio and statistical significance of alpha?**

A: The Sharpe ratio measures risk-adjusted return: excess return divided by standard deviation. It does not require a regression or a benchmark. Statistical significance of alpha, measured by the t-statistic from a regression, tests whether the fund's return above its benchmark exposure is distinguishable from zero. A fund can have a high Sharpe ratio but insignificant alpha if its returns are explained by factor exposures. Conversely, a fund with low Sharpe ratio could have significant alpha if it generates consistent returns uncorrelated with its benchmark. For evaluating manager skill, the t-statistic of alpha is more informative. For evaluating a standalone investment, the Sharpe ratio is more relevant.

**Q3: How do I test whether a series is mean reverting?**

A: Use the Augmented Dickey-Fuller (ADF) test. In Python: `from statsmodels.tsa.stattools import adfuller; result = adfuller(series)`. If the p-value is below 0.05, you have evidence of mean reversion. You can also calculate the half-life of mean reversion by fitting an AR(1) model: Y(t) - Y(t-1) = a + b*Y(t-1) + error. The half-life = -ln(2)/ln(1+b). If b is close to zero, mean reversion is slow; if b is close to -1, mean reversion is fast. Be cautious: mean reversion tests have low power with short samples, meaning they frequently fail to detect mean reversion that actually exists. Use 10+ years of data if possible.

**Q4: Why is time series regression different from cross-sectional regression?**

A: In cross-sectional regression, you compare different entities at one point in time (e.g., the returns of 500 stocks in January 2025). In time series regression, you follow one entity over many time periods (e.g., the returns of one fund over 120 months). Time series data has temporal dependencies -- today's observation is related to yesterday's -- which violates the independence assumption of standard regression. This means standard errors may be too small, making results look more significant than they are. Time series regression requires checks for autocorrelation (Durbin-Watson or Breusch-Godfrey test), heteroscedasticity (ARCH effects in financial data), and stationarity. Use Newey-West standard errors or HAC (heteroscedasticity and autocorrelation consistent) standard errors to correct for these issues.

**Q5: How can I tell if a factor (like value or momentum) is actually being compensated by the market?**

A: A factor is considered "compensated" if it has a persistent, positive risk premium with a plausible economic explanation. Test this by examining: (1) the average return of a long-short portfolio sorted on the factor over a long period (50+ years, multiple countries), (2) the t-statistic of this average return (should be above 3.0 given the multiple testing problem), (3) whether the factor survives after transaction costs, (4) whether it has an economic rationale (risk-based: investors are compensated for bearing a risk; behavioral: investors systematically make errors), and (5) whether it persists out of sample and in international markets. Value and momentum pass all five tests. Most other factors fail at least one.

**Q6: What is the practical relevance of quantitative methods for a buy-and-hold index investor?**

A: Even if you never run a regression, understanding quantitative methods protects you from being misled. When an advisor shows you a "proven" strategy, you can ask about out-of-sample testing, survivorship bias, and transaction costs. When a fund manager claims alpha, you can assess whether the t-statistic is meaningful. When financial media promotes a correlation (e.g., "the January effect," "sell in May"), you can evaluate whether it is statistically robust or data-mined noise. Quantitative literacy is defense against the constant stream of spurious claims in the financial industry. It is also essential for understanding factor investing and making informed decisions about factor tilts in your portfolio.

**Q7: How should I handle the fact that financial data has fat tails and is not normally distributed?**

A: Standard regression assumes normally distributed errors. Financial returns have fat tails (extreme events occur much more frequently than a normal distribution predicts) and sometimes skewness. This means standard significance tests can be unreliable. Practical remedies include: (1) using robust standard errors (HAC, bootstrapped), (2) checking results with non-parametric tests that do not assume normality, (3) being especially cautious about results that depend on extreme observations (remove them and see if results hold), and (4) recognizing that models calibrated to "average" market conditions will underestimate tail risk. For portfolio construction, consider using the t-distribution or historical simulation rather than assuming normal distributions.

---

---

## YouTube Script

**Week 45: Quantitative Methods for Investors**

[VISUAL: Title card -- "Numbers Game: Statistical Tools Every Investor Needs"]

**Alex**: Today we are going to talk about math. Not the kind you hated in school -- the kind that keeps you from being fooled out of your money. Quantitative methods are the investor's toolkit for separating real patterns from random noise. And in financial markets, most "patterns" are noise.

**Sam**: I have seen plenty of charts that seem to show patterns. Stock X goes up every January. Indicator Y predicts recessions. How do I know which ones are real?

**Alex**: That is exactly the right question, and the answer involves understanding a few core statistical concepts: regression, R-squared, significance testing, time series behavior, and the many ways data can lie to you. Let us start with the most important tool in empirical finance: linear regression.

[VISUAL: "Linear Regression" section header]

**Alex**: Regression answers a simple question: how does one variable change when another variable changes? In finance, the most common application is the CAPM regression. You take a fund's monthly returns and regress them against the market's monthly returns.

[ANIMATION: animation/week45_regression.py -- Animated scatter plot of fund returns (Y-axis) versus market returns (X-axis). Points appear one by one as monthly observations. A regression line is fitted dynamically as each point appears, showing how the line shifts and stabilizes as more data accumulates. The slope of the line is labeled as "Beta" and updates in real time. The Y-intercept is labeled as "Alpha" and also updates. After all 60 months of data are plotted, the final regression line is drawn in bold with the equation displayed. Residuals are shown as vertical dashed lines from each point to the regression line. A second phase shows the addition of a second factor (SMB, the size factor), transitioning the 2D scatter to a 3D view where the regression plane is visible, demonstrating how alpha shrinks when additional factors are included. The animation concludes by showing R-squared as a percentage bar that fills up proportional to explained variance.]

**Sam**: So the slope of that line is beta -- how sensitive the fund is to the market -- and the intercept is alpha -- the return the fund generates above what you would expect from its market exposure.

**Alex**: Exactly. And this is where it gets interesting. Suppose a fund manager tells you they have generated 3% alpha per year over the past 5 years. Sounds great. You run the CAPM regression and confirm: alpha is 0.25% per month, or 3% annualized, with a beta of 1.05.

**Sam**: So the manager has skill?

**Alex**: Maybe. But then you run a multi-factor regression -- the Fama-French three-factor model. You add the size factor (small stocks minus big stocks) and the value factor (cheap stocks minus expensive stocks). Suddenly, the alpha drops to 0.08% per month and is no longer statistically significant.

**Sam**: What happened?

**Alex**: The manager's "alpha" was actually just exposure to the size and value factors. They were buying small-cap value stocks, which have historically outperformed. The "skill" was really just a factor tilt that you can replicate with cheap index funds charging 0.05% instead of the manager's 1.5% fee.

[VISUAL: Side-by-side comparison -- CAPM alpha vs. three-factor alpha for a hypothetical fund]

**Sam**: That is a powerful tool. But how do I know if the regression results are reliable?

[VISUAL: "R-Squared and Significance" section header]

**Alex**: Two key statistics: R-squared and the p-value. R-squared tells you what fraction of the fund's return variation is explained by the factors. A typical large-cap equity fund has an R-squared of 0.85 to 0.95 against the market -- meaning 85-95% of its movement is driven by market movements.

**Sam**: So a high R-squared means the model is a good fit?

**Alex**: This is one of the most common traps. High R-squared means the model explains a lot of the variation in the PAST data. It does NOT mean the model will predict the future. And low R-squared does NOT mean the model is useless.

**Sam**: How can low R-squared be useful?

**Alex**: In financial return prediction, an R-squared of 0.02 -- two percent -- sounds pathetic. But if you can genuinely predict 2% of the variance in stock returns, you can generate enormous profits. Renaissance Technologies, the most successful hedge fund in history, is rumored to operate with predictive R-squared values in the 1-5% range. They make billions.

**Sam**: So 2% predictability in market returns is actually a lot?

**Alex**: In a competitive market where millions of participants are trying to find edges, predicting even 1% of variance consistently puts you in an elite category. The mistake people make is comparing financial R-squared values to R-squared values from, say, physics experiments, where R-squared of 0.99 is common. Finance is a social science with much more noise.

[VISUAL: Scale showing R-squared values -- physics (0.99), engineering (0.90), social science (0.30), finance predictions (0.02)]

**Alex**: Now, the p-value and t-statistic tell you something different. They tell you whether the coefficient -- say, the alpha -- is statistically distinguishable from zero.

**Sam**: Meaning: is the alpha real, or could it be random noise?

**Alex**: Right. The t-statistic is the coefficient divided by its standard error. A t-stat above 2 is roughly "significant at the 5% level" -- meaning there is less than a 5% chance you would see a result this extreme if the true alpha were zero.

**Sam**: So a t-stat of 2.5 on a fund's alpha means I should believe the alpha is real?

**Alex**: It means the evidence is reasonably strong, but you need context. How many months of data? Was the period unusual? Did you test many funds and report only the one with the best result? And critically: is the alpha large enough to matter after fees?

**Sam**: What do you mean?

**Alex**: Suppose a fund has alpha of 0.01% per month -- that is 0.12% per year -- with a t-statistic of 3.0. Statistically significant! But 0.12% per year is utterly irrelevant to your wealth. After fees and transaction costs, it is gone. Statistical significance is not the same as practical significance.

[VISUAL: Table comparing statistically significant alphas that are practically meaningless vs. practically meaningful]

**Sam**: That is an important distinction. So what about time series? You mentioned stationarity.

[VISUAL: "Time Series Basics" section header]

**Alex**: This is crucial and overlooked. Financial data is ordered in time, and the behavior of data over time determines what kind of analysis is valid and what kind of strategies can work.

**Alex**: The most important concept is stationarity. A stationary time series has statistical properties -- mean, variance -- that do not change over time. Stock RETURNS are approximately stationary: the average monthly return of the S&P 500 is roughly the same in any decade (around 0.7-0.9% per month). But stock PRICES are not stationary -- they trend upward over time.

**Sam**: Why does that distinction matter?

**Alex**: Because running a regression on non-stationary data produces nonsense. This is one of the most common errors in amateur financial analysis. If you regress the S&P 500 price level on US GDP level, you will find an R-squared of 0.95 and a hugely significant coefficient.

**Sam**: That sounds like a strong result.

**Alex**: It is completely spurious. Both series trend upward over time. You would find the same "significant" relationship between the S&P 500 and the number of iPhones sold, or world population, or the cumulative number of Marvel movies released. Any two trending series will show a spurious correlation.

**Sam**: So how do you avoid this?

**Alex**: Work with returns or changes instead of levels. Regress stock RETURNS on GDP GROWTH, not stock prices on GDP levels. Returns and growth rates are (approximately) stationary, so any relationship you find is much more likely to be genuine.

[VISUAL: Side-by-side regression -- S&P 500 price vs. GDP (spurious, R-sq = 0.95) next to S&P 500 returns vs. GDP growth (genuine, R-sq = 0.04)]

**Alex**: The second important time series concept is autocorrelation -- how much a series is correlated with its own past values. If today's stock return is positive, is tomorrow's more likely to be positive (momentum), negative (mean reversion), or unrelated (random walk)?

**Sam**: And the answer is...?

**Alex**: At the daily level, stock returns are approximately random -- no significant autocorrelation. At the monthly to annual level, there is weak positive autocorrelation -- a hint of momentum. At the multi-year level, there is negative autocorrelation -- evidence of mean reversion. This pattern actually supports both momentum strategies at medium horizons and value strategies at long horizons.

**Sam**: You mentioned mean reversion. How do you test for it?

[VISUAL: "Mean Reversion" section header]

**Alex**: Mean reversion means a variable tends to return to its long-term average after being displaced. This is enormously important because if something mean-reverts, you can build a strategy around buying when it is below average and selling when it is above.

**Sam**: Like buying stocks when the P/E ratio is low and selling when it is high?

**Alex**: Exactly -- because the P/E ratio IS mean reverting. The CAPE ratio (cyclically adjusted P/E) for the US market has fluctuated between about 5 and 45 over the past century, but it always returns toward its long-term average of about 17. The key question is how fast it reverts. The half-life of mean reversion for the CAPE ratio is about 3-7 years, meaning it takes several years for a deviation to be halfway corrected. That is too slow for a trading strategy but valuable for long-term asset allocation.

**Sam**: What about stock prices themselves?

**Alex**: Stock prices do NOT mean revert. This is a critical distinction. A stock at $100 that drops to $50 does not tend to return to $100. It could go to $25 or $200 or anywhere. The price is approximately a random walk. But the VALUATION -- the P/E ratio, the price-to-book ratio -- does mean revert. The distinction between prices and valuations is essential.

[VISUAL: Two charts side by side -- stock price (random walk, no mean reversion) and P/E ratio (oscillating around a mean)]

**Alex**: The standard test for mean reversion is the Augmented Dickey-Fuller test, which checks whether a series has a "unit root" -- essentially, whether it is a random walk. If the test rejects the unit root, the series is likely stationary and mean-reverting.

**Sam**: This brings us to the pitfalls. You said most claimed patterns are false.

[VISUAL: "Statistical Pitfalls" section header]

**Alex**: Let me describe the biggest one first: p-hacking, also called data snooping. Imagine you are a researcher. You have a dataset of stock returns and 200 potential explanatory variables -- everything from earnings ratios to weather patterns to CEO demographics.

**Sam**: Two hundred variables is a lot.

**Alex**: And that is the point. At the 5% significance level, you expect 10 of those 200 variables to show a "significant" relationship with returns purely by chance. Five percent times 200 equals 10 false positives.

**Sam**: So you just test 200 things, find 10 that "work," publish the best one, and you look like a genius.

**Alex**: And nobody ever sees the 190 failures. This is called the file drawer problem -- the failed tests go into the file drawer and never get published. The researcher writes a paper titled "The Predictive Power of CEO Surname Length on Stock Returns" with a t-statistic of 2.3 and gets it published. It is complete nonsense, but it looks rigorous.

[VISUAL: Diagram showing 200 tests with 10 false positives highlighted, then one being selected for publication]

**Alex**: Harvey, Liu, and Zhu published an influential paper in 2016 arguing that the traditional significance threshold of t-stat > 2.0 is far too low for financial research. Given the sheer number of factors that have been tested across all published studies, they recommend t-stat > 3.0 as the minimum for a new factor to be credible.

**Sam**: So a lot of published research is probably wrong?

**Alex**: A substantial fraction, yes. And the problem is worse than just published research. Every quantitative investor, every hedge fund quant, every retail trader running backtests -- they are all searching through the same data. The cumulative amount of data snooping across the entire industry is staggering.

**Sam**: How do you protect against this?

**Alex**: Five defenses. First, require an economic rationale -- the pattern must make logical sense, not just statistical sense. Second, demand out-of-sample testing -- does it work on data the model has never seen? Third, check international markets -- does the US pattern appear in Japan, Europe, emerging markets? Fourth, apply Bonferroni correction -- if you tested 100 variables, your significance threshold should be 0.05/100 = 0.0005, not 0.05. Fifth, be suspicious of any result that seems too clean or too good.

[VISUAL: "Five Defenses Against Data Snooping" bullet list]

**Sam**: What about overfitting? How is that different from p-hacking?

**Alex**: P-hacking is about testing too many hypotheses. Overfitting is about making your model too complex for the data you have. Imagine fitting a model to 60 months of stock returns. A simple model with one factor captures the broad trend. A complex model with 20 parameters can fit every wiggle in the data perfectly.

**Sam**: And the complex model would look much better on historical data.

**Alex**: In sample, yes. It has R-squared of 0.99. But on NEW data, it falls apart. R-squared drops to 0.05. The complex model memorized the noise in the historical data. The simple model, with its modest R-squared of 0.30, actually performs better out of sample because it captured the signal, not the noise.

**Sam**: Is there a rule of thumb for how complex a model can be?

**Alex**: A rough guideline is at least 20 observations per parameter, preferably 50. With 60 months of data, your model should have at most 3 parameters (60/20). A model with 10 parameters on 60 observations is almost certainly overfit.

[VISUAL: In-sample vs. out-of-sample performance -- simple model stable, complex model collapses]

**Alex**: Another critical pitfall is survivorship bias. This is subtle and devastating.

**Sam**: I know the concept -- you only look at the survivors, not the failures.

**Alex**: Right. But in finance, the magnitude of the bias is larger than most people realize. Take mutual funds. You want to study the average return of equity mutual funds from 2000 to 2020. You pull data on 3,000 currently existing funds. But 2,000 funds that existed in 2000 have since been closed or merged -- mostly because they performed badly. Your sample contains only the winners.

**Sam**: So the average return looks better than it really was.

**Alex**: Survivorship bias in mutual fund databases is estimated at 1-2% per year. In hedge fund databases, it is 3-5% per year because hedge funds voluntarily report and stop reporting when they do badly. After adjusting for survivorship bias and backfill bias (funds report historical performance only after they have a good track record), the average hedge fund's return drops from the claimed 10-12% to something like 4-6%.

**Sam**: What about stock-level survivorship bias?

**Alex**: Same issue. If you analyze the historical returns of current S&P 500 members going back to 1990, you are including Apple, Amazon, and Google (which were added after they became huge winners) and excluding Enron, WorldCom, and Lehman Brothers (which were removed when they went bankrupt). This inflates historical returns significantly.

[VISUAL: Histogram showing hedge fund returns before and after survivorship bias correction]

**Sam**: Let me ask about correlation. Everyone says "correlation does not equal causation." But what does that actually mean in practice?

[VISUAL: "Correlation vs. Causation" section header]

**Alex**: Let me give you a real example. In the 2000s, many quantitative models used the correlation between housing prices and mortgage default rates. Housing prices always went up nationally, so defaults were always low, so the models said mortgage-backed securities were safe.

**Sam**: And then housing prices fell nationally for the first time in decades.

**Alex**: The correlation was real -- historically, rising housing prices were indeed associated with low defaults. But the models confused correlation with causation. The CAUSE of low defaults was not rising prices per se, but the economic conditions that produced rising prices. When those conditions changed, the correlation flipped, and trillions of dollars in "safe" assets became toxic.

**Sam**: So the correlation was only valid in one economic regime.

**Alex**: Exactly. And this illustrates a fundamental problem: correlations in financial markets are not stable. Stock-bond correlations have been positive, then negative, then positive again over the past 60 years. Building a portfolio that assumes stable correlations is building on quicksand.

[VISUAL: Chart of rolling stock-bond correlation 1960-2025, showing regime changes]

**Alex**: Perhaps the most dangerous aspect of correlations is that they spike during crises. During normal times, asset classes have moderate correlations. During a crisis, everything falls together. The diversification you thought you had evaporates precisely when you need it most.

**Sam**: So diversification is less reliable than it looks?

**Alex**: On average, it works. During crises, it works less well. This is called the "correlation asymmetry" problem -- correlations are higher on the downside than on the upside. Risk models that use average correlations systematically underestimate tail risk.

**Sam**: Let us talk about practical tools. If I want to actually do some of this analysis, what do I need?

[VISUAL: "Practical Tools" section header]

**Alex**: Python is the standard tool. With the libraries pandas, numpy, and statsmodels, you can do everything we have discussed. Running a regression is one line of code: `sm.OLS(y, X).fit()`. Testing for stationarity: `adfuller(series)`. Computing autocorrelation: `acf(series, nlags=20)`.

**Sam**: And for people who do not code?

**Alex**: Excel can handle basic regression (use the LINEST function or the Analysis Toolpak). Google Sheets has built-in functions for correlation (CORREL) and R-squared (RSQ). These are sufficient for single-factor regressions and basic correlation analysis. For anything more complex -- multi-factor models, time series tests, rolling regressions -- you really need Python or R.

**Sam**: What is the one thing I should take away from this lesson?

**Alex**: Skepticism. Informed, quantitative skepticism. Whenever someone presents a financial pattern, strategy, or claim backed by data, ask five questions. What is the sample size? Was it tested out of sample? Is there survivorship bias? How many other hypotheses were tested? And does it make economic sense? If any answer is unsatisfactory, the claim is probably noise dressed up as signal.

**Sam**: And noise dressed up as signal can cost you real money.

**Alex**: It costs investors billions every year. Fees paid to managers whose "alpha" is just factor exposure. Money lost on strategies that were overfit to historical data. Capital deployed on correlations that reversed in the next market regime. Quantitative literacy is your defense. You do not need to become a quant -- you just need to know enough to ask the right questions.

[VISUAL: Summary card -- "Key Takeaways: R-squared is not predictive power, t-stat > 3.0 for new factors, work with returns not prices, demand out-of-sample evidence, correlation is not causation and is not stable"]

**Sam**: Thanks, Alex. Next week, we will take these concepts further and look at how to properly test investment strategies through backtesting.

**Alex**: That is right. Week 46 will cover backtesting frameworks, the many biases that make backtests unreliable, and how to tell when a backtest result is genuine versus an artifact. It is one of the most practically important lessons in this entire series.

[VISUAL: End card -- "Next Week: Backtesting and Strategy Validation"]
