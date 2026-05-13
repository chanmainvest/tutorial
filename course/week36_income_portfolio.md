# Week 36: Building an Income Portfolio — the L3 Capstone

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Every other week in this tutorial has assumed you are accumulating —
working, saving, and compounding. This week assumes the opposite. You
have the pile. Now you need it to *pay you*. Whether that pile funds
retirement at 65, supports a partner who stopped working, or simply
covers the tuition cheque that arrives every September, the moment you
flip from accumulation to distribution the optimisation problem
changes shape entirely. You stop optimising for terminal wealth and
start optimising for *cash that lands in the chequing account on
schedule, after tax, with the smallest possible chance of running out*.

Four reasons this matters as the capstone for the L3 income block.

1. **Income is mechanically harder than growth.** A growth portfolio
   only has to compound. An income portfolio has to compound *and*
   produce reliable cash *and* survive a bad first decade — the
   "sequence-of-returns risk" that the famous 4% rule was invented to
   answer. We will explain why the 4% rule is correct in spirit and
   misleading in detail in 2026.
2. **Sources of yield are not interchangeable.** A 5% Treasury coupon,
   a 5% qualified dividend, a 5% REIT distribution, and a 5%
   covered-call premium look identical on a brokerage statement and
   are radically different products. They have different default
   risks, different inflation sensitivities, different drawdown
   profiles, and — most expensively — different tax treatments. A
   portfolio that ignores the difference can lose 30% of its
   *spendable* yield to the IRS for no good reason.
3. **The hierarchy of after-tax yield is the single biggest lever you
   control.** Tax efficiency is the explicit anchor. In the 32% federal
   bracket, a qualified dividend keeps about 80 cents of every dollar.
   A bond coupon keeps about 63 cents. A short-term option premium
   keeps the same 63 cents — sometimes less, depending on state. The
   *order* in which you fill your taxable, IRA, and Roth accounts with
   these income streams is worth more than picking better individual
   tickers ever will be.
4. **The four-tranche framework and the barbell
   need a distribution-side translation.** During accumulation, the
   four tranches govern *how you allocate*. During distribution they
   govern *which sleeve you draw from this quarter*. The income
   capstone is what stitches everything from Weeks 4-5 (60/40 and
   bonds), Weeks 14-15 (pair trades and barbell), and Weeks 26-28
   (options as orders) into a single cash-producing machine.

This lesson lays out the four real income sources, the after-tax
ladder, the canonical product menu (SCHD / VYM / DVY / SPYI for
dividend equity, BND / VTEB / PFF for fixed income, VNQ for REITs,
JEPI / JEPQ for premium-write), the 4% rule and its 2026 critique, and
ends with two model portfolios — one taxable, one tax-advantaged —
that target a 4-5% sustainable yield with bond-like volatility.

---

### 2. What You Need to Know

#### 2.1 The Four Real Sources of Portfolio Income

Strip away every product wrapper and there are only four ways a US
portfolio actually produces cash. Memorise this list. Every yield ETF
ever launched is some packaging of these four ingredients.

1. **Treasury coupons.** The US government promises to pay. Default
   risk is rounded to zero. State and local income tax do not apply.
   Federal tax applies at ordinary rates. The 2-year Treasury is the
   floor your safe sleeve cannot reasonably go below; the 10-year is
   the duration anchor for a balanced portfolio.
2. **Investment-grade and high-yield corporate coupons.** Companies
   pay you to lend to them. IG (LQD, AGG's corporate slice, BND's
   corporate slice) yields 80-150 bps above Treasuries. HY (HYG, JNK)
   yields 250-450 bps above. Both pay ordinary income at the federal
   *and* state level, which is critical when you compute after-tax.
3. **Qualified dividends.** Long-held common stock dividends meeting
   the IRS holding-period test are taxed at long-term capital-gains
   rates: 0/15/20% federal depending on bracket, plus state. The
   S&P 500 yields about 1.4% as of April 2026. Curated dividend ETFs
   (SCHD, VYM, DVY) yield 2.5-3.7%. The premium over the index is
   compensation for tilting toward "boring" sectors — staples,
   healthcare, financials, industrials — and away from the cap-light
   compounders that drove the post-2020 rally.
