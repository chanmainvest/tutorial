## Part 2: YouTube Script

---

**VIDEO TITLE:** Why 90% of Fund Managers Lose to the Index — and the Tiny Minority That Actually Earn Their Fees

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO]**

**Stella:** Welcome back. Horace, this is the cold-shower week. We
have spent forty-two weeks building a toolkit, and now we are about
to spend a whole lesson telling people that almost all of them
should not be active investors at all.

**Horace:** That's right. Before we look at the rare strategies that
do generate alpha — and we will, in the next several weeks — we have
to look at the base rate. Because if you don't know the base rate,
every active pitch sounds reasonable. Once you know it, your
default has to be passive, and active becomes a thing you only do
for very specific reasons.

**Stella:** Let's start with the headline number.

**Horace:** SPIVA. S&P Indices Versus Active. The April 2026
scorecard for US large-cap funds, ending December 2024. Show the
chart.

**[VISUAL: image/week43_spiva_chart.png]**

**Horace:** Five bars, by horizon. One year, sixty percent of
large-cap funds underperform the S&P 500. Three years, seventy-five.
Five years, eighty. Ten years, eighty-five. Fifteen years, ninety.
The longer the window, the worse it gets. Why? Fees compound, luck
washes out, and the survivorship-adjusted accounting starts to
bite.

**Stella:** And this is net of fees.

**Horace:** Net of fees, asset-weighted, survivorship-adjusted.
This is the cleanest dataset the industry has on its own
underperformance, and it has been telling the same story for
twenty-three years.

**Stella:** People say "fine, the average is bad, but I will just
pick the good ones."

**Horace:** That is the persistence question. And the answer is
worse than people expect. Show the transition matrix.

**[VISUAL: image/week43_persistence_table.png]**

**Horace:** Take the top quartile of large-cap funds in any
five-year window. Pure chance says twenty-five percent of them
should remain top quartile in the next five years. The empirical
number, averaged across SPIVA's persistence reports, is closer to
fifteen percent. Below random.

**Stella:** Why below random?

**Horace:** Mean reversion of style, asset bloat, manager turnover,
and fee hikes after a hot run. The very thing that put a fund in
the top quartile is the thing that makes it vulnerable in the next
window. Last cycle's winner is structurally overexposed to the
next reversal.

**Stella:** So past performance is not just non-predictive — it
is mildly anti-predictive at the top.

**Horace:** Correct. Buying after a great five-year print is the
modal retail mistake. It is also what fund-of-funds and most
advisors do for a living.

**Stella:** Talk about survivorship bias.

**Horace:** Every average return number you read in fund
marketing is calculated on funds that still exist. Over fifteen
years, thirty to forty percent of US equity mutual funds close,
merge, or quietly liquidate. They do not close because they were
good. They close because they were bad. Drop them, and your
"average" is the average of survivors only. SPIVA adjusts for
this. Marketing numbers do not.

**Stella:** Same in hedge funds?

**Horace:** Worse. Hedge fund databases are *voluntary*. Funds
report when they are doing well and stop reporting when they
aren't. The estimated upward bias on industry-average hedge
fund returns is two to four percent a year. Most of the
"hedge funds beat the market" claim disappears once you adjust.

**Stella:** Okay, so the average is bad and persistence is
bad. But we are going to spend the next several weeks on active
strategies. Why?

**Horace:** Because the SPIVA tail is real. There are four
distinct categories of strategies that have generated documentable,
persistent alpha for decades. They do not look like what most
retail investors call active management.

**Stella:** Walk through them.

**Horace:** One. Deep-value activism. Take a large concentrated
position in a mispriced public company, then engage with the
board or management to force a value-unlock. Spin off a
division, sell the company, do a buyback. Pre-1969 Buffett
partnership, Paul Singer's Elliott, ValueAct, Pershing Square,
Trian. Holding periods are three to seven years. The persistence
is documented. Capacity is inherently limited because you can only
fit so many activists in one company.

**Stella:** Two.

**Horace:** Quantitative systematic. Statistical, model-driven
trading at scale. Renaissance Medallion. AQR. Two Sigma. DE Shaw.
Citadel and Millennium on the multi-strat side. They mine
thousands of weak signals and combine them. Edge sources are
speed, data, infrastructure, headcount, and ruthless risk
management. Medallion has compounded around forty percent net of
fees since 1988. It is also closed to outsiders. The retail
cousins — AQR factor funds, MTUM, BTAL — deliver a fraction of
the gross edge after fees and constraints.

