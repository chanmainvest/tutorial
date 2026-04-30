# Side Lesson 10: Dividends — Qualified vs Ordinary, Dividend Growth, and the SCHD/VYM/DGRO Landscape

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Dividends are one of those topics where the folk-wisdom and the math
disagree, loudly. Over the long run roughly 30-40% of the S&P 500's
total return has come from reinvested dividends; once you compound the
reinvestment, the figure climbs above 80% of *cumulative* terminal
wealth from the 1930 base. That is a large slice of equity returns to
hand-wave through. At the same time, an academic in any decent
finance department will tell you that — in a frictionless world — the
choice between paying a dividend and retaining the cash is irrelevant,
because you can replicate either one by selling shares or
reinvesting. Both statements are simultaneously true. The job of this
lesson is to live inside that tension without pretending it is not
there.

Four reasons to take dividends seriously even after you have read
Modigliani-Miller:

1. **Tax treatment is *not* irrelevant.** A qualified dividend taxed
   at 15% is materially better than an ordinary dividend taxed at 32%
   plus 5% state. Modigliani-Miller assumed no taxes; you live in a
   world that has them. Where a payment lands on the IRS's two
   parallel rate schedules changes the after-tax cash flow by hundreds
   of basis points per year.
2. **Dividend *growth* is a quality signal, not a yield signal.** A
   stock that has raised its payment 25 years in a row had to grow
   earnings to support it. The Aristocrats list and the funds tracking
   it (NOBL, SCHD, DGRO) lean toward profitable, low-leverage,
   low-beta names. The yield is the by-product; the discipline is the
   feature.
3. **Behaviour beats theory.** A 70-year-old whose paycheck stops on
   Friday cannot live on "the math says you can sell 4% per year." A
   distribution that arrives in cash without an active sell decision
   is, for many retail investors, the difference between staying
   invested through a 30% drawdown and capitulating at the bottom.
   That preference is not irrational; it is just not in the textbook.
   Horace's `course/SOUL.md` #12 — *the market can stay irrational
   longer than you can stay solvent* — applies to the investor too.
4. **Dividend funds are a real allocation, not a meme.** SCHD alone
   crossed $70B in AUM by 2025, with VYM, DGRO, and NOBL adding
   another ~$120B between them. This is one of the largest single
   strategy categories in the ETF market. Knowing how the four canonical
   funds differ — SCHD's quality screen, VYM's market-cap-weighted
   yield, DGRO's growth-rate filter, NOBL's 25-year streak — is part
   of being literate in the income sleeve of a four-tranche
   portfolio.

![Three-bar grouped chart for SCHD, VYM, DGRO, NOBL, and SPYI showing five-year annualised total return, trailing five-year dividend growth rate, and current trailing twelve-month yield. SCHD and DGRO lead on growth; SPYI leads on yield with near-zero dividend growth; NOBL pays the lowest yield but has the longest growth track record.](image/side10_div_etf_compare.png)

This lesson is the operating manual for the income tranche — the
*Income* slot in the four-tranche stack of `SOUL.md` #13. You will
not learn whether dividends are "good" or "bad"; that is the wrong
question. You will learn which payments qualify for the lower
schedule, what dividend growth actually buys you, how to tell the
canonical ETFs apart, and where the math really does say "irrelevant"
versus where the IRS code says "actually, that costs you 17
points."

The interactive panel on the website lets you set a starting yield, a
dividend-growth rate, a holding horizon, and a federal bracket. It
returns the yield-on-cost at year N, the cumulative dividends
collected, and the after-tax cash. Use it after you finish the
prose.

---

### 2. What You Need to Know

#### 2.1 Qualified vs Ordinary — The 60-Day Holding Window

A dividend is *qualified* — and therefore taxed at the preferential
long-term capital-gains schedule (0%, 15%, or 20%, plus the 3.8% NIIT
above $200k single / $250k MFJ) — when **all three** of the following
hold:

1. The payer is a **US C-corporation** or a **qualified foreign
   corporation** (treaty country, or trades on an established US
   exchange via ADR).
