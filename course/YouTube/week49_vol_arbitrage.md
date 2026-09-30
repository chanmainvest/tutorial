## Part 2: YouTube Script

---

**VIDEO TITLE:** Variance Risk Premium — Volatility Arbitrage, Short Straddles, and Gamma Scalping (Week 49)

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00 to 1:30]**

Stella: Welcome back to the Investing Tutorial. This is Week 49, and today we're at the deep end of the vol pool — variance risk premium, short straddles, and gamma scalping. Horace, why is this a Level-4/5 lesson and not a Level-2 one?

Horace: Because it sits at the intersection of two things most investors never reconcile. Alpha is rare, and the variance risk premium is one of the cleanest places where alpha actually lives. Vol is the tail that wags the dog. Vol arbitrage is the trade where you collect the alpha *and* take the tail risk — at the same time. Get the size wrong and you blow up; get the size right and you collect 4-5% a year on a sleeve of your portfolio for a decade.

Stella: So we're talking about insurance underwriting, basically.

Horace: That's the cleanest analogy. You're the insurance company. The option buyers are the policyholders. They overpay the actuarial fair value because they're afraid, and you collect the premium. The question is whether you're sized to survive the hurricane.

Stella: Let's start with the IV-RV chart.

[VISUAL: image/week49_iv_rv_history.png]

**[SECTION 1: The IV vs RV chart — 1:30 to 5:30]**

Horace: This is the entire trade in one picture. Top panel: VIX in red, the 30-day annualised realised volatility of SPX in blue. From 2010 to today. The red line is what option prices are charging. The blue line is what actually happened. Notice how often red sits above blue.

Stella: The bottom panel is the spread.

Horace: Right — implied minus realised, the variance risk premium. When that line is positive, sellers of vol are getting paid more than they're losing. When it goes negative — those are the cliffs. Mark them on the chart: Feb 2018, Volmageddon. March 2020, COVID. Late 2022, the gilt-and-Fed shock. August 2024, the yen carry unwind.

Stella: And on average, how big is the premium?

Horace: Plus 3 to plus 4 vol points. Across 36 years of data. The mean is roughly 3.9. The 75th percentile is around plus 7. The 5th percentile, the bad weeks, is around minus 8. The 1st percentile — Volmageddon — was minus 25.

Stella: So most of the time you're winning by 4. And once every few years you give back 25 in a single week.

Horace: That's the trade. Positive expected value, negative skew. The math says the average is profitable. The question is whether you're sized to take a minus 25 without going to zero.

**[SECTION 2: Why VRP exists — 5:30 to 8:00]**

Stella: Why hasn't this been arbitraged away?

Horace: Four structural reasons. One: insurance demand is calendar-driven. Pension funds, endowments, risk-parity books — they buy SPX puts on a schedule, not on a model. They don't care if the price is rich. Two: investors are loss-averse. They overpay for downside protection by roughly the loss-aversion ratio, two-to-two-and-a-half times. Three: variance is non-self-financing — when you're losing on a short variance trade, you have to *post more collateral* exactly when you're least solvent. The premium compensates the survivors.

Stella: And four?

Horace: Skew. OTM puts trade at higher implied vols than ATM. The 25-delta SPX put is typically 3-5 vol points above the ATM. Selling that skew adds another premium on top of the basic VRP. So when you sell an iron condor, you're capturing both layers.

Stella: Has this premium shrunk over time?

Horace: It has not. The 1990s averaged plus 4. The 2000s averaged plus 3.5. The 2010s, plus 4.2. The 2020s so far, plus 3.6. It's remarkably stable across regimes. That's because the structural reasons — insurance demand, loss aversion, collateral mechanics — don't disappear during quiet periods.

**[SECTION 3: How to actually harvest it — 8:00 to 12:00]**

Stella: Let's talk about the three ways to capture VRP.

Horace: First way, institutional: short variance swaps. You go to a Goldman or Morgan Stanley desk, you sell a 30-day SPX variance swap at, say, vol-strike 19. At expiry, you collect 19² minus realised² times your notional. Pure VRP harvest. No delta hedging required. Not retail-accessible.

Stella: Second way?

Horace: Short straddle delta-hedged. The retail version of the variance swap. You sell an at-the-money SPX call and put, same strike, 30 days out. You re-hedge the delta back to zero every day at the close, using /MES futures or SPX futures. The PnL is approximately your vega times implied-minus-realised. So if you sold at IV 19 and realised vol comes in at 15, you make four vol points times your vega. You earn the same VRP, just with daily mechanics.

Stella: And it's a pain to manage.

Horace: It is. Daily delta hedging means daily transactions, daily friction, and a real risk that you mess up the hedge during the one event when it matters. Most retail accounts shouldn't run this strategy.

Stella: Third way?

