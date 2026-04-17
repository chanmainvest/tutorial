# Week 31: Yield Curves - The Bond Market's Crystal Ball

## Reading Section

### a) Why This Is Important

The yield curve is the single most watched indicator in the entire bond market, and for good reason. It has predicted every U.S. recession in the past 50 years. It drives the pricing of trillions of dollars in mortgages, corporate loans, and government debt. It shapes Federal Reserve policy and influences every asset class from stocks to real estate. Yet most individual investors cannot explain what a yield curve is, let alone interpret it.

**Why understanding yield curves is essential:**

**1. The yield curve predicted every recession since 1970.** When the yield curve inverts, meaning short-term rates rise above long-term rates, a recession has followed within 6 to 24 months in every instance. No other economic indicator has such a consistent track record. The 2-year/10-year Treasury spread inverted in 2022, and understanding what this meant gave informed investors a significant edge in portfolio positioning.

**2. The yield curve determines borrowing costs throughout the economy.** Mortgage rates, auto loan rates, corporate bond rates, and credit card rates are all influenced by the yield curve. When the curve is steep, banks profit handsomely by borrowing short and lending long. When it is flat or inverted, bank profitability shrinks, lending tightens, and the economy slows. Understanding this mechanism helps you understand economic cycles.

**3. The yield curve is the foundation of bond investing.** If you own bonds or bond funds (and you should for diversification), the yield curve determines your returns. Changes in the curve's shape affect different bond maturities differently. A long-term bond fund can gain 15% in a year when rates fall, or lose 15% when rates rise. This week's material, combined with Week 32 (duration and convexity), gives you the tools to manage this interest rate risk intelligently.

**4. The yield curve connects to everything in fixed income.** Weeks 33 (credit analysis), 34 (rate sensitivity), and 36 (income portfolio construction) all assume you understand yield curves. Credit spreads are measured relative to the Treasury yield curve. Rate sensitivity analysis uses yield curve movements as inputs. And constructing a bond portfolio requires understanding how different parts of the curve behave.

**5. Yield curves embody market expectations.** The curve reflects millions of investors' collective expectations about future interest rates, inflation, and economic growth. Reading the curve is like reading the market's mind. A steep curve says the market expects growth and possibly higher rates. A flat curve says the market expects slower growth. An inverted curve says the market expects economic contraction. This information is free and updated in real time.

---

### b) What You Need to Know

#### What Is a Yield Curve?

A yield curve is a graph that plots the yields (interest rates) of bonds with equal credit quality but different maturities. The most commonly referenced yield curve is the U.S. Treasury yield curve, which plots the yields on Treasury bills, notes, and bonds from 1 month to 30 years.

```
U.S. TREASURY YIELD CURVE (EXAMPLE - NORMAL SHAPE):

  Yield
  5.0% |                                              *
       |                                        *
  4.5% |                                  *
       |                            *
  4.0% |                      *
       |                *
  3.5% |          *
       |     *
  3.0% | *
       |
  2.5% |
       +---+---+---+---+---+---+---+---+---+---+---
       1m  3m  6m  1y  2y  3y  5y  7y  10y 20y 30y
                    Maturity

  KEY DATA POINTS (EXAMPLE):
  Maturity     Yield     Common Name
  ========     =====     ==============================
  1 month      2.80%     Treasury Bill (T-Bill)
  3 months     3.10%     Treasury Bill
  6 months     3.40%     Treasury Bill
  1 year       3.60%     Treasury Bill
  2 years      3.80%     Treasury Note (T-Note)
  5 years      4.10%     Treasury Note
  10 years     4.40%     Treasury Note (benchmark)
  20 years     4.65%     Treasury Bond (T-Bond)
  30 years     4.80%     Treasury Bond (long bond)
```

#### Types of Rates: Spot, Forward, and Par

Before analyzing yield curves, you must understand three different types of interest rates.

**Spot Rate (Zero-Coupon Rate):** The yield on a zero-coupon bond that pays no intermediate coupons. This is the "pure" rate for a specific maturity. If the 5-year spot rate is 4.2%, it means a dollar invested today in a 5-year zero-coupon bond will compound at 4.2% per year.

**Forward Rate:** The implied future interest rate derived from today's spot rates. The forward rate is the rate the market expects (or prices in) for a future period. The "2-year rate, 3 years from now" (written as 3f2 or f(3,5)) is derived from the 3-year and 5-year spot rates.

**Par Rate (Par Yield):** The coupon rate at which a coupon-paying bond would be priced exactly at par (100). This is what most people mean when they say "the yield curve," because most Treasury bonds pay coupons. The par yield curve is what you see quoted on financial news.

