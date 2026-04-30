# Week 31: Yield Curves — Shape, Level, Slope, Curvature

---

## Part 1: Reading Section

---

### 1. Why This Is Important

The yield curve is the single chart that, more than any other, tells
you what the bond market thinks. It is the price of money for every
maturity from one day to thirty years, drawn as a line. Its level
prices every mortgage and every corporate bond. Its slope prices every
recession probability the market is willing to bet on. Its curvature
prices the path of Fed policy. About 95% of all the variance in
how the curve moves can be summarised in three numbers.

You need to read this chart for four reasons.

1. **The curve is the foundation of every other rate.** Mortgages
   sit a couple of points above the 10-year. Investment-grade
   corporate bonds sit one to two points above the matched-maturity
   Treasury. High-yield credit sits four to six points above. If
   you understand the Treasury curve, you understand the price of
   credit risk in the entire economy because every other yield is
   a *spread* over it.
2. **Inversions have predicted every US recession since 1970.** Not
   most of them — every single one. The 2y/10y spread inverted in
   July 2022, stayed inverted for over two years, and uninverted
   in late 2024. By the textbook playbook a recession should have
   followed within 6 to 24 months. Whether or not it did, an
   investor who could *read* this chart in 2022 had cleaner hands
   than one who could not.
3. **Three factors explain almost all curve movement.** Principal
   component analysis on Treasury yields decomposes the curve into
   level (parallel shifts, ~70% of variance), slope (steepening or
   flattening, ~20%), and curvature (the belly versus the wings,
   ~5%). Every interest-rate trade you will ever see — duration
   bets, steepeners, butterflies — maps cleanly onto these three
   factors.
4. **Forwards are the market's *expected* future spot rates.** The
   forward rate two years out is what the curve is pricing for the
   short rate two years from today. If you have a different view,
   you have a tradeable view. If you have the same view, you do
   not. Reading forwards turns the curve into a probability
   distribution over future Fed policy.

This lesson covers construction (par/spot/forward), the three PCA
factors, the regime taxonomy (bull-flattener/bear-steepener and the
two "wrong" cousins), butterfly trades on curvature, and the April
2026 curve in context.

---

### 2. What You Need to Know

#### 2.1 What the Curve Is, Exactly

A yield curve is a graph of yield versus maturity for a set of bonds
of equivalent credit quality. The Treasury curve is the canonical
example because the credit risk is constant (zero, by US convention)
and the only thing varying is time-to-maturity.

The five tenors that get watched are 3-month, 2-year, 5-year, 10-year,
and 30-year. Their FRED ticker family is `DGS3MO`, `DGS2`, `DGS5`,
`DGS10`, `DGS30`. The 3-month sits closest to the Fed funds rate. The
2-year reflects expected Fed policy over the next two years. The 10-
and 30-year embed everything from inflation expectations to term
premium to global savings flow.

![Current US Treasury curve as of April 2026 plotted alongside the curves from June 2007 (pre-GFC, near-flat), April 2020 (post-COVID, pinned at zero), and July 2023 (peak inversion in the modern era). The April 2026 curve has uninverted and is gently upward sloping — the textbook normal shape, after three years of unusual inversion.](image/week31_curve_today.png)

Read the chart left to right. The 2007 curve is nearly flat — that
flatness was the warning bell before the GFC. The 2020 curve is pinned
near zero across the front because the Fed hit the lower bound. The
2023 curve is *inverted*: the 3-month is above the 10-year by more
than 150 basis points, the deepest inversion since Volcker. The
April 2026 curve is back to a normal upward shape — a regime change
that itself is the story this week.

#### 2.2 Par, Spot, and Forward — Three Rates from the Same Bond

When a financial paper says "the 10-year yield is 4.0%," it almost
always means the *par yield* — the coupon a 10-year Treasury would
need to pay to be priced exactly at 100. Par is the quoted rate.

