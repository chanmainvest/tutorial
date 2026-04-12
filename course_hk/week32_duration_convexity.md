<!-- 此檔案需要翻譯為香港繁體中文 -->
<!-- This file needs translation to HK Traditional Chinese -->

# Week 32: Duration and Convexity - Measuring Bond Price Sensitivity

## Reading Section

### a) Why This Is Important

Last week you learned to read the yield curve and interpret its shape. This week you will learn to quantify exactly how much your bond portfolio will change in value when interest rates move. Duration and convexity are the tools that make this possible, and they are non-negotiable knowledge for anyone who owns bonds or bond funds.

**Why duration and convexity matter:**

**1. Interest rate risk is the dominant risk in bond investing.** If you own a 10-year Treasury bond and interest rates rise by 1%, your bond loses approximately 8-9% of its value. On a $100,000 position, that is an $8,000-$9,000 loss. Without understanding duration, you have no way to predict, measure, or manage this risk. Duration quantifies it precisely.

**2. Duration determines your portfolio's vulnerability to rate changes.** A portfolio with a duration of 2 years will lose about 2% if rates rise by 1%. A portfolio with a duration of 15 years will lose about 15%. The difference between these two portfolios is enormous, and yet many investors own bond funds without knowing their duration. This is like driving at an unknown speed on a highway. You need the speedometer.

**3. Convexity makes duration more accurate.** Duration is a first-order approximation. It works well for small rate changes but becomes increasingly inaccurate for large moves. Convexity is the correction factor. For a 2% rate increase, duration alone might predict a 16% loss, but convexity adjusts this to 14.5%. That 1.5% difference on a $500,000 bond portfolio is $7,500. Convexity matters.

**4. Negative convexity creates hidden risks.** Mortgage-backed securities and callable bonds have negative convexity, meaning they behave worse than duration suggests in extreme rate environments. Many investors in 2022 discovered this the hard way when their MBS holdings lost far more than their stated duration implied. Understanding negative convexity is essential for avoiding these surprises.

**5. Immunization uses duration to eliminate interest rate risk.** Pension funds, insurance companies, and any investor with a specific future liability can use duration matching to ensure that their assets will exactly meet their obligations regardless of what interest rates do. This concept, while more applicable to institutions, illuminates how duration works and why it is so fundamental to professional bond management.

**6. Duration connects to everything in fixed income.** Weeks 34 (rate sensitivity), 36 (income portfolio), and all credit analysis depend on understanding duration. When a bond fund says "modified duration: 6.2 years," you need to know exactly what that means for your portfolio. This week gives you that knowledge.

---

### b) What You Need to Know

#### The Price-Yield Relationship

Before understanding duration, you must understand the fundamental relationship between bond prices and yields.

```
THE INVERSE RELATIONSHIP:

  When interest rates GO UP, bond prices GO DOWN.
  When interest rates GO DOWN, bond prices GO UP.

  WHY?

  You own a bond paying 4% coupon. New bonds now pay 5%.
  Your 4% bond is less attractive -> its price falls.

  You own a bond paying 4% coupon. New bonds now pay 3%.
  Your 4% bond is more attractive -> its price rises.

  PRICE-YIELD CURVE:

  Price
  $130 |*
       | *
  $120 |  *
       |   **
  $110 |     **
       |       **
  $100 |         ***
       |            ***
   $90 |               ****
       |                   *****
   $80 |                        ********
       +----+----+----+----+----+----+----+----
       1%   2%   3%   4%   5%   6%   7%   8%
                     Yield (YTM)

  KEY OBSERVATION:
  The curve is CONVEX (bowed toward the origin).
  - A 1% rate DROP causes a LARGER price gain
    than a 1% rate RISE causes a price loss.
  - This asymmetry is convexity, and it benefits bondholders.
```

#### Macaulay Duration

Macaulay duration is the weighted average time until you receive all the bond's cash flows, where the weights are the present values of each cash flow.

```
MACAULAY DURATION CALCULATION:

  Bond: 5% coupon, 3-year maturity, YTM = 4%, par = $1,000

  Year    Cash Flow    PV Factor    PV of CF     Weight     Year x Weight
  ====    =========    =========    ========     ======     =============
  1       $50          0.9615       $48.08       0.0462     0.0462
  2       $50          0.9246       $46.23       0.0445     0.0889
  3       $1,050       0.8890       $933.45      0.8976     2.6928
  ====    =========    =========    ========     ======     =============
  Total                             $1,040.40*   1.0000     2.8279

  * Bond trades at premium because coupon (5%) > yield (4%)

  Macaulay Duration = 2.83 years

  INTERPRETATION:
  Although this bond has 3 years to maturity, the weighted
  average time to receive cash flows is 2.83 years.
  The duration is shorter than maturity because you receive
  coupon payments before maturity, pulling the average forward.

  SPECIAL CASE: Zero-Coupon Bond
  A 3-year zero-coupon bond has Macaulay duration = 3.00 years.
  Duration equals maturity because there is only one cash flow,
  at maturity. No earlier coupons to pull the average forward.
```

```
FACTORS AFFECTING MACAULAY DURATION:

  Factor              Effect on Duration     Explanation
  ==================  ====================   =======================
  Higher coupon       SHORTER duration        More cash flow early
  Lower coupon        LONGER duration         Less cash flow early
  Longer maturity     LONGER duration         Cash flows further out
  Shorter maturity    SHORTER duration        Cash flows closer
  Higher yield        SHORTER duration        Distant CFs worth less
  Lower yield         LONGER duration         Distant CFs worth more

  DIAGRAM - HOW COUPON AFFECTS DURATION:

  High Coupon Bond (8%):            Low Coupon Bond (2%):
  More weight on early CFs          Most weight on final CF

  Weight                            Weight
  |  ##                             |
  |  ## ##                          |
  |  ## ## ##                       |  ##
  |  ## ## ## ####                  |  ## ##
  |  ## ## ## ####                  |  ## ## ## ## ########
  +--+--+--+--+--+--               +--+--+--+--+--+--
   1  2  3  4  5 Mat                1  2  3  4  5 Mat

  Duration ~3.8 years               Duration ~4.7 years

  Coupon payments "pull" the duration toward the present.
  Higher coupons pull harder, resulting in shorter duration.
```

