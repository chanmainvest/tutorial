# Week 35: Advanced Financial Statement Analysis — DuPont, Working Capital, and Distress Models

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Week 8 taught you to read the three statements. Week 19 taught you the
capital structure they sit on. Week 20 taught you to trust cash over
earnings. Week 21 taught you to discount the cash. This week is the
operator's wrench set — the small number of compact ratios and scoring
models that professional analysts actually use, every quarter, for every
name they cover, to answer four very practical questions:

1. **Where does this company's return on equity actually come from?** A
   17% ROE at JPMorgan is a fundamentally different animal from a 17%
   ROE at Ford. One is built on a 12× balance sheet and a 4% margin,
   the other on a 7× balance sheet and a 3% margin doing very different
   work. The DuPont decomposition splits ROE into its three (or five)
   drivers so you can tell margin businesses from leverage businesses
   from turnover businesses, and notice when one of those legs starts to
   wobble.

2. **Is the working capital a tailwind or a tap on the brake?** A
   manufacturer that ships product before it gets paid, holds inventory
   for ninety days, and pays suppliers in thirty is bleeding cash even
   when the income statement looks fine. The cash conversion cycle —
   DSO + DIO − DPO — turns that into a single number you can track
   quarter to quarter and compare across competitors.

3. **Are the earnings being managed?** The Beneish M-score combines
   eight ratios into one probability that a firm is manipulating
   earnings. It will not catch every fraud (Wirecard's was a different
   class of lie), but Beneish flagged Enron in 1997, three years before
   it imploded. As an investor you do not need a perfect detector. You
   need something that fires often enough to make you actually open the
   10-K when the score lights up.

4. **Is the company a going concern, or is it walking toward Chapter 11?**
   The Altman Z-score, published by Edward Altman in 1968 and barely
   modified since, predicts bankruptcy risk over the next two years with
   roughly 80–90% accuracy on the original test set. Its threshold zones
   — distress below 1.81, gray 1.81–2.99, safe above 2.99 — are crude,
   and that is the point. Crude rules survive regimes; finely tuned
   ones do not. SOUL #1 again: alpha is rare, but *avoiding negative
   alpha* is cheap, and a $0 ten-line spreadsheet is one of the cheapest
   sources.

The chart below ([image/week35_dupont_compare.png](image/week35_dupont_compare.png))
shows what DuPont looks like when you put five very different
businesses next to each other. Apple is a margin machine with serious
leverage from buybacks. JPMorgan is a leverage machine with thin
margins and almost no asset turnover. Ford is a turnover machine with
both thin margins and meaningful leverage. The same 13–17% ROE is being
manufactured three different ways, and the path to a 0% ROE is
different for each.

---

### 2. What You Need to Know

#### 2.1 DuPont Decomposition — Three-Factor and Five-Factor

The original DuPont formula, named after the analyst department at
DuPont Corporation in the 1920s, is identity arithmetic:

$$ \text{ROE} \;=\; \frac{\text{Net Income}}{\text{Equity}}
   \;=\; \underbrace{\frac{\text{NI}}{\text{Sales}}}_{\text{Net Profit Margin}}
   \;\times\; \underbrace{\frac{\text{Sales}}{\text{Assets}}}_{\text{Asset Turnover}}
   \;\times\; \underbrace{\frac{\text{Assets}}{\text{Equity}}}_{\text{Equity Multiplier}} $$

The two middle ratios cancel algebraically. What survives is a
description of *how* a company gets to its ROE. Margin × Turnover is
operating efficiency; Equity Multiplier is leverage. A high ROE built
on margin is a brand or moat business. A high ROE built on turnover is
a logistics or scale business. A high ROE built on leverage is a
financial business — or, when leverage rises in a non-financial, an
early warning sign.

The five-factor extension splits margin into three pieces — tax
burden, interest burden, and operating margin — to isolate where
profitability is being squeezed:

$$ \text{ROE} \;=\; \frac{\text{NI}}{\text{EBT}} \times \frac{\text{EBT}}{\text{EBIT}}
   \times \frac{\text{EBIT}}{\text{Sales}} \times \frac{\text{Sales}}{\text{Assets}}
   \times \frac{\text{Assets}}{\text{Equity}} $$

