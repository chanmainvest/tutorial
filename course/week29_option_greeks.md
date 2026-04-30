# Week 29: The Greeks - Delta, Gamma, Theta, Vega, Rho

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Weeks 25-28 taught you the *mechanics* of options: what a call is, what a
put is, how to sell a covered call against stock you own, how to sell a
cash-secured put against cash you would deploy anyway. You can already
open positions and you understand the payoff diagrams at expiration.
What you cannot yet do is answer the questions a position asks of you
*before* expiration: the underlying moved $2 today, why did my call only
go up $0.40? I sold a put two weeks ago, the stock has not moved, why
am I up half my premium already? The S&P is flat and the VIX collapsed
five points, why did my long call get crushed? Each of these is a Greek
question, and the Greeks have closed-form answers.

The Greeks are the partial derivatives of the Black-Scholes premium
with respect to each of its inputs. That is a sentence calculus
students recognise; for everyone else the practical translation is:
*how much does the option's price change when one input moves and
everything else stays put?* Five inputs matter (spot, time, vol, rate,
and the strike, which does not move), so there are five Greeks. They
are not optional reading - by Week 30 we layer multiple options into
spreads and condors, and a spread is exactly a *combination of Greek
exposures* designed to isolate one risk while neutralising another.
You cannot think about a vertical or an iron condor coherently without
delta, gamma, theta, and vega in your head.

Four reasons to put the work in:

1. **Greeks turn confusion into accounting.** When a position behaves
   in a way you did not expect, the Greeks decompose the surprise into
   line items: *delta P&L plus gamma P&L plus theta P&L plus vega P&L
   plus rho P&L equals what your account did today.* That decomposition
   is the difference between "options are weird" and "options are
   measured."
2. **Greeks let you size by risk, not by ticket count.** "I sold three
   calls" is not a position description. "I am short 150 deltas, long
   $9 of theta per day, short $40 of vega per vol-point" is. The first
   tells you nothing about how the position breathes; the second lets
   you compare the trade to every other trade in your book on the
   same dimensions.
3. **Greeks expose the second-order risk that kills option sellers.**
   Theta-collectors (covered calls, cash-secured puts, condors)
   sound like an income strategy and feel like an income strategy
   right up until volatility expands. The position is short vega and
   short gamma; both work against you when realised volatility ticks
   higher. SOUL #6 - vol-tail-wags-dog - is fundamentally a statement
   about gamma and vega risk that the Greek decomposition makes
   literal.
4. **Greeks are the language of every advanced lesson that follows.**
   Spreads (Week 30), LEAPS (Week 38), the VIX (Week 40), volatility
   surfaces, and the entire side25 lesson on second-order Greeks all
   assume you can think *natively* in Δ, Γ, Θ, ν. This week is the
   foundation those lessons build on.

We will derive each Greek from Black-Scholes, work a single example
end-to-end on a $100 stock with a 30-day at-the-money call, look at
how each Greek moves with spot and with time, and then translate the
Greek profiles into how the four conservative strategies from Weeks
25-28 actually breathe in your account.

---

### 2. What You Need to Know

#### 2.1 The Five Greeks at a Glance

There are five primary Greeks. Each is a partial derivative of the
option premium $P$ with respect to one input, holding the other four
fixed. The standard symbols and what they measure:

$$
\Delta = \frac{\partial P}{\partial S} \qquad
\Gamma = \frac{\partial^2 P}{\partial S^2} \qquad
\Theta = \frac{\partial P}{\partial t} \qquad
\nu = \frac{\partial P}{\partial \sigma} \qquad
\rho = \frac{\partial P}{\partial r}
$$

Plain English, in order: delta is the option's *speedometer* (how
much premium changes per $1 of spot), gamma is its *acceleration*
(how much delta itself changes per $1 of spot), theta is its
*time-decay clock* (how much premium melts per calendar day), vega
is its *vol-sensitivity* (how much premium changes per one
percentage-point move in implied volatility), and rho is its
*rate-sensitivity* (how much premium changes per one percentage-
point move in the risk-free rate).

