## Part 2: YouTube Script

---

**VIDEO TITLE:** "The Greeks Beyond the Greeks — Vanna, Charm, Color, and Why Dealers Pin SPX"

**RUNTIME TARGET:** ~12 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Horace:** *(seated, leaning into camera)* Two months ago we did
Week 29, the five Greeks. Delta, gamma, theta, vega, rho. We told
you that was 95 percent of what retail needs. And we still mean it.

**Stella:** *(off-camera, dryly)* So what's the other five percent?

**Horace:** The other five percent is what professional options
desks call the **higher-order Greeks**. Vanna. Charm. Color. Volga.
And the reason they have started mattering more — even for retail
who just look at the SPX chart — is because of the 0DTE explosion
since 2022. So today's lesson does two things. One, it teaches you
the math. Two, it shows you how dealer positioning around quarterly
OpEx now visibly moves the index. Most of this is going to be
context, not action items. The retail filter at the end is a
straight-up "if you have less than 5 percent of net worth in
options, watch this for fun."

**Stella:** Fun. Got it.

**[VISUAL: image/side20_second_order.png — full screen, 5 sec]**

**Horace:** That's our reference image — four panels of the
second-order Greeks on a 30-day at-the-money SPY-style call. Don't
memorize it. Recognize the shapes.

---

**[1:15 — RECAP THE FIRST FIVE]**

**Horace:** Quick recap. Delta, slope of the option-price curve.
Gamma, the curvature. Theta, the daily decay. Vega, sensitivity to
implied volatility. Rho, sensitivity to interest rates. That is
Week 29. If any of those words feel new, pause and watch that one
first.

**Stella:** What is a higher-order Greek?

**Horace:** It is a **derivative of a derivative.** Delta is how
much the option price moves per dollar of spot. *Vanna* is how
much delta moves per vol-point of IV. *Charm* is how much delta
moves per day of time elapsed. They are cross-partials.

---

**[2:30 — VANNA]**

**Horace:** Let's do vanna first because it is the one that
explains something most retail traders have already noticed without
being able to name. You are long an out-of-the-money put. The
market sells off. VIX spikes. And your put has *gone up more than
your delta predicted*. Not just because spot moved, not just
because vega — the delta itself shifted.

**Stella:** Because vanna.

**Horace:** Because vanna. The math is that vanna equals minus phi
of d1 times d2 over sigma. Don't memorize that. Memorize this: when
IV rises, OTM option deltas walk back toward the money in absolute
value. Your minus-25 put becomes a minus-40-ish put just from the
IV move.

**[VISUAL: image/side20_second_order.png, top-right panel zoomed]**

**Horace:** Top-right panel. That sine-wave-looking thing. Zero at
the money, peaks of opposite sign on either wing. That is vanna's
shape. Dealers running tail-hedge books obsess over the wing
exposure — the 10-delta and the 25-delta — exactly because that
is where vanna lives.

---

**[4:30 — CHARM]**

**Horace:** Charm is the same mechanic but with time instead of
vol. How much does my delta shift just from a day passing — even
if the underlying does not move at all?

**Stella:** *(skeptical)* Surely that is tiny.

**Horace:** It is tiny per-day. The number is in the third decimal.
Multiply it by a weekend, multiply it by a 100-lot, and you have
several hundred shares of effective stock exposure that has
silently appeared between Friday close and Monday open. Delta-
hedging desks rebalance for charm into Friday's print. We don't —
we just need to know it exists, because it is why **pin risk on
expiration Friday is real.** The closer you get to expiry, the
more violently delta drifts with no spot move.

**[VISUAL: image/side20_second_order.png, top-left panel]**

---

**[6:00 — COLOR]**

**Stella:** And color?

**Horace:** Color is gamma's version of charm. Just as charm is
how delta drifts with time, color is how *gamma* drifts with time.
Gamma is a bell. As you approach expiry, that bell gets taller and
narrower at the at-the-money strike. Color is the rate of that
narrowing. Bottom-left of the image.

**Stella:** And so on for volga.

**Horace:** Volga is the convexity of vega. Vega is not constant
in IV — when IV rises, vega itself rises for OTM strikes. That is
why deep-OTM puts can quintuple on a vol spike. Bottom-right.

---

**[7:30 — DEALER PINNING]**

**Horace:** OK, here is the part that is actually visible to retail.

**[VISUAL: image/side20_dealer_pinning.png — full screen, 5 sec]**

**Horace:** Illustrative SPX intraday on a quarterly OpEx Friday.
The index drifts in the morning, then around lunch starts
oscillating in a tighter and tighter band around the round-number
strike. By the close, it is doing 0.15-percent jiggles around 5000
like it is glued there.

**Stella:** Why does that happen?

**Horace:** Aggregate dealer gamma. Open interest at round strikes
is huge — 5000, 5100, 4900 on SPX. If dealers as a group are short
that gamma — meaning customers bought the options — then every
time the index ticks up, dealers have to sell to stay delta-neutral.
Every time it ticks down, they buy. They mechanically dampen moves.
The result is the pin.

**Stella:** Always a pin?

**Horace:** Not always. If dealers are net-long gamma — customers
sold the options instead — same setup produces the *opposite*:
moves get amplified. That is what happens on Powell-day FOMCs
sometimes. You don't need to predict it; you need to know which
regime you are in. Squeezemetrics, SpotGamma, and a couple of others
publish dealer-gamma estimates daily.

---

**[9:30 — INTERACTIVE WALKTHROUGH]**

**Horace:** The interactive on the page lets you sweep all five
first-order Greeks plus the four second-order ones for any
contract.

**[VISUAL: course/interactive/side20_greeks_explorer.html]**

**Horace:** Set spot 100, strike 100, 30 days, 20 percent vol. Look
at the nine numbers in the top row. Then below, you have a
sensitivity heat map — you can pick any one of the nine Greeks and
see how it changes as you move spot and DTE. Pick **vanna**. Notice
the diagonal stripe pattern — vanna is biggest at the wings and at
medium DTE. Now pick **color**. The whole surface concentrates near
ATM in the last 7 days. That is the gamma narrowing we just talked
about, visualized.

**Stella:** And charm?

**Horace:** Charm shows the largest absolute values right next to
expiration on the wings. Hovering near the money? Charm is small.
Already deep ITM or OTM, with 5 days left? Charm is huge.

---

**[10:45 — RETAIL FILTER]**

**Horace:** Three rules to take home.

**Stella:** *(counting)* One.

**Horace:** Less than 5 percent of net worth in options? You don't
need this. Read it once for context. Use the first-order Greeks for
sizing.

**Stella:** Two.

**Horace:** Running a delta-hedged book, holding through expiry
week, or doing 0DTE? You need this. Vanna and charm are doing your
P&L while you are not looking.

**Stella:** Three.

**Horace:** Watch quarterly OpEx weeks — March, June, September,
December. The pinning pattern is real, dealer-gamma estimates are
published, and the play is "do not chase intraday SPX action that
looks magnetized to a round strike." It is not magic. It is flow.

---

**[OUTRO — 11:45]**

**Horace:** That is Side 20. Next up, Side 21 will be — *(beat)* —
Stella, what is next?

**Stella:** *(reading off-screen)* Tax-loss harvesting deep dive.

**Horace:** Yeah. Less exotic, more money.

**Stella:** Always more money.

**[END]**
