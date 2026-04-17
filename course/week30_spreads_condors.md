# Week 30: Spreads and Condors - Defined-Risk Options Strategies

## Reading Section

### a) Why This Is Important

In the previous weeks, you learned single-leg options strategies: buying calls or puts, selling covered calls, and selling cash-secured puts. These are powerful tools, but they have limitations. A covered call requires owning 100 shares of stock. A cash-secured put requires setting aside the full cash to purchase shares. Both demand significant capital.

**Spreads solve the capital problem.** By combining two or more options into a single position, you can create trades that require far less capital while having clearly defined maximum profit and maximum loss. This is why spreads are the backbone of professional options trading.

**Why learning spreads and condors is critical:**

**1. Defined risk changes everything.** When you sell a naked put, your maximum loss is the strike price times 100 (if the stock goes to zero). With a put spread, your maximum loss is the difference between strikes minus the premium received, typically a small fraction of the naked put risk. This means you can participate in options selling with a fraction of the capital and a fraction of the risk. A trade that might require $15,000 in cash for a cash-secured put can be replicated for $500-$1,000 with a spread.

**2. Spreads allow you to express nuanced market views.** Single-leg options are blunt instruments: you are bullish, bearish, or neutral. Spreads let you express views like "I think the stock will stay between $140 and $160 for the next 30 days" or "I think the stock will go up but not past $165" or "I expect volatility to decrease." These precise views can be translated into precisely structured positions.

**3. Iron condors are the quintessential income strategy.** An iron condor profits when the stock stays within a range. In a market that spends roughly 70-80% of its time in consolidation, this is a strategy that aligns with the natural tendency of prices. Many full-time options traders use iron condors as their primary income vehicle, consistently generating 3-8% per month on capital deployed.

**4. Spread analysis relies on the Greeks.** This lesson builds directly on Week 29. You will see how combining options with different strikes and types creates positions with customized Greek profiles. Understanding delta, theta, vega, and gamma at the spread level is what separates competent options traders from beginners.

**5. Spreads are the building blocks of advanced strategies.** Butterflies, calendars, diagonals, ratio spreads, and virtually every advanced options strategy is built from the basic spreads you will learn today. Master vertical spreads and iron condors, and you have the foundation for everything that follows.

---

### b) What You Need to Know

#### What Is a Spread?

A spread is a position created by simultaneously buying one option and selling another option on the same underlying stock. The options differ in strike price, expiration date, or both. By combining a long and short option, you create a position with limited risk and limited profit potential.

```
SPREAD = BUY one option + SELL another option
         (same underlying, same expiration for vertical spreads)

WHY SPREADS EXIST:

  Single Option:  Unlimited profit potential, limited or large risk
  Spread:         Limited profit potential, LIMITED RISK

  The trade-off: You give up unlimited upside/downside
  in exchange for defined, manageable risk.
```

#### Vertical Spreads: The Foundation

A **vertical spread** uses two options with the same expiration date but different strike prices. There are four types:

```
THE FOUR VERTICAL SPREADS:

  +-----------------------------------------------------------+
  |                     BULLISH                                |
  |                                                           |
  |  Bull Call Spread (DEBIT)    Bull Put Spread (CREDIT)     |
  |  Buy lower strike call      Sell higher strike put        |
  |  Sell higher strike call    Buy lower strike put          |
  |  You PAY net premium        You RECEIVE net premium       |
  |  Profit if stock RISES      Profit if stock stays UP      |
  +-----------------------------------------------------------+
  |                     BEARISH                                |
  |                                                           |
  |  Bear Put Spread (DEBIT)    Bear Call Spread (CREDIT)     |
  |  Buy higher strike put      Sell lower strike call        |
  |  Sell lower strike put      Buy higher strike call        |
  |  You PAY net premium        You RECEIVE net premium       |
  |  Profit if stock FALLS      Profit if stock stays DOWN    |
  +-----------------------------------------------------------+
```

#### Debit Spreads vs. Credit Spreads

The distinction between debit and credit spreads is fundamental:

**Debit Spread:** You pay money to enter the trade. Your maximum profit occurs when both options expire in the money. You profit from a directional move.

**Credit Spread:** You receive money to enter the trade. Your maximum profit occurs when both options expire out of the money. You profit from the stock staying away from your short strike.

```
DEBIT vs. CREDIT SPREADS:

                    DEBIT SPREAD              CREDIT SPREAD
  Entry Cost:       You PAY premium           You RECEIVE premium
  Max Profit:       Width - Premium Paid      Premium Received
  Max Loss:         Premium Paid              Width - Premium Received
  Profit When:      Stock moves your way      Stock stays away
  Theta Effect:     NEGATIVE (hurts you)      POSITIVE (helps you)
  Probability:      Typically < 50%           Typically > 50%
  Risk/Reward:      Higher reward, lower      Lower reward, higher
                    probability               probability

  Width = Difference between strike prices

  Example: Bull Call Spread on AAPL at $150

  DEBIT (Bull Call Spread):         CREDIT (Bull Put Spread):
  Buy $150 Call: -$5.00             Sell $150 Put: +$5.00
  Sell $155 Call: +$2.50            Buy $145 Put: -$2.50
  Net: PAY $2.50                    Net: RECEIVE $2.50
  Max Profit: $5 - $2.50 = $2.50   Max Profit: $2.50
  Max Loss: $2.50                   Max Loss: $5 - $2.50 = $2.50
```