4. **Option premium.** Selling calls or puts (Weeks 26-28) creates
   short-term income. With near-zero exception, equity-option premium
   is taxed as short-term capital gains at the federal *and* state
   level. The headline distribution yields on JEPI (~7-8%), QYLD,
   PUTW, SPYI, and the entire buy-write fund family are large
   precisely because the IRS gets a big bite first.

A fifth category you will see in marketing — REIT distributions —
is partly category 2 (the REIT pays through interest and rent
collected) and partly category 3 (qualified dividends from any equity
holdings). REITs as a wrapper get a 20% Section 199A deduction at the
investor level since 2018, which makes them somewhat tax-friendlier
than raw bond coupons but still meaningfully worse than qualified
dividends.

The yield-hierarchy chart shows the *headline* (pre-tax) numbers as of
April 2026. Read it as the menu before tax.

![Bar chart of pre-tax yield by income source as of April 2026: 2-year Treasury 3.9%, 10-year Treasury 4.2%, LQD (IG corporate) 5.0%, HYG (high-yield corporate) 7.5%, S&P 500 dividend yield 1.4%, VYM 2.9%, SCHD 3.6%, VNQ 3.8%, JEPI 7.8%. Bars are coloured by tax category — Treasuries blue, corporates red, qualified-dividend equity green, REITs purple, option-premium gold — to preview the after-tax sort that comes next.](../image/week36_yield_hierarchy.png)

#### 2.2 The After-Tax Hierarchy and Why It Reverses the Menu

Pre-tax, JEPI's 7.8% looks like the obvious winner. After tax in a
taxable account at the 32% federal bracket plus 5% state, the picture
inverts. The next chart applies the right tax rate to each line item:

- Treasury coupons: 32% federal, 0% state ⇒ 32% effective.
- IG / HY corporate coupons: 32% + 5% = 37% effective.
- Qualified dividends (S&P 500, SCHD, VYM, DVY): 15% federal LTCG +
  5% state = 20% effective.
- REIT distributions (VNQ): 37% combined, but the 199A deduction
  reduces the *taxable* portion to 80%, giving roughly 29.6%
  effective.
- Option-premium ETFs (JEPI/QYLD/SPYI): 32% + 5% = 37% effective.

After-tax, SCHD's 3.6% becomes 2.9%. JEPI's 7.8% becomes 4.9%. The
11-bp gap on the y-axis is much smaller than it looked. And after you
adjust for option-premium ETFs' historical underperformance versus
their underlying index (Week 27, QYLD vs QQQ; Week 28, PUTW vs SPY),
the apparent yield premium is mostly a tax leak you are paying *to
yourself*.

![After-tax yield bars at the 32% federal + 5% state bracket: Treasuries lose 32% of yield (2-year drops to 2.7%, 10-year to 2.9%), corporate coupons lose 37%, qualified-dividend equity keeps 80% (SCHD drops only from 3.6% to 2.9%), REITs lose ~30%, option premium loses 37% (JEPI drops from 7.8% to 4.9%). The chart shows a hierarchy: qualified dividends keep the most of their yield, option premium and corporate coupons keep the least.](../image/week36_tax_adjusted.png)

The operational rule that falls out:

- **Hold qualified-dividend equity in the taxable account** — the
  preferential rate is the whole point.
- **Hold option-premium and HY-corporate sleeves in the IRA / 401(k)** —
  the IRS bite gets deferred (traditional) or eliminated (Roth).
- **Hold Treasuries in the taxable account if you live in a high
  state-tax state** (CA/NY/HI) — the state exemption is a free 5%.
- **Hold REITs in the IRA** if your bracket is high enough that the
  199A deduction does not fully offset your state rate.

This is location, not allocation. It is one of the few free lunches
the US tax code gives you.

#### 2.3 The Canonical Product Menu

Theory only matters if you can implement it with three or four
tickers at a Vanguard, Fidelity, or Schwab account. Here is the
April-2026 product menu by sleeve.

**Dividend equity (qualified yield, growth-of-income).**
- `SCHD` — Schwab US Dividend Equity. ~100 holdings, 10-year
  dividend-growth screen, sector-balanced toward industrials,
  staples, healthcare. Yield ~3.6%, expense ratio 6 bps.
- `VYM` — Vanguard High Dividend Yield. ~440 holdings, market-cap
  weighted within the high-yield half of the index. Yield ~2.9%,
  ER 6 bps.
