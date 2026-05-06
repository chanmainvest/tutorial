# Week 5: Bonds — Coupons, Prices, and Yields

---

## Part 1: Reading Section

---

### 1. Why This Is Important

A bond is the simplest financial instrument in the world. You lend
someone a known amount, on a known schedule, for a known coupon, and
they pay you back at a known date. Four numbers and a calendar.
Stocks have nothing this clean.

And yet — bonds, the simplest instrument, generated the largest
single multi-decade trend in modern financial history (a forty-year
bull market from 1981 to 2020 in falling yields), and then in 2022
delivered the worst calendar year for US Treasuries on record. Both
moves were already inside the four-number contract, waiting for the
investor to do the price-yield arithmetic.

You need to understand bonds for four reasons.

1. **They are the discount rate of everything.** Every cash flow on
   earth — your house, a stock's earnings stream, a private-equity
   exit, a pension liability — is priced by discounting against the
   risk-free Treasury curve. When the 10-year yield moves from 1.5%
   to 4.5%, every long-duration asset on the planet reprices. You
   cannot understand any other asset class without understanding
   what its discount rate is doing.
2. **They are an asset class in their own right.** Last week's 60/40
   leaned on Treasuries for the diversification benefit. This week
   we open the bond box and ask: what are we actually holding,
   how does it pay, and how does its price form? After this lesson
   the 40 in 60/40 is no longer a black box.
3. **They tell you what the market expects.** The yield curve, the
   spread between BAA corporates and 10-year Treasuries, and the
   TIPS breakeven rate are three separate, daily-quoted, public
   forecasts of growth, default risk, and inflation. The bond
   market is the cheapest macro intelligence service on earth.
4. **The 1981-2020 bond bull market is the regime backdrop for
   almost every "passive works" claim of the last two generations.**
   Horace's regime-shift framing — that we are 40+ years into a
   passive-investing-friendly regime that *has triggers we should
   watch* — sits squarely on top of the bond chart. A generation
   of investors has never seen a real bond bear market. 2022 was
   the first warning shot.

---

### 2. What You Need to Know

#### 2.1 The Bond Cash Flow — Four Numbers and a Calendar

A bond is fully specified by:

- **Face value** $F$ — the amount returned at maturity. Almost
  always $1,\!000 in the US market, conventionally quoted as 100.
- **Coupon rate** $c$ — the annual interest rate, fixed at issue.
  A 4% coupon on a $1,\!000 face pays $40 per year.
- **Years to maturity** $N$ — when face is repaid.
- **Payment frequency** $m$ — how many coupon payments per year.
  US Treasuries and corporates: $m = 2$ (semi-annual). Many
  international bonds: $m = 1$ (annual). Some municipals: $m = 4$.

Each coupon is $C = F \cdot c / m$. So a 4% semi-annual coupon
on $1,\!000 face pays $20 every six months for $N$ years, plus
$1,\!000 at the end.

That's it. That's the contract. Everything else — price, yield,
duration, convexity — is *math performed on those four numbers
plus a discount rate*.

#### 2.2 Price Is Just Discounted Cash Flow

If you require an annual return of $y$ (the **market yield**, or
**yield to maturity**) on the bond's risk profile, then the price
you should be willing to pay today is the present value of every
cash flow:

$$ P = \sum_{t=1}^{m \cdot N} \frac{C}{(1 + y/m)^{t}} + \frac{F}{(1 + y/m)^{m \cdot N}} $$

That sum has a closed form:

$$ P = C \cdot \frac{1 - (1 + y/m)^{-mN}}{y/m} + \frac{F}{(1 + y/m)^{mN}} $$

But the formula matters less than the *shape*: a bond is one
geometric series of coupons plus one balloon payment of face. Drop
either piece and you have a different instrument (the geometric
series alone is an annuity; the balloon alone is a zero-coupon
bond).

Three immediate consequences:

- If $y = c$, then $P = F$. The bond trades **at par**.
- If $y > c$, the cash flows aren't generous enough to give the
  buyer the required return at face. The price must drop. Bond
  trades at a **discount**.
- If $y < c$, the buyer is happy to pay more than face for the
  generous coupon. Bond trades at a **premium**.