```
RELATIONSHIP BETWEEN RATE TYPES:

  Spot Rates (Zero-Coupon):        Forward Rates (Implied Future):
  1-year spot = 3.50%              Year 1 to Year 2 forward = 4.10%
  2-year spot = 3.80%              Year 2 to Year 3 forward = 4.40%
  3-year spot = 4.00%              Year 3 to Year 5 forward = 4.65%
  5-year spot = 4.20%

  HOW FORWARD RATES ARE DERIVED:

  The 2-year spot (3.80%) must equal the geometric average of:
    Year 1 spot (3.50%) and Year 1-to-2 forward rate

  (1 + 0.038)^2 = (1 + 0.035)^1 x (1 + f)^1
  1.0774 = 1.035 x (1 + f)
  f = 1.0774 / 1.035 - 1
  f = 4.10%

  The forward rate (4.10%) is HIGHER than either spot rate.
  This is because the yield curve is upward-sloping, implying
  that rates are expected to be higher in the future.

  DIAGRAM:

  Today          Year 1         Year 2         Year 3
    |              |              |              |
    |--- 3.50% --->|              |              |
    |              |--- 4.10% --->|              |
    |                             |--- 4.40% --->|
    |                                            |
    |------------ 3.80% -------->|               |
    |                                            |
    |------------------ 4.00% ----------------->|
    |                                            |
    2-year spot = geometric average of           |
    1-year spot + 1-year forward                 |
```

```
PAR RATE vs. SPOT RATE:

  When the yield curve is upward-sloping:
    Par Rate < Spot Rate (at the same maturity)

  When the yield curve is downward-sloping (inverted):
    Par Rate > Spot Rate (at the same maturity)

  When the yield curve is flat:
    Par Rate = Spot Rate

  Why? A coupon-paying bond receives intermediate cash flows
  that are discounted at lower spot rates (for earlier years).
  This pulls the par yield below the spot rate when the curve
  slopes up, and pushes it above when the curve slopes down.

  EXAMPLE (UPWARD-SLOPING CURVE):

  Maturity    Spot Rate    Par Rate    Difference
  ========    =========    ========    ==========
  1 year      3.50%        3.50%      0.00%  (same, no coupons)
  2 years     3.80%        3.79%      0.01%
  5 years     4.20%        4.16%      0.04%
  10 years    4.50%        4.40%      0.10%
  30 years    4.90%        4.72%      0.18%

  The difference grows with maturity because longer bonds
  have more intermediate cash flows affected by lower
  short-term spot rates.
```

#### Yield Curve Shapes

The yield curve takes three primary shapes, each conveying different information about the market's expectations.

**Normal (Upward-Sloping):**

```
NORMAL YIELD CURVE:

  Yield
  5.0% |                                       ___*___
       |                               ____*---
  4.0% |                      _____*---
       |              ____*---
  3.0% |      ____*---
       | __*--
  2.0% |
       +---+---+---+---+---+---+---+---+---
       1m  3m  1y  2y  3y  5y  10y 20y 30y

  WHAT IT MEANS:
  - Investors demand higher yields for longer maturities
    (compensation for more time = more risk)
  - The economy is expected to grow normally
  - Inflation expectations are stable or moderately rising
  - Banks can profit by borrowing short (low rates) and
    lending long (high rates) -> credit expansion

  HISTORICAL CONTEXT:
  - This is the "default" shape for most of history
  - Occurs during economic expansions and early recovery
  - Spread between 2y and 10y typically 100-200 bps
```

**Flat:**

```
FLAT YIELD CURVE:

  Yield
  5.0% |
       |
  4.0% | *----*----*----*----*----*----*----*----*
       |
  3.0% |
       |
  2.0% |
       +---+---+---+---+---+---+---+---+---
       1m  3m  1y  2y  3y  5y  10y 20y 30y

  WHAT IT MEANS:
  - The market is uncertain about future direction
  - Often a TRANSITION between normal and inverted
  - Short-term rates have risen (Fed tightening) but
    long-term rates have not followed
  - Banks have little incentive to lend (no term spread)
  - Economic growth is expected to slow

  HISTORICAL CONTEXT:
  - Often appears late in a Fed tightening cycle
  - Preceded several recessions as a transitional phase
  - 2y-10y spread near 0 bps (+/- 25 bps)
```

**Inverted (Downward-Sloping):**

```
INVERTED YIELD CURVE:

  Yield
  5.5% |
       |
  5.0% | *
       |   *
  4.5% |     *---*
       |            *---*
  4.0% |                  *---*
       |                        *---*---*
  3.5% |
       +---+---+---+---+---+---+---+---+---
       1m  3m  1y  2y  3y  5y  10y 20y 30y

  WHAT IT MEANS:
  - Short-term rates are HIGHER than long-term rates
  - The market expects the Fed to cut rates in the future
    (because rates need to come down to avoid/fight recession)
  - Economic contraction is expected
  - Banks lose money on new lending -> credit contraction
  - THE SINGLE BEST PREDICTOR OF RECESSION

  HISTORICAL CONTEXT:
  - Inverted before every U.S. recession since 1970
  - 2-year/10-year spread inverted in July 2022
  - Average lead time: 12-18 months before recession
  - No false signals in 50 years (though lead time varies)
```