2. You held the underlying share for **more than 60 days during the
   121-day window centred on the ex-dividend date** (so the stock
   must be in your account for at least 61 days inside that 121-day
   block).
3. You did not hedge the position with a deep-in-the-money short call
   or a synthetic short during the holding window. (Constructive sale
   rules under IRC §1259; the IRS counts a hedged long as not
   "really" held.)

A dividend that fails any of those tests is **ordinary** and is taxed
at your regular wage rate — up to 37% federal plus state plus NIIT,
i.e. as much as 44.6%. The biggest ordinary-bucket sources are:

- **REIT distributions** (most of them; the 199A 20% qualified
  business income deduction takes the effective rate down by 20% but
  does not move them onto the LTCG schedule).
- **MLP distributions** (mostly return-of-capital, with the rest
  taxed as ordinary income on the K-1).
- **Foreign companies not traded on a US exchange** (if you bought
  the local-listed shares directly via a foreign broker, the
  dividends are usually ordinary).
- **Bond ETFs paying "dividends"** (these are interest payments
  dressed up as distributions; always ordinary).
- **Money-market and HYSA "dividends"** (interest).

The rule that catches retail investors is the *60-day holding*
requirement. Buy a stock the day before its ex-date, sell two weeks
later — the dividend is non-qualified, and you owe ordinary rates on
something you only held 14 days. Schwab and Fidelity flag this on
the 1099-DIV, but the system reports the dollar split (Box 1a vs Box
1b); it does not retro-fix your cost basis. The 60-day rule is
why dividend-capture trading strategies almost never work after
tax.

#### 2.2 The 2026 Rate Stack

Two parallel schedules, applied to the same dollar of investment
income depending on which bucket it falls in.

**Ordinary schedule** (wages, interest, REIT distributions,
non-qualified dividends, short-term capital gains; 2026 single
filer):

| Bracket | Taxable income |
|---|---|
| 12% | $12,150 - $50,400 |
| 22% | $50,400 - $107,825 |
| 24% | $107,825 - $206,000 |
| 32% | $206,000 - $262,000 |
| 35% | $262,000 - $657,000 |
| 37% | above $657,000 |

**LTCG / qualified-dividend schedule:**

| Rate | Taxable income (single) |
|---|---|
| 0% | up to $49,450 |
| 15% | $49,450 - $545,750 |
| 20% | above $545,750 |

Plus a flat **3.8% NIIT** on top of either schedule for households
above $200k single / $250k MFJ.

Two practical corollaries:

- A 32%-bracket retiree taking $4,000 of SCHD dividends keeps
  $3,200 (15% LTCG + 5% state). The same retiree taking $4,000 of
  VNQ (REIT) distributions keeps $2,624 (32% × 0.80 from 199A + 5%
  state). Same headline yield, almost 18% gap in cash to the
  household.
- A 12%-bracket investor pays **zero** on qualified dividends.
  This is the single largest *legal* free lunch in the US tax code
  for low- and middle-income retirees. Until you cross $49,450 of
  taxable income, your SCHD distribution is tax-free. Asset
  *location* (this dividend in *which* account) is the lever that
  lets you stay in that bracket.

#### 2.3 Yield vs Dividend Growth — Two Different Questions

The single most common framing error in dividend investing is to read
the **trailing-twelve-month yield (TTM)** as if it were the rate of
return. It is not. Yield is one term of two:

$$ \text{Total return} \approx \text{Dividend yield} + \text{Capital growth} $$

For a slow-moving dividend payer the second term tracks the first
through dividend *growth*: a company that grows its dividend 8% per
year tends to compound its share price at roughly the same rate over
long windows, because the payout policy is anchored to earnings.

The four canonical filters and what each one is actually optimising
for:

| ETF | Index | Yield (Apr 2026) | 5y div CAGR | What it screens for |
|---|---|---|---|---|
| **SCHD** | Dow Jones US Dividend 100 | ~3.6% | ~10% | Quality + 10y dividend track + cash-flow ROE |
| **VYM** | FTSE High Yield ex-REIT | ~2.9% | ~6% | Top half of S&P 500 by yield, cap-weighted |
| **DGRO** | Morningstar US Div Growth | ~2.3% | ~10% | 5y consecutive dividend increases, payout < 75% |
| **NOBL** | S&P 500 Dividend Aristocrats | ~2.0% | ~7% | **25 consecutive years** of dividend increases |
| **SPYI** | S&P 500 + monthly call overwrite | ~12.0% | ~0% | Premium-write income, not dividend growth |

The point of putting SPYI on the same bar chart is the contrast. SPYI
is a covered-call ETF (`course/week27_covered_calls.md`); its 12%
distribution comes from option premium, not from companies growing
their cash flows. The dividend growth column for SPYI is roughly
zero — the distribution rises and falls with implied volatility, not
with corporate earnings. That is a *different* kind of income, taxed
differently (mostly short-term capital gains and return-of-capital,
none of it qualified), and it should occupy a different sleeve of
the four-tranche stack than SCHD or VYM.

**Yield-on-cost (YoC).** A position with a 3.6% starting yield that
grows the dividend 10% per year reaches a **YoC** of:

$$ \text{YoC}_N = y_0 \cdot (1+g)^N $$

After ten years that is 3.6% × 1.10^10 = 9.34%. After twenty years it
is 24.2% on the original cost. This is the math that makes
dividend-growth investing emotionally durable: a retiree in 2046 who
bought SCHD in 2026 is — on paper — collecting nearly 25% of her
original investment in cash dividends every year, even though the
*current* yield of SCHD has not moved. YoC is a vanity metric for
performance attribution, but a real one for lifestyle planning.

![Line chart of S&P 500 Dividend Aristocrats Index dividend per share from 1990 to 2024. Growth is steady at roughly 7% per year, with a brief flatline through the 2008 GFC and a small dip in 2020 from oil-name cuts, but the slope resumes within a year in both cases.](image/side10_aristocrats_growth.png)

#### 2.4 The Modigliani-Miller View — Why Some People Hate Dividends

Here is the classical argument, in one paragraph. In a world without
taxes or transaction costs, a $100 stock that pays a $4 dividend on
the ex-date becomes a $96 stock plus $4 of cash in your account. You
were holding $100 of value before; you are holding $100 of value
after. If you preferred no payment, you reinvest the $4 and you are
back to $100 in stock. If your neighbour holds $100 in a non-paying
stock and wants $4 of cash, she sells $4 of stock and is also holding
$96 plus $4. The two policies are identical in wealth terms; the
only difference is the *path*. Modigliani and Miller (1961) proved
this formally and won a Nobel Prize for it.

In the *real* world the assumption breaks in three places:

1. **Taxes.** A forced dividend is a forced taxable event. The
   investor who sells $4 of stock chooses *when* to realise the
   gain; the investor who receives a $4 dividend has no such choice.
   At a 32% ordinary rate (non-qualified) that is a 1.28% friction
   per year *imposed* on you. SOUL #15.
2. **Transaction costs.** Selling $4 of a $100 stock costs nothing
   on a commission-free broker, but it costs *attention* — a real
   resource for many investors. The dividend is automatic. The "rip
   $4 off the top yourself" prescription is theoretically clean but
   behaviourally fragile.
3. **Information signalling.** A board that raises the dividend is
   also signalling "we expect to keep earning this". A board that
   cuts is signalling the opposite. The market reads the *change* in
   payout as a forecast about future cash flows, and the empirical
   literature (Lintner 1956, Brav-Graham-Harvey-Michaely 2005)
   confirms that managers know it and manage accordingly. Pure
   irrelevance would imply boards do not care about dividend policy;
   they very obviously do.

The honest synthesis is: in a frictionless model, dividends are
neutral; in the real world, the tax friction is real but
quantifiable, and the behavioural value of the automatic payment is
also real but not in the textbook. Both sides are right about
something.

