# Week 32: Duration and Convexity — Bond Price Sensitivity Beyond Macaulay

---

## Part 1: Reading Section

---

### 1. Why This Is Important

In Week 5 you learned that a bond is four numbers and a calendar, and
that price is just discounted cash flow. In Week 18 you learned that
the discount rate is the universal denominator of finance. In Week 31
you learned to read the curve. This week you learn the verb that
connects those nouns: **how much**.

How much does my bond fund lose when the 10-year yield jumps 50 bps?
How much does my pension liability move when the curve flattens? How
much of a TLT drawdown is "normal" versus "regime change"? These are
not abstract questions. They are the daily P&L of every fixed-income
position on earth, and they are answered by two numbers — duration
and convexity — calculated from the bond contract you already know.

You need to internalise four things from this lesson.

1. **Duration is not "years until maturity."** It is the
   *cash-flow-weighted average time* until you get your money back,
   which equals the elasticity of price to yield. A 10-year coupon
   bond has a duration around 8, not 10. A 30-year zero-coupon bond
   has a duration of exactly 30. Confusing duration with maturity is
   the single most common mistake in fixed income, and it cost a
   generation of "10-year Treasury" buyers in 2022 the chance to
   measure their own risk before the move.
2. **Convexity is not a footnote — it is the entire long end.** For
   small yield moves, the linear duration approximation is fine. For
   large moves (the 2022 yields-tripling type of move), convexity
   adds back the curvature you've been ignoring. On a 30-year
   Treasury, ignoring convexity over a 300 bps move misstates the P&L
   by several percentage points. Convexity is also positive for
   straight bonds — a free asymmetry in the holder's favour, which
   gets paid for in lower yields on the long end.
3. **Key-rate duration is how professionals actually hedge.** The
   single-number "modified duration: 6.2 years" is a portfolio
   summary, not a hedging tool. Real fixed-income desks decompose
   duration along the curve — 2-year KRD, 5-year KRD, 10-year KRD,
   30-year KRD — and hedge each bucket separately because the curve
   does not move in parallel. Twists, flatteners, and steepeners are
   the daily reality.
4. **2022 was duration risk made visible — the vol tail wagging
   the dog.** TLT, the 20-year-plus Treasury ETF with a
   modified duration around 17, fell about 33% in 2022 — a worse
   calendar year than the S&P 500 in 2008. The bonds did exactly
   what their duration said they would do. The *investors* — many of
   whom thought "Treasuries are safe" — got blindsided because they
   never looked up their own duration. The 40-year tail of falling
   yields had wagged the entire risk-perception dog.

---

### 2. What You Need to Know

#### 2.1 Macaulay Duration — The Weighted Average Maturity

Frederick Macaulay defined duration in 1938 as the weighted average
time until a bond's cash flows arrive, where each weight is the
present value of that cash flow as a share of the bond's price:

$$ D_{\text{Mac}} \;=\; \frac{1}{P} \sum_{t=1}^{m N} \frac{t}{m} \cdot \frac{C_t}{(1+y/m)^{t}} $$

Three properties follow immediately from this formula.

- **A zero-coupon bond's Macaulay duration equals its maturity
  exactly.** With only one cash flow at time $N$, the weighted
  average has only one entry: $D_{\text{Mac}} = N$. A 30-year STRIPS
  has duration 30 by construction.
- **A coupon bond's duration is strictly less than its maturity.**
  The intermediate coupons pull the weighted average toward the
  present. A 30-year 5% coupon bond at par has Macaulay duration
  around 15.4 — about half the headline maturity number that names
  the bond.
- **Higher coupon -> lower duration.** More cash arrives early, so
  the weighted average shifts left. The Week 32 image
  `week32_duration_curve.png` shows three duration curves stacked
  inside the same maturity axis: the 45-degree line is zero-coupon,
  the 5%-coupon curve sags below it, and the 10%-coupon curve sags
  further still.

