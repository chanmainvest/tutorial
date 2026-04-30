# Week 43: Active Management — SPIVA, Persistence, and What Very Few Managers Actually Do

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Almost every investor, at some point, hears the same pitch: *this fund
beat the market last year, this manager has a special process, this
strategy has worked for a decade, you should pay 1% a year (or 2-and-20)
for it.* The pitch is sometimes true. It is, on the data, almost always
false. This lesson is the cold-shower week. Before we look at the rare
strategies that *do* generate alpha, we have to look squarely at the base
rate — at how rare manager skill actually is, how poorly past performance
predicts future performance, and how the survivorship bias built into
every fund advertisement systematically lies to you.

You need this material for four reasons.

1. **It anchors SOUL #1.** Horace's first principle — *the market is
   right most of the time, alpha is the rare gap* — is not a slogan; it
   is a numerical claim. The SPIVA scorecards make it concrete. Over 15
   years, roughly 90% of US large-cap equity managers underperform the
   S&P 500. Default to passive is not a preference, it is what the
   evidence forces you to do unless you can name a specific reason this
   manager is in the surviving 10%.
2. **Persistence is worse than random.** Even the funds that *did* beat
   the market in one five-year window very rarely repeat. SPIVA's
   persistence reports show only ~15% of top-quartile funds remain top
   quartile in the following five years. Random would predict 25%.
   Past performance is not just *not predictive* — for the top
   performers it is mildly *anti-*predictive, because mean reversion
   and benchmark drift work against last cycle's heroes.
3. **You will be sold survivorship-biased numbers.** When Morningstar
   tells you the average large-cap fund returned 9% over the last
   twenty years, that average only counts funds that *still exist*.
   The 30-40% of funds that closed or merged because of poor
   performance are dropped from the calculation. Once you re-add them,
   the gap to the index widens further. If you don't know to ask
   "survivorship-adjusted?" you will systematically overestimate
   manager skill.
4. **A small handful of strategies actually work.** SPIVA does not
   say *no one* beats the market. It says the average active mutual
   fund does not. Inside that average sits a tail of strategies — deep
   value activism, quantitative systematic, event-driven, high-touch
   CTAs — that are documentably persistent over decades. They are not
   accessible through a Vanguard ticker, they require capital, lockups,
   or specific expertise, and three of the four are not what most retail
   investors think of when they hire an "active" manager. SOUL #5 lists
   the alpha sources Horace himself uses; this lesson maps where the
   institutional taxonomy puts them.

This week is the bridge between *should I be active or passive?* (almost
always passive) and the lessons that follow on *if I am going to be
active in part of my book, what do I actually have to do?*

---

### 2. What You Need to Know

#### 2.1 The SPIVA Scorecard — How Bad Is It Really?

S&P Dow Jones publishes the SPIVA (S&P Indices Versus Active) scorecard
twice a year. It is the closest thing the industry has to an audited,
survivorship-adjusted ledger of active manager performance. The
methodology is simple: for each Morningstar fund category, compare the
asset-weighted (and equal-weighted) net-of-fee return of every fund that
existed at the start of the period to the appropriate S&P benchmark, and
report the percentage that underperformed.

The April 2026 scorecard, looking at periods ending December 2024,
gives the following picture for **US large-cap equity funds**:

- 1-year window: ~60% of funds underperform the S&P 500.
- 3-year window: ~75%.
- 5-year window: ~80%.
- 10-year window: ~85%.
- 15-year window: ~90%.

See `image/week43_spiva_chart.png` for the bar chart.

The pattern is not subtle. As the window lengthens, the percentage of
underperforming managers monotonically rises. Why? Because over a
single year, luck dominates. Over fifteen years, fees compound, the
high-fee tail gets dragged below the index by sheer expense, and
survivorship-adjusted accounting starts to bite. Pulling 100 bps a
year out of an 8% gross return is pulling more than an eighth of the
total return — and that is what you are paying the average mutual fund
to do *to* you, not *for* you.

Other categories tell similar stories. Small-cap is slightly better
for active (more inefficient market, ~80% underperform at 15y).
International developed is similar. Emerging markets is slightly
worse for the index, but adjusted for currency hedging the gap
narrows. The one place where active *consistently* wins is, surprise,
the most expensive corner of the market: liquid hedge funds and
illiquid private credit, both of which have selection bias and
mark-to-model issues that flatter their numbers. We will look at
those carefully in later weeks.

#### 2.2 The Persistence Problem

A reasonable response to SPIVA is: "Fine, the *average* manager is
bad. But there must be *some* persistent winners. I will just pick
those." This is what every fund-of-funds, every wirehouse advisor, and
most pension consultants do for a living. The data says it does not
work either.