#### Modified Duration

Modified duration converts Macaulay duration into a direct measure of price sensitivity. It answers the question: "How much will the bond's price change for a 1% change in yield?"

```
MODIFIED DURATION FORMULA:

  Modified Duration = Macaulay Duration / (1 + YTM/n)

  Where n = number of coupon payments per year
  (n=2 for semiannual, n=1 for annual)

  Example (semiannual coupons):
  Macaulay Duration = 2.83 years
  YTM = 4% (semiannual = 2% per period)

  Modified Duration = 2.83 / (1 + 0.04/2)
                    = 2.83 / 1.02
                    = 2.77 years

  PRICE SENSITIVITY APPROXIMATION:

  % Price Change = -Modified Duration x Change in Yield (in %)

  If yields rise 1%:
    % Price Change = -2.77 x 1% = -2.77%
    On a $100,000 position: LOSS of $2,770

  If yields fall 1%:
    % Price Change = -2.77 x (-1%) = +2.77%
    On a $100,000 position: GAIN of $2,770
```

```
MODIFIED DURATION BY BOND TYPE:

  Bond Type                     Typical Duration   Price Impact per 1%
  ============================  ================   ===================
  Money Market / T-Bills        0 - 0.25 years     0 - 0.25%
  Short-Term Bond Fund          1 - 3 years        1 - 3%
  Intermediate Bond Fund        3 - 7 years        3 - 7%
  Aggregate Bond Index (AGG)    6 - 7 years        6 - 7%
  Long-Term Bond Fund           10 - 18 years      10 - 18%
  30-Year Treasury Bond         18 - 22 years      18 - 22%
  Zero-Coupon 30-Year           ~30 years           ~30%

  VISUAL COMPARISON:

  Rate rises 1%, portfolio losses:

  Money Market    |#                              0.1%
  Short-Term      |###                            2%
  Intermediate    |######                         5%
  Aggregate       |########                       6.5%
  Long-Term       |################               14%
  30-Year Zero    |################################ 28%
                   0%    5%    10%    15%    20%   25%   30%
```

#### Effective Duration

For bonds with embedded options (callable bonds, mortgage-backed securities, putable bonds), modified duration does not work because the cash flows change when rates change. For these bonds, we use **effective duration**, which measures price sensitivity empirically.

```
EFFECTIVE DURATION:

  Effective Duration = (P_down - P_up) / (2 x P_0 x Delta_y)

  Where:
    P_down = Bond price when yield decreases by Delta_y
    P_up   = Bond price when yield increases by Delta_y
    P_0    = Current bond price
    Delta_y = Yield change used (typically 0.25% or 0.50%)

  EXAMPLE:

  Callable bond, current price = $102.00, yield = 5.00%

  If yield drops to 4.75%: Price = $103.20
  If yield rises to 5.25%: Price = $100.50

  Effective Duration = ($103.20 - $100.50) / (2 x $102.00 x 0.0025)
                     = $2.70 / $0.51
                     = 5.29 years

  COMPARE: Modified duration of the same bond might be 7.2 years.
  The difference (7.2 vs 5.29) is because when rates fall, the
  issuer is likely to CALL the bond (buy it back), capping the
  upside. This call risk shortens the effective duration.

  WHEN TO USE WHICH:

  Bond Type                 Use This Duration
  ========================  ==========================
  Non-callable Treasury     Modified Duration
  Non-callable Corporate    Modified Duration
  Callable Corporate Bond   Effective Duration
  Mortgage-Backed Security  Effective Duration
  Putable Bond              Effective Duration
  Floating Rate Note        Effective Duration
```

#### PVBP (Price Value of a Basis Point)

PVBP, also called DV01 (Dollar Value of 01), measures the dollar change in bond price for a 1 basis point (0.01%) change in yield. It translates duration into actual dollar amounts.

```
PVBP / DV01 CALCULATION:

  PVBP = Modified Duration x Price x 0.0001

  Example:
  Bond price = $98.50, Modified Duration = 7.5 years

  PVBP = 7.5 x $98.50 x 0.0001 = $0.0739 per $100 face value

  For $100,000 face value:
  PVBP = $0.0739 x 1,000 = $73.88

  Meaning: A 1 basis point rise in rates causes a $73.88 loss.
           A 10 bp rise causes a ~$739 loss.
           A 100 bp (1%) rise causes a ~$7,388 loss.

  PVBP BY MATURITY ($100,000 FACE VALUE):

  Maturity    Duration    PVBP (per bp)    Loss per 1%
  ========    ========    =============    ===========
  2-year      1.9         $19              $1,900
  5-year      4.5         $45              $4,500
  10-year     8.2         $82              $8,200
  20-year     14.5        $145             $14,500
  30-year     20.0        $200             $20,000

  A 30-YEAR BOND LOSES $200 FOR EVERY SINGLE BASIS POINT
  MOVE IN RATES. For a $1,000,000 position, that is $2,000/bp.

  This is why pension funds and insurance companies obsess
  over managing duration. Their bond portfolios are in the
  billions, and even a few basis points matter enormously.
```

