# Week 38: LEAPS — Long-Dated Options as Multi-Year Leverage

---

## Part 1: Reading Section

---

### 1. Why This Is Important

A LEAPS — Long-term Equity Anticipation Security — is just a listed call or put with an expiration date more than one year in the future. Two-year and 30-month expirations are the norm on SPY, QQQ, and the top 50 US single names. Mechanically nothing distinguishes a LEAPS from any other option. Pricing comes out of the same Black-Scholes formula, the same Greeks apply, and the same broker handles it. What changes is the time scale, and the time scale changes everything.

The single most important fact about a LEAPS is that its per-day theta is roughly proportional to $1/\sqrt{T}$. A 730-day call has theta-per-day about one-fifth that of a 30-day call at the same delta. That one number — five times less daily decay — is what turns options from a short-term speculation instrument into a multi-year position-sizing tool, and it is what makes LEAPS the natural bridge between weeks 25-30's premium-collection strategies and week 37's deep-ITM stock replacement.

Four reasons this lesson sits where it does in the curriculum.

1. **They make week 37's stock replacement durable.** A 90-day deep-ITM call works for a tactical view; a 24-month deep-ITM LEAPS works for a thesis. Holding period matters because every roll costs bid-ask, slippage, and a tax event. Longer-dated contracts mean fewer rolls.
2. **They unlock the poor man's covered call (PMCC).** The PMCC swaps a 100-share long for a deep-ITM LEAPS, then sells short-dated calls against it the same way week 27 sells calls against shares. The capital required drops by 70-80% and the income mechanics survive intact.
3. **They are tax-clean.** Held more than 365 days, a LEAPS sold at a gain is taxed at the long-term capital-gains rate — 15-20% federal — identical to the underlying stock. Options are the most tax-efficient leverage available to the US retail investor; LEAPS are the part of the option universe where that statement is most clearly true.
4. **They are the operational instrument of the barbell.** The barbell — boring core plus concentrated alpha sleeves — only works if the boring core can be funded with a small slice of capital. LEAPS are how that gets done: 25% of the capital controls the equity exposure; the other 75% can fund the alpha sleeves or sit in T-bills.

This lesson covers the math behind why the per-day decay is small, the three canonical LEAPS strategies, and the risks that the 30-DTE option trader has not seen before.

---

### 2. What You Need to Know

#### 2.1 What Defines a LEAPS

A LEAPS is, by CBOE convention, a listed equity or ETF option with more than nine months of life left at the moment of measurement. Practically:

- The CBOE issues new January-expiration LEAPS roughly 2.5 years before expiry. In April 2026 you can buy SPY calls expiring January 2027, January 2028, and (for the most liquid names) January 2029.
- A handful of underliers — SPY, QQQ, IWM, and the top single names — also list June-expiration and quarterly LEAPS to round out the calendar.
- Once a LEAPS reaches nine months of life, it converts to a "regular" option for inventory purposes; nothing changes about the contract itself.

Liquidity falls off quickly with expiration. SPY January 2027 spreads are 1-3 cents on near-the-money strikes; SPY January 2029 spreads can be 30-50 cents. Single-name LEAPS outside the top 50 names are usually too wide to trade size in.

#### 2.2 Why Daily Theta Is Small (the $1/\sqrt{T}$ Fact)

The Black-Scholes theta of an at-the-money call on a non-dividend-paying stock simplifies to approximately:

$$ \Theta \approx -\frac{S \sigma}{2\sqrt{T}} \cdot \phi(d_1) - rKe^{-rT}\Phi(d_2) $$

The first term dominates for low rates. The $1/\sqrt{T}$ on $S\sigma$ means daily theta scales as the inverse of the square-root of time-to-expiry. Two consequences:

- A 30-DTE ATM call on a $100 stock with $\sigma = 22\%$ has theta of about -$0.066/day (roughly 0.07% of spot per day).
- A 730-DTE ATM call on the same stock has theta of about -$0.013/day — five times less per day.

Across a 30-day holding period the long-dated option loses 30 × $0.013 = $0.39, while the short-dated option loses its full $1.97 of extrinsic. The long-dated buyer pays one-fifth the daily carrying cost for the same dollar of upside per dollar move.