There is a caution about units before we go further. Brokerage
platforms quote theta as *per calendar day* (annual theta divided by
365), vega as *per one volatility point* (vega divided by 100), and
rho as *per one percentage-point of rate* (also divided by 100).
Black-Scholes-the-formula gives them in continuous-time, per-unit
form; everything in this lesson is in the *broker-quoted, practical*
form because that is what your trading screen will show you.

#### 2.2 The Black-Scholes Engine, in One Box

For a non-dividend-paying European call with spot $S$, strike $K$,
time-to-expiry $T$ (in years), implied vol $\sigma$, and risk-free
rate $r$:

$$
d_1 = \frac{\ln(S/K) + (r + \tfrac{1}{2}\sigma^2)T}{\sigma \sqrt{T}}, \qquad
d_2 = d_1 - \sigma \sqrt{T}
$$

$$
C = S \, N(d_1) - K e^{-rT} N(d_2)
$$

where $N(\cdot)$ is the standard-normal CDF. Each Greek then has a
closed form:

$$
\Delta_{\text{call}} = N(d_1), \qquad
\Gamma = \frac{\varphi(d_1)}{S \sigma \sqrt{T}}
$$

$$
\Theta_{\text{call}} = -\frac{S \varphi(d_1) \sigma}{2\sqrt{T}}
                       - r K e^{-rT} N(d_2)
$$

$$
\nu = S \varphi(d_1) \sqrt{T}, \qquad
\rho_{\text{call}} = K T e^{-rT} N(d_2)
$$

Here $\varphi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ is the standard-
normal density. For puts, delta becomes $N(d_1) - 1$, the rho term
flips sign and uses $-N(-d_2)$, and the second term in theta flips
sign; gamma and vega are *identical* for calls and puts at the same
strike (this is one of the cleanest facts in option pricing - any
asymmetry between calls and puts at the same strike has to live in
delta, theta-via-rate, or rho).

You do not need to memorise these. You need to recognise that every
Greek is just one input changing and the rest held fixed - and that
the closed forms make every panel of every chart in this lesson a
two-line Python function.

#### 2.3 The Worked Example - $100 Stock, 30-Day ATM Call

Spot $S = \$100$, strike $K = \$100$, expiry in 30 calendar days
($T = 30/365 \approx 0.0822$ years), implied vol $\sigma = 20\%$,
risk-free rate $r = 4\%$. Plugging into the formulas:

| Quantity | Value |
| --- | --- |
| $d_1$ | $0.086$ |
| $d_2$ | $0.029$ |
| $N(d_1)$ | $0.534$ |
| $N(d_2)$ | $0.511$ |
| Call premium $C$ | $\$2.45$ |
| **Delta** | **+0.534** |
| **Gamma** | **+0.069** |
| **Theta / day** | **-$0.044** |
| **Vega / 1 vol-pt** | **+0.114** |
| **Rho / 1% rate** | **+0.042** |

Read those rows like a position briefing. The call costs $2.45.
For every $1 the stock moves up, the call gains roughly $0.53
(delta). For every additional $1 of upside *after* that first dollar,
the option gains another ~$0.07 *more* than the previous dollar
(gamma). One day passing costs you 4.4 cents per share even if
nothing else changes (theta). If implied vol ticks up from 20% to
21%, you make 11 cents (vega). If the Fed surprised the market by
hiking rates 100 basis points overnight (it does not), you would
make about 4 cents (rho). Multiply every dollar by 100 because one
contract controls 100 shares: this $2.45 option is a $245 ticket
with a $53 / $1-stock-move directional exposure.

[image: image/week29_greeks_vs_spot.png — The four primary Greeks
plotted across spot for this same option.]

#### 2.4 Delta - Direction and "Probability ITM"

Delta is the most-used Greek. It tells you the *equivalent stock
position* the option behaves like, and it doubles as a quick-and-
dirty estimate of the probability the option finishes in the money.

Three ways to read the same number:

- **As a hedge ratio.** A call with $\Delta = 0.50$ moves like
  half a share of stock. To hedge ten such calls (1,000 share-
  equivalents) to delta-neutral, you sell 500 shares against them.
- **As a directional exposure.** A portfolio of options with net
  delta $+150$ behaves like 150 shares of the underlying for small
  moves. If the stock moves up $1 you make ~$150; if it moves
  down $1 you lose ~$150.