The *spot rate* (or zero-coupon rate) is the yield on a bond that
pays nothing until maturity, then pays back principal. Spots are
the building blocks: every coupon bond is a portfolio of zero-coupon
strips at different maturities.

The *forward rate* is the implied future spot. If today's 1-year
spot is $r_1$ and today's 2-year spot is $r_2$, then the 1-year
forward 1-year-out, $f_{1,2}$, is the rate that satisfies:

$$ (1 + r_2)^2 = (1 + r_1) \cdot (1 + f_{1,2}) $$

Solving:

$$ f_{1,2} = \frac{(1+r_2)^2}{1+r_1} - 1 $$

**This is not a forecast — it is a no-arbitrage identity.** If the
forward rate were any different from this, you could borrow and lend
across maturities to extract a riskless profit. Markets price this
identity to within a basis point in every developed-market sovereign
bond market on earth.

The interpretation, however, *is* economic. The forward rate
embodies the rate the market expects (plus a term premium). A flat
curve says the market expects roughly today's short rate to persist.
An upward-sloping curve says the market expects the short rate to
*rise*. An inverted curve says the market expects the short rate to
*fall*. That last case is, mechanically, what an inversion is: a
collective bet on Fed cuts.

#### 2.3 The Three PCA Factors — Level, Slope, Curvature

In 1991 Robert Litterman and José Scheinkman published a working paper
at Goldman Sachs that decomposed Treasury curve movements via principal
component analysis. They found three factors:

| Factor | Loosely | % of curve variance | What moves it |
|---|---|---:|---|
| Level | All yields up or down together | ~70% | Inflation expectations, term premium |
| Slope | Long end versus short end | ~20% | Fed policy expectations, growth |
| Curvature | Belly versus wings | ~5% | Convexity demand, hedging flow |

Together the three factors explain about 95% of all daily Treasury
yield variance. A duration trade is a level bet. A steepener or
flattener is a slope bet. A *butterfly* trade is a curvature bet.

The level factor is the boring one and also the largest. When the
Fed signals tighter, the whole curve shifts up by a roughly parallel
amount. When inflation prints cooler, the whole curve drops.

The slope factor is the *interesting* one because it is what predicts
recessions. When the curve flattens or inverts, it is the slope
factor going negative — the market saying the short rate has further
to fall than the long rate.

The curvature factor is the *trader's* one. Pension funds and
insurance companies buy long-dated bonds for convexity matching;
butterfly trades exploit the relative cheapness or richness of the
belly versus the wings. We come back to this in §2.6.

#### 2.4 The Four Curve Regimes — Bull/Bear × Steepener/Flattener

Slope movements decompose into four regimes by *which end is moving
more* and *in which direction*:

| Regime | What happens | Macro driver | Asset playbook |
|---|---|---|---|
| **Bull steepener** | Short rates fall faster than long rates → curve steepens, both ends drop | Fed cutting into a slowdown | Long bonds rally, equities mixed; lengthen duration |
| **Bull flattener** | Long rates fall faster than short → curve flattens, both ends drop | Recession fear, flight to quality | Long bonds rally most; flight-to-quality |
| **Bear steepener** | Long rates rise faster than short → curve steepens, both ends climb | Reflation, rising inflation expectations | Short duration, value/cyclical stocks, commodities |
| **Bear flattener** | Short rates rise faster than long → curve flattens or inverts | Fed hiking faster than the long end believes | Cash beats bonds, growth stocks penalised |

The 2022-23 cycle was a textbook *bear flattener* turning into an
*inversion*. The Fed hiked from 0.25% to 5.50% while the 10-year
went from 1.5% to 4.0%. Short rates moved 5 points; long rates
moved 2.5 points; the curve inverted by 100 basis points. Then in
2024-25 the Fed cut, the short end fell faster, and the curve
*bull-steepened* back to normal.

