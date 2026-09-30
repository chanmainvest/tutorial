## Part 2: YouTube Script

---

**VIDEO TITLE:** LEAPS — Long-Dated Options as Multi-Year Leverage

**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00-1:30]**

**Stella:** Welcome back. I'm Stella, and today we're on Week 38 — LEAPS. Last week we talked about replacing 100 shares of SPY with one deep-in-the-money call, and I think a lot of people came away with one big question, which is: how long does that work for? How long can I hold that call before time decay eats me alive? Horace, the answer is the topic of today's lesson.

**Horace:** It is. The headline is one number. A 730-day option has roughly one-fifth the per-day theta of a 30-day option at the same delta. That's the entire reason LEAPS exist as a category. Once you internalise that one fact, every multi-year option strategy that retail investors run — stock replacement, the poor man's covered call, the married LEAPS — flows directly from it.

**Stella:** We have two charts and one interactive today. First chart is the theta math. Second chart is the poor man's covered call. Let's start with the theta chart.

**[SECTION 1 — THE THETA CURVE, 1:30-6:00]**

**[VISUAL: image/week38_leaps_theta.png]**

**Horace:** This chart plots the absolute value of daily theta in dollars per share against days-to-expiration, on a $100 stock with 22% implied vol and a 4% risk-free rate. There are five curves, one for each delta band — 10, 30, 50, 70, and 90.

**Stella:** And the shape of every curve is the same.

**Horace:** Right. They all look like one-over-square-root-T. At 30 DTE the ATM 50-delta line is up around six and a half cents per day. At 365 DTE it's down to about two cents. At 730 DTE it's around 1.3 cents. Five times less per day than the 30-day point.

**Stella:** What about the 90-delta line — the one that matters for stock replacement?

**Horace:** The 90-delta deep-ITM line is the lowest curve on the chart. At 30 DTE it's about three cents per day. At 730 DTE it's down around half a cent per day. On a $100 stock that's half a basis point of carry per day on the underlying notional. That is essentially free leverage for the 24-month period.

**Stella:** And the 10-delta line?

**Horace:** Look where the 10-delta line is at 30 DTE — under one cent per day. That sounds cheap. But that 10-delta call is also moving 10 cents on the dollar, not 90. So as a percentage of premium, the 10-delta is the most theta-vulnerable contract on the board. The chart is dollar theta, not percentage theta.

**Stella:** So when we say "LEAPS have low theta," we should be specific.

**Horace:** Yes. We mean low dollar theta per day per share. We don't mean low percentage theta. The percentage theta on a far-OTM LEAPS can still be brutal because the premium is small. The strategies that work with LEAPS are the ones that buy meaningful delta — 70-delta, 90-delta — and let the small dollar theta do the work.

**Stella:** This is the chart you've been waving at students for years to explain why a 24-month deep-ITM call is the cleanest leverage instrument in the public markets.

**Horace:** Pretty much. The math is sitting right there on the curve.

