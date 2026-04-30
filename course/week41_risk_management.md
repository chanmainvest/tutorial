# Week 41: Risk Management — Position Sizing, Stop Losses, Kelly, and Bankroll Preservation

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Every retail loss-blowup story you have ever read shares the same
shape. The investor was usually right about *direction* and wildly
wrong about *size*. The Reddit screenshot showing "$50k lost on
weekly SPY puts" is rarely a story of a bad thesis; it is almost
always a story of a fine thesis sized at four times the bankroll
the investor could survive. Position sizing is the most under-
rated discipline in all of investing. It is what separates people
who compound for thirty years from people who blow up in three.

You need this material for four reasons.

1. **Sizing is the only knob you fully control.** You cannot make
   the market trend up. You cannot force your edge to be real.
   But you absolutely choose, before you click, what fraction of
   your capital is in this trade. That single decision dominates
   long-run wealth more than any view, any pick, any timing.
2. **The math of drawdowns is asymmetric.** A -50% drawdown
   requires a +100% recovery. A -75% drawdown requires +300%. A
   -90% drawdown requires +900%. Sizing dictates how deep your
   worst drawdown goes; recovery cost grows non-linearly. SOUL
   #12 — staying *solvent* longer than the market stays
   irrational — is impossible without sizing.
3. **Edge is uncertain. Kelly is uncertain too.** The Kelly
   criterion gives you the geometric-growth-maximising bet size
   *if* your edge estimate is correct. In equities, your edge
   estimate is never correct to the third decimal. Fractional
   Kelly — a quarter or even an eighth of full Kelly — is the
   honest answer to that uncertainty.
4. **Leverage is the silent multiplier of every mistake.** Two-
   times leverage doubles your return *and* your variance. But
   for max drawdown, the relationship is closer to multiplicative:
   a -25% drawdown at 1x becomes roughly -50% at 2x. Three times
   leverage on a 16% vol equity book turns a survivable bear
   market into a margin-call event. The blowup is non-linear.

This lesson works through Kelly, fractional Kelly, the 1-2% per-
trade rule, stop losses versus hedges, correlation-adjusted
sizing for multi-position books, and the leverage-versus-drawdown
math. It then ties the whole thing back to SOUL #6 (vol-tail-wags-
dog) and SOUL #12 (irrational > solvent).

---

### 2. What You Need to Know

#### 2.1 The Kelly Criterion — Geometric-Growth-Optimal Bet Size

John Kelly (Bell Labs, 1956) asked a simple question: if I have a
repeated bet with edge, what fraction of my bankroll should I
risk each time to maximise the long-run *geometric* growth rate
of my wealth? The answer for a binary win/lose payoff is:

$$ f^* = \frac{b p - q}{b} $$

where:

- $p$ = probability of winning,
- $q = 1 - p$ = probability of losing,
- $b$ = net odds received on a win (so a 1:1 bet has $b = 1$, a
  2:1 bet has $b = 2$).

Plug in a coin-flip with 55% heads and 1:1 odds: $f^* = (1 \cdot
0.55 - 0.45) / 1 = 0.10$. Kelly says bet ten percent of your
bankroll on each flip. Above ten percent, the geometric growth
rate falls. Above twenty percent — twice Kelly — your expected
long-run growth becomes *zero*. Above $f = 2 f^*$ you are
mathematically guaranteed to ruin yourself given enough trials,
even with a positive edge.

For equity strategies, the win rate is rarely above 55% and the
average win-to-loss ratio is rarely above 1.5. A typical setup
might be $p = 0.52$, $b = 1$, giving $f^* = 0.04$ — about four
percent of bankroll per trade. That is the universe you are
operating in. You are not in a 1956 horse-race. You are in a
near-fair-coin world where Kelly outputs single-digit percentages.

`[VISUAL: image/week41_kelly_curve.png]`