![10-year minus 2-year US Treasury spread, 1976 through April 2026, FRED series T10Y2Y. Annotated regions mark the major regimes: the 1980s Volcker bear-flattener, the 1989 / 2000 / 2006 / 2019 / 2022 inversions, and the 2008-09 / 2020 / 2024-25 bull-steepening unwinds.](image/week31_slope_history.png)

The honest reading of this chart: every single dip below zero has been
followed, within 6 to 24 months, by a recession dated by the NBER
Business Cycle Dating Committee. The 2022 inversion is the longest
on the chart. As of April 2026 the spread has uninverted but only
just — the curve is still flatter than its long-run average.

#### 2.5 Reading Today's Curve — April 2026

Pull up the chart at the top of §2.1. As of April 2026:

- **3-month:** ~3.5%, well below the cycle peak of 5.5%.
- **2-year:** ~3.6%, pricing roughly one more Fed cut over the next
  two years.
- **5-year:** ~3.8%.
- **10-year:** ~4.0%.
- **30-year:** ~4.3%.

The 10y-2y spread is back to roughly +40 basis points after spending
two years deeply negative. The 10y-3m spread is back to slightly
positive. The curve has *fully uninverted* but it is not yet *steep*
in the historical sense — the long-run median 10y-2y spread is
roughly +95 basis points.

The forward curve embedded in these spots is gently rising — the
market is pricing the short rate to drift roughly back to today's
10-year over the next decade, suggesting the market believes neutral
real rates have repriced higher than the 2010-2020 norm. This matters
for every long-duration asset, including equities. SOUL #2 — the
40-year bond bull regime ended in 2022 — gets a quiet confirmation
on this chart.

#### 2.6 Butterfly Trades — Trading Curvature

A butterfly is a market-neutral trade against the *curvature* of the
curve. The classic structure is long the belly, short the wings,
weighted to be duration-neutral. For example: long $50M of 5-year
Treasuries; short $25M of 2-year and $25M of 30-year, weighted by
DV01 so the position has zero net duration.

If the belly is *cheap* relative to the wings, the trade earns when
the curvature mean-reverts. If the belly is *rich*, the inverse
butterfly profits.

Pension funds and insurers create persistent *richness* at the long
end (they need 30-year duration) and at the very short end (they
park cash there). The belly tends to be relatively *cheap* in normal
times. Trader convention quotes the butterfly as
$2 \cdot y_{\text{belly}} - y_{\text{short}} - y_{\text{long}}$,
which equals zero when the curve is perfectly straight, positive
when the belly is cheap (high yield), and negative when the belly is
rich.

This is one of the five alpha sources from SOUL #5 — relative-value
fixed income. It is not retail-friendly because the gross notional
involved is large and the carry is small. But it lives on the same
chart you have been staring at all week, and the interactive panel
below lets you compute the butterfly statistic from any curve you
draw.

#### 2.7 The Practical Toolkit — Which Number Matters Most

For a retail investor reading the curve once a month, the priority
order is:

1. **Level of the 10-year.** Sets the discount rate for every long-
   duration asset on earth. Through Week 5 and Week 21 we already
   know stocks compete with bonds — the 10-year is the bond.
2. **10y-2y or 10y-3m spread.** Recession indicator and slope
   factor in one. Inverted = late-cycle warning.
3. **Forward 1-year, 1-year-out.** Where the market thinks the
   short rate goes next year. Compare against the Fed dot plot
   for a quick consensus check.
4. **Curvature.** Optional. Useful if you trade fixed income
   actively; ignorable for buy-and-hold.

The interactive at the bottom of this lesson lets you slide all five
tenors and watch the slope, curvature, and 1y1y forward update live.
Hit the preset for "1981" and see what 16% rates with a deeply
inverted curve look like. Hit "2020" and see the zero-bound. Hit
"today" and see April 2026.

---

### 3. Common Misconceptions

