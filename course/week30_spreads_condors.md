# Week 30: Spreads, condors and butterflies — building the barbell out of options

---

## Part 1: Reading Section

---

### 1. Why This Is Important

The last four weeks taught the single-leg vocabulary: long calls and
puts as cheap directional bets, covered calls as a paid sell ticket,
cash-secured puts as a paid buy ticket, and the Greeks as the partial
derivatives that price the whole machine. Single legs are honest, but
they are also blunt. A naked short put on SPY at the $500 strike on a
$50,000 account ties up $50,000 of collateral and exposes you to a
$50,000 hole if the market goes to zero. That is not a position
sizing decision — that is a position the size of *the entire account*.

Spreads fix this. A spread is two (or four) options stitched together
on the same underlying so that the long leg *caps* the loss of the
short leg. The position now has a printed maximum loss the day you put
it on, a printed maximum profit, and a capital requirement equal to
the spread width minus credit received — typically one to three
hundred dollars per contract, not five-figure cash. The same $50,000
account can run *fifty* of these in parallel without ever risking the
account on a single tail.

This matters for four concrete reasons:

**(1) Defined-risk options ARE the barbell.** The barbell
holds high-conviction safety on one end and asymmetric, capped-loss
speculation on the other. A long-dated SPY call spread, an iron
condor on QQQ, a butterfly on AAPL into earnings — every one of these
has the *exact* structural property the barbell asks for: a known,
small, prepaid maximum loss in exchange for a payoff that need not be
linear in the underlying. The L3 ("asymmetric") sleeve is not built
from leveraged ETFs and lottery tickets; it is built from spreads.

**(2) Credit spreads are the engineered version of the L2 income
sleeve.** Week 27 sold covered calls and Week 28 sold cash-secured
puts; both work but both are capital-heavy. Replacing the cash-secured
put with a 5-wide bull put spread keeps the same directional thesis
("I'd buy this name lower"), keeps the same theta-positive carry, and
shrinks the capital requirement by 80-95%. The gross monthly yield
*on capital actually at risk* goes up; the dollar income goes down;
the survivability goes way up. Most professional premium sellers run
spreads, not naked options, for exactly this trade-off.

**(3) Iron condors monetise the fact that markets are mean-reverting
inside their realised range about 70% of the time.** An
iron condor profits when SPY closes between the two short strikes at
expiry. With short strikes at ±1 standard deviation and 30 days to
expiry, the lognormal probability of profit is ~68%; with shorts at
±0.75σ it is ~55%; with shorts at ±0.5σ it is ~38%. The trader picks
the spot on the probability curve they are willing to live with and
sizes the wings to cap the tail. This is mean-reversion *priced and
hedged* — not the retail version that holds a falling knife.

**(4) Butterflies and broken-wing butterflies are how you express a
*precise* view.** A long butterfly centred at $100 makes its maximum
profit if the stock pins at $100 at expiry and loses a small fixed
amount everywhere else. That is a bet on a *level*, not a direction.
A trader who has done the work on a name's earnings reaction or
options-expiry pin can express that view for one or two hundred
dollars of risk and a 4-to-1 payoff, where a long-stock or naked-
options version would cost five figures and offer no such asymmetry.

Spreads are also where a vol-aware trader starts paying attention:
debit spreads are short-vega (you bought volatility), credit spreads
are long-theta and short-vega (you sold volatility), butterflies are
short-vega *and* short-gamma. Picking the right structure is no
longer "bullish vs bearish" — it is "what do I think happens to
realised vs implied vol over the next thirty days, conditional on my
directional view." That is the language professional options desks
speak; this week is where you start speaking it too.

---

### 2. What You Need to Know

#### 2.1 The four vertical spreads — one slide, four trades

A vertical spread uses two options of the *same type* (both calls or
both puts), *same expiry*, and *different strikes*. Holding one and
selling the other gives four named structures:

- **Bull call spread** (debit). Buy lower-strike call, sell higher-
  strike call. Pay net premium. Max profit = width minus debit. Max
  loss = debit. Bullish, capped, theta-negative.