```
PORTFOLIO PVBP:

  Portfolio PVBP = Sum of all position PVBPs

  Example Portfolio ($500,000 total):
  Position              Amount     Duration   PVBP
  ====================  =========  ========   =========
  2-Year Treasury       $150,000   1.9        $28.50
  5-Year Treasury       $200,000   4.5        $90.00
  10-Year Treasury      $100,000   8.2        $82.00
  Cash                  $50,000    0.0        $0.00
  ======================================================
  TOTAL                 $500,000   4.02*      $200.50

  * Portfolio Duration = Total PVBP / (Total Value x 0.0001)
    = $200.50 / ($500,000 x 0.0001) = 4.01 years

  If rates rise 50 bps uniformly:
    Portfolio loss = $200.50 x 50 = $10,025 (about 2.0%)

  If rates rise 100 bps (1%):
    Portfolio loss = $200.50 x 100 = $20,050 (about 4.0%)
```

#### Convexity

Duration is a linear approximation. It works well for small rate changes but becomes increasingly inaccurate for larger moves. Convexity is the correction factor that accounts for the curvature of the price-yield relationship.

```
WHY DURATION ALONE IS NOT ENOUGH:

  For a bond with Duration = 10 and Price = $100:

  Yield Change   Duration Estimate    Actual Price    Error
  ============   =================    ============    =====
  -0.25%         +$2.50 ($102.50)     $102.53         $0.03
  -0.50%         +$5.00 ($105.00)     $105.13         $0.13
  -1.00%         +$10.00 ($110.00)    $110.52         $0.52
  -2.00%         +$20.00 ($120.00)    $122.14         $2.14
  +0.25%         -$2.50 ($97.50)      $97.47          $0.03
  +0.50%         -$5.00 ($95.00)      $94.87          $0.13
  +1.00%         -$10.00 ($90.00)     $89.73          $0.27
  +2.00%         -$20.00 ($80.00)     $80.53          $0.53

  Duration OVERESTIMATES losses and UNDERESTIMATES gains.
  The error grows with larger rate changes.
  Convexity corrects this error.

  GRAPHICAL VIEW:

  Price
  $130 |*
       | *
  $120 |  *                Actual price-yield curve (curved)
       |   **              ---
  $110 |     **           Duration estimate (straight line)
       |       **
  $100 |     ----***-----------
       |   --        ****
   $90 | --              ****
       |--                   *****
   $80 |                          ********
       +----+----+----+----+----+----+----
       1%   2%   3%   4%   5%   6%   7%
                     Yield

  The gap between the curved line and the straight line
  is the convexity effect. It is always in the bondholder's
  favor for normal (positive convexity) bonds.
```

```
CONVEXITY-ADJUSTED PRICE CHANGE:

  % Price Change = -Duration x Delta_y + (1/2) x Convexity x (Delta_y)^2

  Where Delta_y is the yield change in decimal form

  Example:
  Duration = 10 years, Convexity = 120, Price = $100

  Yield rises 1% (Delta_y = 0.01):
    Duration effect:   -10 x 0.01 = -0.10 = -10.00%
    Convexity effect:  0.5 x 120 x (0.01)^2 = +0.006 = +0.60%
    Total: -10.00% + 0.60% = -9.40%
    Price: $100 x (1 - 0.094) = $90.60

  Yield falls 1% (Delta_y = -0.01):
    Duration effect:   -10 x (-0.01) = +0.10 = +10.00%
    Convexity effect:  0.5 x 120 x (-0.01)^2 = +0.006 = +0.60%
    Total: +10.00% + 0.60% = +10.60%
    Price: $100 x (1 + 0.106) = $110.60

  NOTICE: The convexity adjustment is ALWAYS POSITIVE.
  It adds to gains (when rates fall) and reduces losses (when rates rise).
  This is positive convexity, and it is favorable for bondholders.

  COMPARISON:
  Rate Change    Duration Only    With Convexity    Difference
  ===========    =============    ==============    ==========
  -2%            +20.00%          +22.40%           +2.40%
  -1%            +10.00%          +10.60%           +0.60%
  -0.5%          +5.00%           +5.15%            +0.15%
  +0.5%          -5.00%           -4.85%            +0.15%
  +1%            -10.00%          -9.40%            +0.60%
  +2%            -20.00%          -17.60%           +2.40%
```

#### Negative Convexity

Some bonds have negative convexity, meaning the price-yield curve bends the wrong way. Instead of gaining more on rate drops than they lose on rate rises, these bonds gain less and lose more. The primary culprits are callable bonds and mortgage-backed securities (MBS).

```
NEGATIVE CONVEXITY:

  WHY IT OCCURS (CALLABLE BONDS):

  When rates fall, the issuer can CALL the bond (buy it back at par).
  This caps the bond's upside. As rates approach the call threshold,
  the bond's price stops rising and flattens near the call price.

  Price
  $115 |          Non-callable bond (positive convexity)
       |        **
  $110 |      ** .....
       |    **  .     ..... Callable bond (negative convexity)
  $105 |  ** ..
       | **.
  $100 |*.                           CALL PRICE (cap)
       |                        -.-.-.-.-.-.-.-.-.-.-
   $95 |                    ..
       |                ..
   $90 |            ..                Both bonds similar
       |        ..                    when rates rise
   $85 |    ..
       +----+----+----+----+----+----+----+----
       2%   3%   4%   5%   6%   7%   8%   9%

  Below ~4% yield: Callable bond's price is CAPPED near $105
  because the issuer will likely call it. The non-callable bond
  continues to rise.

  This "capping" creates NEGATIVE CONVEXITY in the low-rate region.
```

