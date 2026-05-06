# Week 14: Pair Trading — Relative Value, Mean Reversion, and the Simplest Equity-Hedge-Fund Strategy

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Week 13 introduced long/short — the architecture. This week applies
that architecture to its narrowest, most teachable form: **two stocks,
one long, one short, equal dollar, sized to the spread between them.**
Pair trading. The simplest equity-hedge-fund strategy in the book, and
the cleanest place for a retail investor to learn the mechanics of
relative value before scaling up to anything more complicated.

You need this lesson for four reasons.

1. **It is the cleanest test of the long/short toolkit you just
   learned.** Long Coke / short Pepsi at equal dollar is dollar-
   neutral by construction, roughly beta-neutral by virtue of the
   two stocks having near-identical sensitivities to the consumer-
   staples factor, and the entire P&L is the *spread alpha* — the
   difference between two close substitutes. There is nowhere for a
   directional view to hide. If the trade works, you traded the
   spread; if it doesn't, you didn't. Pair trading is the laboratory
   in which you find out whether you have any relative-value edge at
   all.

2. **It is the entry point to a real, durable alpha source — not
   the made-up kind.** The structural alphas that actually compound
   after costs are liquidity, sector rotation, long-term trends, and
   buying what the passive machinery has abandoned.
   Pair trading sits inside the structural-alpha class because the
   pair trader is *supplying liquidity to the temporarily dislocated
   leg*. When PEP gaps down on a weak quarter and KO sits still, the
   pair trader who buys the dislocation is on the other side of
   forced sellers (mutual-fund redemptions, factor unwinds, index
   rebalances). The reversion of the spread back to its long-run
   relationship is the structural payment for that liquidity.

3. **It teaches you why "real-looking" pairs decay — the regime
   change problem.** Regime change is the recurring bell of this
   course: regimes change, often without warning, and a strategy that
   worked for a decade can stop working in a quarter. Pair trading
   is the cleanest case study of that principle in retail-accessible
   form. Two stocks that have moved together for fifteen years can
   permanently de-couple — KO and PEP did, partially, after PEP's
   snack-foods business compounded faster than KO's beverage-only
   one. A pair trade that ignored that fundamental divergence and
   kept fading the widening spread back to its 10-year mean would
   have been wrong for six straight years. **Cointegration is a
   conditional, regime-dependent property, not a permanent one.**

4. **It frames the August 2007 quant quake — the canonical case
   study for crowded factor risk.** When too many quants run
   essentially the same pair-trading and stat-arb strategies, the
   pairs themselves become a factor — a factor that can unwind
   in correlated panic. Over four trading days in August 2007, a
   forced unwind by one or two large multi-strat funds drove a
   simultaneous reversal across the standard pair-trading factor,
   and most of the field lost two-to-four sigma on what should have
   been independent trades. The lesson — your alpha is only alpha
   when the people running the same strategy aren't all forced to
   exit at the same time — is one of the most important risk-
   management lessons in modern finance, and pair trading is where
   it was first learned.