The chart shows full-Kelly $f^*$ as a function of win rate $p$
across five payoff ratios. Notice three things. First, at the
typical equity-edge point ($p \approx 0.52$, $b = 1$) full Kelly
is around four percent. Second, the curve is steeper than people
expect — moving win rate from 50% to 55% triples Kelly. Third,
when $p < q / b$ (the no-edge boundary) Kelly goes negative,
which is the maths politely telling you not to take the bet.

#### 2.2 Fractional Kelly — The Honest Answer to Edge Uncertainty

Full Kelly assumes you *know* your edge. In practice you are
estimating $p$ and $b$ from a finite track record, and the
standard error of that estimate is large. Edward Thorp, the
mathematician who beat Vegas blackjack and ran a hedge fund for
two decades, settled on **half-Kelly** for everything he did.
The general formula for $k$-fractional Kelly:

$$ f_k = k \cdot f^* $$

with $k$ commonly chosen as $0.5$ (half-Kelly), $0.25$ (quarter-
Kelly), or $0.125$ (eighth-Kelly). Two facts make fractional
Kelly the default rather than full Kelly.

First, **the geometric-growth penalty for under-betting is mild**.
At half-Kelly you capture roughly 75% of the optimum growth rate.
At quarter-Kelly you still capture about 44%. The penalty for
*over-betting*, however, is severe and asymmetric: at twice
Kelly you grow at zero, and beyond that you lose money in
expectation. So shading toward smaller-than-optimal is cheap
insurance.

Second, **the variance reduction is enormous**. Half-Kelly cuts
your drawdowns roughly in half compared to full Kelly. Quarter-
Kelly cuts them again. For a strategy with a 30% annualised
volatility, full Kelly produces drawdowns that can hit 80%;
quarter-Kelly keeps them under 25%. SOUL #12 — staying solvent
longer than the market stays irrational — is the entire reason
quarter-Kelly is the industry standard for stock strategies.

The honest rule for retail: when you have a directional view on
an individual stock, **size at quarter-Kelly or smaller**. When
you have an index-level view, the same rule applies. Full Kelly
is for blackjack tables where you literally counted the deck. It
is not for your tax-deferred account.

#### 2.3 The 1-2% Per-Trade Loss Rule

Professional traders rarely think in Kelly terms day to day.
They think in a much simpler frame: *what is the maximum dollar
loss I am willing to take on this single position?* The
canonical rule is **one to two percent of total bankroll**.

Mechanics: if your bankroll is \$100,000 and your max loss per
trade is 1%, you are willing to lose \$1,000 on this trade. If
your stop is \$5 below entry on a \$100 stock, your position
size is $1{,}000 / 5 = 200$ shares — \$20,000 of stock. If your
stop is \$2 below entry, your position size is $1{,}000 / 2 =
500$ shares — \$50,000. The dollar-at-risk drives the share
count, not the share count driving the dollar-at-risk.

Why the 1-2% range works:

- At 2% per loss, twenty consecutive losses produce roughly a
  $1 - 0.98^{20} \approx 33\%$ drawdown. Survivable.
- At 5% per loss, twenty consecutive losses produce a $1 -
  0.95^{20} \approx 64\%$ drawdown. Career-ending.
- At 10% per loss, twenty consecutive losses leave you with
  $0.9^{20} \approx 12\%$ of your starting capital. Game over.

The 1-2% rule does not assume you are a great trader. It assumes
you are an average trader who will, sooner or later, encounter a
losing streak. Sized at 2%, you survive that streak. Sized at
10%, you do not.

#### 2.4 Stop Losses versus Hedges — Two Different Tools

A **stop loss** is an exit. You decide, before entering the
trade, the price at which you will close the position and accept
the loss. The trade is then over — no more upside, no more
downside. Mechanically: a stop-loss order at the broker, or a
mental stop you actually honour.