#### 2.5 Foreign Withholding — The Canadian and European Cases

A US investor holding a foreign dividend payer will see foreign
withholding tax deducted before the cash hits the brokerage account.
The two cases retail investors actually meet:

- **Canadian dividend payers (ENB, BCE, RY, TD).** Canada withholds
  **15%** at source under the US-Canada tax treaty (it would be
  25% without the treaty). The 15% appears as "foreign tax paid"
  in box 7 of the 1099-DIV. You claim it back via the **Foreign
  Tax Credit (FTC)** on Form 1116.
- **European payers (Nestlé, Novartis, Shell B-share via ADR).**
  Most treaty rates are 15%; Switzerland withholds 35% but allows
  reclaim via Form 88 (most retail investors never bother).

The FTC has two structural limits that catch beginners:

1. **It is a credit, not a refund.** You can offset it only against
   your US tax bill. If your US tax owed in a given year is zero
   (e.g. you live primarily on Roth distributions), the foreign
   withholding is dead-weight loss. This is why holding foreign
   dividend payers in a Roth IRA is a *worse* outcome than holding
   them in a taxable account: in the taxable account you reclaim
   the 15%, in the Roth you eat it.
2. **The credit is sleeved by income category.** Passive-category
   foreign tax credits offset passive-category US tax owed.
   Excess credits carry back one year and forward ten, but for most
   retail investors with modest foreign exposure the credit fully
   offsets in the year paid.

The general rule, restated: **foreign dividend payers belong in a
taxable account so that the withholding is recoverable**; broad US
dividend payers can live in any account; REITs and bond payers go
into the IRA stack. (`course/side04_tax_efficiency.md` has the full
asset-location matrix.)

---

### 3. Common Misconceptions

1. **"High yield = high return."** No. A 12% yield from a covered-call
   ETF is not the same animal as a 3% yield from a dividend grower.
   Cover the difference with the dividend-growth column of the ETF
   table; the SPYI total return over 5 years has trailed SCHD by
   several percentage points despite the four-times-larger headline.
2. **"Dividends are 'free money'."** They come out of the share
   price on the ex-date, dollar-for-dollar. Modigliani-Miller is
   right about that part.
3. **"Reinvesting dividends in a taxable account is tax-free."** No.
   The dividend is taxed in the year paid, *whether or not* you
   reinvest it. DRIP is not a tax shelter; it is an autopilot for the
   reinvestment leg, nothing more.
4. **"REIT dividends are qualified."** Almost never. REIT
   distributions are mostly ordinary income; the 199A 20% deduction
   is a partial offset, not a re-classification.
5. **"Foreign dividends should go in the Roth because they're
   tax-advantaged."** Backwards. Putting foreign dividends in the
   Roth eats the foreign withholding with no offset. Foreign payers
   belong in taxable.
6. **"Dividend stocks are safer than the S&P."** Sometimes. Aristocrats
   like KO, JNJ, PEP, PG do tend to have lower beta. But "safe" is
   regime-dependent: in 2022 the S&P 500 fell ~18% and many high-yield
   names (utilities, especially) fell more because they are
   long-duration bond proxies (`course/week34_rate_shock_grid.png`).
7. **"You should chase the highest-yielding stock in a sector."**
   The highest yield in a sector is usually the highest yield because
   the market is pricing a dividend cut. Both AT&T (2021) and General
   Electric (2018) screened "best yield in their sector" right
   before they cut. Yield is a *result*; quality is the input.
8. **"NOBL is the best dividend ETF because Aristocrats."** The 25-year
   filter is mechanical, not predictive. NOBL excludes payers like
   Microsoft (started in 2003) and Apple (re-started in 2012) that
   have been the dominant capital-return stories of the last decade.
   Filtering rules have side effects.

---

### 4. Q&A Section

**Q1. If I bought a stock on its ex-dividend date, do I get the
dividend?**
No. The ex-date is the cut-off; the buyer on or after the ex-date is
buying the stock *without* the right to the next payment. The price
drops by the dividend amount on the ex-date specifically because of
this.