```
OTHER SHAPES:

  HUMPED CURVE:              STEEP CURVE (Bear Steepener):
  Short rates low             Short rates very low
  Middle rates highest        Long rates very high
  Long rates moderate

  Yield                       Yield
  5% |       *****            6% |                        *
     |     **     **             |                    *
  4% |   **         **       5% |               *
     | **             **        |          *
  3% |*                 **   4% |     *
     |                    *     | *
  2% |                       3% |
     +---+---+---+---+---      +---+---+---+---+---
     1y  3y  5y  10y 30y       1y  3y  5y  10y 30y

  Humped: Transition shape,    Steep: Early recovery,
  often before inversion.      Fed holding rates low.
  Middle maturities are        Market expects significant
  most affected by policy.     future rate increases.
```

#### The Yield Curve as Recession Predictor

The yield curve's predictive power deserves special attention because it is one of the most reliable signals in all of finance.

```
HISTORICAL YIELD CURVE INVERSIONS AND RECESSIONS:

  Inversion Date   Recession Start   Lead Time   2y-10y Spread
  ==============   ===============   =========   =============
  Aug 1978         Jan 1980          17 months   -154 bps
  Sep 1980         Jul 1981          10 months   -216 bps
  Jan 1989         Jul 1990          18 months   -18 bps
  Feb 2000         Mar 2001          13 months   -52 bps
  Aug 2006         Dec 2007          16 months   -19 bps
  Jul 2022         ???               ???         -107 bps

  FALSE SIGNALS: 0 (every inversion led to recession)

  NOTE: Lead time varies from 10 to 18 months.
  The curve inverts long before the recession is obvious.
  By the time recession is officially declared (which happens
  AFTER the fact), the curve has usually already un-inverted
  and is steepening again.
```

**Why Does Inversion Predict Recession?**

The mechanism is not just correlation; there is causation:

```
THE INVERSION-RECESSION MECHANISM:

  Step 1: Fed raises short-term rates to fight inflation
          |
          v
  Step 2: Short rates rise above long rates (inversion)
          |
          v
  Step 3: Banks cannot profit from lending
          (borrow at 5%, lend at 4% = LOSS)
          |
          v
  Step 4: Banks tighten lending standards
          (fewer loans approved, higher standards)
          |
          v
  Step 5: Businesses cannot get financing
          Consumer credit tightens
          |
          v
  Step 6: Economic activity slows
          Hiring freezes, layoffs begin
          |
          v
  Step 7: RECESSION

  The curve does not just predict recession; it CAUSES it
  through the credit channel. When banks cannot make money
  lending, the economy's credit engine stalls.
```

```
USING THE YIELD CURVE FOR PORTFOLIO DECISIONS:

  Curve Shape         Action for Investors
  ================    ==========================================
  Normal (steep)      - Favor stocks over bonds
                      - Overweight banks and financials
                      - Hold shorter-duration bonds (less risk)
                      - Economy is healthy, risk-on

  Flattening          - Begin shifting to quality stocks
                      - Extend bond duration slightly
                      - Reduce cyclical stock exposure
                      - Watch for inversion signal

  Inverted            - Reduce stock allocation (slowly)
                      - Extend bond duration (lock in high rates)
                      - Overweight defensive sectors
                      - Build cash position
                      - Do NOT panic sell (recession may be
                        12+ months away)

  Steepening from     - The recession is either happening or
  inversion (bull     ending. Fed is cutting rates.
  steepener)          - Begin adding stock exposure
                      - Bonds are rallying, take some profits
                      - Transition from defensive to cyclical
```

#### Term Premium

The term premium is the extra yield investors demand for holding longer-maturity bonds instead of rolling over short-term bonds. It is compensation for the additional risks of locking up money for longer periods: inflation risk, interest rate risk, and uncertainty.

```
TERM PREMIUM CONCEPT:

  Long-term yield = Expected average of future short rates
                    + TERM PREMIUM

  Example:
  If the market expects the Fed funds rate to average 3.5%
  over the next 10 years, the 10-year yield might be 4.0%.

  10-year yield (4.0%) = Expected avg rate (3.5%) + Term premium (0.5%)

  The term premium is NOT directly observable. It must be
  estimated using models (Kim-Wright, ACM model, etc.)

  TERM PREMIUM OVER TIME:

  Period              Estimated Term Premium    Context
  ==================  ======================    ====================
  1980s-1990s         +200 to +300 bps          High inflation memory
  2000s               +100 to +150 bps          Moderate
  2010-2020           -50 to +50 bps            QE era, negative!
  2021-2024           +50 to +150 bps           Post-QE normalization

  NEGATIVE TERM PREMIUM?
  Yes, this happened during QE (quantitative easing).
  The Fed was buying long-term bonds, pushing prices up
  and yields down. This artificial demand compressed the
  term premium below zero. Investors were effectively
  PAYING for the privilege of holding long bonds, because
  the Fed was a guaranteed buyer.
```