Tax burden (NI/EBT) and interest burden (EBT/EBIT) are between zero
and one. Each is a leak. The five-factor version is what you reach for
when an ROE is moving and you cannot tell whether it is the operating
business, the tax code, the cost of debt, the asset base, or the
buyback that is doing the work. It almost always turns out to be more
than one.

For Apple in FY2024 the three-factor reads roughly NPM 24% × Turnover
1.07 × Equity Multiplier 6.4 → ROE ≈ 165%. That equity multiplier is
not leverage in the bad sense — it is the consequence of $725B of
buybacks since 2013 (Week 19). Apple has shrunk the denominator faster
than the numerator. ROE in that situation is no longer a measure of
business quality; it is a measure of how aggressively the company has
returned capital. Use ROIC (Week 21) for the cleaner read.

#### 2.2 Cash Conversion Cycle and Working Capital Efficiency

The cash conversion cycle (CCC) is how many days a dollar of input
spending stays trapped in the business before it comes back as a
dollar of cash from a customer:

$$ \text{CCC} \;=\; \text{DSO} + \text{DIO} - \text{DPO} $$

- **DSO** (days sales outstanding) = Receivables / Revenue × 365.
  How long customers take to pay you.
- **DIO** (days inventory outstanding) = Inventory / COGS × 365.
  How long product sits before being sold.
- **DPO** (days payables outstanding) = Payables / COGS × 365.
  How long you take to pay suppliers.

A negative CCC — Apple, Costco, Amazon — means suppliers finance your
inventory. You are running on float. A positive CCC means *you* are
financing the supply chain, which is a working-capital tax that grows
with revenue. Watch the trend more than the level. Three rising
quarters of DSO is one of the most reliable advance warnings of a
revenue-recognition problem.

A second working-capital ratio every analyst eventually internalises is
the **accruals ratio**:

$$ \text{Accruals ratio} \;=\; \frac{\Delta\text{Working Capital} - \Delta\text{Cash}}
                                       {\text{Average Total Assets}} $$

This is the Sloan (1996) accruals anomaly in summary form (see Week 20,
[image/week20_accruals_anomaly.png](image/week20_accruals_anomaly.png)).
High positive values mean the income statement is leading the cash flow
statement — the firm is booking revenue and profit faster than the cash
arrives. Sloan's quintile spread averaged ~9% per year, and it has not
inverted in three decades.

#### 2.3 The Beneish M-Score — Earnings Manipulation Detector

Daniel Beneish's 1999 paper combined eight one-year-change ratios into a
single probit-style score. The mnemonic: DSRI, GMI, AQI, SGI, DEPI,
SGAI, LVGI, TATA. You will rarely compute it by hand — your data
provider does it — but the intuition matters:

| Variable | What it captures |
|---|---|
| **DSRI** Days Sales in Receivables Index | Receivables growing faster than sales |
| **GMI** Gross Margin Index | Margin deterioration year-over-year |
| **AQI** Asset Quality Index | Non-current non-PPE assets rising (capitalised costs) |
| **SGI** Sales Growth Index | Aggressive growth tempts management |
| **DEPI** Depreciation Index | Slowing depreciation (longer useful lives) |
| **SGAI** SG&A Index | SG&A rising faster than sales |
| **LVGI** Leverage Index | Rising leverage |
| **TATA** Total Accruals to Total Assets | The Sloan anomaly piece |

The composite is:

$$ M \;=\; -4.84 + 0.92 \cdot \text{DSRI} + 0.528 \cdot \text{GMI} + 0.404 \cdot \text{AQI}
   + 0.892 \cdot \text{SGI} + 0.115 \cdot \text{DEPI} - 0.172 \cdot \text{SGAI}
   - 0.327 \cdot \text{LVGI} + 4.679 \cdot \text{TATA} $$