**1. "An inversion *causes* a recession."**
   It does not. The inversion is the market's *prediction* of a
   recession, expressed through forwards. The causation runs the
   other way: late-cycle conditions cause the Fed to be tight, which
   pushes the short end up while long-rate inflation expectations
   anchor or fall. Inversion is a symptom, not the disease.

**2. "The yield curve is always upward-sloping in normal times."**
   Often, but not always. About 80% of post-1976 monthly observations
   show 10y > 2y. The other 20% include genuine normal flat periods
   as well as inversions. Calling the curve "broken" because it is
   not steep is reading the median as the law.

**3. "Long bonds are safer than short bonds."**
   Lower default risk on US Treasuries is the same at every maturity.
   Long bonds have *more* interest-rate risk because their duration
   is higher. A 30-year zero loses ~30% on a one-percentage-point
   yield rise; a 2-year loses ~2%. Long bonds are more *volatile*,
   not safer. SOUL #6: vol tail wags the dog.

**4. "Forwards are forecasts."**
   Forwards are no-arbitrage identities derived from spots. They
   *embody* the market's expected path plus a term premium. They
   are not anyone's forecast in particular, and the market's
   expectation is wrong much of the time — see Eugene Fama's 1984
   work showing forward rates are biased estimators of future spots.

**5. "If I think rates are going down, buy long bonds."**
   Often correct, but the magnitude depends on whether the *whole
   curve* shifts down (level) or just the long end (bull flattener).
   A bull steepener — short end falls faster — does not benefit
   long-duration positions much. Decompose the trade you want into
   level, slope, and curvature before sizing.

**6. "The Fed controls the yield curve."**
   The Fed controls the very front (overnight rate, and via quantitative
   easing the long end somewhat). The middle and long end are set
   by global savings flow, term premium, and inflation expectations.
   In 2022-23 the Fed hiked 5 percentage points; the 10-year moved
   only 2.5. The market does not always follow.

**7. "All inversions are alike."**
   They are not. The 1980 inversion under Volcker was caused by the
   short rate being driven to 19%. The 2006-07 inversion was a
   gentler 50bp inversion driven by housing optimism on the long
   end. The 2022-23 inversion was a 150bp post-COVID bear flattener.
   Same shape; very different macro story each time.

**8. "Butterfly trades are for retail investors."**
   They are not. Carry is small, gross notional is large, and the
   position has to be DV01-balanced and hedged. This is an
   institutional or hedge-fund activity. Retail can express the
   *direction* of the curvature view by overweighting or
   underweighting the 5-year sleeve of a bond ladder.

**9. "Real yields don't matter for the curve."**
   They are most of the long-end story. Decompose nominal = real +
   breakeven inflation. The 10-year real yield (TIPS, FRED `DFII10`)
   moved from -1.0% in 2021 to +2.0% in 2024. Two thirds of the
   2022-23 long-rate rise was a real-rate move, not an inflation-
   expectation move. SOUL #2 again.

**10. "Once I read the curve, I can time the market."**
   You can read the curve. You can position duration. You can
   probability-weight an equity drawdown. You cannot time the
   market with the curve as your only signal. The 2022 inversion
   was followed by an 18-month *equity rally* before any meaningful
   correction. Signals are probabilistic; sizing matters more than
   conviction.

---

### 4. Q&A

**Q1: How do I actually read a yield curve plot for the first time?**

A: Three glances. (a) Look at the level — where is the 10-year? Above
4% is meaningfully restrictive territory in modern terms; below 2% is
extraordinarily loose. (b) Look at the slope — is the right end higher
than the left? Upward = normal. Flat or down = late-cycle. (c) Look
at the belly — is the 5-year sitting on a straight line between the
2-year and the 30-year, or is it bowed? Bowed up = market pricing rate
cuts through the medium term; bowed down = sudden tightening expected.

**Q2: What is the difference between the 10y-2y and the 10y-3m spreads?**