- **As a probability proxy.** Under Black-Scholes, $N(d_1)$ and
  $N(d_2)$ are *not the same probability*; the true risk-neutral
  probability of finishing ITM is $N(d_2)$, not delta. But the two
  are close for ATM options - close enough that traders quote
  "30-delta put" and "30% chance of expiring ITM" interchangeably,
  which is fine for quick decisions and wrong for anything
  requiring three decimals.

Delta runs from 0 to +1 for calls and 0 to -1 for puts. ATM
options have $|\Delta| \approx 0.5$. Deep ITM calls converge to
+1 (they behave like the underlying). Deep OTM calls converge to
0 (they behave like nothing).

#### 2.5 Gamma - The Curvature That Bites Sellers

Gamma is the *rate of change of delta* per $1 move in the underlying.
Two facts about gamma drive the bulk of Greek-aware risk management:

1. **Gamma peaks at-the-money.** Delta is most rapidly changing where
   the option is closest to flipping between "expiring in" and
   "expiring out". Far ITM and far OTM options have stable deltas
   (near 1 and near 0 respectively); ATM options have delta that
   ricochets with every dollar of spot.
2. **Gamma explodes near expiry.** As $T \to 0$, the gamma of an
   ATM option diverges. A 30-day ATM call has gamma ~0.07; a 1-day
   ATM call can have gamma north of 1.0. This is why the last
   week before expiry is qualitatively different from any earlier
   week and why option sellers either close or roll before they
   carry a short ATM strike into expiration week.

Long gamma (you bought the option) is good news on a move - your
delta moves with you. Stock rallies → your call's delta climbs from
0.50 toward 0.70, so you participate more in further upside. Stock
drops → delta falls toward 0.30, so you bleed less on further
downside. *Long gamma decelerates losses and accelerates gains.*
That is what you are paying theta for.

Short gamma (you sold the option) is the mirror image. Stock rallies
against your short call → your delta gets *more* short, so each
additional dollar of upside hurts more. Stock drops against your
short put → your delta gets *more* long, so each additional dollar
of downside hurts more. SOUL #6 says volatility-tails wag the dog;
*the mechanism is short gamma*. The position looks like steady
income at low realised vol and bleeds at compounding speed when
vol arrives.

#### 2.6 Theta - The Cost of Carrying Time

Theta is negative for long options (you lose value each calendar
day) and positive for short options (you collect each calendar day).
Three things to know about theta:

1. **Theta is highest at-the-money.** Same logic as gamma - the
   ATM option has the most extrinsic value to lose, so the daily
   melt is biggest there in absolute dollars. ITM and OTM options
   have less extrinsic to lose, so their theta is smaller.
2. **Theta accelerates as expiry approaches.** A 90-day ATM call
   loses theta at maybe $0.013 per day; a 30-day ATM call loses
   $0.04 per day; a 7-day ATM call loses $0.10 per day; a 1-day
   ATM call can lose $0.20 per day or more. The decay is non-
   linear - roughly *two-thirds* of a 90-day ATM call's premium
   is gone by the time DTE hits 30.
3. **Theta and gamma are joined at the hip.** A position cannot
   be long gamma without paying theta and cannot be short gamma
   without collecting theta. The arbitrage-free price of carrying
   gamma is theta. *That trade-off is what option-selling income
   strategies are.*

[image: image/week29_theta_decay.png — Theta acceleration and
the corresponding premium decay curve from 90 DTE down to 1 DTE
on the same ATM call.]

The 30-45 DTE window is the conventional sweet spot for theta-
collectors. Earlier than that, daily decay is small relative to
premium received; later than that, gamma starts to bite and the
position swings around violently with small spot moves. Weeks 27
and 28 used 30-45 DTE for exactly this reason - now you can see
on the chart why.

#### 2.7 Vega - The Greek That Hides In Plain Sight

Vega is the change in premium per *one percentage point* move in
implied vol. It is positive for *both* long calls and long puts
(buyers benefit when vol expands), negative for both short calls
and short puts (sellers benefit when vol contracts).

Three properties:

1. **Vega peaks at-the-money** - same shape as gamma.
2. **Vega is largest for *long-dated* options.** This is the
   cleanest counter-example to "all Greeks behave like gamma":
   gamma peaks near expiry, vega peaks far from expiry. A 1-year
   ATM option might have vega ~$0.40; a 30-day ATM option ~$0.11;
   a 1-day ATM option ~$0.02. Long-duration options are *vol
   instruments* almost more than they are direction instruments.
3. **Vol crush is a vega event.** When you buy an option ahead of
   earnings and IV ranks at the 90th percentile, you are buying
   30-50 vega-points of "earnings premium" that the market will
   evaporate the moment the print drops. The stock can move
   exactly the way you predicted and you can still lose money,
   because the directional gain (delta + gamma) does not cover
   the vega loss. Beginners learn this once.

Vega-aware position management is what separates *income
strategies* from *vol strategies*. A covered call sold at 15% IV
in a calm market has small vega; the same covered call sold at
40% IV during a market panic has large negative vega and can
print you a fast profit if vol mean-reverts even with the stock
unchanged. Side25 develops this further.

#### 2.8 Rho - The Greek You Mostly Ignore

Rho measures sensitivity to the risk-free rate. For a 30-day ATM
call on a $100 stock, rho is about $0.04 per 1% rate move - so
even a Fed-meeting-day swing of 25 bp moves the option's price
by about a *penny*. For most retail option positions on most days
of most months, rho is a rounding error.

When does rho actually matter?

1. **LEAPS** - long-dated equity options (1-3 year expiries) have
   rho large enough to register. A 2-year ATM LEAPS call on a
   $100 stock has rho near $1.40 per 1% rate move - that *is*
   meaningful.
2. **Regime transitions.** When the Fed is moving 75 bp at a
   meeting (think Q1 2022 or Q3 2025), even short-dated rho
   compounds across positions in a way you should at least be
   aware of.

Outside those, rho lives at the back of the dashboard. We mention
it for completeness; we do not optimise around it.

#### 2.9 How the Greeks Drive the Strategies You Already Know

The four conservative strategies from Weeks 25-28 each have a
characteristic Greek signature. Knowing it lets you predict how
each will breathe.

**Long calls (Week 25/26):** $\Delta > 0$, $\Gamma > 0$, $\Theta < 0$,
$\nu > 0$. You are paying theta and rho-bleed every day for the
right to participate in upside *and* benefit from a vol expansion.
This is a directional + vol bet wearing a leverage costume.

**Long puts (Week 25):** $\Delta < 0$, $\Gamma > 0$, $\Theta < 0$,
$\nu > 0$. Same Greek shape as a long call but with negative delta -
you are buying *insurance* against a drawdown, and the vega
component is precisely the reason puts get more expensive *during*
a sell-off (vol expands, vega works in your favour, but you
already paid for the put before the move).

**Covered calls (Week 27):** stock + short call. Net Greek:
$\Delta \approx 100 - 50 = +50$ per share-pair, $\Gamma < 0$ (small),
$\Theta > 0$ (you collect daily), $\nu < 0$ (small). You have
muted upside, retained most of the downside, and traded both for
a steady theta drip. SOUL #15 - the income SHOULD count as a tax-
shifting tool, not as alpha.

**Cash-secured puts (Week 28):** short put + cash. Net Greek:
$\Delta \approx +50$ per contract (similar directional exposure
to a covered call), $\Gamma < 0$, $\Theta > 0$, $\nu < 0$. The
trade is *equivalent* to a covered call by put-call parity - same
Greek skeleton, same risk profile, same theta engine. The
brokerage-margin treatment differs, the strategic logic does not.

**Iron condors and verticals (Week 30, preview):** combinations
designed to be *delta-neutral* and *short gamma + short vega +
long theta*. The trade is "I think realised vol will be lower
than implied vol." The Greeks let you measure exactly how much
vol-edge you need to break even.

The interactive at the end of this lesson lets you set spot,
strike, DTE, vol, and rate, and watch all five Greeks live as
sliders move - including a chart that sweeps the chosen Greek
across spot. *Drag the DTE slider and watch gamma climb at the
strike; that is the entire risk profile of selling weekly options
in one animation.*

[interactive: interactive/week29_greeks_lab.html]

