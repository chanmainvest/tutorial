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
   ones do not. Alpha is rare, but *avoiding negative alpha* is cheap,
   and a $0 ten-line spreadsheet is one of the cheapest sources.

The chart below shows what DuPont looks like when you put five very different
businesses next to each other. Apple is a margin machine with serious
leverage from buybacks. JPMorgan is a leverage machine with thin
margins and almost no asset turnover. Ford is a turnover machine with
both thin margins and meaningful leverage. The same 13–17% ROE is being
manufactured three different ways, and the path to a 0% ROE is
different for each.

![Side-by-side DuPont decomposition for five very different US large-caps — Apple, Microsoft, Coca-Cola, JPMorgan, and Ford. Each firm is shown as a stacked or grouped set of bars for the three DuPont legs: net profit margin, asset turnover, and equity multiplier. Apple shows ~24% margin × 1.07 turnover × 6.4 multiplier (a margin machine with buyback-amplified leverage); Microsoft is the cleanest software profile (high margin, low turnover, low multiplier); Coca-Cola is a brand business (high margin, low turnover, moderate leverage); JPMorgan is a leverage machine (huge multiplier ~12, thin turnover); Ford is a turnover machine (3% margin × 0.65 turnover × 6.6 leverage). Same headline ROE band, three structurally different paths to it.](../image/week35_dupont_compare.png)

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
[image/week20_accruals_anomaly.png](../image/week20_accruals_anomaly.png)).
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
*screening filter* — a tool for looking at the right numbers, not a
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

The chart below shows three trajectories. GE 2010-2024 (the deteriorate-and-recover
curve), Ford 2018-2024 (perpetually parked in the gray zone, which is
about right for a cyclical), and Apple 2020-2024 (deeply safe, the
shape of a brand business with a clean balance sheet). Same model,
same cutoffs, completely different stories.

![Time-series chart of the Altman Z-score for three US large-caps — GE, Ford, and Apple — across roughly 2010–2024. The y-axis shows Z; horizontal bands at Z=1.81 and Z=2.99 mark the distress / gray / safe zones. GE traces a deteriorate-and-recover curve: starts in the gray zone around 2.5 in 2010, drifts up briefly, then slides through gray into distress (below 1.3) by 2018 — the dividend-cut and writedown year — before partially recovering. Ford is parked in the gray zone (Z ~1.5–1.7) the entire stretch, the home address for a deep-cyclical manufacturer. Apple sits well above 5 throughout, deeply safe — fortress balance sheet, brand business. Same model, same cutoffs, three completely different stories.](../image/week35_zscore_distress.png)

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

None of this is alpha generation in the new-edge sense. It is the
opposite: it is the *negative-alpha filter*. Most amateur portfolios
underperform not because they failed to find the next Apple but because
they held a Bear Stearns or a Valeant or a GE in the 2017 stretch when
a five-minute screen would have asked them to think twice. The
[interactive lab](interactive/week35_fsa_lab.html) at the end of this
lesson lets you pick a preset firm or punch in your own numbers and
watch the Z-score band classification flip in real time.

**Horace's view — this work is defensive, not offensive, and the
textbook quietly misframes it.** The orthodox CFA framing puts DCF,
quality screens, and the Z-score on the *alpha-generation* side of
the ledger — as if a careful analyst, armed with these tools and a
clean spreadsheet, can systematically pick winners that the rest of
the market has missed. My own experience says that is the wrong way
to read this material. The market is right far more often than I am.
Genuine, articulable mispricings — the rare moments where I can
point to *exactly* where the crowd has it wrong and why — are not
what DCF produces; DCF produces a fair-value range that mostly
agrees, within a wide band, with where the stock already trades.
The honest read is that this entire toolkit is *negative-alpha
filtering*: it stops you being on the wrong side of an asymmetric
mispricing that the rest of the market has already priced in.

That reframing changes how you spend your time. If you treat
financial-statement work as alpha generation, you grind harder on
the marginal name, looking for an edge that probably isn't there
and overtrading when you talk yourself into one. If you treat it as
the negative-alpha filter — as the screen that decides which names
*never enter* the portfolio in the first place — you spend the same
hours much more productively. The real edges in this course are
elsewhere: macro, sector rotation, structural flow mispricings, the
occasional tax or instrument-structure advantage. The bottom-up
toolkit is what keeps you from owning the next Valeant, *not* what
finds you the next Apple. Worth doing carefully. Not worth
mistaking for the source of returns.

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
need any of this either. The middle two tranches are where the
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