**Q2. What is the holding-period rule again, in plain English?**
You must hold the stock more than 60 days inside a 121-day window
that straddles the ex-date (60 before, 60 after, plus the ex-date
itself). Hold less, and the dividend is taxed at ordinary rates even
if the company is a perfectly normal US C-corp.

**Q3. Why did my SCHD distribution drop in Q2 of last year?**
Distributions vary quarter to quarter as the underlying companies
declare on their own schedules. SCHD's annual total grows at
roughly its 10% trailing CAGR, but a single quarter can be 30% above
or below the smoothed line.

**Q4. Are MLP distributions dividends?**
No. They are *partnership distributions* and arrive on a K-1, not a
1099-DIV. Most of the cash is technically a return-of-capital that
reduces your basis until you sell, then is recaptured as ordinary
income. Not friendly to retail.

**Q5. What is the difference between dividend growth and dividend
yield investing?**
Yield investing optimises today's cash; growth investing optimises
the trajectory. SCHD blends both screens. VYM is more yield-tilted.
DGRO is more growth-tilted. NOBL is the strictest growth filter
(25-year streak) and consequently has a lower headline yield.

**Q6. Will dividend ETFs underperform in a tech-led market?**
Often, yes. SCHD trailed VOO by 7-10 percentage points per year in
the 2020-2024 window because the dominant winners (NVDA, MSFT, GOOGL,
META, AMZN) either pay no dividend or do not pass the SCHD quality
screen. This is a feature, not a bug; you do not buy SCHD to win
when growth wins. You buy it for the income tranche.

**Q7. Where should I hold SCHD?**
Either a taxable account (qualified dividends taxed at LTCG rates) or
a Roth (tax-free forever). A Traditional IRA is fine but slightly
suboptimal because you turn LTCG-rate cash flows into ordinary
income on withdrawal. The location loss is roughly 5-10 bp/year.

**Q8. Where should I hold REITs?**
Traditional IRA or Roth. Never a regular taxable account at a high
bracket if you can avoid it. The 199A deduction helps but does not
fully fix the ordinary-rate problem.

**Q9. What is "yield-on-cost" and why do dividend investors talk about
it?**
YoC is the current annual dividend divided by your *original* cost
basis. After 20 years of 10% dividend growth on a 3.6% starter
yield, your YoC is 24%. It is psychologically powerful for retirees
because it makes the long-term compounding tangible — even if it has
no implication for forward expected return.

**Q10. Do dividend ETFs work outside the US?**
Yes, but US investors should stick to US-listed wrappers. Per
`course/SOUL.md` #16, the US is the only equity market with the
liquidity, governance, and ETF infrastructure where retail can
operate confidently. SCHD, VYM, DGRO, NOBL, and SPYI are all
US-listed and US-domiciled. Do not buy the Irish-domiciled
"international clones" — you trade foreign withholding for
PFIC-status nightmares.

**Q11. What is the right size for the income sleeve in a four-tranche
portfolio?**
For a 50-year-old with a 15-year accumulation runway, ~25% of total
financial assets in the income tranche is a defensible default
(`course/SOUL.md` #13). For a 65-year-old in early retirement, 35-45%
is more typical. The split *within* the sleeve between dividend
ETFs, bonds, and premium-write is what `course/week36_income_portfolio.md`
walks through.

**Q12. Is there a dividend version of "the market is wrong about this
stock"?**
Yes — it's called the **dividend trap**. A 9% yield in a sector
where peers yield 3% is the market saying "we are pricing a 67%
chance of a cut." Sometimes the market is wrong; usually it is not.
Verify the payout ratio, free-cash-flow coverage, and balance-sheet
leverage before assuming the yield is real.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Dividends in 2026 — Qualified vs Ordinary, Growth vs Yield, and the SCHD/VYM/DGRO/NOBL/SPYI Stack
**RUNTIME TARGET:** ~12 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00 to 1:00]**

[VISUAL: image/side10_div_etf_compare.png]