---

### 3. Common Misconceptions

1. **"Delta is the probability of finishing in the money."** It is
   *close*, not equal. The risk-neutral probability of finishing ITM
   is $N(d_2)$, not $N(d_1) = \Delta$. The two diverge when vol or
   time is large. Use delta as a quick proxy; do not bet money on
   it being exact.

2. **"Theta is the same every day."** No. Theta on a 90-day option
   is small; on a 7-day option it is large. The headline number
   you read at trade entry is *today's* theta, not the path-average.
   The whole point of the theta-decay chart is that it accelerates.

3. **"If gamma is positive, I always make money on a move."** Long
   gamma helps you on *any* move, but you still pay theta to hold
   it. If realised volatility is below implied (i.e. the move is
   smaller than what the option priced in), theta wins and you
   lose. Long gamma is profitable only when realised vol exceeds
   implied vol over the holding period. *Every long-gamma trade is
   implicitly a long-vol trade.*

4. **"Vega and gamma are the same Greek."** They peak at the same
   strike (ATM) and have similar bell shapes versus spot, but they
   do *opposite* things versus time: gamma rises as expiry
   approaches, vega falls. A 1-day ATM option is mostly gamma; a
   1-year ATM option is mostly vega. Confusing them costs money
   when DTE matters.

5. **"Short options have unlimited risk because of theta."** Theta
   is *positive* for short options - it is your friend, not your
   enemy. The unlimited risk on a naked short call comes from
   *delta* (the underlying can run away from you) compounded by
   *gamma* (your delta gets shorter as it does). Theta is the
   payment you collect for accepting that risk, not the source
   of it.

6. **"Higher delta is always better for a call buyer."** Higher
   delta means more directional participation, but it also means
   *more capital outlay* (deep-ITM calls cost almost as much as
   the stock) and *lower vega* (you give up the IV-expansion
   bet). The 0.30-0.40 delta range is the conventional "speculative
   long" sweet spot precisely because it balances directional
   exposure against capital efficiency and convex vega payoff.

7. **"Vega only matters around earnings."** It matters every day
   any time IV is far from its long-run average. Owning long
   options at 30% IV when the post-FOMC reality is 18% IV is a
   guaranteed slow bleed independent of what the stock does.
   Persistent IV crush is the reason most retail directional
   options trades lose money even when the directional view was
   right.

8. **"Rho is irrelevant."** Almost true for short-dated options;
   not true for LEAPS. A 2-year ATM call on a $200 stock has
   meaningful rho. If you trade LEAPS without checking rho, you
   are leaving exposure unmonitored.

9. **"I can ignore the Greeks because my broker shows me a P&L
   chart."** A P&L chart at expiration is one slice of a five-
   dimensional surface. Greeks tell you the *path* between today
   and expiration. The chart tells you what happens *only* if you
   hold to the bell. Most positions are closed before that.

10. **"The Greeks are too mathematical for retail traders."** The
    formulas are mathematical; the *concepts* are arithmetic. If
    you can read a speedometer (delta), accept that the speedometer
    itself shifts under you (gamma), pay rent on parking (theta),
    and own a thermostat for fear (vega), you understand the
    Greeks. You do not need to derive Black-Scholes to use them.

---

### 4. Q&A Section

**Q: What is the easiest way to estimate delta if I don't have a
calculator?**
A: For ATM options, delta is approximately 0.50 for calls and -0.50
for puts. For each $1 of moneyness (ITM or OTM), shift delta by
about $0.05 / (\sigma \sqrt{T})$ - so for a 30-day, 20% vol option,
that is roughly $0.05 / 0.057 \approx 0.88$ per $1 of moneyness,
capped at $\pm 1$. In practice, just read it off your broker.

**Q: Why does my long call lose money on a flat day?**
A: Theta. Even with spot, vol, and rate unchanged, one calendar day
passing burns extrinsic value. For a 30-day ATM call that is roughly
$0.04 per share. If you bought 5 contracts, that is $20 of theta
across the day - on a quiet Tuesday, that is the entire P&L.