- `DVY` — iShares Select Dividend. ~100 holdings, value-heavier than
  SCHD. Yield ~3.4%, ER 38 bps.
- `SPYI` — NEOS S&P 500 High-Income. Index-tracking with a partial
  call-write overlay; positions itself as a hybrid of dividend equity
  and option premium. Yield ~12% headline but the option-premium
  share inherits the option-premium tax problem.

The yield ladder is real. SCHD sits in the middle of the ladder by
design — the dividend-growth screen filters out the highest-yielding
names that are in distress. That is a *feature*, not a bug, and is
why we treat SCHD as the default dividend sleeve for the model
portfolio in §2.6.

**Fixed income.**
- `BND` — Vanguard Total Bond Market. Treasuries + IG corporates +
  agency MBS, intermediate duration ~6 years. The default core bond.
- `VTEB` — Vanguard Tax-Exempt Bond. Investment-grade municipals.
  Tax-equivalent yield rises sharply for high-bracket investors in
  taxable accounts; this is the right tool for the bond sleeve in a
  taxable account if your federal bracket is 32% or higher.
- `PFF` — iShares Preferred & Income Securities. Preferred stock,
  yields 6-7%, but most preferreds are issued by financial firms so
  this sleeve is a bet on bank credit risk, not a pure bond.
- `TLT` / `IEF` — long and intermediate Treasury duration tools when
  you want pure interest-rate exposure separated from credit.

**Real assets / inflation hedge.**
- `VNQ` — Vanguard Real Estate. The REIT sleeve. Yield ~3.8%,
  inflation sensitivity comes through rent escalators and replacement-
  cost equity in real estate.
- `SCHH` — cheaper REIT alternative, similar profile.

**Option premium (Weeks 26-28).**
- `JEPI` — JPMorgan Equity Premium Income. ~80% defensive low-vol
  equity + ~20% equity-linked notes that synthesise call-write
  premium. Yield ~7-8%, ER 35 bps. The single largest fund in the
  category.
- `JEPQ` — Nasdaq cousin of JEPI. Higher volatility, higher yield,
  closer to QYLD's payoff shape but with active selection on the
  equity sleeve.
- `QYLD` / `XYLD` / `RYLD` — passive monthly at-the-money buy-write
  on QQQ / SPY / IWM. Pure call-write exposure; the cap-on-upside
  is severe (Week 27).
- `PUTW` / `WTPI` — systematic put-write ETFs. Mirror image of
  buy-writes; cap-on-upside replaced with cushion-on-downside (Week 28).

#### 2.4 The 4% Rule and Why It Needs an Update for 2026

Bengen (1994) and the Trinity study (1998) gave retirees the most
quoted rule of thumb in finance: with a 60/40 portfolio, you can
safely withdraw 4% of the *initial* balance, increase that dollar
amount by inflation each year, and have a 95%+ chance of not running
out over a 30-year retirement. The rule is based on rolling 30-year
windows of US data 1926-1995.

Three things have changed.

1. **Bond yields started Bengen's window above 7% and a typical
   retirement window started above 5%.** The 2010-2021 zero-rate
   regime crushed the bond contribution to 4%-rule sustainability.
   Updates by Pfau and others put the safe withdrawal rate as low as
   2.8% for portfolios *starting* in 2010-2020. The 2022-2024 yield
   reset has lifted that back to roughly 3.5-3.8%. April 2026 is the
   first time since 2008 that the math works close to the original
   number again, but it is not 4%.
2. **Sequence-of-returns risk dominates.** A retiree drawing 4%
   through 1973-1974 (60/40 down a real ~30%) ran out of money in
   roughly year 22. A retiree drawing 4% through 1995-1999 (60/40 up
   a real ~140%) finished with roughly ten times the starting
   balance. The same rule, the same numerical sequence, the same
   asset mix — totally different lived experience.
3. **Variable-spending rules dominate fixed-real spending.** Guyton-
   Klinger guard rails, the Bogleheads' "spend a percent of current
   balance," and Vanguard's "dynamic spending" all beat the rigid 4%
   rule by 50-100 bps of safe withdrawal in Monte-Carlo, with
   essentially no behavioural cost. This week's interactive uses a
   simplified version: target 4-5% of *current balance*, with a hard
   floor and ceiling.