```
WHY TERM PREMIUM MATTERS:

  If the 10-year yield is 4.5%, how much is:
    a) Expectations of future rates? (monetary policy path)
    b) Term premium? (compensation for risk)

  This decomposition matters because:

  If 10y yield is HIGH because of HIGH TERM PREMIUM:
    -> Bonds are offering good compensation for risk
    -> May be a good time to buy long bonds
    -> The "real" expected rate path may be lower than you think

  If 10y yield is HIGH because of HIGH EXPECTED RATES:
    -> The market expects the Fed to keep rates elevated
    -> Long bonds may still fall further if expectations rise
    -> The term premium may actually be low (poor compensation)

  VISUAL DECOMPOSITION:

  10-year yield: 4.50%
  |===============================================|
  |    Expected Rates: 3.80%     | Term Premium:  |
  |                              |    0.70%       |
  |===============================================|
```

#### Key Yield Curve Spreads

Several specific spreads on the yield curve are closely watched by investors and economists.

```
IMPORTANT YIELD CURVE SPREADS:

  Spread              Definition                 Significance
  ==================  ========================   =========================
  2y-10y              10y yield - 2y yield       Most watched recession
                                                 indicator. Inverts before
                                                 every recession.

  3m-10y              10y yield - 3m T-bill      Fed's preferred recession
                                                 indicator. More sensitive
                                                 to current Fed policy.

  Fed Funds - 10y     10y yield - Fed Funds      Measures full extent of
                                                 monetary policy impact
                                                 on long rates.

  2y-30y              30y yield - 2y yield       Term spread for long-
                                                 duration investors.

  5y-30y              30y yield - 5y yield       Long-end steepness.
                                                 Important for pension
                                                 funds and insurers.

  EXAMPLE READINGS:

  Spread    Normal Value   Current (example)   Signal
  ========  ============   =================   ===========
  2y-10y    +100-200 bps   -50 bps             Inverted!
  3m-10y    +100-250 bps   -120 bps            Inverted!
  2y-30y    +150-250 bps   +20 bps             Nearly flat

  When BOTH the 2y-10y AND 3m-10y are inverted,
  the recession signal is strongest.
```

#### Yield Curve Shifts and Portfolio Impact

The yield curve does not move uniformly. Different maturities can move by different amounts and even in different directions.

```
TYPES OF YIELD CURVE MOVEMENTS:

  1. PARALLEL SHIFT (all maturities move equally):

  Yield                          Yield
  5% |          ****             5.5%|          ****
     |     ****                      |     ****
  4% |****                       4.5%|****
     |                               |
  3% |                           3.5%|
     +---+---+---+---               +---+---+---+---
     2y  5y  10y 30y                2y  5y  10y 30y
       Before                         After (+50 bps)

  Impact: All bonds lose value proportional to their duration.
  Long bonds lose more than short bonds.

  2. STEEPENING (long rates rise more than short rates):

  Yield                          Yield
  4.5%|          ****            5.0%|               ****
     |     ****                      |         ****
  4% |****                       4.5%|    ****
     |                               |****
  3.5%|                          4.0%|
     +---+---+---+---               +---+---+---+---
     2y  5y  10y 30y                2y  5y  10y 30y
       Before                         After (steepening)

  Impact: Long bonds suffer more than short bonds.
  Strategy: Shorten duration. Overweight short maturities.

  3. FLATTENING (short rates rise more than long rates):

  Yield                          Yield
  4.5%|          ****            4.5%|****----****----****
     |     ****                      |
  4% |****                       4.0%|
     |                               |
  3.5%|                          3.5%|
     +---+---+---+---               +---+---+---+---
     2y  5y  10y 30y                2y  5y  10y 30y
       Before                         After (flattening)

  Impact: Short bonds lose more; long bonds may actually gain
  if long rates fell. Strategy: Extend duration if you expect
  flattening to continue.

  4. TWIST (short and long move in opposite directions):

  Yield                          Yield
  4.5%|          ****            5.0%|****          ****
     |     ****                      |    ****
  4% |****                       4.5%|        ****
     |                               |
  3.5%|                          4.0%|
     +---+---+---+---               +---+---+---+---
     2y  5y  10y 30y                2y  5y  10y 30y
       Before                         After (twist/butterfly)

  Impact: Short and long bonds lose; middle may be stable.
  This is the hardest movement to hedge against.
```

#### Reading the Current Yield Curve

