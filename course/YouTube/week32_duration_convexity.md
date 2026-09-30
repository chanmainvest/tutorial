## Part 2: YouTube Script

---

**VIDEO TITLE:** Duration & Convexity — Why Your "Safe" 30-Year Treasury Lost a Third of Its Value
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00-1:30]**

**Stella:** Last week we read the yield curve. The week before we
priced bonds. Today, we answer the question every bond holder asked
in 2022 and never had a good answer to: *how much* will I lose if
rates rise 1%?

**Horace:** And the answer is not "it depends." It's two numbers,
calculated from a contract you already understand. Duration. And
convexity. By the end of this lesson you will know why TLT lost a
third of its value in 2022, why that loss was completely
predictable from numbers published in the prospectus, and why
"Treasuries are safe" is one of the most expensive sentences in
modern finance.

**Stella:** The vol tail wags the dog, and it wrote this episode.
A 40-year trend in falling yields convinced an entire generation
that long Treasuries were a free safety. The math says otherwise.

---

**[SECTION 1 — Macaulay Duration — 1:30-4:30]**

**Horace:** Macaulay duration. 1938. Frederick Macaulay asked: when
do I really get my money back from a bond?

**Stella:** Not the maturity date.

**Horace:** Not the maturity date. The *cash-flow-weighted average
date*. If a 10-year bond pays a coupon every six months, half my
money arrives long before year ten. The weighted average comes back
shorter. Roughly eight years for a 5% coupon.

**[VISUAL: image/week32_duration_curve.png]**

**Stella:** Three lines on the chart. The 45-degree line is
zero-coupon — duration equals maturity, exactly. The other two
sag below — 5% coupon and 10% coupon. The higher the coupon, the
more cash arrives early, the shorter the duration.

**Horace:** A 30-year zero — STRIPS — has duration 30. A 30-year
5%-coupon Treasury has duration around 15. They are *not* the same
instrument. They are not in the same risk neighbourhood.

**Stella:** This is the first mistake people make. They think
"30-year bond" means "30-year duration." It doesn't. Unless you've
stripped the coupons.

---

**[SECTION 2 — Modified Duration — 4:30-7:30]**

**Horace:** Macaulay is years. Useful for talking to humans. Useless
for predicting P&L. For P&L we need *modified* duration.

**Stella:** Modified duration is just Macaulay divided by one plus
yield-over-frequency. The reason for that divisor is calculus. The
reason it matters is this single formula: percent price change is
approximately *minus modified duration times the yield change*.

**Horace:** Three numbers worth memorising. Two-year T-note,
modified duration about 1.9. Ten-year, about 8.1. Thirty-year,
about 17.

**Stella:** Same yield curve. Same credit. Three completely
different risk exposures.

**Horace:** This is why "I own Treasuries" is not a risk statement.
It's a *credit* statement. The price risk is hidden inside the
maturity choice.

---

**[SECTION 3 — Effective Duration — 7:30-9:30]**

**Stella:** Modified duration assumes the cash flows don't move.
That's true for a Treasury. It's *false* for a mortgage-backed
security.

**Horace:** When rates fall, homeowners refinance. Your MBS gets
called early. When rates rise, nobody refinances, and your MBS
extends — you're stuck with low coupons longer.

**Stella:** That asymmetry is *negative convexity*. To measure it
properly we use *effective* duration — shock the curve, reprice the
bond, take the slope numerically. For Treasuries it equals modified
duration. For MBS it doesn't.

**Horace:** The Fed's QT in 2022 hammered MBS portfolios because
their effective duration *extended* into the hike. A 7-year MBS
became, behaviourally, a 12-year MBS at exactly the wrong moment.

---

**[SECTION 4 — Convexity — 9:30-13:00]**

**Horace:** Now the curvature term. Duration is a tangent line. The
price-yield curve is a curve. The gap between them is convexity.

**[VISUAL: image/week32_convexity_payoff.png]**

**Stella:** Three lines. The blue is the true price-yield curve. The
dashed orange is the linear duration prediction. The green is
duration-plus-convexity — the quadratic.