The interactive panel later in this lesson lets you slide $c$, $y$,
$N$, and $m$ live and watch $P$ recompute. Spend two minutes on
it. Internalising the shape of the price-yield curve is worth more
than memorising any formula.

#### 2.3 Why Price and Yield Move Inversely

This is the single most asked-about feature of bonds, so be
explicit. The cash flows are *fixed at issue*. Coupons are $C$
forever, face is $F$ forever. The only thing that changes day to
day in the secondary market is the *discount rate* the market
applies to those fixed cash flows. Higher discount rate -> lower
present value -> lower price. Lower discount rate -> higher present
value -> higher price.

The relationship is **monotonic and convex**. Monotonic: each $1
move in yield always moves price in the opposite direction.
Convex: the price-yield curve bows toward the origin, which means
**a 1% drop in yield raises price by *more* than a 1% rise in
yield lowers it**. That asymmetry is convexity, and for long bonds
it is large. Watch it on the interactive: hold $c$, $N$ fixed,
slide $y$ from 0% to 15% and see how the curve bends.

#### 2.4 Duration — The "How Sensitive" Number

A 30-year bond and a 2-year bond do not respond equally to a 1%
move in yield. Duration is the linear approximation of how much
the price moves for a 1% yield change.

The **Macaulay duration** is the weighted average maturity of the
cash flows, where each weight is the present value of that cash
flow divided by the price:

$$ D_{\text{Mac}} = \frac{1}{P} \left[ \sum_{t=1}^{m N} \frac{(t/m) \cdot C}{(1 + y/m)^{t}} + \frac{N \cdot F}{(1 + y/m)^{m N}} \right] $$

The **modified duration** is the elasticity of price with respect
to yield:

$$ D_{\text{mod}} = \frac{D_{\text{Mac}}}{1 + y/m} \quad \Rightarrow \quad \frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y $$

Rules of thumb worth memorising:

- 2-year Treasury: $D_{\text{mod}} \approx 1.9$. A 1% rate rise ->
  ~1.9% price drop.
- 10-year Treasury: $D_{\text{mod}} \approx 8.5$. A 1% rise ->
  ~8.5% price drop.
- 30-year Treasury: $D_{\text{mod}} \approx 19$. A 1% rise ->
  ~19% price drop.

In 2022, the 10-year yield rose from ~1.5% to ~3.9%, about 2.4%.
Multiply by a duration of 8.5 and you get the realised -18% total
return on the 10-year — almost exactly the loss we attributed to
"bonds" in last week's 60/40 chart. The duration approximation is
not a curiosity; it is the explanation. The deeper math (convexity
adjustment, key-rate durations, OAS) waits for Week 32.

#### 2.5 Yield to Maturity, Current Yield, and Coupon Rate

Three numbers that everyone confuses.

- **Coupon rate**: the *contractual* interest rate. Fixed at issue.
  Never changes. Used for computing the dollar coupon.
- **Current yield**: $C \cdot m / P$. What the coupon stream alone
  pays you, ignoring the pull-to-par on the principal. Useful for
  income-oriented buyers but **incomplete** as a return measure.
- **Yield to maturity (YTM)**: the single discount rate $y$ that
  makes the present value of *all* cash flows (coupons + face)
  equal to today's price. The internal rate of return on the bond.
  This is the headline yield you see quoted everywhere.

When a bond trades at par, all three are equal. When it trades at
a discount, YTM > current yield > coupon rate (you get the coupon
*and* a capital gain at maturity). When it trades at a premium,
YTM < current yield < coupon rate.

Always compare bonds on YTM, not coupon. The coupon is a contract
detail; the YTM is the return you actually earn if you hold to
maturity and reinvest at the same rate.

#### 2.6 Credit Spreads — The Premium for Default Risk

A US Treasury is the textbook default-free asset (it is *as*
default-free as the dollar itself, which is a separate
philosophical issue — see Week 31). Anything else is riskier.
The market prices that extra risk by demanding a higher yield on
the corporate bond than on the matched-maturity Treasury. The
difference is the **credit spread**.

The chart below plots the BAA-corporate-minus-10-year-Treasury
*annual return* spread from 1928 through 2024 (Damodaran annual
series, BAA being the lowest investment-grade rating). It is the
single best long-run historical proxy we have for the realised
behaviour of corporate default risk vs Treasuries.