```
STEP-BY-STEP YIELD CURVE ANALYSIS:

  1. OBSERVE THE SHAPE
     Is it normal, flat, inverted, or humped?
     -> This tells you the market's macro outlook.

  2. CHECK KEY SPREADS
     What is the 2y-10y spread? The 3m-10y spread?
     -> Negative = recession warning.
     -> Positive and steepening = expansion signal.

  3. COMPARE TO RECENT HISTORY
     Has the curve flattened, steepened, or shifted?
     -> Flattening from normal: late cycle, be cautious.
     -> Steepening from inversion: recovery may be starting.

  4. IDENTIFY THE DRIVER
     Are short rates moving (Fed policy) or long rates
     moving (inflation expectations, term premium)?
     -> Fed-driven flattening: short end rising.
     -> Market-driven steepening: long end rising.

  5. CONSIDER TERM PREMIUM
     Are long rates high because of expectations or risk?
     -> High term premium = bonds may be attractive.
     -> Low term premium = bonds may be expensive.

  WHERE TO FIND YIELD CURVE DATA:
  - Treasury.gov (official daily yields)
  - FRED (Federal Reserve Economic Data) - free, excellent
  - Your brokerage platform (most have yield curve tools)
  - Financial news sites (CNBC, Bloomberg, Reuters)
```

---

### c) Common Misconceptions

**Misconception 1: "An inverted yield curve means a recession is imminent."**

Inverted, yes, but imminent, no. The average lead time between inversion and recession onset is 12 to 18 months. In some cases it has been as long as 24 months. Many investors see the inversion, panic, sell everything, and then watch the market rally for another year before the recession arrives. The yield curve is an early warning system, not an immediate alarm. Use it to gradually adjust your portfolio over months, not to make dramatic changes overnight.

**Misconception 2: "The yield curve reflects what will happen to interest rates."**

The yield curve reflects the market's expectations of future rates plus a term premium. Expectations can be wrong. In the 2010s, the yield curve consistently implied that rates would rise, but the Fed kept them near zero for years. Forward rates are not forecasts; they are prices that reflect the current supply and demand for bonds at different maturities. They are useful indicators but not prophecies.

**Misconception 3: "A steeper yield curve is always better for the economy."**

A steep curve is generally positive because it encourages bank lending and signals growth expectations. But an excessively steep curve, especially one driven by surging long-term rates, can indicate inflation fears and may actually tighten financial conditions. A 30-year Treasury yield at 6% means mortgage rates at 7-8%, which slows housing and consumer spending. Context matters more than shape alone.

**Misconception 4: "I should buy long-term bonds when the yield curve inverts."**

This is partially correct but the timing matters. The curve often inverts because the Fed has raised short-term rates aggressively. Long-term rates may not have peaked yet. The optimal time to buy long bonds is typically when the Fed signals it will start cutting rates, which is usually after the inversion and closer to the recession. Buying too early means you may endure further price declines before the eventual rally.

**Misconception 5: "The yield curve is only relevant for bond investors."**

The yield curve affects every asset class. Stock valuations are influenced by the discount rate, which comes from the yield curve. Real estate prices are driven by mortgage rates, which track the long end of the curve. Corporate profitability depends on borrowing costs. Bank earnings are directly tied to the curve's steepness. Even commodity prices are influenced by the rate environment. Every investor should monitor the yield curve.

**Misconception 6: "Spot rates, forward rates, and par rates are interchangeable."**

They are mathematically related but not the same. Using par rates when you should use spot rates for discounting cash flows leads to pricing errors. Zero-coupon bonds should be priced with spot rates. Coupon bonds can be priced either with spot rates (discounting each cash flow separately) or with par rates (single discount rate). Forward rates are useful for valuing forward-starting instruments and for inferring market expectations. Using the wrong rate type is a common source of error in bond analytics.

---

### d) Q&A

**Q: Where can I see the current yield curve?**

A: The U.S. Treasury publishes daily yield data at treasury.gov/resource-center/data-chart-center. The Federal Reserve's FRED database (fred.stlouisfed.org) has excellent yield curve tools and historical data. Most brokerage platforms also display the current yield curve. For real-time data during market hours, financial news sites like CNBC and Bloomberg provide up-to-the-minute yield information. The "Daily Treasury Par Yield Curve Rates" page on treasury.gov is the official source.

**Q: How do I calculate forward rates from spot rates?**

A: The general formula is: (1 + S_n)^n = (1 + S_m)^m x (1 + f)^(n-m), where S_n is the n-year spot rate, S_m is the m-year spot rate, and f is the forward rate from year m to year n. Solve for f. For example, if the 2-year spot is 3.80% and the 3-year spot is 4.00%: (1.04)^3 = (1.038)^2 x (1 + f). So 1.12486 = 1.07744 x (1 + f). Therefore f = 4.40%. This says the market prices the 1-year rate, 2 years from now, at 4.40%.

**Q: The 2y-10y spread and the 3m-10y spread sometimes give different signals. Which should I follow?**

A: Both are useful but measure different things. The 2y-10y spread reflects market expectations of medium-term rate policy. The 3m-10y spread is more tied to current Fed policy (the 3-month T-bill rate tracks the Fed Funds rate closely). The Fed's own research (using the "near-term forward spread") gives more weight to the 3m-10y spread. In practice, when both are inverted, the signal is strongest. When they diverge, the 3m-10y spread may be more relevant for near-term recession risk.

**Q: Can the yield curve be manipulated by the Fed?**

