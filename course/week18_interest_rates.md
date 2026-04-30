# Week 18: Interest Rates — What the Fed Does, What the Market Does, and How Rates Flow Into Asset Prices

---

## Part 1: Reading Section

---

### 1. Why This Is Important

There is one number that prices every other number in finance, and it
is the discount rate. The discount rate is built out of two pieces:
the risk-free Treasury yield, and a credit/equity spread on top.
Move the Treasury yield, and *every dollar of every future cash flow
on the planet* — your mortgage, your stocks, your private equity
fund's NAV, your country's pension liability, the lease on the
warehouse next door — silently reprices. There is no asset that
sits outside this gravitational field.

The Federal Reserve does not set this number directly. The Fed sets
*one* rate (the overnight federal-funds rate) on *one* day every six
or seven weeks, and the market does the rest. Mortgage rates, the
10-year Treasury, BAA corporate yields, junk-bond spreads, the dollar,
and equity multiples all adjust without permission. The Fed plants a
flag at the short end; the market builds the curve.

You need to internalise four things from this lesson.

1. **Rates are the universal denominator.** A stock at $100 with $5 of
   earnings growing at 3% is worth one number at a 4% discount rate
   and a very different number at an 8% discount rate. Same business,
   same earnings, different price. The interactive at the end of this
   lesson lets you slide the discount rate across a typical
   long-duration cash flow and watch present value collapse. Do that
   exercise once — really do it, with the slider — and you will
   never again ask "why did the market drop on the Fed announcement?"

2. **The Fed funds rate is a lever, not a result.** What you actually
   pay on your mortgage, what an investment-grade firm pays on its
   bonds, and what the Treasury pays at the 10-year auction are *market*
   rates. They are influenced by Fed policy but are not set by it.
   The cascade chart in §2.1 shows the four layers — funds, 10-year,
   30-year mortgage, BAA — and how the spread between them widens in
   stress and during regime change.

3. **Real rates, not nominal rates, drive valuations.** A 5% nominal
   yield in a 5% inflation world is the same real return as 0% in a
   0% inflation world. The market separates the two through the TIPS
   breakeven (§2.3). When 2022 happened, *nominal* yields tripled but
   *real* yields went from -1% to +2%. The +3% real-rate move is what
   crushed long-duration tech, not the nominal headline.

