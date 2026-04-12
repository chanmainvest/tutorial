# Week 38: LEAPS and Long-Term Options

---

## Reading Section

### a) Why This Is Important

LEAPS -- Long-Term Equity Anticipation Securities -- are options with expiration dates one to two or more years in the future. They occupy a unique and valuable niche in the options universe, bridging the gap between short-term options trading and long-term stock ownership.

Understanding LEAPS is critical because:

- **Time is on your side (relatively)**: Unlike short-dated options that bleed value daily, LEAPS have much slower time decay. This gives your investment thesis months or years to play out, dramatically changing the risk/reward calculus of options strategies.
- **Stock replacement**: Deep in-the-money LEAPS can replicate the return profile of stock ownership at a fraction of the capital. This makes them a legitimate tool for capital-efficient long-term investing, not just speculation.
- **Income generation**: The "poor man's covered call" strategy uses LEAPS as a substitute for stock in a covered call setup, generating income with far less capital than owning shares outright.
- **Portfolio construction**: LEAPS allow sophisticated investors to construct portfolios with defined risk, leveraged exposure, and capital efficiency that is impossible with stocks and margin alone.

The catch is that LEAPS still have an expiration date. They still have time decay, even if it is slower. They still have extrinsic value that represents a real cost. And they require active management -- rolling, adjusting, and monitoring -- that stock ownership does not.

This lesson teaches you how to use LEAPS intelligently: when they are a superior alternative to stock, when they are not, how to select strikes and expirations, and how to manage them over their lifetime.

---

### b) What You Need to Know

#### 1. What Are LEAPS?

LEAPS are simply options contracts with longer expiration dates. While standard options typically expire within a few weeks to a few months, LEAPS have expirations extending one to two and a half years into the future. The term "LEAPS" is a trademark of the CBOE, but traders use it generically to refer to any long-dated option.

```
LEAPS vs. STANDARD OPTIONS

Feature                Standard Options      LEAPS
----------------------------------------------------------
Expiration             1 week - 6 months     1 - 2.5 years
Typical theta decay    Fast, accelerating     Slow, gradual
Premium cost           Lower absolute         Higher absolute
Extrinsic value        Higher % of premium    Lower % (if deep ITM)
Delta stability        Changes rapidly        More stable
Vega sensitivity       Lower                  Higher
Liquidity              Generally higher       Often lower
Bid-ask spread         Tighter                Wider
Available on           Most optionable        Most large-cap
                       stocks                 stocks and ETFs
```

**Key point**: LEAPS are available on most large-cap stocks and major ETFs. They typically get listed about 2.5 years before expiration and are available in January expirations (and sometimes other months). When a LEAPS contract gets within 9 months of expiration, it is no longer considered a LEAPS -- it becomes a regular option.

#### 2. Advantages of LEAPS

**Advantage 1: Time for Your Thesis to Play Out**

This is the single most important advantage. Short-dated options require you to be right about both *direction* and *timing*. LEAPS relax the timing constraint significantly.

```
SCENARIO: You believe NVDA will benefit from AI growth over
the next 18 months. NVDA is at $800.

3-Month ATM Call ($800 strike, $45 premium):
  - Must be right within 3 months
  - Breakeven: $845 (+5.6%)
  - If NVDA trades sideways for 2 months then rallies: 
    most of your premium is gone before the move happens

18-Month LEAPS Call ($800 strike, $130 premium):
  - Have 18 months to be right
  - Breakeven: $930 (+16.3%) -- higher, but much more time
  - If NVDA trades sideways for 6 months then rallies:
    you still have 12 months of time value remaining
  - Theta burn during sideways period: ~$0.20/day vs ~$0.50/day
```

**Advantage 2: Lower Theta Decay**

Theta (time decay) is not linear. It accelerates as expiration approaches. This works enormously in favor of LEAPS holders.

```
THETA DECAY PROFILE (ATM option, 30% IV, $200 stock)

Days to          Daily Theta     Monthly Theta     % of Premium
Expiration       ($/day)         ($/month)         Lost/Month
----------------------------------------------------------------
730 (2 years)    $0.04           $1.20             0.5%
548 (1.5 yr)     $0.05           $1.50             0.7%
365 (1 year)     $0.06           $1.80             1.0%
180 (6 months)   $0.09           $2.70             1.8%
90  (3 months)   $0.13           $3.90             3.3%
30  (1 month)    $0.22           $6.60             8.5%
7   (1 week)     $0.46           N/A               ~30%

KEY INSIGHT: A 2-year LEAPS loses 0.5% of its value per month
to theta. A 1-month option loses 8.5%. That is a 17x difference
in the cost of maintaining the position.
```

```
THETA DECAY CURVE (ASCII Visualization)

Premium
  ^
  |****
  |    ****
  |        ****
  |            ****
  |                *****
  |                     *****
  |                          ******
  |                                *********
  |                                         ************
  |                                                     *****
  +---+---+---+---+---+---+---+---+---+---+---+---+---+--->
  24  22  20  18  16  14  12  10   8   6   4   2   0
                    Months to Expiration

  The curve shows that decay is gradual for the first 12-18
  months, then accelerates dramatically in the final 6 months.
  This is why most LEAPS traders roll or close positions when
  they reach 6-9 months to expiration.
```

**Advantage 3: Higher Vega Sensitivity**

LEAPS have higher vega than short-dated options. This means they benefit more from increases in implied volatility. If you buy a LEAPS when IV is low and IV subsequently increases, you can profit from the volatility expansion even if the stock moves only modestly.