A: Both are slope measures. The 10y-2y is more popular among traders
because the 2-year integrates Fed expectations over a longer window.
The 10y-3m is the academic favourite (Estrella and Mishkin, 1996,
showed it is the strongest single recession predictor). In practice
they invert and uninvert at slightly different times; the 10y-3m
typically inverts later but is regarded as a more reliable signal.

**Q3: Why does the curve invert before recessions?**

A: Late-cycle Fed tightening drives the short end up. Long-end
inflation expectations are *forward-looking* — if traders believe the
hiking will eventually slow growth and inflation, the long end stays
anchored or falls. The result: short above long. The market is
saying "the Fed is too tight; cuts are coming." When those cuts
arrive, they typically arrive into a slowing economy. So the
inversion is the market pricing the rate cuts that the recession
will bring.

**Q4: Can I trade the yield curve as a retail investor?**

A: Yes, with limits. The cleanest tools: SHV (1-3 month T-bills, ~0
duration), IEF (7-10 year, ~8 duration), TLT (20+ year, ~17 duration).
A long IEF / short SHV trade is a long-duration / curve level bet. A
long TLT / short IEF is a long-end *steepening* bet against the
belly. Margin and futures (UB and TY contracts) give cleaner
expressions but require more capital and more risk management.
Butterfly trades are not really doable retail.

**Q5: How does the curve relate to mortgage rates?**

A: 30-year mortgage rates track the 10-year Treasury plus a 1.5–2.5%
spread (the "MBS basis"). When the 10-year rises 100bp, mortgages
typically rise about 100bp. When the curve inverts, banks' net interest
margin compresses, lending tightens, and mortgage spreads sometimes
widen further. The full chain — Fed → 10-year → mortgage → housing —
is the topic of Week 18.

**Q6: What is the "term premium" and why does it matter?**

A: The term premium is the extra yield long bonds pay above the
expected average of future short rates, to compensate investors for
locking up money. Estimates vary, but the New York Fed's ACM model
puts the 10-year term premium near 0% in 2020, rising to ~80bp by
2025. A higher term premium steepens the curve without any change
in expected Fed policy. Some of the post-2022 long-end rise is term
premium repricing, not inflation expectations.

**Q7: Why was the 2022-24 inversion so unusually long?**

A: Two reasons. (1) Inflation was the most persistent in 40 years,
so the Fed had to hold restrictive policy longer than any prior
post-1990 cycle. (2) The economy did not slow sharply enough to
force cuts — fiscal stimulus and onshoring kept demand robust. The
market kept pricing cuts in the forwards; the Fed kept not cutting;
and the inversion persisted. By the time uninversion arrived in
late 2024, the inversion had lasted ~26 months — the longest since
records began.

**Q8: What does a steep curve mean for stocks?**

A: A *bull steepener* (Fed cutting, short end falling) is typically
good for equities because the discount rate is dropping. A *bear
steepener* (long end rising on growth or inflation) is mixed: cyclical
and value sectors benefit; long-duration growth stocks suffer because
their cash flows are far in the future and a higher discount rate
hits them hardest. Reading the *type* of steepening matters more
than the steepening itself.

**Q9: Are forward rates the same as Fed dot-plot expectations?**

A: Usually similar, sometimes very different. The Fed's own forecast
is published quarterly in the Summary of Economic Projections (the
"dot plot"). Market forwards are continuous and unbiased of any
individual member's forecast. Through 2022-23 the market consistently
priced cuts that the Fed dot-plot had not yet endorsed; the market
turned out to be early. The gap between forwards and the dot-plot
is one of the more reliable contrarian signals — pay attention when
they diverge.

**Q10: How does this connect to the rest of the course?**