```
NEGATIVE CONVEXITY IN MORTGAGE-BACKED SECURITIES:

  MBS have the worst negative convexity because homeowners
  can refinance (prepay their mortgage) at any time.

  When rates fall:
  - Homeowners refinance -> prepayments accelerate
  - You get your principal back at par (no premium)
  - Your high-coupon cash flows are replaced by lower yields
  - Duration SHORTENS (you get money back faster, but at the
    worst time because you cannot reinvest at high rates)

  When rates rise:
  - Homeowners stop refinancing -> prepayments slow
  - Your principal is locked up for longer
  - Duration EXTENDS (you are stuck holding a low-coupon
    bond for longer, exactly when you would want to reinvest
    at higher rates)

  THIS IS THE OPPOSITE OF WHAT YOU WANT.

  Duration SHORTENS when rates fall (gains are capped)
  Duration EXTENDS when rates rise (losses are magnified)

  This is why MBS underperformed dramatically in 2022.
  As rates surged from 1.5% to 4.5%, MBS duration extended
  from ~4 years to ~7 years, amplifying losses.

  COMPARISON OF CONVEXITY:

  Bond Type              Duration   Convexity    Behavior
  =====================  ========   =========    ==================
  Zero-Coupon Treasury   High       Very High    Best convexity
  Coupon Treasury        Moderate   Positive     Good convexity
  Investment Grade Corp  Moderate   Positive     Good convexity
  Callable Corporate     Moderate   Mixed*       Neg when rates low
  Agency MBS             Moderate   Negative     Worst convexity
  Interest-Only Strip    High       Very Neg     Extreme neg convex.

  * Negative near call price, positive far from call price
```

```
PORTFOLIO IMPLICATIONS OF NEGATIVE CONVEXITY:

  Scenario: $200,000 bond portfolio, Duration = 6 years

  POSITIVE CONVEXITY PORTFOLIO (Treasuries):
    Convexity = 55

    Rates fall 2%:
      Duration: +12.00%   Convexity: +1.10%   Total: +13.10%
      Gain: $26,200

    Rates rise 2%:
      Duration: -12.00%   Convexity: +1.10%   Total: -10.90%
      Loss: $21,800

    ASYMMETRY: Gained $4,400 more than lost. Convexity helps.

  NEGATIVE CONVEXITY PORTFOLIO (MBS):
    Convexity = -30

    Rates fall 2%:
      Duration: +12.00%   Convexity: -0.60%   Total: +11.40%
      Gain: $22,800

    Rates rise 2%:
      Duration: -12.00%   Convexity: -0.60%   Total: -12.60%
      Loss: $25,200

    ASYMMETRY: Lost $2,400 more than gained. Convexity hurts.

    NET DIFFERENCE: $6,800 between the two portfolios!
    And this understates the MBS problem because duration
    itself extends when rates rise, making the true loss worse.
```

#### Immunization

Immunization is a strategy that uses duration matching to ensure that a bond portfolio will meet a specific future liability regardless of interest rate changes.

```
IMMUNIZATION CONCEPT:

  PROBLEM:
  You need exactly $1,000,000 in 7 years for a future obligation.
  You have $700,000 today to invest in bonds.
  If rates rise, your bonds lose value but you can reinvest coupons
  at higher rates. If rates fall, your bonds gain value but you
  reinvest coupons at lower rates. These two effects offset.

  SOLUTION:
  Match the DURATION of your portfolio to your TIME HORIZON.

  If your liability is in 7 years, build a portfolio with
  Macaulay Duration = 7 years.

  WHY THIS WORKS:

  Two effects of a rate change:

  1. PRICE EFFECT:
     Higher rates -> lower bond prices (hurts)
     Lower rates -> higher bond prices (helps)

  2. REINVESTMENT EFFECT:
     Higher rates -> coupons reinvested at higher rates (helps)
     Lower rates -> coupons reinvested at lower rates (hurts)

  When Duration = Time Horizon:
     Price effect and reinvestment effect exactly OFFSET.
     You reach your target regardless of rate changes.

  DIAGRAM:

  Portfolio Value
  at Horizon
       |
       |         *        *
       |        * *      * *
       |       *   *    *   *
  $1M  |------*-----****-----*------ Target
       |     *                 *
       |    *                   *
       |   *                     *
       +---+---+---+---+---+---+---
           -3% -2% -1%  0% +1% +2% +3%
                Rate Change

  At duration = horizon, the value converges to the target
  regardless of the rate change. The "valley" at the center
  is shallow and both sides converge near the target.
```

```
IMMUNIZATION EXAMPLE:

  Liability: $1,000,000 due in 5 years
  Current rates: 4.5%
  Required investment today: $1,000,000 / (1.045)^5 = $802,451

  Build a portfolio with Duration = 5 years

  Option A: Buy a 5-year zero-coupon bond
    Duration = 5 years (exactly matches)
    Simple but may not be available at desired size

  Option B: Barbell with 2-year and 10-year bonds
    Weight in 2-year (duration 1.9): w
    Weight in 10-year (duration 8.2): 1-w

    Target: w x 1.9 + (1-w) x 8.2 = 5.0
    Solving: 1.9w + 8.2 - 8.2w = 5.0
             -6.3w = -3.2
             w = 0.508

    Invest 50.8% in 2-year ($407,646)
    Invest 49.2% in 10-year ($394,805)
    Portfolio duration = 5.0 years

  IMPORTANT: Immunization requires REBALANCING.
  As time passes and rates change, the portfolio duration shifts.
  You must periodically (quarterly or after significant rate moves)
  rebalance to maintain duration = remaining time to liability.

  IMMUNIZATION CONDITIONS:
  1. Portfolio duration = liability duration (time to payment)
  2. Present value of portfolio >= present value of liability
  3. Portfolio must be rebalanced periodically
  4. Works best for parallel yield curve shifts
  5. Does not protect against non-parallel shifts perfectly
```