A: The Fed directly controls the Federal Funds rate, which is a very short-term rate. It also influences the yield curve through quantitative easing (QE) and quantitative tightening (QT). During QE, the Fed buys long-term bonds, pushing long rates down and flattening or even inverting the curve artificially. During QT, the Fed sells long-term bonds, pushing long rates up and steepening the curve. The question of whether the inverted curve in 2022-2023 was a true recession signal or partly an artifact of previous QE is actively debated by economists.

**Q: What is the "uninversion" and why does it matter?**

A: Uninversion is when the yield curve returns from inverted to normal. Paradoxically, the uninversion often occurs right as the recession begins or shortly before. This is because the Fed starts cutting rates (pulling short rates down) in response to economic weakness, causing the short end to drop faster than the long end. So the curve steepens even as the economy deteriorates. Historically, the uninversion has been as important a signal as the initial inversion. It often marks the transition from "recession is coming" to "recession is here."

**Q: How should I position my bond portfolio based on the yield curve?**

A: The basic framework is: in a steepening environment, shorten duration (overweight shorter maturities) because long rates are rising. In a flattening environment, extend duration moderately because long rates are falling relative to short rates. When the curve is inverted and the Fed is expected to cut, lock in high short-term rates with CDs or T-bills, and begin extending duration to capture price gains when long rates eventually fall. We will cover these strategies in more detail in Week 34 (rate sensitivity) and Week 36 (income portfolio).

**Q: What is the "term structure of interest rates" and is it the same as the yield curve?**

A: They are closely related but technically different. The term structure of interest rates refers to the theoretical relationship between interest rates and time to maturity, usually expressed as spot rates. The yield curve, in common usage, refers to the par yield curve plotted from observed market prices of coupon-paying bonds. For practical purposes, investors use the terms interchangeably, but in academic and professional contexts, "term structure" specifically means the spot rate curve.

---

## YouTube Script

[VISUAL: Animated intro with show logo. Text: "Week 31: Yield Curves - Level 3: Advanced"]

**Horace:** Welcome back, everyone. This week we are shifting gears from options to bonds. Specifically, we are going to learn about the yield curve, which I consider the single most important indicator in all of financial markets.

**Stella:** That is a bold claim. More important than stock market earnings, GDP, or employment data?

**Horace:** I stand by it. The yield curve has predicted every U.S. recession in the past 50 years. No other indicator has that track record. Zero false signals. It drives trillions of dollars in mortgage rates, corporate borrowing costs, and bank profitability. And it is free to read, updated every day.

[VISUAL: A newspaper-style headline montage showing: "Yield Curve Inverts" (2006), followed by "Recession Declared" (2008). Then "Yield Curve Inverts" (2019), followed by "Recession Declared" (2020). Then "Yield Curve Inverts" (2022) with a question mark.]

**Stella:** OK, you have my attention. Let us start from the beginning. What exactly is a yield curve?

**Horace:** A yield curve is simply a graph. On the x-axis, you have maturity, from 1 month out to 30 years. On the y-axis, you have the yield, the interest rate. You plot the yield of government bonds at each maturity and connect the dots. That line is the yield curve.

[ANIMATION: Reference animation/week31_yield_curve_build.py - Starting with empty axes labeled "Maturity" (x-axis) and "Yield" (y-axis). Treasury bond data points appear one by one: 1-month bill at 2.8%, 3-month at 3.1%, 6-month at 3.4%, 1-year at 3.6%, 2-year at 3.8%, 5-year at 4.1%, 10-year at 4.4%, 30-year at 4.8%. As each point appears, a smooth curve forms connecting them. The final shape is a typical upward-sloping normal yield curve.]

**Stella:** So it slopes upward. Short-term rates are lower and long-term rates are higher. Why?

**Horace:** Think of it like this. If I asked you to lend me money for one year, you might ask for 3.5% interest. But if I asked you to lend me money for 30 years, you would want much more, maybe 5%. Why? Because in 30 years, a lot can go wrong. Inflation could spike, I might not pay you back, or you might need the money for something else. That extra yield for taking on more time is called the term premium.

**Stella:** So longer maturity equals more risk equals more yield.

**Horace:** Exactly. Under normal conditions, the yield curve slopes upward. This is called a normal yield curve. Investors are being compensated for the additional risk of lending money for longer periods.

**Stella:** But sometimes the curve has different shapes, right?

**Horace:** There are three main shapes. Normal, which is upward-sloping and signals a healthy economy. Flat, where short and long rates are about equal, which signals uncertainty and transition. And inverted, where short rates are actually higher than long rates, which is the recession warning.

[VISUAL: Three yield curves displayed side by side. Left: "Normal" with a clear upward slope labeled "Healthy Economy." Center: "Flat" with a horizontal line labeled "Transition / Uncertainty." Right: "Inverted" with a downward slope labeled "RECESSION WARNING"]

**Stella:** Let us talk about the inverted curve because that is the famous one. How does it predict recessions?