#### Bull Call Spread (Debit Call Spread)

The bull call spread is the simplest directional spread. You buy a call at a lower strike and sell a call at a higher strike.

```
BULL CALL SPREAD EXAMPLE:

  AAPL at $150. You are moderately bullish.

  Buy 1 AAPL $150 Call (30 days): Pay $5.00
  Sell 1 AAPL $155 Call (30 days): Receive $2.50
  Net Debit: $2.50 per share ($250 per spread)

  Max Profit: ($155 - $150) - $2.50 = $2.50/share ($250)
  Max Loss:   $2.50/share ($250)
  Breakeven:  $150 + $2.50 = $152.50

  PAYOFF DIAGRAM AT EXPIRATION:

  P&L
  +$250 |                          ___________________
        |                     ____/
     $0 |_________________ __/
        |                 |
  -$250 |_________________|
        +----+----+----+----+----+----+----+----
        $140 $142 $144 $146 $148 $150 $152 $155 $160
                              |         |
                           Buy Strike  Sell Strike
                              $150       $155

  Below $150: Both expire worthless. Lose full $250.
  $150-$155: Long call gains value, short call still OTM.
  Above $155: Both ITM. Max profit of $250 locked in.
```

```
GREEKS FOR BULL CALL SPREAD:

  Component          Delta   Gamma   Theta    Vega
  =================  ======  ======  ======   =====
  Long $150 Call     +0.50   +0.03   -$0.08   +$0.10
  Short $155 Call    -0.30   -0.02   +$0.06   -$0.08
  ===================================================
  NET SPREAD         +0.20   +0.01   -$0.02   +$0.02

  Interpretation:
  - Low delta (+0.20): Moderate directional exposure
  - Low gamma (+0.01): Delta is relatively stable
  - Low theta (-$0.02): Small daily cost ($2/day)
  - Low vega (+$0.02): Minor volatility sensitivity

  Compare to buying the $150 call alone:
  - Delta: +0.50 (2.5x more exposure)
  - Theta: -$0.08 ($8/day cost, 4x more expensive)
  - Max loss: $5.00 (2x more risk)

  The spread REDUCES everything: exposure, cost, and risk.
```

#### Bear Put Spread (Debit Put Spread)

The bear put spread is the bearish mirror of the bull call spread.

```
BEAR PUT SPREAD EXAMPLE:

  AAPL at $150. You are moderately bearish.

  Buy 1 AAPL $150 Put (30 days): Pay $4.80
  Sell 1 AAPL $145 Put (30 days): Receive $2.30
  Net Debit: $2.50 per share ($250 per spread)

  Max Profit: ($150 - $145) - $2.50 = $2.50/share ($250)
  Max Loss:   $2.50/share ($250)
  Breakeven:  $150 - $2.50 = $147.50

  PAYOFF DIAGRAM AT EXPIRATION:

  P&L
  +$250 |___________________
        |                   \____
     $0 |                        \__  _________________
        |                           |
  -$250 |                           |_________________
        +----+----+----+----+----+----+----+----
        $138 $140 $142 $144 $146 $148 $150 $152 $155
                         |              |
                      Sell Strike    Buy Strike
                        $145           $150
```

#### Credit Spreads: Bull Put Spread and Bear Call Spread

Credit spreads are the income-generating versions of vertical spreads. Instead of paying to bet on direction, you collect premium and profit when the stock stays in your favor.

```
BULL PUT SPREAD (CREDIT) EXAMPLE:

  AAPL at $155. You are neutral to bullish.

  Sell 1 AAPL $150 Put (30 days): Receive $2.80
  Buy 1 AAPL $145 Put (30 days): Pay $1.30
  Net Credit: $1.50 per share ($150 per spread)

  Max Profit: $1.50/share ($150) - if AAPL stays above $150
  Max Loss:   ($150 - $145) - $1.50 = $3.50/share ($350)
  Breakeven:  $150 - $1.50 = $148.50

  PAYOFF DIAGRAM AT EXPIRATION:

  P&L
  +$150 |                          ___________________
        |                     ____/
     $0 |                ____/
        |           ____/
  -$350 |__________/
        +----+----+----+----+----+----+----+----
        $140 $142 $144 $146 $148 $150 $152 $155
                    |              |
                 Buy Strike    Sell Strike
                   $145          $150

  PROBABILITY ANALYSIS:
  Stock needs to stay above $148.50 for profit.
  Currently at $155, that is $6.50 (4.2%) of cushion.
  With delta of short put at 0.30, probability of
  profit is approximately 70%.
```

```
BEAR CALL SPREAD (CREDIT) EXAMPLE:

  AAPL at $155. You are neutral to bearish.

  Sell 1 AAPL $160 Call (30 days): Receive $2.00
  Buy 1 AAPL $165 Call (30 days): Pay $0.80
  Net Credit: $1.20 per share ($120 per spread)

  Max Profit: $1.20/share ($120) - if AAPL stays below $160
  Max Loss:   ($165 - $160) - $1.20 = $3.80/share ($380)
  Breakeven:  $160 + $1.20 = $161.20

  PAYOFF DIAGRAM AT EXPIRATION:

  P&L
  +$120 |___________________
        |                   \____
     $0 |                        \__
        |                           \____
  -$380 |                                \______________
        +----+----+----+----+----+----+----+----
        $150 $152 $155 $158 $160 $162 $164 $166
                              |              |
                           Sell Strike    Buy Strike
                             $160          $165
```

