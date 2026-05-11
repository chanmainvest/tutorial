# Week 5: Bonds — Coupons, Prices, and Yields

---

## Part 1: Reading Section

---

### 1. Why This Is Important

A bond is the simplest financial instrument in the world. You lend
someone a known amount, on a known schedule, for a known
**interest payment** (the *coupon* — that's the bond-market word
for it, and we'll use it for the rest of the lesson), and they
pay you back at a known date. Four numbers and a calendar.
Stocks have nothing this clean.

And yet — this simplest instrument generated the largest single
multi-decade trend in modern financial history (a forty-year bull
market from 1981 to 2020 in falling yields), and then in 2022
delivered the worst calendar year for US Treasuries on record.
Both moves were already inside the four-number contract. §2.2
shows the one equation that turns the contract into a price; the
rest of the lesson is just consequences of that equation.

*(Side note: that same present-value equation — future cash flows
discounted back to today — is also how stocks, real estate, and
every other cash-flow asset are valued. It is the most important
formula in the entire course. We meet it cleanly here in bonds
because bonds have the cleanest cash flows; we apply it to
stocks in Week 21.)*

You need to understand bonds for **five** reasons.

1. **They set the base of the discount rate for everything.** Every
   cash flow on earth — your mortgage (which is literally a bond
   you issued to the bank), a stock's earnings stream, a
   private-equity exit, a pension liability — is priced by
   discounting at the risk-free Treasury curve **plus an
   asset-specific risk premium**. The Treasury curve is the
   *base*; the premium is what the market demands on top for the
   particular asset's risk. When the 10-year yield moves from
   1.5% to 4.5%, the base moves under every long-duration asset
   on the planet, and they all reprice (the spread on top can
   move too, but the base move is what nobody can hide from).
   You cannot understand any other asset class without
   understanding what its discount rate is doing. Worth knowing
   that bonds are also *historically* prior: organised sovereign
   debt markets predate organised stock markets by centuries
   (Sidney Homer's *A History of Interest Rates* traces continuous
   bond markets back to 13th-century Venice and Genoa; the
   Amsterdam stock exchange was a 1602 latecomer, and through
   most of the 18th and 19th centuries equities had a *worse*
   reputation than bonds — closer to gambling than investing). The
   modern instinct that "stocks are the main asset class and bonds
   are a sleepy add-on" is a 20th-century artefact, not a
   permanent truth.
2. **They are an asset class in their own right.** Last week's 60/40
   leaned on Treasuries for the diversification benefit. This week
   we open the bond box and ask: what are we actually holding,
   how does it pay, and how does its price form? After this lesson
   the 40 in 60/40 is no longer a black box.
3. **The bond market is bigger than the stock market — and it is
   what institutions actually trade.** Global bond market
   outstanding is roughly USD 130-140 trillion (BIS / SIFMA, 2024
   estimates), against roughly USD 110 trillion in global equity
   market cap. US Treasuries alone are ~USD 27 trillion. *Daily*
   trading volume in US Treasuries runs ~USD 900 billion versus
   ~USD 500 billion across all US-listed stocks combined. Why
   does this matter to a retail equity investor? Because almost
   every form of leverage in the rest of the financial system is
   *collateralised by Treasuries*: bank reserves, repo (the
   overnight funding market that keeps brokers, hedge funds, and
   primary dealers running), futures-exchange margin, swap-dealer
   collateral, central-bank liquidity facilities. When Treasuries
   move, the *cost and availability of leverage* moves under every
   other asset. Stress in the Treasury market (e.g. March 2020,
   the September 2019 repo spike) is a stress signal for the
   whole system. Stocks are the visible tip; bonds are the
   plumbing underneath.
4. **They tell you what the market expects.** The yield curve, the
   credit spread between BAA corporates and 10-year Treasuries,
   and the TIPS breakeven rate are three separate, daily-quoted,
   public forecasts of growth, default risk, and inflation. The
   bond market is the cheapest macro intelligence service on
   earth.
5. **The 1981-2020 bond bull market is the regime backdrop for
   almost every "passive works" claim of the last two
   generations.** A generation of investors has never seen a real
   bond bear market — and 2022 was the first warning shot. This
   regime-shift framing is *not* original to this course: Howard
   Marks laid it out cleanly in his December 2022 Oaktree memo
   *"Sea Change"* (and again in the May 2023 follow-up), arguing
   that the four decades of falling rates from 1980 onward were a
   one-off tailwind for almost every asset and that we are now
   entering a higher-rate regime in which different strategies
   will work. Ray Dalio's *Principles for Dealing with the
   Changing World Order* (2021) makes the longer cycle argument;
   Lyn Alden's *Broken Money* (2023) makes the monetary-plumbing
   argument; Stanley Druckenmiller has been making the
   debt-and-deficit version of the same point in interviews since
   2022. The point is that several serious investors with
   different lenses converged on the same call: the rate regime
   that made buy-and-hold look easy is over, or at minimum no
   longer the safe default. We will return to this throughout
   Levels 4 and 5.

---

### 2. What You Need to Know

#### 2.1 The Bond Cash Flow — Four Numbers and a Calendar

**Scope of this lesson.** Everything below is about *plain-vanilla
fixed-rate bonds* — the contract is locked at issue and never
changes. Callable bonds, floating-rate notes, TIPS,
mortgage-backed securities, convertibles, and structured credit all
add extra moving parts (issuer optionality, rate-resetting
coupons, inflation-indexed principal, prepayment risk,
equity-linked payoffs, tranching). We touch TIPS in §2.5 and
§Q4, and credit/structured products get full treatment in Weeks
31-34. For this week, fix the picture of a coupon plus a
balloon.

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
**starting from the same yield, a 1% drop in yield raises price by
*more* than a 1% rise of the same size lowers it**. (The two
moves have to start from the same yield level and be the same
absolute size; convexity is a *local* property of the curve, not
a universal claim about any pair of yield moves.) That asymmetry
is convexity, and for long bonds it is large. Watch it on the
interactive: hold $c$, $N$ fixed, slide $y$ from 0% to 15% and
see how the curve bends.

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
detail; the YTM is the return you actually earn **only if** you
(a) hold to maturity and (b) reinvest every coupon at the same
yield. Both conditions are usually violated. If you sell before
maturity at a different yield, your *realised* return depends on
where prices are that day — not on the YTM you bought at. If
reinvestment rates fall (rise), your realised return ends up
*below* (above) the original YTM. YTM is the bond's quoted
internal rate of return; it is **not** a guaranteed realised
return for a non-buy-and-hold investor.

**Intuition check before you move on.** A coupon is a number
stamped on a contract — say "$40 a year forever until I pay
back your $1,000" — and it never changes. A *yield* is the
*return* a buyer demands today for taking on that contract.
Those two numbers don't have to agree, because the *price* moves
in between to make them agree. If demand is high, the price
rises; the same $40-a-year stream now gives the buyer a *lower*
percentage return on the higher purchase price; the yield drops.
If demand collapses, the price falls; the same $40 now gives the
buyer a *higher* percentage return; the yield rises. Coupon =
contract; price = market; yield = the percentage return that
falls out of the two. **Open the interactive bond pricer below**
before you continue: hold the coupon at 4%, slide the market
yield from 2% to 8%, and watch the price drop and the YTM
climb. Two minutes on the slider is worth more than ten
re-readings of this paragraph. This is the equation behind every
asset valuation in the rest of the course — do not skip it.

#### 2.6 Credit Ratings — and Why Not to Trust Them Blindly

Before we look at the spread between corporate bonds and
Treasuries, you need to know what makes a corporate bond
*riskier* in the first place — and how the market signals that.

When a company (or a country, or a city) issues a bond,
third-party **credit rating agencies** assign it a letter grade
from "basically as safe as Treasuries" down to "close to
default." The big three are Moody's, S&P, and Fitch. Their
scales differ slightly but map roughly to the same buckets:

| Bucket | S&P / Fitch | Moody's | Plain English |
|---|---|---|---|
| Investment grade — highest | AAA | Aaa | Treasury-like (US gov was AAA until 2011) |
| Investment grade — high | AA / A | Aa / A | Strong company, low default risk |
| Investment grade — lowest | BBB+ to BBB- | Baa1 to Baa3 | Adequate; "BBB" / "BAA" — the line we plot |
| **Cutoff** | --- | --- | Below this is no longer "investment grade" |
| Speculative / "junk" | BB+ down to CCC | Ba1 down to Caa | High yield; meaningful default risk |
| Default / near-default | CC, C, D | Ca, C | Restructuring or already missed a payment |

The "BAA" you'll see on the chart in §2.7 is just Moody's
spelling for the lowest investment-grade rung — the same place
S&P writes "BBB". It is the cleanest century-long corporate
series, which is why we use it.

**The rating system has a structural conflict of interest.** The
rating agencies are paid by the *issuer* of the bond, not by
the buyer. The company that wants its debt to look safer goes
shopping for a rating, and the agency that gives it the higher
grade gets the contract. This is the financial equivalent of
letting students hire and pay their own examiners — and then
asking the examiners to certify how smart the students are.
This isn't a thought experiment. The historical record is
brutal:

- **Enron** carried *investment-grade* ratings until four days
  before it filed for the largest US bankruptcy at the time
  (December 2001).
- **Lehman Brothers** held an A-tier rating from all three
  agencies on the morning it failed in September 2008.
- **The 2008 housing crisis** is the canonical case: tens of
  thousands of subprime mortgage-backed securities were stamped
  AAA — the same rating as US Treasuries — and a large
  fraction of them went on to lose 60-100% of value. The Senate
  Permanent Subcommittee on Investigations (Levin-Coburn report,
  2011) documented agencies rubber-stamping deals over their own
  analysts' objections to keep the issuer fees flowing.
- **Greek sovereign debt** was investment-grade until late 2009;
  within months of the downgrade cascade, it was trading at 30
  cents on the dollar.

What does this mean for a retail investor? **Treat ratings as a
rough sort, not a verdict.** A AAA does not mean "safe"; it
means "the issuer paid for that letter, and historically defaults
in this bucket have been rare *until they aren't*." The market
price and the daily yield spread (§2.7) tell you what *traders
with their own money on the line* think — and they almost always
move before the ratings do. A bond whose yield spread blows out
to distressed levels while it still carries an investment-grade
rating is the market telling you the rating is wrong; ignore the
letter and read the spread.

#### 2.7 Credit Spreads and the Realised Credit Premium

A US Treasury is the textbook default-free asset (it is *as*
default-free as the dollar itself, which is a separate
philosophical issue — see Week 31). Anything else is riskier.
The market prices that extra risk by demanding a higher yield on
the corporate bond than on the matched-maturity Treasury.

Two numbers, *don't confuse them*:

- **Yield credit spread.** A *yield difference* — for example
  Moody's BAA corporate yield minus the 10-year Treasury yield, or
  the option-adjusted spread (OAS) on an investment-grade index.
  Quoted live, every day, in basis points. **Widens upward** when
  default risk reprices (Dec 2008 OAS hit ~600 bps; Mar 2020 hit
  ~400 bps; calm markets sit near 100-150 bps). This is the
  number traders mean when they say "spreads blew out."
- **Realised excess return.** The *return* on corporate debt
  minus the *return* on Treasuries over the same holding period
  (e.g. annual). It bundles together what you *earned* from the
  starting yield spread *and* the price impact of any spread
  movement during the year. In a year where spreads blow out,
  this number goes sharply *negative* — corporate prices fall
  more than Treasury prices.

The chart below shows the second one — annual realised excess
return of BAA corporates over the 10-year Treasury, from 1928
through 2024 (Damodaran annual series, BAA being the lowest
investment-grade rating). It is the cleanest century-long proxy
for what a retail buy-and-hold investor would have *experienced*
holding corporates instead of Treasuries.

![Annual realised excess return of BAA corporate bonds over the 10-year US Treasury, 1928 through 2024 (Damodaran annual data). Bars go sharply negative in 1932, 1974, 2008, and 2020 as defaults reprice and Treasuries rally on flight-to-safety. Long-run average is small and positive; the distribution has a fat left tail.](image/week05_credit_spreads.png)

Three reads:

1. **The long-run mean excess return is small and positive** —
   investment-grade corporate debt has earned roughly 1-2% per
   year above Treasuries on average. That is the unconditional
   *realised* credit premium.
2. **The distribution has a fat left tail.** In a credit blow-up
   year (1932, 1974, 2008, 2020), corporates can underperform
   Treasuries by 10%-25% in a single year as default risk
   reprices (yield spreads blow *out*, corporate prices blow
   *down*) and Treasuries rally on the flight-to-safety bid.
3. **Yield spreads are an early-warning signal — but read them
   live, not on this chart.** Daily/weekly OAS *can* widen ahead
   of equity bottoms during a credit cycle. The annual realised
   excess-return chart above is too coarse to use as a leading
   indicator: it tells you a bad year *happened*, not that one is
   *coming*. For real-time monitoring, watch a daily yield-spread
   series (e.g. ICE BofA US Corporate OAS on FRED). The lesson
   from this chart is the long-run *shape* of the payoff, not
   timing.

For most retail investors the practical answer is: **the credit
premium is real but small, and the tail risk is asymmetric**.
Holding investment-grade corporate debt instead of Treasuries earns
you maybe 1% extra in normal years and costs you 10%+ in the
years that matter most. For diversification against equities, hold
Treasuries. For yield-pickup *income* in retirement, a small
allocation to investment-grade corporates is reasonable.

**Credit default swaps (CDS), capital structure, and the wider
credit complex — short preview.** What we just covered is plain
corporate debt — the borrower borrows, you lend, you collect.
The wider credit complex includes a few more pieces you should
at least *recognise* now and that we cover properly in Weeks
31-34:

- **Capital structure (senior vs junior).** A single company can
  issue several layers of debt. *Senior* (or "secured") debt has
  the first claim on assets in bankruptcy and the lowest yield;
  *junior* / *subordinated* debt is paid only after senior is
  satisfied and yields more to compensate. Below that sits
  preferred equity, then common equity. Each layer is a
  different bond, with a different recovery rate when things
  break. Structured products like CMOs and CDOs slice the same
  underlying loan pool into *tranches* with the same stack —
  AAA tranches eat losses last, equity tranches first. The 2008
  blow-up was largely a misrating of those tranches. (Week 33.)
- **Bonds vs bank loans vs private credit.** A *bond* is
  publicly issued, traded in a secondary market, governed by an
  indenture, and rated. A *bank loan* ("leveraged loan") is a
  privately negotiated agreement, usually senior secured,
  floating-rate, and held by banks or loan-fund vehicles — it
  trades but more thinly. *Private credit* / *direct lending* is
  a non-bank loan from a fund directly to a company, often
  unrated and held to maturity. Same economic idea (someone
  borrows, someone lends), three different liquidity, disclosure,
  and pricing regimes.
- **Credit default swaps (CDS).** A CDS is *insurance on a bond*.
  The buyer pays an annual premium (the CDS spread, in basis
  points); if the underlying bond defaults, the seller pays out.
  The CDS spread is the cleanest market-priced view of default
  risk on a given issuer. Sovereign-CDS markets in particular
  often move *before* the rating agencies act — Greek 5-year CDS
  was screaming distress for months while the official rating was
  still investment-grade. (Week 33 covers the mechanics; the
  retail takeaway here is that you can *read* CDS spreads as a
  free macro signal even though almost no retail investor
  *trades* them.)

#### 2.8 The Forty-Year Bull Market and the 2022 Break

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
  The argument *for* a higher floor: US federal debt is now ~120%
  of GDP, deficits are running ~6-7% of GDP in peacetime, and
  every year the Treasury has to roll over trillions of dollars
  of maturing debt at whatever the prevailing rate is (the *debt
  wall*; §2.10). When the supply of new bonds is enormous and
  growing, the marginal buyer demands a higher yield to absorb
  it — the Treasury cannot dictate the rate, it can only set the
  coupon and let the auction price tell it the true yield.
  Combine that with three sovereign-credit downgrades (S&P pulled
  US AAA in August 2011 to AA+; Fitch followed in August 2023;
  Moody's downgraded in May 2025), and "yields can only fall from
  here" stops being a safe assumption.

The regime-shift framing here is *not* original to this course.
Howard Marks's December 2022 Oaktree memo *"Sea Change"* and the
May 2023 follow-up *"Sea Change II"* lay out the argument that
four decades of falling rates were a one-off tailwind under every
asset class, and that the next decade will reward different
behaviours. Ray Dalio's *Principles for Dealing with the Changing
World Order* (2021) makes the longer cycle case; Lyn Alden's
*Broken Money* (2023) makes the monetary-plumbing case; Stanley
Druckenmiller has been hammering the debt-and-deficit version in
interviews since 2022; David Rosenberg has the deflationist
counter-argument. We are not picking a winner here — we are
flagging that several serious investors with very different
lenses converged on "the rate regime that made buy-and-hold look
easy is over, or at minimum no longer the safe default." That
passive index investing *worked* across 1981-2020 partly because
bonds rallied and equity multiples expanded together as rates
fell. The trigger that breaks the regime is **a sustained rise
in long yields**, and we are watching that trigger fire right
now in real time. It is too early to declare the regime over;
it is too late to pretend nothing has changed.

#### 2.9 TIPS, Floating-Rate Notes, and Bond Maturities You'll Meet

So far we have been looking at plain *fixed-rate* nominal bonds
(face value and coupon both stated in dollars). The bond
universe has a few common variants you'll bump into immediately
as a retail investor; they all live on top of the same
present-value equation, but with one or two pieces swapped out.

- **TIPS (Treasury Inflation-Protected Securities).** The
  *principal* indexes to CPI. The coupon rate is fixed but applies
  to the inflation-adjusted principal, so dollar coupons grow with
  CPI too. The yield quoted on a TIPS is the *real* yield (above
  CPI). You're betting that *realised* inflation will exceed the
  **breakeven inflation rate** = nominal Treasury yield − TIPS
  real yield. (April 2026: ~4.2% − ~1.8% ≈ 2.4% on the 10-year.)
  Caveats: (a) the CPI those bonds index to is the *official*
  BLS CPI, which we already saw in Week 1 has been methodologically
  rebased multiple times since 1990 and is widely argued to
  *under-state* lived inflation — so even "inflation-protected"
  bonds are protected against the *measured* number, not
  necessarily your grocery bill; (b) when CPI prints high, the
  Fed often hikes nominal rates in response, which pushes TIPS
  prices *down* via duration even as the principal accrual
  pushes them *up* — the two effects partially cancel and TIPS
  can lose money in a rate-hiking inflation surprise (this
  happened in 2022); (c) **Canada discontinued new issuance of
  Real Return Bonds in November 2022** citing weak demand at
  auction, and that decision has been criticised by pension funds
  ever since — a useful reminder that even sovereign issuers can
  withdraw inflation protection from the menu. Historically the
  TIPS breakeven has been a roughly unbiased but *noisy*
  forecast of subsequent CPI: it tracks the long-run direction
  but routinely misses by 1-2 percentage points, and during
  liquidity stress (Q4 2008, March 2020) it temporarily
  collapses to absurd levels because TIPS are far less liquid
  than nominals.
- **Floating-rate notes (FRNs).** The coupon resets periodically
  to a benchmark (SOFR + a fixed spread, or for many corporate
  FRNs, 3-month SOFR + 30-150 bps). When the benchmark moves,
  the coupon moves with it, so the *price* barely changes —
  duration is essentially the time to the next reset, which for
  a quarterly-reset note is ~0.25 years. FRNs are useful when
  you expect rates to rise (you keep collecting the higher
  coupons without taking the price hit) and useless when you
  expect them to fall (you give up the chance to lock in a
  higher fixed yield). The trade-off vs a vanilla nominal bond:
  you swap *duration risk* for *reinvestment risk*.
- **Common bond maturities.** Treasuries come in T-bills (4, 8,
  13, 17, 26, 52 weeks; zero-coupon, sold at a discount to face),
  notes (2, 3, 5, 7, 10 year), and bonds (20, 30 year).
  Investment-grade corporates cluster heavily at 5, 10, 30 year.
  *Perpetual bonds* ("perps") have no maturity — the issuer
  pays the coupon forever and may *call* (redeem) the bond at
  par on specified dates; the UK *consols* issued in the 18th
  century were the canonical case (some ran for over 250 years
  before being redeemed in 2015). *Century bonds* (50- to
  100-year maturities) are issued occasionally by sovereigns and
  blue-chip corporates — Disney issued a 100-year in 1993,
  Argentina issued a USD century bond in 2017 (and defaulted on
  it three years later, which tells you everything you need to
  know about reaching for yield on long-duration sovereign
  credit).
- **Convertible bonds.** A bond bundled with an embedded equity
  call option — the holder can convert the bond into a fixed
  number of shares of the issuer's stock. They yield less than
  straight bonds because the equity option is worth something.
  Convertibles are their own asset class with their own
  Greeks-flavoured pricing math; we touch them when we cover
  options in Weeks 25-30 and again when we look at issuer
  capital-structure plays.
- **Callable bonds.** The issuer reserves the right to redeem the
  bond early at a stated price. This is a short option *the
  buyer wrote to the issuer* — when rates fall, the issuer
  refinances cheaper and calls the old bond, capping your upside.
  Callable bonds therefore yield *more* than non-callable ones
  for the same credit/maturity. Most US Treasuries are
  *non-callable*; corporates and especially municipals are often
  callable — always check the indenture before you build a
  ladder.

#### 2.10 The Debt Wall and the Refinancing Cycle

A bond is finite — every bond has a maturity date when the
issuer has to hand back the principal. For an issuer with a
steady stream of debt outstanding (every government, every large
company, every mortgage holder), bonds are constantly maturing
and have to be *refinanced*: the issuer comes back to market
and sells new bonds to raise the cash to pay off the old ones.
This recurring obligation is the **refinancing cycle**.

When you stack the maturities of all the bonds an issuer has
outstanding by year, you get a wall — a year in which a large
lump of debt is coming due all at once. Two examples to make this
concrete:

- **The US Treasury debt wall.** Roughly USD 7-9 trillion of US
  Treasury debt matures every year and has to be rolled at
  whatever the prevailing yield happens to be that day. When the
  Treasury issued a 10-year note at 0.7% in 2020, that note
  matures in 2030 and gets refinanced at whatever the 10-year
  yield is in 2030. If the 10-year is 4.5%, the federal interest
  bill rises mechanically and permanently — the Treasury cannot
  "choose" not to roll. As of 2026, US federal interest expense
  has crossed USD 1 trillion per year and now exceeds the entire
  defence budget. That is the refinancing cycle eating fiscal
  space in real time.
- **The corporate "maturity wall."** Roughly USD 1.8-2 trillion
  of US investment-grade and high-yield corporate debt matures
  in the 2025-2027 window — most of it issued at 2-3% during the
  2020-2021 zero-rate window. Companies that locked in cheap
  long-dated debt then are now refinancing at 5-7%. For a
  highly-levered firm whose interest coverage was already thin,
  a 300 bp jump in refi cost is the difference between
  comfortable and distressed. A wave of high-yield defaults in
  the next 24-36 months — if it comes — will be primarily a
  refinancing-cycle event, not a recession event.

The refinancing cycle is why "yields are higher than they used
to be" is not a temporary bookkeeping fact — every year that
passes, more of an issuer's old cheap debt rolls into new
expensive debt, and the *average* coupon paid grinds higher
toward the prevailing rate. For sovereigns this is the slow path
to fiscal pressure; for corporates it is the slow path to credit
repricing. Either way, it is *bond plumbing* — not a forecast,
an accounting consequence — and worth watching.

#### 2.11 How Retail Actually Buys Bonds (and Why ETFs Have Their Own Problem)

Almost no retail investor buys individual corporate bonds.
Three reasons:

1. **Liquidity is awful.** Most corporate-bond CUSIPs trade a
   handful of times a *week*, not a day. Bid/ask spreads are
   often 50-200 bps — you pay 1-2% just to get in and out. By
   contrast Treasuries are the most liquid asset on earth (tight
   bid/ask, $900b daily volume), and *those* you can comfortably
   buy individually.
2. **Minimum lot sizes are large.** Many corporate issues trade
   in $5,000 or $10,000 minimums; a diversified 50-name corporate
   portfolio needs a quarter-million dollars before you can even
   start.
3. **Single-issuer default risk is real.** Lose 30% on one
   bankrupt name and your whole bond sleeve takes a hit you can't
   diversify away with a small handful of issuers.

So retail typically holds a *bond ETF* (LQD, BND, AGG, HYG, etc.).
That solves the three problems above but introduces one of its
own that you should know about:

**Most bond indices are weighted by amount of debt outstanding.**
Think about that. A market-cap-weighted *stock* index assigns
the biggest weight to the company the market values most highly
(Apple, Microsoft). A market-cap-weighted *bond* index assigns
the biggest weight to the issuer that has *borrowed the most*.
The most-indebted issuer is not necessarily the safest; it is
literally the one with the most debt to repay. Aggregate bond
ETFs end up overweight the US Treasury (which is fine — it is
at least the borrower with printing-press authority) but also
overweight the most-leveraged investment-grade corporates. This
is structurally different from stock-index investing and is a
reason "buy a corporate-bond ETF and forget it" is not as
benign a default as "buy a stock-index ETF and forget it." If
you want corporate exposure, look at *equal-weighted* or
*fundamentals-weighted* bond ETFs, or accept the cap-weight
bias deliberately.

This is also why a corporate-bond ETF in a credit blow-up does
not behave like a Treasury ETF in a rate move: its top holdings
are exactly the issuers most likely to be downgraded and
repriced. The 2008 LQD drawdown (-15% peak-to-trough in late
2008) and the March 2020 HYG drawdown (-21% in three weeks) are
the historical precedents.

---

### 3. Common Misconceptions

**Misconception 1: "Treasuries are riskless."**

Treasuries are *credit*-riskless **in nominal dollars** (the US
government can print the dollars it owes). They are not
*price*-riskless or *purchasing-power*-riskless. In 2022 the
10-year lost 18% of its price. In 1973-1981 it lost roughly 40%
of its real value. "No default risk" is not the same as "no
risk."

A sharper version: even sovereigns *can* and *do* default on
their own-currency debt. **Russia in August 1998** defaulted on
its domestic ruble-denominated GKO bonds because, although it
could have printed rubles to pay, the cost (collapsing the FX
peg, hyperinflation, banking-system implosion) was judged worse
than the default. **Argentina** has serially defaulted on
peso-denominated debt; **Mexico's 1982 "tequila"** crisis
included a forced restructuring of dollar *and* peso obligations.
"Print to pay" is a *political* choice, not a mathematical
guarantee. The US specifically has its **AAA stripped three
times**: S&P in August 2011 (debt-ceiling brinksmanship), Fitch
in August 2023 ("erosion of governance"), Moody's in May 2025
(rising debt burden and persistent fiscal deficits). Treasuries
are still the deepest, most-liquid sovereign bond on earth and
still the global reserve collateral asset — but "riskless" was a
20th-century shorthand that no longer survives literal
inspection. *Default by inflation* is the more realistic
scenario for any sovereign with debt in its own currency: pay
back the nominal dollars, just dollars worth less.

**Misconception 2: "If I hold to maturity, I can't lose."**

In *nominal* terms, yes — you get face plus coupons back. But the
real value of those payments depends on inflation between purchase
and maturity. A 30-year bond bought at 2% in 2020 is contractually
locked in to deliver a real loss if inflation averages 3% over the
holding period. Holding to maturity protects you from price
volatility, not from inflation. (We come back to *where* the
price volatility comes from — duration and yield-curve moves —
properly in **Week 31** on the yield curve and **Week 32** on
duration & convexity. For Level 1 the rule of thumb in §2.4 is
enough: longer maturity = more price swing per 1% yield move.)

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
When you buy a corporate bond instead of a Treasury, you are not
just collecting "a bit of extra yield" — you are *taking on the
risk that the company defaults*, and the extra yield (the credit
spread) is the market's price for that risk. Functionally, that
makes the corporate-bond holder the *seller of default insurance*
to the company: the company pays you the extra yield each year
(the "insurance premium"), and in exchange, *if* the company goes
bust, you eat some of the loss (the "insurance payout"). It is
the same risk pattern an insurance company sees on a fire policy:
lots of small premiums collected, and once in a while a house
burns down and they pay out a big claim.

That shape of payoff — small wins most of the time, occasional
large losses — is what "**negatively skewed**" means in plain
language. Picture the distribution of annual returns: it has a
short fat right side ("normal year, +1.5% extra") and a long
thin left tail ("crisis year, -15%"). The *average* return is
positive, but most of the bad-year losses are bigger than any
single good-year gain. So selling credit insurance is not free
yield; it is paid risk-taking, and the years where it costs you
are exactly the years your equity sleeve is *also* down. That's
why the diversification job in 60/40 belongs to Treasuries, not
corporates.

**Misconception 6: "Long bonds have higher yields, so they're
better."**

Longer maturity earns the *term premium* — but with much higher
duration risk. The Sharpe ratio of long Treasuries is comparable
to or *worse* than that of intermediate Treasuries over most
historical windows. Reach for the term premium only if you have
a specific liability that matches that maturity, or you are
explicitly making a **duration bet** (deliberately overweighting
long bonds because you think yields will *fall*, which would push
long-bond prices up sharply via their high duration; the inverse
bet is to *avoid* long bonds because you think yields are
heading higher — the 2020 "buy TLT" investor discovered the wrong
side of this in 2022). And note: "just roll short bonds into long
bonds" sounds free but isn't. When the yield curve is *inverted*
(short yields > long yields), as it was for most of 2022-2024,
rolling short into long actually *gives up* yield. We cover the
curve shape and the term-premium story properly in **Week 31**.

**Misconception 7: "Inflation-protected bonds (TIPS) are always
better than nominal bonds."**

TIPS are better when inflation surprises *upward* relative to the
breakeven rate priced into them. They are worse when inflation
surprises downward, or when the breakeven is expensive. TIPS are a
*relative* trade against nominal Treasuries, not a free upgrade.
Two extra points worth absorbing: (i) TIPS index to *official*
CPI — so they protect against the CPI methodology used by the
BLS, not necessarily against the actual cost-of-living change you
feel (recall the Week 1 ShadowStats discussion); (ii) when CPI
prints high and the Fed responds by hiking rates, TIPS take
duration losses that partially or fully offset the
inflation-accrual gains — TIPS *lost money* in 2022 even though
inflation was at multi-decade highs, because the rate-hike
response drove their real yields up sharply. (§2.9 covers the
mechanics; §Q4 walks the breakeven calculation.)

**Misconception 8: "Negative-yield bonds make no sense and no one
should buy them."**

European and Japanese institutional investors held trillions of
dollars in negative-yielding bonds during 2014-2021. Some of that
demand was voluntary (price upside if rates went *more* negative;
FX-hedged carry that was positive once you hedged dollars back to
euros), but a meaningful chunk was effectively *forced*: bank,
insurance, and pension regulation in the EU (Solvency II for
insurers, Basel III LCR for banks) requires institutions to hold
a minimum amount of high-quality liquid assets — which in
practice means sovereign bonds — regardless of the yield, and
liability-matching pension funds discounting at long real rates
are obliged to hold matched-duration bonds even at negative
yields. So "it makes no sense for me as a retail investor" is
correct (you can just hold cash); "it makes no sense for anyone"
is wrong. Notice the asymmetry: regulated institutions can be
*compelled* into a trade you can walk away from — one of the
structural retail advantages we'll come back to in later levels.

---

### 4. Q&A Section

**Q1: I want monthly income from bonds. What's the cleanest way?**

A: Build a *bond ladder* — buy individual Treasuries or TIPS
maturing in each of the next 5-10 years, equal-weighted. Each
year one rung matures and you reinvest at the then-current yield.
Cash flow is roughly the average yield × portfolio value. Avoids
fund duration drift and gives you a predictable schedule. The
brokerage tools at Fidelity, Schwab, and Vanguard let you
click through the mechanics in 15 minutes — but before you
place orders, *check each line*: bid/ask spread (corporates can
be wide; Treasuries are tight), callable status (a callable bond
is not a true ladder rung — the issuer can take it back early),
the exact maturity date (line up with when you actually need
the cash), tax treatment (Treasury interest is state-tax-exempt;
munis are federal-tax-exempt; corporates are fully taxable), and
minimum lot size (some bonds trade in $5,000 or $10,000 minimums
that won't fit a small ladder evenly).

**Q2: Should I buy individual bonds or bond ETFs?**

A: Treat Treasuries and corporates differently.

- **Treasuries.** Modern brokers (Fidelity, Schwab, Vanguard,
  Interactive Brokers, plus TreasuryDirect) make individual
  T-bills, notes, and bonds cheap and liquid even for small
  accounts — bid/ask is tight and there are no fund expense
  ratios. For a buy-and-hold ladder you can comfortably go
  individual at any account size.
- **Corporates.** Individual corporate bonds have wide bid/ask
  spreads, thin secondary-market liquidity, and meaningful
  single-issuer default risk. For retail accounts of essentially
  any size, an ETF (LQD investment-grade, HYG/JNK high-yield) is
  the better tool.
- **Bond funds in general.** ETFs (BND, AGG, IEF, TLT, SHY) buy
  you instant diversification and a constant-duration sleeve.
  The cost is the duration-drift problem from Misconception 3:
  the fund never matures, so you can't "hold to maturity" your
  way out of a price drawdown. For a specific future cash need,
  match an individual Treasury to the date.

**Q3: What's the right bond duration for me?**

A: Roughly match your investment horizon. 1-3 year Treasuries (SHY)
for money you need within five years. Intermediate (IEF, ~7 yr) for
the diversifier sleeve in a 60/40-style portfolio. Long bonds (TLT,
~20 yr) only as a deliberate **duration bet** — buying long
bonds *because* you expect yields to fall and want the
high-duration price gain that produces, *not* as a sleepy
default. The 2022 lesson: duration is a *loaded* dimension; don't
accidentally take more than you intended.

**Q4: How is a TIPS different from a regular Treasury?**

A: A TIPS' principal adjusts upward with CPI. The coupon rate is
fixed but applies to the inflation-adjusted principal, so dollar
coupons grow with inflation too. The "real yield" you see quoted
on TIPS is the yield *above* CPI. The **breakeven inflation**
rate is the difference between the nominal Treasury yield and the
TIPS real yield at the same maturity — if realised CPI over the
holding period exceeds breakeven, TIPS win; if it falls short,
nominals win. (April 2026: 10-year nominal ~4.2%, 10-year TIPS
real ~1.8%, so 10-year breakeven ~2.4%. TIPS win the next decade
if average official CPI is above 2.4%.)

Three honest caveats. First, the CPI those bonds index to is the
same *official* BLS series we picked apart in Week 1 — hedonic
adjustments, geometric-mean weighting, owner-equivalent rent —
so TIPS protect against the *measured* number, not necessarily
your grocery bill. Second, when CPI rises and the Fed hikes
rates in response, TIPS take *duration losses* that partially
offset the inflation-accrual gains, which is exactly why TIPS
lost money in 2022 even with inflation at multi-decade highs.
Third, historically the breakeven has been a **roughly unbiased
but noisy** forecast of subsequent CPI: it tracks the long-run
direction but routinely misses by 1-2 percentage points, and
during liquidity stress (Q4 2008, March 2020) the breakeven
temporarily collapses to absurd levels because TIPS are far
thinner than nominals. Treat the breakeven as the market's *best
central estimate*, not as a precise forecast.

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
*inverted* curve — it has historically been one of the most
reliable recession leading indicators, with a 12-24 month lead.
The inversion warning fired before each of the 1990, 2001, 2008,
and 2020 recessions; it also pre-dates the early-1980s Volcker
recessions. The most famous recent precedent is the inverted
curve from mid-2006 through mid-2007, with the recession landing
late-2007.

*As of April 2026* (this paragraph will age), the curve has just
*un*-inverted after a record-long inversion that began in mid-
2022. Historically the recession often arrives *after* the
un-inversion, not during the inversion itself, so "the curve is
back to normal" is *not* an all-clear. Whether the post-inversion
recession is off the table or merely delayed is the live debate;
by the time you read this, the answer may already be in.

This is genuinely the most-traded "signal" in fixed income, and
Level 1 only scratches the surface. **Week 31** does the full
yield-curve lesson — level / slope / curvature, what *each* shape
is telling you, why segments of the curve trade differently, and
how to read the curve in real time. For now: know the shape,
know that an inversion is the warning, and use the Week 10
economic-cycles dashboard for the live read.

**Q7: What is "convexity" in one sentence?**

A: The bend in the price-yield curve — the higher-order term that
makes price gains from falling rates larger than price losses from
the same-size rising rates. Long bonds and zero-coupon bonds have
the most convexity. It's a free option that gets paid for via
slightly lower yield. Week 32 unpacks it formally.

**Q8: Are corporate bonds a substitute for Treasuries in 60/40?**

A: No. Corporate bonds have meaningful equity-correlation in
crises (the realised-excess-return chart in §2.7 makes this
concrete) and so they don't deliver the negative correlation that
Treasuries give you in a flight-to-safety event. If you want
yield, take it on the *equity* side; keep the bond sleeve in
Treasuries for the diversification job.

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

A: Week 4 used Treasuries as a black box; this week opens the
box. Week 15 (multi-asset / four-tranche / the barbell shape)
chooses *short* Treasuries over long for the safe sleeve based
on §2.4 — you take the rate-cut diversification benefit without
absorbing 20-year duration shocks like 2022. Week 18 covers
Fed-vs-market interest rates and how they cascade into asset
prices. **Week 31 is the full yield-curve lesson** (level,
slope, curvature, inversion mechanics in detail). **Week 32**
is the rigorous duration and convexity math (key-rate durations,
convexity adjustment, OAS). **Week 33** is the credit lesson
(rating mechanics, IG vs HY, structured-credit tranching, CDS).
**Week 34** is rate-sensitivity across asset classes (the 2022
case study end-to-end). Week 47 and 50 cover long-volatility /
managed-futures overlays that hedge the inflation tail that
bonds can't.

The interactive panel below lets you slide the four-number bond
contract (face, coupon, maturity, payment frequency) and the
market yield, and watch the price recompute live. The chart shows
the price-yield curve from 0% to 15% with your current point
marked. Watch the curvature change as you increase maturity — the
30-year line is dramatically more convex than the 2-year. Macaulay
and modified duration are reported below the chart.

*If you are reading this on a device or in a context where the
interactive panel can't render, the static chart below shows the
same relationship for representative 2-year, 10-year, and 30-year
bonds at a 4% coupon — longer maturity is a steeper, more bowed
curve, which is duration and convexity made visible.*

![Price-yield curves for 2-, 10-, and 30-year 4% semi-annual coupon bonds, plotted from 0% to 15% market yield. All three curves cross at price = par when yield = 4%. The 30-year curve is dramatically steeper and more convex than the 2-year curve, which appears almost linear at this scale — a visual demonstration of why long bonds carry more duration and more convexity than short ones.](image/week05_price_yield.png)

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

**[SEGMENT 6: CREDIT RATINGS — THE LETTERS THAT LIE TO YOU]**

**Horace:** Quick segment before we look at the chart. When a
company issues a bond, three rating agencies — Moody's, S&P,
Fitch — stamp it with a letter grade. Triple-A at the top.
Down through double-A, single-A, triple-B. That's the bottom of
*investment grade*. Below that is *speculative* or *junk*.

**Stella:** And the chart we're about to look at uses BAA?

**Horace:** Right. BAA is just Moody's spelling for the lowest
investment-grade rung. S&P writes the same thing as BBB.

**Stella:** OK. So I should trust those letters?

**Horace:** Funny you ask. The agencies are paid by the company
*issuing* the bond, not by you, the buyer. The issuer goes
shopping for the best rating it can get. That conflict of
interest has blown up several times. Enron carried
investment-grade ratings until four days before bankruptcy.
Lehman was rated single-A on the morning it failed in 2008. The
entire 2008 housing crisis was driven by tens of thousands of
subprime mortgage securities stamped triple-A and then losing
60 to 100 percent of value. Greek government debt was
investment-grade right up until it traded at 30 cents.

**Stella:** So the rating means nothing.

**Horace:** Not nothing. It's a rough sort. But the *yield
spread* — what real traders are paying to lend to that issuer
right now — is the live signal. When the spread blows out while
the rating is still investment grade, the market is telling you
the rating is wrong. Read the spread, not the letter.

---

**[SEGMENT 7: CREDIT — YIELD SPREAD VS REALISED EXCESS RETURN]**

[VISUAL: image/week05_credit_spreads.png]

**Horace:** A US Treasury is the textbook default-free asset.
Anything else is riskier. The market prices that extra risk by
demanding a higher yield. The *yield difference* — BAA corporate
yield minus 10-year Treasury yield, or option-adjusted spread on
an investment-grade index — that is the credit spread proper.
It's quoted live every day in basis points, and it widens *upward*
when things break.

**Stella:** Okay. So what's this chart?

**Horace:** Different number. Pay attention. This is *realised
annual excess return* — BAA corporate total return minus 10-year
Treasury total return, year by year, since 1928. Same data
family, different question. The yield spread tells you what
traders are pricing today. The bars on this chart tell you what
a buy-and-hold investor actually *earned* holding corporates
instead of Treasuries each year.

**Stella:** And the long-run mean?

**Horace:** Small and positive. About 1 to 2 percent per year on
average. That is the realised credit premium investment-grade
corporate debt has paid above Treasuries over the last century.

**Stella:** And the spikes?

**Horace:** 1932. 1974. 2008. 2020. The four worst credit blow-ups
of the modern era. In each one, yield spreads blew *out* —
upward — corporate prices got marked *down*, and Treasuries
rallied on the flight-to-safety bid. So realised excess return
for that year goes sharply negative on this chart. Corporates
underperformed Treasuries by 10 to 25 percent in a single year.
Fat left tail.

**Stella:** So selling credit insurance...

**Horace:** ...is a structurally negatively-skewed payoff. Steady
small income, rare large losses. Not free yield.

One caveat on this chart: it's annual. Don't use it as a
timing tool. Daily yield spreads can move ahead of equity
bottoms during a credit cycle, and traders watch them live for
exactly that reason. The annual realised-return chart you're
looking at here is too coarse for that job; it tells you the
shape of the long-run payoff, not when the next blow-up starts.

The retail takeaway: hold Treasuries for the diversification
job, not corporates. If you want yield, take it on the equity
side.

---

**[SEGMENT 8: THE FORTY-YEAR BULL MARKET AND THE 2022 BREAK]**

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

**Stella:** Can yields keep grinding higher from here?

**Horace:** That's the live question. The argument for *higher
for longer* is mechanical. US federal debt is around 120 percent
of GDP. Deficits are running 6 to 7 percent of GDP in peacetime.
And every year the Treasury has to roll over trillions of dollars
of old debt. When a 10-year note issued in 2020 at 0.7 percent
matures in 2030, the Treasury has to refinance it at whatever the
10-year is *that* day. So the average interest rate the
government pays grinds higher year by year. The federal interest
bill has already crossed a trillion dollars annually — more than
the defence budget. That's not a forecast, that's accounting. It
puts upward pressure on the supply of new bonds and downward
pressure on Treasury prices. And the rating agencies have noticed:
S&P pulled the AAA in 2011, Fitch in 2023, Moody's in 2025.

**Stella:** What's the lesson?

**Horace:** This is the regime point, and it isn't original to me.
Howard Marks wrote a memo called *Sea Change* in December 2022
laying out exactly this argument. Ray Dalio's *Changing World
Order* makes the longer-cycle version. Lyn Alden's *Broken Money*
makes the monetary-plumbing version. Druckenmiller has been
shouting about the deficit version since 2022. Different lenses,
same conclusion: the rate regime that made buy-and-hold look easy
is over, or at minimum no longer the safe default.

We have been forty years inside a regime that made passive index
investing look like a free lunch. The regime had a specific macro
signature: falling yields, rising bond prices, expanding equity
multiples, benign correlation between the two. The trigger that
breaks the regime is a *sustained* rise in long yields. We are
watching that trigger fire right now.

It is too early to say the regime is over. It is too late to
pretend nothing has changed. The bond chart is the regime backdrop
to everything else we cover from Week 31 onward.

---

**[SEGMENT 9: TIPS, FLOATERS, AND THE BOND-MARKET PLUMBING]**

**Horace:** Two more pieces and we're done. First: not every
bond is a fixed-rate nominal bond. The two variants you'll meet
fastest as a retail investor are TIPS and floaters.

TIPS — Treasury Inflation-Protected Securities — have a principal
that indexes to CPI. So your dollar coupons grow with inflation.
The yield quoted on a TIPS is the *real* yield, above CPI. The
difference between the regular Treasury yield and the TIPS yield
at the same maturity is the *breakeven* — the inflation rate the
market is pricing in. If actual inflation comes in higher than
breakeven, TIPS win. Lower, nominals win. Two warnings: TIPS
index to *official* CPI, which we already saw in Week 1 has its
own problems, and TIPS lost money in 2022 even with high
inflation because the Fed hiked rates and the duration loss
wiped out the inflation accrual. They're a *relative* trade
against nominals, not a free upgrade. Worth knowing: Canada
stopped issuing new inflation-protected bonds in November 2022
citing weak demand at auction — a useful reminder that even the
sovereign can pull inflation protection off the menu.

Floaters — floating-rate notes — reset their coupon to a
benchmark like SOFR every quarter. So when rates move, the
coupon moves with them and the price barely changes. You're
trading duration risk for reinvestment risk. Floaters were the
right bond to own in 2022 and the wrong bond to own in 2024 once
rates peaked.

**Stella:** And callable, convertible, perpetual...

**Horace:** All real, all add complications, all in the reading
section. Headlines: *callable* means the issuer can redeem
early when rates fall — that's the issuer's option, you wrote
it, so callable bonds yield more. *Convertibles* bundle a bond
with an equity call option — we'll meet those properly in the
options weeks. *Perpetual bonds* never mature — the UK's old
*consols* ran for over 250 years. *Century bonds* run 50 to 100
years — Argentina issued a 100-year US-dollar bond in 2017 and
defaulted on it three years later, which tells you everything
about reaching for yield on long sovereign credit.

**Stella:** Last piece?

**Horace:** How retail actually owns bonds. Almost nobody buys
individual corporates. The bid-ask is wide, the lots are big,
and single-name default risk is real. So retail buys ETFs. LQD
for investment grade, HYG for high yield, BND or AGG for the
broad market. Those solve the diversification problem but
introduce one of their own: most bond indices are *weighted by
amount of debt outstanding*. The biggest weight goes to the
issuer that has *borrowed the most*. That is structurally
different from market-cap-weighted equities, where the biggest
weight goes to the company the market values most. "Buy a
bond ETF and forget it" is not as benign a default as the same
strategy in stocks. Worth knowing.

---

**[SEGMENT 10: THE INTERACTIVE]**

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
is the linear sensitivity. Credit spread is what the market
charges you for taking default risk — small steady premium most
years, big losses in the bad ones, just like writing insurance.
Ratings give you a rough sort but the spread tells you the
truth. The forty-year bull market is the regime that built passive
investing's reputation, and it ended in 2022.

That's the entire bond universe in one paragraph. We will spend
Week 31 on the yield curve, Week 32 on the deeper duration math,
Week 33 on credit, and Week 34 on rate sensitivity across asset
classes. Tonight, slide the interactive until the four-number
contract feels obvious.

**Stella:** Next week?

**Horace:** Gold — the five-thousand-year store of value. Why it
sits in a portfolio at all when it doesn't pay you a coupon or
earn an ROE, and what's actually different about a gold ETF, a
gold futures contract, and a coin in your safe.

---

**END SCREEN:** "Next: Week 6 — Gold: The 5,000-Year Store of Value"
