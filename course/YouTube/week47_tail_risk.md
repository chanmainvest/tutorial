## Part 2: YouTube Script

---

**VIDEO TITLE:** Tail Risk — Universa-Style Hedging, Put Protection, and CTAs as the Long-Vol Diversifier
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00–1:30]**

**HORACE:** Welcome back. This is Week 47 — tail risk. After
forty-six lessons of careful asset allocation, today we talk about
the part of the portfolio that *exists* to make money the day
everything else loses it.

**STELLA:** And the headline number we want viewers to walk away
with: in March 2020, Mark Spitznagel's firm Universa publicly
reported a +4,144% return on the hedge sleeve. On a 3.3%
allocation, that took a portfolio that was supposed to be down 30%
and turned it into roughly *flat* for the month.

**HORACE:** That is the geometry of tail risk done right. Today we
explain *how* — and how to do a smaller, retail version of the
same trade in a regular brokerage account.

---

**[SECTION 1 — What "tail" actually means — 1:30–4:30]**

**HORACE:** Stella, when finance textbooks teach risk, what
distribution do they assume?

**STELLA:** Normal. Bell curve. Mean and standard deviation fully
describe the return distribution.

**HORACE:** Right. And under the bell curve, October 19th, 1987 —
the day the S&P fell 22.6% in one session — should occur roughly
once every 10 to the 50th years. That is more than the age of the
universe by many orders of magnitude. It happened on a Monday.

**STELLA:** And then a 12% single-day drop happened on March 16,
2020, and an 8% single-day drop on August 24, 2015, and Volmageddon
on February 5, 2018, and—

**HORACE:** The point is the textbook is wrong. Markets are
fat-tailed. The 5-sigma days the bell curve says happen once every
14,000 years — they happen every 3 to 5 years in real data. 3-sigma
days the textbook says happen once every 18 months — they happen 5
to 8 times a year, clustered around crises.

**STELLA:** So if the textbook risk numbers are wrong, the question
is what an investor should *do* about it.

**HORACE:** Two things. One, stop trusting Sharpe ratios as if they
fully describe risk. Two, allocate a small slice of the portfolio
to something that is *paid* when the textbook is most wrong.

---

**[SECTION 2 — The cost-of-insurance tradeoff — 4:30–7:30]**

**HORACE:** [VISUAL: image/week47_tail_hedge_payoff.png] Here's the
geometry. We've got $100,000 in SPY and a $1,000 quarterly tail-
hedge budget. Look at the unhedged line — straight diagonal, down
30 grand at a 30% market crash. Now look at the hedged line.

**STELLA:** It kinks. It bends sharply at around minus 10% and goes
flat — even slightly positive — by minus 30%.

**HORACE:** That kink is what convexity buys you. A $1,000 deep-OTM
put on a quarterly cycle, sized at roughly 15% out of the money —
when the market falls 30%, that $1,000 becomes $50,000 or more.
The puts are paying out at thirty, forty, fifty times what you
spent on them.

**STELLA:** And the cost in normal years?

**HORACE:** That's the critical number. Spend $1,000 a quarter,
$4,000 a year, on a $100k portfolio — that's a 4% hedge sleeve
spend, but most of that is recovered or recovered-plus in any
normal year by the rest of the portfolio compounding. The net
*drag* is closer to 1% of total NAV per year. That is your
insurance premium.

**STELLA:** And the question is whether you recoup that 1% in the
crash years.

**HORACE:** That is the empirical question, and the answer in the
historical record is yes — by a very large margin — provided you
don't quit the program right before the crash arrives, which is
the hardest part.

---

**[SECTION 3 — Universa architecture — 7:30–10:00]**

**HORACE:** Let me sketch the Universa-style architecture
explicitly.

**STELLA:** Hedge size?

**HORACE:** 0.5 to 2% of NAV per year, depending on regime. Smaller
when implied vol is high, bigger when implied vol is low. Buy
insurance when it's cheap, not when it's expensive.

**STELLA:** Strikes?

**HORACE:** Deep out of the money. 25 to 35% below spot. These are
the contracts that are nearly free in dollar terms but explode in
convexity in a crash. ATM puts are too expensive — 6 to 8% per
year drag. Deep-OTM puts are 0.2 to 1% per year drag.

**STELLA:** Tenor?

**HORACE:** 60 to 90 days, rolled quarterly. Monthly is too
expensive — theta eats the sleeve alive. Annual is too far out —
the gamma profile flattens. The 60–90-day window is the sweet spot
Universa uses publicly.

**STELLA:** And what about the framing as a barbell?

**HORACE:** Exactly. Most of the portfolio sits in slow-compounding
boring base — index, T-bills, gold. A small sleeve is the convex
tail hedge. Bounded downside on the hedge — most you can lose is
the premium. Unbounded upside — 30 to 100x payoffs in crashes.

**STELLA:** And the volatility-tail point?