#### Duration and Convexity in Practice

```
COMMON BOND FUND METRICS:

  Fund                     Duration   Convexity   What This Means
  =======================  ========   =========   ===================
  Vanguard Short-Term       2.7        0.08       Low rate sensitivity
  (BSV)                                           Safe in rising rates

  Vanguard Total Bond       6.5        0.65       Moderate sensitivity
  (BND)                                           Core bond holding

  iShares 7-10 Year         7.8        0.70       Above average
  (IEF)                                           Meaningful rate risk

  iShares 20+ Year          17.2       3.95       Very high sensitivity
  (TLT)                                           Extreme rate risk

  iShares MBS               5.8       -0.30       Moderate duration
  (MBB)                                           NEGATIVE convexity!

  PVBP PER $100,000 INVESTED:

  BSV:  $27/bp    -> $2,700 per 1% rate change
  BND:  $65/bp    -> $6,500 per 1% rate change
  IEF:  $78/bp    -> $7,800 per 1% rate change
  TLT:  $172/bp   -> $17,200 per 1% rate change
  MBB:  $58/bp    -> $5,800 per 1% rate change (with neg convexity!)
```

```
PRACTICAL GUIDELINES:

  YOUR RISK TOLERANCE AND DURATION:

  Conservative (cannot tolerate > 5% bond loss):
    Maximum duration = 5 / expected rate move
    If you expect rates could rise 1%: max duration = 5 years
    Funds: BSV, short-term bond funds, T-bills

  Moderate (can tolerate 5-10% bond loss):
    Maximum duration = 10 / expected rate move
    If you expect rates could rise 1%: max duration = 10 years
    Funds: BND, intermediate bond funds

  Aggressive (willing to accept > 10% bond loss for
             higher yield and convexity benefits):
    Duration > 10 years
    Funds: TLT, long-term bond funds
    Only appropriate if you believe rates will fall

  DURATION MATCHING RULE OF THUMB:
  Your bond portfolio duration should approximately match
  your investment time horizon.

  5-year time horizon -> Duration ~5 years
  10-year time horizon -> Duration ~10 years

  This provides natural immunization against rate changes:
  price losses from rising rates are offset by higher
  reinvestment income, and vice versa.
```

---

### c) Common Misconceptions

**Misconception 1: "Duration is the average life of a bond."**

Macaulay duration is the weighted average time to receive cash flows, which is conceptually related to "average life" but is not the same thing. Modified duration is purely a price sensitivity measure and has nothing to do with the bond's life span. When someone says "this bond has a duration of 7," they usually mean modified duration of 7, which means the bond's price changes by approximately 7% for a 1% change in yield. Duration as a number of years is a mathematical coincidence of the units, not a time measurement.

**Misconception 2: "If a bond has a 5-year duration, I will lose exactly 5% if rates rise 1%."**

Duration provides an approximation, not an exact prediction. The actual price change depends on convexity, the shape of the yield curve shift, credit spread changes, and other factors. For small rate changes (25-50 basis points), duration is quite accurate. For large rate changes (100+ basis points), convexity becomes important and the duration estimate can be significantly off.

**Misconception 3: "Higher duration always means higher risk."**

Duration measures interest rate risk specifically. A bond could have low duration but high credit risk (a junk bond maturing in 2 years) or high duration but low credit risk (a 30-year Treasury). Total bond risk includes interest rate risk (duration), credit risk (default probability), liquidity risk, and reinvestment risk. Duration captures only the first of these.

**Misconception 4: "I should always minimize duration because rates might rise."**

If rates are already high and the economy is weakening, extending duration can be highly profitable. In late 2023, when the 10-year Treasury yielded over 5%, investors who extended duration captured significant gains as rates fell. The goal is not to minimize duration but to align duration with your market outlook and risk tolerance. In a falling-rate environment, longer duration is your friend.

**Misconception 5: "Mortgage-backed securities are safe because they are government-backed."**

Government-backed MBS (issued by Ginnie Mae, Fannie Mae, Freddie Mac) have virtually no credit risk. But they have significant interest rate risk amplified by negative convexity. In 2022, the iShares MBS ETF (MBB) lost over 11%, and individual MBS tranches lost much more. "Government-backed" means you will get your money back eventually, but it does not protect you from price declines caused by rising rates and negative convexity.

**Misconception 6: "Convexity does not matter for small portfolios."**

For a $50,000 bond portfolio with moderate duration, the convexity effect on a 1% rate change might be $200-$300. That is not trivial. More importantly, understanding convexity changes how you think about bond selection. Given two bonds with the same duration and yield, you should prefer the one with higher convexity. It gives you better upside and less downside. This free benefit (higher convexity at the same duration) is available to investors of any size.

**Misconception 7: "Duration matching means buying a bond that matures when I need the money."**

Maturity matching and duration matching are different. A 10-year coupon bond might have a duration of 7.5 years. If your liability is in 7.5 years, you should match the duration (7.5), not the maturity (10). Alternatively, you could combine shorter and longer bonds to create a portfolio with the target duration. Duration matching is about the weighted average timing of cash flows, not the final maturity date.

---

### d) Q&A

**Q: How do I find the duration of my bond fund?**

A: Every bond fund and ETF reports its "effective duration" or "modified duration" on its fact sheet and website. For Vanguard funds, go to the fund page and look under "Risk & Volatility." For iShares, look under "Exposure Breakdown." Your brokerage platform also typically displays duration alongside other fund characteristics. If you own individual bonds, your brokerage platform may calculate duration for each position, or you can use online bond calculators.

**Q: If I own BND (Vanguard Total Bond Market) with a duration of 6.5 years, how much will I lose if rates rise by 0.50%?**