Horace: Iron condors. Defined-risk version. We covered this in Week 30. You sell an OTM put spread and an OTM call spread at the same expiry. Maximum profit is the credit; maximum loss is the strike width minus the credit. You give up roughly half the premium of a short straddle in exchange for capping the catastrophic tail. This is the right starting place for a retail short-vol book.

[VISUAL: image/week49_short_straddle_pnl.png]

Horace: Take a look at this chart — cumulative PnL of a short ATM SPX 30-day straddle, delta-hedged daily, 2010-2024. Compounded from 1 dollar.

Stella: The wealth line goes from 1 to about 1.8.

Horace: About 5% a year, average. But look at Feb 2018 — it drops 30% in a week. Look at March 2020 — drops 25% in three weeks. Late 2022, drops about 15% over six weeks. Three Volmageddon-class events in fifteen years.

Stella: So if you sized this at 100% of capital, it would have gone to zero in 2018.

Horace: Easily. If you sized at one-third of capital — closer to what the 1/3 Kelly rule says — your worst draw would have been about 10%. If you paired it with a 1% NAV gamma-scalp sleeve, your worst draw would have been about 5%.

**[SECTION 4: Gamma scalping, the long-vol cousin — 12:00 to 15:00]**

Stella: Let's talk gamma scalping.

Horace: Gamma scalping is the mirror of short-straddle delta-hedged. Same instruments, same daily hedging, opposite direction. You buy the ATM straddle, you re-hedge delta to zero every day. Each daily hedge is a buy-low / sell-high transaction — when SPX rallied, you were long delta, you sell at the high; when it fell, you were short delta, you buy at the low.

Stella: And the PnL is realised-minus-implied.

Horace: Right. You're paying implied vol up front via the premium. You're collecting realised vol via the daily hedge round-trips. You make money if and only if realised exceeds implied — which is the *opposite* of the VRP. So gamma scalping has *negative* expected value on average.

Stella: Then why do it?

Horace: Because the times it pays — 2008, 2018, 2020, 2022 — it pays *enormously*. A 1% NAV gamma scalp sleeve carrying minus 25% per year in calm markets can turn into plus 200% during a Volmageddon-class event. That offsets the cliff in the short-vol book. The barbell is short-vol *and* long-gamma. Not short-vol alone.

Stella: How big is the long-gamma sleeve relative to the short-vol sleeve?

Horace: Rule of thumb, 10-15% of the short-vol notional. So if you're carrying a 10% NAV short straddle, you carry 1-1.5% NAV long gamma. The long sleeve costs you roughly 1% of NAV per year in calm markets. The short sleeve makes you 5-7%. Net 4-6% per year, with a maximum single-event drawdown of maybe 5% rather than 30%.

**[SECTION 5: The cliff stories — 15:00 to 17:00]**

Stella: Tell the three stories — 2018, 2020, 2022.

Horace: 2018, Volmageddon. Six months of VIX 9-12. Short-vol books had compounded 25-30%. On Feb 5, SPX dropped 4%, but the front-month VIX future *doubled* between 3:30 and 4:15 PM. XIV — the 1x short-VIX ETN — went from 108 to 5 in two hours. Anyone short uncovered VIX futures at 5 PM lost more than the entire trade.

Stella: 2020.

Horace: COVID. Two weeks descending from VIX 14 to VIX 82.7, the all-time high. Realised vol spiked to 75 annualised. The IV-RV spread *inverted by 25 vol points* and stayed inverted for three weeks. Short-vol books that had been earning 4-5% a year took 25-30% draws each week for three weeks. Survivors had position-size discipline; non-survivors did not.

Stella: 2022.

Horace: Different mode. Slow grind. VIX in the high 20s for six weeks, RV repeatedly printing in the low 30s. No single cliff, but cumulative bleed of 15-20% on short-vol books across September and October. The lesson: the worst regimes aren't always the dramatic ones; sometimes the slow grind is what kills the book.

Stella: And the takeaway?

Horace: Two things. Vol moves first, vol moves more than the body, vol announces nothing in the implied signal. And the barbell is short-vol *and* long-gamma. Not short-vol alone.

**[SECTION 6: The interactive — 17:00 to 17:30]**

Stella: We've got a VRP lab on the site this week. Sliders for IV, RV, days to expiry, and capital deployed. The chart shows expected straddle PnL and the vega Sharpe.

Horace: Use it to feel the asymmetry. Set IV to 20, RV to 17 — you make money. Set RV to 25 — you take a 4-vol-point loss. Set RV to 50 — Volmageddon. The lab is calibrated to the actual SPX numbers. Play with it.

**[OUTRO — 17:30 to 18:00]**

Stella: Next week, week 50, factor tilts. Real factors, real ETFs, real returns. A Level-4 capstone before we close the curriculum.

Horace: VRP is real. VRP is heavy-tailed. Survive one Volmageddon and you collect for a decade. Don't survive one and you collect for nothing. Size accordingly. See you next week.