![Annual BAA corporate bond total return minus 10-year US Treasury total return, 1928 through 2024 (Damodaran data, decimal). Spread spikes downward in 1932, 1974, 2008, and 2020 as defaults reprice and Treasuries rally on flight-to-safety. Long-run average is small and positive; the distribution has a fat left tail.](image/week05_credit_spreads.png)

Three reads:

1. **The long-run mean spread is small and positive** — investment-
   grade corporate debt earns roughly 1-2% per year above
   Treasuries on average, which is the unconditional credit
   premium.
2. **The distribution has a fat left tail.** In a credit blow-up
   year (1932, 1974, 2008, 2020), corporates can underperform
   Treasuries by 10%-25% in a single year as default risk reprices
   and Treasuries rally on the flight-to-safety bid.
3. **The spread spikes are leading indicators.** Credit spreads
   widen *before* equity bear markets typically bottom. By the
   time you see the spike on the chart, the recession trade is
   already happening across the rest of the market.

For most retail investors the practical answer is: **the credit
premium is real but small, and the tail risk is asymmetric**.
Holding investment-grade corporate debt instead of Treasuries earns
you maybe 1% extra in normal years and costs you 10%+ in the
years that matter most. For diversification against equities, hold
Treasuries. For yield-pickup *income* in retirement, a small
allocation to investment-grade corporates is reasonable.

#### 2.7 The Forty-Year Bull Market and the 2022 Break

The chart below plots the 10-year US Treasury yield from 1962
through 2026, the longest clean monthly run we have on FRED's DGS10
series.