STELLA: Today's lesson is about dividends. Specifically: when does
the IRS tax them at the lower rate, when does it tax them at the
higher rate, and how do the canonical dividend ETFs — SCHD, VYM,
DGRO, NOBL, and the covered-call wrapper SPYI — actually compare?

HORACE: Three things you'll come away with. One: the rule for what
makes a dividend "qualified" — you have to hold the stock more than
60 days around the ex-date. Two: the gap between SCHD's roughly 10%
dividend growth rate and VYM's roughly 6% — that's the difference
between SCHD and VYM in one number. Three: yield-on-cost — why an
investor who bought a 3.6% yielder twenty years ago is collecting
24% on her original money today, even though the *current* yield
hasn't moved.

STELLA: This is a side lesson, so we're keeping it tight. Twelve
minutes.

---

**[SECTION 1 — Qualified vs ordinary, the 60-day rule, 1:00 to 3:30]**

HORACE: The single most important fact in this lesson is that the
US tax code runs *two parallel rate schedules* on investment income.
The ordinary schedule taxes wages, bond interest, REIT distributions,
and short-term capital gains. The other schedule — the LTCG schedule
— taxes long-term capital gains and *qualified dividends* at a much
lower rate.

STELLA: How much lower?

HORACE: At 32% bracket — which is most US households making over
about 200 grand single — the ordinary rate is 32% and the qualified
rate is 15%. Plus state. Plus 3.8% NIIT above 200K. The gap is
around 17 percentage points.

STELLA: So the question is: what makes a dividend "qualified"?

HORACE: Three tests. The payer has to be a US C-corp or a qualified
foreign corp. You have to hold the stock more than 60 days inside
the 121-day window centred on the ex-date. And you can't be hedging
with a deep-in-the-money short call during the holding period. If
all three pass, the dividend lands in the LTCG bucket. Miss any one
of them and it's ordinary.

STELLA: The 60-day rule trips people up.

HORACE: Right. If you bought the stock the day before its ex-date,
collected the dividend, and sold a week later — that dividend is
*not* qualified. Ordinary rate, full stop. This is why
dividend-capture strategies almost never beat after tax.

STELLA: What about REITs?

HORACE: REIT distributions are almost never qualified. They're
ordinary income. The 199A deduction takes 20% off the effective rate
— so a 32% bracket REIT investor pays roughly 25.6%, not 32% — but
they don't move onto the LTCG schedule. That's why REITs go in the
IRA stack, not in taxable.

---

**[SECTION 2 — Yield vs growth, the SCHD/VYM/DGRO/NOBL/SPYI table, 3:30 to 7:00]**

[VISUAL: image/side10_div_etf_compare.png]

STELLA: Show me the chart of the five canonical dividend ETFs.

HORACE: Three bars per fund. The first is the trailing five-year
total return. The second is the trailing five-year dividend CAGR —
how fast the distribution itself has grown. The third is the
current TTM yield.

STELLA: SPYI is the outlier — 12% yield.

HORACE: Yes, and that's the lesson. SPYI is a covered-call ETF.
Its distribution comes from selling option premium against an S&P
500 portfolio, not from companies growing their earnings. So the
*growth* column for SPYI is essentially zero. The headline yield is
huge but it's a different kind of income — it's option premium,
which is taxed at short-term cap gains, not at qualified rates.

STELLA: And SCHD versus VYM versus DGRO?

HORACE: SCHD is Schwab's quality-and-yield blend. The Dow Jones US
Dividend 100 index. About a 3.6% yield, 10% per year dividend growth.
VYM is Vanguard's pure-yield top-half-of-S&P-500 cut — 2.9% yield,
6% growth. DGRO is iShares' growth filter — companies with five
straight years of dividend increases — 2.3% yield, 10% growth. NOBL
is the strictest — 25 straight years of increases — 2% yield, 7%
growth.

STELLA: So which one is "best"?

