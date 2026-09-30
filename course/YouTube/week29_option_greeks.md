## Part 2: YouTube Script

---

**VIDEO TITLE:** The Greeks - Delta, Gamma, Theta, Vega, Rho
Without the Calculus
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00-1:30]**

**Stella:** Welcome back to the chanmainvest tutorial. I'm Stella.

**Horace:** I'm Horace. Today is Week 29, and we are doing the
Greeks.

**Stella:** Four weeks of options behind us. We can buy a call,
buy a put, sell a covered call, sell a cash-secured put. What
we cannot yet do is *explain* what the position is doing on any
given Tuesday. The Greeks are the explanation.

**Horace:** Five letters. Delta, gamma, theta, vega, rho. Each
one is a partial derivative of the option price with respect to
one input. If "partial derivative" is intimidating, here is the
non-calculus version: *one input changes, everything else stays
fixed, how much did the option price change?* That is a Greek.

**Stella:** Five inputs in Black-Scholes - spot, time, vol, rate,
strike. Strike does not move. So there are five sensitivities,
five Greeks. We will walk through each one with the same option
as our reference.

**Horace:** $100 stock, $100 strike, 30 days to expiration, 20%
implied volatility, 4% risk-free rate. We will compute all five
Greeks for that single contract and then look at how they change
across spot and time.

**[VISUAL: image/week29_greeks_vs_spot.png]**

**Stella:** This is our anchor chart. Four panels - delta, gamma,
theta, vega - all for the same 30-day at-the-money call, all
plotted versus spot from $60 to $140. Hold this image in your
head; we are going to walk through each panel.

---

**[PART 1: DELTA — 1:30-4:30]**

**Horace:** Top-left panel. Delta. The S-curve from 0 at the
left edge to 1 at the right edge, crossing 0.5 right at the
strike. Three ways to read that number.

**Stella:** First, as a hedge ratio. A call with delta 0.5 moves
like half a share of stock. Buy ten such calls, you are
synthetically long 500 shares.

**Horace:** Second, as directional exposure. Net delta on a
portfolio tells you the dollar P&L per dollar of underlying
move. Plus 200 deltas? You make $200 if the index moves up $1.

**Stella:** Third - and this is the one beginners get
half-right - delta is *approximately* the probability the option
finishes in the money. Approximately. The true risk-neutral
probability is $N(d_2)$, not $N(d_1)$. They are close enough
that "30-delta put" and "30% chance of expiring ITM" are used
interchangeably on trading desks.

**Horace:** And different enough that you should not put it on
your tax return. For our worked example, delta is +0.534. The
true ITM probability is +0.511. Close, not equal.

**Stella:** Practical takeaway: delta is the *direction*
dimension of the position. Everything that follows is
about second-order effects - what happens to delta itself when
something moves.

---

**[PART 2: GAMMA — 4:30-7:30]**

**Horace:** Top-right panel. Gamma. The bell curve centred on
the strike. Two facts to memorise.

**Stella:** One: gamma peaks at-the-money. Far ITM and far OTM
options have stable deltas. ATM options have delta that
ricochets with every dollar of underlying.

**Horace:** Two: gamma explodes near expiry. Our 30-day option
has gamma 0.07. A one-day version of the same option would have
gamma north of one. That divergence is the entire reason last-
week-before-expiration is qualitatively different from any
other week.

**Stella:** And gamma has a sign that flips depending on whether
you are buyer or seller. *Long* gamma - you bought the option -
is friendly. Stock rallies, your delta climbs from 0.5 toward
0.7, you participate more in further upside. Stock drops,
delta falls toward 0.3, you bleed less on further downside.
Long gamma decelerates losses, accelerates gains.

**Horace:** Short gamma is the opposite. Stock rallies against
your short call, your delta gets *more* short, each additional
dollar hurts more. Vol-tail-wags-dog is fundamentally a
statement about short gamma. The position
prints steady income at low realised vol and bleeds at
compounding speed when vol arrives.

**Stella:** Long gamma is good news on a move. You pay for it
in theta. Which is exactly the next panel.

---

**[PART 3: THETA — 7:30-11:00]**

**Horace:** Bottom-left panel. Theta - the daily time-decay.
Negative for long options, positive for short options. Read
the panel: theta is most negative at-the-money, just like
gamma peaks ATM. ITM and OTM options have less extrinsic to
melt, so their theta is smaller in absolute terms.

**Stella:** And theta accelerates as expiration approaches.

**[VISUAL: image/week29_theta_decay.png]**

**Horace:** Left side of this chart - absolute theta per day,
plotted against days-to-expiry. At 90 DTE, theta is about a
penny per day. At 30 DTE, four cents. At 7 DTE, ten cents. At
1 DTE, twenty cents. The same option's theta moves by 20x in
the last 90 days.