A: Week 5 introduced bonds; Week 18 traced the rate cascade through
mortgages and credit; Week 10 used the inversion as a regime
indicator; Week 23 discussed factor decay including the term factor;
Week 32 covers duration and convexity (the math of how curve
movements turn into bond returns). The yield curve is the spinal
column the entire fixed-income half of this course is built on.
After this week you should be able to read a Bloomberg yield curve
panel as fluently as you read a price chart of SPY.

The interactive below lets you draw your own curve. Drag the five
sliders. Watch the slope, the curvature, and the implied 1y1y
forward update. Hit the presets to see history. Decide which world
you think we are heading back to.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Yield Curves — Shape, Slope, Curvature, and What Each Tells You | Week 31

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO]**

**Horace:** This week, the most informative single chart in the bond
market. The yield curve. What it is, what makes it move, and what
its shape tells you about every other asset class in the world.

**Stella:** This is the chart that predicted every recession since
1970, right?

**Horace:** Right. And by the end of today you'll be able to read
it in three glances — level, slope, curvature.

---

**[SEGMENT 1: WHAT THE CURVE IS]**

[VISUAL: image/week31_curve_today.png]

**Horace:** The yield curve plots yield versus maturity for the same
borrower — for us, the US Treasury. Five tenors carry most of the
information: 3-month, 2-year, 5-year, 10-year, 30-year. We have four
curves on the screen: April 2026 in heavy blue. Pre-GFC June 2007
in grey. Post-COVID April 2020 in green, pinned at zero. And July
2023 in red — the deepest inversion since Volcker.

**Stella:** What's the story?

**Horace:** Three regime changes in 19 years. 2007 — flat as a
table, the warning bell before the GFC. 2020 — the Fed at zero
across the front. 2023 — fully inverted, 150 basis points, the
market screaming "you're too tight." 2026 — uninverted, mildly
upward-sloping, the new normal.

---

**[SEGMENT 2: THREE TYPES OF RATE]**

**Horace:** Before we talk shape, three vocabulary items. Par yield —
what most papers quote, the coupon a bond would need to pay to be
priced at 100. Spot rate — the yield on a zero-coupon bond, no
intermediate payments. Forward rate — the implied rate the market
is pricing for some future period.

**Stella:** And the forward is calculated from the spot?

**Horace:** No-arbitrage identity. If today's 1-year is 3.5% and
today's 2-year is 3.8%, then the 1-year-rate-1-year-from-now must
be the rate $f$ such that $1.038^2 = 1.035 \times (1 + f)$. Solve,
$f$ equals about 4.1%. The market is pricing the 1-year rate to
*rise* from 3.5 to 4.1 next year. That is information.

**Stella:** And it's not a forecast?

**Horace:** It's an *implied* forecast. The market's collective bet,
plus a term premium. Eugene Fama showed in 1984 that forwards are
biased estimators of future spots — they tend to over-predict the
rate move. But they price every fixed-income instrument on earth.
Real money trades on them.

---

**[SEGMENT 3: THE THREE PCA FACTORS]**

**Horace:** Litterman and Scheinkman, 1991, Goldman Sachs working
paper. Take 30 years of Treasury yield data, run principal component
analysis, see what comes out. Three factors. Level — yields up or
down together — about 70% of variance. Slope — long versus short
— about 20%. Curvature — belly versus wings — about 5%. Together,
95% of all daily curve movement.

**Stella:** So three numbers describe almost everything.

**Horace:** Right. Every duration trade is a level bet. Every
steepener or flattener is a slope bet. Every butterfly is a
curvature bet. If you can't decompose your trade into those three,
you don't know what you own.

---

**[SEGMENT 4: BULL/BEAR × STEEPENER/FLATTENER]**

**Horace:** Slope movements come in four flavours.

Bull steepener: short rates falling faster than long. Fed cutting
into a slowdown. Long bonds rally hard, equities mixed. Lengthen
duration here.

Bull flattener: long rates falling faster than short. Recession fear,
flight to quality. Long bonds rally most.