![Macaulay duration as a function of maturity for zero-coupon, 5%-coupon, and 10%-coupon bonds. The zero-coupon line is exactly the 45-degree y=x line; the coupon-bond curves bend below it, plateauing as maturity grows. At 30 years, a 5% coupon bond has duration about 15.4, not 30.](image/week32_duration_curve.png)

Macaulay's units are years. That's the only number you can describe
to a non-quant friend without losing them in calculus. But for
hedging P&L, we want a different unit: percent price change per
percent yield change. That is modified duration.

#### 2.2 Modified Duration — Price Sensitivity in Percent

Modified duration is Macaulay duration divided by one period of
yield compounding:

$$ D_{\text{mod}} \;=\; \frac{D_{\text{Mac}}}{1 + y/m} $$

Why this divisor? Because it converts "weighted average time" into
the linear price-yield slope:

$$ \frac{\Delta P}{P} \;\approx\; -\,D_{\text{mod}} \cdot \Delta y $$

Read it out loud: *for a small yield move $\Delta y$, the percentage
price change is about minus modified duration times the yield move.*
A 10-year Treasury at 4% with $D_{\text{mod}} = 8.1$ years loses
about 8.1% of its price for each 1% rise in yield, and gains 8.1%
for each 1% fall. The minus sign is the inverse price-yield
relationship from Week 5, now quantified.

Three working numbers worth memorising for April 2026:

- 2-year T-note, $D_{\text{mod}} \approx 1.9$. A 50 bps move moves
  price by ~1%.
- 10-year T-note, $D_{\text{mod}} \approx 8.1$. A 50 bps move moves
  price by ~4%.
- 30-year T-bond, $D_{\text{mod}} \approx 17.0$. A 50 bps move moves
  price by ~8.5%.

Same yield curve, three very different sensitivities. This is why
"I own Treasuries" is not a risk statement. The maturity matters.

#### 2.3 Effective Duration — When Cash Flows Aren't Fixed

Modified duration assumes the cash-flow schedule is fixed. That is
true for vanilla Treasuries and investment-grade corporates. It is
*false* for callable bonds, putable bonds, and the entire
mortgage-backed securities (MBS) universe, where the cash flows
themselves move with rates — homeowners refinance when rates fall,
extend when rates rise.

For these "rate-dependent cash flow" bonds, duration must be
measured numerically by shocking the curve up and down and
remeasuring price:

$$ D_{\text{eff}} \;=\; \frac{P_{-} \;-\; P_{+}}{2 \cdot P_0 \cdot \Delta y} $$

where $P_-$ is the price after a downward parallel shock of $\Delta
y$, $P_+$ is the price after an upward shock, and $P_0$ is today's
price. For a vanilla Treasury, effective duration matches modified
duration to several decimals. For a 30-year MBS, effective duration
is much shorter than modified duration when rates fall (the prepay
option kicks in) and much longer when rates rise (extension risk).
That asymmetric profile is **negative convexity**, and it is the
reason MBS portfolios behaved so badly in 2022 — they extended into
the rate hike instead of contracting away from it.

#### 2.4 Convexity — The Curvature Term

Duration is a tangent line. The price-yield curve is a curve. The
gap between them is convexity. Taylor-expand price as a function of
yield around the current yield $y_0$, keep two terms instead of one,
and divide by price:

$$ \frac{\Delta P}{P} \;\approx\; -\,D_{\text{mod}} \cdot \Delta y \;+\; \tfrac{1}{2} \cdot C \cdot (\Delta y)^{2} $$

with convexity defined as the second derivative scaled by price:

$$ C \;=\; \frac{1}{P} \cdot \frac{d^{2}P}{d y^{2}} $$

The image `week32_convexity_payoff.png` shows all three lines on top
of each other for a 30-year, 5%-coupon bond at 5% yield: the true
price-yield curve, the linear duration approximation, and the
duration + convexity quadratic. For a 100 bps move the duration
line is fine. For a 300 bps move (the 2022 type of move) the linear
approximation undershoots the gain on the rally side and overshoots
the loss on the sell-off side.