```
VEGA COMPARISON ($200 stock, ATM call)

Expiration        Vega (per 1% IV change)
------------------------------------------
30-day call       $0.23
90-day call       $0.40
180-day call      $0.56
365-day call      $0.79
730-day LEAPS     $1.12

A 5% increase in IV adds:
  30-day call:    $1.15 per share
  730-day LEAPS:  $5.60 per share

This is both an advantage and a risk. If IV drops,
LEAPS lose more value than short-dated options.
```

#### 3. Deep ITM LEAPS as Stock Replacement

This is the most practical and powerful use of LEAPS for long-term investors. By purchasing deep in-the-money LEAPS calls, you can replicate the return profile of stock ownership with significantly less capital.

**How it works:**

Buy a LEAPS call with a delta of 0.80 or higher (deep ITM). This option will move almost dollar-for-dollar with the stock and contains minimal extrinsic value relative to its total premium.

```
STOCK REPLACEMENT EXAMPLE: AAPL at $185

Option 1: Buy 100 shares of AAPL
  Cost:            $18,500
  Dividend income: ~$100/year (0.54% yield)
  Risk:            Full downside to $0

Option 2: Buy 1 LEAPS $140 call, 2-year expiry
  Delta:           0.88
  Premium:         $52 per share ($5,200 total)
  Intrinsic value: $185 - $140 = $45
  Extrinsic value: $52 - $45 = $7 per share ($700 total)

Capital comparison:
  Stock:           $18,500
  LEAPS:           $5,200
  Capital freed:   $13,300 (72% less capital deployed)

Return comparison if AAPL goes to $220 (+19%) in 18 months:
  Stock return:    $3,500 + $150 dividends = $3,650 (19.7%)
  LEAPS return:    ($220-$140) - $52 = $28 per share = $2,800 (53.8%)

  LEAPS made less in absolute dollars ($2,800 vs $3,650)
  but much more in percentage terms (53.8% vs 19.7%)
  and deployed $13,300 less capital

Return comparison if AAPL drops to $150 (-19%) in 18 months:
  Stock loss:      -$3,500 + $150 dividends = -$3,350 (-18.1%)
  LEAPS loss:      ($150-$140) - $52 = -$42 per share + ~$2 time = -$4,000 (-77%)

  Wait -- LEAPS lost MORE in absolute dollars and percentage!
  Yes, because of the extrinsic value decay. But the maximum
  loss is capped at $5,200 (the premium), whereas the stock
  could theoretically drop to zero (loss = $18,500).
```

**When stock replacement works:**
- The stock is expected to appreciate significantly (more than the extrinsic value cost)
- You want to free up capital for diversification or other investments
- You want defined-risk exposure to a volatile name
- The freed-up capital can earn a meaningful return (bonds, money market)

**When stock replacement fails:**
- The stock trades sideways (extrinsic value decays with no offsetting gain)
- The stock pays a significant dividend (you miss the income)
- You need indefinite holding period (LEAPS expire, stocks do not)
- Bid-ask spreads are wide (transaction costs erode returns)

#### 4. Selecting the Right LEAPS

**Strike selection:**

```
LEAPS STRIKE SELECTION GUIDE

For Stock Replacement (conservative):
  Target delta: 0.80 - 0.90
  Typical strike: 15-25% below current stock price
  Extrinsic value: Usually 3-8% of premium
  Leverage: 3-5x
  Probability of expiring ITM: 75-85%

For Moderate Leverage:
  Target delta: 0.60 - 0.75
  Typical strike: 5-15% below current stock price
  Extrinsic value: Usually 15-30% of premium
  Leverage: 5-8x
  Probability of expiring ITM: 60-70%

For Aggressive Leverage:
  Target delta: 0.40 - 0.55
  Typical strike: At-the-money or slightly OTM
  Extrinsic value: 100% of premium (all time value)
  Leverage: 8-15x
  Probability of expiring ITM: 40-50%

RECOMMENDATION: For most investors, the conservative
stock replacement approach (delta 0.80-0.90) offers
the best balance of leverage, cost, and probability.
```

**Expiration selection:**

Choose the longest available expiration in most cases. Here is why:

```
COST OF ROLLING vs. BUYING LONGER DURATION

Strategy A: Buy 1-year LEAPS and roll annually
  Year 1 extrinsic: $7/share
  Year 2 extrinsic: $7/share (after rolling)
  Total cost over 2 years: $14/share

Strategy B: Buy 2-year LEAPS upfront
  Extrinsic value: $10/share

  Savings: $4/share (29% less extrinsic value cost)

Theta is non-linear, so a 2-year option does NOT cost
twice as much extrinsic value as a 1-year option.
The longer you go, the cheaper the per-day cost of time.
```

#### 5. LEAPS Covered Calls (Poor Man's Covered Call)

The "poor man's covered call" (PMCC) is one of the most capital-efficient income strategies available. Instead of buying 100 shares of stock to sell covered calls against, you buy a deep ITM LEAPS call and sell short-dated calls against it.

```
TRADITIONAL COVERED CALL vs. POOR MAN'S COVERED CALL

Traditional Covered Call on MSFT at $400:
  Buy 100 shares:                     $40,000
  Sell 1 monthly $410 call:           +$6.00/share (+$600)
  Monthly income:                     $600
  Return on capital (monthly):        1.5%
  Capital required:                   $40,000

Poor Man's Covered Call on MSFT at $400:
  Buy 1 LEAPS $340 call (18-month):   $72/share ($7,200)
    Delta: 0.82
    Intrinsic: $60
    Extrinsic: $12
  Sell 1 monthly $410 call:           +$6.00/share (+$600)
  Monthly income:                     $600
  Return on capital (monthly):        8.3%
  Capital required:                   $7,200

SAME income. 82% less capital deployed.
Return on capital is 5.5x higher.
```