**Horace:** The mechanism is surprisingly straightforward. It starts with the Federal Reserve raising short-term interest rates to fight inflation. When the Fed pushes short rates high enough, they rise above long rates, and the curve inverts. Now think about what this means for banks. Banks make money by borrowing short and lending long. They take in deposits at short-term rates and make loans at long-term rates. The difference is their profit margin.

**Stella:** And when the curve inverts, that profit margin disappears.

**Horace:** Or goes negative. If a bank borrows at 5% and can only lend at 4%, it loses money on every new loan. So what do banks do? They stop lending. They tighten credit standards. Fewer loans get approved.

[ANIMATION: Reference animation/week31_bank_mechanism.py - A visual chain reaction. Step 1: A "Fed" building raising a lever labeled "Short-term rate" to 5%. Step 2: A curve graphic showing the short end above the long end. Step 3: A bank building with an equation "Borrow at 5% - Lend at 4% = -1% LOSS" flashing red. Step 4: A "LOANS" spigot being turned off. Step 5: Business icons and consumer icons showing "Denied" stamps on loan applications. Step 6: An economic activity graph declining.]

**Horace:** When credit dries up, businesses cannot get financing. Consumers cannot get loans. Economic activity slows. Hiring freezes. Eventually, layoffs begin. And that is a recession. The yield curve does not just predict it; it is part of the causal mechanism.

**Stella:** And this has happened before every recession since 1970?

**Horace:** Every single one. The 2-year/10-year Treasury spread inverted before the recessions of 1980, 1981, 1990, 2001, 2008, and 2020. Average lead time is 12 to 18 months. And there have been zero false signals. No other indicator comes close to this track record.

[VISUAL: Timeline spanning 1978 to 2024. Each inversion event is marked with an inverted triangle, and each subsequent recession is marked with a gray shaded bar. Arrows connect each inversion to its recession with the lead time in months: 17, 10, 18, 13, 16, etc.]

**Stella:** But you said 12 to 18 months lead time. So when the curve inverts, you should not panic immediately.

**Horace:** This is crucial. The inversion is an early warning, not an immediate alarm. Many investors see the inversion, sell everything, and then watch the stock market rally for another 12 months before the recession arrives. The correct response is to gradually adjust your portfolio over months: shifting to higher quality stocks, extending bond duration to lock in high rates, building a cash position, and reducing cyclical exposure. Do not panic. Prepare.

**Stella:** Now I want to understand the different types of rates because the reading distinguished between spot rates, forward rates, and par rates.

**Horace:** Great question. These three are related but different. The spot rate, also called the zero-coupon rate, is the yield on a bond that pays no coupons and just returns your money at maturity. It is the "pure" rate for a specific maturity. The 5-year spot rate tells you exactly what return you get for locking up money for exactly 5 years.

**Stella:** And a forward rate?

**Horace:** A forward rate is the implied future interest rate derived from today's spot rates. Here is the key idea. If the 1-year spot rate is 3.5% and the 2-year spot rate is 3.8%, we can calculate what the market implies the 1-year rate will be one year from now.

[VISUAL: A timeline diagram. "Today" at the left. Two paths: Path 1 shows "Invest for 2 years at 3.80% spot rate." Path 2 shows "Invest for 1 year at 3.50%, then reinvest for 1 year at ??? forward rate." Both paths end at the same point. The forward rate of 4.10% is revealed as the rate that makes both paths equivalent.]

**Horace:** The math says the implied forward rate is about 4.10%. This means that for both investment paths to give you the same result, the 1-year rate next year would need to be 4.10%. This is what the market is pricing in.

**Stella:** Is that what will actually happen?

**Horace:** Not necessarily. Forward rates are market-implied expectations, not forecasts. They can be wrong, and often are. But they tell you what the market is pricing, which is valuable information even if it turns out to be incorrect.

**Stella:** What about par rates?

**Horace:** Par rates are the coupon rates at which a coupon-paying bond would trade exactly at par, at $100. This is what most people see when they look at yield curves on financial news. When CNBC shows the "10-year Treasury yield at 4.4%," that is essentially the par rate. For an upward-sloping curve, par rates are slightly below spot rates because the intermediate coupon payments are discounted at lower short-term rates.

**Stella:** Let us talk about the term premium because this seems like an underappreciated concept.

**Horace:** The term premium is the extra yield investors demand for bearing the risk of holding longer-maturity bonds. The long-term yield equals the expected average of future short-term rates plus the term premium. If the market expects rates to average 3.5% over the next 10 years, and the 10-year yield is 4.5%, then the term premium is roughly 1%.

**Stella:** So not all of the yield is about rate expectations?

**Horace:** Correct. And this distinction matters enormously. During the quantitative easing era, the Fed bought trillions of dollars in long-term bonds. This compressed the term premium, in some estimates pushing it below zero. Investors were actually paying for the privilege of holding long bonds because the Fed was a guaranteed buyer. When QE ended and the Fed started selling bonds (quantitative tightening), the term premium expanded, pushing long rates up even if rate expectations did not change.