![Bond price as a function of yield for a 30-year, 5%-coupon bond. The blue curve is true price; the dashed orange line is the linear duration tangent; the green curve is the duration-plus-convexity quadratic. Convexity narrows the gap to zero for any move within roughly +/-150 bps. The asymmetry — gains exceed losses for symmetric yield shocks — is the convexity benefit a long-bond holder pays for in lower yield.](image/week32_convexity_payoff.png)

That asymmetry is the central feature: **for a straight bond,
convexity is always positive, and it always works in the holder's
favour**. A 100 bps rally produces a slightly bigger price gain than
a 100 bps sell-off produces in price loss. The market knows this,
which is why long-bond yields embed a small "convexity discount"
relative to where pure expectations would put them.

#### 2.5 Key-Rate Durations — The Curve Doesn't Move in Parallel

The single number $D_{\text{mod}} = 8$ assumes a parallel shift —
every point on the curve moves by the same amount. In reality the
curve twists. Short rates move on Fed policy. Long rates move on
inflation expectations and term premium. The 2022 sell-off was a
bear flattener (short rates up faster than long); the 2024 rally
was a bull steepener (long rates down faster than short). Neither
is parallel.

Key-rate duration (KRD) decomposes total duration into the
contribution from each maturity bucket. Standard buckets are 3M,
2Y, 5Y, 10Y, 30Y. For a 10-year bullet Treasury, almost all of the
duration sits in the 10Y bucket. For a 30-year MBS, duration is
spread across 5Y, 10Y, and 30Y buckets because the prepay option
makes the effective cash flow date sensitive to multiple parts of
the curve. A bond fund manager hedging a portfolio doesn't short
"Treasury duration" — they short specific futures contracts (TU at
2Y, FV at 5Y, TY at 10Y, US at 30Y) sized by KRD bucket. That is
how professionals actually run a duration-neutral book.