#### Capital Efficiency of Spreads

```
CAPITAL COMPARISON:

  Strategy                  Capital Required    Max Profit   Max Loss   ROI
  ========================  ================    ==========   ========   ====
  Cash-Secured Put $150     $15,000             $280         $15,000    1.9%
  Bull Put Spread           $350 (margin)       $150         $350       42.9%
    $150/$145

  100 Shares of Stock       $15,500             Unlimited    $15,500    n/a
  Bull Call Spread           $250                $250         $250       100%
    $150/$155

  NOTE: Spread returns look high but remember:
  - Cash-secured put has ~80% win rate, spread has ~70%
  - Spread max loss happens more frequently as % of capital
  - Capital efficiency must be weighed against win rate
  - Never risk more than 2-5% of portfolio on a single spread
```

#### The Iron Condor

An iron condor combines a bull put spread and a bear call spread on the same stock with the same expiration. It profits when the stock stays within a range.

```
IRON CONDOR STRUCTURE:

  An iron condor is TWO credit spreads:

  Bull Put Spread (below market):
    Sell Put at Strike B
    Buy Put at Strike A (lower, protection)

  Bear Call Spread (above market):
    Sell Call at Strike C
    Buy Call at Strike D (higher, protection)

  A < B < Current Price < C < D

  VISUAL:

                      Current Price
                           |
  Buy Put   Sell Put       |       Sell Call   Buy Call
    (A)       (B)          |         (C)         (D)
     |         |           |          |           |
     v         v           v          v           v
  ===|=========|===========|==========|===========|===
  $135       $140        $150       $160        $165
     <-------->                       <---------->
     Protection                       Protection
        Wing                             Wing
               <------------------------->
                   Profit Zone
```

```
IRON CONDOR EXAMPLE:

  AAPL at $150. You expect it to stay between $140 and $160.

  Bull Put Spread (downside):
    Sell 1 AAPL $140 Put:  Receive $1.20
    Buy 1 AAPL $135 Put:   Pay $0.50

  Bear Call Spread (upside):
    Sell 1 AAPL $160 Call:  Receive $1.00
    Buy 1 AAPL $165 Call:   Pay $0.30

  TOTAL Net Credit: $1.20 - $0.50 + $1.00 - $0.30 = $1.40/share
  Total Credit Received: $140 per iron condor

  Max Profit: $1.40/share ($140) - both spreads expire worthless
  Max Loss:   $5.00 - $1.40 = $3.60/share ($360) - one side breached
  Width:      $5.00 (difference between strikes in each spread)
  Breakeven (lower): $140 - $1.40 = $138.60
  Breakeven (upper): $160 + $1.40 = $161.40

  PAYOFF DIAGRAM AT EXPIRATION:

  P&L
  +$140 |              _________________________
        |         ____/                         \____
     $0 |    ____/                                   \____
        |___/                                             \___
  -$360 |                                                     |
        +----+----+----+----+----+----+----+----+----+----+----
        $130 $133 $136 $139 $142 $145 $148 $151 $154 $157 $160 $165
              |         |                        |         |
           Buy Put   Sell Put                Sell Call  Buy Call
            $135      $140                     $160      $165

  PROFIT ZONE: $138.60 to $161.40 (a $22.80 range)
  Stock needs to move less than 7.6% in either direction.
```

```
IRON CONDOR GREEKS:

  Component              Delta   Gamma   Theta    Vega
  =====================  ======  ======  ======   =====
  Short $140 Put         +0.18   -0.015  +$0.04   -$0.06
  Long $135 Put          -0.10   +0.010  -$0.02   +$0.04
  Short $160 Call        -0.15   -0.012  +$0.03   -$0.05
  Long $165 Call         +0.08   +0.008  -$0.02   +$0.03
  =======================================================
  NET IRON CONDOR        +0.01   -0.009  +$0.03   -$0.04

  Interpretation:
  - Delta near zero: Market neutral (this is the point!)
  - Negative gamma: Big moves in either direction hurt
  - Positive theta: Earning ~$3/day from time decay
  - Negative vega: Benefits from declining IV

  IDEAL CONDITIONS FOR IRON CONDORS:
  1. High IV (more premium to collect, and IV likely to fall)
  2. Range-bound market (stock staying between strikes)
  3. 30-45 days to expiration (optimal theta decay)
  4. No major catalysts expected (earnings, FDA, etc.)
```

#### Probability and Expected Value

Understanding probability is essential for spread trading.

```
PROBABILITY FRAMEWORK FOR CREDIT SPREADS:

  The short strike's delta approximates the probability
  of that strike being breached at expiration.

  Example: Iron Condor on AAPL at $150

  Short $140 Put:  Delta = 0.18 -> ~18% chance of breach
  Short $160 Call: Delta = 0.15 -> ~15% chance of breach

  Probability of EITHER side being breached:
    ~18% + ~15% = ~33% (approximately, assuming independence)

  Probability of profit (both sides expire OTM):
    ~67%

  EXPECTED VALUE CALCULATION:

  Win:  67% x $140 profit = +$93.80
  Lose: 33% x $360 loss   = -$118.80
  Expected Value per trade = -$25.00

  WAIT, THAT IS NEGATIVE?

  Yes, if you hold to expiration and never manage the position.
  But active management changes this dramatically.

  WITH ACTIVE MANAGEMENT (close at 50% profit, close at 2x loss):

  Adjusted win rate: ~78% (closing early captures more wins)
  Adjusted avg win:  $70 (50% of $140)
  Adjusted avg loss: $200 (closing at 2x loss before max loss)

  Win:  78% x $70  = +$54.60
  Lose: 22% x $200 = -$44.00
  Expected Value per trade = +$10.60

  MANAGEMENT IS WHAT MAKES IRON CONDORS PROFITABLE.
```