- **Bear put spread** (debit). Buy higher-strike put, sell lower-strike
  put. Pay net premium. Max profit = width minus debit. Max loss =
  debit. Bearish, capped, theta-negative.
- **Bull put spread** (credit). Sell higher-strike put, buy lower-
  strike put. Receive net premium. Max profit = credit. Max loss =
  width minus credit. Mildly bullish to neutral, theta-positive.
- **Bear call spread** (credit). Sell lower-strike call, buy higher-
  strike call. Receive net premium. Max profit = credit. Max loss =
  width minus credit. Mildly bearish to neutral, theta-positive.

The width is the strike distance — $5, $10, $25, whatever the chain
offers. Wider = more capital at risk, more dollars of max profit,
same shape. Two trades with the same delta but different widths
express the same view at different sizes.

The four payoff shapes — bull call, bear put, iron condor and butterfly
all in one frame — are drawn at expiry in
[course/image/week30_spread_payoffs.py](course/image/week30_spread_payoffs.py).
The maximum profit, maximum loss, and breakeven for each are marked on
the chart so you can verify the formulas on the diagram instead of
on the page.

![Four-panel payoff diagram at expiry for the canonical defined-risk option structures, all on a $100-area underlying. Top-left: bull call spread (buy $150 / sell $155 call) — the line slopes up between the strikes and caps at +$250 above $155, floor at -$250 below $150, breakeven $152.50. Top-right: bear put spread — mirror image. Bottom-left: iron condor with shorts at $470/$530 on SPY $500 — flat profit zone of +$180 between the two short strikes, sloping down to -$320 outside the wings at $465 and $535. Bottom-right: long butterfly centred at $150 — the classic tent shape, peaking at +$780 at the middle strike and decaying to a -$220 floor beyond either wing. Each panel labels max profit, max loss, and breakevens so the formulas can be read off the chart.](image/week30_spread_payoffs.png)

#### 2.2 Worked example — bull call spread on AAPL at $150

AAPL trades at $150. You expect a quiet drift higher over the next
30 days. The chain shows:

- $150 call: $5.00 mid (delta ~0.55).
- $155 call: $2.50 mid (delta ~0.35).

The bull call spread:

- **Buy** 1 AAPL $150 call: pay $5.00.
- **Sell** 1 AAPL $155 call: receive $2.50.
- **Net debit:** $2.50 per share = **$250** per spread.

Three numbers fall straight out of the structure:

- **Maximum profit:** width minus debit = ($155 - $150) - $2.50 =
  **$2.50 per share = $250 per spread**, achieved if AAPL closes at or
  above $155 at expiry.
- **Maximum loss:** the debit paid = **$250**, suffered if AAPL closes
  at or below $150.
- **Breakeven:** lower strike + debit = **$152.50**.

Risk/reward is **1-to-1**: $250 risked to make $250. The same view
expressed by buying the $150 call alone would cost $500 and need AAPL
above $155 to double — same target, twice the capital, and the long
call also bleeds twice the theta. The spread is the more capital-
efficient version of the same idea, with a precisely capped tail.

The cost of the spread version is the upside above $155: if AAPL rips
to $170, the long call version makes $1,500 and the spread makes only
$250. That is the trade — a ceiling in exchange for a floor.

#### 2.3 Iron condor — two credit spreads stitched into one trade

An iron condor is a bull put spread *and* a bear call spread on the
same underlying and the same expiry. Four legs, all out-of-the-money,
all collected for credit. The position profits if the underlying
closes between the two short strikes at expiry.

Worked example on SPY at $500, 30 days to expiry, IV 20%, r 4%.

The one-month one-standard-deviation move is
$500 \times 0.20 \times \sqrt{30/365} \approx \$28.65$. Round to $30.
Sell shorts at ±1σ, wings 5 points further out:

- **Sell** $470 put, **buy** $465 put: credit ~$0.95.
- **Sell** $530 call, **buy** $535 call: credit ~$0.85.
- **Total credit:** ~$1.80 per share = **$180 per condor**.
- **Width of each wing:** $5; **max loss** = $5 - $1.80 = **$3.20 per
  share = $320**. (Only one wing can lose at expiry.)