![Line chart of absolute daily theta in dollars per share against days-to-expiration (DTE) on a $100 stock with σ=22%, r=4%, with five curves — one for each delta band (10Δ, 30Δ, 50Δ, 70Δ, 90Δ). Every curve has the same 1/√T shape: at 30 DTE the ATM 50Δ line is around $0.066/day; at 365 DTE it falls to ~$0.02/day; at 730 DTE ~$0.013/day, roughly five times less than the 30-DTE point. The 90Δ deep-ITM line is the lowest curve throughout, dropping near half a cent per day at 730 DTE — the math behind why a deep-ITM LEAPS is the cleanest leverage instrument in the public markets.](../image/week38_leaps_theta.png)

The same fact extends across deltas. A 0.90Δ deep-ITM LEAPS has daily theta closer to -$0.005/day at 730 DTE — almost negligible. That is the math behind week 37's claim that you can hold a deep-ITM 12-month call for nine months at a cost of 1.5-2.5% of the underlying notional. The fact also explains why LEAPS are wrong for short-term thesis trades: the same $1/\sqrt{T}$ scaling means buying a LEAPS for a 30-day move is overpaying for time you do not need.

#### 2.3 The Three Canonical LEAPS Strategies

**Strategy 1: Stock replacement (week 37 anchor).** A single deep-ITM (0.85-0.95Δ) LEAPS replicates 85-95% of the underlying's economic exposure for 25-35% of the capital. Held 9-15 months and rolled when 90 days remain. The rest of the position is T-bill yield on the freed cash. This is the canonical L1 application.

**Strategy 2: Poor man's covered call (PMCC).** Buy a deep-ITM LEAPS. Sell a short-dated (30-45 DTE) out-of-the-money call against it. The sold call captures premium the same way a covered call does against shares (week 27), but the long leg is a $25 LEAPS instead of $100 of stock. Capital outlay falls from $10,000 (for 100 shares) to roughly $2,500 — a 75% reduction. Annualized credit yield is similar to a covered-call program, often 10-18% on the LEAPS premium, which on a per-capital basis is 3-5x what the covered call produces.