A score above −1.78 is classified as "likely manipulator". Beneish back-
tested it against 74 known manipulators and flagged ~76% with a 17%
false-positive rate. It famously fired on Enron in 1997 and 1998, on
WorldCom in 1999, on Valeant in 2014. It missed Wirecard, because
Wirecard simply made up the cash balance — there was no earnings
manipulation footprint, just an outright lie. The lesson: M-score is a
*screening filter* (SOUL #5, "look at the right numbers"), not a
verdict. When it lights up, you read the 10-K. When it doesn't, you
still read the 10-K, just with less urgency.

#### 2.4 The Altman Z-Score — Bankruptcy Prediction

Edward Altman, NYU, 1968. Multiple discriminant analysis on 33 bankrupt
and 33 non-bankrupt manufacturers. The original public-firm formula:

$$ Z \;=\; 1.2 \, A + 1.4 \, B + 3.3 \, C + 0.6 \, D + 1.0 \, E $$

| Term | Definition | Interpretation |
|---|---|---|
| A | Working capital / Total assets | Short-term liquidity buffer |
| B | Retained earnings / Total assets | Cumulative profitability |
| C | EBIT / Total assets | Operating productivity of assets |
| D | Market value of equity / Total liabilities | Market-tested solvency cushion |
| E | Sales / Total assets | Asset turnover |

The cutoffs:

- **Z > 2.99** — "safe" zone. Bankruptcy in next 2 years rare.
- **1.81 ≤ Z ≤ 2.99** — gray zone. Watch list.
- **Z < 1.81** — distress zone. Materially elevated bankruptcy
  probability.

Two warnings. First, Altman calibrated the model on US manufacturers
with public equity. The variants — Z' for private firms, Z'' for
non-manufacturers and emerging markets — change the coefficients and
cutoffs. Use the right one. Second, Z is a noisy point estimate; the
*trend* matters more than any single reading. GE's Z drifted from 2.6
in 2012 down to 1.2 by 2018, three years before the dividend cut and
the breakup. The trend line was the signal; the absolute level was just
the noise.

The chart [image/week35_zscore_distress.png](image/week35_zscore_distress.png)
shows three trajectories. GE 2010-2024 (the deteriorate-and-recover
curve), Ford 2018-2024 (perpetually parked in the gray zone, which is
about right for a cyclical), and Apple 2020-2024 (deeply safe, the
shape of a brand business with a clean balance sheet). Same model,
same cutoffs, completely different stories.

#### 2.5 Putting It Together — The Two-Page Health Check

In practice, here is what a compact diligence sheet looks like for a
new name:

1. **DuPont 3-factor and 5-factor for the trailing 5 years.** Are any
   of the legs trending in a direction the management story does not
   explain?
2. **CCC for the trailing 8 quarters.** Direction matters more than
   level. Compare to two named competitors.
3. **Accruals ratio for the trailing 5 years.** Persistent positive
   reading is a yellow flag.
4. **Beneish M-score, latest fiscal year.** Above −1.78 is a yellow
   flag. Above −1.0 is a red flag.
5. **Altman Z-score, latest 5 years.** Below 1.81 in two consecutive
   years is a position-size question. Trending down through the gray
   zone is a research question.

None of this is alpha generation in the SOUL #5 sense. It is the
opposite: it is the *negative-alpha filter*. Most amateur portfolios
underperform not because they failed to find the next Apple but because
they held a Bear Stearns or a Valeant or a GE in the 2017 stretch when
a five-minute screen would have asked them to think twice. The
[interactive lab](interactive/week35_fsa_lab.html) at the end of this
lesson lets you pick a preset firm or punch in your own numbers and
watch the Z-score band classification flip in real time.

---

### 3. Common Misconceptions

1. **"High ROE is always good."** A high ROE built entirely on a rising
   equity multiplier is leverage in disguise. Decompose it before you
   admire it.
2. **"DuPont is just bookkeeping arithmetic."** It is identity
   arithmetic, but the *change* in each factor is information. A
   margin compressing while turnover and leverage hold steady tells you
   exactly which line of the income statement to investigate.
3. **"A negative cash conversion cycle is a goal."** It is a
   *consequence* of supplier power and customer payment terms. You
   cannot will it into existence; chasing it through aggressive payable-
   stretching can break supplier relationships and collapses in
   recessions.
4. **"The Beneish M-score is a fraud detector."** It detects the
   *footprint* of accounting manipulation — receivables and accruals
   and margin changes. Frauds that bypass the books entirely (fake
   cash balance, fake invoices, related-party transactions) leave no
   M-score footprint.
5. **"Altman Z below 1.81 means bankruptcy."** It means *elevated
   probability* of bankruptcy in the next two years, not certainty.
   Plenty of firms live in the distress zone for years and emerge.
   Plenty of firms in the gray zone go to zero. Use it as a sizing and
   research signal, not an exit signal in isolation.
6. **"These models work the same for banks and insurers."** They do
   not. Banks have a balance sheet that is mostly financial assets;
   asset turnover is meaningless and Z-score variants are required.
   Use ROTCE and tangible book trends instead.
7. **"You need a Bloomberg terminal to do this."** You need an SEC
   EDGAR account, which is free, and a calculator. Every ratio in this
   lesson can be computed from a 10-K in under thirty minutes.
8. **"If the M-score and Z-score both look fine, the company is
   safe."** They are necessary, not sufficient. Wirecard was fine on
   both. So was Bernie Madoff's "fund". The models score *what is in
   the books*. They do not audit whether the books are real.

---

### 4. Q&A Section

**Q: Should I use three-factor DuPont or five-factor?**
A: Start with three-factor for screening across many names. Move to
five-factor when one of the three is moving and you need to know which
of tax, interest, or operating margin is doing the work. Five-factor
is also essential for cross-country comparisons because tax burdens
diverge sharply across jurisdictions.

**Q: How often should I recompute these ratios?**
A: Each fiscal quarter when the 10-Q drops, plus a clean run through
the 10-K every January. Working capital ratios in particular are
volatile quarter-to-quarter; trend over 4-8 quarters matters far more
than a single point.

**Q: What is the typical M-score for a clean blue-chip?**
A: For mature, slow-growing US large-caps the M-score sits around −2.5
to −3.0. Apple, Microsoft, Coca-Cola, JPMorgan all run comfortably
below the −1.78 threshold. Aggressive-growth names routinely score
between −2.0 and −1.5 simply because the SGI (sales growth index) is
elevated; that is a feature of the model, not necessarily a manipulation
signal.

**Q: Which of the four models is most useful?**
A: Honestly, the cash conversion cycle. It is the most robust to
reporting style, easiest to compute, hardest to fake without leaving a
trail elsewhere, and most directly tied to the operating reality. The
M-score and Z-score are scoring composites; CCC is a measurement of an
actual physical fact about the business.

**Q: Can I use the Z-score for an ETF or a fund?**
A: No. Z-score requires a single corporate balance sheet. For a fund
or ETF you would aggregate the holdings — Bloomberg and similar tools
report a weighted-average Z-score for index ETFs, but the
interpretation is loose. The model was designed for single-firm
distress prediction, not portfolio risk.

**Q: What is the right benchmark for DSO and DIO?**
A: The named competitor in the 10-K's own competitive section, plus
the industry median. Direction matters more than level. A retailer
with DIO of 90 and a competitor at 60 should worry; a retailer whose
own DIO went from 60 to 90 over four quarters should worry more.

**Q: Why does AAPL's equity multiplier look so extreme?**
A: Buybacks. Apple has retired roughly $725B of equity since 2013
(see Week 19 chart). The denominator of ROE has shrunk faster than
the numerator. The "ROE" reading north of 150% is real arithmetic but
not a meaningful measure of business quality at this point. Use ROIC
or return on tangible assets instead.

**Q: Does the M-score still work after 25 years of academic
publication?**
A: Less well than at publication, but it has not collapsed. The
mechanical relationships it captures — receivables growing faster than
sales, gross margin deteriorating, accruals running positive — remain
the actual physical signatures of earnings management. Public
disclosure of the formula has *raised the cost* of crude manipulation,
which is itself a form of efficacy.

**Q: How does this fit into Horace's four-tranche framework?**
A: Mostly Tranche 2 (factor / quality sleeve) and Tranche 3 (active /
single-name alpha). Tranche 1 (passive index) does not need any of
this; you bought the basket. Tranche 4 (cash and dry powder) does not
need any of this either. The middle two tranches are where SOUL #5's
"look at cash, look at quality" alpha sources live, and these are the
ratios that operationalise that look.

**Q: I have a stock with a low Z-score. Should I sell?**
A: Not on the basis of the score alone. First check the trend (is it
deteriorating, stabilising, or recovering?). Second check whether the
company is being correctly classified — banks, REITs, insurance, and
asset-light tech do not behave like 1968 manufacturers. Third look at
the bond market: if credit spreads on the company's debt are not
widening, the bond market does not believe the equity model. The
combination of a deteriorating Z trend and widening credit spreads is
the actionable signal, not either alone.

**Q: Can these ratios be gamed by management?**
A: Yes, all of them, partially. Working capital can be window-dressed
at quarter-end (factoring receivables, paying suppliers slowly).
Margins can be smoothed by changing inventory accounting. Even
bankruptcy probability can be lowered for a quarter by a debt-for-
equity swap that drives up book equity. The defence is the trend, not
the point. A company that consistently games one ratio will eventually
break another.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Advanced Financial Statement Analysis — DuPont, Cash
Conversion, and the Two Scoring Models Every Stock Picker Should Know

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00 to 1:20]**