A **hedge** is a capped-loss overlay that *keeps the position
open*. Long 100 SPY at \$520 with a \$500 protective put: your
maximum loss is capped at \$20 per share plus the premium,
*and* you keep all the upside above \$520 minus the premium.
The position is alive; only the tail is amputated.

Three rules for choosing between them:

1. **Use a stop when your conviction is event-dependent.** If a
   key earnings number, an FDA decision, or a Fed meeting could
   invalidate your thesis, stop loss the position when the news
   prints. There is no point holding a thesis that has been
   refuted.
2. **Use a hedge when the thesis is right but the path is
   volatile.** If you think NVDA is fairly valued for a 12-month
   horizon but you cannot stomach a -30% interim drawdown,
   collar it (long stock + short OTM call + long OTM put). You
   keep the multi-year thesis alive while bounding the path-
   level pain.
3. **Use neither when the position is sized small enough that
   you do not need either.** This is the most under-used option.
   A 1% position needs no stop and no hedge. A 25% position needs
   both. Position sizing is the cheapest insurance you have ever
   bought.

Stops have a known failure mode: gap risk. If overnight news
opens the stock 20% below your stop, you fill at the open, not
at the stop. Hedges with options do not have that failure mode
because the put has already been bought.

#### 2.5 Correlation-Adjusted Sizing for Multi-Position Books

The 1-2% rule per trade assumes trades are *independent*. They
are not. If you are long ten tech stocks and the Nasdaq sells
off 5%, all ten move together. Your effective single-trade
exposure is much higher than the per-trade rule suggests.

The fix is to think in terms of **correlated dollar-risk
buckets** rather than individual trades. A simple framework:

- All stocks in the same sector count as one bucket. Cap that
  bucket at 6-10% total at-risk.
- All positions correlated to a single macro factor (rates,
  USD, oil) count as one bucket. Same cap.
- Apply the 1-2% rule *within* each bucket, after the bucket
  cap.

Concretely: if you want to be long six semiconductors, do not
size each at 2%. Size the *aggregate* tech-sector at 8%, then
divide that across the six names — about 1.3% each. When the
sector rotates against you, your loss is bucket-capped, not
position-summed.

The institutional version of this is **risk parity**: weight
positions inverse to their volatility, then apply a covariance
overlay to scale down correlated bets. Retail does not need the
matrix algebra; the bucket rule captures 80% of the benefit.

#### 2.6 Leverage and Drawdown — The Asymmetric Blowup

Leverage scales both return and variance, but its effect on
drawdowns is **non-linear and asymmetric**. The intuition:

$$ \text{DD}_{\text{lev}} \approx (1 + L) \cdot \text{DD}_{\text{unlev}} \quad \text{(plus financing drag)} $$

A diversified equity book with a -25% peak-to-trough drawdown at
1x becomes roughly -50% at 2x leverage and -75% at 3x. Add the
borrow cost (currently \~5% annual at retail margin rates) and
the realised drawdown is even worse, because the drag eats into
your equity *during* the drawdown, when you can least afford it.

`[VISUAL: image/week41_leverage_drawdown.png]`

The chart simulates expected max drawdown over a 30-year horizon
for a strategy with 10% expected return and 16% annualised
volatility, across leverage levels from 1.0 to 3.0. Notice the
shape. From 1.0 to 1.5 the curve climbs roughly linearly. From
1.5 to 2.0 it bends upward. Beyond 2.0 it goes vertical: at 3x,
the expected worst drawdown over thirty years is around -85%,
which is a polite way of saying *margin call, position liquidated
at the worst possible moment, account closed*.

The lesson: leverage above 1.5x is a different sport. You can do
it, but you must size the *underlying* position much smaller to
keep the *levered* drawdown survivable. That defeats the point of
the leverage. SOUL #6 is operating at full strength here:
volatility is normally distributed in textbooks, fat-tailed in
real life, and leverage makes the fat tail unsurvivable.

