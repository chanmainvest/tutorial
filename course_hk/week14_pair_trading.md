<!-- 此檔案需要翻譯為香港繁體中文 -->
<!-- This file needs translation to HK Traditional Chinese -->

# Week 14: Pair Trading Fundamentals

## Reading Section

### a) Why This Is Important

In Week 13, we learned about long and short trading. We saw how hedge funds combine long and short positions to reduce market risk while profiting from stock selection. Pair trading takes this concept and refines it into one of the most elegant, systematic strategies in quantitative finance.

Pair trading matters for several important reasons:

**Market Direction Independence:** The single biggest risk for any investor is a broad market crash. If you hold a portfolio of stocks and the S&P 500 drops 30%, almost everything goes down regardless of quality. Pair trading largely eliminates this risk. Because you are simultaneously long one stock and short a related stock, market-wide movements wash out. When the market crashes, both stocks in your pair drop, and your net position is largely unaffected. Your profit or loss comes from the relative movement between the two stocks, not from the market's direction.

**Quantitative Foundation:** Pair trading is one of the earliest and most well-documented quantitative strategies. It was pioneered at Morgan Stanley in the mid-1980s by Nunzio Tartaglia's quantitative research group. Since then, it has been studied extensively in academic finance. The statistical tools used in pair trading, including correlation, cointegration, mean reversion, and z-scores, form the foundation of many more advanced quantitative strategies. Learning pair trading gives you a practical entry point into the world of systematic investing.

**Risk-Adjusted Returns:** Because pair trading hedges away market risk, the returns tend to be more consistent and less volatile than directional strategies. While you may not capture the huge gains of a bull market, you also avoid the devastating drawdowns of a bear market. For investors who care about risk-adjusted returns (and every serious investor should), pair trading offers an attractive profile.

**Transferable Skills:** The analytical techniques you learn in pair trading transfer to many other areas of finance. Correlation analysis helps you understand portfolio diversification. Cointegration is used in fixed income relative value trading, currency pair trading, and commodity spread trading. Mean reversion concepts appear throughout quantitative finance, from statistical arbitrage to options pricing. Mastering pair trading gives you a toolkit that extends far beyond this single strategy.

**Professional Relevance:** Pair trading and its more sophisticated cousin, statistical arbitrage, are among the most common strategies used by quantitative hedge funds and proprietary trading firms. If you are considering a career in quantitative finance, understanding pair trading is foundational. Even in fundamental investing, the concept of relative value, asking whether Stock A is cheap relative to Stock B rather than cheap in absolute terms, is a core analytical skill.

In this lesson, we will cover the conceptual framework of relative value, how to identify suitable pairs, the statistical tools used to evaluate pairs, the mechanics of executing pair trades, and the risks and limitations of the strategy.

---

### b) What You Need to Know

#### The Concept of Relative Value

Most investors think in absolute terms. "Is Apple cheap?" "Is the market overvalued?" These are absolute value questions. Pair trading is built on relative value thinking: "Is Apple cheap RELATIVE TO Microsoft?"

```
ABSOLUTE vs. RELATIVE VALUE:

  ABSOLUTE VALUE (traditional investing):
  +----------------------------------------------------------+
  | Question: "Is AAPL undervalued?"                          |
  | Method:   Analyze AAPL's fundamentals, DCF, comps        |
  | Risk:     Market crash drags AAPL down regardless         |
  | Result:   You can be RIGHT about AAPL but still LOSE     |
  |           money if the whole market falls                  |
  +----------------------------------------------------------+

  RELATIVE VALUE (pair trading):
  +----------------------------------------------------------+
  | Question: "Is AAPL cheap relative to MSFT?"               |
  | Method:   Compare their price ratio or spread over time   |
  | Risk:     Relationship between the two stocks breaks down |
  | Result:   Market crash affects BOTH stocks, so the        |
  |           relative position is largely unaffected          |
  +----------------------------------------------------------+

  VISUAL EXAMPLE:

  Market crashes 20%:
  
  Absolute Value Investor:
  Long AAPL only:  AAPL drops 18%  ->  Loss: -18%
  
  Pair Trader:
  Long AAPL:       AAPL drops 18%  ->  Loss: -18%
  Short MSFT:      MSFT drops 22%  ->  Gain: +22%
                                       Net:  + 4%
  
  The pair trader PROFITED in a crash because AAPL
  fell less than MSFT, confirming the relative value thesis.
```

#### What Makes a Good Pair?

Not every two stocks make a good pair. The ideal pair has specific characteristics that make the strategy reliable:

```
CRITERIA FOR A GOOD PAIR:

  1. SAME SECTOR / INDUSTRY
  +----------------------------------------------------------+
  | Stocks in the same industry are affected by the same      |
  | forces: regulations, commodity prices, consumer trends.   |
  | This ensures they move together in general, making the    |
  | strategy sector-neutral.                                  |
  |                                                           |
  | Good:  Coca-Cola (KO) and PepsiCo (PEP)                 |
  | Good:  Exxon (XOM) and Chevron (CVX)                     |
  | Bad:   Apple (AAPL) and ExxonMobil (XOM)                 |
  +----------------------------------------------------------+

  2. HIGH HISTORICAL CORRELATION
  +----------------------------------------------------------+
  | The two stocks should have moved together historically.   |
  | Correlation measures the degree to which two stocks       |
  | move in the same direction.                               |
  |                                                           |
  | Correlation ranges from -1.0 to +1.0:                    |
  |   +1.0 = perfect positive (move in lockstep)             |
  |   +0.0 = no relationship                                 |
  |   -1.0 = perfect negative (move opposite)                |
  |                                                           |
  | For pair trading, look for correlation > 0.80             |
  +----------------------------------------------------------+

  3. SIMILAR BUSINESS MODEL AND SIZE
  +----------------------------------------------------------+
  | Companies should be comparable in terms of:               |
  | - Market capitalization (both large-cap, or both mid-cap) |
  | - Revenue model (both subscription, both advertising)     |
  | - Geographic exposure (both domestic, both global)        |
  | - Growth profile (both mature, or both high-growth)       |
  +----------------------------------------------------------+

  4. MEAN-REVERTING SPREAD
  +----------------------------------------------------------+
  | The price ratio or spread between the two stocks should   |
  | tend to revert to a historical average. When it deviates, |
  | it should come back. This is testable statistically.      |
  +----------------------------------------------------------+

  5. COINTEGRATION (the gold standard)
  +----------------------------------------------------------+
  | Cointegration is a statistical property that means two    |
  | series share a long-run equilibrium relationship.         |
  | Even if each stock wanders randomly on its own, the       |
  | DIFFERENCE between them is stationary (mean-reverting).   |
  | This is stronger than correlation and more reliable.      |
  +----------------------------------------------------------+
```

#### Classic Pair Examples

```
WELL-KNOWN TRADING PAIRS:

  BEVERAGES:
  +-------------------+-------------------+
  | Coca-Cola (KO)    | PepsiCo (PEP)     |
  | Both global       | Both global        |
  | beverage leaders   | beverage leaders  |
  | Similar margins   | Similar margins    |
  | Correlation: ~0.85| over 20+ years    |
  +-------------------+-------------------+

  ENERGY:
  +-------------------+-------------------+
  | ExxonMobil (XOM)  | Chevron (CVX)     |
  | #1 US oil major   | #2 US oil major   |
  | Similar exposure   | Similar exposure  |
  | to oil prices     | to oil prices      |
  | Correlation: ~0.90|                    |
  +-------------------+-------------------+

  TECHNOLOGY:
  +-------------------+-------------------+
  | Visa (V)          | Mastercard (MA)   |
  | Payment network   | Payment network    |
  | Duopoly           | Duopoly            |
  | Similar growth    | Similar growth     |
  | Correlation: ~0.92|                    |
  +-------------------+-------------------+

  FINANCIALS:
  +-------------------+-------------------+
  | Goldman Sachs (GS)| Morgan Stanley(MS)|
  | Investment bank   | Investment bank    |
  | Similar business  | Similar business   |
  | mix               | mix                |
  | Correlation: ~0.88|                    |
  +-------------------+-------------------+

  HOME IMPROVEMENT:
  +-------------------+-------------------+
  | Home Depot (HD)   | Lowe's (LOW)      |
  | #1 home improve.  | #2 home improve.  |
  | Same customers    | Same customers     |
  | Same drivers      | Same drivers       |
  | Correlation: ~0.87|                    |
  +-------------------+-------------------+
```

#### Correlation vs. Cointegration

This distinction is crucial and often misunderstood. Many beginners equate correlation with suitability for pair trading. This is a mistake.