**Q: When should I worry about gamma the most?**
A: Two situations. First, when you are *short* options inside the
last two weeks before expiration with the stock close to your
strike - gamma there is large enough to flip you from "winning the
trade" to "underwater on the trade" with one news headline. Second,
when you are running multiple short-option positions in the same
underlying - gammas add, and a portfolio that is short 30 gamma is
qualitatively different from one short 5 gamma.

**Q: Are gamma and vega the same thing?**
A: No, but they share the at-the-money peak. Their *time profiles*
are opposite: gamma rises into expiry, vega falls. A short-dated
ATM option is mostly a gamma instrument; a long-dated ATM option
is mostly a vega instrument. This is why "selling weeklies" and
"selling LEAPS-puts" are very different strategies even though
both are short premium.

**Q: What is "vol crush" and which Greek explains it?**
A: Vega. Implied volatility tends to be elevated before
known-event dates (earnings, FOMC, biotech FDA decisions) and to
collapse the moment the event passes. If you own long options
across the event, you collect the directional move (delta and
gamma) but you also eat the IV collapse (a vega loss). Net P&L
is whatever wins. Beginners assume "stock moved my way → I made
money"; the Greek decomposition makes the loss diagnosable.

**Q: How big is rho really? Should I ever worry about it?**
A: For a 30-day ATM call, rho is about $0.04 per 1% rate move per
share. So a 25 bp Fed move is about a penny. Don't worry about
it on short-dated trades. For LEAPS (1-3 year expiries) rho can
be $1-$3 per 1% per share - large enough that a Fed pivot moves
the LEAPS premium materially even with the stock unchanged. So:
LEAPS yes, weeklies no.

**Q: If I sell a covered call, what does my net Greek profile look
like?**
A: Stock + short call. Per-100-shares-plus-one-short-call:
delta $\approx +50$ (you have ceded half your upside delta to the
short call), gamma slightly negative, theta positive (you are
collecting), vega slightly negative. The position has muted
upside, almost full downside, and a positive theta drip. SOUL #15
- the daily theta is income, not alpha.

**Q: What changes if I sell a cash-secured put instead?**
A: The Greek skeleton is identical to a covered call by put-call
parity - same delta, same gamma, same theta, same vega. The
*broker margin treatment* differs (one ties up shares, the other
ties up cash), but the risk profile is the same trade in two
costumes.

**Q: Can a short option position ever be long gamma?**
A: Not on a single short option. *Combinations* can engineer any
Greek profile - a long calendar (sell front-month, buy back-
month at the same strike) is short gamma but long vega; a long
straddle (buy a call and a put at the same strike) is long both.
Once you start composing positions, the Greeks add and you can
build essentially any signature you want.

**Q: How fast do the Greeks change in real markets?**
A: Delta changes continuously as spot moves (that is gamma).
Gamma drifts up as expiry approaches and explodes in the last
week. Theta accelerates non-linearly - the chart in §2.6 shows
the curve. Vega changes any time IV moves, which on equity
options is daily and on event-driven names hourly. Rho changes
with the rate curve, which is slow on most days. The five
Greeks together are a *time-varying* dashboard; nothing about
them is set at trade entry.

**Q: Where do dividends fit in?**
A: We deliberately used the no-dividend version of Black-Scholes
to keep this lesson clean. For dividend-paying stocks, a known
discrete dividend reduces call values and increases put values
(forward price drops by the PV of dividends). The Greeks shift
correspondingly, and continuous-dividend yield $q$ enters the
formulas as $S \to S e^{-qT}$ throughout. The shape of every
Greek profile is unchanged; the levels move modestly. For most
retail option work, ignoring dividends is a small error.

**Q: What is the single biggest practical use of the Greeks?**
A: Position sizing. "Three short puts" is uninformative;
"+150 deltas, +$8 theta per day, -$35 vega per vol-point,
-12 gamma" describes the trade. With those numbers you can ask:
*at what spot move do I lose all my theta? at what vol expansion
does my vega loss exceed two weeks of theta collected? what
does my delta become if the stock drops 5%?* Those are the
questions a Greek-aware trader answers before the trade is open;
a beginner answers them after the loss is realised.

---

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
dollar hurts more. SOUL number 6 - vol-tail-wags-dog - is
fundamentally a statement about short gamma. The position
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