**Stella:** Right side: the premium itself. The option starts
at $4.05 with 90 days, drops to $2.45 by 30 DTE, and lands
near zero in the final week. The orange band is the last 30
days, where roughly 63% of the original premium is gone.

**Horace:** That curve is the *entire* income-strategy thesis
from Weeks 27 and 28. The 30 to 45 DTE window is where theta
collection compensates the seller for accepting short gamma.
Earlier than that, daily theta is too small relative to the
premium received. Later than that, gamma starts to bite hard
enough to swamp theta on any meaningful move.

**Stella:** Theta and gamma are joined at the hip. You cannot
be long gamma without paying theta. You cannot collect theta
without being short gamma. The arbitrage-free price of carrying
one is the other. That trade-off *is* what option-selling
income strategies are.

---

**[PART 4: VEGA — 11:00-13:30]**

**Horace:** Bottom-right panel. Vega - sensitivity to a one-
percentage-point change in implied volatility. Three things
to know.

**Stella:** One: vega peaks at-the-money. Same shape as gamma.

**Horace:** Two: vega is *largest for long-dated options* -
this is the cleanest counter-example to "all the Greeks behave
like gamma." Gamma rises into expiry. Vega falls into expiry.
A one-year ATM option has vega around forty cents per vol-
point. Our 30-day option has eleven cents. A one-day option
has two cents. Long-duration options are vol instruments
almost more than direction instruments.

**Stella:** Three: vol crush is a vega event. Buy a call ahead
of earnings when implied vol is at the 90th percentile - you
own thirty or forty vega-points of "earnings premium" that
the market evaporates the moment the print drops. The stock
can move exactly the way you predicted and you can still
*lose* money on the option. Beginners learn this once.

**Horace:** Vega is what separates *income strategies* from
*vol strategies*. A covered call sold at 15% IV in a calm
market has small vega exposure. Sold at 40% IV during a
panic, the same covered call is short a lot of vega and can
print you a fast profit on vol mean-reversion alone, with the
stock unchanged.

---

**[PART 5: RHO — 13:30-14:30]**

**Stella:** Rho gets one minute and that is generous. For a
30-day ATM call, rho is about $0.04 per 1% rate change per
share. A 25 bp Fed move is a penny. On short-dated retail
options, rho is rounding error.

**Horace:** Two situations where rho actually matters. LEAPS
- two-year options have rho near $1.40 per 1% per share, big
enough to register. And regime transitions - when the Fed is
moving 75 bp at a meeting, accumulated rho across a book
matters. Outside those, you can ignore it.

---

**[PART 6: THE INTERACTIVE — 14:30-16:30]**

**[VISUAL: interactive/week29_greeks_lab.html]**

**Stella:** Pull up the Greeks Lab. Five sliders - spot, strike,
DTE, vol, rate. A toggle for call versus put. Six pills that
let you choose which Greek to plot.

**Horace:** Three things to do with this. First: slide DTE
down toward zero with spot at the strike, watch the chart with
gamma selected. Watch the bell collapse and spike. That is
the gamma-explosion that makes weekly options a different
risk regime.

**Stella:** Second: select theta, then slide DTE down. Watch
the theta well at the strike deepen non-linearly. You can
*see* the theta acceleration that the static chart shows - now
under your fingers.

**Horace:** Third: select vega, slide DTE up to 365. The vega
bell gets bigger. Long-dated options *are* vol instruments.
Compare to gamma, which goes the other way. That contrast is
the cleanest mental model you can have for "what kind of
option am I holding."

**Stella:** And the live numbers in the strip across the top
update with every slider. Premium, all five Greeks, color-
coded by which one each one is. That is your dashboard.

---

**[OUTRO — 16:30-18:00]**

**Horace:** Five Greeks. One for each input that moves.

**Stella:** Delta is direction. Gamma is acceleration. Theta is
the rent on time. Vega is the thermostat for fear. Rho is the
back-of-the-dashboard slow-moving rate sensitivity.

**Horace:** Two sentences to take with you. *Long gamma is
profitable only when realised vol exceeds implied vol over the
holding period - every long-gamma trade is implicitly a long-
vol trade.* And: *theta and gamma are joined at the hip, you
cannot collect one without being short the other.*

**Stella:** Next week we layer multiple options into spreads
and condors - and a spread is exactly a *combination of Greek
exposures* designed to isolate one risk and neutralise the
others. None of it makes sense without this week's foundation.

**Horace:** Side25 takes the second-order Greeks - vanna,
vomma, charm - much further. We will get there. For now, get
comfortable with these five.

**Stella:** Read the misconceptions list. Run the interactive.
We will see you in Week 30.

**[END]**