**PMCC Rules and Guidelines:**

```
PMCC SETUP RULES

1. LEAPS Selection:
   - Minimum delta: 0.75 (prefer 0.80+)
   - Minimum expiration: 12 months (prefer 18+)
   - Strike deep enough that intrinsic > short call premium
   
2. Short Call Selection:
   - Expiration: 30-45 days
   - Delta: 0.20-0.30 (OTM)
   - Strike above LEAPS breakeven if possible
   
3. Risk Management:
   - Width between LEAPS strike and short call strike
     should be greater than total LEAPS extrinsic value paid
   - Roll short call if it goes ITM
   - Roll LEAPS when it reaches 6-9 months to expiry

MAXIMUM PROFIT CALCULATION:
  Max profit = (Short call strike - LEAPS strike) - Net debit
  
  Example: LEAPS $340 cost $72, Short $410 call received $6
  Net debit = $72 - $6 = $66
  Max profit = ($410 - $340) - $66 = $70 - $66 = $4/share
  
  Wait -- that seems small! But that is per expiration cycle.
  Over 12 monthly cycles: 12 x $6 = $72 in premiums collected.
  If stock stays between $340 and $410, total return potential
  is much higher.
```

**Scenario Analysis for PMCC:**

```
PMCC: MSFT $340 LEAPS call / Short monthly $410 call
Net debit: $66/share. MSFT currently at $400.

Scenario 1: MSFT rises slowly to $420 over 6 months
  Short calls collected: ~$36 (6 months x $6 avg)
  LEAPS appreciation: $400 -> $420 = ~$16 (delta 0.82)
  BUT: short $410 call is challenged
  Action: Roll short call up and out for credit
  Estimated profit: $30-40/share over 6 months (45-60% return)

Scenario 2: MSFT trades sideways at $400 for 12 months
  Short calls collected: ~$72 (12 months x $6 avg)
  LEAPS theta decay: ~$8 over 12 months
  Net income: $72 - $8 = $64/share (89% return on $72 LEAPS)

Scenario 3: MSFT drops to $360 over 6 months
  Short calls collected: ~$24 (lower premiums as stock drops)
  LEAPS depreciation: ~$36 (delta-adjusted)
  Net loss: -$36 + $24 = -$12/share (-17% return)
  LEAPS still has 12+ months of time value
  Can continue selling calls at lower strikes

Scenario 4: MSFT crashes to $300
  Short calls collected: ~$12
  LEAPS value: approximately $5-10 (deep OTM now)
  Net loss: -$54 to -$59/share (-75-82% return)
  This is the tail risk of PMCC -- similar to stock ownership
```

#### 6. Cost Comparison to Stock Ownership

Let us do a comprehensive cost analysis over different time periods:

```
TOTAL COST OF OWNERSHIP: $200 STOCK, 3-YEAR PERIOD

Strategy 1: Buy and Hold Stock
  Initial investment:    $20,000
  Dividends received:    $900 (1.5% annual yield)
  Transaction costs:     $0 (commission-free)
  Opportunity cost:      $0 (capital is fully deployed)
  Total cost:            -$900 (net income from dividends)
  Net cost of ownership: Stock price change +/- $900

Strategy 2: Roll Annual LEAPS (deep ITM, delta 0.85)
  Year 1 LEAPS cost:    $5,500 (extrinsic: $700)
  Year 2 LEAPS cost:    $5,800* (extrinsic: $750, roll cost ~$100)
  Year 3 LEAPS cost:    $6,100* (extrinsic: $800, roll cost ~$100)
  Total extrinsic paid: $2,250 over 3 years
  Capital freed:         ~$14,000 (invested at 4% = $1,680)
  Dividends missed:      -$900
  Net cost:              $2,250 + $900 - $1,680 = $1,470

  *Approximate, depends on stock price at roll time

BREAK-EVEN ANALYSIS:
  LEAPS are cheaper than stock when:
  Interest on freed capital > Extrinsic value + Missed dividends
  $14,000 x r > $750/year + $300/year
  r > 7.5% (approximate)

  In a high interest rate environment (5%+), LEAPS become
  more cost-competitive because the freed capital earns more.
  In low rate environments, stock ownership is usually cheaper.
```

#### 7. Managing LEAPS Positions

LEAPS require ongoing management. Here is a comprehensive management framework:

**Rolling:**

Rolling means closing your current LEAPS position and opening a new one with a later expiration. This is necessary because LEAPS eventually become short-dated options with accelerating theta decay.

```
WHEN TO ROLL LEAPS

Trigger 1: Time-based
  Roll when LEAPS reaches 6-9 months to expiration
  Reason: Theta acceleration begins in earnest
  
  Example: Bought 24-month LEAPS in January 2024
  Expiration: January 2026
  Roll window: April-July 2025 (6-9 months before expiry)
  Roll to: January 2027 LEAPS

Trigger 2: Delta-based
  Roll when delta drops below 0.65 (for stock replacement)
  Reason: Position is losing its stock-like characteristics
  
  Example: Bought $160 LEAPS call when stock was $200 (delta 0.85)
  Stock drops to $175. Delta is now 0.70. Not yet at trigger.
  Stock drops to $165. Delta is now 0.58. Roll to lower strike
  or close position.

Trigger 3: Profit-based
  Consider rolling when position is up 50-80%
  Reason: Lock in profits while maintaining exposure
  
  Example: Bought $160 LEAPS for $52. Stock rose to $240.
  LEAPS now worth $85. Profit: $33 (63%).
  Sell current LEAPS, buy new $200 strike LEAPS for $55.
  Lock in $30 of profit, maintain bullish exposure.

ROLL MECHANICS:
  Roll = Sell current LEAPS + Buy new LEAPS
  Net cost = New LEAPS premium - Current LEAPS value
  The roll is a debit (costs money) if buying more time
  Track cumulative roll costs to know true break-even
```