**Stella:** Welcome back to Chanmainvest. Week 35. We have spent the
last twenty-something weeks building up the toolkit. Read the
statements, understand capital structure, separate cash from earnings,
discount cash to a fair value, then size with risk metrics. This week
we close the financial-statement-analysis arc with the four wrenches
that professional analysts actually pull out of the box every quarter.

**Horace:** Four tools, two pages of paper, half an hour per company.
DuPont decomposition. Cash conversion cycle. Beneish M-score. Altman
Z-score. None of them generate alpha by themselves. Together they make
up something almost as valuable — a *negative-alpha filter*. They tell
you which positions to think twice about before sizing up.

**Stella:** And we have a hands-on lab at the end of this week's
lesson where you can move sliders and watch the Z-score classification
flip in real time. Let us get into it.

---

**[SECTION 1 — DuPont, 1:20 to 5:00]**

**Stella:** First wrench. DuPont decomposition. Horace, walk us
through the identity.

**Horace:** Return on equity equals net income over equity. That is
the headline number on every annual report. DuPont splits that one
ratio into three. ROE equals net profit margin, times asset turnover,
times the equity multiplier. The middle two cancel algebraically — net
income over equity is mathematically the same thing — but the *split*
is information.

**Stella:** What kind of information?

**Horace:** Margin tells you the *quality of the business*. Turnover
tells you the *intensity of the assets*. Equity multiplier tells you
the *leverage*. Two firms with the same 17% ROE can be radically
different animals.

