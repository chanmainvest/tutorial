## Part 2: YouTube Script

---

**VIDEO TITLE:** Position Sizing — The Most Under-Rated Discipline in Investing
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Stella:** Welcome back to the channel. I'm Stella, and as
always I'm here with Horace. Horace, today's topic is
position sizing, stop losses, and Kelly. Tell me why this is
the lesson you said *most* retail investors skip.

**Horace:** Because it's invisible work, Stella. Picking the
stock feels like investing. Sizing it correctly feels like
admin. So most people spend ninety percent of their time on
the pick and ten percent on the size — and that's exactly
backwards. Sizing dominates long-run wealth more than any
single pick you'll ever make.

**Stella:** Counter-intuitive.

**Horace:** Completely. Here's the headline. Two investors
have the same identical thesis on the same stock. Investor A
sizes it at 5% of bankroll with a quarter-Kelly bet. Investor
B sizes it at 50% with full Kelly and a margin loan. Same
thesis. Same direction. Same return per dollar deployed. Over
twenty years, A compounds to a fortune. B has blown up
somewhere between year three and year seven, almost
guaranteed by the math.

**Stella:** Even if B is right?

**Horace:** *Especially* if B is right on average. Because
"right on average" includes a sequence of three or four
losing trades in a row, and B's sizing makes that sequence
fatal. The anchor is simple: the market can stay irrational
longer than you can stay solvent. If you're not solvent, your
edge doesn't compound. It just stops.

---

**[SECTION 1 — KELLY CRITERION — 1:10]**

**Stella:** Let's start with Kelly. You wrote the formula: $f
\text{ star} = (b p - q) / b$.

**Horace:** John Kelly, Bell Labs, 1956. He was working on
information theory and noticed the same math applies to
betting. The question: if you have a repeated bet with edge,
what fraction of your bankroll should you risk to maximise
the long-run *geometric* growth rate?

**Stella:** Why geometric, not arithmetic?

**Horace:** Because you compound. A bet that wins 100% half
the time and loses 50% half the time has positive arithmetic
expectation — $0.5 \times 1.0 + 0.5 \times (-0.5) = 0.25$, a
+25% expected return. But geometrically, you multiply 2.0 by
0.5 and you're back where you started. Your geometric growth
rate is zero. Kelly maximises the geometric rate.

**[VISUAL: image/week41_kelly_curve.png]**

**Stella:** What's the chart showing?

**Horace:** Full-Kelly fraction $f$ star plotted against win
rate $p$, for five different reward-to-risk ratios. Look at
the central line, the 1:1 case — that's a coin flip with a
slight edge. At $p = 0.52$, which is about what an equity
strategy with mild positive expectancy looks like, full Kelly
is right around 4%. Four percent of bankroll per trade. That
is *full* Kelly — the maximum.

**Stella:** And quarter-Kelly is one percent.

**Horace:** One percent per trade, yes. That's where most
serious retail traders live. The reason isn't superstition —
it's the math of edge uncertainty.

---

**[SECTION 2 — FRACTIONAL KELLY — 4:00]**

**Stella:** Walk me through why fractional Kelly is the
default.

**Horace:** Two reasons. First, the penalty for under-betting
is mild. At half-Kelly you capture about 75% of the growth
rate of full Kelly. At quarter-Kelly you still get 44%.
Compare that to over-betting: at *twice* Kelly your expected
growth rate is *zero*, and beyond that you lose money even
with positive edge. So the cost of being a little too small
is small; the cost of being a little too big is catastrophic.

**Stella:** Asymmetric penalty.

**Horace:** Right. Second reason — variance. Full Kelly on
equities can produce 70-80% drawdowns. Quarter-Kelly keeps
them under 25%. And remember: the drawdown is the thing that
ends your career, not the average return. Edward Thorp ran
half-Kelly for everything he did at his hedge fund, for
twenty years. If Thorp can settle for half-Kelly, you can
settle for quarter.

---

**[SECTION 3 — THE 1-2% RULE — 6:00]**

**Stella:** Most professional traders don't think in Kelly
terms day to day, do they?

**Horace:** No, they think in dollar-at-risk per trade. The
canonical rule: **never lose more than 1 to 2 percent of
bankroll on any single trade**. That's it. Whatever your
sizing math gives you, cap it at 2%.

**Stella:** Math example?

**Horace:** Bankroll \$100,000. Max loss 1%. That's \$1,000
of dollar-at-risk. You're looking at a stock at \$80 with a
stop at \$76. Loss per share at the stop is \$4. So you can
buy 250 shares — about \$20,000 of notional. The stop, not
the share count, drove the position size.

**Stella:** And if your stop were tighter?

**Horace:** Closer stop, bigger position. Stop at \$78
instead of \$76 — loss per share is \$2 — you can buy 500
shares, \$40,000 of notional. Same dollar-at-risk. Twice the
notional. People get this backwards all the time. They pick a
share count first and let the stop move; that's how 1% trades
turn into 5% losses.

---

**[SECTION 4 — STOPS VERSUS HEDGES — 8:30]**