```
CORRELATION vs. COINTEGRATION:

  CORRELATION:
  Measures whether two stocks move in the SAME DIRECTION.
  Two stocks can be highly correlated but NOT mean-reverting.
  
  Example of HIGH CORRELATION but NO COINTEGRATION:
  
  Price
  $200 |          Stock A  /
       |                 /  /  Stock B
  $150 |              /  /
       |           /  /
  $100 |        /  /
       |     /  /
  $ 50 |  /  /
       |/  /
       +--|------|------|------|----->  Time
       Year 1   Year 2  Year 3  Year 4
  
  Both go up together (correlated = 0.95).
  But the GAP between them keeps GROWING.
  The spread does NOT revert to a mean.
  BAD for pair trading.


  COINTEGRATION:
  Measures whether the SPREAD between two stocks is stable.
  The spread may deviate temporarily, but it always comes back.
  
  Example of COINTEGRATED pair:
  
  Price
  $160 |    A         A    A          A
       |   / \  B    / \  / \   B    / \
  $140 |  /   \/\  /    \/   \ / \  /   \
       | / B    \/B         B\/   \/     B
  $120 |/                                 \
       +--|------|------|------|------|----->  Time
       Year 1   Year 2  Year 3  Year 4 Year 5
  
  Stocks A and B weave around each other.
  Sometimes A is ahead, sometimes B is ahead.
  But the spread between them is STABLE.
  When they diverge, they converge back.
  GOOD for pair trading.


  KEY INSIGHT:
  +----------------------------------------------------------+
  | Correlation tells you if two stocks move in the same      |
  | direction. Cointegration tells you if the DISTANCE        |
  | between them is stable. For pair trading, cointegration   |
  | is what matters.                                          |
  |                                                           |
  | Analogy: Two dogs on leashes held by one owner.           |
  | The dogs may wander left and right (not perfectly         |
  | correlated in their moment-to-moment steps), but the      |
  | leash keeps them from getting too far apart. The leash    |
  | is cointegration.                                         |
  +----------------------------------------------------------+
```

#### Testing for Cointegration

The standard test for cointegration in pair trading is the Augmented Dickey-Fuller (ADF) test, also known as the Engle-Granger two-step method:

```
TESTING FOR COINTEGRATION - Two-Step Process:

  STEP 1: Calculate the spread (or ratio)
  +----------------------------------------------------------+
  | Spread = Price_A - (beta x Price_B) - alpha               |
  |                                                           |
  | Where beta is the hedge ratio from linear regression:     |
  | Price_A = alpha + beta x Price_B + residuals              |
  |                                                           |
  | The residuals ARE the spread.                             |
  +----------------------------------------------------------+

  STEP 2: Test if the spread is stationary (ADF test)
  +----------------------------------------------------------+
  | Apply the Augmented Dickey-Fuller test to the residuals.  |
  | If p-value < 0.05, the spread is stationary              |
  | (mean-reverting), and the pair is cointegrated.           |
  |                                                           |
  | H0 (null): Spread has a unit root (not stationary)        |
  | H1 (alternative): Spread is stationary (mean-reverting)   |
  |                                                           |
  | If we reject H0 (p < 0.05), the pair is cointegrated.    |
  +----------------------------------------------------------+

  PRACTICAL INTERPRETATION:

  ADF Test Result          Pair Trading Suitability
  ==================       ========================
  p-value < 0.01           Strong cointegration. Excellent pair.
  p-value 0.01 - 0.05      Moderate cointegration. Good pair.
  p-value 0.05 - 0.10      Weak cointegration. Use with caution.
  p-value > 0.10           Not cointegrated. Avoid this pair.

  EXAMPLE:
  
  Run regression:  KO_price = 0.52 + 1.12 x PEP_price + residuals
  
  ADF test on residuals:
  Test statistic: -3.42
  p-value: 0.009
  
  Conclusion: p-value < 0.01, so KO and PEP are cointegrated.
  The spread between them is mean-reverting.
  This is a valid pair for trading.
```

#### The Price Ratio and Spread

There are two main ways to measure the relationship between a pair of stocks:

```
TWO APPROACHES TO PAIR MEASUREMENT:

  1. PRICE RATIO METHOD
  +----------------------------------------------------------+
  | Ratio = Price_A / Price_B                                 |
  |                                                           |
  | Example: KO at $60, PEP at $170                          |
  | Ratio = 60 / 170 = 0.353                                 |
  |                                                           |
  | If historical average ratio is 0.370, KO is relatively   |
  | cheap vs. PEP (ratio below average).                     |
  | Trade: Buy KO, Short PEP.                                |
  +----------------------------------------------------------+

  Price Ratio Chart (KO/PEP):
  
  0.42 |
       |      *
  0.40 |     * *
       |    *   *
  0.38 |   *     *            *
       |  *       *          * *
  0.36 |--*--------*--mean--*---*----------  <- Historical Mean
       |            *      *     *
  0.34 |             *    *       *    *
       |              *  *         *  * *
  0.32 |               **          **   *  <- Current (below mean)
       |                                    
  0.30 +--|----|----|----|----|----|----|-->
          J    F    M    A    M    J    J
  
  Signal: Ratio below mean -> Buy KO, Short PEP


  2. SPREAD METHOD (using hedge ratio)
  +----------------------------------------------------------+
  | Spread = Price_A - (hedge_ratio x Price_B)                |
  |                                                           |
  | Hedge ratio from regression: beta = 0.35                  |
  | Spread = KO - (0.35 x PEP) = 60 - (0.35 x 170) = 0.50  |
  |                                                           |
  | If mean spread is 2.00, current spread of 0.50 is below  |
  | average. KO is cheap relative to PEP.                     |
  | Trade: Buy KO, Short PEP.                                |
  +----------------------------------------------------------+

  WHICH METHOD TO USE?
  +----------------------------------------------------------+
  | Ratio method: Simpler, intuitive, works for stable pairs. |
  | Spread method: More rigorous, accounts for the hedge      |
  |   ratio, better for pairs with different volatilities.    |
  | Most quantitative traders use the spread method.          |
  +----------------------------------------------------------+
```

#### Z-Score: The Trading Signal

The z-score standardizes the spread so you can compare deviations across different pairs and time periods:

```
Z-SCORE CALCULATION:

  Z-score = (Current Spread - Mean Spread) / Std Dev of Spread

  Example:
  Current spread:     0.50
  Historical mean:    2.00
  Standard deviation: 0.80
  
  Z-score = (0.50 - 2.00) / 0.80 = -1.875

  INTERPRETATION:
  The spread is 1.875 standard deviations BELOW its mean.
  This means KO is unusually cheap relative to PEP.


  Z-SCORE TRADING SIGNALS:

  Z-score
  +3.0 |                                    <- Extreme (short A, long B)
       |
  +2.0 |-------- SELL SIGNAL --------        <- Enter short A, long B
       |
  +1.0 |
       |
   0.0 |=============== MEAN ===============  <- Fair value
       |
  -1.0 |
       |
  -2.0 |-------- BUY SIGNAL ---------        <- Enter long A, short B
       |
  -3.0 |                                    <- Extreme (long A, short B)


  STANDARD TRADING RULES:

  +----------------------------------------------------------+
  | ENTRY SIGNALS:                                            |
  |                                                           |
  | Z-score < -2.0:  Buy Stock A, Short Stock B              |
  |   (A is cheap relative to B)                             |
  |                                                           |
  | Z-score > +2.0:  Short Stock A, Buy Stock B              |
  |   (A is expensive relative to B)                         |
  |                                                           |
  | EXIT SIGNALS:                                             |
  |                                                           |
  | Z-score returns to 0:  Close both positions              |
  |   (Spread has reverted to the mean)                      |
  |                                                           |
  | STOP-LOSS:                                                |
  |                                                           |
  | Z-score exceeds +/- 4.0:  Close positions, take loss     |
  |   (Relationship may have broken down)                     |
  +----------------------------------------------------------+
```

#### How a Pair Trade Works: Complete Example