HORACE: Wrong question. They're not substitutes. SCHD is the default
single-fund pick if you want one income ETF that does both jobs —
yield and growth. NOBL is the cleanest quality screen but
underweights the new-economy compounders that started paying
dividends in the last decade. DGRO is the Microsoft-and-Apple-friendly
version. VYM is the highest yield without going into junk. SPYI is
not a dividend ETF — it's a covered-call ETF; treat it as part of the
options-income sleeve, not the dividend sleeve.

---

**[SECTION 3 — Aristocrats and the case for dividend growth, 7:00 to 9:00]**

[VISUAL: image/side10_aristocrats_growth.png]

HORACE: Look at this chart. This is the dividend per share of the
S&P 500 Dividend Aristocrats Index from 1990 to 2024.

STELLA: It's a very clean line.

HORACE: Roughly 7% per year, all the way through. Notice 2008 — the
GFC. The dividend per share of the index *flatlined*. It did not
collapse. Companies got kicked out of the Aristocrats list when they
cut, but the surviving members kept paying, and the new replacements
kept paying. By 2010 the slope resumes.

STELLA: COVID?

HORACE: Tiny dip in 2020, mostly because of energy names that cut.
Resumed within a year.

STELLA: That stability is the case for dividend growth as a strategy.

HORACE: Right. The Aristocrats filter is mechanical — you must have
raised the dividend 25 years in a row. That filter, applied
historically, gave you ~7% per year compounding income through two
of the worst macro shocks of the last 40 years. That's the empirical
foundation underneath the SCHD/DGRO/NOBL family.

---

**[SECTION 4 — Modigliani-Miller and the irrelevance debate, 9:00 to 10:30]**

STELLA: Some academics will tell you dividends don't matter. The
share price drops by the dividend on the ex-date, so it's
"economically equivalent" to selling shares.

HORACE: Modigliani-Miller, 1961. They're right in their model. In a
frictionless world the choice between dividend and retention is
neutral. But three frictions break the model in the real world.
First, taxes — a dividend is a forced taxable event; you don't get
to choose when to realise. Second, behaviour — most retail investors
will not actually execute the "sell 4% per year" prescription with
the same discipline they cash a dividend cheque. Third, signalling —
a board that raises the dividend is signalling expected future cash
flow; the market reads it.

STELLA: SOUL #12.

HORACE: Yes — the market can stay irrational longer than you can stay
solvent, and that applies to the investor too. A 70-year-old whose
paycheck stops on Friday cannot live on "the math says you can sell
shares." The dividend is operationally robust in a way the
do-it-yourself withdrawal isn't.

---

**[SECTION 5 — Foreign withholding and asset location, 10:30 to 11:30]**

STELLA: One more wrinkle: foreign dividend payers.

HORACE: Canada and most of Europe withhold 15% at source — the
treaty rate — before the cash hits your brokerage. You claim it back
on Form 1116 as a Foreign Tax Credit. But the credit is only
recoverable against US tax owed. So if you put your foreign
dividend payers in a *Roth IRA*, you eat the 15% with no offset.
That's the opposite of the usual asset-location intuition.

STELLA: Which means foreign dividends go where?

HORACE: Taxable. So you can recover the FTC. Bonds and REITs go in
the IRA stack. Domestic dividend ETFs like SCHD can sit anywhere.
Side 4 has the full asset-location matrix.

---

**[OUTRO — 11:30 to 12:00]**

STELLA: Three things to take away.

HORACE: One. Hold the position more than 60 days around the ex-date
or the dividend is not qualified. Two. Yield is not return; dividend
*growth* is the actual signal. Three. SCHD/VYM/DGRO/NOBL are not
substitutes — different filters for different jobs. SPYI is not a
dividend fund; it's a covered-call wrapper.

STELLA: Open the interactive panel. Set a 3.6% starting yield, 10%
growth, 20-year horizon, your bracket. Watch the yield-on-cost climb
to 24%. That's the chart that makes dividend growth investing
emotionally durable.

HORACE: Next side lesson is on the mechanics of foreign-listed ETFs
and PFIC rules. See you there.