**[VISUAL: image/week35_dupont_compare.png]**

**Stella:** And the chart on screen now is exactly that comparison
across five very different firms — Apple, Microsoft, Coca-Cola, JPMorgan,
and Ford. Walk us through it.

**Horace:** Start with Apple on the left. Net profit margin around 24
percent. Asset turnover roughly 1.07. Equity multiplier 6.4. Multiply
those out and you get an ROE north of 150 percent. That equity
multiplier looks like leverage but it is mostly the buyback story from
Week 19 — Apple has retired so much equity that the denominator is
unnaturally small.

**Stella:** Microsoft next.

**Horace:** Margin even higher, around 36 percent. Turnover lower at
0.48 because they sit on a huge cash and intangible asset base.
Equity multiplier under 2. ROE in the high thirties. That is what a
clean software business looks like. Margin doing all the work.

**Stella:** Coca-Cola.

**Horace:** Margin 23 percent — brand premium. Turnover under 0.5,
because the brand is on the balance sheet as goodwill. Multiplier 4 —
moderate leverage. ROE in the low forties. Brand businesses always
have this shape. High margin, low turnover, modest leverage.

**Stella:** JPMorgan and Ford are interesting.

**Horace:** Both around 13 to 17 percent ROE — same headline, totally
different paths. JPMorgan: margin 37 percent on revenue, but turnover is
tiny — four cents of sales per dollar of assets. The leverage
multiplier is 11.6, because that is what banks are. They borrow short
and lend long. The ROE is built on leverage. Ford is the opposite:
turnover 0.65, almost twenty times JPM's, but margin only 3 percent.
Leverage 6.6. Same ROE, completely different fragility profile.

**Stella:** And the practical takeaway for an investor?