```
PAIR TRADE WALKTHROUGH: Coca-Cola (KO) vs. PepsiCo (PEP)

  SETUP (based on historical analysis):
  +----------------------------------------------------------+
  | Pair: KO / PEP                                           |
  | Correlation: 0.87                                         |
  | Cointegration p-value: 0.008 (strongly cointegrated)      |
  | Hedge ratio (beta): 0.35                                  |
  | Mean spread: 2.00                                         |
  | Spread std dev: 0.80                                      |
  | Lookback period: 252 trading days (1 year)                |
  +----------------------------------------------------------+

  DAY 1: SIGNAL DETECTED
  +----------------------------------------------------------+
  | KO price: $58.00                                          |
  | PEP price: $172.00                                        |
  | Spread = 58 - (0.35 x 172) = 58 - 60.20 = -2.20         |
  | Z-score = (-2.20 - 2.00) / 0.80 = -5.25                 |
  |                                                           |
  | Wait - that seems extreme. Let us use a more realistic   |
  | example with actual reasonable numbers.                    |
  +----------------------------------------------------------+

  Let us recalibrate with cleaner numbers:

  HISTORICAL ANALYSIS:
  +----------------------------------------------------------+
  | Price ratio (KO/PEP) over last year:                     |
  | Mean ratio: 0.370                                         |
  | Std deviation: 0.015                                      |
  +----------------------------------------------------------+

  DAY 1: ENTRY SIGNAL
  +----------------------------------------------------------+
  | KO price: $57.00                                          |
  | PEP price: $172.00                                        |
  | Current ratio: 57 / 172 = 0.3314                         |
  | Z-score = (0.3314 - 0.370) / 0.015 = -2.57              |
  |                                                           |
  | Signal: Z-score < -2.0                                   |
  | KO is cheap relative to PEP.                             |
  | Action: BUY KO, SHORT PEP                                |
  +----------------------------------------------------------+
  
  POSITION SIZING (dollar-neutral):
  +----------------------------------------------------------+
  | Total capital allocated: $50,000                          |
  |                                                           |
  | Long leg:  Buy 439 shares of KO at $57.00 = $25,023     |
  | Short leg: Short 145 shares of PEP at $172 = $24,940    |
  |                                                           |
  | Approximately equal dollar amounts on each side.          |
  | Net market exposure: ~$83 (essentially zero).             |
  +----------------------------------------------------------+

  DAY 15: CONVERGENCE BEGINS
  +----------------------------------------------------------+
  | KO rises to $59.50  (+4.4%)                              |
  | PEP drops to $169.00 (-1.7%)                             |
  | Current ratio: 59.50 / 169.00 = 0.3521                  |
  | Z-score = (0.3521 - 0.370) / 0.015 = -1.19              |
  |                                                           |
  | The spread is converging toward the mean.                 |
  | Hold the position.                                        |
  +----------------------------------------------------------+
  
  P&L so far:
  +----------------------------------------------------------+
  | KO long:  439 x ($59.50 - $57.00) = +$1,097.50          |
  | PEP short: 145 x ($172.00 - $169.00) = +$435.00         |
  | Total P&L: +$1,532.50 (+3.07% on $50,000)               |
  | Both sides are profitable!                                |
  +----------------------------------------------------------+

  DAY 28: EXIT SIGNAL
  +----------------------------------------------------------+
  | KO at $61.00  (+7.0% from entry)                         |
  | PEP at $166.00 (-3.5% from entry)                        |
  | Current ratio: 61.00 / 166.00 = 0.3675                  |
  | Z-score = (0.3675 - 0.370) / 0.015 = -0.17              |
  |                                                           |
  | Z-score near zero = spread has reverted to mean.          |
  | Action: CLOSE BOTH POSITIONS                             |
  +----------------------------------------------------------+
  
  FINAL P&L:
  +----------------------------------------------------------+
  | KO long:  439 x ($61.00 - $57.00) = +$1,756.00          |
  | PEP short: 145 x ($172.00 - $166.00) = +$870.00         |
  | Total P&L: +$2,626.00                                    |
  | Return: +$2,626 / $50,000 = +5.25% in 28 days           |
  | Annualized: ~68% (though not every trade works this well)|
  +----------------------------------------------------------+
```

#### Dollar-Neutral vs. Beta-Neutral

When sizing a pair trade, there are two main approaches:

```
POSITION SIZING APPROACHES:

  1. DOLLAR-NEUTRAL
  +----------------------------------------------------------+
  | Equal dollar amounts on each side.                        |
  | Long $25,000 of Stock A, Short $25,000 of Stock B.       |
  |                                                           |
  | Simple to implement, but not perfect if the two stocks    |
  | have different betas (market sensitivities).              |
  |                                                           |
  | Example: If Stock A has beta 1.2 and Stock B has beta 0.8|
  | Your $25K long has effective market exposure of $30K      |
  | Your $25K short has effective market exposure of -$20K    |
  | Net market exposure: $10K (not truly neutral)             |
  +----------------------------------------------------------+

  2. BETA-NEUTRAL
  +----------------------------------------------------------+
  | Adjust position sizes so that market exposure cancels.    |
  |                                                           |
  | Formula:                                                  |
  | Short $ = Long $ x (Beta_Long / Beta_Short)              |
  |                                                           |
  | Example: Stock A beta = 1.2, Stock B beta = 0.8          |
  | If long $25,000 of A:                                    |
  | Short $ = $25,000 x (1.2 / 0.8) = $37,500 of B         |
  |                                                           |
  | Market exposure check:                                    |
  | Long: $25,000 x 1.2 = $30,000 effective                 |
  | Short: -$37,500 x 0.8 = -$30,000 effective              |
  | Net: $0 (truly market neutral)                           |
  +----------------------------------------------------------+

  COMPARISON:
  
  Method           Simplicity    Market Neutrality    Best For
  ==============   ==========    =================    =========
  Dollar-neutral   High          Approximate          Same-sector
                                                      similar-beta
                                                      pairs
  Beta-neutral     Medium        Precise              Cross-sector
                                                      or different-
                                                      beta pairs
```

#### The Sector-Neutral Approach

Pair trading is most reliable when both stocks are in the same sector. Here is why:

```
WHY SECTOR NEUTRALITY MATTERS:

  SAME-SECTOR PAIR (KO vs PEP):
  +----------------------------------------------------------+
  | Shared risk factors:                                      |
  | - Consumer spending trends              HEDGED            |
  | - Sugar / commodity prices              HEDGED            |
  | - FDA regulations on beverages          HEDGED            |
  | - Retail distribution changes           HEDGED            |
  | - Weather affecting sales               HEDGED            |
  |                                                           |
  | Company-specific factors:                                 |
  | - KO launches successful new product    CAPTURED          |
  | - PEP has management misstep            CAPTURED          |
  |                                                           |
  | Result: You profit from company-specific differences      |
  | while sector-wide risks cancel out.                       |
  +----------------------------------------------------------+

  CROSS-SECTOR PAIR (AAPL vs XOM):
  +----------------------------------------------------------+
  | Different risk factors:                                   |
  | - Tech sector: AI hype, regulation      NOT HEDGED        |
  | - Energy sector: Oil prices, OPEC       NOT HEDGED        |
  | - Consumer electronics demand           NOT HEDGED        |
  | - Drilling permits, ESG pressure        NOT HEDGED        |
  |                                                           |
  | Result: You are exposed to sector rotation risk.          |
  | If tech rallies and energy drops, both sides of           |
  | your trade move against you simultaneously.               |
  +----------------------------------------------------------+

  SECTOR-NEUTRAL PAIR CATEGORIES:

  +-------------------+----------------------------------------+
  | Sector            | Example Pairs                          |
  +-------------------+----------------------------------------+
  | Beverages         | KO/PEP                                |
  | Oil Majors        | XOM/CVX                               |
  | Banks             | JPM/BAC, GS/MS                        |
  | Payment Networks  | V/MA                                  |
  | Home Improvement  | HD/LOW                                |
  | Semiconductors    | AMD/INTC, AVGO/TXN                    |
  | Airlines          | DAL/UAL                               |
  | Telecom           | VZ/T                                  |
  | Pharma            | JNJ/PFE, MRK/ABBV                     |
  | E-commerce        | AMZN/SHOP (different sizes, careful)   |
  | Autos             | GM/F                                  |
  | Fast Food         | MCD/YUM                               |
  +-------------------+----------------------------------------+
```

#### Mean Reversion and Half-Life

The half-life of a spread tells you how long it typically takes for the spread to revert halfway to its mean. This is crucial for determining your trading horizon:

```
HALF-LIFE OF MEAN REVERSION:

  CONCEPT:
  If the spread is currently 2 standard deviations from the mean,
  the half-life tells you how many days (on average) it takes
  for the spread to move back to 1 standard deviation from the mean.

  CALCULATION:
  From the Ornstein-Uhlenbeck process:
  
  Spread_t = Spread_{t-1} x theta + noise
  
  Where theta is the mean reversion speed.
  Half-life = -ln(2) / ln(theta)

  INTERPRETATION:
  +-------------------+------------------------------------------+
  | Half-life         | Trading Implication                      |
  +-------------------+------------------------------------------+
  | < 5 days          | Very fast reversion. Day-trading pairs.  |
  |                   | May be too fast for retail traders.       |
  +-------------------+------------------------------------------+
  | 5 - 15 days       | Fast reversion. Swing trading pairs.     |
  |                   | Good for active retail traders.           |
  +-------------------+------------------------------------------+
  | 15 - 30 days      | Moderate reversion. Position trading.    |
  |                   | Ideal for most pair traders.              |
  +-------------------+------------------------------------------+
  | 30 - 60 days      | Slow reversion. Longer-term pairs.       |
  |                   | Requires patience and capital.            |
  +-------------------+------------------------------------------+
  | > 60 days         | Very slow. May not be reliably           |
  |                   | mean-reverting. Avoid for pair trading.   |
  +-------------------+------------------------------------------+

  VISUAL:

  Spread
  Deviation
       |
  +2 SD|     *
       |    * *
  +1 SD|   *   *
       |  *     *         <- Half-life: time to go from +2 SD to +1 SD
   Mean|--*------*--------*---*---*---*-----
       |          *      *
  -1 SD|           *    *
       |            *  *
  -2 SD|             **
       +--|----|----|----|----|----|----|-->
          0    5   10   15   20   25   30  Days
          
          |<-Half-life->|
          (example: ~8 days)
```

#### Practical Implementation Steps

```
PAIR TRADING IMPLEMENTATION CHECKLIST:

  STEP 1: UNIVERSE SELECTION
  +----------------------------------------------------------+
  | - Start with stocks in the same sector/industry           |
  | - Filter for sufficient liquidity (avg volume > 1M)       |
  | - Filter for sufficient market cap (> $5B)                |
  | - Remove stocks with pending mergers or special events    |
  +----------------------------------------------------------+
       |
       v
  STEP 2: CORRELATION SCREENING
  +----------------------------------------------------------+
  | - Calculate pairwise correlations for all pairs           |
  | - Filter for correlation > 0.80 over trailing 252 days   |
  | - This reduces the universe dramatically                  |
  +----------------------------------------------------------+
       |
       v
  STEP 3: COINTEGRATION TESTING
  +----------------------------------------------------------+
  | - Run Engle-Granger test on remaining pairs               |
  | - Keep only pairs with p-value < 0.05                     |
  | - Calculate hedge ratios from the regression              |
  +----------------------------------------------------------+
       |
       v
  STEP 4: HALF-LIFE CALCULATION
  +----------------------------------------------------------+
  | - Estimate mean reversion speed for each pair             |
  | - Filter for half-life between 5 and 60 days              |
  | - Shorter = faster trades; longer = more patience needed  |
  +----------------------------------------------------------+
       |
       v
  STEP 5: Z-SCORE MONITORING
  +----------------------------------------------------------+
  | - Calculate rolling z-score for each validated pair       |
  | - Set entry threshold (typically z = +/- 2.0)            |
  | - Set exit threshold (typically z = 0)                    |
  | - Set stop-loss threshold (typically z = +/- 4.0)        |
  +----------------------------------------------------------+
       |
       v
  STEP 6: TRADE EXECUTION
  +----------------------------------------------------------+
  | - When z-score triggers entry, execute both legs          |
  |   simultaneously                                          |
  | - Use dollar-neutral or beta-neutral sizing               |
  | - Monitor daily for exit or stop-loss signals             |
  +----------------------------------------------------------+
       |
       v
  STEP 7: PERFORMANCE TRACKING
  +----------------------------------------------------------+
  | - Track P&L for each pair separately                      |
  | - Monitor correlation and cointegration stability         |
  | - Re-run statistical tests monthly                        |
  | - Replace pairs that lose cointegration                   |
  +----------------------------------------------------------+
```

#### Risks of Pair Trading

```
PAIR TRADING RISKS:

  1. DIVERGENCE RISK (Relationship Breakdown)
  +----------------------------------------------------------+
  | The historical relationship between two stocks can break. |
  |                                                           |
  | Causes:                                                   |
  | - One company gets acquired                               |
  | - Regulatory change affects one but not the other         |
  | - Major product failure or breakthrough at one company    |
  | - Accounting fraud at one company                         |
  |                                                           |
  | Example: Pair trading Lehman Brothers vs Goldman Sachs    |
  | would have been catastrophic in 2008 when Lehman went     |
  | bankrupt while Goldman survived.                          |
  |                                                           |
  | Mitigation: Use stop-losses (exit if z-score > 4),       |
  | diversify across multiple pairs, re-test cointegration    |
  | regularly.                                                |
  +----------------------------------------------------------+

  2. EXECUTION RISK (Leg Risk)
  +----------------------------------------------------------+
  | A pair trade requires executing two trades simultaneously.|
  | If one leg fills and the other does not (or fills at a    |
  | different price), you have unintended directional         |
  | exposure.                                                 |
  |                                                           |
  | Example: You enter a buy order for KO and a short order  |
  | for PEP. KO fills instantly but PEP has a short-sale     |
  | restriction and your short does not execute. Now you are  |
  | just long KO with no hedge.                              |
  |                                                           |
  | Mitigation: Use liquid stocks, trade during high-volume   |
  | periods, consider using limit orders with contingencies.  |
  +----------------------------------------------------------+

  3. MODEL RISK (Statistical False Positives)
  +----------------------------------------------------------+
  | Past cointegration does not guarantee future              |
  | cointegration. Statistical tests can produce false        |
  | positives, especially when testing many pairs.            |
  |                                                           |
  | If you test 1,000 pairs, ~50 will appear cointegrated    |
  | at the 5% significance level purely by chance.            |
  |                                                           |
  | Mitigation: Require economic rationale (same sector),     |
  | use out-of-sample testing, apply multiple testing         |
  | corrections (Bonferroni, Holm).                           |
  +----------------------------------------------------------+

  4. REGIME CHANGE RISK
  +----------------------------------------------------------+
  | Market regimes shift. A pair that was stable for years    |
  | may break during a crisis or structural change.           |
  |                                                           |
  | Example: Before 2020, airlines traded in relatively      |
  | tight pairs. COVID-19 caused divergences that no          |
  | historical model anticipated.                             |
  |                                                           |
  | Mitigation: Use adaptive lookback windows, monitor        |
  | macro conditions, reduce position sizes during            |
  | uncertainty.                                              |
  +----------------------------------------------------------+

  5. CROWDING RISK
  +----------------------------------------------------------+
  | Popular pairs attract many traders. When everyone trades  |
  | the same pair, the edge diminishes. Worse, if many        |
  | traders exit simultaneously, the convergence trade can    |
  | reverse violently.                                        |
  |                                                           |
  | The "quant meltdown" of August 2007 saw many quant        |
  | funds using similar pair trading strategies suffer         |
  | simultaneous losses as they all tried to exit at once.    |
  |                                                           |
  | Mitigation: Trade less obvious pairs, diversify across    |
  | many pairs, avoid the most popular pair trades.           |
  +----------------------------------------------------------+

  6. SHORT SELLING CONSTRAINTS
  +----------------------------------------------------------+
  | The short leg of a pair trade faces all the risks we      |
  | discussed in Week 13: borrow costs, share recall,         |
  | short-sale restrictions, and dividend payments.           |
  |                                                           |
  | Mitigation: Only pair trade liquid, easy-to-borrow        |
  | stocks. Factor borrow costs into expected returns.        |
  +----------------------------------------------------------+
```

---

### c) Common Misconceptions

**Misconception 1: "If two stocks are highly correlated, they make a good pair."**

This is the most common and most dangerous misconception in pair trading. Correlation measures whether two stocks move in the same direction. Cointegration measures whether the spread between them is stable and mean-reverting. Two stocks can have a correlation of 0.95 and still be terrible for pair trading if their spread drifts over time. Amazon and Google were highly correlated for years, but they are not cointegrated because their growth rates and valuations diverge persistently. Always test for cointegration, not just correlation.

**Misconception 2: "Pair trading is risk-free because you are long and short at the same time."**

Pair trading eliminates broad market risk (beta), but it does not eliminate stock-specific risk. If the company you are long announces terrible earnings and the company you are short announces great earnings, you lose on both sides of the trade. The relationship between the two stocks can break down permanently due to acquisitions, regulatory changes, or fundamental shifts. Pair trading reduces risk; it does not eliminate it.

**Misconception 3: "The wider the spread divergence, the better the opportunity."**

While a larger divergence (higher z-score) might suggest a bigger profit potential, extreme divergences often signal that the relationship is breaking down rather than presenting an opportunity. A z-score of 5 might mean "incredible bargain" or it might mean "something fundamental has changed and the spread will never revert." This is why stop-losses are essential. Professional pair traders are wary of extreme divergences and investigate the cause before trading.

