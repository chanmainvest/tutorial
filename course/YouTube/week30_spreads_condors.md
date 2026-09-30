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