The honest April-2026 number for a 60/40 portfolio with no
discretionary-spending flexibility is roughly 3.7%. With the
flexibility to cut 10-15% in bad years, 4.5%. The model income
portfolio in §2.6 is engineered around that 4-5% target.

#### 2.5 The Distribution-Side Four-Tranche Framework

The four tranches in accumulation translate cleanly to
distribution. The same buckets exist; the *direction of cash flow*
reverses.

| Tranche | Accumulation purpose | Distribution purpose |
|---|---|---|
| 1. Cash / T-bills | Emergency fund | 1-2 years of spending, the "no-sell zone" |
| 2. Bonds | Volatility ballast | 5-7 years of spending; refilled from sleeve 3 in good years |
| 3. Diversified equity | Compounding engine | The wealth machine; refills sleeve 2 |
| 4. Concentrated bets | Asymmetric upside | Optional yield overlays (JEPI, premium-write) |

The barbell is the cross-section: short-duration safe
income on one end (T-bills, 2-year Treasuries, VTEB if taxable), and
long-duration real assets on the other (VNQ, equity dividend growers,
optional premium overlay). The middle — long-duration intermediate
Treasuries — is the *least* useful sleeve in a distribution portfolio
relative to the two ends, because it has neither the nominal-rate
sensitivity that long Treasuries give nor the inflation pass-through
that equities and real estate give.

The interactive in §2.7 is the live version of this. You set the
five-sleeve mix and get blended yield, after-tax yield (with bracket
toggle), expected volatility, and expected drawdown.

#### 2.6 Two Model Portfolios

Two reference points. Both target a 4-5% pre-tax distribution yield
with bond-like volatility (8-10% annualised standard deviation).
Both are buildable today at any major US broker for under 12 bps in
weighted expense ratio.

**Model A — Taxable, 32% federal bracket.**

| Sleeve | Ticker | Weight | Yield | Rationale |
|---|---|---:|---:|---|
| Dividend equity | SCHD | 35% | 3.6% | Qualified dividends, low ER, sector diversity |
| Dividend equity | VYM | 10% | 2.9% | Adds breadth, market-cap weight |
| Tax-exempt bonds | VTEB | 25% | 3.4% (≈5.0% TEY) | Federal exempt; lifts after-tax yield substantially |
| REITs | VNQ | 10% | 3.8% | Inflation pass-through; 199A partial relief |
| Treasuries | IEF (7-10yr) | 15% | 4.2% | State-tax-exempt anchor |
| T-bills | SGOV | 5% | 4.5% | Spending buffer |
| **Blended** | | **100%** | **3.7%** | After-tax ≈ 3.0% |

Volatility ~9% annualised; max-drawdown estimate -22% (1973-style
inflation shock or 2022-style dual decline). After-tax distribution
yield 3.0%; with a balance-of-portfolio variable-spending rule you can
sustain 4.0-4.5% real spending.

**Model B — Tax-advantaged (IRA / 401(k)), 32% bracket.**

| Sleeve | Ticker | Weight | Yield | Rationale |
|---|---|---:|---:|---|
| Dividend equity | SCHD | 30% | 3.6% | Qualified-dividend feature wasted; here for dividend-growth |
| Premium-write | JEPI | 15% | 7.8% | Highest pre-tax yield; tax irrelevant inside IRA |
| Total bond | BND | 25% | 4.6% | IG + Treasury blend |
| HY corporate | HYG | 10% | 7.5% | Credit premium; HY taxed punitively in taxable |
| REITs | VNQ | 10% | 3.8% | 199A irrelevant inside IRA |
| Cash | SGOV | 10% | 4.5% | Buffer |
| **Blended** | | **100%** | **5.1%** | After-tax = 5.1% (no tax inside) |

Volatility ~10% annualised; max-drawdown estimate -25%. The IRA
portfolio runs higher pre-tax yield because every income source is
taxed identically — so you load up on the punitively-taxed sleeves
exactly here, where the punishment does not apply.

The interactive lets you build either, and the bracket toggle shows
the Model-A and Model-B after-tax numbers side by side.

#### 2.7 The Live Builder

The interactive is a five-sleeve allocator: Treasuries, IG corporate,
qualified dividends, REITs, premium-write. It computes pre-tax yield
(weighted average), after-tax yield (weighted by tax category at the
selected bracket), expected volatility (square-root of weighted
covariance), and expected maximum drawdown (heuristic: 0.6 × peak
historical loss for each sleeve, blended by weight). The
tax-bracket toggle covers 12% / 22% / 32% / 37%, which is the four
brackets where real allocation decisions get made. Use it to verify
the §2.6 model portfolios; use it to test your own.