**[SECTION 2 — POOR MAN'S COVERED CALL, 6:00-12:00]**

**Stella:** Let's pull up the second chart. This is the poor man's covered call payoff.

**[VISUAL: image/week38_pmcc_payoff.png]**

**Horace:** The PMCC is the single most popular LEAPS strategy among retail traders, and it deserves to be. Think about what a regular covered call is — long 100 shares, short one out-of-the-money call. To run that on a $100 stock you tie up $10,000 of capital. The PMCC swaps the 100 shares for a deep-ITM LEAPS. Same delta exposure, much smaller capital outlay.

**Stella:** Walk through the chart.

**Horace:** The setup on this chart is a $100 stock. Long leg is a January 2028 call at the 80 strike — that's deep-ITM, about 0.90 delta, two-year expiration. Costs roughly $25 a share, $2,500 per contract. Short leg is a 30-day call at the 110 strike — out of the money, 30-delta, sells for about $1.50 a share, $150 of credit. Net debit on the position is $25 minus $1.50 = $23.50. Compare that to $100 a share for the covered call equivalent.

**Stella:** And the chart shows the P&L at the short call's expiration, not at the LEAPS' expiration.

**Horace:** Exactly. We hold the LEAPS, we sold a 30-day call, so 30 days later the short call's fate is decided. The horizontal axis is the stock price 30 days from now. The vertical axis is the net P&L on the position at that point.

**Stella:** What's the shape?

**Horace:** Three regions. Below 80, the LEAPS is approaching its strike — the LEAPS still has 23 months to recover but its mark-to-market value is dropping fast. Between 80 and 110, both legs are gaining or holding value — the LEAPS is going up, the short call is decaying. Above 110, the short call goes intrinsic and starts eating into the LEAPS' upside dollar-for-dollar.

**Stella:** Where's the maximum profit?

**Horace:** Right at the short call strike — $110. At that point the LEAPS still has all its time value, the short expires exactly worthless, and we collected the full $1.50 of premium. The peak P&L on this position is about $9.50 a share, $950 a contract, on $2,350 of capital. That's a 40% return in 30 days *if* the stock pins exactly $110 — which it won't, but the shape is what matters.

**Stella:** And the maximum loss?

**Horace:** Capped at the net debit, $23.50 a share, $2,350 a contract. That happens if the stock collapses far below 80 and the LEAPS goes effectively to zero. On a covered call equivalent the max loss is $100 minus credits, much bigger absolute number. On the PMCC it's bounded by what you put in.

**Stella:** What are people getting wrong about this trade?

**Horace:** Three things. One — they treat it like a covered call. It's not. It's a diagonal spread. The long leg has expiration, theta, and vega. Two — they pick the short strike below the LEAPS strike. That creates a calendar that pays a debit on close, not a credit. Always pick the short strike above the long strike. Three — they don't roll. The LEAPS needs to roll at 90 DTE every cycle. The short calls roll every 30 days the same way week 27 does it.

**Stella:** Tax-wise?

**Horace:** Standard equity-option rules. The long LEAPS, held over 365 days, becomes long-term capital gain when sold. The short calls are realized short-term every cycle but they're typically small premiums; the tax noise is small. Options are the most tax-efficient leverage available; LEAPS-PMCC is the cleanest example of that statement.

**[SECTION 3 — THE INTERACTIVE, 12:00-15:00]**

**Stella:** Let's pull up the interactive lab.

**[VISUAL: interactive/week38_leaps_lab.html]**

**Horace:** Four strategies on the toggle bar. Stock — straight 100 shares. LEAPS only — the stock-replacement strategy from week 37 ported into the LEAPS framework. PMCC — long LEAPS plus short 30-day call. Married LEAPS plus put — long LEAPS plus protective put.

**Stella:** Sliders?

**Horace:** Spot, LEAPS strike, LEAPS DTE, short-call strike for PMCC, short-call DTE for PMCC, implied vol, risk-free rate. Outputs are net debit, breakeven, max profit, max loss, daily theta of the whole position, and net delta.

**Stella:** What's the first thing students should try?

**Horace:** Set spot to 100, pick the LEAPS-only strategy. LEAPS strike 80, DTE 730. Now drag the DTE down toward 30 and watch the daily theta number. It will multiply by about five from one end to the other. That's the headline of today's lesson sitting in one number.

**Stella:** And then?

**Horace:** Switch to PMCC. Same LEAPS, add a 110-strike short call at 30 DTE. The net debit drops, the daily theta of the *position* — net of long and short — gets close to zero or even slightly positive on certain days, and the delta drops from 0.90 to about 0.60. That tells you what you've given up to lower the cost: you sold off 30% of your upside delta to cheapen the position by about 6%.

**Stella:** Last one — the married LEAPS plus put.

**Horace:** Same LEAPS, plus a 95-strike put at 30 DTE. Watch the max loss number — instead of -$2,350 it's now about -$700, capped by the put. The cost: about $2.50 of put premium reduces your peak P&L by the same amount. You bought a floor, you paid for it, and the breakeven moves up by the put cost.

**[OUTRO — 15:00-18:00]**

**Stella:** Tying this back together — barbell, tax, and four-tranche.

**Horace:** Three callbacks. The barbell — LEAPS are the instrument that makes the barbell capital-efficient. You can hold equity beta in 25% of the dollar capital and use the freed 75% for whatever the four-tranche framework asks for. Tax via options — LEAPS held over 365 days are the cleanest long-term-capital-gain instrument outside of holding stock outright. And the four tranches — the LEAPS strategy you choose maps to the tranche. Stock replacement is the L1 boring core, PMCC is the L2 income strategy, married LEAPS is the L3 defined-risk play.

**Stella:** Three rules of operating a LEAPS position?

**Horace:** Roll at 90 DTE, never less. Pick strike by delta, not by round number. Size by notional, not by premium. Do those three things and the strategy runs itself.

**Stella:** Next week is Week 39 — broken-wing butterflies and ratio spreads. We'll see how the same vega and theta math plays out on more complex multi-leg structures. Until then, see you in the next one.

**Horace:** See you next week.