#### Managing Spread Trades

Management is the most important skill in spread trading. Here are the key rules.

```
MANAGEMENT RULES FOR CREDIT SPREADS AND IRON CONDORS:

  RULE 1: TAKE PROFITS EARLY
    - Close at 50% of max profit (e.g., sold for $1.40, buy back at $0.70)
    - Why? The last 50% of profit takes disproportionately more time
      and carries more risk. Closing early frees capital for new trades.
    - A trader who closes at 50% and redeploys capital can often
      make more than holding a single position to expiration.

  RULE 2: CUT LOSSES AT A PREDETERMINED LEVEL
    - Close if loss reaches 1.5x to 2x the credit received
    - Example: Received $1.40, close if spread is worth $2.80-$3.50
    - Never let a spread go to max loss. Max loss means you held
      through the worst possible outcome.

  RULE 3: CLOSE BEFORE EXPIRATION WEEK
    - Gamma risk makes the last week dangerous
    - Close or roll 7-10 days before expiration
    - The last 10% of profit is not worth the gamma risk

  RULE 4: DO NOT DEFEND LOSING POSITIONS BLINDLY
    - Rolling a losing spread can work, but only if the thesis
      (stock staying in range) is still intact.
    - If the stock has fundamentally broken out of your range,
      close the trade and accept the loss.
```

```
ROLLING A CREDIT SPREAD:

  Original Position:
    Sold AAPL $140/$135 Put Spread for $1.40
    15 days to expiration
    AAPL has dropped to $142 (threatening the $140 short strike)

  OPTION 1: Close for a loss
    Spread is now worth $2.50
    Loss: $2.50 - $1.40 = $1.10/share ($110 per spread)

  OPTION 2: Roll down and out
    Close current spread: Pay $2.50
    Open new spread 30 days out:
      Sell $138/$133 Put Spread: Receive $1.80
    Net debit to roll: $2.50 - $1.80 = $0.70
    Total at risk: $1.40 (original) + $0.70 (roll cost) = $2.10
    But now you have 30 more days and a lower short strike ($138)

  WHEN TO ROLL vs. WHEN TO CLOSE:

  Roll if:
    - Stock is near but not through your short strike
    - You can collect meaningful credit for the new position
    - Your original thesis (range-bound) still applies
    - IV has not collapsed (rolling into low-IV options is poor value)

  Close if:
    - Stock has blown through your short strike significantly
    - Your thesis is broken (trend has changed)
    - The roll does not provide meaningful credit improvement
    - You have already rolled once (avoid "rolling into a hole")
```

#### Position Sizing for Spreads

```
POSITION SIZING GUIDELINES:

  RULE: Never risk more than 2-5% of total portfolio on a
  single spread or iron condor.

  Example: $100,000 portfolio, 3% risk per trade

  Max risk per trade: $3,000

  Iron Condor max loss: $360 per condor

  Maximum contracts: $3,000 / $360 = 8 iron condors

  DIVERSIFICATION:
    - Spread risk across 3-5 different underlyings
    - Stagger entry dates (do not enter all at once)
    - Mix strike widths based on conviction
    - Keep total portfolio risk in spreads under 15-20%

  EXAMPLE ALLOCATION ($100,000 portfolio):

  Position                          Contracts   Max Risk   % of Port
  ================================  =========   ========   =========
  AAPL Iron Condor (30 days)        3           $1,080     1.1%
  SPY Iron Condor (45 days)         2           $720       0.7%
  MSFT Bull Put Spread (30 days)    4           $1,200     1.2%
  QQQ Bear Call Spread (30 days)    3           $960       1.0%
  ================================================================
  TOTAL                             12          $3,960     4.0%

  Remaining 96% of portfolio is in stocks, bonds, and cash.
  Options spreads are an income overlay, not the core portfolio.
```

#### Choosing Strike Width and Distance

```
STRIKE WIDTH COMPARISON ($5 vs. $10 vs. $20 width):

  AAPL at $150, 30 days, Bull Put Spread:

  $5 Width ($145/$140):
    Credit: $0.80    Max Loss: $4.20    ROC: 19%    Win Rate: ~75%
    Capital at risk per spread: $420

  $10 Width ($145/$135):
    Credit: $1.10    Max Loss: $8.90    ROC: 12%    Win Rate: ~75%
    Capital at risk per spread: $890

  $20 Width ($145/$125):
    Credit: $1.30    Max Loss: $18.70   ROC: 7%     Win Rate: ~75%
    Capital at risk per spread: $1,870

  OBSERVATIONS:
  - Narrower spreads have higher ROC (return on capital)
  - Wider spreads collect more total credit but lower ROC
  - Win rate is the same (determined by short strike, not width)
  - Narrower spreads reach max loss more quickly
  - For iron condors, $5 width is most common for retail traders

  RECOMMENDED: $5 width for accounts under $100,000
               $10 width for larger accounts or higher conviction
```