A: Approximate loss = duration x rate change = 6.5 x 0.50% = 3.25%. On a $100,000 position, that is approximately $3,250. The convexity adjustment for a 0.50% move is small (about +0.16%), so the actual loss would be closer to 3.09%, or $3,090. For practical purposes at the retail level, the duration approximation of $3,250 is close enough.

**Q: Should I care about Macaulay duration or modified duration?**

A: For investment decision-making, use modified duration (or effective duration for bonds with embedded options). Modified duration directly tells you price sensitivity. Macaulay duration is primarily used for immunization calculations and for understanding the concept. When bond fund fact sheets report "duration," they almost always mean effective duration, which is close to modified duration for option-free bonds.

**Q: What is "key rate duration" and when does it matter?**

A: Key rate duration (also called partial duration) measures sensitivity to rate changes at specific points on the yield curve. A bond might have a 2-year key rate duration of 0.5 and a 10-year key rate duration of 6.0. This means it is much more sensitive to changes in 10-year rates than 2-year rates. Key rate durations matter when you expect non-parallel yield curve shifts. If you think the long end will rise but the short end will stay flat, key rate durations tell you exactly how your portfolio will respond. Most retail investors can ignore key rate durations, but institutional investors use them extensively.

**Q: How do I increase or decrease my portfolio duration?**

A: To increase duration, shift from shorter-maturity bonds/funds to longer-maturity ones. Replacing BSV (duration 2.7) with IEF (duration 7.8) increases duration. To decrease duration, do the opposite, or add cash (duration zero) to the portfolio. You can also use Treasury futures to adjust duration synthetically without selling existing holdings. For a simple approach, blend a short-duration fund with a long-duration fund to hit your target.

**Q: Does duration apply to stocks or only bonds?**

A: Duration is primarily a bond concept, but the underlying principle applies to any asset with known future cash flows. Equity duration is a concept used in academic finance, where high-growth stocks (with cash flows far in the future) have longer "duration" and are more sensitive to discount rate changes. This explains why growth stocks suffered more than value stocks in 2022 when rates rose sharply. The cash flows of growth companies are further in the future, making their present value more sensitive to the discount rate.

**Q: What happened to MBS duration in 2022 and why was it so bad?**

A: In early 2022, MBS had an effective duration of approximately 4 years. As rates rose sharply from 1.5% to 4.5%, prepayments slowed dramatically (nobody refinances from a 3% mortgage to a 6% mortgage). This caused MBS duration to extend to approximately 7 years, right as rates were rising. The combination of rising rates AND extending duration created losses far worse than the initial 4-year duration would have predicted. This "duration extension" in a rising-rate environment is the practical manifestation of negative convexity, and it is why MBS should be treated with extra caution compared to Treasuries of similar duration.

---

## YouTube Script

[VISUAL: Animated intro with show logo. Text: "Week 32: Duration and Convexity - Level 3: Advanced"]

**Alex:** Welcome back. Last week we learned how to read the yield curve. This week we are going to learn how to measure exactly how much your bonds will move when rates change. We are talking about duration and convexity.

**Sam:** Duration is one of those terms I see on every bond fund fact sheet, and I always just kind of gloss over it. I know it is important but I do not really understand what it means.

**Alex:** You are not alone. Most retail investors ignore duration, and that is a costly mistake. Duration is the single most important number for understanding your bond portfolio's risk. Let me put it in simple terms. Duration tells you how much your bond or bond fund will change in price for a 1% change in interest rates.

**Sam:** Give me an example.

**Alex:** If your bond fund has a duration of 6.5 years, like the Vanguard Total Bond Market fund, and rates rise by 1%, your fund will lose approximately 6.5%. On $100,000, that is a $6,500 loss. If rates rise by 2%, you lose approximately 13%, or $13,000.

[VISUAL: A scale/gauge showing duration = 6.5 years. As a "rates" slider moves up by 1%, a portfolio value bar drops from $100,000 to $93,500. Text: "Duration of 6.5 = lose 6.5% per 1% rate increase"]

**Sam:** And if rates fall, the opposite?

**Alex:** Exactly. A 1% rate drop would give you approximately a 6.5% gain, or $6,500. Duration works in both directions.

**Sam:** OK so higher duration means more sensitivity to rates. What determines a bond's duration?

**Alex:** Three main factors. First, maturity. Longer-maturity bonds have higher duration. A 30-year Treasury has a duration around 20 years while a 2-year Treasury has a duration around 1.9 years. Second, coupon rate. Higher coupons mean lower duration because you receive more cash flow earlier. Third, yield level. Higher yields mean lower duration because distant cash flows are discounted more heavily.

[ANIMATION: Reference animation/week32_duration_factors.py - Three side-by-side demonstrations. 1) Two bonds with different maturities (2-year and 30-year) showing their cash flow timelines as weighted bars, with the center of gravity (duration) marked. The 30-year has its center much further right. 2) Two bonds with different coupons (2% and 8%) showing how higher coupons pull the center of gravity forward. 3) Two bonds at different yield levels showing how higher yields compress the far cash flows.]

**Sam:** Can you explain the different types of duration? I have seen Macaulay, modified, and effective.

**Alex:** Sure. Macaulay duration is the original concept. It is the weighted average time until you receive all the bond's cash flows. Think of it like the balance point on a seesaw. If you put all the bond's cash flows on a timeline, weighted by their present value, the balance point is the Macaulay duration.

**Sam:** So for a zero-coupon bond, the Macaulay duration equals the maturity?

**Alex:** Exactly, because there is only one cash flow at the end. For a coupon bond, the Macaulay duration is always less than the maturity because the coupon payments pull the balance point forward.