**Misconception 4: "You can pair trade any two stocks in the same sector."**

Same-sector membership is necessary but not sufficient. Ford and Tesla are both in the automotive sector, but they have very different business models, growth profiles, investor bases, and volatility characteristics. A pair trade between them would be unreliable because the factors driving their stock prices are quite different despite sharing a sector classification. The best pairs are companies with truly similar business models, customer bases, and competitive positions.

**Misconception 5: "Pair trading always profits from mean reversion."**

Pair trading profits from mean reversion of the spread, but mean reversion is a statistical tendency, not a guarantee. Some trades will hit stop-losses as the spread continues to diverge. Some pairs will lose their cointegration relationship. The edge in pair trading comes from the fact that, over many trades, the spread reverts to the mean more often than it does not. Individual trades can and will lose money.

**Misconception 6: "Pair trading was killed by quant funds and algorithms."**

It is true that the proliferation of quantitative trading has made simple pair trading less profitable than it was in the 1990s. The obvious pairs and simple z-score signals have been arbitraged by faster, more sophisticated players. However, pair trading remains viable for several reasons: new pairs form as industries evolve, the strategy works across asset classes beyond equities, and fundamental-driven pair trading (combining statistical signals with fundamental analysis) still offers an edge that pure statistical approaches miss. The strategy has evolved, not died.

---

### d) Common Questions and Answers

**Q1: How much capital do I need to start pair trading?**

A: Because you need to hold both a long and a short position simultaneously, pair trading requires more capital than simple stock buying. A single pair trade with roughly $12,500 on each side requires about $25,000 total. However, because the short side uses margin, you typically need an approved margin account with at least $25,000 (the Pattern Day Trader minimum in the US, if you plan to trade frequently). For diversification across multiple pairs, $50,000-$100,000 is more realistic. Some brokers allow smaller pair trades, but tight position sizing becomes difficult below $25,000.

**Q2: How many pairs should I trade simultaneously?**

A: Diversification across pairs is important because individual pairs can break down. Professional pair traders typically hold 10-30 pairs simultaneously, which provides sufficient diversification. For individual investors, 5-10 pairs is more manageable and still provides reasonable diversification. The key is that each pair should be somewhat independent, trading KO/PEP and MCD/YUM is fine because they are in different sub-industries (beverages vs restaurants), but trading XOM/CVX and XOM/COP is less diversified because XOM appears in both pairs.

**Q3: How often do I need to rebalance or adjust pair trade positions?**

A: There are three triggers for adjusting positions. First, when the z-score reaches your exit threshold (typically 0), you close the trade. Second, when the z-score reaches your stop-loss threshold (typically plus or minus 4), you close the trade to limit losses. Third, if the dollar amounts of the two legs have drifted significantly (say, more than 10% apart), you should rebalance to maintain approximately equal dollar exposure. Most pair traders check their positions daily and rebalance weekly if needed.

**Q4: Can I pair trade ETFs instead of individual stocks?**

A: Yes, and this is often easier for beginners. ETF pairs like XLF/XLK (Financials vs Technology), GLD/SLV (Gold vs Silver), or EEM/EFA (Emerging Markets vs Developed International) can be used for pair trading. ETFs offer higher liquidity, lower single-stock risk, and easy borrowing for short selling. The tradeoff is that ETF pairs tend to revert more slowly because sector-level divergences are smoother than individual stock divergences.

**Q5: What lookback period should I use for calculating the spread mean and standard deviation?**

A: There is no universally correct answer, but 60 to 252 trading days (roughly 3 months to 1 year) is the most common range. Shorter lookback periods are more responsive to recent changes but more susceptible to noise. Longer lookback periods are more stable but may include outdated data. A common approach is to use a 126-day (6-month) rolling window for z-score calculation and test cointegration on 1-2 years of data. Some traders use an exponentially weighted moving average to give more weight to recent observations.

**Q6: What happens if one stock in my pair gets acquired?**

A: This is one of the biggest risks in pair trading. If you are long Stock A and short Stock B, and Stock B receives a takeover bid at a 30% premium, Stock B jumps 30% overnight and you lose 30% on your short leg while Stock A may barely move. This scenario can result in a large loss on what appeared to be a hedged position. Mitigation strategies include: avoiding stocks with active takeover rumors, keeping individual pair sizes small (2-5% of capital), and monitoring M&A activity in the sectors you trade.

**Q7: Is pair trading the same as statistical arbitrage?**

A: Pair trading is the simplest form of statistical arbitrage (stat arb). Traditional pair trading involves a single pair of stocks. Statistical arbitrage extends this to trading many pairs simultaneously, using more sophisticated models, incorporating multiple factors beyond just price relationships, and often trading hundreds or thousands of pairs with automated execution. Think of pair trading as one-dimensional stat arb. Professional stat arb funds use the same core concepts (cointegration, mean reversion, z-scores) but apply them at much larger scale with more complexity.

**Q8: Can pair trading work in a trending market?**

A: Yes, and this is one of its advantages. Because pair trading is market-neutral (or approximately so), the strategy is largely indifferent to whether the market is trending up, down, or sideways. In a bull market, both stocks tend to rise, and you profit if your long rises more than your short. In a bear market, both stocks tend to fall, and you profit if your short falls more than your long. The strategy struggles when sector-specific factors cause one stock to decouple from its pair, regardless of overall market direction.

**Q9: How do taxes work for pair trading?**

A: Pair trading creates both capital gains and losses within the same trade. The long leg generates a capital gain or loss when closed, and the short leg generates a short-term capital gain or loss (short positions are always taxed as short-term, regardless of holding period). Because you frequently open and close positions, most pair trading profits are taxed at short-term capital gains rates. The wash sale rule can also be a factor if you re-enter a pair within 30 days of closing it at a loss. Consult a tax professional familiar with active trading strategies.

**Q10: What software or tools do I need for pair trading?**

A: At minimum, you need: (1) a brokerage account with margin and short-selling capabilities, (2) historical price data for your target stocks (freely available from Yahoo Finance or your broker), and (3) a spreadsheet or programming environment to calculate correlations, run cointegration tests, and compute z-scores. Python with libraries like pandas, statsmodels, and numpy is the most popular choice. R is also widely used. Some brokers offer built-in pair trading analytics. For beginners, a spreadsheet with basic formulas is sufficient to get started, though you will eventually want to automate the analysis.

---

## YouTube Script

[VISUAL: Animated intro with show logo. Text: "Week 14: Pair Trading Fundamentals - Level 2: Intermediate"]

**Alex:** Welcome back. Last week we covered long and short trading, and I mentioned that this week we would explore one of the most elegant strategies in quantitative finance. Today we are talking about pair trading.

**Sam:** Pair trading. I have heard hedge fund managers talk about this, but it always seemed like something only quants with PhD degrees could do.

**Alex:** That is a common perception, but the core concept is actually very intuitive. Let me start with an analogy. Imagine you are at a racetrack and you have two horses from the same stable. Horse A and Horse B. They have similar training, similar records, and they usually finish close together.

**Sam:** OK, I am following.

**Alex:** Now, today the odds on Horse A are unusually high, meaning the market thinks Horse A will do poorly. But you know these two horses always finish close together. So instead of betting on which horse will win the race, you bet that the GAP between them will be small. You bet on Horse A to outperform relative to Horse B.

**Sam:** So you are not predicting who wins the race. You are predicting that the gap between them will close.

**Alex:** Exactly. And here is the beautiful part. It does not matter if both horses run fast or both horses run slow. You do not care about the absolute performance. You only care about the relative performance. That is pair trading.

[VISUAL: Racetrack animation showing two horses running. Both could be fast or slow, but the bettor only cares about the gap between them. Arrow points to the gap labeled "This is what you trade."]

**Sam:** OK translate that into stocks for me.

**Alex:** Let us use a classic example: Coca-Cola and PepsiCo. These two companies are in the same industry, sell similar products, face similar competitive pressures, and their stock prices tend to move together over time. Historically, the ratio of their prices stays within a fairly narrow band.

[VISUAL: Side-by-side comparison of KO and PEP showing logos, key metrics (similar revenue, similar margins, similar market cap), and a chart of their prices moving roughly together over 5 years]

**Alex:** Now occasionally, something happens that causes one stock to temporarily outperform or underperform the other. Maybe Coca-Cola misses earnings expectations by a penny and the stock drops 3%, while Pepsi is flat. Or maybe Pepsi gets a negative analyst report and drops while Coke holds steady.

**Sam:** And a pair trader would see that as an opportunity?

**Alex:** Exactly. If the ratio between their prices has deviated from its historical average, a pair trader bets that it will revert back to normal. If Coke is temporarily cheap relative to Pepsi, you buy Coke and short Pepsi. If Coke is temporarily expensive relative to Pepsi, you short Coke and buy Pepsi.