- **Capital required:** $500 minus credit, i.e. ~$320 (the broker
  collects the wing width as margin).
- **Breakevens:** $470 - $1.80 = $468.20 and $530 + $1.80 = $531.80.
- **Probability of profit (POP):** the lognormal probability that SPY
  closes inside [$470, $530] at expiry, ~**68%**.

Risk/reward 1.78-to-1 (lose 320 to make 180), POP 68% — this trade
has positive expectancy as long as realised volatility comes in at or
below the 20% the chain priced. That last clause is everything: the
iron condor is a *short-vol* trade in disguise. When realised vol
exceeds implied, the structure loses its edge no matter how the price
walk looks. Vol moves first.

The probability-of-profit curve for the SPY $500 iron condor across
three short-strike distances is drawn in
[course/image/week30_condor_pop.py](course/image/week30_condor_pop.py).
Tighter shorts give wider profit zones in *theta* terms but a far
lower POP; the chart shows the trade-off at 1σ, 0.75σ, and 0.5σ.

![Bar chart of the lognormal probability-of-profit (POP) for an iron condor on SPY at $500, 30 DTE, IV 20%, plotted against three short-strike distances: 1σ (~±$30 from spot), 0.75σ (~±$22), and 0.5σ (~±$15). The 1σ bar reads ~68% POP, 0.75σ reads ~55%, and 0.5σ reads ~38%. Each bar is annotated with the corresponding net credit and the loss/profit ratio so the trade-off — credit buys POP, POP buys credit — is visible at a glance. The 1σ shorts are the conventional retail default; tighter shorts pay more premium but the win-rate falls off sharply.](image/week30_condor_pop.png)

#### 2.4 Butterfly — pinning the level

A long butterfly centred at strike $K$ is three legs:

- **Buy** 1 call at $K - w$.
- **Sell** 2 calls at $K$.
- **Buy** 1 call at $K + w$.

The wings $w$ are equal, and the two short calls in the middle absorb
most of the cost. The position pays maximum if the underlying closes
exactly at $K$ at expiry and loses a small, fixed amount everywhere
else.

Worked example on AAPL at $150, 30 days, IV 25%:

- **Buy** $140 call: pay $11.00.
- **Sell 2** $150 calls: receive $5.00 x 2 = $10.00.
- **Buy** $160 call: pay $1.20.
- **Net debit:** $11.00 - $10.00 + $1.20 = **$2.20 per share = $220**.
- **Max profit:** width minus debit = $10 - $2.20 = **$7.80 per share
  = $780**, only at $150 exactly at expiry.
- **Max loss:** the debit = **$220**, beyond $140 below or $160 above.
- **Breakevens:** $142.20 and $157.80.

Risk/reward **3.5-to-1** but with a much narrower profit zone than a
condor. POP at expiry is low (the *peak* is a single point), but the
position has positive vega-to-vol-rank carry: as expiry approaches, if
the stock stays near the middle strike, the butterfly's mark-to-market
P&L grows non-linearly because the short middle strikes lose value
faster than the long wings. The professional name for this is
"gamma-scalping a butterfly" — it is a directional bet on *time
passing while the stock pins*.

Butterflies are the natural structure for: pinning at a round-number
strike near max-pain on options-expiry Friday; expressing a "drift to
fair value" view on a stretched name; betting on a quiet earnings
reaction *after* IV has been crushed; or sitting in front of a
known catalyst with capped tail risk.

#### 2.5 Picking width, distance, and DTE — the three knobs

Every defined-risk structure has the same three knobs and they are
the only knobs that matter:

- **Width** (strike-to-strike distance of the wings or legs): doubles
  the dollars at risk and the dollars of credit, leaves the *shape*
  alone. Width is the *size* knob.
- **Distance from spot** (how far OTM the short strikes sit): the
  POP knob. Closer to spot = more credit, lower POP, higher delta.
  Further from spot = less credit, higher POP, lower delta. The
  delta-on-the-short is a clean proxy: a 30-delta short ≈ 30%
  probability ITM ≈ 70% POP per leg.