[VISUAL: A seesaw/balance beam. On the left side, small bags of money at years 1, 2, 3, 4 represent coupon payments. On the right side, a large bag at year 5 represents the final coupon plus principal. The balance point (triangle fulcrum) is at year 4.2, labeled "Macaulay Duration = 4.2 years". Below: "Maturity = 5 years, but duration is only 4.2 years"]

**Sam:** And modified duration?

**Alex:** Modified duration takes Macaulay duration and adjusts it to directly measure price sensitivity. The formula is simple: modified duration equals Macaulay duration divided by one plus the yield. The result tells you the percentage price change for a 1% yield change. When people say "duration" in an investment context, they almost always mean modified duration.

**Sam:** What about effective duration?

**Alex:** Effective duration is used for bonds with embedded options, like callable bonds and mortgage-backed securities. For these bonds, the cash flows change when rates change because the issuer might call the bond or homeowners might refinance their mortgages. Modified duration does not account for this. Effective duration is calculated empirically by observing how the bond's price actually changes when you bump rates up and down.

[VISUAL: Three boxes side by side. "Macaulay Duration: Weighted average time to cash flows. Used for immunization." "Modified Duration: Price sensitivity to rates. Used for risk measurement." "Effective Duration: Price sensitivity for bonds with options. Handles callable bonds and MBS."]

**Sam:** Let us talk about PVBP because I want to understand the dollar impact.

**Alex:** PVBP stands for Price Value of a Basis Point. One basis point is one hundredth of one percent, or 0.01%. PVBP tells you how many dollars your bond position changes for a 1 basis point move in rates.

**Sam:** How do you calculate it?

**Alex:** Multiply modified duration by the bond price by 0.0001. For example, a $100,000 position with duration of 8 years has a PVBP of $100,000 times 8 times 0.0001, which equals $80. Every single basis point move in rates changes your position by $80.

[VISUAL: Table showing PVBP calculations for $100,000 invested in different maturities. 2-year: $19/bp. 5-year: $45/bp. 10-year: $82/bp. 20-year: $145/bp. 30-year: $200/bp. A highlight shows: "30-year bond: $200 per basis point. A 50 bp move = $10,000 gain or loss."]

**Sam:** So if I own $100,000 in TLT, the long-term Treasury ETF, with a duration of 17 years?

**Alex:** Your PVBP is $170 per basis point. A 1% rate move, which is 100 basis points, changes your position by $17,000. That is a 17% swing. In 2022, when rates rose about 2.5%, TLT lost approximately 31%. If you knew the duration, you could have predicted that.

**Sam:** That really puts it in perspective. Now let us talk about convexity because you said duration alone is not enough.

**Alex:** Right. Duration is a straight-line approximation of a curved relationship. Think about it this way. The actual relationship between bond prices and yields is a curve, not a straight line. Duration draws a tangent line to that curve at the current yield. For small movements along the curve, the tangent line is a good approximation. For large movements, the tangent line diverges from the actual curve.

[ANIMATION: Reference animation/week32_convexity_demo.py - A price-yield curve is drawn (the classic convex curve). A tangent line (duration) is drawn at the current yield point. As the yield slider moves left (rates falling), the actual price on the curve rises above the tangent line - this gap is labeled "Convexity bonus: you gain MORE than duration predicts." As the yield slider moves right (rates rising), the actual price on the curve is above the tangent line - this gap is labeled "Convexity cushion: you lose LESS than duration predicts."]

**Sam:** So convexity always helps you?

**Alex:** For bonds with positive convexity, yes. You gain more than duration predicts when rates fall, and you lose less than duration predicts when rates rise. This asymmetry is free. It is a mathematical property of fixed cash flow streams discounted at different rates.

**Sam:** How do I use convexity in my calculations?

**Alex:** The formula adds a second term. Percentage price change equals negative duration times the rate change, plus one-half times convexity times the rate change squared. The second term is always positive for positive convexity bonds, which is why it always helps.

[VISUAL: The formula displayed clearly with a worked example. "% Change = -Duration x Ay + 0.5 x Convexity x (Ay)^2". Example: Duration 10, Convexity 120, rates rise 1%. Duration effect: -10%. Convexity effect: +0.6%. Total: -9.4% instead of -10%. "Convexity saved you 0.6% on a $100,000 portfolio = $600"]

**Sam:** Now I have to ask about negative convexity because that sounds scary.

**Alex:** Negative convexity is exactly what it sounds like. Instead of the curve bending in your favor, it bends against you. You gain less than expected when rates fall and lose more than expected when rates rise.

**Sam:** Why would any bond have negative convexity?

**Alex:** The primary cause is embedded options that favor the issuer or the borrower. In a callable bond, the issuer can call (buy back) the bond when rates fall. This caps your upside near the call price. You cannot benefit from further rate declines because the issuer will just take the bond away from you and reissue at lower rates.

[VISUAL: Two price-yield curves overlaid. The solid curve (non-callable Treasury) shows a smooth convex shape, with price rising significantly as rates fall. The dashed curve (callable bond) follows the Treasury curve on the right (high rates) but flattens and caps near the call price on the left (low rates). The area between the curves on the left is labeled "Lost upside due to call option"]

**Sam:** And mortgage-backed securities are even worse?

**Alex:** Much worse. Every homeowner with a mortgage has the option to refinance at any time. When rates fall, homeowners refinance en masse. Your MBS gets its principal returned at par, and you have to reinvest at the now-lower rates. But when rates rise, nobody refinances. Your money is locked in at the old low rate for much longer than expected. Duration extends exactly when you do not want it to.

**Sam:** This is what happened in 2022, right?