For the retail investor: don't memorise KRDs. Just know that when
your bond ETF prospectus reports a single duration number, it has
already collapsed five-or-more dimensions into one, and that
collapse is wrong by several percent of NAV in any non-parallel
move. If you own a barbell (Week 31's barbell strategy), your KRD
profile is fundamentally different from a bullet of the same total
duration.

#### 2.6 The 2022 TLT Drawdown — Duration Risk Made Visible

iShares 20+ Year Treasury Bond ETF (TLT) is the canonical long-bond
proxy. Its modified duration sits around 17 years. In 2022 the
30-year Treasury yield rose from about 1.9% to about 4.0%, a move
of 210 bps. Linear duration predicts:

$$ \frac{\Delta P}{P} \;\approx\; -\,17 \cdot 0.0210 \;=\; -35.7\% $$

Convexity gives some back. With long-bond convexity around 350,
$\tfrac{1}{2}\cdot 350 \cdot (0.021)^2 = +7.7\%$. Net prediction:
about $-28\%$. TLT actually delivered roughly $-31\%$ on price plus
about $+2\%$ in coupons, for a total return near $-29\%$. The
formula nailed it within a percent.

Two things to take from this. First, the math worked — there was no
market dysfunction, no failure of the model. Second, the *people*
holding TLT did not do this calculation in advance. Many bought
"Treasuries" expecting safety in a Fed hiking cycle, never having
asked the question "what is my duration." The vol tail wagged the
dog: a regime that had run for 40 years made everyone
forget that long Treasuries can lose a third of their value in a
year. Duration is the antidote — but only if you actually compute
it before you buy.

**Horace's view — the 2022 failure was a portfolio-shape problem,
not a bond-math problem.** My own read on why long bonds did so much
damage that year is that they were sitting inside what most people
called the "diversified core" — the bond half of a 60/40, the
long-duration sleeve of a target-date fund, the "safe" allocation in
a balanced portfolio. The whole point of holding them there was that
they were supposed to *hedge* the equity drawdown. Instead they
correlated to it and *added* to it, because they were never genuine
safety to begin with — they were a leveraged duration bet that
worked for 40 years and then didn't. In the barbell shape I run now,
the safety end is short-duration cash and bills plus gold, *not*
long Treasuries. Long Treasuries, if I want them at all, sit on the
asymmetric end as a specific rates trade with a thesis behind it,
not as the portfolio's pillow. The diversified core had quietly
become its own concentration risk — a concentrated bet on the
40-year disinflationary regime — and 2022 was the year that
concentration printed.

#### 2.7 Putting Duration to Work — Three Practical Rules

1. **Match duration to your liability or your horizon.** If you need
   the money in 5 years, hold bonds with duration around 5. The
   reinvestment-rate risk and price risk cancel each other out
   roughly at the duration horizon — this is **immunisation**, the
   foundation of pension and insurance bond management.
2. **Use modified duration to size hedges, not to predict big
   moves.** For yield changes within +/-50 bps, linear duration is
   accurate enough. Beyond that, use the convexity-corrected
   quadratic. Beyond +/-200 bps, reprice the bond directly from cash
   flows — the approximation breaks down. The interactive lab below
   lets you watch all three predictions side by side as you slide
   the rate shock.
3. **Treat "duration of my bond fund" as a pinned-up number on the
   wall.** Open the prospectus, find effective duration, write it
   down. A 50 bps Fed surprise on Wednesday afternoon will cost you
   that number times one half percent. If that number scares you,
   shorten the fund. If not, you have the right ballpark for your
   fixed-income sleeve.

---

### 3. Common Misconceptions

1. **"Duration equals years to maturity."** Only true for zero-coupon
   bonds. Coupon bonds are always shorter-duration than their
   maturity.
2. **"Modified duration is in percent."** No — modified duration is
   in years (it's the semi-elasticity), and the *product* of
   $D_{\text{mod}}$ with $\Delta y$ (in decimal) gives the percent
   price change.
3. **"Convexity is a small correction; ignore it."** True for +/-50
   bps, dangerously false for +/-300 bps. The 2022 long-bond move
   would have been mispriced by 4-7 percentage points without
   convexity.
4. **"Negative convexity is bad."** Negative convexity earns the
   holder *more yield* in normal regimes — that's why MBS yield
   more than Treasuries. The "bad" only shows up in extreme moves.
   You're being paid for the option you wrote.
5. **"All Treasury bonds are equally safe."** They are equally
   *credit-safe*. Their *price-risk profiles are completely
   different* — a 2-year T-note and a 30-year T-bond are almost
   different asset classes from a duration standpoint.
6. **"Duration changes slowly."** It changes meaningfully with
   yields. As yields rise, modified duration falls (the bond's
   effective horizon shortens). The number on your prospectus is a
   snapshot, not a constant.
7. **"My bond fund's duration is the average of holdings'
   maturities."** No — it's the dollar-weighted average of holdings'
   modified durations, which is shorter than the maturity average
   for any coupon-paying portfolio.
8. **"Convexity is always positive."** True for vanilla bonds.
   False for callable corporates, MBS, and any bond where the
   issuer or the underlying borrower holds a prepay option.
9. **"I don't own bonds, so this doesn't apply."** Equity valuation
   is duration math too — a stock with cash flows growing forever
   has a much longer "equity duration" than a mature dividend payer,
   which is why high-multiple growth stocks crashed harder than
   value in 2022.
10. **"The yield curve will move parallel."** It almost never does.
    Twists, steepeners, flatteners, and bull/bear variants of each
    are the normal regime. Single-number duration only describes
    parallel-shock P&L.

---

### 4. Q&A Section

**Q1: Why divide Macaulay by $(1+y/m)$ to get modified duration?**
Macaulay is in time units (years). Modified is the elasticity of
price to yield — i.e., $-\frac{dP/dy}{P}$. A bit of calculus on the
present-value formula shows the algebraic relationship is exactly
$D_{\text{Mac}}/(1+y/m)$. You can also see it as a small
discrete-compounding correction: at $y=0$, Macaulay equals
modified; at higher yields they diverge.

**Q2: How do I find the duration of my bond ETF?**
Check the fund company's website. iShares, Vanguard, and
SPDR all publish "effective duration" prominently in fund
characteristics. Do not confuse it with "average maturity." For
TLT in April 2026, effective duration is around 16.7. For BND
(total-bond market), about 6.3. For SHV (1-3 month T-bills), about
0.1.

**Q3: Why do long bonds have positive convexity?**
The price-yield function $P(y)$ is a sum of $1/(1+y)^t$ terms. Each
term is convex in $y$ (positive second derivative), and the longer
the time $t$, the more convex. Long bonds amplify this curvature.
Mathematically, convexity scales roughly with the *square* of
duration, which is why convexity matters disproportionately at the
long end.

**Q4: What's a typical duration target for a retiree?**
There's no single answer, but the common pension-style rule is to
match portfolio duration to your average liability date. A retiree
with a 15-year horizon could justify intermediate (5-7 year) bond
duration; younger savers with longer horizons can hold longer
duration without it being inappropriate. Most "lifecycle" target-
date funds default to 5-7 year duration in the bond sleeve and
shorten gradually with age.

**Q5: Did anyone make money on the 2022 bond move?**
Yes — anyone short long-duration Treasuries via TLT puts, ZROZ
shorts, or paying-fixed in the swaps market. Several macro hedge
funds (Brevan Howard, Element Capital) had banner years. The
informational content was free (the Fed had told the market it
would hike); the willingness to position against a 40-year trend
was rare.

**Q6: How does convexity get priced into long bond yields?**
The "convexity discount" — long bonds yield slightly less than
pure expectations would say, because the holder is getting positive
asymmetry for free. The discount is small (5-15 bps at the 30-year
in normal regimes) but real. Inverse-floaters and other
high-convexity instruments trade at noticeably wider discounts to
fair-yield models.

**Q7: What's "DV01" and how does it relate to duration?**
DV01 (or PV01) is the dollar price change for a 1 bps yield move:
$\text{DV01} = D_{\text{mod}} \cdot P \cdot 0.0001$. It's how
fixed-income desks size positions in dollar terms. A trader who
"is long $1M DV01" makes/loses $1M per 1 bps move in their
benchmark yield.

**Q8: How do I hedge a bond portfolio's duration?**
Sell Treasury futures sized by DV01. The TY (10-year futures)
contract has a DV01 around $80; selling enough TY contracts to
match your portfolio's DV01 leaves you duration-neutral. For
non-parallel shifts you'd ladder the hedge across TU/FV/TY/US
contracts using key-rate DV01s.

**Q9: Does duration apply to TIPS the same way?**
Yes, but to *real* yields, not nominal. TIPS modified duration is
the sensitivity of price to real-rate moves. A 10-year TIPS has
real duration around 8.5 — about the same number as a nominal
Treasury — but it's measuring exposure to a different rate. In
2022 nominal yields exploded but real yields exploded more, which
is why TIPS lost almost as much as nominals.

**Q10: How does duration apply to equities?**
Stocks have effective duration too — measured by how price responds
to discount-rate moves. High-multiple growth stocks (cash flows far
in the future) have equity durations of 25+, while dividend-paying
utilities are around 10-15. The 2022 Nasdaq drawdown wasn't a
"tech bubble" so much as a duration repricing — the same Taylor
expansion at work, just on equity cash flows.

**Q11: What's the difference between effective duration and
option-adjusted duration?**
Effective duration shocks the *yield* and remeasures price.
Option-adjusted duration (OAD) shocks the *yield curve* in a
model that accounts for embedded options (calls, prepay, etc.).
For an MBS, OAD differs from modified duration because the prepay
option shortens the effective cash flows. Same idea, more precise
machinery.

**Q12: How do I use the lab below?**
Slide maturity to see duration grow roughly linearly. Slide coupon
to see duration shrink as more cash arrives early. Slide the rate
shock and watch the three price predictions diverge — exact, linear-
duration-only, and duration+convexity. The convexity-corrected
prediction tracks exact almost perfectly out to +/-200 bps; beyond
that, even quadratic Taylor breaks down and you should reprice from
cash flows directly.

---

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