- **Days to expiry (DTE)**: 30-45 DTE is the sweet spot for credit
  spreads (covered in Week 27). Theta accelerates inside 21 DTE; vega
  shrinks. Short DTE = faster decay, more gamma risk; long DTE =
  cleaner carry, more capital tied up.

A retail trader running a steady book usually fixes two of these
three (e.g. 30-delta shorts, 30 DTE) and varies width to size the
position. A professional varies all three with the vol surface.

The interactive [course/interactive/week30_spread_builder.html](course/interactive/week30_spread_builder.html)
lets you toggle structure (vertical / iron condor / butterfly) and
move all three knobs in real time, watching net premium, max
profit, max loss, breakevens, POP, and the payoff diagram update
together.

#### 2.6 Capital efficiency — the side-by-side that justifies the chapter

Same SPY thesis ("market closes between $470 and $530 in 30 days"),
five ways to express it:

| Structure | Capital | Max profit | Max loss | POP | Yield on cap |
|---|---|---|---|---|---|
| Long stock (held flat) | $50,000 | ~$1,000 carry | ~$50,000 | ~50% | ~2% / 30d |
| Short straddle, 1σ | ~$15,000 | ~$3,200 | unlimited | ~68% | ~21% / 30d |
| Iron condor, 1σ short, 5-wide | ~$320 | $180 | $320 | ~68% | ~56% / 30d |
| Iron condor, 0.75σ short, 5-wide | ~$280 | $220 | $280 | ~55% | ~78% / 30d |
| Long butterfly at $500 | ~$220 | $780 | $220 | ~25% | ~355% / 30d at peak |

The yield-on-capital column is the punchline. The defined-risk
structures are *one to two orders of magnitude* more efficient on
capital than the underlying-stock or short-straddle versions of the
same view. The iron condor and butterfly are not exotic — they are
the *correct* way to size a non-directional view inside a barbell.

The price you pay is precision. Every defined-risk trade has a
specific window where it works; outside that window it pays the max
loss. That is the discipline the structure forces on the trader, and
why this chapter is the gateway to L3.

#### 2.7 Tax, assignment, and the practical wrinkles

Vertical spreads almost never get assigned early *as a unit* — the
long leg always covers the short leg if the short is exercised. The
real risk is *single-leg* early assignment near ex-dividend dates on
the short call of a credit call spread; if it happens, you wake up
short stock with the long call still alive, which is fine but
requires same-day action. Iron condors and butterflies share the
same property at the wing level.

For tax purposes: defined-risk option spreads on broad-based
indices (SPX, NDX, RUT, *not* SPY/QQQ/IWM ETFs) are 1256-contracted
and taxed 60% long-term / 40% short-term regardless of holding
period. That is a structural advantage worth ~10 percentage points
of after-tax return for a high-bracket US trader running monthly
condors. The price is wider bid/ask spreads on the index options
versus their ETF cousins. For most retail accounts, SPY/QQQ/IWM
condors are the right starting point and the tax difference becomes
worth the slippage at six-figure annual options income, not before.

In an IRA, defined-risk spreads are usually permitted at level 3
options approval; naked short options are not. This is one of the
underrated reasons a retail trader graduates to spreads — it unlocks
the only legal way to run an income-options book inside the tax-
sheltered account. Week 31 covers IV rank, vol regimes, and how to
size all of this against the realised-vol environment.

---

### 3. Common Misconceptions

**1. "Credit spreads are 'safer' than debit spreads."** They have
higher POP but worse risk/reward. A 5-wide credit spread sold for
$1.80 has POP ~70% and loses 1.78x what it can make. Over many trades
the expected value depends on whether IV was rich versus realised vol;
*neither* structure is automatically safer.

**2. "An iron condor with shorts at 1σ is a free 68% win-rate trade."**
The 68% is conditional on lognormal returns at the priced IV. When
IV under-prices realised (vol expansions, gap days, earnings), the
true POP collapses. The 1σ condor is a short-vol trade with 1.78-to-1
risk, not a coin flip with extra rake.