[ANIMATION: Reference animation/week14_pair_trade.py - Animation showing the price ratio of KO/PEP over time as a line chart. The mean ratio is shown as a horizontal dashed line. As the ratio dips below the mean (KO relatively cheap), a "BUY KO / SHORT PEP" signal appears in green. As it rises above the mean, a "SHORT KO / BUY PEP" signal appears in red. The animation then zooms into one trade cycle, showing: entry when the ratio is 2 standard deviations below the mean, the spread gradually converging back to the mean, and exit when the ratio returns to normal. P&L counters update in real-time for both legs of the trade.]

**Sam:** And when the ratio comes back to normal, you close both positions and pocket the profit.

**Alex:** Right. And here is why this is so powerful. Notice that you are simultaneously long one stock and short the other. What happens if the entire stock market crashes 20%?

**Sam:** Both Coke and Pepsi would drop.

**Alex:** But they would drop by roughly similar amounts because they are in the same industry and affected by the same factors. Your long position loses money, but your short position makes money. They roughly cancel out. Your pair trade is insulated from the market crash.

[VISUAL: Three-panel scenario showing: (1) Market crashes 20%, KO drops 18%, PEP drops 22%. Long KO: -18%, Short PEP: +22%, Net: +4%. (2) Market rallies 15%, KO rises 18%, PEP rises 12%. Long KO: +18%, Short PEP: -12%, Net: +6%. (3) Market flat, KO rises 3%, PEP falls 2%. Long KO: +3%, Short PEP: +2%, Net: +5%.]

**Sam:** So you make money in all three scenarios? That seems too good to be true.

**Alex:** It is not too good to be true, but there are important caveats we will get to. First, let me be clear about what makes a good pair, because not any two stocks will work.

**Sam:** What criteria do you look for?

**Alex:** Four main things. First, same sector or industry. Coca-Cola and Pepsi work because they face the same competitive forces. Apple and ExxonMobil would be a terrible pair because completely different factors drive their prices.

**Sam:** Makes sense. What else?

**Alex:** Second, similar business models and size. You want companies that are genuine competitors. Visa and Mastercard are a great pair because they run nearly identical payment networks. Goldman Sachs and Morgan Stanley work because they are both investment banks of similar scale.

[VISUAL: Grid showing "Good Pairs" with checkmarks (KO/PEP, XOM/CVX, V/MA, HD/LOW, GS/MS) and "Bad Pairs" with X marks (AAPL/XOM, GOOGL/JNJ, TSLA/F)]

**Sam:** What about the third criterion?

**Alex:** Third, high historical correlation. You want stocks that have moved together in the past. A correlation above 0.80 is a good starting point. But here is where I need to introduce a crucial distinction that trips up a lot of people.

**Sam:** What is that?

**Alex:** The difference between correlation and cointegration. This is probably the single most important concept in pair trading, and getting it wrong is the most common reason pair trades fail.

**Sam:** OK. Explain the difference.

**Alex:** Correlation tells you whether two stocks move in the same direction. When one goes up, the other tends to go up. When one goes down, the other tends to go down. High correlation means they move in sync.

**Sam:** That sounds like what you want for pair trading.

**Alex:** It is necessary, but it is not sufficient. Here is why. Imagine two stocks that both go up over time, Stock A going from $50 to $200 and Stock B going from $50 to $100. Their correlation might be 0.95 because they both trend upward together. But the gap between them keeps growing. Stock A outperforms Stock B consistently.

[VISUAL: Chart showing two lines both trending up, but diverging. Line A rises faster than Line B. Correlation shown as 0.95. But the spread between them keeps widening. Label: "High Correlation, NOT Cointegrated"]

**Sam:** So the spread is not stable. It keeps getting bigger.

**Alex:** Exactly. If you had bet on the spread converging, you would have lost money continuously. This is why correlation alone is not enough.

**Alex:** Cointegration is different. It measures whether the spread between two stocks is stable and tends to return to a mean. Two cointegrated stocks might wander apart temporarily, but they always come back together. Like two dogs on leashes held by one person. Each dog might dart left or right, but the leash keeps them from getting too far apart.

**Sam:** That is a great analogy. The leash is the cointegration.

**Alex:** Exactly. When you find a pair of stocks that is cointegrated, you have statistical evidence that their spread is mean-reverting. When it diverges, it tends to come back. That is the foundation of a profitable pair trade.

[VISUAL: Chart showing two lines weaving around each other. Sometimes A is higher, sometimes B is higher, but they keep converging back. The spread oscillates around zero. Label: "Cointegrated: Spread is Mean-Reverting"]

**Sam:** How do you test for cointegration? Do you need a PhD in statistics?

**Alex:** You need a basic understanding of statistics and a tool that can run the test. The most common method is the Augmented Dickey-Fuller test, also called the ADF test. Here is how it works in plain English.

**Alex:** Step one. You calculate the spread between the two stocks using a regression. You run a regression of Stock A's price on Stock B's price, and the residuals from that regression are your spread.

**Sam:** The residuals. So the part of Stock A's price that cannot be explained by Stock B's price.

**Alex:** Exactly. Step two. You run the ADF test on those residuals. The test asks a simple question: does this spread tend to revert to a mean, or does it wander randomly? If the p-value from the test is less than 0.05, you have evidence that the spread is mean-reverting, which means the pair is cointegrated.

[VISUAL: Simple flowchart: "Step 1: Regress Price A on Price B" -> "Get Residuals (Spread)" -> "Step 2: ADF Test on Residuals" -> Decision diamond: "p-value < 0.05?" -> Yes: "Cointegrated - Good Pair" / No: "Not Cointegrated - Avoid"]

**Sam:** That seems manageable. What tools can you use?

**Alex:** Python is the most popular. With the statsmodels library, the cointegration test is literally one line of code. But you can also use R, Excel with add-ins, or even some brokerage platforms that have pair trading analytics built in.

**Sam:** OK so let us say I have found a good pair. The stocks are in the same sector, they are correlated, they are cointegrated. How do I actually trade it?

**Alex:** This is where the z-score comes in. The z-score standardizes the spread so you know exactly how far it has deviated from normal. The formula is: z-score equals the current spread minus the mean spread, divided by the standard deviation of the spread.

**Sam:** So it tells you how many standard deviations the spread is from its average.

**Alex:** Right. And here are the standard trading rules. When the z-score drops below minus 2, it means Stock A is unusually cheap relative to Stock B. You buy A and short B. When the z-score rises above plus 2, Stock A is unusually expensive relative to Stock B. You short A and buy B. When the z-score returns to zero, the spread has reverted to the mean and you close both positions.

[ANIMATION: Reference animation/week14_pair_trade.py - A second animation showing a z-score chart over time. The z-score oscillates between approximately -3 and +3. Horizontal lines mark the entry thresholds at +2 and -2, and the exit level at 0. When the z-score crosses -2 going down, a green "ENTER: Buy A, Short B" flag appears. When it returns to 0, a white "EXIT: Close Both" flag appears. When it crosses +2 going up, a red "ENTER: Short A, Buy B" flag appears. A running P&L tracker shows cumulative profit from completed trades. The animation plays through 4-5 complete trade cycles.]

**Sam:** And if the z-score keeps going further away from zero instead of reverting?

**Alex:** That is your stop-loss scenario. If the z-score exceeds plus or minus 4, it suggests that the historical relationship may be breaking down. Something fundamental has changed. You close the position and take the loss rather than hoping for a reversion that may never come.

**Sam:** Let us walk through a complete trade example.

**Alex:** Let us do it. We will use Visa and Mastercard, one of the best-known pairs on Wall Street.

[VISUAL: Visa and Mastercard logos side by side, with key stats: Both payment network duopolists, Correlation: 0.92, Cointegration p-value: 0.003]

**Alex:** Imagine the historical price ratio of Visa to Mastercard has averaged 0.55 over the past year, with a standard deviation of 0.02. Today, Visa is at $250 and Mastercard is at $490. The current ratio is 250 divided by 490, which equals 0.510.

**Sam:** The ratio is below the average. Visa is cheap relative to Mastercard?

**Alex:** Let us check the z-score. Current ratio 0.510, minus the mean of 0.550, divided by the standard deviation of 0.020. That gives us negative 2.0. We are right at our entry threshold.

**Sam:** So the signal says buy Visa, short Mastercard.

**Alex:** Exactly. Now we need to size the position. We will use dollar-neutral sizing, meaning equal dollar amounts on each side. Let us say we allocate $50,000 total. We put $25,000 into long Visa at $250, buying 100 shares. And we put $25,000 into short Mastercard at $490, shorting 51 shares, which is about $24,990.