#### 2.7 The Bankroll Preservation Mindset

Everything in this lesson sits on top of a single mental model:
**your bankroll is the asset**. Trades are merely instruments
through which the bankroll grows or shrinks. The job is not to
"win the trade." The job is to *keep playing* — to remain
solvent through any sequence of outcomes the market can produce,
so the long-run edge has time to compound.

This is what SOUL #12 means by *the market can stay irrational
longer than you can stay solvent*. The investor who blows up in
2022 is not the one who was wrong about the Fed. The investor
who blows up in 2022 is the one who was right about the Fed but
sized the bet at full Kelly, took 3x leverage, and did not put a
hedge on. The thesis worked. The sizing did not.

The bankroll preservation rules, in priority order:

1. Never lose more than 1-2% of bankroll on any single trade.
2. Never lose more than 6-10% of bankroll on any single sector
   or factor.
3. Never run leverage above 1.5x on equities, or 1.0x if the
   underlying strategy is itself volatile (options, crypto,
   single names).
4. Always size at quarter-Kelly or smaller until you have ten
   years of out-of-sample performance proving your edge
   estimate.
5. Always know what would have to happen for you to be ruined,
   and price the option that would prevent it.

These five rules will not make you rich. Skill, time, and a
working edge will. But these rules will *let you stay in the
game long enough* for the skill, time, and edge to do their
work. That is the entire point.

---

### 3. Common Misconceptions

1. **"Bigger size = bigger profit."** Linear in expectation,
   geometric in reality. Above $2 f^*$ you grow at zero. Above
   $3 f^*$ you lose money even with positive edge.
2. **"I have an edge, so I should bet full Kelly."** You do not
   *know* your edge. Half-Kelly captures 75% of the growth and
   cuts drawdowns in half. Quarter-Kelly is the retail default.
3. **"A stop loss means I lose money."** A stop loss means you
   *control* the size of the loss. The alternative is letting
   the market decide.
4. **"Hedging is expensive."** Compared to a margin call,
   hedging is the cheapest line item on your statement. The
   right comparison is hedge cost vs probability-weighted
   blowup cost, not hedge cost vs zero.
5. **"2x leverage doubles my return."** It also doubles your
   variance and roughly doubles your drawdowns. The expected
   geometric return is $L \mu - 0.5 L^2 \sigma^2$ — not linear
   in $L$.
6. **"Leveraged ETFs are 2x exposure forever."** They are 2x
   *daily* exposure. Over time, vol decay subtracts roughly
   $0.5 (L^2 - L) \sigma^2$ per year. See Week 37.
7. **"My positions are uncorrelated."** Stocks in the same
   sector correlate at 0.6-0.9 in normal times and at 0.95+ in
   crashes. Correlations rise to one in the moments you most
   need diversification.
8. **"I can use mental stops."** Mental stops fail when the
   trade is losing money, which is the only time they matter.
   Use the broker's stop or do not use one.
9. **"Risk management is for losers."** Risk management is what
   keeps the winners winning. The hedge funds that have been
   open for thirty years are the ones with risk officers who
   say no.
10. **"I'll add risk after a winning streak."** This is the
    inverse of the right rule. Add risk after *bankroll has
    grown*, never after *streak has happened*. The two are
    different signals.

---

### 4. Q&A Section

**Q1: I have $50,000 and want to risk 1% per trade. The stock is
\$80 with a stop at \$76. How many shares?**
Risk per trade = \$500. Loss per share at stop = \$4. Position =
$500 / 4 = 125$ shares = \$10,000 notional (20% of bankroll).
The position is 20% of the account but the *risk* is 1%. That is
the distinction sizing makes.

**Q2: Why quarter-Kelly and not half-Kelly?**
Half-Kelly assumes your edge estimate has modest error. For
discretionary equity trades the edge estimate has large error
(you are guessing 52%-54% win rates from small samples). Quarter-
Kelly bakes that uncertainty in. If you have a true mechanical
strategy with thousands of trades and stable parameters,
half-Kelly is defensible.