**3. "Butterflies are too narrow to be useful."** They are narrow on
*price* but wide on *time*. A butterfly placed 21 DTE inside a known
pinning name regularly mark-to-markets at 100-200% by 7 DTE without
the underlying having to print exactly at the middle strike. The
"max profit only at $K" rule applies *at expiry*; the path matters.

**4. "Defined-risk spreads have no margin call risk."** They have no
*assignment* margin call (the long leg covers the short leg). They
*do* have variation margin haircuts intra-trade if the broker
re-prices the spread mid-life; on a fast move the margin requirement
can briefly exceed the maximum loss until the broker remarks.

**5. "Wider wings are always safer."** Wider wings raise both the
dollars of credit *and* the dollars at risk by the same width factor.
The probability profile is unchanged; only the position size
changes. Wing width is the size knob, not the safety knob.

**6. "I should sell the highest-credit spread on the chain."** The
highest-credit spread is the one with shorts closest to the money,
i.e. the lowest POP. Maximising credit minimises win-rate. Pick a
target POP first and let the credit fall out of it.

**7. "An iron condor on a meme stock with 90% IV is a great
opportunity."** That 90% IV is the market telling you the realised
move is about to be huge. Selling premium *into* a vol expansion is
the textbook way to lose money on a short-vol structure. Sell when
IV rank is high *and* the catalyst is past.

**8. "A bull call spread is a bullish trade." Mostly. It is a
bullish trade *with a vega haircut*. If the underlying rises but
implied vol crashes (post-earnings, post-Fed), the spread can make
less than expected because both legs are short-vega'd in opposite
directions and the long leg dominates while still OTM. Direction is
necessary; vol is the wrinkle.

**9. "I should always close at 50% profit."** The 50%-of-max rule is
a heuristic from credit-spread sellers that captures the early-decay
sweet spot. For *debit* spreads it makes much less sense; the right
exit is when delta hits 0.85+ on the long leg or 7 DTE, whichever
comes first.

**10. "Defined-risk means risk-free."** Defined-risk means the loss
is *capped at trade entry*. It does not mean small. A 10-wide bear
call spread on a stock that gaps 30% overnight loses every dollar of
its $1,000 max in a single morning. Capped is not a substitute for
sized.

---

### 4. Q&A Section

**Q1. What's the cleanest way to pick the structure for a given view?**
Start with two questions: am I directional, and am I long or short
vol? Long-direction + long-vol = debit call/put spread. Direction
agnostic + short-vol = iron condor. Strong level + short-vol = long
butterfly. Direction + short-vol = credit put/call spread. The four
boxes cover ~80% of practical setups.

**Q2. Is there an optimal width?** No. Width controls position size,
not edge. Pick the width that puts the dollar max-loss at 1-2% of
account equity per trade; that becomes your default. Vary it only
when the broker's commissions become material (tight wings on cheap
underlyings).

**Q3. How is POP actually computed?** Lognormal closed form:
POP for an iron condor =
$\Phi(d^{\text{up}}_2) - \Phi(d^{\text{down}}_2)$ where the d's are the
standard BSM term, with the same $r$, $\sigma$, $T$ used for the
chain. The interactive does this in JS for you.