---

### 3. Common Misconceptions

1. **"High yield is always better."** No. Pre-tax yield without an
   after-tax conversion and a default-risk adjustment is
   marketing-grade arithmetic. JEPI's 7.8% in a taxable account at the
   37% bracket is 4.9%. SCHD's 3.6% in the same account is 2.9%. The
   gap is one-third of the headline.
2. **"Treasuries are tax-free."** Treasuries are *state*-tax-free. They
   are fully federally taxable. In Texas, Florida, or Tennessee that
   distinction is meaningless; in California or New York it is worth
   roughly 5% of the coupon.
3. **"Municipals are always better than Treasuries."** Only if your
   federal bracket × (1 - state rate adjustment) makes the
   tax-equivalent yield higher. At the 12% federal bracket, munis
   almost never win; at the 32% federal bracket, they almost always
   do.
4. **"Covered-call ETFs have free yield."** No. The yield is the
   pre-paid sale of upside (Week 27). Over a full cycle, JEPI and
   QYLD lag their unhedged underlyings by 300-500 bps annualised.
5. **"REIT dividends are qualified dividends."** Mostly false. Most
   REIT distributions are non-qualified ordinary income, partially
   sheltered by the 20% 199A deduction.
6. **"Dividend stocks are safer than the index."** Sometimes. The
   dividend-paying half of the S&P 500 has a lower beta than the
   index, but in a credit/financial crisis (2008) banks and REITs —
   which dominate dividend ETFs — drop further than the index.
7. **"You should reinvest dividends in retirement."** If you actually
   need the cash, no — that is buying with one hand and selling with
   the other, and creates avoidable tax in a taxable account.
8. **"4% withdrawal works in any market regime."** It works for the
   1926-1995 sample of US data. It has *failed* in retro-tested
   non-US samples and in zero-rate windows. April 2026 has the math
   close to working again; for low-flexibility retirees, plan for
   3.5-4.0%.
9. **"Bonds are always negatively correlated with stocks."** Week 4
   covered this in detail. The 1970s and 2022 are existence proofs of
   the opposite.
10. **"You should pick the sleeve with the highest yield first and
    fill in the others."** Backwards. Pick the sleeve with the
    highest *after-tax expected return per unit of drawdown
    contribution* first.

---

### 4. Q&A Section

**Q1: My broker is showing JEPI's "30-day SEC yield" as 8.4% but the
"distribution yield" as 7.6%. Which is right?**

Distribution yield is what landed in your account over the trailing
12 months divided by current price. SEC yield is a regulator-defined
forward-looking estimate based on the most recent month's cash flow,
annualised. For a stable holding, the two should be within 50 bps.
For premium-income funds where the option-premium varies with VIX,
the SEC yield can be misleading in either direction. Use distribution
yield for budgeting; use SEC yield for cross-fund comparisons.

**Q2: Should I buy individual bonds or BND?**

For amounts under roughly $100k of bond exposure, BND. The fund has
~10,000 bonds and you cannot replicate that diversification at retail
sizes. Above that, individual Treasuries on the auction market are
attractive — you control the maturity, you can ladder, and you skip
the 3 bp expense ratio. Individual *corporate* bonds at retail are a
trap: spreads are wide, liquidity is thin, and a credit event sinks
the position completely.

**Q3: What about a "60/40 of yield" — half qualified dividends, half
bond coupons?**

That is essentially Model A in §2.6. The distribution yield works out
to 3.7% pre-tax, ~3.0% after-tax in the 32% bracket. The volatility
is bond-like (~9%). For a baseline retiree-style portfolio that is
the right ballpark — but tilt the bonds toward VTEB if you are
taxable, and prefer SCHD over VYM for the dividend-growth tilt.

**Q4: Is the "yield-on-cost" metric useful?**

For pep-talk purposes, yes. For decisions, no. Yield-on-cost rises
because the price you paid is fixed and the dividend grows. It tells
you nothing about whether your *current capital* is generating an
adequate yield versus alternatives. Always compare current
distribution yields, not cost-basis yields.

**Q5: How do I know if a high yield is sustainable?**