**Q3: Should I use a trailing stop or a fixed stop?**
Fixed stops are cleaner for short-term trades — you defined the
thesis, you defined the invalidation, you exit at invalidation.
Trailing stops are better for trend-following positions where
you want to let winners run but lock in gains as the position
moves your way. They have a known failure mode: noise stops you
out before the trend resumes.

**Q4: Is selling cash-secured puts a "hedge"?**
No. Selling a put is a *short volatility* income trade with
defined upside (the premium) and large defined downside (strike
minus premium). It is not a hedge — it adds risk. Buying a put
is a hedge.

**Q5: How do I size options trades?**
Options sizing should be based on **maximum loss**, not
notional. A long call has max loss = premium. Size the premium
at 1-2% of bankroll. A short put has max loss = strike minus
premium. Size *that* at 1-2% of bankroll, which is much
smaller than 1-2% of premium received.

**Q6: My friend doubled his account on TSLA. Should I size up?**
No. He took an unsized bet and got lucky on a single draw. The
correct comparison is *over a thousand draws*, where the
unsized strategy goes to zero with probability one. Use his
result as a survivorship-bias data point, not a sizing
prescription.

**Q7: What's a reasonable max leverage for a buy-and-hold
investor?**
1.0x in tax-deferred accounts; 1.0x to 1.25x in taxable
margin accounts using box-spread financing; 1.5x only with a
written drawdown plan and an explicit liquidity reserve. Above
1.5x is leveraged trading, not buy-and-hold investing.

**Q8: How do I know if I'm over-sizing?**
The sleep test. If a -3% day on the position would change your
mood for the evening, you are over-sized. The position should
be small enough that the worst plausible day is annoying, not
distressing.

**Q9: What about Kelly when I have multiple simultaneous
positions?**
For independent positions, sum of $f^*$ values across positions.
For correlated positions, sum of $f^*$ divided by an effective-
correlation factor. The bucket rule from §2.5 is the practical
shortcut.

**Q10: Does the 1-2% rule apply to long-term index investing?**
No — it applies to active trades with explicit invalidation
points. A 100% index allocation in your retirement account is
not "violating the rule"; it is a different category of capital
with a different time horizon. The rule applies to your
*trading sleeve*, not your buy-and-hold sleeve. SOUL #14 — the
barbell — keeps these two sleeves separate by design.

**Q11: How does this connect to the four-tranche framework
(SOUL #13)?**
Each tranche has its own sizing rule. Growth: index-tracking,
no per-trade rule. Income: position size = yield target / asset
yield. Stores of value: fixed allocation, rebalanced. Opt: this
is where Kelly, fractional Kelly, and the 1-2% rule live. Risk
management discipline is loudest in the Opt tranche because
that is where unsized blowups happen.

**Q12: Can I use Kelly for crypto?**
You can compute it. The problem is your $p$ and $b$ estimates
are far less reliable than for equities, and crypto's drawdown
distribution has a fatter left tail than the normal model
underlying Kelly. Use eighth-Kelly or smaller, and treat all
sizing as provisional until you have a multi-cycle track record.

---

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
fatal. SOUL #12 is the anchor: the market can stay irrational
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

**Horace:** The blowup is *aggressively* non-linear. SOUL #6
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
view, any pick, any timing. SOUL #12 is the anchor — stay
solvent longer than the market stays irrational. SOUL #6 is
the warning — vol-tail-wags-dog, especially under leverage.
Quarter-Kelly. One to two percent per trade. Bucket your
correlated bets. Cap leverage at 1.5x. Use stops for thesis-
events and hedges for path-volatility. That's the discipline.
It will not make you rich. It will let you stay in the game
long enough to *get* rich.

**Stella:** Thanks for watching. See you next week.