**Tax considerations:**

LEAPS can have significant tax implications. Positions held for more than 12 months and sold for a profit qualify for long-term capital gains treatment. This is a major advantage over short-dated options, which almost always generate short-term capital gains.

```
TAX COMPARISON (assuming 37% income / 20% LTCG brackets)

Short-term option trade (held < 1 year):
  $5,000 profit
  Tax: $5,000 x 37% = $1,850
  After-tax profit: $3,150

LEAPS (held > 1 year):
  $5,000 profit
  Tax: $5,000 x 20% = $1,000
  After-tax profit: $4,000

  Difference: $850 more after-tax profit with LEAPS
  That is 27% more money in your pocket.

IMPORTANT: To qualify for LTCG, you must hold the LEAPS
for more than 12 months. Buy a 2-year LEAPS and you have
plenty of time to exceed the 12-month threshold before
you need to roll.
```

#### 8. LEAPS on ETFs

LEAPS on broad market ETFs (SPY, QQQ, IWM) deserve special mention because they offer leveraged exposure to diversified indices with defined risk.

```
LEAPS ON SPY: LEVERAGED INDEX EXPOSURE

SPY at $500. You want $100,000 of S&P 500 exposure.

Traditional: Buy 200 shares of SPY
  Cost: $100,000
  Annual dividends: ~$1,400 (1.4% yield)

LEAPS: Buy 2 deep ITM LEAPS $420 calls, 2-year expiry
  Delta: 0.85
  Premium: $95/share ($19,000 total)
  Intrinsic: $80/share ($16,000)
  Extrinsic: $15/share ($3,000)
  Effective exposure: 200 shares x 0.85 = 170 share equivalents

Capital freed: $81,000
$81,000 invested in Treasury bills at 4.5% = $3,645/year

Net cost of LEAPS strategy:
  Extrinsic value decay: ~$3,000 over 2 years = $1,500/year
  Missed dividends: $1,400/year
  Treasury bill income: +$3,645/year
  Net annual benefit: +$745/year

In this high-rate environment, the LEAPS strategy actually
MAKES money compared to stock ownership, while freeing up
$81,000 of capital and providing defined downside risk.

Caveat: If rates drop below ~3%, the economics reverse.
```

#### 9. Advanced LEAPS Strategies

**LEAPS Diagonal Spread:**

```
Buy LEAPS $420 call (24-month, delta 0.85): -$95
Sell near-term $510 call (45-day, delta 0.25): +$7

Net debit: $88/share
Max profit zone: $510 at short call expiry
Monthly income potential: ~$7/month ($84/year)
Income covers: 56% of LEAPS annual extrinsic decay

This is the PMCC structure applied systematically
over the life of the LEAPS.
```

**LEAPS Collar:**

```
Own LEAPS $420 call (24-month): $95
Buy LEAPS $450 put (24-month): $30
Sell LEAPS $550 call (same expiry): -$18

Total cost: $95 + $30 - $18 = $107
Maximum loss: $107 - ($450 - $420) = $107 - $30 = $77/share
Maximum gain: ($550 - $420) - $107 = $130 - $107 = $23/share

This creates a defined-risk, defined-reward position
that caps both upside and downside over 2 years.
```

**LEAPS Calendar Spread:**

```
Sell 6-month $500 call: +$22
Buy 24-month $500 call: -$48

Net debit: $26/share
Profit driver: Faster decay of short-term option
Sweet spot: Stock near $500 at short option expiry

If stock is at $500 when short call expires:
  Short call expires worthless: +$22
  LEAPS still has ~18 months of value: ~$40
  Net position value: $40 on $26 investment = +54%
```

#### 10. Common Pitfalls with LEAPS

```
PITFALL                          SOLUTION
-------------------------------------------------------------------
1. Buying ATM LEAPS for         Buy deep ITM (delta 0.80+) for
   stock replacement             stock replacement; ATM has too
                                 much extrinsic value

2. Forgetting to roll            Set calendar alerts for 9 months
                                 before expiration

3. Ignoring dividends            Factor in missed dividends when
                                 comparing cost to stock

4. Wide bid-ask spreads          Use limit orders at midpoint;
                                 be patient; trade liquid names

5. Over-leveraging because       Treat LEAPS premium as full
   "it is long-term"             position size for risk purposes

6. Not accounting for IV         LEAPS have high vega; buying
                                 when IV is elevated means you
                                 overpay for the position

7. Rolling too late              Rolling at 3 months costs more
                                 than rolling at 9 months because
                                 of theta acceleration

8. Treating LEAPS as stock       LEAPS expire. Stocks do not.
                                 Always have a management plan.
```

---

### c) Common Misconceptions

**Misconception 1: "LEAPS do not have time decay."**

This is dangerously wrong. LEAPS absolutely have time decay -- it is just slower. A 2-year ATM LEAPS on a $200 stock might lose $0.04 per day to theta. Over 30 days, that is $1.20. Over a year, it is $14.60. That is real money. The advantage is not the absence of decay but the rate: $0.04/day versus $0.22/day for a 1-month option. But do not confuse "slower" with "none."

**Misconception 2: "LEAPS are always cheaper than owning stock."**

Only sometimes. In low interest rate environments with high-dividend stocks, owning stock is often cheaper. The extrinsic value of LEAPS, plus missed dividends, can exceed the opportunity cost of tying up capital in stock. LEAPS are most cost-effective on low-dividend stocks in high interest rate environments, where the freed-up capital earns meaningful returns.