```
STRIKE DISTANCE (HOW FAR OTM):

  Probability   Short Strike Delta   Typical Distance OTM   Credit
  ===========   ==================   ====================   ======
  High win      0.10-0.15            12-18% OTM             Low
  Moderate      0.20-0.30            6-12% OTM              Moderate
  Aggressive    0.35-0.45            2-6% OTM               High

  SWEET SPOT: Short strike at delta 0.15-0.25 (10-15% OTM)
  Provides 70-80% probability of profit with reasonable premium.

  For iron condors, aim for short strikes at ~1 standard deviation
  from current price. Your brokerage platform can show you the
  expected move based on implied volatility.

  EXPECTED MOVE CALCULATION:

  Expected Move = Stock Price x IV x sqrt(DTE/365)

  Example: AAPL at $150, IV = 25%, 30 days
  Expected Move = $150 x 0.25 x sqrt(30/365)
                = $150 x 0.25 x 0.287
                = $10.76

  So the market expects AAPL to move about $10.76 in 30 days.
  Selling strikes at $140 put and $160 call places you near
  one standard deviation, which is breached about 32% of the time
  (16% on each side).
```

---

### c) Common Misconceptions

**Misconception 1: "Spreads are just for advanced traders."**

Spreads are actually safer than many single-leg strategies. A defined-risk spread has a known maximum loss before you enter the trade. Compare this to selling a naked put or owning stock, where losses can be dramatically larger. Spreads should be learned early in an options education, not treated as "advanced." They require a different approval level at most brokerages (typically Level 3), but the concepts are straightforward.

**Misconception 2: "Iron condors are a guaranteed income strategy."**

No options strategy guarantees income. Iron condors have high win rates (65-80%) but the losses when they occur are typically larger than the wins. A single bad month can erase several months of gains. The key is proper position sizing (never more than 2-5% risk per trade) and active management (taking profits early and cutting losses). Without discipline, iron condors can produce devastating drawdowns.

**Misconception 3: "Wider spreads are always better because you collect more premium."**

Wider spreads collect more total premium but have lower return on capital and reach max loss in the same scenarios. A $10-wide spread is not twice as profitable as a $5-wide spread; it simply uses more capital for incrementally more premium. For most retail traders, $5-wide spreads provide the best balance of capital efficiency and manageable risk.

**Misconception 4: "I should always hold my spreads to expiration to capture the full credit."**

This is one of the most common and costly mistakes. Research from options analytics firms consistently shows that closing credit spreads at 50% of maximum profit and redeploying capital produces better risk-adjusted returns than holding to expiration. Holding the last 50% of profit exposes you to rapidly increasing gamma risk for diminishing reward.

**Misconception 5: "Credit spreads are always better than debit spreads."**

Neither is inherently better. Credit spreads benefit from time decay and have higher probability but lower reward-to-risk. Debit spreads cost money but profit from directional moves. The choice depends on your market outlook. In high-IV environments, credit spreads are typically favored. In low-IV environments or with a strong directional conviction, debit spreads can be more efficient.

**Misconception 6: "If both legs of my spread expire out of the money, I always keep the full credit."**

This is true if both legs expire truly OTM. But beware of "pin risk" near expiration. If the stock closes right at your short strike, you may be assigned on the short leg while the long leg expires worthless. This leaves you with an unwanted stock position. To avoid this, close spreads before expiration, even if they are near worthless.

---

### d) Q&A

**Q: What brokerage approval level do I need to trade spreads?**

A: Most brokerages require Level 3 options approval for defined-risk spreads (vertical spreads and iron condors). This typically requires some options trading experience, a margin account, and answering questions about your options knowledge. The approval process varies by broker. Fidelity, Schwab, TD Ameritrade, and Interactive Brokers all offer spread trading with appropriate approval. If you have been trading covered calls and cash-secured puts (Levels 1-2), upgrading to Level 3 is usually straightforward.

**Q: How much capital do I need to start trading spreads?**

A: Technically, you can trade a single $5-wide spread with as little as $500 in margin. However, a more practical minimum is $10,000-$25,000. This allows you to diversify across multiple positions while keeping each trade under 5% of your capital. With $25,000, you could comfortably run 5-8 iron condors across different underlyings and expirations.

**Q: Should I trade iron condors on individual stocks or on indexes like SPY?**

A: Both work, but index options (SPY, QQQ, IWM) have advantages. They are more liquid, have tighter bid-ask spreads, cannot gap as dramatically as individual stocks (no single-stock earnings risk), and qualify for favorable 60/40 tax treatment if you use SPX options. Many professional iron condor traders focus exclusively on SPX or SPY. Individual stocks can work but carry event risk (earnings, FDA decisions, etc.) that can blow through strikes overnight.

**Q: What happens if one side of my iron condor is breached?**

A: If the stock moves through one of your short strikes, that side of the iron condor is in danger. The other side is now deeply out of the money and nearly worthless, which is good. Your options are: (1) Close the entire iron condor and take the loss. (2) Close only the threatened side and let the profitable side continue. (3) Roll the threatened side further out in time or further out of the money. Option 2 is common: close the losing side, and the winning side's remaining credit partially offsets your loss.

**Q: How do I calculate my return on capital for a spread?**

A: Return on capital (ROC) for a credit spread is: Credit Received divided by Max Loss. For a $5-wide bull put spread that collects $1.50, max loss is $3.50, and ROC is $1.50/$3.50 = 42.9%. If you close at 50% profit ($0.75), your actual ROC is $0.75/$3.50 = 21.4%. To annualize, divide by the number of days held and multiply by 365. If you held for 20 days: 21.4% x (365/20) = 390% annualized. These percentages sound high but remember, they apply only to the small amount of capital at risk, not your entire portfolio.