Three quick screens. (a) Payout ratio: dividend / earnings under 70%
for industrials and staples, under 90% for utilities, under 95% for
REITs. (b) Free-cash-flow coverage: dividends plus buybacks under
free cash flow. (c) The fund's distribution history: did it cut in
2008, 2020, 2022? A buy-write fund cutting in 2022 is normal; an
equity-dividend fund cutting is a signal.

**Q6: What about preferred stock?**

PFF yields ~6.5% and feels like a bond. It is not. Preferreds are
junior to bonds, senior to common, and almost entirely issued by
banks and insurers. The 2008 crisis was a near-total wipe of bank
preferreds. Sized at 5-10% of a bond sleeve they are a fine yield
enhancer; sized at 30%+ they are a concentrated bank-credit bet.

**Q7: Should I use leverage on bonds (NTSX, RPAR, etc.)?**

Levered "stocks-and-bonds in the same fund" products amplify the
correlation assumption. They worked beautifully 1995-2021 and
melted down in 2022 when stocks and bonds fell together. They are an
accumulation tool, not a distribution tool. Do not use them for the
income sleeve.

**Q8: How often should I rebalance an income portfolio?**

Annually, plus a calendar-driven cash-refill of the spending-buffer
sleeve. The "smart" rule is: in a year where the equity sleeve is up
sharply, refill 18 months of spending into cash and bonds; in a flat
or down year, do not sell equities — draw from cash and bonds. This
is the four-tranche framework working in reverse.

**Q9: What about international dividend ETFs (VYMI, IDV)?**

Our default is US-only investable. International
dividend ETFs add concentration in financials and energy and
introduce withholding-tax leakage that takes a bite out of the
qualified-dividend rate. If you want non-US exposure, take it on the
*total-return* side of the portfolio (the equity growth sleeve), not
the income sleeve.

**Q10: Is there a fund-of-funds that does all of this for me?**

The closest is `VTINX` (Vanguard Target Retirement Income), `AOK`
(iShares conservative allocation), or `JAAA` + `JBBB` (Janus
Henderson AAA / BBB CLO funds for a credit-tilted income sleeve). All
of them solve part of the problem and none solve the
account-location problem in §2.2 — which is the largest source of
after-tax yield uplift available to you. Build it sleeve by sleeve.

**Q11: How much cash should I hold?**

For a retiree, 1-2 years of spending. For a working accumulator,
3-6 months. The reason for the asymmetry is the tail. A retiree who
is *forced* to sell equities at a 30% drawdown to fund this month's
groceries is destroying compounding more than any 1% cash drag could
cost. The cash sleeve is insurance against the bad-sequence tail.

**Q12: What about annuities?**

A single-premium immediate annuity (SPIA) at age 75-80 looks much
better than the 4% rule for *that portion* of the portfolio you
genuinely need to floor. The right framing is not "annuity vs no
annuity" but "what fraction of base spending does Social Security
cover, and do I need to top up the rest with a SPIA?" That is a
financial-planning question more than an investment one — and a
fine reason to talk to a fee-only fiduciary at the right age.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Building an Income Portfolio That Actually Pays You — the L3 Capstone (Week 36)

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

### INTRO

**[VISUAL: title card "Week 36 — Building an Income Portfolio"]**

**Stella:** Horace, this is the capstone of the income block. Weeks
4 and 5 we did 60/40 and bonds. Weeks 26, 27, 28 we did options as
limit orders. Now we put it all together. What's the one sentence?

**Horace:** Pre-tax yield is what gets advertised. After-tax yield is
what gets *spent*. And the gap is bigger than almost anyone realises.

**Stella:** And we're doing this in April 2026, with the yield
environment that finally makes the math work again.

**Horace:** Right. Two-year Treasury 3.9, ten-year 4.2, IG corporate
5, high-yield 7.5, S&P 500 dividend 1.4, SCHD 3.6, JEPI 7.8. That
menu has been *unobtainable* for almost a decade. We're not going
back to ZIRP for a while. So this is the lesson where we stop
optimising for terminal wealth and start optimising for cash that
lands in the chequing account on schedule.

**Stella:** Walk me through the four real income sources first, and
then we'll do the after-tax conversion that flips the menu upside
down.

---

### PART 1 — THE FOUR INCOME SOURCES