**HORACE:** Vol-tail-wags-dog. The few crash days dominate the
return distribution. Sidestep them and you compound at a higher
rate, even after paying the insurance premium. Don't sidestep them
and you get the textbook arithmetic — which the textbook gets
wrong.

---

**[SECTION 4 — CTAs and managed futures — 10:00–13:00]**

**HORACE:** Now the second long-vol path. CTAs.

**STELLA:** Commodity Trading Advisors. Trend followers.

**HORACE:** Right. Systematic trend-following across 50 to 200
liquid futures markets — equity indices, rates, currencies,
commodities. Buy what's going up, sell what's going down, scale
position size by realised vol.

**STELLA:** [VISUAL: image/week47_cta_2008.png] This is 2008. S&P
down 38%. 60/40 down 22%. Bonds up 5%. SocGen CTA Index — *plus
14%*.

**HORACE:** 2008 is the cleanest CTA year on record. Trends in
every macro market: stocks down all year, bonds up all year, dollar
up, commodities collapsed in the second half. Trend followers were
short stocks, long bonds, long the dollar, short commodities — and
they rode every one of those moves.

**STELLA:** But CTAs lose money in chop?

**HORACE:** Yes. Q4 2018, March 2020 V-shape, 2022–23 sequence —
classic whipsaw. The trend signal buys the rip and gets stopped
out, sells the dip and gets stopped out. The strategy needs price
*persistence*. A clean down trend is paradise. A volatility spike
followed by a snapback is hell.

**STELLA:** So if you want both — the gap-down protection and the
slow-trend protection?

**HORACE:** Pair them. 1% put-hedge sleeve plus 5% CTA allocation.
The puts cover the gap-down events the trend signal can't catch.
The CTAs cover the slow grinding bear market the puts may have
expired before catching. Different failure modes, different capture
profiles.

**STELLA:** Retail vehicles?

**HORACE:** KMLM, DBMF, CTA — these are liquid US-listed managed-
futures ETFs with expense ratios in the 90 to 100 basis point
range. Not hedge-fund 2-and-20. US-listed only —
which these are.

---

**[SECTION 5 — Sizing and practical rules — 13:00–15:30]**

**HORACE:** Three practical rules for sizing a tail hedge.

**STELLA:** One.

**HORACE:** Cap the carry at 1% of total NAV per year. Anything
above that turns the hedge into a directional bearish bet, and
directional bearish bets have terrible odds against the long-run
upward drift of US equities.

**STELLA:** Two.

**HORACE:** Roll quarterly, not annually. Sixty to ninety days out,
struck where premium-over-notional is around 0.4%, rolled on the
same calendar each quarter. Don't skip a quarter because the market
is calm. The discipline is the whole edge.

**STELLA:** Three.

**HORACE:** Strike selection by *price*, not by distance. Backsolve
to the strike where premium per dollar of notional is 0.4%. That
floats with implied vol — when VIX is 12, you can buy strikes 25%
out of the money for 0.4%; when VIX is 30, you're limited to 5 to
10% out of the money. Either way, the sleeve *size* is constant;
the strike *distance* moves.

**STELLA:** [VISUAL: interactive/week47_tail_lab.html] And the
interactive lab here lets viewers plug in their portfolio size,
hedge budget, strike, and DTE, and see the carry vs. the crash
payoff side by side.

**HORACE:** Try the minus 30% scenario at a 1% budget and a 15%
OTM strike. Watch the unhedged number — minus 30 grand on $100k —
and the hedged number, which lands roughly flat. That single plot
is the entire investment thesis of the strategy.

---

**[SECTION 6 — What this is not — 15:30–17:00]**

**HORACE:** Three things this is *not*, because every retail
implementation gets these wrong.

**STELLA:** One — it's not market timing.

**HORACE:** The hedge is on *continuously*. We don't try to predict
crashes. We pay the premium every quarter regardless. Most
quarters, the premium evaporates. That's the deal.

**STELLA:** Two — it's not a substitute for asset allocation.

**HORACE:** A barbell with no base is just a deep-OTM put
portfolio, and that has a deeply negative expected return on its
own. The base — the index, the T-bills, the gold — is what
compounds. The hedge protects the compounder.

**STELLA:** Three — it's not free.

**HORACE:** 0.5 to 2% of NAV per year of carry is real money. Make
sure the size is tolerable across a 7 to 10 year no-crash window
before committing. If you can't carry the cost without quitting,
pick a smaller sleeve or skip it.

---

**[OUTRO — 17:00–18:00]**

**STELLA:** Next week — Week 48, capital efficiency: how
institutional allocators stack levered exposures so the same
capital is doing two jobs at once.

**HORACE:** And what we covered this week: the fact that tail
events arrive on a schedule the textbook can't model, the Universa
architecture for paying a little to be on the right side of those
events, CTAs as the systematic long-realised-vol diversifier, and
the barbell logic applied to the *insurance* leg of
the portfolio.

**STELLA:** Open `interactive/week47_tail_lab.html`. Set a budget,
set a strike, click the minus 30% button. The arithmetic is the
lesson.

**HORACE:** See you next week.