**Q4. What about buying-power reduction in a margin account?** For a
credit spread, BPR = wing width − credit, applied to the wider of the
call or put side for an iron condor (you can only lose on one side at
expiry, so brokers don't double-count). For a debit spread, BPR =
debit. For a butterfly, BPR = debit.

**Q5. When does a debit spread beat a long call?** When you don't
need the upside above the short strike. If your target is "AAPL to
$155 in 30 days" and you don't think it goes to $170, the debit
spread costs half and bleeds half the theta. If you think it goes to
$200, buy the call.

**Q6. How do I roll a tested credit spread?** Standard rule: roll
*out* (later expiry) and *down/up* (further from current spot) for a
small additional credit. Never pay debit to roll a losing spread out
in time without moving the strikes; that compounds the loss into the
new month. If the only roll on offer is a debit, take the loss and
re-enter fresh.

**Q7. Are iron condors the same as iron butterflies?** No. An iron
condor has two *different* short strikes (call and put). An iron
butterfly has the *same* short strike for both, sold at the money.
The iron fly is closer to a short straddle with wings — larger
credit, narrower profit zone, lower POP, higher max profit. Most
retail desks treat the iron fly as a separate structure.

**Q8. What does "broken-wing" mean?** A butterfly with unequal wing
widths. Buy 1 $140C, sell 2 $150C, buy 1 $165C is a broken-wing
butterfly with a wider upper wing. The asymmetry skews the payoff:
maximum profit shifts, max loss shrinks on one side and grows on the
other. Used to express a "level + a directional bias" view in one
ticket.

**Q9. Why do I need to know all this if I'm just an L1 indexer?** You
don't, today. You will the moment you have idle cash on a quiet week
and a directional thesis, or the moment a high-IV-rank earnings event
tempts you into a too-large naked short put. A 5-line bull put spread
turns that temptation into a sized, capped, professional trade. The
structures are the discipline.

**Q10. What's the tax difference between a SPY condor and an SPX
condor for a US filer?** SPY (and QQQ, IWM) condors are taxed as
ordinary short-term capital gains (held <1 year). SPX (and NDX, RUT)
condors are 1256 contracts: 60% long-term / 40% short-term blended
rate regardless of holding period. For a 35%-bracket trader running
$50k of annual condor income, SPX saves roughly $5,000-7,000 of
federal tax per year — a meaningful chunk of L2 alpha that exists
purely because of the tax code.

**Q11. Should I trade weeklies or monthlies?** Monthlies (30-45 DTE).
Weeklies have steeper theta but much higher gamma and bid/ask noise.
For learning and for steady-state retail income the monthly cycle is
the right rhythm. Weeklies are an advanced extension once the book
runs cleanly.

**Q12. How do I know if my POP estimate is realistic?** Compare the
chain's IV against the 20- and 60-day realised vol of the underlying.
If implied is at or below realised, your POP is overstated; the
market is telling you it expects a bigger move than the lognormal
model. If implied is well above realised (high IV rank), the POP is
honest and the trade has positive structural carry. Week 31 makes
this routine.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Spreads, Condors and Butterflies — How Pros Actually Sell Premium

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Stella:** Last week we drew the four Greeks. The week before, you
walked us through covered calls and cash-secured puts. They both
sounded great in the lesson — and then I tried to actually price one
on SPY at five hundred bucks. The cash-secured put wanted *fifty
thousand dollars* of collateral.

**Horace:** Yep. That is the moment every retail trader has, and it
is the moment that splits the people who use options once from the
people who use options for a living.

**Stella:** Because you can't run an income book where every trade is
your entire account.

**Horace:** Right. So today we fix it. We take the same theses — the
same "I'd buy SPY lower" or "I'd sell AAPL higher" or "this thing's
going nowhere for thirty days" — and we express each one with two or
four legs instead of one. Maximum loss printed on the ticket. Capital
requirement under five hundred bucks. Same edge.

**Stella:** And these are the structures the pros actually run.

**Horace:** Spreads. Condors. Butterflies. By the end of this you
should be able to look at any options chain and pick the right
structure for what you actually believe.

---

**[BLOCK 1 — Vertical spreads, 1:10]**

**Stella:** Walk me through "vertical spread" in one sentence.

**Horace:** Two options, same type, same expiry, different strikes.
You buy one and you sell the other. The one you sold caps your
profit; the one you bought caps your loss. That's it.

**Stella:** Four flavours, right?

**Horace:** Four flavours. Bull call spread is two calls — buy the
lower, sell the higher, you pay net. Bear put spread is two puts —
buy the higher, sell the lower, you pay net. Those are the *debit*
spreads. Then bull put — sell the higher put, buy the lower put,
collect cash. And bear call — sell the lower call, buy the higher
call, collect cash. Those are the *credit* spreads.

**Stella:** And the point is the long leg covers the short leg.

**Horace:** Exactly. Worst case for a 5-wide spread is five hundred
bucks, minus whatever credit you took in. Not the five thousand the
short option alone would cost you.

**[VISUAL: image/week30_spread_payoffs.png — 2x2 panel]**

**Stella:** This is the chart that makes it click for me. Top-left,
bull call spread on AAPL at one-fifty. Buy the $150 call for five
bucks, sell the $155 call for two-fifty, net debit two-fifty per
share, two hundred and fifty dollars per spread. The line goes flat
above $155 — that's the cap. It goes flat at minus two-fifty below
$150 — that's the floor.

**Horace:** And the breakeven is one-fifty-two-fifty. Lower strike
plus the debit. Risk-reward is exactly one-to-one — risk two-fifty
to make two-fifty.

**Stella:** Top-right, bear put spread.

**Horace:** Mirror image. Buy the higher put, sell the lower put. You
pay a debit, you make money on the way down. Same one-to-one shape.

---

**[BLOCK 2 — Iron condor, 4:00]**

**Stella:** Bottom-left of that chart — iron condor.

**Horace:** Bottom-left is the one I want most retail traders to fall
in love with. It is two credit spreads stitched together. A bull put
spread below the market and a bear call spread above the market, same
ticker, same expiry. Both shorts are out of the money. You collect
both credits. You profit if the stock closes anywhere between the two
short strikes at expiry.

**Stella:** Walk me through the SPY example.

**Horace:** SPY at five hundred. Thirty days out. Twenty percent
implied vol. The one-month one-sigma move is about twenty-eight bucks
— call it thirty. Sell the $470 put, buy the $465 put for protection.
That's the put side. Sell the $530 call, buy the $535 call for
protection. That's the call side.

**Stella:** Total credit?

**Horace:** Roughly a buck eighty per share. Hundred and eighty
dollars per condor. Max loss is the wing width minus the credit, so
five minus one-eighty equals three-twenty. Capital requirement,
roughly three-twenty. You make a hundred and eighty if SPY stays
between $470 and $530. You lose three-twenty if it closes outside one
of the wings.

**Stella:** And the probability of profit is —

**Horace:** Roughly sixty-eight percent at the one-sigma shorts.
That's just the lognormal probability that SPY closes inside one
standard deviation, with a tiny drift adjustment.

**[VISUAL: image/week30_condor_pop.png — POP bar chart]**

**Stella:** This second chart is the trade-off in one picture. Three
bars. Shorts at one-sigma — sixty-eight percent. Shorts at three-
quarter-sigma — fifty-five. Shorts at half-sigma — thirty-eight.

**Horace:** Tighter shorts pay more credit but the win-rate falls
off a cliff. That fifty-five percent looks tempting because the
credit nearly doubles, but the trade is now a coin flip with a 1.3-
to-1 loss ratio. The half-sigma version is essentially a short
straddle with wings — high payout, terrible win-rate.

**Stella:** And the 1σ version is the one most retail desks default
to.

**Horace:** Sixty-eight percent POP, 1.78-to-1 risk, three hundred
and twenty bucks of capital. Run ten of those across SPY, QQQ, IWM,
and a handful of large-cap names every month and you have a real
income book on a real account.

---

**[BLOCK 3 — Butterflies, 8:30]**

**Stella:** Bottom-right of the payoff chart. The pointy one.

**Horace:** Long butterfly. Three legs. Buy one $140 call, sell two
$150 calls — that's the body — and buy one $160 call. The two short
calls in the middle pay for most of the trade.

**Stella:** And it pays maximum if the stock closes exactly at $150.

**Horace:** Exactly. Net debit is two-twenty per spread. Max profit
is seven-eighty if AAPL pins at $150 at expiry. Max loss is the
debit, two-twenty, beyond either wing. Risk-reward is three-and-a-
half to one.

**Stella:** That sounds insane. Why doesn't everyone do it?

**Horace:** Because the probability of profit *at expiry* is low. The
peak is a single point. You only get the seven-eighty if AAPL closes
within a couple of bucks of $150 on Friday afternoon. But — and this
is the part nobody tells you — the trade rarely *needs* to ride to
expiry. If AAPL drifts toward $150 with a week to go, the butterfly
is already up two or three hundred dollars on the mark, because the
two short calls have decayed faster than the long wings.

**Stella:** So you can take it off early.

**Horace:** Almost always. Butterflies are usually closed at 50-100%
of debit, sometimes a couple of weeks before expiry, and never held
through the last 24 hours unless the stock is *already* pinned. They
are a directional-on-level, time-decay-accelerating, capped-risk
trade. Best fit: post-earnings drift, options-expiry pinning,
mean-reversion to a round-number magnet.

---

**[BLOCK 4 — The spread builder, 11:30]**

**Stella:** Let's open the lab.

**[VISUAL: course/interactive/week30_spread_builder.html]**

**Horace:** Pill bar across the top — vertical, iron condor,
butterfly. Pick the structure first. Then the four sliders — strike
width, distance from spot, days to expiry, implied volatility.

**Stella:** I'll start on iron condor at the defaults. SPY at $500,
shorts at one sigma, five-wide wings, 30 DTE, 20 vol. The four big
numbers — net premium one-eighty-ish, max profit one-eighty-ish, max
loss three-twenty, POP sixty-eight percent. That matches what you
worked through.

**Horace:** Now drag distance-from-spot in. Watch what happens.

**Stella:** Net credit goes up — three bucks, five, seven. POP
collapses — sixty-eight, fifty-five, forty.

**Horace:** That's the only trade-off in this entire lesson. Credit
buys you POP and POP buys you credit. The lab makes it visceral.

**Stella:** Drag width up. Wing 5 becomes wing 10.

**Horace:** Max profit and max loss both double. POP unchanged.
Capital required doubles. Same shape, twice the size.

**Stella:** And switching to vertical?

**Horace:** Single-sided. One short, one long. Only one breakeven.
The payoff diagram below redraws live. Switch to butterfly and the
diagram becomes the tent.

---

**[BLOCK 5 — When to use which, 14:00]**

**Stella:** Quick decision tree.

**Horace:** Two questions. One: am I directional or non-directional?
Two: am I long-vol or short-vol?

**Stella:** Directional + long-vol?

**Horace:** Debit call or put spread. You're paying for the move and
betting the move is bigger than the chain expects.

**Stella:** Directional + short-vol?

**Horace:** Credit put spread for bullish, credit call spread for
bearish. You're betting the move you want happens *and* the chain is
overpaying for the chance it doesn't.

**Stella:** Non-directional + short-vol?

**Horace:** Iron condor. The bread-and-butter monthly income trade.

**Stella:** Pinning + short-vol?

**Horace:** Long butterfly at the magnet strike.

**Stella:** That's the whole grid.

**Horace:** That's most of what an options income book actually does.
Earnings strategies, calendar spreads, ratio diagonals — those are
overlays on top of these four. Get these four right and you can
sleep at night.

---

**[BLOCK 6 — Tax and account-type, 15:30]**

**Stella:** Options are a tax tool first. Where does
that show up here?

**Horace:** Two places. One — an iron condor on SPX, NDX, or RUT is
a 1256 contract: 60% long-term, 40% short-term tax treatment, no
matter how long you held it. SPY, QQQ, IWM condors are ordinary
short-term. For a high-bracket US trader running steady monthly
condors, SPX saves roughly ten percentage points of after-tax return.

**Stella:** And the IRA angle?

**Horace:** Naked short options aren't allowed in most IRAs. Defined-
risk spreads are. So the *only* legal way to run a credit-premium
income book inside the tax-sheltered account is through these
structures. That alone is worth learning them for.

---

**[OUTRO — 17:00]**

**Stella:** Recap.

**Horace:** Spreads turn a single-leg option into a printed maximum
loss for fifty to a hundred bucks of capital. Iron condors monetise
mean-reversion at sixty-plus percent win rates. Butterflies pin
levels for three-and-a-half-to-one payoff. They are the L3 sleeve of
the barbell — capped, asymmetric, professional.

**Stella:** Next week — implied volatility rank, vol regimes, and
how to size all of this against realised vol so the structures
actually work.

**Horace:** See you in week thirty-one.

**[END]**