**Misconception 3: "I should buy ATM LEAPS for maximum leverage."**

ATM LEAPS offer more leverage but at a much higher cost. All of the premium is extrinsic value, meaning 100% of your investment decays over time. For stock replacement, deep ITM LEAPS (delta 0.80+) are far superior because most of the premium is intrinsic value (which does not decay) and only a small portion is extrinsic value.

**Misconception 4: "LEAPS are set-it-and-forget-it investments."**

LEAPS require active management. You need to monitor delta, theta acceleration, and the overall thesis. Most importantly, you need to roll before theta accelerates, typically at the 6-9 month mark. Treating LEAPS like stock and ignoring them leads to time decay eating away profits and eventually leaving you with a short-dated option that behaves nothing like your original position.

**Misconception 5: "The poor man's covered call is strictly better than a regular covered call."**

The PMCC is more capital-efficient, but it has a higher risk per dollar invested. If the stock drops 30%, the stock-based covered call might lose 25% of its value (offset by premium collected). The PMCC might lose 70-80% of its value, because the LEAPS loses significantly more of its value on a percentage basis. The PMCC is also more complex to manage and has wider bid-ask spreads.

**Misconception 6: "I can always roll my LEAPS at a reasonable cost."**

Rolling costs depend on implied volatility, bid-ask spreads, and how far the stock has moved. If the stock has dropped significantly, your current LEAPS may be worth very little, and the new LEAPS costs a substantial premium. In practice, rolling a losing position can be very expensive, and at some point it is better to close the position and reassess.

---

### d) Common Questions and Answers

**Q1: How deep in-the-money should I go for stock replacement LEAPS?**

A: Target a delta of 0.80 to 0.90. This typically means a strike price 15-25% below the current stock price. The deeper you go, the more the LEAPS behaves like stock (less leverage, less extrinsic value, higher probability of success). Going too deep (delta > 0.95) means you are paying almost full stock price, which defeats the capital efficiency purpose. Going too shallow (delta < 0.70) means too much of your premium is extrinsic value, increasing your cost of carry.

**Q2: How do I handle dividends when using LEAPS instead of stock?**

A: You do not receive dividends on LEAPS. However, dividends are partially priced into the option: the call premium is reduced (and put premium is increased) by the expected dividend stream. So you are not entirely "missing" the dividend -- you are paying less for the LEAPS because of it. For high-dividend stocks (yield > 3%), the missed income makes LEAPS less attractive. For low-dividend or no-dividend stocks, this is not an issue.

**Q3: When should I roll my LEAPS?**

A: The standard guideline is to roll when you reach 6-9 months to expiration. At this point, theta begins accelerating meaningfully. Roll to the longest available expiration for the lowest per-day time decay cost. If your position is profitable, consider rolling to a higher strike to lock in some gains. If the position is losing, assess whether your thesis is still valid before committing capital to a new LEAPS.

**Q4: Can I use LEAPS in a retirement account?**

A: Yes. Most IRAs allow buying LEAPS calls and puts. LEAPS are particularly attractive in IRAs because of the tax treatment. Since LEAPS are held long-term (over 12 months), they would qualify for long-term capital gains treatment in a taxable account. In an IRA, all gains are tax-deferred (traditional) or tax-free (Roth) regardless, so there is no tax advantage difference. But the capital efficiency of LEAPS is still valuable in IRAs, where you cannot use margin.

**Q5: What happens to my LEAPS if the company is acquired?**

A: If the acquisition is for cash at a fixed price, your call options will be adjusted and eventually settled at the acquisition price minus your strike. If the acquisition is for stock, your options will be adjusted to reference the acquiring company's stock. In either case, options protect you -- you will receive the appropriate value. However, the time value of your LEAPS will collapse to near zero after an acquisition announcement, since the stock price becomes fixed.

**Q6: How do LEAPS perform in a bear market?**

A: LEAPS calls lose value in bear markets, but their performance depends on the depth of ITM. A deep ITM LEAPS (delta 0.90) will lose roughly 90% of the stock's decline in dollar terms, but potentially more in percentage terms (due to leverage). However, the key advantage of LEAPS in bear markets is that your maximum loss is capped at the premium paid. If you own $5,000 of LEAPS instead of $20,000 of stock and the stock drops 60%, you lose at most $5,000 versus $12,000.

**Q7: Should I use LEAPS calls or LEAPS puts for hedging?**

A: For hedging existing stock positions, LEAPS puts are the standard tool. A LEAPS put gives you the right to sell at a specific price, providing a "floor" for your position. The advantage over short-dated puts is the extended protection period with lower annualized cost. A 2-year LEAPS put might cost 8-10% of the stock price, providing 2 years of downside protection at an annualized cost of 4-5%.

**Q8: How does interest rate change affect LEAPS pricing?**

A: LEAPS are more sensitive to interest rates than short-dated options (they have higher rho). Rising interest rates increase call prices and decrease put prices. In the current high-rate environment, LEAPS calls are more expensive than they were when rates were near zero. Conversely, LEAPS puts are cheaper. This is because higher rates increase the cost of carry for the replicating portfolio (stock plus borrowing).

---

## YouTube Script

[VISUAL: Opening title card -- "Week 38: LEAPS and Long-Term Options" with a calendar showing months stretching into the future]

**Alex**: Welcome back. Last week we covered options leverage, and I mentioned that there is a way to get leverage with much less time pressure. That brings us to today's topic: LEAPS. Sam, have you heard of LEAPS before?

**Sam**: I know the acronym -- Long-Term Equity Anticipation Securities. They are just options with really long expiration dates, right? One to two years out?