![Payoff diagram for a poor man's covered call (PMCC) at the short call's expiration: long one January 2028 $80 LEAPS (≈0.90Δ, paid ~$25/share) plus short one 30-day $110 call (sold for ~$1.50). The x-axis is the underlying stock price 30 days from now; the y-axis is the package P&L. The curve climbs from a -$2,350 floor below the $80 LEAPS strike, peaks at +$950 at the $110 short-call strike (where the short expires worthless and the LEAPS keeps its time value), and is capped flat above $110 (every dollar of further upside is offset by the short going intrinsic). Net debit is ~$23.50/share; max loss is bounded at the debit; max profit hits at exactly the short-call strike. The chart visualises why PMCC is the capital-efficient cousin of week 27's covered call.](../image/week38_pmcc_payoff.png)

The PMCC's max profit is reached when the underlying closes exactly at the short call's strike at the short call's expiration; both legs have positive value, the short expires worthless, and the LEAPS retains most of its time value. Max loss is the net debit paid, achieved if the underlying collapses below the LEAPS strike before its expiration. Roll the short call out (further DTE) and up (higher strike) the same way week 27 rolls a covered call.

**Strategy 3: Married LEAPS plus put (synthetic stock with floor).** Buy a deep-ITM LEAPS for upside; buy a slightly-out-of-the-money put for downside protection. The pair behaves like a long stock position with a defined floor. The premium for the protective put eats into the freed-cash advantage, but for a position the investor is determined to hold through a recession or a known event, the structure caps losses cleanly. Less common than the other two; useful around earnings, FOMC, or geopolitical events.

#### 2.4 Tax Treatment

For a US taxable account holding equity or ETF LEAPS:

- **Long LEAPS held > 365 days, sold at gain → long-term capital gain.** Same 15-20% federal rate as the stock would have been. State tax follows the federal treatment.
- **Long LEAPS held < 365 days, sold at gain → short-term capital gain.** Taxed at marginal income rates (up to 37%). This is the trap: a LEAPS bought on April 5, 2026 and sold on April 4, 2027 is short-term; the same trade closed on April 7, 2027 is long-term. The line is sharp.
- **Loss treatment.** Capital losses, deductible against other capital gains, with up to $3,000/yr against ordinary income and indefinite carryforward.
- **PMCC has tax wrinkles.** Rolling the short call leg can technically reset the holding period of the LEAPS in some configurations (constructive sale rules under §1259, qualified covered call under §1092). For typical PMCC mechanics — short call strike well above the LEAPS strike, no constructive sale — the LEAPS holding period is preserved. Document carefully if the IRS asks.
- **No mark-to-market.** Equity options are not Section 1256 contracts; gains crystallise only at sale. SPX index options are 1256 (60/40 LTCG/STCG blend, marked to market at year-end), but LEAPS as commonly used here are equity/ETF options.

The cleanest tax case: buy a 24-month LEAPS, hold it to month 13, sell. That is unambiguously long-term capital gain at 15-20%. This is the precise mechanism behind "tax via options."

#### 2.5 The Risks the 30-DTE Trader Has Not Seen

A 30-day option position is over before the world changes. A 24-month LEAPS sits through every Fed meeting, earnings cycle, and political event between purchase and expiration. The new risks:

1. **Vega risk dominates.** The vega of a 24-month ATM call is roughly $0.55-0.75 per share per 1% change in implied volatility — about 10x the vega of a 30-day call. Buy a LEAPS when VIX is at 30, watch VIX revert to 15, and you can lose 25-35% of premium to vol crush even with the underlying flat. Anchor: do not buy LEAPS when VIX is in its top decile.
2. **Interest-rate sensitivity (rho).** A 24-month call has meaningful rho — about $0.10-0.20 per share per 1% rate move. If the Fed cuts 200bps over the LEAPS' life, your call loses real value (because the implicit financing cost embedded in the call is smaller). Less of a concern in 2026 with rates in steady state, but real.
3. **Dividend risk.** The pricing model assumes a continuous dividend yield. If the underlying raises its dividend mid-LEAPS, the call price drops. For SPY (1.3%) the effect is small; for a 4-6% yielder it is structural. Stock-replacement and PMCC strategies generally restrict to low-yield underliers.
4. **Liquidity dries up.** January 2028 LEAPS at $0.10 OTM strikes can have $0.40 bid-ask. Always trade LEAPS at the mid, never at market. If your strike has open interest below 100, pick a different strike.

[VISUAL: interactive/week38_leaps_lab.html]

#### 2.6 Sizing and Rolling

Three operating rules.

1. **Never let a LEAPS get inside 90 DTE.** The last 90 days is where gamma and theta accelerate. Roll forward 12-18 months when 90 days remain. The roll cost on SPY is typically 4-6% of position notional; budget for it.
2. **Match strike to delta target, not to round numbers.** A 0.92Δ stock-replacement LEAPS on SPY in April 2026 is the January 2027 416 strike — not the round 400 or 420. Pick strike by delta first; the dollar number falls out.
3. **Size by notional, not by premium.** One 0.92Δ SPY LEAPS controls roughly $48,000 of SPY exposure. If the sleeve target is $100k of SPY, buy 2 contracts, not 8. The capital outlay is incidental; the delta-controlled notional is the position.

Try the [LEAPS Lab](interactive/week38_leaps_lab.html) interactive — pick a strategy (stock, LEAPS-only, PMCC, married LEAPS+put), drag the sliders, and watch net debit, breakeven, daily theta of the position, and position delta update in real time.

---

### 3. Common Misconceptions

1. **"LEAPS are just expensive options."** They are options with more time. Per dollar of upside per dollar move, they are *cheaper* on a daily-decay basis than short-dated options. The absolute premium is higher because they buy more time.
2. **"Theta is bigger on a LEAPS because the premium is bigger."** Per-day theta scales as $1/\sqrt{T}$, not as the premium. A 730-DTE ATM call has roughly one-fifth the daily theta of a 30-DTE ATM call.
3. **"The PMCC is a covered call."** It is not — the PMCC is a diagonal spread. The long leg is an option, not stock, which means it has expiration, theta, and vega. Treat it like a spread, not like covered stock.
4. **"LEAPS are illiquid."** SPY, QQQ, top-50 single-name LEAPS at standard strikes have spreads of 1-3% on near-the-money and 5-10% on deep-ITM. Anything outside that universe genuinely is illiquid; stay in the liquid set.
5. **"I'll buy a 24-month LEAPS so I never have to roll."** You roll when 90 days remain. A 24-month LEAPS is a 21-month position, not a 24-month one. Rolling is part of the strategy, not an exception.
6. **"LEAPS are safer than stock because max loss is the premium."** Max loss as a percentage of premium can still be 100%. As a percentage of the equivalent stock notional it is smaller, but the relevant comparison depends on how you sized.
7. **"A PMCC with a high-IV stock pays better."** It pays bigger nominal premiums but the long LEAPS leg also costs more (vega works both ways). The capital efficiency ratio is roughly the same; the dollar volatility is larger.
8. **"I can sell calls on the LEAPS that go to the LEAPS strike."** No — the short call strike must be above the LEAPS strike to avoid being a calendar/diagonal that pays a debit. Standard PMCC has short strike above long strike.
9. **"LEAPS in an IRA earn the freed cash tax-free, so I should always use LEAPS in an IRA."** Long calls are permitted in most IRAs; short calls in a PMCC are also permitted (covered by the LEAPS). However, naked short legs are not. Check broker rules before assuming the PMCC works in your IRA.
10. **"LEAPS are for buy-and-hold."** They are for *position-and-roll*. A LEAPS held to expiration is just an expensive way to buy stock.

---

### 4. Q&A Section

**Q1. How much cheaper is daily theta on a 2-year LEAPS vs a 30-day option?**
At the money, roughly five times cheaper per day. The $1/\sqrt{T}$ scaling gives $\sqrt{730/30} \approx 4.9$. Deep-ITM the ratio is bigger because the 30-day deep-ITM call has near-zero extrinsic to begin with.

**Q2. What's the right LEAPS strike for stock replacement?**
80-85% of spot. That is the band where delta is 0.85-0.95 on a 12-24 month call at typical vols (15-25%) — the band where extrinsic is small relative to dollar exposure controlled.

**Q3. What's the right short-call strike on a PMCC?**
30-day expiration, 0.20-0.30 delta — 5-10% out of the money. Same rules as week 27's covered call. Avoid strikes below the LEAPS strike (creates a debit calendar) or at the LEAPS strike (no upside left).

**Q4. What if my short call gets assigned early?**
On a non-dividend underlier, early assignment is rare and almost always favorable to you (the assignor gave up time value). On a dividend-paying underlier, the day before ex-dividend the short ITM call may be assigned to capture the dividend; you then are short stock and long the LEAPS, which still has positive synthetic-stock characteristics but requires immediate close-out and re-establishment.

**Q5. Can I run a PMCC in an IRA?**
Yes, at most major brokers (Schwab, Fidelity, IBKR). The short call is "covered" by the long LEAPS for risk purposes. Naked short calls are not allowed; PMCC short calls are.

**Q6. How does the freed-cash carry interact with the LEAPS theta?**
On a 0.92Δ LEAPS, theta is roughly 1.5-2.5% of underlying notional per year. Freed cash earning 4.3% T-bills on 75% of notional yields 3.2% of underlying notional per year. Net carry: +0.7% to +1.7% per year before dividends skipped. The LEAPS is roughly self-financing on indexes.

**Q7. How does this interact with the four-tranche framework?**
LEAPS-replaced equity sleeve consumes 25-30% of the dollar capital that the underlying sleeve target requires. The freed 70-75% can fund the L2 strategies sleeve, the L3 alpha sleeve, or sit in T-bills. This is the operational version of the barbell.

**Q8. Should I worry about implied vol when buying LEAPS?**
Yes — more than for short-dated options. Vega on a 24-month call is ~10x a 30-day call's vega. Don't buy LEAPS when VIX is in its top decile (currently above ~28). At VIX 15-20 in April 2026, LEAPS pricing is reasonable.

**Q9. What's the difference between LEAPS on SPY and on SPX?**
SPX index options are Section 1256 contracts: 60/40 long/short capital gains regardless of holding period, marked to market at year-end. Cash-settled, European-style. SPY options are equity options: standard holding-period rules apply, physical settlement, American-style. SPX LEAPS at 10x notional are tax-cleaner; SPY LEAPS at 1x notional are operationally simpler.

**Q10. Will my broker require special permission for LEAPS or PMCCs?**
LEAPS purchase is Level 1 or 2 options approval — broadly available. The PMCC short leg requires Level 3 (spreads) at most brokers. Naked short calls require Level 4. Check before placing the trade.

**Q11. What's the worst that can happen on a PMCC?**
Underlying collapses below the long LEAPS strike before LEAPS expiration. The LEAPS goes to zero; the short call expired worthless along the way collecting some premium but not enough to offset the LEAPS loss. Max loss is net debit minus all premiums collected over the life of the position.

**Q12. When does the LEAPS strategy fail?**
Three regimes: (1) sustained multi-year drawdown — the LEAPS can go to zero before you can roll; (2) high-vol whipsaw where a high-IV LEAPS purchase is followed by IV crush; (3) anything illiquid where bid-ask round-trips eat the freed-cash carry. Stick to liquid underliers and IV rank below 50.

---

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