This lesson sits in the *opportunistic* slot of the four-tranche
structure and on the alpha end of the barbell. Most
of your wealth is in the safety end (cash, Treasuries, gold,
deep-ITM long-dated calls on names you'd own anyway). A small
sleeve at the alpha end is where the pair-trading book lives — the
*pinwheel*, in Horace's phrase, that spins when the rest of the
portfolio is sitting still.

---

### 2. What You Need to Know

#### 2.1 Relative Value — the Core Reframe

Long-only investing asks an absolute question: "Is KO cheap?" The
answer requires a view on KO's earnings, multiple, growth, balance
sheet, and the broader equity-risk premium. Get any of those wrong
and the trade can be wrong even if KO is "cheap" by your model.

Pair trading replaces the absolute question with a relative one:
**"Is KO cheap *relative to* PEP?"** The two beverage incumbents
share a customer base, a regulatory regime, an exposure to the
commodity-price cycle in sugar and aluminium, an exposure to the
consumer-staples factor, an exposure to USD strength, and roughly
the same multiple regime. A bad consumer-staples macro hits both;
a sugar-tax scare hits both; a strong-dollar quarter hits both.
What it does *not* hit symmetrically is the company-specific
operational variance — KO's bottler restructuring, PEP's
snack-foods margin, an FX shock specific to one country, a recall
that lands on one brand. The spread isolates that company-specific
variance from everything else.

The directional risk you eliminate is large. The 60/40 holder of
2,000 shares of KO has roughly half a million dollars exposed to
"the consumer staples factor wakes up tomorrow and falls 10% on a
risk-off day." The dollar-neutral pair trader long 1,000 KO and
short 1,000 PEP has approximately *zero* dollars exposed to that
factor. What the pair trader has, instead, is a $0 net but $200
gross book that is exposed to **the difference between two stories
that look similar**. That difference is what they get paid for —
or punished for, when the difference turns out to be permanent
rather than mean-reverting.

This is why pair trading is a clean teaching example: it strips off
market beta entirely and lets you see, in isolation, whether the
relative-value bet has any signal at all.

#### 2.2 Spread Construction and the Z-Score

Once you've picked a pair, you need a way to say *how dislocated*
it is. The standard approach is the **rolling-Z-score on the
log-spread**.

Construct it in three steps.

1. **Form the log-spread** as `s_t = log(P^A_t) - log(P^B_t)`.
   Working in log-space is the convention because it makes the
   spread invariant to dollar normalisation and gives a multiplicative
   interpretation: a constant `s_t` means a constant *ratio* of
   prices, regardless of level.
2. **Compute the rolling mean and stdev** over a lookback window —
   60 trading days is a common starting point for daily data.
   Call them `mu_t` and `sigma_t`.
3. **Z-score** the spread: `z_t = (s_t - mu_t) / sigma_t`. By
   construction, in a stable cointegrated relationship, `z_t` is
   approximately distributed mean-zero, unit-variance, with most
   observations falling between -2 and +2.

The image below shows what this looks like for KO and PEP from
2015 through 2024 — the top panel is normalised prices, the
bottom panel is the rolling-60-day Z-score with +/-2 sigma bands.

![Two-panel chart of KO and PEP from 2015 through 2024. Top panel: KO and PEP daily AdjClose prices both rebased to 100 at the start of 2015, drifting together for most of the decade with episodic divergences. Bottom panel: rolling 60-trading-day Z-score of log(KO) - log(PEP), with the +/-2 sigma bands highlighted; the series spends the bulk of the time inside the bands and visits the +/-2 lines a handful of times across the ten-year window.](image/week14_kopep_spread.png)

A pair trader looks at the bottom panel and asks: *when the line
hits +2, do I trust that it'll come back to zero, and how long
will it take?* The answer comes from cointegration, not correlation.

#### 2.3 Correlation vs Cointegration — Why the Distinction Matters

Two random walks can be highly correlated and still diverge to
infinity. That is the trap that kills naive pair trades.

- **Correlation** measures whether two return series move together
  *over short horizons*. Two stocks with monthly correlation of
  0.85 just means their monthly returns line up; it says nothing
  about whether the *spread between their levels* mean-reverts.
- **Cointegration** is stronger. Two price series are cointegrated
  if there exists a linear combination of them that is *stationary*
  — i.e., the spread itself has a stable mean and variance and
  reverts when it strays. Cointegration is the mathematical
  formalisation of "they share a long-run equilibrium relationship."

In practice, cointegration is tested with the Engle-Granger
two-step procedure or a Johansen test on level series; the details
are second-order. The *intuition* is the part you must internalise:
**you can trade pairs only when the spread is mean-reverting, and
correlation alone does not guarantee that.** The textbook
counter-example is two assets in different secular trends — both
might rally together for years (high correlation) while the *gap*
between them widens monotonically (no cointegration). A pair trader
who fades that widening gap loses every quarter for a decade.

A practical rule: before you trade a pair, plot the spread Z-score
over a 5-to-10-year window and ask "does this thing visibly come
home, repeatedly, after each excursion?" If yes, the cointegration
test is mostly confirming what your eye already saw. If no, no
amount of statistical machinery will rescue the trade.

#### 2.4 Classic Pairs and Why They Work

Four canonical retail-accessible US-listed pairs, with the structural
reason each cointegrates:

| Pair | Sector | Why the spread mean-reverts |
|---|---|---|
| **KO / PEP** | Consumer staples — beverages | Two near-identical global beverage incumbents; same customer base, same commodity cost structure, same defensive multiple regime. Spread breaks only when one company makes a strategic-mix change (PEP's snack-foods build-out is the classic example). |
| **V / MA** | Financials — payments duopoly | Visa and Mastercard are a regulatory duopoly with identical economics: card interchange, network effects, oligopolistic pricing power. Spread breaks only on company-specific litigation or geographic-mix exposure (China, Russia). |
| **XOM / CVX** | Energy — integrated supermajors | Both run integrated upstream-downstream books with similar reserves, similar geography, similar capital-allocation discipline. Spread breaks on idiosyncratic operational events — refinery accidents, project-cost overruns. |
| **GLD / SLV** | Precious metals ETFs | Gold and silver share a monetary-debasement story, but silver is half industrial, half monetary; the spread (the "gold-silver ratio") cycles between 50 and 90 with cyclical mean-reversion driven by the relative weight of those two demand drivers. |

The *common* feature is that the two legs share a structural
driver and differ on a *contained* idiosyncratic dimension. The
trade is paid for the contained dimension (the spread mean-reverts)
and protected against the structural one (it nets out).

#### 2.5 Entry/Exit Rules and a Worked Backtest

The textbook rule is **+/-2 sigma entry, 0 sigma exit, with a hard
stop at +/-3 to +/-4**.

- When `z` falls below -2: the spread is two standard deviations
  cheap, A is unusually cheap relative to B. Go long A, short B at
  equal dollar.
- When `z` rises above +2: the spread is two standard deviations
  rich. Go short A, long B at equal dollar.
- When `z` crosses zero: the spread is back at its rolling mean.
  Exit. Do not wait for the opposite tail; the marginal expected
  return from running another sigma is small and the regime-change
  risk grows with holding period.
- If `z` continues past +/-3 or +/-4 in the wrong direction: **cut
  the position and re-evaluate the cointegration assumption** —
  more often than not, the relationship has broken structurally
  rather than dislocated stochastically.

The chart below shows that ruleset applied to KO/PEP from 2015
through 2024. The top panel is the Z-score with up-arrows on long-
spread entries and down-arrows on short-spread entries; the bottom
panel is the cumulative log-spread P&L net of a 5 bp round-trip
cost per side change.

![Two-panel pair-trading backtest of KO/PEP from 2015 through 2024. Top panel: 60-day Z-score of log(KO)-log(PEP) with horizontal lines at +/-2 sigma and at zero, with green up-arrows marking entries to long the spread (Z hits -2) and red down-arrows marking entries to short the spread (Z hits +2). Bottom panel: the cumulative P&L line of the +/-2 entry, 0 exit rule with 5 bp per-trade costs, showing many small wins and one or two regime breaks where the spread did not mean-revert and the trade was cut.](image/week14_pair_pnl.png)

What the chart teaches: **most pair trades are small wins, with
occasional regime breaks that cost more than several wins put
together.** This is exactly the shape of a structural-alpha return
stream. It is also why pair trading is run as a *book of many
pairs* rather than one — the law of large numbers is what makes
the small-edge-per-pair model viable. A single-pair retail
implementation is more education than alpha; the production
version diversifies across thirty to fifty pairs simultaneously.

#### 2.6 The 2007 Quant Quake — Crowding Risk Is Real

In the first week of August 2007, the standard equity-stat-arb book
— roughly defined as "long the cheap leg of a pair, short the
rich leg, across many pairs simultaneously" — lost between 4 and
12 sigma of its expected daily return for four straight days. The
unwind cascaded across most of the major multi-strat hedge funds
running similar models: AQR, Renaissance Equity Market-Neutral,
Goldman Global Equity Opportunities. Some funds halved in a week.

The post-mortem is now well-documented. One of the largest multi-
strats — most of the public reconstruction blames Goldman's
quant book, though the precise actor is less important than the
mechanism — was forced to deleverage suddenly, likely due to a
margin call originating from an unrelated subprime-mortgage book.
Closing the equity book required selling its long stat-arb leg
(buying back the short side) en masse. Because every other major
quant ran *the same pairs from the same factor data*, those same
pairs simultaneously moved adversely against everyone else's
book. As losses mounted, more funds were forced to deleverage,
which moved the pairs further, which forced more funds to
deleverage. **Standard pair-trading factor exposure had become a
crowded trade — and crowded trades, when they unwind, do so
together.**

The lesson is foundational and is the cleanest illustration in
finance of the regime-change principle. **An alpha source
remains alpha only as long as the population running it is small
enough that no forced exit can simultaneously move all the trades
against you.** The day too many people run the same strategy, the
strategy itself becomes the risk factor. This is why modern stat
arb runs a continuous "crowdedness factor" overlay — measuring
how many other funds are likely in the same trade — and dials
gross exposure down as crowdedness rises. The retail pair trader
inherits the same discipline in miniature: do not over-size a
canonical, well-known pair, because every other dollar in that
trade is implicitly correlated with yours.

#### 2.7 Where Pair Trading Sits in the Barbell

The barbell is most of your wealth in safety, a small
sleeve in genuine asymmetric edge. **Pair trading lives at the
edge end.** Sized correctly, a pair-trading sleeve runs at single-
digit percentage of total portfolio, in dollar-neutral pairs
where the gross exposure is two-to-three times sleeve size and
the net is approximately zero. The sleeve's expected contribution
to total portfolio return is small (3-8% annualised on the *sleeve*,
which translates to 0.3-0.8% on a 10% sleeve allocation); the
expected contribution to total portfolio *Sharpe* is potentially
much larger because the sleeve's returns are roughly orthogonal to
the long-only book.

This is the right way to think about pair trading for a retail
investor: **not as a way to compound wealth, but as a way to
reduce the variance of the wealth path.** It is a Sharpe-ratio
play, not a return play. Anyone who promises you a pair-trading
strategy with double-digit gross returns and low drawdowns is
either over-fitted, levered, or selling a course.

---

### 3. Common Misconceptions

**Misconception 1: "High correlation means a good pair."**

Correlation measures co-movement of returns; cointegration measures
mean-reversion of levels. High correlation with no cointegration
is the canonical wide-and-keep-widening trap.

**Misconception 2: "If a pair has worked for ten years, it'll keep
working."**

KO/PEP's relationship has shifted twice in the last twenty years
on PEP's snack-foods build. Cointegration is conditional on the
underlying business mix staying stable. When the mix changes, the
spread re-prices to a *new* equilibrium, and the trader fading
the old equilibrium loses for years. The regime has shifted.

**Misconception 3: "Z-score of +/-2 is a hard rule."**

The thresholds are calibration choices, not laws. In a low-vol
regime, +/-1.5 sigma fires more trades and may be the right cut;
in a high-vol regime, +/-2.5 reduces false positives. Calibrate
to the pair, the lookback, and the realised vol regime — not to
the textbook number.

**Misconception 4: "I'll just trade one pair to learn."**

A single-pair book is not pair trading; it is one trade with high
operational overhead. Real pair-trading strategies run thirty-plus
pairs to make the law of large numbers work. The single-pair
exercise is education; do not confuse it with alpha.

**Misconception 5: "Pair trading is risk-free because it's market-
neutral."**

Pair trading has spread risk, regime-break risk, crowding risk
(2007), borrow-cost risk on the short leg, and operational risk
on margin and dividends. Net dollars zero is not net risk zero —
LTCM was market-neutral and still lost 90%.

**Misconception 6: "If the spread keeps widening, my position
gets bigger and the eventual reversion is more profitable."**

This is the martingale fallacy applied to pairs. As the spread
widens, your mark-to-market loss grows, the broker raises your
margin requirement, and the very mechanism that should make the
trade more profitable in theory becomes the mechanism that forces
you out before the reversion arrives. Stay solvent first —
the market can stay irrational longer than you can — and that
discipline is the anchor here.

**Misconception 7: "Borrow cost is small enough to ignore."**

For mega-cap pairs (KO, PEP, V, MA) it usually is — single-digit
basis points. For smaller-cap or specialty pairs it isn't, and
the borrow rate can flip from 1% to 30% on a press release.
Always check the borrow on the short leg before sizing the
trade.

**Misconception 8: "The 2007 quant quake is ancient history."**

The same mechanism repeats. February 2018 had a vol-target
factor unwind. March 2020 had a multi-strat de-leveraging week.
Every few years, factor crowding produces another four-day
correlated unwind. The quake was the cleanest case study, not
the only one.

**Misconception 9: "If I use options to express the pair, I avoid
the borrow problem."**

You also avoid the linear-spread P&L. An options-based pair has
non-linear exposure to volatility and a defined-cost premium that
eats into the spread alpha. It is not a free upgrade — it is a
different trade with different greeks.

**Misconception 10: "Pair trading is alpha, full stop."**

Pair trading is alpha *as long as the spread cointegrates and the
strategy isn't crowded*. Both conditions can fail. It is structural
alpha conditional on regime and crowding — not a permanent free
lunch.

**Misconception 11: "The strategy works because I picked the right
pair."**

The strategy works because *many* pairs simultaneously revert
slightly, and the small per-pair edge aggregates into a usable
return stream at the book level. Single-pair returns are mostly
noise; book-level returns are where the alpha is recognisable.

---

### 4. Q&A

**Q1: Should a retail investor with a $100k portfolio actually run
a pair-trading book?**

A: Probably not as a serious P&L source. The minimum scale for a
pair-trading book to be statistically meaningful is twenty-to-
thirty pairs simultaneously, with operational discipline on
borrow, margin, and dividends. Below that scale, you have a
high-overhead toy. *Run one or two pairs in small size for
education* — a few percent of your portfolio — and treat the
output as tuition. If you want the alpha without the overhead,
buy a market-neutral mutual fund or ETF and let someone else
run the book.

**Q2: What lookback window should I use for the Z-score?**

A: 60 trading days is a sensible starting point for daily data;
40 is more responsive but noisier; 120 is more stable but slower
to detect regime breaks. The right answer is a function of how
fast the cointegration of *your specific pair* tends to reset.
For mega-cap pairs (KO/PEP), 60 to 90 days. For more
volatile pairs (small-cap, biotech), 30 to 60. Calibrate, do
not adopt by default.

**Q3: How big a position can I take in one pair?**

A: A common institutional rule is 2-5% of the sleeve per pair,
with a hard 10% cap. For a retail investor, on a $100k
portfolio with a $10k pair-trading sleeve, that's $200-500 of
gross exposure per pair (i.e., $200 long + $200 short = $400
gross at the small end). It feels small. It is small. Pair
trading is a per-pair-tiny, many-pair-aggregated strategy by
design.

**Q4: When do I cut a pair and admit the cointegration broke?**

A: When `z` extends past +/-3 to +/-4 and shows no signs of
returning, *and* you can identify a fundamental reason for the
break — a strategic-mix change in one of the companies, a
regulatory event that hits one and not the other, a takeover.
A spread that goes to -3.5 *with no fundamental story* is more
likely to revert than one that goes to -2.5 *with* a clear
story. Trade the fundamental, not just the Z-score.

**Q5: How does pair trading interact with taxes?**

A: Poorly, in a US taxable account. Pair trades have short
holding periods on average (weeks to a few months), so realised
gains are short-term — taxed at ordinary income rates, not
long-term capital. The tax drag on a pair-trading book is one
of the largest hidden costs. This is one reason institutional
pair traders run inside tax-deferred wrappers (pension money,
insurance separate accounts) where the structural tax disadvantage
is absent.

**Q6: How do dividends work for the short leg?**

A: You owe them. If you are short PEP across the ex-dividend
date, the dividend is debited from your account on pay-date and
credited to the lender. There is no offset. For dividend-rich
pairs (utilities, REITs), this is a meaningful drag and must be
included in the per-trade cost calculation.

**Q7: What's the difference between pair trading and statistical
arbitrage?**

A: Stat arb is pair trading scaled up: the same Z-score logic, but
applied across hundreds-to-thousands of pairs simultaneously,
with multi-factor decomposition (sector neutralisation, factor
neutralisation), with optimised execution (VWAP/TWAP, dark pools),
and held for shorter horizons (intraday to a few days). Pair
trading is the educational unit; stat arb is the production
implementation.

**Q8: Why did the 2007 quant quake hit specifically pair traders?**

A: Because the universe of "pairs" identified by a standard
cointegration screen is largely the same across funds — the same
sector pairs, the same factor neutralisations, the same
optimisation. When one large player has to liquidate, they unwind
*the same trades* that everyone else is on. Diversification in
trade count does not help when the trades themselves are factor-
correlated.

**Q9: Can I use options instead of stock for the short leg?**

A: Yes, and for retail it's often cleaner — buy a put on the
expensive leg instead of shorting the stock. You avoid borrow,
locate, and dividend obligations. You pick up theta decay and a
volatility-dependent premium, and the linear-spread P&L is
distorted into something more option-like. For a small retail
sleeve where operational simplicity dominates, options-based
pairs are a reasonable choice. The barbell logic
naturally points here.

**Q10: How does pair trading fit with the four tranches?**

A: Pair trading is *opportunistic* — it sits in the third tranche
alongside specific structural-alpha trades. It is not bedrock
(too volatile, too operationally demanding), not core (it doesn't
target a long-run risk premium), and not asymmetric speculation
(no convex payoff). It earns its place by being roughly
orthogonal to the rest of the portfolio.

**Q11: What does a typical pair-trading sleeve P&L look like?**

A: Many small wins (50-150 bps each on the gross), occasional
regime breaks that cost 200-500 bps, and a flat-line during
periods of compressed cross-sectional vol. Annualised return on
the sleeve is typically in the 4-8% range gross, with realised
vol of 5-10%. After fees and taxes for retail, considerably
less. The chart shape is "many small steps up, occasional cliffs
down," and the Sharpe ratio is the metric that matters — not the
absolute return.

**Q12: What should I read next if I want to actually build this?**

A: Three things. (a) The original Gatev-Goetzmann-Rouwenhorst
paper (2006) on pair trading — the academic baseline. (b)
Khandani-Lo (2007), the post-mortem on the August 2007 quant
quake. (c) The chapters in Lopez de Prado's *Advances in
Financial Machine Learning* on cointegration and triple-barrier
labelling. Read in that order — academic foundation, the war
story, then the modern toolkit.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Pair Trading — The Simplest Equity-Hedge-Fund Strategy in the Book | Week 14

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO]**

**Horace:** Last week, we talked about long-short. The architecture.
This week, we're going to apply that architecture to its narrowest,
most teachable case. Two stocks. One long, one short. Equal dollar.
That's it. Pair trading.

**Stella:** Why pair trading?

**Horace:** Because it's the cleanest place in retail-accessible
finance to learn what relative value actually means. By the end of
this video, you'll know what a Z-score is, why correlation is not
the same as cointegration, why most pair trades work most of the
time and one in twenty blows up, and what happened in August 2007
when too many people were running the same pair-trading models at
the same time.

**Stella:** Let's go.

---

**[SEGMENT 1: THE REFRAME]**

**Horace:** Long-only investing asks "is KO cheap." That's an
absolute question. The answer requires you to have a view on KO's
earnings, the multiple, the discount rate, the equity risk premium.
A lot of moving parts. You can be right on all of them and still
lose money if the consumer staples sector falls 15% next month.

Pair trading asks a different question. "Is KO cheap *relative to*
PEP?" That's a relative question. Both companies share the same
customer base, the same regulatory regime, the same exposure to
sugar prices, to aluminium prices, to a strong dollar quarter, to
a defensive consumer-staples factor. All of those drivers cancel
out when you go long one and short the other at equal dollar. What's
left is the company-specific operational variance.

**Stella:** And that's what you trade.

**Horace:** That's what you trade. You're betting that the
*difference* between two near-identical stories is mean-reverting.
Sometimes it is, sometimes the difference turns out to be a
permanent regime shift, and that's the whole game.

---

**[SEGMENT 2: BUILDING THE SPREAD]**

[VISUAL: image/week14_kopep_spread.png]

**Horace:** Here's the spread. Top panel is KO and PEP, daily, from
2015 through 2024, both rebased to 100 at the start of 2015.

**Stella:** They don't move identically.

**Horace:** They don't. PEP outperformed for big stretches because
of its snack-foods business. But notice how they generally move
*together* on the macro shocks — March 2020, the 2022 inflation
selloff. The differences are smaller than the shared moves. That's
the structural cointegration showing up visually.

**Stella:** And the bottom panel?

**Horace:** Bottom is the rolling 60-day Z-score of the log-spread.
We take log of KO minus log of PEP. Compute a 60-day rolling mean
and rolling standard deviation. Subtract the mean, divide by the
stdev. What you get is a normalised series that, in a stable
cointegration, sits inside +/-2 most of the time and visits the
tails when the spread dislocates.

**Stella:** So when the line touches +2, KO is two standard
deviations rich versus PEP.

**Horace:** And when it touches -2, KO is two standard deviations
cheap versus PEP. The pair trader's question, looking at this
chart, is: *do I trust that it'll come home, and how long will it
take?*

---

**[SEGMENT 3: CORRELATION VS COINTEGRATION]**

**Horace:** Critical distinction. Most retail traders conflate these.

Correlation measures whether two return series move together over
the short horizon. Two stocks with monthly correlation of 0.85
just means their monthly returns line up.

Cointegration is stronger. Two price *levels* are cointegrated if
the spread between them is stationary — has a stable mean, stable
variance, mean-reverts.

**Stella:** And you can have one without the other?

**Horace:** Yes. That's the trap. Imagine two stocks both in a
strong uptrend. They both go up 30% a year for ten years. Their
monthly returns are highly correlated. But the *gap between them*
might be widening monotonically, because one's compounding faster
than the other. High correlation, no cointegration. A pair trader
fading that widening gap loses every quarter for ten years.

**Stella:** What's the practical test?

**Horace:** Look at the spread Z-score over a five-to-ten-year
window. Ask yourself: "does this thing repeatedly come home after
each excursion?" If yes, the math is mostly confirming what your
eye saw. If no, no statistical test will rescue you. Cointegration
is something you can usually see before you formally test it.

---

**[SEGMENT 4: THE FOUR CLASSIC PAIRS]**

**Horace:** Four canonical pairs every quant has run.

KO and PEP. Beverages. Same customer, same commodity inputs, same
defensive multiple. Spread breaks only when one company changes its
business mix — PEP's snack-foods build is the textbook example.

V and MA. Visa and Mastercard. Regulatory duopoly, near-identical
economics. Spread breaks on company-specific litigation or
geographic mix.

XOM and CVX. ExxonMobil and Chevron. Both integrated supermajors,
similar reserves, similar geography. Spread breaks on idiosyncratic
operational events — refinery accidents, cost overruns.

GLD and SLV. Gold and silver. Share a monetary debasement story.
Silver is half industrial. The gold-silver ratio cycles between 50
and 90. That cycle is your cointegration.

**Stella:** They all have the same shape. Two near-identical stories
that diverge on a contained dimension.

**Horace:** Exactly. The structural driver nets out. The *contained*
idiosyncratic driver is what you get paid for.

---

**[SEGMENT 5: ENTRY EXIT RULES]**

[VISUAL: image/week14_pair_pnl.png]

**Horace:** Textbook ruleset. +/-2 sigma to enter, zero to exit.

Z below -2: long the spread. Long KO, short PEP at equal dollar.
Z above +2: short the spread. Short KO, long PEP.
Z crosses zero: exit. Don't wait for the opposite tail. The
marginal expected return from running another sigma is small and
the regime-change risk grows with holding period.

If Z extends past +/-3 or +/-4 in the wrong direction: cut. The
relationship has probably broken. Don't martingale.

**Stella:** What does the resulting P&L look like?

**Horace:** Bottom panel shows the cumulative log-spread P&L over
ten years. Many small wins. Some flat periods. Occasional cliffs
down where a spread didn't revert and we cut. That shape — many
small wins, occasional regime-break losses — is the *signature*
of a structural-alpha return stream. It's also why you run a book
of thirty pairs, not one pair. The law of large numbers is what
makes this strategy work.

**Stella:** So one-pair retail is mostly education, not alpha.

**Horace:** Mostly education. Run one or two pairs in tiny size.
Learn the operational mechanics. Borrow rates, dividends, margin
calls. Then either scale up to a real book or buy a market-neutral
fund and let someone else run it.

---

**[SEGMENT 6: THE 2007 QUANT QUAKE]**

**Horace:** The most important risk story in pair trading. First
week of August 2007. The standard equity-stat-arb book lost
between four and twelve sigma of its expected daily return for
four straight days. AQR. RenTech's market-neutral fund. Goldman's
quant book. Some funds halved in a week.

**Stella:** What happened?

**Horace:** One of the largest multi-strats — the public
reconstruction mostly points at Goldman, the precise actor matters
less than the mechanism — had to deleverage its equity book
suddenly. Probably triggered by a margin call from a totally
unrelated subprime mortgage book. To unwind the equity book, they
had to sell the long leg and buy back the short leg of every pair
trade simultaneously.

**Stella:** And every other quant had the same pairs.

**Horace:** *Exactly*. Because every quant runs a cointegration
screen against the same factor data, the *universe of pairs* is
nearly identical across funds. So when Goldman starts unwinding,
all the other funds' books move adversely at the same time.
Losses mount. More funds are forced to deleverage. The pairs move
further. More forced sales. It cascades for four days.

**Stella:** What's the lesson?

**Horace:** Crowding itself becomes a regime. **Your alpha
is alpha only as long as the population running it is small enough
that no forced exit can simultaneously move all your trades.** The
day too many people run the same model, the model itself becomes
the risk factor. Modern stat arb runs a continuous "crowdedness
factor" — measuring how many other funds are likely on the same
trade — and dials gross down when crowdedness rises. Retail traders
inherit the same discipline in miniature: don't oversize a famous,
canonical pair.

---

**[SEGMENT 7: BARBELL POSITIONING]**

**Horace:** Where does this fit in the portfolio?

The barbell. Most of your wealth at the
safety end — cash, Treasuries, gold, deep-ITM long-dated calls on
names you'd own anyway. A small sleeve at the alpha end. Pair
trading lives at the alpha end.

**Stella:** Sized how?

**Horace:** Single-digit percentage of total portfolio. The gross
exposure is two to three times sleeve size — long $X plus short
$X is gross 2X — and the net is approximately zero by construction.

**Stella:** And the contribution?

**Horace:** Small in absolute return. Maybe 0.3 to 0.8 percent on
the total portfolio if the sleeve runs 4-8% on itself. But the
contribution to the *Sharpe ratio* of the total portfolio is
larger, because the sleeve's returns are roughly orthogonal to
your long-only book.

This is the right way to think about pair trading for a retail
investor. Not as a way to compound wealth. As a way to **reduce
the variance of the wealth path**. It's a Sharpe-ratio play, not
a return play.

**Stella:** Anyone who promises double-digit pair-trading returns
with low drawdowns —

**Horace:** Is over-fitted, levered, or selling a course. Probably
all three.

---

**[SEGMENT 8: THE INTERACTIVE]**

**Horace:** Below the script there's an interactive lab. Pick one
of four pre-loaded pairs. KO/PEP, V/MA, XOM/CVX, GLD/SLV. Slide
the entry Z-score, the exit Z-score, the lookback window. Watch
the cumulative P&L, the trade count, the win rate, and the
Sharpe ratio respond in real time.

**Stella:** What's the right calibration?

**Horace:** Try the textbook +/-2 entry, 0 exit, 60-day lookback
first. Then push the entry threshold tighter — say +/-1.5 — and
notice you fire more trades but each trade is lower-edge. Push
it wider — +/-2.5 — and you fire fewer but cleaner trades. There's
no global optimum across pairs. The point is to *feel* how
sensitive the strategy is to its parameters. If a small change in
threshold flips the P&L sign, the strategy was over-fit. If the
P&L is robust across a band of parameters, you have something.

---

**[OUTRO]**

**Horace:** Pair trading. Long the cheap leg, short the rich leg,
exit on the mean. The simplest equity-hedge-fund strategy in the
book.

**Stella:** And the right next step in the long-short toolkit you
started learning last week.

**Horace:** Three takeaways. One — **correlation is not
cointegration**, and the trap is fading a widening spread that
isn't actually mean-reverting. Two — **the structural alpha is
real but conditional**: real because the pair trader supplies
liquidity to the dislocated leg; conditional because the
cointegration can break and the strategy can crowd. Three —
**run it as a sleeve, not as a substitute**. Single-digit
percentage of portfolio, sized for Sharpe contribution, not for
absolute return.

**Stella:** Next week we move to volatility — Week 15 is "Volatility
as an Asset Class." VIX, vol-of-vol, the persistent risk premium
in selling vol. Same long-short architecture, applied to a
non-equity instrument.

**Horace:** See you next week.

---