Bear steepener: long rates rising faster than short. Reflation, rising
inflation expectations. Short duration; value and cyclicals win.

Bear flattener: short rates rising faster than long. Fed hiking
faster than the long end believes. Cash beats bonds. Growth
stocks penalised.

**Stella:** And 2022 was…

**Horace:** Textbook bear flattener turning into inversion. Fed went
from 0.25% to 5.50% — five points. The 10-year went from 1.5% to
4.0% — two and a half points. Curve inverted by a full point.

---

**[SEGMENT 5: THE SLOPE HISTORY CHART]**

[VISUAL: image/week31_slope_history.png]

**Horace:** Fifty years of the 10y-2y spread. Every dip below zero
on this chart was followed within 6 to 24 months by a recession.
1980 — Volcker. 1989. 2000 — dotcom. 2006 — pre-GFC. 2019. 2022 —
the longest one in the data, lasted into late 2024.

**Stella:** And April 2026?

**Horace:** Spread is back to about plus 40 basis points. Uninverted,
but flatter than the long-run median of plus 95. We are in the
post-uninversion phase, which historically is *also* the phase
where recessions tend to land.

---

**[SEGMENT 6: TODAY'S CURVE]**

**Horace:** April 2026 numbers, give or take a few basis points.
3-month at 3.5%. 2-year 3.6%. 5-year 3.8%. 10-year 4.0%. 30-year
4.3%. The forward 1-year 1-year-out is around 3.7% — the market is
pricing roughly one more Fed cut over the next two years and then a
flat path.

**Stella:** Term premium?

**Horace:** New York Fed's ACM model has the 10-year term premium
near 80 basis points as of late 2025, up from roughly zero in 2020.
That repricing is real and is part of the story. SOUL number two —
the 40-year bond bull market ended in 2022 — gets a quiet
confirmation here. Real yields at +2% are the new normal.

---

**[SEGMENT 7: CURVATURE AND BUTTERFLIES]**

**Horace:** The curvature factor. Long the belly, short the wings,
duration-balanced. If the 5-year is *cheap* relative to the 2 and
the 30, the trade earns when curvature mean-reverts. Pension funds
and insurers create persistent richness at the wings — they need 30-
year duration; they park cash short — and the belly tends to be
relatively cheap as a result.

**Stella:** Retail-friendly?

**Horace:** Not really. Gross notional is large, carry is small,
DV01-matching is fiddly. This is an institutional alpha source —
SOUL number five, alpha source three, relative-value fixed income.
Retail can express the *direction* of the curvature view by tilting
their bond ladder toward or away from the 5-year sleeve.

---

**[SEGMENT 8: THE INTERACTIVE]**

**Horace:** The interactive panel below the lesson lets you drag five
sliders — 3-month, 2-year, 5-year, 10-year, 30-year. The plot
re-renders. Three numbers update: slope (10 minus 2), curvature (2
times the 5 minus 2 minus 30), and the implied 1y1y forward. Hit
the preset for 1981 and see Volcker's 16% inverted curve. Hit
"2020" for the zero-bound. Hit "today" for April 2026.

**Stella:** What's the homework?

**Horace:** Slide today's curve. Then drag the 10-year up by 100
basis points, like a 1970s-style inflation shock. Watch the slope
flatten and the curvature go negative. That is the trade you
want to be on the *right side* of, and reading this chart is how
you tell.

---

**[OUTRO]**

**Horace:** The yield curve. Three numbers tell you almost everything
— level, slope, curvature. Inversions don't cause recessions; they
predict them. Forwards aren't forecasts; they are no-arbitrage
identities that happen to embody the market's expected path. And
the curve is the spinal column of fixed income. Next week we map
those movements onto bond *returns* — duration and convexity.

**Stella:** End screen?

**Horace:** Slide the interactive. Then we'll see you next week.

---

**END SCREEN:** "Next: Week 32 — Duration and Convexity"