**Stella:** Three.

**Horace:** Event-driven. Merger arbitrage, distressed credit,
post-reorg equity, special situations. Company A announces it
will buy company B at fifty, B trades at forty-eight, the
two-dollar spread is your wage for warehousing deal-break risk.
Davidson Kempner, Farallon, Apollo's distressed desk, Oaktree.
Sharpe ratios in the 0.7 to 1.2 range. Drawdowns are bond-like
in normal times and equity-like in crises.

**Stella:** Four.

**Horace:** High-touch CTAs and discretionary macro. Trend
followers — Man AHL, Winton in its heyday, Aspect, Lynx — and
discretionary macro traders — Soros's old Quantum, Brevan Howard,
Caxton. They sit on commodity, FX, and rate trends, scale with
volatility, and provide convex *crisis alpha*. They make money
when equities crash. CTAs do five to eight percent net long-term
with negative correlation to drawdowns, which is what makes them
useful as a sleeve.

**Stella:** What unites the four?

**Horace:** Each has a *structural* reason for the return.
Activists get paid for engaging. Quants get paid for processing
data faster than anyone else. Event-driven gets paid for
warehousing deal risk. CTAs get paid for providing convex
insurance. None of them is "I am just a smarter fundamental
analyst than the buy-side." If a manager cannot tell you the
structural reason in one sentence, you are paying for noise.

**Stella:** Walk us through the interactive.

**Horace:** Sure. Open it.

**[VISUAL: interactive/week43_active_evaluator.html]**

**Horace:** Three inputs. Fund expense ratio. Excess return over
benchmark over five years, annualised. And the fund's tracking
error — the standard deviation of the active return.

**Stella:** And the outputs.

**Horace:** Information ratio — excess return divided by tracking
error. T-statistic equals IR times the square root of years.
Standard error logic from Week 17. And the punchline: the
implied probability that the observed excess return is luck, not
skill. One minus the probability that t exceeds the observed
value under a null of zero true alpha.

**Stella:** Run a typical mutual fund.

**Horace:** Expense ratio one percent. Excess return one and a
half percent gross — so half a percent net of fee. Tracking
error four percent. IR is 0.125. T-stat is 0.125 times root five,
about 0.28. Probability this is luck, not skill — about
thirty-nine percent. That is barely better than a coin flip.

**Stella:** Now run a great fund.

**Horace:** Excess return five percent net, tracking error six
percent, expense ratio one percent. IR 0.83. T-stat 0.83 times
root five, about 1.86. Luck probability about three percent.
*That* is statistically meaningful skill — and it is also rare in
the data.

**Stella:** What does this mean for the average investor?

**Horace:** Default to passive for your beta sleeve. That is the
first rule. That is your growth tranche, your income tranche, your
store of value tranche. If you hire active anywhere, demand a structural
story — one of the four categories above and access you actually
have. Watch fees. Don't chase last cycle's winner. And benchmark
your own DIY trading book against the index just like you would a
manager. Three years, IR below 0.3, return that capital to the
index. Same SPIVA logic applies to you.

**Stella:** Anything else?

**Horace:** One more thing. SPIVA does not say *no one* beats the
market. It says the *average* active fund does not, and that
*persistence* does not exist in the mutual-fund universe. The rare
strategies that do work — the four tranches — are not what most
retail investors mean when they say "active." They are
specialised, capacity-limited, and three of the four are not
accessible through a 1% mutual fund. The next several weeks will
walk through how the rare cases actually work.

**[OUTRO]**

**Horace:** Three takeaways. One. Default to passive. Ninety
percent of US large-cap funds underperform the S&P 500 over
fifteen years. The base rate is brutal and stable. Two.
Persistence is below random at the top quartile. Last cycle's
winner is statistically more likely to underperform than a
random fund. Stop chasing performance. Three. Real alpha exists,
in four documented categories — deep-value activism, quantitative
systematic, event-driven, high-touch CTAs — but each has a
structural reason and most are not retail-accessible at low fees.
If you are paying for active without a structural story, you are
paying for noise.

**Stella:** Next week, we open the hood on attribution and ask:
when a manager *does* outperform, what part of the return is
asset allocation and what part is security selection? See you
then.

---