**[VISUAL: image/week36_yield_hierarchy.png]**

**Horace:** Strip every product wrapper off and there are exactly
four ways a US portfolio produces cash. Treasury coupons. Corporate
coupons — investment grade or high yield, the credit-risk ladder.
Qualified dividends from common stock. And option premium. That's
the menu. Everything else is packaging.

**Stella:** REITs?

**Horace:** REITs are a hybrid. Most of the distribution is non-
qualified ordinary income because it comes from rent, but a piece is
genuine qualified dividend from any stock the REIT operates as a
holding. The IRS gives them a 20% Section 199A discount on the
ordinary slice, which is why they sit between corporate coupons and
qualified dividends on the after-tax chart.

**Stella:** And the chart on screen — that's the pre-tax menu.

**Horace:** Yeah. Look at the bars. JEPI at 7.8 looks like the
champion. HYG at 7.5 looks great. SCHD at 3.6 looks middling. The
S&P 500 dividend yield at 1.4 looks irrelevant.

**Stella:** Now do tax.

---

### PART 2 — THE AFTER-TAX FLIP

**[VISUAL: image/week36_tax_adjusted.png]**

**Horace:** This is the same chart, after a 32% federal bracket plus
5% state. Treasuries lose 32% of their yield because they're
state-exempt. Corporate bonds lose 37% because they're not. Qualified
dividends — SCHD, VYM, S&P 500 — only lose 20% because they get the
LTCG rate. REITs lose around 30% after the 199A discount.
Option-premium funds — JEPI, QYLD, SPYI — lose the full 37% because
short-term option premium is short-term capital gain.

**Stella:** So JEPI 7.8 becomes...

**Horace:** 4.9%.

**Stella:** And SCHD 3.6 becomes...

**Horace:** 2.9%. The gap was 4.2% pre-tax. After-tax, in a taxable
account, the gap is 2.0%. You just paid the IRS 2.2 cents per dollar
of yield to *create* the apparent advantage.

**Stella:** And we haven't even gotten to JEPI lagging the S&P 500
by 300 to 500 bps a year on total return.

**Horace:** Right. That's a Week 27 conversation — the cap-on-upside
problem. After-tax yield *plus* total-return drag, and the JEPI
advantage in a taxable account is actually negative.

**Stella:** What's the operational rule that drops out?

**Horace:** Account location. Qualified-dividend
equity goes in the taxable account because the LTCG rate is the
whole point. Option-premium and high-yield-corporate sleeves go in
the IRA, where the IRS bite gets deferred or eliminated. Treasuries
go in the taxable account if you live in a high-state-tax state.
REITs go in the IRA at a high bracket. This isn't about *picking*
better funds. It's about *placing* them.

---

### PART 3 — THE PRODUCT MENU

**Horace:** Quick tour through the canonical product menu. You can
build the entire thing with eight tickers.

**Stella:** Dividend equity sleeve.

**Horace:** SCHD is the default. Schwab US Dividend Equity. About 100
holdings, 10-year dividend-growth screen, 6 bps expense ratio, 3.6%
yield. VYM is the breadth alternative — 440 holdings, market-cap
weighted, 2.9% yield. DVY is value-heavier. SPYI is a hybrid that
adds an option-premium overlay; I'd treat it as part dividend equity
and part premium-write — and the premium-write piece inherits the
premium-write tax problem.

**Stella:** Fixed income.

**Horace:** BND for the core bond — Treasuries plus IG corporates
plus agency MBS. VTEB for the muni equivalent in a taxable account.
PFF for preferreds, but cap that at five to ten percent of the bond
sleeve because preferreds are mostly bank credit risk in a bond
wrapper. TLT and IEF for pure-duration tools.

**Stella:** Real assets.

**Horace:** VNQ for REITs. SCHH is the cheaper alternative. That's
your inflation-pass-through sleeve.

**Stella:** Premium-write.

**Horace:** JEPI is the giant. Eighty percent low-vol equity, twenty
percent equity-linked notes synthesising call-write premium. ER 35
bps. JEPQ is the Nasdaq cousin. QYLD, XYLD, RYLD are the passive
buy-writes from Week 27. PUTW is the Week-28 put-write equivalent.

---

### PART 4 — THE 4% RULE IN APRIL 2026

**Horace:** Stella, you remember the 4% rule.