**Q: Can I leg into a spread, buying one side first and selling the other later?**

A: You can, but it is generally not recommended for beginners. Legging in exposes you to execution risk. If you buy the long option and the stock moves before you can sell the short option, you may get a worse price on the spread. Most brokerage platforms allow you to enter spreads as a single order, which guarantees you get both legs filled at your desired net price. Use the spread order functionality.

**Q: How many iron condors should I have on at one time?**

A: For a typical retail account ($50,000-$200,000), 3-5 iron condor positions at any given time is reasonable. Diversify across different underlyings and stagger entry dates by one to two weeks. This ensures you do not have all positions expiring at the same time and reduces correlation risk. Total capital at risk in iron condors should not exceed 15-20% of your portfolio.

---

## YouTube Script

[VISUAL: Animated intro with show logo. Text: "Week 30: Spreads and Condors - Level 3: Advanced"]

**Horace:** Welcome back. Last week we learned the option Greeks. This week we are going to use those Greeks to build more sophisticated options positions. We are talking about spreads and iron condors.

**Stella:** This is exciting because one of the limitations of covered calls and cash-secured puts is the capital requirement. You need to own 100 shares or set aside $14,000 in cash. Spreads seem like they can do similar things with much less capital.

**Horace:** That is exactly right. A cash-secured put on Apple might require $15,000 in capital. A put spread on Apple might require $350. You achieve similar economic exposure with a fraction of the capital. And more importantly, your maximum loss is defined before you enter the trade.

[VISUAL: Side-by-side comparison. Left: "Cash-Secured Put" showing $15,000 capital, $280 max profit, $15,000 max loss. Right: "Bull Put Spread" showing $350 capital, $150 max profit, $350 max loss. Annotation: "27x less capital required."]

**Stella:** Let us start with the basics. What exactly is a spread?

**Horace:** A spread is simply buying one option and selling another option on the same stock. By combining a long and short option, you create a position where both your profit and your loss are limited. The two options partially offset each other.

**Stella:** And there are different types of spreads?

**Horace:** There are four basic vertical spreads. A vertical spread means both options have the same expiration but different strike prices. You have the bull call spread, the bear put spread, the bull put spread, and the bear call spread. The first two are debit spreads where you pay money to enter. The second two are credit spreads where you receive money to enter.

[VISUAL: A 2x2 grid. Columns: "Debit (You Pay)" and "Credit (You Receive)". Rows: "Bullish" and "Bearish". Bull Call Spread in top-left, Bull Put Spread in top-right, Bear Put Spread in bottom-left, Bear Call Spread in bottom-right]

**Stella:** Let us walk through a bull call spread first since it is the most intuitive.

**Horace:** Sure. Let us say Apple is at $150 and you are moderately bullish. You buy the $150 call for $5.00 and you sell the $155 call for $2.50. Your net cost is $2.50 per share, or $250 per spread. That is your maximum loss. Your maximum profit is the difference between the strikes, $5.00, minus what you paid, $2.50, which equals $2.50 per share or $250.

[ANIMATION: Reference animation/week30_spread_payoff.py - Building a spread payoff diagram step by step. First, the long call payoff line appears (the classic hockey stick shape starting at -$500 at $150 and rising after $150). Then the short call payoff appears (inverted hockey stick starting at +$250 at $155). Finally, the two are combined into the spread payoff, which shows the characteristic shape: flat at -$250 below $150, rising between $150 and $155, and flat at +$250 above $155.]

**Stella:** So my maximum risk is the $250 I paid, and no matter how high Apple goes, I can only make $250?

**Horace:** Correct. You have capped both your downside and your upside. The breakeven is $152.50, which is the lower strike plus the premium paid. Below $150, you lose the full $250. Between $150 and $155, your profit increases linearly. Above $155, you keep the maximum $250.

**Stella:** And how does this compare to just buying the $150 call outright?

**Horace:** Great question. If you just bought the $150 call for $5.00, your maximum loss is $500, and your profit potential is unlimited. The spread costs $250 instead of $500, so you risk half as much. But you give up anything above $155. The spread is more capital efficient but has a capped reward.

[VISUAL: Two payoff diagrams overlaid. Solid line: Bull Call Spread, showing the characteristic capped shape. Dashed line: Long Call alone, showing unlimited upside. The area between them above $155 is shaded and labeled "Upside you give up in exchange for lower cost and lower risk"]

**Stella:** Now let us talk about credit spreads. These are the income-generating version, right?

**Horace:** Exactly. With a credit spread, you receive money upfront and your goal is for both options to expire worthless. Let me walk through a bull put spread. Apple is at $155. You sell the $150 put for $2.80 and buy the $145 put for $1.30. You receive a net credit of $1.50 per share, or $150 per spread.

**Stella:** So I get paid $150 to enter the trade. What are the outcomes?

**Horace:** If Apple stays above $150 at expiration, both puts expire worthless and you keep the entire $150. That is your maximum profit. If Apple drops below $145, you hit maximum loss: the $5.00 width minus the $1.50 credit, which is $3.50 per share or $350 per spread. In between, there is a breakeven at $148.50.