**Alex**: That is the basic definition, yes. But they are much more than just "long options." LEAPS change the entire dynamic of how options work in your portfolio. The time factor -- which is usually the enemy of option buyers -- becomes much more manageable. Let me show you why that matters.

[VISUAL: Side-by-side comparison of theta decay curves for 30-day option vs 2-year LEAPS]

**Alex**: Look at these two theta decay curves. The 30-day option loses value rapidly -- almost half its value in the final two weeks. The 2-year LEAPS? It barely moves for the first year. The daily theta on a 2-year LEAPS is about one-fifth of a 30-day option of the same strike.

**Sam**: So the time decay is there, but it is slow enough that your thesis has time to play out.

**Alex**: Exactly. And that is the single biggest advantage. With short-dated options, you need to be right about direction AND timing. With LEAPS, timing becomes much less critical. If you believe NVIDIA will benefit from AI spending over the next 18 months, a LEAPS call lets you express that view without needing NVIDIA to rally next week.

[ANIMATION: animation/week38_leaps_decay.py -- Animated visualization of theta decay over time for options at different expirations. The animation starts with four option premium bars representing 3-month, 6-month, 12-month, and 24-month options. A simulated clock advances day by day. As time passes, each bar shrinks at its own rate -- the 3-month option shrinks rapidly and hits zero quickly, the 6-month follows, while the 12-month and 24-month bars barely move initially. The animation clearly shows the non-linear acceleration of theta decay, with the curve steepening dramatically in the final 60-90 days. Key milestones are labeled: "theta begins accelerating" at 90 days, "danger zone" at 30 days.]

**Sam**: That animation makes it so clear. The decay is almost invisible for the 2-year option during the first year. It is the final few months where things get aggressive.

**Alex**: Right, and that is why LEAPS traders have a critical rule: roll your LEAPS when they reach six to nine months to expiration. You want to exit before that steep part of the curve.

**Sam**: Got it. So what are the main ways people use LEAPS?

**Alex**: There are three primary strategies. The first and most important is stock replacement.

[VISUAL: Slide titled "Deep ITM LEAPS as Stock Replacement"]

**Alex**: The idea is simple. Instead of buying 100 shares of Apple at $185 for $18,500, you buy a deep in-the-money LEAPS call -- say a $140 strike call expiring in two years -- for about $52 per share, or $5,200.

**Sam**: That is 72% less capital. But how closely does it track the stock?

**Alex**: With a delta of 0.88, it moves 88 cents for every dollar Apple moves. It is not a perfect substitute, but it is close. And here is the key math.

[VISUAL: Comparison table showing stock vs LEAPS returns at various Apple price points]

**Alex**: If Apple goes to $220, a 19% gain, your stock position makes $3,500. Your LEAPS makes about $2,800. Less in absolute dollars, but that is a 54% return on $5,200 of capital. Meanwhile, you had $13,300 freed up. Put that in Treasury bills at 4.5% and you earn another $600 a year.

**Sam**: So the LEAPS gives me most of the upside, uses way less capital, and the freed capital earns a return. What is the catch?

**Alex**: Several catches. First, you miss dividends. Apple pays about $100 a year on 100 shares -- small for Apple, but it can be significant for higher-yielding stocks. Second, if Apple drops, you lose a higher percentage on the LEAPS than on the stock, because of leverage. And third, there is the extrinsic value -- the $7 per share of time premium. That decays over time.

**Sam**: How much does that extrinsic value matter?

**Alex**: Let us calculate it. Seven dollars per share of extrinsic value over two years is $3.50 per year, or about 1.9% of the stock price annually. If you compare that to margin interest -- which is 5-8% per year -- it is actually quite reasonable. And if the freed capital earns 4.5%, you are more than covering the extrinsic value cost.

[VISUAL: Cost comparison chart -- LEAPS extrinsic value vs margin interest vs freed capital return]

**Sam**: That makes sense in a high interest rate environment. What about when rates are low?

**Alex**: Great question. When rates were near zero in 2020-2021, the LEAPS strategy was less attractive because the freed capital earned nothing. The break-even interest rate for this to work is roughly the extrinsic value cost plus missed dividends divided by the freed capital. For most stocks, that is around 3-4%. Below that, just buy the stock.

**Sam**: OK, let us talk about the second strategy. You mentioned the "poor man's covered call."

**Alex**: Yes, this is one of my favorite strategies.

[VISUAL: Diagram showing PMCC structure -- long deep ITM LEAPS plus short near-term OTM call]

**Alex**: A traditional covered call requires you to buy 100 shares and sell a call against it. On Microsoft at $400, that is $40,000 of capital to generate maybe $600 per month in premium. The poor man's covered call replaces the stock with a deep ITM LEAPS.

**Sam**: So instead of $40,000 in stock, I buy a LEAPS for maybe $7,000 to $8,000?

**Alex**: Exactly. You buy a $340 strike LEAPS call for $72 per share -- $7,200 total. Then you sell the same monthly $410 call for $6, collecting $600 per month. Same income, but on $7,200 of capital instead of $40,000.

**Sam**: That is the same $600 monthly income on 82% less capital. The return on capital jumps from 1.5% per month to over 8% per month!

**Alex**: In percentage terms, yes. But I need to be careful here because the risk profile is different.

[VISUAL: Risk comparison for traditional CC vs PMCC]

**Alex**: With the traditional covered call, if Microsoft drops 30%, you lose about $12,000 on the stock minus the premiums collected. Your position still exists -- you still own the shares. With the PMCC, if Microsoft drops 30%, your LEAPS might lose 70-80% of its value. The position could be nearly wiped out.

**Sam**: So the higher percentage returns come with higher percentage risk.