S&P also publishes a Persistence Scorecard. Take all US large-cap
funds, rank them on five-year performance, and put the top quartile
to one side. Now wait five years and look at where those funds rank
in the *next* five-year window. Random chance says 25% of them should
remain in the top quartile. The empirical number, averaged across
many vintages, is closer to **15%**.

That is not just below random — it is meaningfully below random. The
last cycle's stars *systematically* underperform pure chance going
forward. The reasons are mechanical, not mysterious:

- **Style drift / mean reversion.** A fund that crushed it because it
  was overweight US tech from 2015 to 2020 is structurally
  overexposed to the next reversal of that factor. The very thing
  that put it in the top quartile in window 1 is what makes it
  vulnerable in window 2.
- **Asset bloat.** Success attracts inflows. A fund that ran $200M of
  small-cap value with a sharp process can absorb maybe $1B before
  it has to broaden the universe and dilute the edge. Most successful
  funds end up running $10B+ and look like the index they once beat.
- **Manager turnover.** The PM who built the track record retires, or
  is poached. The "fund" you are buying is now a different team.
- **Fees.** Top-quartile funds are routinely the ones that hike fees
  after a good run, eating tomorrow's relative performance.

The transition picture is laid out in
`image/week43_persistence_table.png`. The diagonal — top-stays-top,
bottom-stays-bottom — is barely above the off-diagonal. Last cycle's
quartile rank carries almost no information about next cycle's rank.

#### 2.3 Survivorship Bias — Why the Average Looks Better Than It Is

Every fund advertisement you see suffers from the same accounting
trick, often unintentionally. When a fund family looks at "the
average return of our equity funds over the last 10 years," they only
include funds that *still exist*. The funds that performed badly
enough to be closed, merged into a different fund, or quietly
liquidated are dropped from the dataset.

Over a 15-year horizon, roughly 30-40% of US equity mutual funds that
existed at the start are no longer there at the end. They didn't
disappear because they were too good. They disappeared because they
were too bad. Removing them from the average is the equivalent of
ranking a graduating class only after dropping out the bottom third.

When SPIVA recomputes the same numbers *survivorship-adjusted* — i.e.
including the dead funds at their last reported NAV — the
underperformance gap widens by another 50-150 basis points a year.
This is why the SPIVA percentages we quoted in §2.1 are honest where
fund-family marketing is not.

Survivorship bias also infects:

- **Hedge fund index returns.** The major HF databases are voluntary.
  Funds report when they are doing well and stop reporting when they
  are not. Estimated upward bias on industry-average returns: 200-400
  bps a year.
- **Backtest databases.** Stock returns from CRSP are clean.
  Strategy-level backtests, less so — surviving signals are
  published, dead ones go in a drawer.
- **Manager track records.** A PM who ran two funds, one that died
  and one that lived, will only mention the live one on the
  marketing page.

Whenever you hear an *average* return from any non-SPIVA source,
your first question should be: *survivorship-adjusted, or not?*

#### 2.4 The Four Tranches That Actually Generate Alpha

If active is, in aggregate, a losing game, why are we even teaching
it for the next ten weeks? Because hidden in the SPIVA tail are four
distinct, durable, documented strategies that do generate persistent
alpha — but they don't look like the stockpicking you imagine when
you hear the word "active manager." Here is the institutional
taxonomy.

**1. Deep-value activism.** Take large concentrated positions in
mispriced public companies, then engage with management or the board
to force a value-unlock — a sale, a spin-off, a buyback, a strategic
shift. Berkshire Hathaway's pre-1990s era, ValueAct, Elliott
Management (Paul Singer), Pershing Square, Trian. Capacity is
inherently limited (you can only fit so many activists in one
company), holding periods are 3-7 years, and the persistence is
documentable. Buffett's pre-1969 partnership compounded ~30%/yr
gross. Singer's Elliott has compounded ~13%/yr net since 1977
through every regime. This is SOUL #5's *buying what passive flows
have abandoned* with engagement attached.

**2. Quantitative systematic.** Statistical, model-driven trading at
scale. Renaissance Technologies' Medallion (closed to outsiders,
~40%/yr net since 1988), AQR's market-neutral and managed-futures
suite, Two Sigma, DE Shaw, the modern multi-strat platforms (Citadel,
Millennium, Point72). These shops mine thousands of weak signals and
combine them. Edge sources: speed, data, infrastructure, headcount,
and ruthless risk management. *Not* available via a 1% mutual fund.
The retail-accessible cousins (AQR factor funds, BTAL, MTUM) deliver
a fraction of the gross edge after fees and constraints. SOUL #1's
*you still need the toolkit* warning lives here — these strategies
require capital, infrastructure, and discipline most investors don't
have.