![10-year US Treasury constant-maturity yield, 1962 through April 2026 (FRED DGS10, monthly). The dominant feature is the 1981 peak near 15.8% under Volcker's anti-inflation campaign, followed by a four-decade decline to the 2020 trough near 0.5%, then a sharp climb back above 4% by 2024 with current readings near 4.2% in April 2026. Annotated peaks and troughs.](image/week05_yield_history.png)

Three regimes you need to recognise.

- **1962-1981: yields rose.** Inflation accelerated through the
  Vietnam war, the Bretton Woods collapse, and two oil shocks.
  Bond returns over this period were poor in nominal terms and
  catastrophic in real terms — the worst sustained bond bear
  market of the 20th century. Holders of "safe" long Treasuries
  lost real wealth for two decades.
- **1981-2020: yields fell, in a near-uninterrupted forty-year
  trend.** Volcker's 1981 rate peak broke inflation expectations,
  and every subsequent shock — 1987, 1990, 2000, 2008, 2020 — was
  met with lower terminal rates than the previous one. Bonds
  delivered roughly 7% nominal annualised returns over this stretch,
  the best forty-year run in their history.
- **2020-202?: yields rose again.** The COVID liquidity flood, then
  the 2022 inflation shock, ended the forty-year trend. The 10-year
  ran from 0.5% to 5% in 30 months. As of April 2026, the curve
  is near 4.2% and the market is debating whether we're in a 1980s-
  style normalisation or the start of a long secular grind higher.

The Horace frame: passive index investing
*works* in regimes where bonds rally and stocks rally together
because rates are falling. A generation of investors built the
"just buy and hold" intuition on the 1981-2020 backdrop. The
trigger that breaks the regime is **a sustained rise in long
yields**. We are watching that trigger fire right now in real time.
It is too early to declare the regime over; it is too late to
pretend nothing has changed.

---

### 3. Common Misconceptions

**Misconception 1: "Treasuries are riskless."**

Treasuries are *credit*-riskless (the US government can print the
dollars it owes). They are not *price*-riskless or
*purchasing-power*-riskless. In 2022 the 10-year lost 18% of its
price. In 1973-1981 it lost roughly 40% of its real value. "No
default risk" is not the same as "no risk."

**Misconception 2: "If I hold to maturity, I can't lose."**

In *nominal* terms, yes — you get face plus coupons back. But the
real value of those payments depends on inflation between purchase
and maturity. A 30-year bond bought at 2% in 2020 is contractually
locked in to deliver a real loss if inflation averages 3% over the
holding period. Holding to maturity protects you from price
volatility, not from inflation.

**Misconception 3: "Bond funds just hold bonds — they should
behave the same as holding the bonds directly."**

A bond fund maintains a roughly constant duration by selling old
bonds and buying new ones. An individual bond's duration *falls
mechanically* as it approaches maturity. So a fund that targets
20-year duration is, in a rising-rate environment, the structurally
worst possible thing to hold — exactly what TLT investors learned in
2022. If you have a specific liability date, hold individual bonds
matched to that date; a fund is not equivalent.

**Misconception 4: "Higher coupon means higher yield."**

The coupon is the contract; the yield is the market price. A 10%
coupon bond can have a 3% yield (it's trading at a huge premium)
and a 1% coupon bond can have a 6% yield (it's at a deep
discount). Always compare on YTM, not coupon.

**Misconception 5: "Credit spreads are just extra yield — free
income."**

The historical credit premium is 1%-2% in the average year and
-10%-or-worse in the years that matter (1932, 1974, 2008, 2020).
Credit spread is *insurance you sell to companies in exchange
for steady income*, with rare large losses. Selling insurance
isn't free income; it's a structurally negatively-skewed payoff.

**Misconception 6: "Long bonds have higher yields, so they're
better."**

Longer maturity earns the *term premium* — but with much higher
duration risk. The Sharpe ratio of long Treasuries is comparable
to or *worse* than that of intermediate Treasuries over most
historical windows. Reach for the term premium only if you have a
specific liability that matches that maturity, or you are
explicitly making a duration bet.

**Misconception 7: "Inflation-protected bonds (TIPS) are always
better than nominal bonds."**

TIPS are better when inflation surprises *upward* relative to the
breakeven rate priced into them. They are worse when inflation
surprises downward, or when the breakeven is expensive. TIPS are a
*relative* trade against nominal Treasuries, not a free upgrade.

**Misconception 8: "Negative-yield bonds make no sense and no one
should buy them."**

European and Japanese institutional investors held trillions of
dollars in negative-yielding bonds during 2014-2021 because:
liability-matching, regulatory capital requirements, currency
hedging carry, and price upside if rates went *more* negative.
"It makes no sense for me as a retail investor" is correct. "It
makes no sense for anyone" is wrong.

---

### 4. Q&A Section

**Q1: I want monthly income from bonds. What's the cleanest way?**

A: Build a *bond ladder* — buy individual Treasuries or TIPS
maturing in each of the next 5-10 years, equal-weighted. Each
year one rung matures and you reinvest at the then-current yield.
Cash flow is roughly the average yield × portfolio value. Avoids
fund duration drift and gives you a predictable schedule. The
brokerage tools at Fidelity, Schwab, and Vanguard all let you
build a ladder in 15 minutes.

**Q2: Should I buy individual bonds or bond ETFs?**

A: For amounts under ~$100k, ETFs (BND, AGG, IEF, TLT, SHY) are
cheaper and more liquid. For amounts above that, or for retirees
with specific liability dates, individual Treasuries can be
better — you avoid the duration mismatch and you can hold to
maturity. Corporate bonds individually are almost never worth it
for retail (poor liquidity, wide spreads); use a fund (LQD).

**Q3: What's the right bond duration for me?**

A: Roughly match your investment horizon. 1-3 year Treasuries (SHY)
for money you need within five years. Intermediate (IEF, ~7 yr) for
the diversifier sleeve in a 60/40-style portfolio. Long bonds (TLT,
~20 yr) only as a deliberate duration bet — not as a default. The
2022 lesson: duration is a *loaded* dimension; don't accidentally
take more than you intended.

**Q4: How is a TIPS different from a regular Treasury?**

A: A TIPS' principal adjusts upward with CPI. The coupon rate is
fixed but applies to the inflation-adjusted principal, so dollar
coupons grow with inflation too. The "real yield" you see quoted on
TIPS is the yield *above* CPI. Buy TIPS when you think realised
inflation will exceed the breakeven (the difference between nominal
and TIPS yields). In April 2026 the 10-year breakeven is about
2.4%; TIPS win if average CPI over the next decade exceeds that.

**Q5: Why did the long bond fall 30% in 2022 when "bonds are safe"?**

A: Long-bond duration is roughly 19. Yields went from ~1.5% to
~4%. Multiply: 19 × 2.5% ≈ 47% expected price drop, partially
offset by coupon income, netting to the realised -30% range.
"Bonds are safe" is shorthand for "low credit risk", not "low
price volatility." Long bonds have equity-like price volatility
when rates move sharply.

**Q6: What's the yield curve and why do people obsess over it?**

A: The yield curve is yields plotted against maturity (3-month,
1-year, 5-year, 10-year, 30-year). Normally upward-sloping (longer
= higher yield). When the 2-year exceeds the 10-year — the
*inverted* curve — it has historically been the single best
recession leading indicator, with a 12-24 month lead. April 2026
state: curve has just *un*-inverted after a record-long inversion.
Whether the post-inversion recession is now off the table or merely
delayed is the live debate.

**Q7: What is "convexity" in one sentence?**

A: The bend in the price-yield curve — the higher-order term that
makes price gains from falling rates larger than price losses from
the same-size rising rates. Long bonds and zero-coupon bonds have
the most convexity. It's a free option that gets paid for via
slightly lower yield. Week 32 unpacks it formally.

**Q8: Are corporate bonds a substitute for Treasuries in 60/40?**

A: No. Corporate bonds have meaningful equity-correlation in
crises (the BAA spread chart in §2.6 makes this concrete) and so
they don't deliver the negative correlation that Treasuries give
you in a flight-to-safety event. If you want yield, take it on
the *equity* side; keep the bond sleeve in Treasuries for the
diversification job.

**Q9: How much of my portfolio should be bonds?**

A: Outside of the 60/40 baseline (Week 4), the barbell shape
holds *less* bonds than 60/40, *more* in cash + short Treasuries
on the safe side, and *more* in equity tail bets on the
asymmetric side. A 30-year-old building wealth probably runs
20-30% in short Treasuries; a 65-year-old in distribution probably
runs 40-50%. The exact number is less important than understanding
*what role* bonds play (price stability + recession hedge) and
sizing accordingly.

**Q10: What about high-yield ("junk") bonds?**

A: High yield is a *third* asset class. Correlated more to equities
than to Treasuries (about 0.7 to S&P 500). Sharpe ratio over the
full cycle is mediocre. Default rates spike in recessions. A small
allocation can be defensible for income-focused retirees but it
should never replace your Treasury sleeve — it doesn't do the
diversification job that Treasuries do.

**Q11: Where does this lesson connect to the rest of the course?**

A: Week 4 used Treasuries as a black box; this week opens the box.
Week 13-14 (the barbell) chooses *short* Treasuries over long for
the safe sleeve based on §2.4. Week 31-34 covers the 2022 inflation
break in macro detail (the regime story behind the yield-history
chart). Week 32 specifically does the rigorous duration and
convexity math. Week 47 and 50 cover long-volatility / managed-
futures overlays that hedge the inflation tail that bonds can't.

The interactive panel below lets you slide the four-number bond
contract (face, coupon, maturity, payment frequency) and the
market yield, and watch the price recompute live. The chart shows
the price-yield curve from 0% to 15% with your current point
marked. Watch the curvature change as you increase maturity — the
30-year line is dramatically more convex than the 2-year. Macaulay
and modified duration are reported below the chart.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Bonds — Coupons, Prices, and Yields | Week 5

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO]**

**Horace:** Last week was the 60/40 portfolio. We treated the 40 as
a black box called "Treasuries." This week we open the box.

**Stella:** And inside the box is...

**Horace:** Four numbers and a calendar. That's it. A bond is the
simplest financial instrument on earth. Face value, coupon rate,
maturity, payment frequency. Done. Stocks have nothing this clean.

**Stella:** So why did the simplest instrument blow up the worst in
2022?

**Horace:** Because the *price* of a bond isn't one of the four
numbers. The price is what falls out when you discount those four
numbers at today's market yield. And in 2022, the discount rate
moved more in twelve months than it had in any previous twelve
months on record.

---

**[SEGMENT 1: THE FOUR NUMBERS]**

**Horace:** Let's get concrete. A 10-year US Treasury, 4% coupon,
$1,000 face, semi-annual payments. The contract says: every six
months for ten years, you get $20. At the end, you get the $1,000
back. Twenty payments of $20 plus a balloon of $1,000.

**Stella:** And the price I pay today is not necessarily $1,000.

**Horace:** Correct. The price is whatever today's buyers are willing
to pay for that exact stream of cash. If today's market yield on
ten-year risk is 4%, you pay exactly $1,000 — par. If today's
yield is 5%, you pay less than $1,000, because the $20 coupons
aren't generous enough at 5%. If today's yield is 3%, you pay more
than $1,000, because $20 every six months is more than the market
demands.

**Stella:** And someone always exists on the other side.

**Horace:** That's the part people miss. Every traded bond is
someone agreeing the price is right *and* someone disagreeing.
Nobody is forced to trade. The price is just the level where the
two sides meet.

---

**[SEGMENT 2: THE PRICING FORMULA]**

**Horace:** Here's the equation. Price equals the present value of
every coupon, plus the present value of the face. Discounted at
yield divided by the payment frequency. That's it.

It looks ugly written out — sum from t=1 to mN of C divided by
(1 plus y over m) to the t, plus F divided by (1 plus y over m)
to the mN. It looks ugly. It is not ugly. It is a geometric series
plus a balloon. The sum has a closed form, but you don't need to
memorise the closed form. You need to internalise the *shape*.

**Stella:** Which is?

**Horace:** A bond is one stream of small coupons plus one big
balloon at the end. The coupons together are an *annuity*. The
balloon by itself is a *zero-coupon bond*. Every fixed-income
security in the world is some weighted sum of those two pieces.

---

**[SEGMENT 3: PRICE AND YIELD GO OPPOSITE WAYS]**

**Horace:** The most asked-about feature of bonds. The cash flows
are fixed at issue. Coupons are $20 per period forever. Face is
$1,000 forever. The only thing that changes day to day is the
discount rate the market applies to those fixed cash flows.

**Stella:** Higher discount rate means lower present value.

**Horace:** Right. So higher yield means lower price. Lower yield
means higher price. Always. Without exception. And the relationship
isn't a straight line — it's *convex*. The curve bows toward the
origin. Which means a 1% drop in yield raises price *more* than a
1% rise in yield lowers it. That asymmetry is convexity, and for
long bonds it's substantial.

**Stella:** That sounds like a free lunch.

**Horace:** It's a paid-for lunch. The market knows about convexity
and prices it in. You collect the convexity benefit at the cost of
slightly lower coupon. Week 32 does the math. For now, just notice
the curve in the interactive bends.

---

**[SEGMENT 4: DURATION — THE ONE NUMBER YOU MUST KNOW]**

**Horace:** Not all bonds respond equally to a 1% rate move. Duration
tells you *how much* a given bond's price moves for a 1% yield
change. Here are the three numbers I want you to memorise.

Two-year Treasury: duration about 1.9. Ten-year: about 8.5.
Thirty-year: about 19.

**Stella:** So if rates go up 1%, the long bond falls 19%.

**Horace:** Approximately, yes. And here is the punchline of 2022.
The ten-year yield went from 1.5% to 3.9%. That's a 2.4% move.
Multiply by duration of 8.5. You get an 18% loss.

**Stella:** Which is exactly what happened.

**Horace:** Exactly. Last week we said "bonds had their worst year
since 1937." Now you know *why* in one multiplication. Duration
times yield change. The 60/40 chart isn't mysterious; it's
arithmetic.

---

**[SEGMENT 5: COUPON, CURRENT YIELD, YTM — THREE THINGS, NOT ONE]**

**Horace:** Three numbers people confuse constantly.

Coupon rate. The contract. Fixed at issue. Never changes. Used to
compute the dollar coupon.

Current yield. Coupon dollars divided by current price. What the
income stream alone pays. Ignores the gain or loss at maturity.

Yield to maturity. The internal rate of return on the bond.
Discount rate that makes price equal the sum of present values.
This is the headline yield. Always compare bonds on YTM, not
coupon.

**Stella:** And when the bond trades at par...

**Horace:** All three are equal. When the bond trades at a
discount — price below face — YTM is the highest of the three.
At a premium, YTM is the lowest. The interactive shows you all
three simultaneously.

---

**[SEGMENT 6: CREDIT SPREADS]**

[VISUAL: image/week05_credit_spreads.png]

**Horace:** A US Treasury is the textbook default-free asset.
Anything else is riskier. The market prices that extra risk by
demanding a higher yield. The difference is the credit spread.

This chart is the BAA-corporate-minus-10-year-Treasury return
spread from 1928 forward. Long-run mean is positive but small —
corporate investment-grade earns about 1 to 2 percent extra per
year on average.

**Stella:** And the spikes?

**Horace:** 1932. 1974. 2008. 2020. The four worst credit blow-ups
of the modern era. Corporates can underperform Treasuries by 10 to
25 percent in a single year as default risk reprices. The
distribution has a fat left tail.

**Stella:** So the credit premium is...

**Horace:** Insurance you sell to corporations in exchange for
steady small income, with rare large losses. Selling insurance is
a structurally negatively-skewed payoff. It's not free yield.

The retail takeaway: hold Treasuries for the diversification job,
not corporates. If you want yield, take it on the equity side.

---

**[SEGMENT 7: THE FORTY-YEAR BULL MARKET AND THE 2022 BREAK]**

[VISUAL: image/week05_yield_history.png]

**Horace:** This is the most important chart in the entire bond
universe. Ten-year Treasury yield from 1962 through April 2026.

Three regimes. From 1962 to 1981, yields rose. Inflation, Vietnam,
Bretton Woods, the oil shocks. Volcker breaks the back of inflation
in 1981 with a 15.8% peak in the ten-year. From 1981 to 2020, yields
fell. Forty years. Almost uninterrupted. Every shock met with lower
terminal rates than the previous shock. The ten-year hit 0.5% in
2020.

**Stella:** And then?

**Horace:** Then 2022 happened. Yields ran from 0.5% to roughly 5%
in thirty months. As of April 2026 we're sitting around 4.2%, and
the market is debating whether this is a 1980s-style normalisation
or the start of something more durable.

**Stella:** What's the lesson?

**Horace:** This is the regime point. We have been forty
years inside a regime that made passive index investing look like a
free lunch. The regime had a specific macro signature: falling
yields meant rising bond prices, rising equity multiples, and a
benign correlation structure between the two. The trigger that
breaks the regime is a *sustained* rise in long yields. We are
watching that trigger fire right now.

It is too early to say the regime is over. It is too late to
pretend nothing has changed. The bond chart is the regime backdrop
to everything else we cover from Week 31 onward.

---

**[SEGMENT 8: THE INTERACTIVE]**

**Horace:** Open the bond pricer panel. Five inputs: face value,
coupon, years to maturity, market yield, and payments per year.
Slide them. Watch the price update.

**Stella:** What should I look for?

**Horace:** Three things. First, set yield equal to coupon. Confirm
the price is exactly face. Second, hold everything constant and
move maturity from 2 years to 30 years. Watch the price-yield curve
bend much harder. That's convexity becoming visible. Third, watch
the duration readout. Notice that as you raise the coupon, duration
falls — high-coupon bonds return cash faster, so they're less
sensitive to the discount rate.

**Stella:** And the duration prediction?

**Horace:** Pick a bond. Read duration off the panel. Move yield by
1%. Multiply. Compare to the actual price change. The approximation
is excellent for small moves and breaks for large moves. That's
where convexity comes in. Save the rigorous version for Week 32.

---

**[OUTRO]**

**Horace:** Bonds are four numbers and a calendar. The price is
discounted cash flow. Yield and price move opposite ways. Duration
is the linear sensitivity. Credit spread is insurance you sell.
The forty-year bull market is the regime that built passive
investing's reputation, and it ended in 2022.

That's the entire bond universe in one paragraph. We will spend
Week 32 on the deeper math and Weeks 31-34 on the macro regime
that broke. Tonight, slide the interactive until the four-number
contract feels obvious.

**Stella:** Next week?

**Horace:** Diversification done right. Or, why you can't just buy
twenty stocks and call it a day.

---

**END SCREEN:** "Next: Week 6 — Diversification Beyond 60/40"