**Alex**: Exactly. The PMCC is more capital-efficient but not inherently safer. You need to be comfortable with the idea that your LEAPS can lose most of its value in a severe downturn.

**Sam**: How do you manage it on an ongoing basis?

**Alex**: There are three key management actions.

[VISUAL: Three management pillars for PMCC]

**Alex**: First, managing the short call. If the stock rallies and your short call goes in-the-money, you roll it up and out -- close the current one, open a new one at a higher strike with a later expiration, ideally for a credit.

**Sam**: What if I cannot roll for a credit?

**Alex**: Then you have two choices. Take the assignment -- close the LEAPS and the short call simultaneously, locking in the maximum profit of the spread. Or roll for a small debit if you still want the position. Never roll for a large debit -- that destroys the income strategy's economics.

**Alex**: Second management action: rolling the LEAPS. When the LEAPS reaches six to nine months to expiration, you sell it and buy a new one further out. You want to do this before theta accelerates.

**Sam**: And the third?

**Alex**: Adjusting strike width. If the stock has moved significantly, your LEAPS might be very deep ITM or moving toward ATM. If it is getting too close to ATM, consider rolling to a deeper strike to maintain the stock-like characteristics.

**Sam**: Let us talk about selecting the right LEAPS. How do I choose the strike and expiration?

[VISUAL: LEAPS selection decision tree]

**Alex**: For stock replacement, your target delta is 0.80 to 0.90. This usually means a strike 15-25% below the current stock price. Go deeper and you are paying too much (nearly stock price). Go shallower and you are getting too much leverage and extrinsic value.

**Sam**: And for expiration?

**Alex**: Always buy the longest available expiration. Time value is not linear -- a two-year LEAPS does not cost twice as much extrinsic value as a one-year. The per-day cost of time is lower the longer you go. This means buying a two-year LEAPS and rolling once is cheaper than buying two consecutive one-year LEAPS.

[VISUAL: Chart comparing extrinsic value per day for different expirations]

**Sam**: That is an important insight. Let me make sure I understand. If a 1-year LEAPS has $7 of extrinsic value and a 2-year has $10, I am paying $10 for two years versus $14 for two consecutive 1-year positions. I save $4.

**Alex**: Exactly. That $4 savings is real money, especially when you are rolling positions year after year. Over a decade of stock replacement using LEAPS, the savings from buying longer duration add up to many thousands of dollars.

**Sam**: What about LEAPS on ETFs? Is that a good idea?

**Alex**: LEAPS on broad market ETFs like SPY and QQQ are one of my favorite applications.

[VISUAL: LEAPS on SPY example with capital allocation diagram]

**Alex**: Consider this. You want $100,000 of S&P 500 exposure. You can buy 200 shares of SPY at $500 each. Or you can buy 2 deep ITM LEAPS calls for about $19,000 and invest the remaining $81,000 in Treasury bills.

**Sam**: And the math works because...

**Alex**: The LEAPS costs about $3,000 in extrinsic value over two years, or $1,500 per year. You miss about $1,400 in dividends per year. Total cost: $2,900 per year. But $81,000 in T-bills at 4.5% earns $3,645 per year. You are actually ahead by $745 per year.

**Sam**: So in a high-rate environment, LEAPS on SPY actually make you money compared to owning the ETF outright?

**Alex**: Yes, with the caveat that you have slightly less upside capture (delta 0.85 instead of 1.00) and you have to manage the position -- rolling, monitoring, paying attention to bid-ask spreads. It is not truly passive like owning SPY.

**Sam**: What about the tax angle?

[VISUAL: Tax comparison slide]

**Alex**: Big advantage for LEAPS. If you hold a LEAPS for more than 12 months, the gain qualifies for long-term capital gains treatment. Currently that is 20% versus 37% for short-term gains. On a $5,000 profit, that is $850 more in your pocket after taxes with LEAPS.

**Sam**: That is a significant difference. Buy a 2-year LEAPS, hold it for 13 months, sell it, and you get the favorable tax rate.

**Alex**: Exactly. And this is another reason to buy the longest duration available. It gives you more time to qualify for long-term capital gains.

**Sam**: What are the biggest mistakes people make with LEAPS?

**Alex**: Let me give you the top five.

[VISUAL: "Top 5 LEAPS Mistakes" list appearing one by one]

**Alex**: Number one: buying ATM LEAPS for stock replacement. This is wrong because all the premium is extrinsic value. You want deep ITM so most of your premium is intrinsic and will not decay.

**Sam**: Because intrinsic value is real value -- it does not evaporate with time.

**Alex**: Exactly. Number two: forgetting to roll. Traders buy a 2-year LEAPS, put it in their portfolio, and forget about it. Eighteen months later, it is a 6-month option with rapidly accelerating theta. Set calendar reminders.

**Alex**: Number three: ignoring implied volatility when buying. LEAPS have high vega, meaning they are very sensitive to IV changes. If you buy when IV is elevated -- say after a market crash when VIX is at 35 -- you are overpaying. When IV normalizes, your LEAPS loses value from vega even if the stock goes up.

**Sam**: So I should buy LEAPS when IV is low?

**Alex**: Ideally, yes. Or at least be aware of the IV environment. Check the IV rank or IV percentile before buying.

**Alex**: Number four: over-leveraging. Just because LEAPS give you leverage does not mean you should lever up your entire portfolio. Use LEAPS to replace stock positions you would hold anyway, not to speculate with five times more exposure than you would normally take.

**Sam**: And number five?

**Alex**: Treating LEAPS as if they were stock. They are not. They expire. They have time decay. They do not pay dividends. They can lose 100% of their value. Always have a management plan: when will you roll, when will you close, what are your exit criteria?

