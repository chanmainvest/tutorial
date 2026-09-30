## Part 2: YouTube Script

---

**VIDEO TITLE:** All-Weather, Risk Parity, and Why 60/40 Is Not Enough — Multi-Asset Portfolios from Scratch
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Stella:** Welcome back. Today is Week 15, and we are putting last
week's pieces inside one allocation framework. By the end of this
video you will know what risk parity actually is, why the
Bridgewater four-quadrant model is the cleanest macro picture you
will ever own, and how the four-tranche book is the retail version
of the same idea.

**Horace:** And we are going to be honest about 2022. The strategy I
am about to recommend lost 25% that year at Bridgewater. Risk parity
is not a magic word. It is a chassis with assumptions, and the
assumptions break sometimes.

**Stella:** Here is the plan. First, the four quadrants. Then the
risk-parity math. Then the 2022 break. Then the four-tranche book
applied at retail scale. Then a backtest 1928 to 2024. Then the
interactive.

---

**[SECTION 1 — THE FOUR QUADRANTS — 1:20]**

**Horace:** Two axes. Growth surprise on the vertical, inflation
surprise on the horizontal. Four cells.

[VISUAL: image/week15_quadrants.png]

**Horace:** Top-right cell, the Goldilocks cell — growth surprises
up, inflation surprises down. That is the 1990s. That is 2013-2019.
Equities win. Long the index, you are home.

**Stella:** Top-left, both surprise up. That is 2003-2007 reflation,
that is 2021. Commodities, energy, materials, emerging markets.

**Horace:** Bottom-right, both surprise down. Deflationary recession.
2001-02. 2008-09. 2020. Long-duration Treasuries dominate.

**Stella:** And bottom-left.

**Horace:** Stagflation. Growth slowing, inflation rising. 1973-74.
1979-80. *2022*. Gold. TIPS. Short-duration cash. The cell where
60/40 dies.

**Stella:** And the punchline?

**Horace:** Most retail portfolios are unhedged top-right bets.
Long-only equity is a one-quadrant trade. It works until it doesn't.

---

**[SECTION 2 — RISK PARITY MATH — 4:00]**

**Stella:** OK, so the Bridgewater answer is: hold one asset levered
to each cell at equal risk contribution. What does that mean
mathematically?

**Horace:** One equation. Weight on each asset equals one-over-its-vol,
divided by the sum of one-over-vols. So equity at 16% vol gets a
small weight; bonds at 6% vol get a big weight; gold at 18% vol gets
a small weight; cash at 1% vol gets a huge weight.

**Stella:** And the cash thing is a problem.

**Horace:** Pure inverse-vol wants 100%+ in cash. So you drop cash
and lever the remainder. Bridgewater levers 1.5 to 2x to hit 10%
target vol on the portfolio. The leverage is mostly Treasury futures
because basis is tight and margin is cheap.

**Stella:** And without leverage?

**Horace:** Unlevered all-weather earns 5-6% per year. Loses to
60/40. The leverage is the price of admission.

---

**[SECTION 3 — THE 2022 BREAK — 6:30]**

**Stella:** Walk us through 2022.

**Horace:** Stock-bond correlation flipped from negative to positive.
Same shock — Fed hiking aggressively into a 9% CPI print — hurt both
legs together. TLT down 31%. SPY down 18%. Bloomberg Aggregate down
13%, the worst year since the index started in 1976.

**Stella:** And risk parity?

**Horace:** Bridgewater All-Weather lost ~25%. AQR's QRPIX lost ~19%.
The leverage on the bond sleeve amplified the bond loss. There was
no quadrant working — gold was flat, equity was down, bonds were
down. The diversification math assumed correlations would stay where
the back-test put them. They did not.

**Stella:** Is risk parity broken?

**Horace:** No. It is *more vulnerable* to correlation regime changes
than the marketing said. The institutional response since 2023 is to
hold less duration leverage and more inflation hedges. The shape is
converging on what we call the four-tranche book.

---

**[SECTION 4 — THE FOUR TRANCHES — 9:30]**

**Stella:** OK, so let's see the retail version.

[VISUAL: image/week15_four_tranches.png]

**Horace:** Forty percent growth. Thirty percent income. Twenty
percent store-of-value. Ten percent opportunistic. Four ETFs gets
you 90% of the way there: VTI, IEF, GLD, BIL.

**Stella:** And how does this compare to Bridgewater's original
weights?

**Horace:** Bridgewater 1996 ran roughly 30% equity, 55% bonds, 7.5%
gold, 7.5% commodities, levered 1.5x. We are running unlevered, with
*more* equity, *less* duration, and *more* gold. Three regime shifts
since 1996 justify that adjustment. The biggest is 2022.

**Stella:** And the opportunistic ten percent?

**Horace:** Cash, T-bills, and a small barbell sleeve — a budget
for long-vol options or for adding to equity at a 30% drawdown. The
sleeve is small but its job is asymmetric. Ten percent that earns
4% sitting in T-bills is not drag; it is the option premium that
funds the next great rebalance trade.

---

**[SECTION 5 — BACKTEST — 12:00]**

**Stella:** Numbers. 1928 to 2024.

**Horace:** 100% equity earns 6.6% real, with a 75% drawdown in
1929-32 and four other 30%+ drawdowns. 60/40 earns 4.4% real with a
53% drawdown. The four-tranche book earns 3.7% real with a 38%
drawdown.

**Stella:** So all-weather costs 90 basis points of CAGR versus
60/40.

**Horace:** Yes. And buys you two things. Every decade — every
single decade since 1928 — finishes positive in real terms. And the
worst real drawdown is fifteen percentage points smaller. For
someone living off the portfolio, that trade is worth it. For a
30-year-old saving in an IRA, it is probably not — they should tilt
toward a barbell shape. More equity, smaller but
genuinely safe sleeve, larger opportunistic tail.

---

**[SECTION 6 — INTERACTIVE — 15:30]**

**Stella:** And the lab.

[VISUAL: course/interactive/week15_allweather_builder.html]

**Horace:** Four sliders, one for each tranche. The fourth is
read-only — it is whatever is left after the first three sum.
Drag growth up, you'll see the wealth curve climb but the drawdown
deepen. Drag income up, drawdown shrinks but Sharpe stays roughly the
same. Drag store-of-value up to 30%, you will see the stagflation
decade — 1973-1981 — completely change shape.

**Stella:** And the Sharpe.

**Horace:** Sharpe is roughly stable across most weight choices in
the realistic range. Which is the deepest lesson of multi-asset
construction. *Risk-adjusted return is more stable than absolute
return.* Whatever decision you make on the slider, you cannot screw
up Sharpe by very much. You can absolutely screw up max drawdown.
Pick the shape that lets you sleep, not the shape with the highest
CAGR.

---

**[OUTRO — 17:30]**

**Stella:** Next week — Week 16 — sectors. Eleven GICS cells. Where
inside the growth tranche the alpha actually lives.

**Horace:** And the homework: open the lab, find the weight that
gives you the smallest max drawdown. Then find the weight that gives
you the highest Sharpe. They are not the same. The gap between them
is your risk budget. That gap is the most important number in this
course.

**Stella:** See you next week.