**3. Event-driven.** Merger arbitrage, distressed credit and
post-reorg equity, special situations, capital-structure
arbitrage. The classic example is the M&A spread trade: when company
A announces it will buy company B at $50 and B trades at $48, the
$2 gap is paid for taking deal-break risk. Deal-break frequency is
~5-10% historically; the residual after losses is the
arbitrageur's wage. Davidson Kempner, Farallon, the distressed
desks at Apollo and Oaktree. These returns are not equity beta —
they are insurance premium for warehousing event risk. Sharpe
ratios are 0.7-1.2, drawdowns are bond-like in normal times and
equity-like in crises.

**4. High-touch CTAs and discretionary macro.** Trend-followers
(Man AHL, Winton in its heyday, Aspect, Lynx) and discretionary
macro traders (Soros's old Quantum, Brevan Howard, Caxton). These
sit on commodity, FX, and rate trends, scaling in and out with
volatility, and provide convex *crisis alpha* — they make money
when equities crash. CTA performance over 1990-2024 averages ~5-8%
net with a Sharpe of 0.4-0.6, but with a strongly negative
correlation to risk-asset drawdowns, which is what makes them
useful as a sleeve, not as a standalone bet.

What unites all four: they have a *structural* reason for the
return. Activists get paid for engaging. Quants get paid for
processing data faster. Event-driven gets paid for warehousing
deal risk. CTAs get paid for providing convex insurance. None of
them are "I am just a smarter analyst." The honest active investor
asks: *what am I being paid for?* If you cannot answer in one
sentence with a structural reason, you are paying a fee for noise.

#### 2.5 What This Means for You

Translate the data into action.

- **Default to passive.** Your beta sleeve (SOUL #13, Tranche 1
  growth) should be index funds. Three or four ETFs cover 90% of
  what most investors need. Anything else has to clear a higher
  bar.
- **If you hire active, demand a structural story.** Either it is
  one of the four tranches above (and you have access — most retail
  investors do not), or there is a documentable, persistent reason
  this specific manager has an edge. "Strong process" is not a
  reason. "We are concentrated activists with a 5-year horizon and
  $4B AUM" is a reason.
- **Watch fees.** Every basis point of fee is a basis point of
  guaranteed underperformance. SPIVA's underperformance percentages
  shrink dramatically when you compare *gross-of-fee* active
  returns. The fee is most of the gap.
- **Be honest about your own active sleeve.** If you trade a small
  options or single-stock book (SOUL #13's Tranche 4 opportunistic
  10%), benchmark it. After three years, if your IR is below 0.3,
  redirect that capital to the index. The same SPIVA logic applies
  to *you*.
- **Don't chase last cycle's winner.** The fund that crushed it
  2020-2024 is statistically more likely to underperform 2025-2029
  than a fund picked at random. Buying *after* a great five-year
  print is the modal retail mistake.

We will spend Week 44 on alpha decomposition (Brinson attribution),
Week 45 on the tools active managers actually use to find the rare
edges, and Week 46 on building a simple, evaluable active sleeve at
the household level.

---

### 3. Common Misconceptions

1. **"Past performance must mean *something*."** It does — it tells
   you what happened. The persistence data says it tells you
   essentially nothing about what will happen next, especially for
   funds that did unusually well.
2. **"Active will beat passive in a bear market."** SPIVA reports
   underperformance percentages by year, including bears. Active
   does not systematically outperform in bears. Cash-heavy funds
   can win a single down year and then drag for ten.
3. **"A 1% fee isn't much."** Compounded over 30 years on a 7%
   gross return, a 1% fee removes about 25% of terminal wealth.
   It is the single largest controllable drag on a long-horizon
   portfolio.
4. **"Sharpe ratios always tell the truth."** Selling deep
   out-of-the-money puts produces a beautiful Sharpe — until the
   day it doesn't. Many "skill" tracks are short volatility
   masquerading as alpha.
5. **"Hedge fund index returns prove the industry adds value."**
   The voluntary-reporting bias is so large in HF databases that
   the average industry print is overstated by 200-400 bps a
   year.
6. **"Passive cannot keep growing forever."** Maybe, but passive's
   share of US equities has gone from 20% in 2010 to over 50% in
   2025 and indexes have not stopped working. The reflexive
   "passive is a bubble" thesis has been wrong for fifteen
   years. SOUL #2's regime call is what would turn it.
7. **"Closet indexers are the safe choice."** They charge active
   fees for index-like portfolios. Active share studies (Cremers
   and Petajisto) find low-active-share funds underperform almost
   without exception.
8. **"I picked good funds — I am in the 15%."** Almost everyone
   thinks that. By construction, only 15% are right.
9. **"Buffett proves stockpicking works."** Buffett is sample size
   one, was a deep-value activist before activism was a label, ran
   capital you cannot replicate (insurance float), and stopped
   beating the S&P meaningfully in his last fifteen years.
10. **"If most managers underperform, the rest must outperform —
    so I can pick those."** No. Most managers cluster near the
    benchmark net of fees, with a left tail of bad ones dragging
    the percentages. The right tail is small, and you cannot
    identify it ex-ante from past returns.

---

### 4. Q&A Section

**Q: What is SPIVA, exactly?**
A: S&P Indices Versus Active. A semi-annual scorecard published by
S&P Dow Jones since 2002 that compares net-of-fee active mutual
fund returns to S&P benchmarks, by Morningstar category, with
survivorship adjustment. It is the most credible public dataset on
active manager underperformance.

**Q: Why does the underperformance percentage rise with horizon?**
A: Three reasons. Fees compound. The luck component shrinks with
sample size, exposing the negative average alpha. And funds that
got lucky early often see asset growth that erodes their edge.

**Q: Are small-cap or international active managers better?**
A: Marginally. Small-cap active still has 75-80% underperformance
over 15 years. International developed is similar. Emerging-market
active does slightly better when measured in local currency, but
worse after adding currency-hedging costs. The "inefficient
markets, active wins there" thesis is mostly folklore.

**Q: How is Renaissance Medallion 40%/yr if alpha is so rare?**
A: It is closed to outsiders, capacity-limited (~$10B), staffed by
PhDs in physics and statistics, and runs at the speed of light.
The strategy is structurally inaccessible, which is why it
persists. Their public funds (RIEF, RIDA) generate a fraction of
that and have had multi-year drawdowns.

**Q: What is a "high-active-share" fund?**
A: A fund whose holdings deviate substantially from its
benchmark — by construction, more than ~80% different by weight.
Cremers and Petajisto (2009) found high-active-share funds
modestly outperformed the index. Closet indexers (active share
< 60%) systematically underperformed. Most fund families now
publish this number.

**Q: If I cannot identify skilled managers ex-ante, what do I do?**
A: Use index funds for 90%+ of your equity exposure. If you want
an active sleeve, prefer (a) low-fee factor ETFs (Week 23) over
discretionary funds, (b) any access you have to the four
documented alpha categories above, or (c) a small DIY active book
that *you* benchmark honestly against an index. The household
SPIVA test applies to your account too.

**Q: Is the rise of passive itself going to break SPIVA?**
A: Doubtful in any meaningful horizon. Passive forces price-makers
to be even more concentrated and competitive among themselves;
the active universe shrinks but doesn't get easier. The share of
underperformers has been stable around 70-90% over fifteen years
even as passive has gone from 20% to 50% of US equity AUM.

**Q: Does SPIVA include hedge funds?**
A: No. SPIVA is mutual funds and ETFs only. Hedge fund
performance has its own (worse) reporting biases and is not
directly comparable.

**Q: Is there a household equivalent of SPIVA?**
A: Yes — DALBAR's QAIB (Week 11). Average individual investor
underperforms a buy-and-hold of the S&P 500 by 4-5% a year
because of behavioural mistakes. DALBAR is the SPIVA of the
household: most self-directed active investors also lose to
passive.

**Q: How should I think about my own DIY trading book then?**
A: Treat it as an active sleeve with a clear benchmark (SPY for
single-stock US, AGG for bond trades) and a clear capital cap
(SOUL #14's barbell — typically 5-15% of net worth). Run it for
three years, compute IR honestly, and if it doesn't clear 0.3,
return the capital to the index sleeve.

**Q: Why is persistence below random and not just at random?**
A: Mean reversion plus fee-driven inflows. The funds that did
best are typically overweight whatever style won last cycle;
that style mean-reverts. Their AUM doubles, fees often rise, and
the strategy gets diluted. The combination is structurally
anti-predictive at the top quartile.

**Q: What about top quintile or top decile? Is the persistence
better there?**
A: It is even worse. The narrower you slice the top, the more
luck-driven the original ranking, the more violent the mean
reversion. SPIVA's persistence reports show top-decile-to-
top-decile persistence in the 5-10% range — well below the 10%
random baseline.

**Q: Should I just give up on active completely?**
A: For the bulk of your wealth, yes — that is what *default to
passive* means. But understanding the four tranches and how the
four-tranche barbell (SOUL #13, #14) places a small explicit
*opportunistic* sleeve on top of a large *passive* core lets you
participate where edge actually exists, without risking the
core.

---

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

**Horace:** Default to passive for your beta sleeve. SOUL one.
That is your growth tranche, your income tranche, your store of
value tranche. If you hire active anywhere, demand a structural
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