[VISUAL: Trade ticket showing: "LONG 100 V @ $250 = $25,000" and "SHORT 51 MA @ $490 = $24,990" with "Net Market Exposure: ~$10 (essentially zero)"]

**Sam:** So we have almost exactly equal dollar amounts on each side. What happens next?

**Alex:** We wait. Over the next few weeks, let us say Visa reports strong results and rises to $262. Mastercard has a mixed quarter and drops to $478. The ratio is now 262 divided by 478, which equals 0.548. The z-score is 0.548 minus 0.550 divided by 0.020, which equals negative 0.1. Essentially zero.

**Sam:** The spread has reverted to the mean. Time to close?

**Alex:** Yes. We sell our 100 shares of Visa at $262, making $12 per share, for a profit of $1,200. We cover our 51 shares of Mastercard at $478, making $12 per share, for a profit of $612. Total profit: $1,812 on a $50,000 position, or 3.6% in a few weeks.

**Sam:** And both sides of the trade were profitable?

**Alex:** In this case, yes. The long went up and the short went down, which is the ideal scenario. But it does not always work that way. Sometimes you make money on one side and lose on the other, but the winning side earns more than the losing side. The key is that the spread converges, not that both legs individually profit.

[VISUAL: P&L breakdown showing: "Long V: +$1,200" (green bar), "Short MA: +$612" (green bar), "Total: +$1,812 (3.6%)" with a note: "Both legs profitable in this case, but only the SPREAD convergence matters"]

**Sam:** What would a losing trade look like?

**Alex:** Great question. Imagine we enter the same trade but instead of converging, the spread diverges further. Maybe Mastercard gets a major partnership announcement that Visa does not get. Mastercard jumps to $520 while Visa barely moves to $252.

**Sam:** So the ratio goes from 0.510 to 252 divided by 520, which is about 0.485. Even further below the mean.

**Alex:** The z-score goes from negative 2.0 to 0.485 minus 0.550 divided by 0.020, which equals negative 3.25. It is moving in the wrong direction. Our long is barely profitable at $200, but our short has lost us: 51 shares times ($520 minus $490) equals $1,530 loss.

**Sam:** Net, we are losing $1,330.

**Alex:** Right. If the z-score hits negative 4.0, we cut the trade. This is where discipline matters. You cannot let a pair trade turn into a thesis trade where you convince yourself it HAS to come back. Sometimes relationships break down.

[VISUAL: Warning graphic showing "Pair Trade Loss Scenario" with a z-score chart diving past -3 toward -4, with a stop-loss line at -4 and text: "When the spread diverges instead of converging, CUT THE TRADE"]

**Sam:** That brings up the question of risk. What are the biggest risks in pair trading?

**Alex:** The number one risk is relationship breakdown, also called divergence risk. The historical relationship between two stocks can change permanently. This is not just theoretical.

**Sam:** Can you give me a real example?

**Alex:** Sure. Imagine you were pair trading two airline stocks in early 2020. Delta and United, for example. They had a strong historical relationship. Then COVID hit. Both stocks crashed, but they did not crash equally. Delta, with its stronger balance sheet, dropped less and recovered faster. United, with more debt and exposure to international travel, dropped more and recovered more slowly. The spread blew out and never fully reverted.

[VISUAL: Chart showing DAL and UAL from 2019-2021. Pre-COVID the ratio is stable. Post-COVID the ratio shifts to a new level and stays there. Label: "Structural break - relationship changed permanently"]

**Sam:** So the cointegration broke down because the underlying business reality changed.

**Alex:** Exactly. COVID was an extreme example, but smaller structural breaks happen regularly. One company gains a new competitive advantage, or loses a major customer, or makes a transformative acquisition. Any of these can break a pair relationship.

**Sam:** How do you protect against that?

**Alex:** Three ways. First, stop-losses. Never let a losing pair trade run indefinitely. If the z-score reaches 4.0, exit. Second, diversification. Trade multiple pairs so that one breakdown does not destroy your portfolio. Third, regular monitoring. Re-run your cointegration tests monthly. If a pair loses its cointegration, stop trading it.

**Sam:** What about the risk of not being able to execute both legs at the same time?

**Alex:** That is called leg risk or execution risk. A pair trade requires two simultaneous trades. If you buy Visa but your short order for Mastercard does not fill, maybe because of a short-sale restriction or a sudden halt in trading, you are left with just a long Visa position with no hedge. That is directional risk, which is exactly what you were trying to avoid.

**Sam:** How do you manage that?

**Alex:** Trade liquid stocks. Large-cap, high-volume stocks like the ones we have been discussing rarely have execution problems. Avoid small or illiquid stocks for pair trading. Also, some brokers offer pair trading order types that execute both legs simultaneously.

**Sam:** Let us talk about how you find pairs in the first place. Do you just look at companies in the same industry and eyeball their charts?

**Alex:** That is how it started. Early pair traders literally looked at charts and said, "These two seem to move together." But today the process is much more systematic.

**Alex:** Step one, define your universe. Maybe it is the S&P 500, or maybe it is all stocks in the Technology sector. Step two, screen for correlation. Calculate pairwise correlations and keep only pairs above 0.80. Step three, test for cointegration. Run the ADF test on the remaining pairs. Step four, calculate the half-life.

**Sam:** Half-life? Like radioactive decay?

**Alex:** Same concept, different application. The half-life tells you how long it takes, on average, for the spread to revert halfway back to the mean. If the spread is 2 standard deviations away, the half-life tells you how many days until it is about 1 standard deviation away.

[VISUAL: Decay curve showing spread deviation over time. Starting at 2 SD, dropping to 1 SD at the "half-life" mark (e.g., 12 days), then continuing to approach 0. Label: "Half-life = ~12 days in this example"]

**Sam:** Why does that matter?

**Alex:** Because it tells you your expected holding period. If the half-life is 5 days, you are looking at a short-term trade. If it is 60 days, you need the patience to hold for two months. Most pair traders prefer half-lives between 10 and 30 days because that balances responsiveness with reliability.

**Sam:** What if the half-life is too long?

**Alex:** Then the spread reverts so slowly that transaction costs, borrow fees, and opportunity cost eat into your profit. A pair with a 200-day half-life might be cointegrated in the statistical sense, but it is not practical for trading.

**Sam:** Makes sense. Now, I have a practical question. How do you size the two legs of a pair trade? You mentioned dollar-neutral earlier.

**Alex:** There are two main approaches. Dollar-neutral means equal dollar amounts on each side. If you put $25,000 long, you put $25,000 short. This is simple and works well when the two stocks have similar volatility and similar beta.

**Sam:** And when they do not?

**Alex:** Then you use beta-neutral sizing. Beta measures how sensitive a stock is to overall market movements. If Stock A has a beta of 1.2 (more volatile than the market) and Stock B has a beta of 0.8 (less volatile than the market), dollar-neutral is not truly market neutral because your long side moves more with the market than your short side.

**Sam:** So you adjust the sizes?

**Alex:** Right. You would short more of Stock B to compensate for the higher beta on your long side. The formula is: short dollars equals long dollars times the long beta divided by the short beta. So if you are long $25,000 with beta 1.2, your short should be $25,000 times 1.2 divided by 0.8, which equals $37,500.

[VISUAL: Scale/balance diagram showing dollar-neutral (unbalanced, tilting toward long side because higher beta) vs beta-neutral (perfectly balanced). Label: "Beta-neutral provides true market neutrality"]

**Sam:** That is more complex but more accurate.

**Alex:** For pairs in the same sector with similar betas, dollar-neutral is usually fine. For pairs with meaningfully different betas, beta-neutral is better.

**Sam:** Let me ask about the quant meltdown you mentioned earlier. What happened in 2007?

**Alex:** This is one of the most important lessons in pair trading history. In August 2007, many quantitative hedge funds, including some of the most sophisticated in the world, suffered enormous losses in a matter of days. The problem was crowding.

**Sam:** Crowding meaning too many funds were trading the same pairs?

**Alex:** Exactly. Many quant funds had discovered the same statistical relationships and were trading the same pairs using the same signals. When one large fund needed to liquidate, it started selling its long positions and covering its shorts. This pushed the spreads in the wrong direction for every other fund holding the same trades.

[VISUAL: Domino effect animation showing Fund A selling, causing spreads to widen, triggering Fund B to sell, causing further widening, triggering Fund C, and so on. Each domino represents a quant fund falling.]

**Alex:** Those other funds then faced margin calls and had to liquidate too, which pushed spreads even wider, triggering more liquidations. It was a cascade. Some quant funds lost 30% or more in a single week.