[VISUAL: Bull put spread payoff diagram with annotations. Flat line at +$150 above $150. Diagonal line from $150 to $145. Flat line at -$350 below $145. Breakeven marked at $148.50. Annotations: "AAPL currently at $155 - you have $6.50 of cushion"]

**Stella:** So I need Apple to stay above $148.50 to profit. And it is currently at $155. That seems very doable.

**Horace:** And that is the appeal of credit spreads. You do not need the stock to go up. You just need it to not go down too much. The probability of profit is around 70% for this trade, based on the delta of the short strike.

**Stella:** Now let us get to the star of the show. The iron condor.

**Horace:** The iron condor is simply a bull put spread and a bear call spread on the same stock, same expiration. You are selling premium on both sides, betting that the stock stays within a range.

[ANIMATION: Reference animation/week30_iron_condor_build.py - Building an iron condor step by step. First, a stock price at $150 with a number line. Then the bull put spread appears below: sell $140 put and buy $135 put, with the payoff shape shown below the line. Then the bear call spread appears above: sell $160 call and buy $165 call, with the payoff shape shown above the line. Finally, both are combined into the complete iron condor payoff, showing the characteristic "table top" shape: loss zones on both ends, profit plateau in the middle.]

**Stella:** Walk me through a specific example.

**Horace:** Apple is at $150. On the downside, I sell the $140 put for $1.20 and buy the $135 put for $0.50. On the upside, I sell the $160 call for $1.00 and buy the $165 call for $0.30. Total credit received: $1.40 per share, or $140 per iron condor.

**Stella:** And the maximum loss?

**Horace:** The maximum loss is the width of one spread, $5.00, minus the total credit, $1.40, which equals $3.60 per share or $360. This happens if Apple drops below $135 or rises above $165 at expiration.

**Stella:** What is the profit zone?

**Horace:** The profit zone is between the two breakevens. Lower breakeven is $140 minus $1.40, which is $138.60. Upper breakeven is $160 plus $1.40, which is $161.40. So Apple needs to stay between $138.60 and $161.40. That is a $22.80 range, or about 7.6% in either direction from the current price.

[VISUAL: The classic iron condor payoff diagram with the profit zone highlighted in green. The current stock price at $150 is marked in the center. Below the diagram, text shows: "Profit Zone: $138.60 to $161.40 (15.2% total range)" and "Probability of Profit: ~67%"]

**Stella:** Let us look at the Greeks for this iron condor, because that connects to what we learned last week.

**Horace:** Great idea. The iron condor has near-zero delta, which means it is market neutral. It does not care if the stock goes up or down a little. It has negative gamma, which means big moves in either direction hurt. It has positive theta, meaning you earn money every day from time decay. And it has negative vega, meaning you benefit when implied volatility decreases.

[VISUAL: Greek dashboard for the iron condor. Delta: +0.01 (nearly zero, with a green checkmark). Gamma: -0.009 (with a caution symbol). Theta: +$3/day (with a dollar sign icon). Vega: -$4 per 1% IV (with a down-arrow icon). Commentary below each: "Market neutral", "Big moves hurt", "Earns $3/day", "Lower IV helps"]

**Stella:** So it is basically a bet that things stay boring?

**Horace:** That is a perfect way to describe it. And here is the thing: markets are boring most of the time. Stocks spend roughly 70 to 80% of their time in consolidation ranges. The iron condor is designed to profit during those boring periods.

**Stella:** OK, now here is the critical question. How do we manage these positions? Because I know from the reading that management is what separates profitable condor traders from losing ones.

**Horace:** This is the most important part of the entire lesson. Rule number one: take profits early. When your iron condor has captured 50% of the maximum profit, close it. Do not wait for the remaining 50%.

**Stella:** Why not? If it is working, why not let it run?

**Horace:** Because the risk-reward flips. In the first half of the trade, you are capturing $70 of profit while risking a $360 max loss. Once you have captured $70, you are now risking $360 to make an additional $70. The last 50% of profit takes disproportionately longer and exposes you to increasing gamma risk as expiration approaches.

[VISUAL: A risk/reward timeline. Left side "Day 1-15" showing "Earning $70 profit" with low risk meter. Right side "Day 15-30" showing "Earning final $70" with high risk meter. Arrow pointing to day 15 saying "Close here for optimal risk-adjusted return"]

**Stella:** That makes a lot of sense. What is rule number two?

**Horace:** Cut your losses at a predetermined level. I recommend closing if the loss reaches 1.5 to 2 times the credit received. So if you received $1.40, close if the spread is worth $2.80 to $3.50. Never let a spread reach maximum loss.

**Stella:** And rule number three?

**Horace:** Close before expiration week. Gamma risk becomes extreme in the last five to seven trading days, especially for at-the-money strikes. If the stock has drifted toward one of your short strikes, you are sitting on a time bomb of gamma. Close the position and redeploy into a new expiration cycle.

[VISUAL: Calendar showing a 30-day option lifecycle. Days 1-21 in green labeled "Trading Zone". Days 22-25 in yellow labeled "Consider closing". Days 26-30 in red labeled "Danger Zone - Close!"]

**Stella:** What if one side of the condor is being threatened? Like if Apple starts dropping toward my $140 put?

**Horace:** You have several options. First, you can close the entire iron condor and accept the loss on the threatened side while banking the profit on the winning side. Second, you can close just the threatened side and leave the winning side on. Third, you can roll the threatened side to a lower strike and further expiration.