**Stella:** Bengen 1994, Trinity 1998. Retire with a 60/40, withdraw
4% of the *initial* balance, inflation-adjust the dollar amount, hold
for thirty years, success rate 95%-plus.

**Horace:** Three things have changed. One — that rule was calibrated
on US data 1926-1995, and the typical 30-year window started with
bond yields north of 5%. The 2010-2021 zero-rate regime crushed it.
Pfau and others ran the numbers; the safe withdrawal rate dropped to
about 2.8% for retirements *starting* in that window.

**Stella:** And now?

**Horace:** The 2022-2024 yield reset has lifted it back to about
3.5-3.8%. April 2026 is the first time since 2008 that the math
works *near* the original number. It's still not 4 — it's 3.7 if
you're rigid about inflation-adjusting the dollar amount.

**Stella:** Two?

**Horace:** Sequence of returns. Same numerical sequence, same asset
mix, but reversed in time — totally different lived experience. The
1973 retiree ran out in year 22. The 1995 retiree finished with ten
times the starting balance.

**Stella:** Three?

**Horace:** Variable spending dominates fixed spending. Guyton-
Klinger guard rails, percent-of-current-balance withdrawal, Vanguard
dynamic spending — they all add 50 to 100 bps to the safe withdrawal
rate, with essentially zero behavioural cost. For a retiree willing
to cut 10-15% in bad years, the 4.5% number is achievable.

---

### PART 5 — THE INTERACTIVE: BUILD-YOUR-OWN

**[VISUAL: interactive/week36_income_builder.html]**

**Stella:** Walk me through the builder.

**Horace:** Five sliders, one per sleeve. Treasuries, IG corporate
bonds, qualified dividends, REITs, premium-write. They sum to 100.
There's a tax-bracket toggle — 12, 22, 32, 37. The four numbers up
top are pre-tax yield, after-tax yield, expected volatility, and
expected max drawdown.

**Stella:** Let's load Model A — the taxable-account portfolio.

**Horace:** Treasuries 20, IG corporate 25 — call that the bond
sleeve including the muni proxy — qualified dividends 45, REITs 10,
premium-write 0. At the 32% bracket the after-tax yield is about
3.0%. Vol around 9%. Drawdown estimate 22%. That's a bond-like-vol
portfolio with three percent of spendable yield, and you supplement
to 4-4.5% with a variable-spending rule.

**Stella:** Now Model B — the IRA portfolio.

**Horace:** Treasuries 10, IG 25, qualified dividends 30, REITs 10,
premium-write 25. The bracket toggle is irrelevant inside an IRA so
your after-tax equals your pre-tax — about 5.1%. Vol 10%. Drawdown
25%. The IRA portfolio runs richer because the punitive-tax sleeves
no longer have the punishment.

**Stella:** What happens at the 12% bracket?

**Horace:** Move the bracket toggle. The whole right side of the
chart flattens — the after-tax yields rise. Qualified dividends are
zero-percent-taxed federally in the 12% bracket! At 12% federal plus
5% state, qualified-dividend equity is a 5% effective rate. That is
the cheapest income you can buy.

**Stella:** Anchor it back to the framework.

**Horace:** The four-tranche framework translates
directly. Cash sleeve is one to two years of spending, your no-sell
zone. Bonds are five to seven years of spending, refilled from
equity in good years. Equity is the wealth machine. The optional
fourth sleeve is your premium-write or concentrated income overlay.
And the barbell is the cross-section. Short-duration
safe income on one end, long-duration real assets on the other. The
middle is the *least* useful sleeve in distribution, exactly opposite
to what most target-date funds offer.

---

### OUTRO

**Stella:** Three takeaways.

**Horace:** One. Pre-tax yield is marketing. After-tax yield is what
gets spent. Convert before you decide. Two. Account location — which
sleeve goes in which account — is worth more than picking better
tickers. The tax code rewards location, not allocation. Three. The 4%
rule works again as of 2026, but only with variable spending; if you
need rigid inflation-adjusted spending, plan for 3.5-3.8%, not 4%.

**Stella:** Next week — Week 37 — we'll cover the dynamic-withdrawal
mechanics in detail: Guyton-Klinger guard rails, the 4-percent-of-
current-balance rule, and how to implement them at a real broker.

**Horace:** And after that, the L3 block wraps and we're into the
final stretch.

**[END]**