4. **We have lived through exactly two regime breaks in 45 years**
   (SOUL anchor #2). The first was Volcker in 1981, ending double-digit
   inflation by ratcheting the funds rate to 20% and triggering the
   four-decade bond bull market. The second is 2022 onward, the end of
   the zero-bound era. The investors holding 60/40 portfolios in 2026
   have spent their whole working career on one side of one regime.
   They need to know what the other side feels like.

---

### 2. What You Need to Know

#### 2.1 The Rate Cascade — Fed Funds, 10-Year, Mortgage, BAA

The interest-rate universe is not one number. It is a layered
hierarchy that the cascade chart makes visible.

![The four-layer interest-rate cascade from 1990 through April 2026: Federal funds rate, 10-year US Treasury yield, 30-year mortgage rate, and BAA corporate bond yield. The Fed sets the bottom layer; the market sets the rest. Spreads widen materially in 2008-09, 2020 COVID, and the 2022-2024 hiking cycle.](image/week18_rate_cascade.png)

Read the chart from the bottom up.

- **Fed funds (FEDFUNDS, green)** is what banks charge each other
  overnight, targeted by the Federal Open Market Committee. It is the
  *only* line on this chart the Fed sets directly. From 2009 to 2015
  and again 2020 to 2022, this line is pinned at the zero bound. The
  hiking cycle from March 2022 to mid-2024 walks it from ~0% to ~5.4%.
- **10-year Treasury (DGS10, blue)** is the auctioned market yield on
  the 10-year US note. It is the most-watched price on earth. Mortgages,
  long-dated corporates, and stock-market discount rates are all
  benchmarked against it. Note how it tracks the funds rate over long
  windows but not short ones — the 10-year is a 10-year forecast of
  the *path* of short rates plus a term premium, not a copy of today's
  funds rate.
- **30-year mortgage (MORTGAGE30US, orange)** sits on top of the 10-year
  with a spread that compresses in calm markets (~150 bps) and widens
  in stress (>250 bps in 2008-09 and again in 2022-23). The spread
  reflects prepayment risk, MBS-investor demand, and bank capacity.
- **BAA corporate (BAA, red)** is the lowest-rung investment-grade
  corporate yield. Its spread over the 10-year Treasury *is* the
  market's read on default risk. In 2008-09 the spread blew out from
  ~170 bps to ~600 bps. In April 2026 it is back near ~190 bps.

What you should take away: the Fed sets one rate, and four other rates
move because of it but not in lock-step with it. Understanding which
spread is widening, and why, is most of what serious macro analysis
actually does.

#### 2.2 The Discount Rate Is the Universal Denominator

Every valuation you will ever see — DDM, DCF, P/E, NAV, IRR — is
arithmetic on top of one assumption: the discount rate $r$. We met
the simplest form back in Week 5. The Gordon growth model says a
perpetuity that pays $D$ next period, growing at $g$ forever, is worth

$$ P = \frac{D}{r - g} $$

Three lines of algebra contain most of what equity valuation is.
Notice what happens at the limits.

- $r = 4\%, g = 0\%$ -> $P/D = 25$. A typical bond-like stock.
- $r = 6\%, g = 2\%$ -> $P/D = 25$. Same multiple, totally different
  story. Higher growth offsets higher discount.
- $r = 4\%, g = 3\%$ -> $P/D = 100$. The "long-duration growth" multiple
  the world saw in 2020-21.
- $r = 8\%, g = 3\%$ -> $P/D = 20$. Same business, +400 bps of discount,
  multiple compressed by 80%.

The 2022 collapse in long-duration tech was *exactly this last move*.
Nominal 10-year Treasury yields rose ~250 bps and equity risk premia
widened ~150 bps. A 4-percentage-point lift in the discount rate cuts
the present value of a long-dated cash-flow stream by roughly half. It
did. The interactive at the end of this lesson computes $P/(r-g)$
live so you can stop arguing with the chart and start sliding the
slider.

The same denominator drives bond duration (Week 5), real-estate cap
rates, private-equity NAV marks, and pension liabilities. Everything
financial is a present-value calculation in disguise. The discount rate
*is* the asset-pricing kernel; everything else is decoration.

#### 2.3 Real Rates and TIPS Breakevens

Nominal yield = real yield + expected inflation. The decomposition
matters because borrowers and lenders both care about purchasing
power, not headline numbers. The Treasury issues two parallel debt
instruments: nominal Treasuries (DGS10) and inflation-protected
Treasuries (TIPS). The yield difference between them is the
**10-year breakeven inflation rate**, FRED series `T10YIE`.

![10-year breakeven inflation rate from 2003 through April 2026, FRED T10YIE = nominal 10-year Treasury yield minus 10-year TIPS yield. The market's daily mark-to-market estimate of average CPI for the next decade. Annotated at the late-2008 deflation scare (briefly negative), the 2022 inflation peak (~2.9%), and the April 2026 reading.](image/week18_breakeven_inflation.png)

Three points jump out.

1. **The 2008 deflation scare**. In November 2008 the breakeven went
   *negative* — the market briefly priced in falling prices for a
   decade. That single print is why the Fed went to QE in early 2009;
   negative breakevens were the deflation alarm bell.
2. **The 2022 inflation peak (~2.9%)**. Even at the peak of 9% headline
   CPI, the 10-year breakeven never broke 3%. The bond market believed
   throughout that the Fed would eventually crush inflation back to
   target. That belief was right and it kept long-rate panic from
   becoming a self-fulfilling prophecy.
3. **The April 2026 reading** sits in the band the Fed targets, which
   is part of why the funds rate is being eased back from peak.

For an equity investor, real rates matter more than nominal because
real cash flows (earnings, dividends, rents) inflate with prices. When
real rates rise — as they did sharply in 2022 — long-duration equity
collapses *more* than the nominal-rate move alone would predict.

#### 2.4 The 1981 Volcker Peak and the 2020 Zero Bound — Two Regime Breaks

If you compress 60 years of US monetary history into two events, they
are these.

In **October 1979 through July 1981**, Paul Volcker walked into the
Fed determined to break double-digit inflation. He did it by letting
the funds rate go where it had to: it peaked above 19% in mid-1981.
The 10-year Treasury yield peaked at 15.8%. The economy went into a
brutal double-dip recession. Inflation broke. And the bond market began
a forty-year bull run that did not end until July 2020, when the
10-year yield hit 0.55%. Anyone who bought the long bond in 1981 and
held through 2020 made an annualised total return that beat the S&P 500.

In **March 2020 through 2022**, the Fed cut the funds rate to zero,
expanded the balance sheet by $4.6 trillion, and held real rates
deeply negative. Asset prices went vertical. Long-duration equity, SPACs,
crypto, residential real estate — everything sensitive to the discount
rate behaved like the discount rate had been *set to zero*, because in
real terms it had.

These two events bracket what SOUL anchor #2 calls the *passive
40-year regime*. The "passive index investing always wins" claim that
animates Bogle, Buffett, and the entire ETF industry is built on top
of the 1981-2020 bond bull market and the disinflation it carried with
it. The strategy works. But the strategy *also* sat on top of a
once-in-history regime backdrop, and SOUL's whole point is that
regime backdrops change.

Anchor #6 (vol-tail-wags-dog) connects directly: Volcker had to break
the bond market to break inflation. In 2022, the Fed had to risk
breaking equities to break post-COVID inflation. When the Fed pulls
the rate lever hard, the *vol* tail wags the policy dog. SVB in March
2023 was exactly this — a regional bank duration-mismatched into the
hiking cycle, then run on by a Twitter-coordinated depositor base in
36 hours. The Fed's BTFP backstop arrived the next weekend.

#### 2.5 The 2022-2024 Hiking Cycle in Detail

The numbers are worth memorising as a calibration set.

- **March 2022**: funds rate moves from 0-0.25% to 0.25-0.50%. First
  hike in three years.
- **November 2022**: funds rate at 3.75-4.00% after four consecutive
  75-bps moves. Fastest tightening pace since 1981.
- **July 2023**: peak funds rate of 5.25-5.50%.
- **March 2023**: SVB, Signature, First Republic. Three banks fail in
  a week. The Fed launches the Bank Term Funding Program backstop and
  keeps hiking.
- **2024**: first cut in September (50 bps), then 25-bps cuts through
  year-end. Funds rate ends 2024 at 4.25-4.50%.
- **April 2026**: funds rate has settled; the breakeven is back near
  the 2% Fed target (see §2.3). The yield curve, inverted from mid-2022
  to early 2025, is back to a normal positive slope.

Three things this cycle taught.

1. The transmission lag from policy to economy is about 12-18 months.
   Hikes that began in March 2022 hit residential housing and small
   business credit hardest in late 2023 and 2024.
2. Most of the asset-price damage happens in *anticipation* of the
   cycle, not during it. The S&P bottomed in October 2022, eight
   months *before* the peak funds rate. Markets price the discount
   rate forward.
3. Duration matters more than ever. The 30-year Treasury lost ~46% of
   its price from August 2020 to October 2023. That is bigger than
   most equity bear markets. Bonds are not "safe."

#### 2.6 Growth Stocks vs Value Stocks Under Rate Changes

Equity duration is real, even though we never quote it. A stock whose
earnings grow at 3% with most of its cash flow inside the next five
years has a low duration; the discount rate doesn't move it much. A
stock whose earnings grow at 25% with the bulk of its cash flow expected
ten or twenty years out has a *very* high duration — it is essentially
a long-dated zero-coupon bond.

Mechanically, **growth stocks are long duration. Value stocks are
short duration.** When rates rise:

- Growth multiples compress hard. The Nasdaq-100 fell 33% in 2022
  while the S&P 500 fell 18% and the Russell 2000 Value fell only 14%.
  Same earnings season, different sensitivity to $r$.
- Value stocks (banks, utilities, industrials) have shorter cash-flow
  duration and often benefit from steeper yield curves directly.
- Bonds, of course, lose price proportionally to duration: 10-year
  -18%, 30-year -33% in 2022 alone.

This is why "growth vs value" rotates with the rate cycle, not with
investor sentiment. The interactive at the end of this lesson includes
a side panel showing exactly how a +100 bps rate move hits four
representative cash-flow streams: a 10-year bond, a 30-year bond, a
high-growth equity (4% growth, 10-year duration), and a value equity
(1% growth, 5-year duration).

The barbell intuition (SOUL anchor #14) survives this rotation: a long
position in short-duration value plus a small allocation to convex
long-duration growth gives you both regime payoffs without betting on
which regime wins. Pure long-duration tech would have been a
career-ender in 2022; pure value would have missed every great
investment of the prior decade. The barbell wins because the regime is
unknowable and rate moves are large.

---

### 3. Common Misconceptions

1. **"The Fed sets mortgage rates."** No. The Fed sets the overnight
   funds rate. Mortgages are priced off the 10-year Treasury plus an
   MBS spread. Both pieces are market-determined.
2. **"Higher rates always mean lower stock prices."** Not always. In
   the early phase of a rate-hiking cycle, when hikes signal a healthy
   economy, equities can rise alongside rates. The 2004-06 cycle is
   the classic example. What matters is whether real rates rise faster
   than expected growth.
3. **"Inflation is good for stocks because companies raise prices."**
   Only at moderate levels and only sometimes. Above ~4% inflation,
   equity multiples compress sharply (1970s, 2022). Stocks are real
   assets, but they are also long-duration discounted cash flows, and
   the discount-rate effect dominates above ~3% inflation.
4. **"TIPS protect against inflation."** Yes, and they are also long
   bonds whose *real* yield can rise. In 2022 TIPS lost ~12% of
   principal value because the real-yield component rose, even though
   they did exactly what they were supposed to on the inflation leg.
5. **"You can't lose money in Treasuries if you hold to maturity."**
   True for nominal terms, false for real terms. A 30-year bond bought
   at 1% yield in 2020 will repay every nominal dollar but is locked
   into a real return of roughly -1% per year for thirty years against
   2026 inflation expectations.
6. **"Cash is safe."** Cash is safe nominally and dangerous in real
   terms during inflation. From 2020 to 2024 a dollar in a 0%-yielding
   bank account lost ~17% of purchasing power. Cash is a *position*,
   not a default. SOUL anchor #13 (four tranches) explicitly carves out
   liquidity *and* T-bills, separately.
7. **"Quantitative easing causes inflation."** Eight years of QE from
   2009-2017 produced no consumer inflation. The 2020-21 round produced
   the biggest inflation in 40 years. The difference was fiscal: 2020-21
   QE was paired with $5+ trillion of fiscal transfers that put cash
   directly in consumer hands. QE alone moves bank reserves, not
   prices.
8. **"The yield curve inversion always means recession."** It has
   preceded every recession since 1955 with one ambiguous exception —
   that is a high hit rate, not a guarantee. The 2022-25 inversion is
   the longest on record and produced a soft landing rather than a
   classic NBER recession.
9. **"Foreign rates don't matter to US stocks."** Wrong. The US dollar
   is the world's reserve currency; rate differentials drive the dollar,
   the dollar drives multinational earnings (~40% of S&P 500 revenue is
   non-US), and the dollar drives commodity prices. The Bank of Japan's
   2024 policy shift was a meaningful S&P 500 input.
10. **"Real rates above 2% are 'normal'."** Real rates *averaged* 2-3%
    from 1900 to 1980. They averaged around 0% from 2008 to 2022. There
    is no single "normal" — the regime defines the level. SOUL anchor
    #2 again.

---

### 4. Q&A Section

**Q: If I had to watch only one rate, which one?**
A: The 10-year Treasury yield. It is the single best summary of every
piece of information in the rate market — Fed policy expectations, term
premium, real growth expectations, and inflation expectations. It is
quoted continuously, has no credit spread, and is the discount rate
everyone references.

**Q: What's the difference between the federal funds rate and the
"discount rate"?**
A: Confusing terminology. The federal funds rate is the overnight
interbank lending rate the Fed targets. The Fed's *discount rate* is
the (slightly higher) rate the Fed charges banks that borrow directly
from the discount window. In practice the discount window is a
backstop; the funds rate is the headline tool. When this lesson says
"discount rate" without qualifier, it means the financial-economics
discount rate $r$ used in DCF, not the Fed window rate.

**Q: How do I know which way real rates are moving?**
A: Subtract the 10-year breakeven (FRED `T10YIE`) from the nominal
10-year (FRED `DGS10`). FRED also publishes `DFII10` (the 10-year TIPS
yield) directly. Real rate = nominal yield - breakeven. A rising real
rate is the most reliable bear signal for long-duration assets.

**Q: Should I lock in fixed-rate or floating-rate debt now?**
A: This is a personal-finance call, not investment advice, but the
framework is: if you expect real rates to rise from here, fix; if you
expect them to fall, float. With the 10-year at ~4% and breakevens
near 2% in April 2026, real rates are around 2% — roughly the long-run
average. Neither aggressive lock-in nor aggressive floating looks
asymmetric here.

**Q: What is "term premium" and why is everyone always talking about
it?**
A: The term premium is the extra yield investors demand to hold a
long bond instead of rolling short bonds. Mathematically, it is the
piece of the 10-year yield that *isn't* explained by expected future
short rates. From 2014 to 2021 it was roughly zero or negative — bond
investors paid a premium for safety. In 2024-25 it has crept back to
~50 bps. A higher term premium means longer-duration assets get
discounted more.

**Q: Does the Fed actually control inflation?**
A: It controls the *demand* side of inflation through interest rates
and bank reserves. It does not control supply shocks (oil, chips,
shipping). The 2021-22 inflation was 60% supply-driven and 40%
demand-driven; the Fed could only attack the demand half. Volcker won
in 1981 because demand was the dominant driver. 1973-74 inflation was
mostly oil-shock supply, and Burns's rate hikes did less.

**Q: Why does the bond market sometimes rally on bad economic news?**
A: Because bad news shifts the path of expected future short rates
*lower*, raising bond prices. Bonds love recessions. Equities mostly
hate them. This is the asymmetric correlation that makes 60/40 work.
Week 4 covered this; it is the central piece of why a portfolio
diversifier exists at all.

**Q: How fast does a Fed hike show up in mortgage rates?**
A: The 30-year mortgage moves on the *expectation* of Fed action, not
the action itself. A "surprise" 25 bps hike moves mortgages maybe
10-20 bps that week. A *change in the expected path* — for example,
a hawkish dot plot — can move mortgages 50-100 bps in a single
afternoon. By the time the Fed acts, the cake is mostly baked.

**Q: Are TIPS a free lunch in inflationary periods?**
A: No. TIPS protect the *principal* against CPI but their *real* yield
floats with the market. In 2022 the real yield rose 250 bps and TIPS
prices fell. They protect against unexpected inflation, not against
real-rate normalisation. They are insurance, not magic.

**Q: How should I think about the discount rate for my own portfolio
decisions?**
A: Pick a personal hurdle rate — the return below which a project
isn't worth your time. For most US investors with full-equity-risk
exposure, this is the 10-year Treasury yield plus an equity risk
premium of 4-5%. So in April 2026, with the 10-year at ~4%, your
hurdle is ~8-9%. Anything you allocate to should clear that, or you
should not be doing it. SOUL anchor #1 (alpha is rare): if you can't
articulate a reason your idea clears the hurdle, it doesn't.

**Q: Is the 1981-2020 bond bull market really over?**
A: Probably yes, but "probably" is not "definitely." A second wave of
disinflation (driven by AI productivity, demographics, globalisation
2.0) could push the 10-year back below 2%. But the *baseline* case
for the rest of this decade is range-bound 3-5% nominal yields, which
is the historical norm. Building a portfolio that *needs* yields to
fall to 1% to work — which most aggressive long-duration tech plays
implicitly do — is a regime-dependent bet, and the regime has changed.

**Q: Where does this lesson connect to the rest of the course?**
A: It is the macro engine sitting under Week 5 (bonds), Week 4 (60/40),
Week 10 (cycles), Week 11 (behavioural pitfalls during rate shocks),
Week 13 (long/short and how it plays in different rate regimes). Every
asset has a duration. The discount rate moves all of them. This week
is the link.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Interest Rates: The One Number That Prices Everything Else (Week 18)

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00 to 1:30]**

[VISUAL: title card "Week 18 — Interest Rates"]

**Horace**: There is a single number that sits underneath every other
number in finance, and most retail investors do not realise it is even
there. It is the discount rate. Today we are going to make it visible.

**Stella**: When I started in this industry, I assumed "interest
rates" meant whatever the Fed announced at the press conference. That
turns out to be roughly 5% of the actual story.

**Horace**: The Fed sets one rate. The market sets every other rate
on earth — including the rate you pay on your mortgage and the rate
implicitly buried in your stock-market valuation. Both of those move
without anyone announcing anything.

**Stella**: Today we will walk through the rate cascade chart, the
universal-denominator argument for why the discount rate is the
gravity of finance, the difference between real and nominal rates,
and the two regime breaks of the last 45 years — Volcker in 1981 and
the zero-bound era ending in 2022.

**Horace**: And I want everyone watching to actually open the
interactive at the end of this lesson and slide the discount-rate
slider. The intuition does not transfer through reading. You have to
move the slider yourself.

**Stella**: Let's start with the cascade.

---

**[§2.1 THE RATE CASCADE — 1:30 to 4:30]**

[VISUAL: image/week18_rate_cascade.png]

**Horace**: This is what 35 years of US interest rates look like in
four lines. The bottom green line, federal funds, is the only one the
Fed actually controls. Notice how it sits at zero from 2009 to 2015
and again from 2020 to 2022 — those are the zero-bound years.

**Stella**: The blue line above it is the 10-year Treasury, and you
can see it does not just copy the funds rate. In 2008-09 the 10-year
was around 2-3% while the funds rate was at zero. In 2022 the 10-year
moved up *before* the Fed started hiking, because the bond market saw
the inflation coming and priced it in.

**Horace**: The orange line on top is the 30-year mortgage. Watch the
gap between mortgage rates and the 10-year Treasury. In normal markets
that gap is about 150 basis points. In the 2008 financial crisis it
blew out to over 250. In 2022 to early 2023 it widened again as MBS
investors demanded more compensation for prepayment risk. That spread
is why mortgage rates went above 7% even though the 10-year topped
out below 5%.

**Stella**: And the red line, BAA corporate, is the lowest rung of
investment-grade corporate bonds. The spread between BAA and 10-year
Treasuries is *the* measure of corporate credit stress. You can see
2008-09 stand out — that's when corporate spreads went from ~170 bps
to ~600 bps. April 2026, we're back to ~190 bps. Calm market.

**Horace**: The lesson from the cascade: the Fed has its hand on one
lever. The market builds the rest of the curve from that lever plus
its expectations of growth, inflation, and risk. Anyone who tells you
"the Fed sets mortgage rates" has not looked at this chart.

---

**[§2.2 DISCOUNT RATE AS UNIVERSAL DENOMINATOR — 4:30 to 8:00]**

[VISUAL: blank, then formulae]

**Stella**: Now the central idea of the lesson. The discount rate is
the universal denominator. Every asset on the planet is a stream of
future cash flows discounted by some rate. Move the rate, you move
every asset.

**Horace**: Let me make this concrete with the simplest equation in
finance: P equals D over r minus g. Price equals the next cash flow
divided by the discount rate minus the growth rate. That is the Gordon
growth model and it is most of what equity valuation actually does.

**Stella**: Plug in numbers. r equals 4%, g equals 0%, you get a P/D
of 25. Reasonable for a slow-growing dividend stock.

**Horace**: Now plug in r equals 4% and g equals 3%. You get a P/D
of 100. That is the long-duration tech multiple of 2020-2021.

**Stella**: Now move r up to 8%, keep g at 3%. P/D drops to 20. Same
business. Same growth. Multiple compressed by 80%.

**Horace**: This is what happened in 2022. Nominal Treasury yields
rose roughly 250 basis points and equity risk premia widened roughly
150 basis points. About 400 basis points of total discount-rate lift.
And the long-duration parts of the market — Nasdaq-100, ARKK, SPACs,
crypto — fell 30 to 80 percent. That was not sentiment. That was
arithmetic.

**Stella**: When you watch CNBC and someone says "the market dropped
because rates rose," they are technically correct but they are
hiding the mechanism. The mechanism is that *r* in the denominator
went up, so prices went down. That's it. That is the whole story.

**Horace**: And the same denominator drives mortgage values, REIT
NAVs, private-equity marks, pension liabilities, and your own personal
hurdle rate for whether to take a job in a startup. All of them.

---

**[§2.3 REAL RATES AND TIPS BREAKEVENS — 8:00 to 11:00]**

[VISUAL: image/week18_breakeven_inflation.png]

**Stella**: Now the most-missed concept. Real rates versus nominal
rates. A 5% nominal yield in a 5% inflation world is the same real
return as 0% in a 0% inflation world. Borrowers and lenders both
care about purchasing power, not headline numbers.

**Horace**: The Treasury issues two parallel debt instruments —
regular nominal Treasuries and inflation-protected Treasuries, TIPS.
The yield difference between them is the breakeven inflation rate. It
is the market's daily, mark-to-market guess at average CPI for the
next ten years.

**Stella**: This chart, FRED series T10YIE, is that breakeven from
2003 onward. Three things to notice.

**Horace**: First, late 2008. The breakeven went *negative*. The
market briefly priced in falling prices for a decade. That is why the
Fed went to QE in early 2009 — negative breakevens are a deflation
alarm bell.

**Stella**: Second, 2022. Even with headline CPI hitting 9%, the
10-year breakeven peaked just under 3%. The bond market believed the
Fed would eventually crush inflation. That belief held the long end
together.

**Horace**: Third, April 2026. We are back inside the Fed's target
band, which is part of why the funds rate has been easing.

**Stella**: For an equity investor, the punchline is: real rates
matter more than nominal. When real rates rose 250 basis points in
2022, long-duration tech got crushed *more* than the nominal-rate
move alone would predict.

**Horace**: TIPS, by the way, protect against *unexpected* inflation,
not against real-rate moves. In 2022 TIPS lost about 12% of principal
because real yields rose. They did their job on the inflation leg.
They could not save you from the real-rate leg.

---

**[§2.4 THE TWO REGIME BREAKS — 11:00 to 14:00]**

[VISUAL: cascade chart again, focused on 1981 and 2020 markers]

**Horace**: Compress 60 years of US monetary history into two events.

**Stella**: Volcker, 1981. Paul Volcker walked into the Fed determined
to break double-digit inflation. He did. The funds rate peaked above
19%. The 10-year peaked at 15.8%. The economy went into a brutal
double-dip recession. And the bond market began a 40-year bull run
that did not end until 2020.

**Horace**: Anyone who bought the long bond in 1981 and held to 2020
made an annualised total return that beat the S&P 500. Bonds. Beating
stocks. For 40 years. It is the single greatest fixed-income trade in
modern history.

**Stella**: Event two: March 2020. The Fed cut to zero, expanded its
balance sheet by $4.6 trillion in 18 months, and held real rates
deeply negative. Asset prices went vertical. Long-duration tech, SPACs,
crypto, real estate — anything sensitive to *r* behaved like *r* had
been set to zero, because in real terms it had.

**Horace**: These two events bracket what SOUL anchor number 2 calls
the *passive 40-year regime*. The "passive index investing always
wins" claim — the entire ethos of modern retail investing — is built
on top of the 1981-2020 bond bull and the disinflation that came
with it.

**Stella**: The strategy works. We are not arguing against passive
investing. But we are saying: the strategy worked on top of a
once-in-history regime backdrop. SOUL's whole point is that regime
backdrops change. And in 2022 the regime started changing.

**Horace**: Vol-tail-wags-dog. SOUL anchor 6. When the Fed pulls the
rate lever hard, things break. Volcker broke 1981 to break inflation.
The 2022 cycle broke Silicon Valley Bank, Signature, and First
Republic in a single week of March 2023, and the Fed had to invent
the BTFP backstop overnight to stop the bleed.

---

**[§2.5 THE 2022-2024 HIKING CYCLE — 14:00 to 16:00]**

[VISUAL: cascade chart, zoomed to 2020-2026]

**Stella**: Quick chronology. March 2022 first hike. November 2022 the
Fed had done four consecutive 75-basis-point moves — fastest tightening
since 1981. July 2023 peak funds rate of 5.25 to 5.50. September 2024
first cut. April 2026 the curve is back to a normal positive slope.

**Horace**: Three lessons from this cycle. One: the lag from policy
to economy is roughly 12 to 18 months. Two: most of the asset-price
damage happens in *anticipation*, not during. The S&P bottomed eight
months before the peak funds rate. Three: duration kills. The 30-year
Treasury lost 46% from August 2020 to October 2023. That is bigger
than most equity bear markets. Bonds are not "safe."

**Stella**: And the rotation between growth and value. In 2022, the
Nasdaq-100 fell 33%, the S&P 500 fell 18%, and Russell 2000 Value
fell only 14%. Same earnings season. Different sensitivity to *r*.

**Horace**: Growth stocks are long duration, value stocks are short
duration. SOUL anchor 14 — the barbell — survives this rotation.
A long position in short-duration value plus a small allocation to
convex long-duration growth gives you both regime payoffs without
having to call the regime. Pure long-duration tech was a career-ender
in 2022. Pure value missed every great trade of the prior decade.
The barbell wins because the regime is unknowable and the rate moves
are large.

---

**[§2.6 THE INTERACTIVE — 16:00 to 17:30]**

[VISUAL: interactive/week18_rate_impact.html]

**Stella**: Open the interactive. There are three sliders — discount
rate, expected growth, starting cash flow — and four output panels.

**Horace**: First exercise. Set growth to 3%, starting cash flow to
$5. Slide the discount rate from 4% up to 8%. Watch the present value
collapse. That is what happened to long-duration tech in 2022.

**Stella**: Second exercise. Look at the side panel. It shows how
+100 basis points of rate change moves four different cash-flow
streams: a 10-year bond, a 30-year bond, a high-growth equity, and
a value equity. Notice the ordering. The 30-year bond and the
high-growth equity both move ~17 to 19 percent. They are essentially
the same instrument from a duration standpoint.

**Horace**: That observation alone, internalised, will change how you
look at portfolio construction. A growth-stock-heavy "diversified"
portfolio is not actually diversified against rate shocks. It is just
the long-bond bet in a different costume.

**Stella**: Spend three minutes on the interactive. Move every slider.
Watch every number change. The intuition does not transfer through
reading. It transfers through dragging.

---

**[OUTRO — 17:30 to 18:00]**

**Horace**: Three takeaways. One: the discount rate is the universal
denominator. Move it, every asset reprices. Two: the Fed sets one
rate; the market sets the rest. Three: we have lived through one
regime — disinflation, falling rates — for 40 years, and that regime
shifted in 2022. SOUL anchor 2.

**Stella**: Next week, Week 19, we go inside inflation itself — what
causes it, what predicts it, and what kinds of inflation are good and
bad for which asset classes. After that, the macro foundation is
complete and we move into the deeper micro of position sizing, factor
exposures, and tax-aware structure.

**Horace**: Until next week.

[VISUAL: end card]