**Sam**: This has been incredibly informative. LEAPS seem like a genuinely useful tool for long-term investors who understand the trade-offs.

**Alex**: They are. But the key word there is "understand." Do not use LEAPS until you can explain the extrinsic value cost, the rolling mechanics, and the risk profile. Paper trade a few positions first. Track them for a few months. Then start small with real capital.

[VISUAL: Summary slide with three key takeaways]

**Sam**: Before we wrap up, can we walk through a real LEAPS management scenario from start to finish? I think that would really solidify the concepts.

**Alex**: Great idea. Let us trace a full lifecycle.

[VISUAL: Timeline graphic showing LEAPS lifecycle over 18 months]

**Alex**: January 2025. You decide to use a LEAPS to get exposure to Amazon, which is trading at $190. You buy a $150 strike call expiring in January 2027 -- that is 24 months out. Premium is $52 per share. Delta is 0.84.

**Sam**: So $5,200 total investment. Intrinsic value is $40, extrinsic is $12.

**Alex**: Correct. Your breakeven at expiration is $202. But remember, you plan to manage this actively, not hold to expiration.

**Sam**: What happens in month three?

**Alex**: March 2025. Amazon has risen to $205. Your LEAPS is now worth $62. That is $10 of profit, a 19% return in three months. The stock moved 7.9%, so you captured about 2.4x the stock's return on a percentage basis. Your delta is now 0.89 -- deeper ITM. Everything is working.

**Sam**: Do you take profits?

**Alex**: Not yet. Your thesis was for Amazon to appreciate over 12-18 months. Three months is too early to exit unless you have a specific reason to doubt the thesis.

**Sam**: OK, month six.

**Alex**: June 2025. Amazon has pulled back to $185. Your LEAPS is now worth $44. You are down $8 from your purchase price, a 15% loss. Delta has dropped to 0.78.

[VISUAL: P&L chart showing the fluctuation]

**Sam**: That 2.6% stock decline turned into a 15% LEAPS decline. The leverage is working against me now.

**Alex**: Yes, but notice -- your LEAPS still has 18 months of life, plenty of time for the thesis to play out. If you had bought a 3-month option in January, it would be expiring right now with the stock below your breakeven. You would have lost most of your investment. The time buffer is saving you.

**Sam**: What about month twelve? That is when rolling becomes relevant, right?

**Alex**: January 2026. Amazon is at $210. Your LEAPS, now with 12 months to expiration, is worth $67. Profit: $15 per share, 29% return. Delta is 0.90. But here is where you need to start thinking about the roll.

**Sam**: Why? You said roll at six to nine months.

**Alex**: True, but I also want to highlight the tax angle. You have now held the LEAPS for 12 months. If you sell now, your $1,500 profit qualifies for long-term capital gains -- 20% tax rate instead of 37%. That is $255 saved versus selling at month eleven.

[VISUAL: Tax calendar showing 12-month threshold]

**Sam**: So the ideal window is: hold past 12 months for tax purposes, but roll before 6 months to expiration for theta purposes.

**Alex**: You have got it. In this case, you have months 12 through 18 as your sweet spot for rolling. Let us say you decide to roll in month 15 -- April 2026. Amazon is at $215. Your current LEAPS, now with 9 months left, is worth $70. You sell it for $7,000.

**Sam**: And buy a new one?

**Alex**: You buy a new January 2028 LEAPS, $170 strike, for $58 per share -- $5,800. This one has delta 0.86, 22 months to expiration, and puts you right back in the optimal zone.

[VISUAL: Roll transaction summary showing sale and purchase]

**Alex**: Your net cash flow on the roll: +$7,000 from selling minus $5,800 for buying equals $1,200 in your pocket. Plus you captured the long-term capital gain on the original position. And you now have a fresh LEAPS with low theta decay and plenty of time.

**Sam**: That is a beautiful illustration of the full lifecycle. The discipline of rolling, the tax planning, the theta management -- it all comes together.

**Alex**: And this is why I say LEAPS are not set-and-forget. They reward active, thoughtful management. The investor who does this well captures most of the stock's upside with a fraction of the capital, pays reasonable costs for the leverage, and maintains defined risk throughout.

**Sam**: One more question. What if Amazon had dropped to $140 instead? Below the strike price?

**Alex**: That is the nightmare scenario. Your LEAPS would be out of the money. With 12 months to expiration, it might still be worth $8-12 depending on IV. Your loss would be about $40-44 per share, or $4,000-4,400 -- a 77-85% loss on the LEAPS.

**Sam**: Compared to a stock loss of $50 per share, or $5,000.

**Alex**: Right. You lost less in dollar terms with the LEAPS ($4,400 max versus $5,000 on stock), and your loss was capped -- it could not get worse than $5,200, your total premium. Meanwhile, the stock could have dropped to $100 for a $9,000 loss. The LEAPS floor saved you from the worst outcomes. But the percentage loss was devastating, which is the leverage at work.

**Sam**: So even in the worst case, the LEAPS framework holds up -- you lose less in dollars, more in percentage, but your risk was defined from day one.

**Alex**: Exactly. That is the trade-off, and it is a trade-off you should make consciously before entering the position.

**Sam**: Can you give us the three key takeaways?

**Alex**: One: LEAPS are a capital-efficient alternative to stock ownership, not a replacement. They have costs and risks that stocks do not. Two: For stock replacement, use deep ITM LEAPS with delta 0.80 or higher. Most of your premium should be intrinsic value. Three: Always roll at six to nine months before expiration, and always have a management plan.

**Sam**: Perfect. Next week, we are shifting gears to a completely different market -- futures. See you then!

[VISUAL: End card -- "Next Week: Week 39 -- Futures Markets Introduction"]

---

*End of Week 38*