**Horace:** When ROE moves, ask which leg moved. If margin compressed,
that is a competitive issue. If turnover dropped, that is an asset
build-up issue. If the multiplier rose, that is the capital structure
moving — could be aggressive buybacks like Apple, could be debt-funded
acquisitions, could be losses eating into book equity. Three very
different stories with the same ROE shape.

---

**[SECTION 2 — Cash Conversion Cycle, 5:00 to 7:30]**

**Stella:** Second wrench. Cash conversion cycle.

**Horace:** Three components. DSO — how long customers take to pay.
DIO — how long inventory sits before selling. DPO — how long *you*
take to pay suppliers. CCC equals DSO plus DIO minus DPO. The number
of days a dollar of input spending stays trapped before coming back as
customer cash.

**Stella:** And why does it matter?

**Horace:** Because growth on a positive CCC is a working-capital tax.
Every additional dollar of revenue ties up more cash in receivables
and inventory. Costco, Apple, Amazon at certain points — they run
*negative* CCCs. Suppliers finance their inventory. They are paid
before they pay. Growth on a negative CCC is a cash *machine*. Growth
on a +90-day CCC is a cash *drain*.

**Stella:** What do I watch for?

**Horace:** Two things. First, the *trend*. Three rising quarters of
DSO is the most reliable advance warning of a revenue-recognition
problem. When the receivables grow faster than the sales, somebody is
booking revenue that customers do not feel obligated to pay yet.
Second, *direction versus competitor*. Compare to two named peers in
the 10-K. If your DSO is rising while the peer's is flat, the problem
is company-specific, not industry-wide.

**Stella:** Quick example?

**Horace:** Valeant Pharmaceuticals before its 2015 collapse — DSO
expanded from roughly 35 days in 2012 to over 100 days by 2015.
Receivables tripled while sales doubled. The CCC tripled. The
M-score eventually fired too, but the working capital number
diverged from the competitive set first. As Stella's Week 20 lesson
put it, cash is the fact and earnings are the opinion. CCC is one of
the cleanest readings of that fact.

---

**[SECTION 3 — Beneish M-score, 7:30 to 11:00]**

**Stella:** Third wrench. Beneish M-score.

**Horace:** Daniel Beneish, 1999. Eight one-year-change ratios combined
into a single probit-style composite. The math is uglier than DuPont;
the interpretation is simple. Above minus 1.78, the model classifies
the firm as a *probable manipulator*. Below, probably not.

**Stella:** What is each of the eight ratios capturing?

**Horace:** DSRI — receivables growing faster than sales. GMI — gross
margin deteriorating. AQI — asset quality, capitalised costs piling up.
SGI — sales growth itself, since fast growth tempts management to
smooth. DEPI — slowing depreciation, longer useful lives, lower
expense. SGAI — SG&A growth versus sales. LVGI — leverage trend. TATA
— total accruals, the Sloan piece from Week 20.

**Stella:** Track record?

**Horace:** Roughly 76 percent hit rate on known manipulators in
Beneish's original test set, with about a 17 percent false-positive
rate. It famously fired on Enron in 1997 — three years before the
collapse — and on WorldCom in 1999. It missed Wirecard, because
Wirecard's fraud was not earnings manipulation. It was making up the
cash balance. Different lie, different footprint, no M-score
signature.

**Stella:** So it is a screen, not a verdict.

**Horace:** Exactly. SOUL number five — alpha sources include "look at
the right numbers". M-score tells you *which 10-Ks to actually open
and read first*. When a name lights up, you read it carefully. When it
doesn't, you still read it, just with less urgency. That filtering
function is worth a lot, even if the model itself doesn't catch every
fraud.

---

**[SECTION 4 — Altman Z-score, 11:00 to 14:30]**

**Stella:** Fourth wrench. Altman Z-score.

**Horace:** 1968. Edward Altman at NYU. Multiple discriminant analysis
on 33 bankrupt and 33 non-bankrupt manufacturers. Five ratios, fixed
weights, single number. Z = 1.2 working-capital-to-assets, plus 1.4
retained-earnings-to-assets, plus 3.3 EBIT-to-assets, plus 0.6 market-
equity-to-total-liabilities, plus 1.0 sales-to-assets.

**Stella:** And the cutoffs.