**Stella:** When do I use a stop and when do I use a hedge?

**Horace:** Three rules. One: stop when the *thesis* could be
invalidated by a known event. Earnings, FDA, Fed meeting.
The thesis dies, the trade dies. Two: hedge when the thesis
is right but the *path* is volatile. You believe NVDA is
fairly valued for next year; you don't want to ride a -30%
interim dip. Collar it — long stock, short an out-of-the-
money call, long an out-of-the-money put. The position stays
alive; the tail is amputated.

**Stella:** And rule three?

**Horace:** Use neither when the position is small enough not
to need either. A 1% position needs no stop. A 25% position
needs both. Position sizing is the cheapest insurance you've
ever bought.

**Stella:** What's the failure mode of a stop?

**Horace:** Gap risk. Stock closes at \$80, your stop is \$76,
overnight news opens it at \$65 — you fill at \$65, not at
\$76. A long put doesn't have that problem because it's
already in your account.

---

**[SECTION 5 — CORRELATION-ADJUSTED SIZING — 11:00]**

**Stella:** What about multiple positions?

**Horace:** The 1-2% rule per trade *assumes* the trades are
independent. They're not. If you're long ten semiconductors
and Nasdaq sells off, all ten move together. Your effective
single-trade exposure is much higher than ten separate 2%
trades.

**Stella:** Fix?

**Horace:** Bucket the correlated names. All semis are one
bucket. Cap that bucket at 6-10% total dollar-at-risk. Then
apply the 1-2% rule *within* the bucket — for six semis at
8% bucket cap, that's about 1.3% each. When the sector
rotates, your loss is bucket-capped, not position-summed.
Institutional risk parity does this with a covariance matrix.
Retail does it with bucket arithmetic. Same idea.

---

**[SECTION 6 — LEVERAGE AND DRAWDOWN — 13:00]**

**Stella:** Let's talk about leverage. You said something
non-obvious — that 2x leverage roughly *doubles* the
drawdown.

**Horace:** Closer to multiplicative than additive, yes. A
diversified equity book with a -25% peak-to-trough drawdown
unlevered becomes -50% at 2x and -75% at 3x. Plus you're
paying borrow cost — call it 5% a year at retail margin
rates — which eats your equity *during* the drawdown, when
you can least afford it.

**[VISUAL: image/week41_leverage_drawdown.png]**

**Horace:** The chart simulates a 30-year horizon for a
strategy with 10% expected return and 16% annualised vol,
across leverage from 1.0 to 3.0. Look at the shape. From 1.0
to 1.5 the line climbs roughly linearly — manageable. From
1.5 to 2.0 it bends upward. Beyond 2.0 it goes vertical. At
3x the expected worst drawdown over thirty years is around
-85%. That's not a drawdown; that's a margin call followed
by a forced liquidation followed by a closed account.

**Stella:** The blowup is non-linear.

**Horace:** The blowup is *aggressively* non-linear. Fat-tailed
volatility
is operating at full strength here: vol is normal in the
textbook, fat-tailed in real life, and leverage turns the
fat tail into the un-survivable tail.

---

**[SECTION 7 — INTERACTIVE WALK-THROUGH — 15:00]**

**Stella:** Let's open the position sizer.

**[VISUAL: interactive/week41_position_sizer.html]**

**Horace:** Five sliders. Bankroll. Max loss per trade as a
percent. Your expected edge per trade in basis points. Your
edge confidence — that's the Kelly fraction, 0 to 1. And
per-trade volatility.

**Stella:** Let me set bankroll to 100k, max loss 1%, edge
50 bps, confidence 0.25 — quarter-Kelly — vol 5%.

**Horace:** Output is recommended position size, max
position count, expected drawdown over a thousand trades,
and blowup probability. With those settings, the sizer
should give you something like \$10,000 per position with
ten simultaneous positions, expected drawdown around 15%,
blowup probability essentially zero.

**Stella:** Now I'll crank confidence to 1.0 — full Kelly —
and vol up to 12%.

**Horace:** Watch the blowup probability. It moves from
near-zero to multiple percent. That's the chart's whole
point. Confidence in your edge estimate is the lever
between "compound for thirty years" and "blow up by year
five." Play with it. Get a feel for the shape.

---

**[OUTRO — 17:30]**

**Stella:** Final word, Horace.

**Horace:** Same as every lesson on risk: sizing is the only
knob you fully control. You can't make the market trend up.
You can't force your edge to be real. But before you click,
you absolutely choose how much capital is on the line. That
single decision dominates your long-run wealth more than any
view, any pick, any timing. The anchor is staying
solvent longer than the market stays irrational. The warning is that
volatility is fat-tailed in real life, especially under leverage.
Quarter-Kelly. One to two percent per trade. Bucket your
correlated bets. Cap leverage at 1.5x. Use stops for thesis-
events and hedges for path-volatility. That's the discipline.
It will not make you rich. It will let you stay in the game
long enough to *get* rich.

**Stella:** Thanks for watching. See you next week.