**Horace:** Inside plus or minus 100 bps, the dashed line is fine.
Beyond that, convexity matters. By 300 bps the linear prediction is
off by several percent.

**Stella:** And notice the asymmetry. A 100 bps rally gives you
*more* price upside than a 100 bps sell-off costs you. That's
positive convexity. It's a free option in the bondholder's favour.

**Horace:** Free in the math sense. The market knows it's there, so
long-bond yields embed a small discount for it. You pay for the
convexity in lower carry.

**Stella:** And the formula? Percent price change is minus modified
duration times delta-y, plus one half times convexity times delta-y
squared. The squared term is the curvature.

---

**[SECTION 5 — 2022 TLT Case Study — 13:00-15:30]**

**Horace:** Let's do the 2022 trade.

**Stella:** TLT. iShares 20-plus-year Treasury. Modified duration
around 17. Convexity around 350.

**Horace:** Thirty-year yield rose from about 1.9% to about 4.0%.
Move: 210 basis points.

**Stella:** Linear prediction: minus 17 times 0.021. Equals minus
35.7%.

**Horace:** Convexity correction: half times 350 times 0.021
squared. Equals plus 7.7%.

**Stella:** Net: minus 28%.

**Horace:** TLT actually delivered minus 31% on price, plus about 2%
in coupons. Total return around minus 29%. The formula nailed it
within a percent.

**Stella:** And here's the part that matters. The math worked. The
bonds did *exactly* what their published duration said they would
do. The investors who got blindsided didn't read the duration. They
read "Treasuries are safe."

**Horace:** A 40-year trend wags the dog. The
duration was right there in the prospectus.

**Stella:** And the deeper reason it hurt so much?

**Horace:** They were sitting inside the "diversified core" — the
bond half of 60/40, the long sleeve of a target-date fund — *as the
hedge against equities*. When they correlated and fell together in
2022, the diversified core was revealed as its own concentrated bet
on a 40-year disinflationary regime. In my own shape now, the safety
end of the barbell is short-duration cash and bills plus gold. Long
Treasuries, if I hold them at all, sit on the asymmetric end as a
specific rates trade — never as the portfolio's pillow.

---

**[SECTION 6 — Key-Rate Durations — 15:30-16:30]**

**Stella:** One more concept and we're done. Single-number duration
assumes the curve moves in parallel. It almost never does.

**Horace:** Twists. Flatteners. Steepeners. The 2022 hike was a
bear flattener — short rates up faster than long. The 2024 cut
cycle was a bull steepener — long rates down faster than short.

**Stella:** Professionals decompose duration into key-rate buckets:
2Y, 5Y, 10Y, 30Y. They hedge each bucket with the appropriate
futures contract — TU, FV, TY, US.

**Horace:** Retail investors don't need to do this. But you need to
know that a single-number duration is hiding several dimensions of
curve risk.

---

**[INTERACTIVE WALKTHROUGH — 16:30-17:30]**

**[VISUAL: interactive/week32_duration_lab.html]**

**Stella:** Now play with it. Slide maturity from 1 to 30. Watch
duration grow — and watch how zeros (coupon = 0) sit on the
y=maturity line, while coupon bonds sag below.

**Horace:** Slide the rate shock. Watch three price predictions
diverge — exact, linear duration only, and duration plus convexity.
Inside plus or minus 200 basis points, the convexity-corrected line
hugs the exact line. Beyond that, both approximations break down
and you should reprice from cash flows directly.

**Stella:** Slide coupon up. Duration shrinks. Slide yield up.
Modified duration shrinks. The number on your prospectus is a
snapshot — it moves with rates.

---

**[OUTRO — 17:30-18:00]**

**Horace:** Three numbers. Macaulay tells you when you really get
your money back. Modified tells you the slope. Convexity tells you
the curvature. With those three you can predict any small bond
move within a percent of NAV.

**Stella:** And next week, Week 33, we put credit on top of duration
— how spreads behave, when they widen, and why "investment grade"
is not a synonym for "safe."

**Horace:** Until then — go look up the duration of every bond fund
you own. Write it on the wall. That number is your risk.

---

**[END]**
