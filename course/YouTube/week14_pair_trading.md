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