**Stella:** Can you walk through the rolling scenario?

**Horace:** Sure. Say you sold the $140/$135 put spread as part of your condor, and Apple has dropped to $142. The put spread is now worth $2.50, meaning you have a $1.10 loss on that side. But the call spread side is nearly worthless since Apple moved away from $160. You can close the entire put spread for $2.50, then simultaneously sell a new $138/$133 put spread 30 days out for maybe $1.80. Your net cost to roll is $0.70. You now have more time and a lower short strike.

[ANIMATION: Reference animation/week30_condor_adjustment.py - An iron condor payoff diagram on a stock that starts at $150. The stock price dot moves to $142. The left side of the condor flashes red. Then the animation shows the left side being "lifted" and moved to a new, lower position ($138/$133), with the payoff diagram adjusting in real-time. A timer resets from 15 days to 45 days, showing the extra time gained.]

**Stella:** But you only roll if your thesis is intact, right? If Apple is crashing because of bad news, maybe you just close and move on.

**Horace:** Exactly. Rolling is for when the stock has drifted but your thesis of range-bound behavior is still valid. If the stock has fundamentally broken out, if there is a regime change, close the position and reassess. Never roll into a hole. One roll is fine. Two rolls is aggressive. Three rolls means your thesis was wrong.

**Stella:** Let us talk about position sizing. How many condors should someone trade?

**Horace:** The golden rule is never risk more than 2 to 5% of your total portfolio on a single spread or iron condor. For a $100,000 portfolio at 3% risk per trade, your max risk is $3,000. With an iron condor that has $360 max loss, you could trade up to 8 contracts. But I would suggest diversifying across 3 to 5 different underlyings rather than putting all 8 contracts on one stock.

[VISUAL: Pie chart of a $100,000 portfolio. A small slice (4%) is labeled "Options Spreads - Active Income". The rest shows "Stocks 60%", "Bonds 25%", "Cash 11%". A zoom-in on the Options Spreads slice shows it divided into: "AAPL Condor 1.1%", "SPY Condor 0.7%", "MSFT Put Spread 1.2%", "QQQ Call Spread 1.0%"]

**Stella:** What about choosing between individual stocks and indexes for iron condors?

**Horace:** Indexes like SPY, QQQ, and IWM have major advantages for iron condors. They are extremely liquid with tight bid-ask spreads. They cannot gap as dramatically as individual stocks because they are diversified baskets. And if you use SPX options instead of SPY, they qualify for 60/40 tax treatment: 60% long-term capital gains and 40% short-term, regardless of how long you hold. That tax advantage alone can add 1 to 2% annually.

**Stella:** But individual stocks have higher premiums, right? Because they are more volatile?

**Horace:** They do, and that is the tradeoff. Higher premium but also higher risk. An individual stock can gap 10% on earnings. SPY might gap 3% on a terrible news day. For pure income generation via iron condors, I lean toward index options. For directional views expressed through spreads, individual stocks can make sense.

**Stella:** Let me ask about debit spreads versus credit spreads. When would I use one over the other?

**Horace:** Use credit spreads when implied volatility is high and you want to profit from time decay. You are essentially saying, "I do not think the stock will reach this level." Use debit spreads when you have a directional conviction and IV is low or moderate. You are saying, "I think the stock will move in this direction." High IV makes credit spreads attractive because you collect more premium. Low IV makes debit spreads attractive because options are cheap to buy.

[VISUAL: A decision flowchart. "What is your view?" branches into "Directional" and "Neutral/Range-bound". "Directional" leads to "Is IV high?" If yes: "Credit spread in the direction you expect". If no: "Debit spread in the direction you expect". "Neutral/Range-bound" leads directly to "Iron Condor (credit on both sides)"]

**Stella:** Before we wrap up, can you give me the key metrics to check before entering a spread trade?

**Horace:** Here is my checklist. One, probability of profit should be above 60% for credit spreads. Two, risk-to-reward ratio should be reasonable, ideally the maximum loss should be no more than 3 to 4 times the maximum profit for credit spreads. Three, the credit received should be at least 20 to 30% of the width of the spread to ensure adequate premium. Four, implied volatility rank should be above 30 for credit spreads, meaning IV is in the upper third of its annual range. Five, there should be no major earnings or catalysts before expiration. And six, position size should be under 5% of portfolio risk.

[VISUAL: Checklist displayed on screen: "Pre-Trade Checklist for Credit Spreads" with six items, each with a checkbox: "1. Probability of Profit > 60%", "2. Max Loss < 4x Max Profit", "3. Credit > 20% of spread width", "4. IV Rank > 30", "5. No earnings/catalysts in window", "6. Position risk < 5% of portfolio"]

**Stella:** That is a solid framework. I feel like I could actually start using this.

**Horace:** And you should start small. Paper trade your first 10 iron condors. Get comfortable with the mechanics, the management rules, and the emotional discipline of taking profits at 50% and cutting losses at 2x. Once you are consistent in paper trading, move to one or two real contracts.

**Stella:** Next week we are moving to fixed income, right? Yield curves?

**Horace:** That is right. We are taking a break from options to build our bond knowledge. We will come back to options in Week 37. But everything we learned about Greeks and spreads will be waiting for you when we return.

**Stella:** Thanks, everyone. See you next week.

[VISUAL: End screen with show logo, "Week 30: Spreads and Condors" summary, and preview of Week 31: Yield Curves]

**Horace:** See you then.