**Alex:** Exactly. MBS went into 2022 with an effective duration of about 4 years. As rates surged, prepayments collapsed and duration extended to about 7 years. So not only were rates rising, but the MBS was becoming more sensitive to those rising rates as they moved higher. It was a double hit. The MBS ETF MBB lost about 11% that year, and some MBS tranches lost much more.

[ANIMATION: Reference animation/week32_mbs_extension.py - A visualization of MBS duration changing. Starting state: rates at 2%, duration at 4 years, shown as a meter. As rates slide from 2% to 5%, the duration meter extends from 4 to 7 years. Simultaneously, a portfolio value bar drops. Annotations show: "Rising rates: BAD" and "Extending duration: MAKES IT WORSE." The combination produces a loss that is larger than what 4-year duration would have predicted.]

**Sam:** So should I avoid MBS entirely?

**Alex:** Not necessarily, but you should understand what you are buying. Government-backed MBS has zero credit risk, and it typically offers a yield premium over comparable Treasuries. That premium is compensation for the negative convexity. If you hold MBS in a stable-rate environment, you collect the extra yield without the convexity problem. The danger is in rapidly changing rate environments. My advice: if you own MBS or a fund that holds MBS, know its duration and understand that in extreme rate moves, it will behave worse than a Treasury of similar duration.

**Sam:** Let me bring this back to practical investing. How should someone use duration to manage their bond portfolio?

**Alex:** Here is my framework. First, know your duration. Look up the effective duration of every bond fund you own. Calculate your portfolio's weighted average duration. Second, stress test your portfolio. Multiply your duration by 1% and by 2% to see how much you would lose if rates rise. Ask yourself if you can tolerate those losses. Third, match your duration to your horizon. If you need the money in 5 years, your duration should be around 5 years. This immunizes you against rate changes.

[VISUAL: A three-step checklist. Step 1: "Know Your Duration" with icons of bond fund fact sheets showing duration numbers. Step 2: "Stress Test" with a table showing "If rates rise 1%/2%/3%, you lose $X/$Y/$Z". Step 3: "Match to Horizon" with a timeline showing "Need money in 7 years -> Duration should be ~7 years"]

**Sam:** What about the allocation between short, intermediate, and long bonds?

**Alex:** In a rising-rate environment or when you are uncertain, stay short. Duration of 2 to 4 years. You sacrifice some yield but protect against rate surprises. In a falling-rate environment, extend duration. Duration of 8 to 15 years. You capture both higher yields and price gains as rates decline. In a stable-rate environment, intermediate duration is fine. Duration of 5 to 7 years. You get reasonable yield without extreme sensitivity.

**Sam:** And what about the yield curve shape? Last week we talked about using the curve's shape for decisions.

**Alex:** They connect directly. When the curve is steep, staying short costs you a lot of yield because long rates are much higher. But long bonds have more duration risk. When the curve is flat, there is no yield advantage to extending, so stay short and take less risk. When the curve is inverted, short-term instruments actually yield more, so you get paid more for taking less risk. That is a free lunch, and it is the market's way of telling you to stay short.

[VISUAL: A decision matrix combining yield curve shape and duration recommendation. "Steep Curve: Long bonds yield much more, but duration risk is high. Moderate duration." "Flat Curve: No yield pickup for duration risk. Stay short." "Inverted Curve: Short rates higher than long rates. Stay short, get paid more."]

**Sam:** Let us talk about immunization briefly. I find this concept elegant even though it is more of an institutional strategy.

**Alex:** Immunization is beautiful in its simplicity. You match your portfolio's duration to the date you need the money. If rates rise, your bonds lose value but you reinvest coupons at higher rates. If rates fall, your bonds gain value but you reinvest coupons at lower rates. These two effects cancel out. At the horizon date, you arrive at approximately the same ending value regardless of what rates did.

**Sam:** So it is like a hedge that works in both directions?

**Alex:** Exactly. And it does not cost anything. You just have to rebalance periodically to keep the duration matched. The catch is it works perfectly only for parallel yield curve shifts. If the curve twists or the shift is non-parallel, there is some tracking error. But for most retail investors, duration matching is far better than not thinking about duration at all.

**Sam:** Let me try to bring all of this together. Duration tells me sensitivity to rates, roughly percentage loss per 1% rate rise. Convexity improves that estimate, and positive convexity always works in my favor. Negative convexity, which is mainly in callable bonds and MBS, works against me. And PVBP converts all of this into actual dollars.

**Alex:** Perfect summary. Let me add one more thought. When you are comparing two bonds or two bond funds with similar duration and yield, always prefer the one with higher convexity. It is free protection. You get more upside in a rate decline and less downside in a rate rise. All else equal, higher convexity is always better.

[VISUAL: Two bonds displayed side by side. Bond A: Duration 7, Yield 4.5%, Convexity 60. Bond B: Duration 7, Yield 4.5%, Convexity 85. A star or checkmark next to Bond B with text: "Same duration, same yield, but better convexity. Choose Bond B."]

**Sam:** And if I can only remember one number?

**Alex:** Remember your portfolio duration. If it is 6, you lose approximately 6% for every 1% rates rise. If it is 3, you lose approximately 3%. That single number tells you more about your bond risk than anything else.

**Sam:** This has been really helpful. I finally understand what those numbers on my fund fact sheets mean.

**Alex:** And that is the whole point. Next week we move to credit analysis, where we will learn how to evaluate the other major risk in bonds: the risk that the borrower does not pay you back. Duration is interest rate risk. Credit analysis is default risk. Together, they give you the complete picture of bond investing.

**Sam:** Thanks, everyone. See you next week.

[VISUAL: End screen with show logo, "Week 32: Duration and Convexity" summary, and preview of Week 33: Credit Analysis]

**Alex:** See you then.