[VISUAL: A bar decomposition of the 10-year yield. The bar is split into two segments: "Expected Average Future Rate: 3.80%" (blue) and "Term Premium: 0.70%" (orange). Total: 4.50%. Below, a second bar shows the QE era: "Expected Rate: 3.00%" and "Term Premium: -0.30%". Total: 2.70%. Annotation: "During QE, the term premium was NEGATIVE"]

**Stella:** That explains why long-term rates can move without the Fed changing policy.

**Horace:** Exactly. The long end of the curve is driven by two independent forces: expectations of future Fed policy and the term premium. This is why the 10-year yield can rise even when the Fed is cutting rates, if the term premium is expanding. And it is why the 10-year can fall even when the Fed is raising rates, if the term premium is compressing.

**Stella:** How should investors actually use the yield curve in their portfolio decisions?

**Horace:** I have a simple framework. When the curve is normal and steep, favor stocks over bonds. Banks and financials do well. Keep bond holdings short-duration. When the curve is flattening, start shifting to higher quality. Watch for the inversion signal. When the curve is inverted, begin gradually reducing stock exposure, extend bond duration to lock in high rates, and build cash.

[VISUAL: A decision matrix. Three columns for "Normal/Steep", "Flat/Flattening", "Inverted". Rows for different asset classes: Stocks, Bonds, Cash, Sectors. Each cell has a recommendation with an up/down/neutral arrow.]

**Horace:** And here is the often-overlooked signal: when the curve un-inverts, meaning it goes from inverted back to normal, that is when the recession is typically imminent or already starting. The un-inversion happens because the Fed starts cutting rates, pulling the short end down. So paradoxically, the curve normalizing can be the most bearish signal of all.

**Stella:** That is counterintuitive. The curve going back to normal is actually worse than being inverted?

**Horace:** For the near-term economic outlook, yes. The inversion says "recession is coming in 12 to 18 months." The un-inversion says "recession may be starting now." Of course, it also means that once you get through the recession, conditions are set for recovery. The curve steepening from inversion is eventually very bullish, just not immediately.

**Stella:** Let me ask about yield curve movements. How does the curve actually shift?

**Horace:** There are four main types of movements. A parallel shift is when all maturities move by the same amount, say everything goes up 50 basis points. A steepening is when long rates rise more than short rates, making the curve more upward-sloping. A flattening is when short rates rise more than long rates, making the curve flatter. And a twist is when short and long rates move in opposite directions.

[ANIMATION: Reference animation/week31_curve_movements.py - Four sequential animations showing each type of yield curve movement. 1) Parallel shift: entire curve lifts up uniformly. 2) Steepening: the right end of the curve lifts while the left stays put. 3) Flattening: the left end lifts while the right stays put. 4) Twist: left end lifts and right end drops simultaneously. Each animation shows a bond portfolio value indicator changing to show the impact.]

**Stella:** And different movements affect different parts of a bond portfolio differently?

**Horace:** Exactly. A parallel shift hits long bonds hardest because they have the most duration. A steepening specifically hurts the long end. A flattening hurts the short end but may benefit the long end. We will quantify all of this precisely next week when we cover duration and convexity.

**Stella:** How do the key yield curve spreads work? I have heard people talk about the "2s-10s spread."

**Horace:** The 2s-10s spread is the 10-year yield minus the 2-year yield. When it is positive, the curve is normal. When it is negative, the curve is inverted. It normally ranges from plus 100 to plus 200 basis points. The other important spread is the 3-month-to-10-year spread, which the Fed itself uses as its preferred recession indicator because the 3-month rate tracks the Fed Funds rate very closely.

[VISUAL: A live-style chart showing the 2y-10y spread over time from 2000 to present. The zero line is highlighted. Periods where the spread dips below zero (2000, 2006, 2019, 2022) are shaded, with subsequent recession periods marked in gray.]

**Stella:** Before we wrap up, where should people go to look at the yield curve?

**Horace:** The best free resource is FRED, the Federal Reserve Economic Data website. It has the current yield curve, historical data, and tools to plot any spread over time. The U.S. Treasury website publishes daily par yield curve rates. And most brokerage platforms have yield curve tools built in. I recommend checking the yield curve at least weekly, or whenever you hear news about Fed policy changes.

**Stella:** This has been fascinating. I feel like I understand something that most retail investors completely ignore.

**Horace:** And that is your edge. When you can read the yield curve, you have access to the collective wisdom of the bond market, which is much larger and often smarter than the stock market. Next week, we build on this foundation with duration and convexity, which will give you the mathematical tools to measure exactly how much your bond portfolio will change when the yield curve moves.

**Stella:** Thanks, everyone. See you next week for duration and convexity.

[VISUAL: End screen with show logo, "Week 31: Yield Curves" summary, and preview of Week 32: Duration and Convexity]

**Horace:** See you then.