**Horace:** Below 1.81, distress zone — bankruptcy probability in the
next two years is materially elevated. Between 1.81 and 2.99, gray
zone, watch list. Above 2.99, safe zone. Original test set had
roughly 80 to 90 percent accuracy.

**[VISUAL: image/week35_zscore_distress.png]**

**Stella:** Chart on screen. Three trajectories. GE, Ford, Apple.

**Horace:** GE is the textbook case. Trace the line. 2010, Z around
2.5 — gray zone, recovering from the 2008 crisis. 2012 to 2014, drifts
up toward 2.7. Then 2015, 2016, 2017 — slides through the gray zone
into distress. By 2018, Z below 1.3. That was the year of the dividend
cut and the Power-segment writedowns. The Z-score said "watch this" in
2015 and "this is in trouble" by 2017. The eventual breakup announced
in 2021 surprised nobody who had been tracking the ratio.

**Stella:** And Ford?

**Horace:** Ford has been parked in the gray zone for years. That is
about right for a US automaker — high asset intensity, cyclical
margins, real but manageable bankruptcy risk in any given downturn.
Ford did file for bankruptcy in many of GM's neighbouring years. Z in
the 1.5 to 1.7 band is the home address for a deep-cyclical
manufacturer. It is not a sell signal; it is a *position-sizing*
signal.

**Stella:** And Apple?

**Horace:** Z above 5 the entire stretch. Deeply safe. Brand business
with negligible debt-to-equity and a fortress cash pile. The Z-score
will never tell you when to *buy* a name like Apple, but it confirms
what you already suspected — there is no balance-sheet tail risk in
the position.

**Stella:** Common pitfalls?

**Horace:** Two. First, Z is calibrated for US manufacturers. There
are variants — Z-prime for private firms, Z-double-prime for
non-manufacturers and emerging markets — that change both
coefficients and cutoffs. Use the right one. Second, the *trend*
matters more than the level. A firm at Z = 1.5 and rising is in better
shape than a firm at Z = 2.5 and falling. Slope dominates altitude.

---

**[SECTION 5 — The Interactive Lab, 14:30 to 16:30]**

**Stella:** Let us walk through this week's interactive tool.

**[VISUAL: interactive/week35_fsa_lab.html]**

**Stella:** Two panels. On the left, the Altman Z-score calculator.
You can pick a preset firm — Apple, Microsoft, Ford, GE in 2018, or
Lehman in 2007 — or punch in your own five components. The Z is
computed live, and the band classification on the right flips between
distress, gray, and safe as you move the inputs.

**Horace:** Try the Lehman 2007 preset. Z under 1.0. Distress band, a
year before the bankruptcy. The market did not know; the model did.

**Stella:** On the right, three sliders for DuPont. Net profit margin,
asset turnover, equity multiplier. Watch the resulting ROE. Set
margin 24 percent, turnover 1.0, multiplier 6 — you get an Apple-
shaped ROE in the 140s. Drop the multiplier to 1, ROE collapses to 24.
That is what the buyback story is doing under the hood.

**Horace:** The four locales are wired up — English, Hong Kong
traditional, Taiwan traditional, mainland simplified. Theme switcher
on the page header swaps the chart palette. Embed it directly into
your study notes if that helps.

---

**[OUTRO — 16:30 to 18:00]**

**Stella:** Recap. Four wrenches. DuPont splits ROE into margin,
turnover, leverage. CCC splits days into receivables, inventory,
payables. M-score scores the manipulation footprint. Z-score scores
the bankruptcy probability. Together they are the negative-alpha
filter — they will not find you the next Apple, but they will keep
you out of the next Valeant.

**Horace:** SOUL number one — alpha is rare. The corollary is that
*avoiding negative alpha is cheap*. A two-page diligence sheet costs
you thirty minutes per name. The names you decide *not* to size up
because of what those sheets show you — that is the yield on this
half-hour.

**Stella:** Next week we move from financial statements into industry
analysis — Porter's five forces, competitive moats, and the kind of
qualitative work that DCF assumptions rest on but rarely justify.

**Horace:** And eventually, in Tranche 3 territory, we put all of this
together into single-name selection. Not yet. First, the rest of the
toolkit.

**Stella:** Until next week.