**Sam:** So the strategy itself was sound, but too many people doing it at once created a fragility?

**Alex:** Precisely. This is one of the fundamental paradoxes of quantitative finance. The more people discover a profitable strategy, the less profitable it becomes, and the more dangerous it becomes in a crisis because everyone exits at the same time.

**Sam:** How do you avoid crowding?

**Alex:** Look for less obvious pairs. Everyone knows about KO/PEP and XOM/CVX. Those are crowded. Look for pairs in less followed sectors or less common combinations that still have economic rationale. Combine statistical signals with fundamental analysis to find pairs that pure quant models might miss.

**Sam:** Can you walk us through what the pair trading research process actually looks like in practice?

**Alex:** Sure. Let us say you want to explore pair trading opportunities in the semiconductor sector. Step one, you list all major semiconductor companies: INTC, AMD, AVGO, TXN, QCOM, NVDA, MRVL, and so on.

**Sam:** That gives you a lot of possible pairs.

**Alex:** Right. With 8 stocks, you have 28 possible pairs. Step two, you pull a year of daily price data for all of them and calculate pairwise correlations. Maybe you find that TXN and AVGO have a correlation of 0.89, while NVDA and INTC have a correlation of only 0.45.

[VISUAL: Correlation matrix heat map for semiconductor stocks, with hot colors (red/orange) for high correlations and cool colors (blue) for low correlations. TXN/AVGO cell highlighted.]

**Sam:** So you filter out the low-correlation pairs?

**Alex:** Yes. You keep only pairs with correlation above 0.80. Maybe that leaves you with 8 pairs out of 28. Step three, you run the cointegration test on each of those 8 pairs. Maybe 3 pass the test with p-values below 0.05.

**Sam:** Now you have 3 potential pairs.

**Alex:** Step four, you calculate the half-life for each. One has a half-life of 8 days, which is nice and fast. Another has a half-life of 22 days, which is moderate. The third has a half-life of 90 days, which is too slow for practical trading. So you drop the third one.

**Sam:** Two pairs remain. And then you start monitoring the z-scores.

**Alex:** Exactly. You calculate rolling z-scores for both pairs and wait for an entry signal. When one pair's z-score crosses plus or minus 2, you enter the trade. You hold until the z-score returns to zero, or you exit at the stop-loss if it crosses plus or minus 4.

**Sam:** This all sounds very systematic. Can it be automated?

**Alex:** Absolutely, and most professional pair traders do automate it. Python is the tool of choice for most people. You can write scripts that download price data, calculate correlations and cointegration, compute z-scores, generate signals, and even execute trades through broker APIs.

**Sam:** Is there an edge left for individual investors, given that hedge funds and algorithms are doing this at massive scale?

**Alex:** That is the right question. The simple, naive version of pair trading, using basic z-scores on the most obvious pairs, has been largely arbitraged away by professionals. But there are still edges available.

**Sam:** Where?

**Alex:** First, fundamental-driven pair trading. Instead of relying solely on statistical signals, combine them with fundamental analysis. If you have deep knowledge of the semiconductor industry and understand why TXN is better positioned than INTC, you can overlay that on the statistical framework and make better pair selections.

**Alex:** Second, event-driven pair trading. Around earnings announcements, one stock in a pair might overreact while the other does not. This creates temporary dislocations that are too brief for large hedge funds to capture but perfect for individual traders.

**Sam:** Because the big funds are too slow?

**Alex:** Not exactly too slow, but trading at their scale, they cannot enter and exit positions in small, illiquid situations quickly enough. An individual trader with a $50,000 position has much more flexibility than a fund trying to deploy $50 million.

**Alex:** Third, less common pairs. Everyone trades KO/PEP. But what about lesser-known pairs in the utility sector, or the REIT sector, or even international pairs? Less attention means more potential opportunity.

[VISUAL: Three boxes showing "Edges for Individual Pair Traders": "1. Fundamental Insight" (brain icon), "2. Event-Driven Timing" (calendar with lightning bolt), "3. Less Crowded Pairs" (magnifying glass on less-known sector)]

**Sam:** This is really fascinating. Before we wrap up, can you give us a quick summary of the key rules for pair trading?

**Alex:** Sure. Rule one: always test for cointegration, not just correlation. Rule two: trade within the same sector to maintain sector neutrality. Rule three: use z-scores for systematic entry and exit signals. Rule four: always use stop-losses. A z-score of 4 is the standard stop. Rule five: diversify across multiple pairs. Rule six: re-test your pairs regularly because relationships change over time. Rule seven: position size conservatively, no more than 5% of capital per pair. And rule eight: factor in all costs, including borrow fees, dividends, and commissions.

**Sam:** Eight rules. I can work with that.

**Alex:** And one bonus rule: start with paper trading. Pair trading is one of those strategies where the concept seems simple but the execution has a lot of nuance. Practice with simulated trades for at least a few months before risking real money.

**Sam:** That is great advice. Let me try to summarize the whole lesson. Pair trading is a market-neutral strategy where you go long one stock and short a related stock, profiting from the convergence of their price ratio. The key statistical concept is cointegration, not just correlation. You use z-scores to identify entry and exit points. The strategy hedges away market risk so you can profit regardless of market direction. The biggest risks are relationship breakdown, execution risk, and crowding. And it requires discipline, stop-losses, and diversification.

**Alex:** Excellent summary. I would add that pair trading is a gateway strategy. The concepts you learn here, correlation, cointegration, mean reversion, z-scores, relative value, all of these are building blocks for more advanced quantitative strategies that you might explore later.

**Sam:** This has been one of my favorite lessons so far. It feels like a different way of thinking about the market.

**Alex:** That is exactly right. Most investors think about absolute value: is this stock cheap or expensive? Pair trading teaches you to think about relative value: is this stock cheap or expensive COMPARED TO something else? That shift in perspective is valuable no matter what kind of investing you do.

[VISUAL: Preview slide: "Coming Up: More Advanced Strategies - Building on the Long/Short Foundation"]

**Sam:** Lightning round before we go?

**Alex:** Let us do it.

**Sam:** Can you pair trade options instead of stocks?

**Alex:** Yes, and some pair traders use options to express their views with defined risk. For example, instead of shorting a stock, you could buy puts. This eliminates the risk of a short squeeze or share recall. More advanced pair traders use options spreads to fine-tune their risk profiles.

**Sam:** How often do pair trades typically last?

**Alex:** It varies with the half-life of the pair, but most pair trades last between one week and two months. Very few extend beyond three months. If the spread has not reverted in that time, something may have structurally changed.

**Sam:** What is the typical win rate for pair trading?

**Alex:** Well-constructed pair trades based on cointegrated pairs typically win 55-65% of the time. The edge comes not from a high win rate but from the combination of a moderate win rate and a favorable reward-to-risk ratio. Your average win should be larger than your average loss because you let winners ride to the mean but cut losers at the stop-loss.

**Sam:** Can you pair trade crypto?

**Alex:** The concepts apply, but crypto pairs tend to be less stable than equity pairs because the crypto market is younger, less liquid, and more prone to structural changes. Some traders pair Bitcoin with Ethereum, but the cointegration relationship is not as robust as established equity pairs. Proceed with extreme caution if you try this.

**Sam:** Final question: what is the one book or resource you would recommend for someone who wants to learn more about pair trading?

**Alex:** "Algorithmic Trading" by Ernest Chan has an excellent chapter on pair trading with practical Python code. For a more academic treatment, "Pairs Trading" by Ganapathy Vidyamurthy is the gold standard. And for a hands-on approach, I would recommend working through Python tutorials on pair trading using free data from Yahoo Finance. Nothing teaches you like building it yourself.

**Sam:** Great recommendations. Thanks, everyone. See you next time.

**Alex:** Thanks for watching. Like and subscribe, and we will see you soon for more intermediate strategies.

[VISUAL: End screen with subscribe button, playlist link to Level 2: Intermediate Strategies series, and social media handles]

---

*Animation Reference: animation/week14_pair_trade.py - This animation illustrates pair trading in two main sequences. The first sequence shows the price ratio of a pair (e.g., KO/PEP) oscillating around its mean over time, with buy and sell signals triggered when the ratio deviates by 2 standard deviations. A complete trade cycle is shown with real-time P&L tracking for both legs. The second sequence displays a z-score chart with clearly marked entry thresholds at plus and minus 2, exit level at zero, and stop-loss levels at plus and minus 4. Multiple trade cycles play through, demonstrating winning trades (spread reverts) and losing trades (spread diverges to stop-loss), with a cumulative P&L counter tracking overall strategy performance.*
