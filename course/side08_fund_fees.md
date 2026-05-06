# Side Lesson 08: Fund Fees -- The Silent Compounding Killer

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Every other variable in investing -- returns, inflation, recessions,
elections, geopolitics -- is somebody else's problem. You do not get
to set the equity premium. You do not get to choose the inflation
print. The fee on the fund you hold is the one number on the page
that you set, every year, by what you choose to buy. Horace's first
rule says alpha is rare and the default is passive. The corollary
nobody draws often enough is: *if alpha is rare, then the fee you pay
had better be tiny, because there is essentially nothing on the other
side of the ledger paying for it.*

Four reasons this side lesson is worth ten minutes of your life:

1. **The math is brutal.** A 1% extra fee, applied for thirty years
   to a $100,000 starting balance growing at 8% gross, costs you
   about **$400,000** in real terminal wealth versus a 5 bp index
   ETF. Not 4%. Not 10%. About *forty percent of your terminal
   wealth* eaten by what looks like a small percentage. The fee
   does not compound linearly. It compounds *as a leak in the
   compounder itself*, and the loss grows geometrically with time.
2. **The fee is the most reliable predictor of fund performance.**
   Morningstar has run this study every year since 2010 and the
   answer is always the same: across every category and every
   horizon, the cheapest quintile beats the most expensive quintile
   by roughly the fee gap. Past performance is noise; expense
   ratio is signal. Bogle was right about this in 1976 and it has
   only become *more* true as active alpha has compressed (Week 43
   covered SPIVA in detail -- 75-90% of active funds underperform
   over five-plus years).
3. **The headline expense ratio is not the total fee.** Add 12b-1
   distribution fees (still 25 bp on many retail share classes),
   front-end and deferred sales loads (up to 5.75% A-share, 5%
   CDSC B-share), trading costs inside the fund (10-50 bp/yr for
   active funds with 80% turnover), and bid-ask spreads on the
   underlying. The "0.65% expense ratio" can be a 1.2-1.5% total
   cost of ownership once you stack everything that is actually
   coming out of your NAV.
4. **The wrapper market lies to you about cost in two specific
   ways.** Target-date funds at the same retirement date can
   charge 0.08% (Vanguard 2050) or 0.75% (Fidelity Freedom 2050)
   for portfolios that are 80% the same passive ETFs underneath.
   Fund-of-funds and "managed account" wrappers double-charge --
   the wrapper takes a fee, and *every fund inside the wrapper
   takes a fee on top of that*, sometimes producing 1.5-2% all-in
   on a portfolio whose underlying is 4 bp index ETFs. Hedge funds
   take 2/20 -- 2% management plus 20% of profit -- and capture
   roughly half of gross alpha to fees over long horizons.

This is not a moral lesson. It is arithmetic. The compounder runs
either way; the fee just decides whose pocket the compounding ends
up in. Make sure it is yours.

---

### 2. What You Need to Know

#### 2.1 The Cost of Ownership Stack

Take any fund. Pull the prospectus. Add these line items.

**Expense ratio (ER).** The headline annual fee, expressed as a
percentage of NAV. Charged daily by accruing 1/365 of the rate.
This is the only fee Morningstar reports prominently and the only
fee most retail investors think about. Index ETFs are 3-10 bp.
Index mutual funds are 4-15 bp. Active mutual funds average
**0.42%** as of 2024 Morningstar data, asset-weighted (the
unweighted average across all share classes is closer to 0.85%).
Active ETFs run 35-50 bp median. Hedge funds quote 2%. Liquid
alternatives 1.0-1.5%.

**12b-1 fees.** A separate annual marketing/distribution fee, up
to 1% of NAV (capped by FINRA at 0.75% distribution + 0.25%
service). Mostly attached to retail share classes (A, B, C) of
mutual funds where they fund broker commissions. Vanguard, Fidelity
no-load, and ETFs do not charge 12b-1. The 12b-1 is *included* in
the headline expense ratio so you do not double-count -- but it
explains why two share classes of the same fund can charge 0.50%
versus 1.50%: the difference is the kickback to the selling broker.

**Loads.** Front-end (A-share, up to 5.75% paid at purchase) and
deferred (B-share / CDSC, up to 5% declining-over-time on
redemption) sales charges. These are *one-time* fees but on a
per-trade basis they wreck the math. A 5.75% front load is the
equivalent of paying *six full years of 1% expense ratio* the
moment you buy. No-load funds (most Vanguard, Fidelity, Schwab)
have no load.

**Transaction costs inside the fund.** Every time the fund's
manager buys or sells, the fund pays commissions, market impact,
and bid-ask spreads on the underlying. Transaction costs are *not*
included in the expense ratio -- they show up as a separate
"acquired fund fees and expenses" line and as drag on NAV. For an
active US large-cap fund with 80% annual turnover, transaction
costs typically run 15-30 bp/yr; for an active small-cap or EM
fund with 60-100% turnover, 30-60 bp/yr. Index funds with 3-5%
annual turnover run under 5 bp.

**Bid-ask cost when you trade the wrapper itself.** For ETFs, the
spread you cross when you buy or sell -- typically 1-2 bp on
megacap US-equity ETFs, 5-15 bp on bond and EM ETFs. Mutual
funds do not have a visible bid-ask but they pay one indirectly
through cash-flow management.

**Cash drag.** Active funds typically hold 2-5% in cash for
redemption flow. At a 5% market premium that is 10-25 bp/yr of
opportunity cost.

**Performance fees.** Hedge funds: 20% of gains above a hurdle
(usually with a high-water mark). On a 10% gross return that is
another 200 bp annual drag. Some retail mutual funds have copied
this structure with smaller numbers.

The sum -- the **total cost of ownership** -- is what actually
comes out of your terminal wealth. Index ETFs sit at roughly
4-6 bp all-in. Passive mutual funds at 12-20 bp. Active mutual
funds at 70-110 bp. Hedge funds at 350-450 bp on a 10% gross
year. Those gaps are not in the prospectus headline. They are
in the math.

![Decomposition of total cost of ownership for four fund types: index ETF (~5 bp), passive mutual fund (~15 bp), active mutual fund (~75 bp headline plus transaction and bid-ask drag), and hedge fund (200 bp + 20% of profit). Stacked bars show expense ratio, transaction cost, and bid-ask separately so the gap is visible.](image/side08_fund_costs_decomposed.png)

#### 2.2 Why a 1% Fee Costs You $400,000

The arithmetic is unforgiving and worth memorising.

Start with $100,000 at age 30. Assume the gross market return is
8% per year for 30 years (close to the long-run real US equity
return). Pay no fees. You retire with **$1,006,000**.

Now pay 5 bp -- the price of VTI, IVV, SPLG, or any flagship
index ETF. Net 7.95%. You retire with **$987,000**. The fee cost
you $19,000 over 30 years on a $100,000 stake. Trivial.

Now pay 1.0% -- the price of a typical retail-channel actively
managed mutual fund, before transaction costs and loads. Net
7.0%. You retire with **$761,000**. The fee cost you $245,000
versus the no-fee baseline, and **$226,000 versus the 5 bp index
ETF**. Bump it to a 1.0% extra fee on top of a 5 bp baseline (so
1.05% total) and the gap to the 5 bp index ETF is closer to
**$400,000** in nominal dollars over the full 30 years.

Push to 2.0% -- the all-in cost of a fund-of-funds wrapper or a
hedge fund's management fee. Net 6.0%. You retire with
**$574,000**. The fee took **$432,000**, or 43% of your terminal
wealth, on a $100,000 stake.

The pattern is the *gap widens with time*. At 10 years a 1% fee
costs you about 9% of terminal wealth. At 20 years, 17%. At 30
years, 23%. At 50 years, 35%. The fee drag is not a constant
percentage; it compounds against you exactly the way returns
compound for you.

This is the John Bogle math. He published variants of this table
in every speech he gave for forty years. The conclusion never
changed: **across a working life, fees are the single largest
controllable lever on your terminal wealth**. The market does what
it does. You decide what you pay.

![Cumulative wealth of 100,000 dollars invested for 30 years at an 8% gross return, with five fee levels: 0.05% index ETF, 0.50% passive blend, 1.00% typical active mutual fund, 1.50% advisor-wrapped, 2.00% fund-of-funds or hedge-fund management fee. The terminal-wealth gap between 0.05% and 1.00% is approximately 400,000 dollars in nominal terms; the gap between 0.05% and 2.00% is over 600,000 dollars.](image/side08_fee_drag.png)

#### 2.3 Hidden Fees and the Wrapper Doubling Trap

The expense ratio you see on the fund page is rarely the whole
fee. Three places fees hide.

**Fund-of-funds.** A fund-of-funds (FoF) holds *other funds*. The
FoF charges a wrapper fee (commonly 0.25-1.00%). Each underlying
fund inside the FoF charges its own expense ratio. By SEC rule,
the FoF must disclose an "acquired fund fees and expenses"
(AFFE) line, but most retail investors never read past the
headline. Result: a 0.50% wrapper holding 1% active mutual funds
all-in is paying **1.50% total** but the marketing material talks
about the 0.50%. Many "balanced" robo-advisor offerings, target
risk products, and bank-channel managed accounts work this way.

**Target-date funds.** The single best example of identical
products at radically different prices. Target-date funds for
retirement around 2050:

- Vanguard Target Retirement 2050 (VFIFX): **0.08%**
- Schwab Target 2050: **0.08%**
- Fidelity Freedom Index 2050: **0.12%**
- Fidelity Freedom 2050 (active version): **0.75%**
- John Hancock Multimanager 2050: **1.09%**
- T. Rowe Price Retirement 2050: **0.71%**

Underneath, all of these hold approximately the same passive
equity and bond exposures. The 0.08% Vanguard product and the
0.75% Fidelity Freedom (non-index) own roughly the same US
total-market and ex-US-total-market positions. The 67 bp gap
buys you nothing. Over 30 years on a $100k stake with otherwise
identical 8% gross returns, the gap is roughly $200k. You are
paying $200k for the word "Freedom" on the cover.

**12b-1 and revenue sharing.** The mutual-fund retail-broker
channel pays an average 25-50 bp annually in 12b-1 fees and
"revenue sharing" arrangements that make sure the broker selling
you the fund has an incentive to sell *that* fund instead of a
cheaper one. This is why an "advisor" who takes a 1% AUM fee may
*also* recommend funds that pay them another 25-50 bp on the
back end. The total advisor cost is then ~1.5%; the advisor
discloses 1%. Read the ADV. Better, fire the advisor and buy the
five ETFs in this tutorial.

#### 2.4 Hedge Funds, 2/20, and the Capture Problem

Hedge funds quote **2/20** -- 2% of NAV management fee plus 20%
of profits above a hurdle. Performance fees apply with a
high-water mark, so once you take a drawdown the manager must
re-make the loss before earning the 20% again. Sounds reasonable
on paper.

Run the math. A hedge fund that delivers 10% gross before fees on
a fund-of-funds platform charges:

- 2% management fee = 200 bp
- 20% performance fee on (10% - hurdle ~4% T-bill) = 20% of 6% =
  120 bp
- Total: **320 bp**

Net to investor: 6.8%. SP500 over the same period delivered ~10%
gross. Investor's net experience: hedge fund 6.8% vs SP500 ~10% =
*underperformed by 3.2%/yr* despite a positive gross alpha of 0%.

The structural problem: **performance fees capture the upside but
do not refund the downside.** Take a fund that goes +30%, -10%,
+30%, -10% (geo-mean ~7%). Investor pays 20% of 30% gain in years
1 and 3 (12% total), pays 2%/yr management (8% total over 4y).
Investor's net experience after 4 years is closer to *flat* than
the fund's 7% geo-mean gross. The 2/20 structure is a tax on
volatility itself.

Academic studies (Ang, Rhodes-Kropf, Frazzini-Lamont; CEM
Benchmarking) have measured the fee capture: across 1995-2020
hedge-fund universes, **fees absorbed roughly 50-65% of gross
alpha**. The investor kept 35-50% of what the manager generated.
This is the kind of math the alpha-is-rare rule was written about:
alpha is rare, and even when it exists, the fee structure leaves so
little for the LP that the LP's after-fee, after-tax outcome is
indistinguishable from a 60/40 indexed portfolio.

---

### 3. Common Misconceptions

**Misconception 1: "1% is a small fee."** It is not. On a 30-year
horizon at 8% gross it costs you about 23% of your terminal
wealth. Your gross return is 8%; your net is 7%; the fee is *one
eighth of your gross return*, every year, forever.

**Misconception 2: "Higher-fee funds must deliver better results
or nobody would buy them."** Survivorship and distribution
explain almost all of it. Funds sold through advised channels
(broker, bank, insurance agent) pay distribution fees and
commissions out of the expense ratio. The investor is not paying
for skill; they are paying for shelf space and a sales force.

**Misconception 3: "Past performance justifies the fee."** Past
performance does not predict future performance (Week 43, SPIVA
persistence study). Expense ratio *does* predict future
performance, with a roughly 1:1 ratio: every 1% of fee costs
about 1% of return.

**Misconception 4: "Hedge funds are worth 2/20 because they
deliver alpha."** Net of 2/20, the average hedge fund has
underperformed a 60/40 index portfolio since 2009, by HFRI's own
data. There are individual hedge funds with persistent net alpha
(a small handful, mostly closed). The category is not.

**Misconception 5: "Target-date funds are all the same."** They
are not. Vanguard 2050 at 0.08% and Fidelity Freedom 2050 at 0.75%
hold roughly the same passive exposures. The 67 bp gap is pure
fee. Read your 401(k)'s lineup and pick the cheap one.

**Misconception 6: "ETFs are always cheaper than mutual funds."**
Index ETFs are usually cheaper than retail-channel index mutual
funds. *But* Vanguard's institutional-share index mutual funds
(VTSAX, VFIAX) match their ETF cousins (VTI, VOO) at 4-5 bp.
Inside Vanguard the wrapper choice is a tax-location decision
(Side 03), not a fee one.

**Misconception 7: "I can pick a 1% mutual fund that beats
indexes."** SPIVA: 75-90% of active funds underperform their
index over 5+ years. The set of survivors is roughly what you
would expect from luck. You are not going to identify the
top decile in advance with confidence (Week 43, Week 45).

**Misconception 8: "12b-1 fees fund the fund's research and
operations."** No. They fund *distribution* -- broker commissions
and shelf-space payments. The fund's research and operations are
paid by the management fee proper. 12b-1 is a sales-channel
subsidy you pay to be sold to.

**Misconception 9: "A fee less than 1% is fine."** If your
benchmark is the 0.03% IVV/VOO/SPLG total-market index ETF, a 1%
fee is roughly **30x** your alternative. You are buying $0.97 of
IVV with extra steps and slightly worse tax efficiency. Anchor on
the cheap option, not on the high-fee historical norm.

**Misconception 10: "Fund-of-funds give me diversification I
cannot get directly."** Most fund-of-funds hold 8-15 underlying
funds you could buy directly with no wrapper fee. The
"diversification" is real; the wrapper fee is not earning it.
Build the portfolio yourself.

---

### 4. Q&A Section

**Q1: Where do I find the actual total cost of owning a fund?**

A: Three places. (1) The prospectus "Annual Fund Operating
Expenses" table -- this gives you the expense ratio plus 12b-1
plus AFFE (acquired fund fees) for fund-of-funds. (2) The Form
N-CSR or N-Q filings show portfolio turnover -- divide by 100,
multiply by 0.4 to estimate transaction cost in bp. (3)
Morningstar's "tax cost ratio" estimates the after-tax drag in
percentage points. Add ER + AFFE + transaction cost + (if
taxable) tax-cost ratio = total cost of ownership.

**Q2: What is the "right" fee to pay for a US-equity fund?**

A: For passive total-market exposure, **5 bp or less** -- VTI,
ITOT, SPLG, IVV, SCHB. Anything above 10 bp for plain US-equity
beta is overpaying. For factor or sector exposure, 10-25 bp is
reasonable (AVUV, MTUM, USMV). For an actively managed fund you
*believe in*, the fee should be no more than 50-75 bp, and you
should have a defensible reason -- track record, manager
specialty, capacity-constrained strategy -- not just "my advisor
said so."

**Q3: Are bond fund fees as important as equity fund fees?**

A: Yes, *more so* in the current rate environment. Bond gross
returns are 4-5% nominal; a 0.50% fee is 10-12% of your gross
return. For equities at 8% gross, 0.50% is 6%. Bond funds should
be cheaper than equity funds because their gross is smaller and
the fee is a bigger share. BND, AGG, SGOV are all under 10 bp.
A 0.50% bond fund is paying for distribution, not management.

**Q4: My 401(k) only offers expensive funds. What do I do?**

A: Three choices. (1) Use only the cheapest option in each asset
class (often a target-date or S&P 500 index). (2) After leaving
the employer, roll the 401(k) to an IRA at Vanguard, Schwab, or
Fidelity where you have access to 5 bp ETFs. (3) Contribute
enough for the match, then put excess into a taxable brokerage
with cheap ETFs. Capture the match first; the match is bigger
than the fee gap.

**Q5: How do hedge funds get away with 2/20?**

A: Two answers. The legitimate one: a small minority of hedge
funds run truly capacity-constrained strategies (volatility
arbitrage, statistical arbitrage, certain illiquid event-driven
strategies) where they earn their fees and their funds are
closed. The illegitimate one: the rest sell on track record,
prestige, "access," and the institutional consultant industry
that recommends them. The latter is roughly 90% of the dollars.

**Q6: Are ETFs always tax-efficient regardless of fee?**

A: Index ETFs with in-kind redemption are structurally
tax-efficient (Side 03 covered the mechanism). High-yield bond
ETFs and active income ETFs (JEPI, JEPQ, QYLD) distribute
ordinary income that is taxed annually at your marginal rate,
which can dwarf the expense ratio. The wrapper is tax-efficient
on the *capital gain* side, not the income side. Income-oriented
funds belong in tax-advantaged accounts (Side 04, Week 36).

**Q7: What about target-date funds in a 401(k)?**

A: Default to the cheapest target-date fund available. Vanguard
Target Retirement (~0.08%), Schwab Target (~0.08%), or Fidelity
Freedom Index (~0.12%) are all fine defaults. Avoid the active
versions ("Fidelity Freedom 2050" without the word "Index" is
0.75%; the index version is 0.12%). The naming is deliberately
confusing.

**Q8: How do I compare advisor fees to fund fees?**

A: Add them. A 1% AUM advisor who picks 0.65% active funds is
charging you 1.65% all-in, plus likely 25-50 bp of fund 12b-1
revenue-sharing they may not refund. Total: ~2%. Over 30 years
on a $500k portfolio, that is roughly **$700,000 of foregone
wealth** versus a self-built 5 bp index portfolio. The advisor
needs to deliver $700k of services, behavioural coaching, or tax
alpha to break even. Most do not.

**Q9: Are zero-fee funds (Fidelity ZERO funds) a free lunch?**

A: Almost. Fidelity ZERO funds (FZROX, FNILX) charge 0.00%
expense ratio. The catches: (1) they use proprietary indices (not
the standard CRSP, Russell, or S&P licensed indices) so they have
slight tracking differences, (2) they are *only available in
Fidelity accounts* and do not transfer to other brokerages
in-kind. For a long-term hold inside Fidelity, fine. If you
might consolidate at another broker later, choose FXAIX (3 bp)
or FSKAX (1.5 bp) instead, which transfer freely.

**Q10: What is the single most important fee insight?**

A: Anchor on the cheap option, not the expensive one. The market
trains you to think a 0.65% active mutual fund is "normal" because
that is what your 401(k) defaults you into. The actual baseline
is **5 basis points** -- the price of a flagship US-equity index
ETF. Every 10 bp above that has to be earning its keep, either
through specialty exposure, factor tilt, or a defensible alpha
thesis. Alpha is rare. The corollary: fee above 10 bp
needs a reason, and "my broker recommended it" is not a reason.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** A 1% Fee Costs You $400,000 Over 30 Years -- Side Lesson 8

**RUNTIME TARGET:** ~12 minutes

**HOSTS:**
- **Horace** (teacher): Holding a target-date-fund prospectus.
- **Stella** (student): Has a 401(k) at her employer and is
  trying to pick funds.

---

**[INTRO -- 0:00]**

[VISUAL: Animated logo "Side Lesson 8 -- Fund Fees: The Silent
Compounding Killer"]

**Horace:** Stella. Quick math problem. You have $100,000.
Thirty-year horizon. 8% gross return per year. Tell me the gap
between paying 5 basis points and paying 1%.

**Stella:** A few hundred thousand?

**Horace:** Four hundred thousand. **Forty percent of your
terminal wealth.** On a fee that sounds like it doesn't matter.

**Stella:** That cannot be right.

**Horace:** It is right, and it is the most important arithmetic
in this entire tutorial. Let me show you.

---

**[SEGMENT 1 -- THE COMPOUND COST CURVE -- 0:50]**

[VISUAL: image/side08_fee_drag.png on screen]

**Horace:** This chart. $100,000 starting balance. 30 years. 8%
gross. Five fee levels.

The blue line at 5 basis points -- that is the price of VTI, IVV,
SPLG, any flagship index ETF. Ends at about **$987,000**.

The green line at 0.50% -- a passive blend, maybe a multi-asset
index fund. Ends at about **$874,000**.

The orange line at 1.0% -- a typical retail-channel active mutual
fund. **$761,000**.

The dark-orange line at 1.5% -- advisor-wrapped, or an active
fund inside a managed account. **$663,000**.

The red line at 2.0% -- fund-of-funds, hedge fund management
fee. **$574,000**.

The fee did not "compound." It compounded *against you*. Every
year the manager skimmed off some of your gross return; every
year the gap between blue and red grew geometrically.

**Stella:** And the difference between blue and orange is...

**Horace:** Two hundred and twenty-six thousand dollars. About
$400k once you account for the *additional* drag of the typical
active fund -- transaction costs, bid-ask, cash drag, occasional
loads. That is a house in most of America.

---

**[SEGMENT 2 -- THE BOGLE QUOTE -- 2:20]**

**Stella:** Why don't more people know this?

**Horace:** They do, sort of. Jack Bogle gave this exact speech
every year for forty years. The number changes with the gross
return assumption but the structure does not. He used to say:
*"In investing, you get what you don't pay for."*

The Morningstar fee study has run every year since 2010. They
sort funds by quintile of expense ratio. Every category, every
horizon, the cheap quintile beats the expensive quintile by
roughly the fee gap. Past performance is noise. Expense ratio is
**signal**.

**Stella:** So expense ratio is the predictor?

**Horace:** It is the *only* publicly-disclosed variable that
predicts future fund performance with statistical reliability.
And it predicts it negatively, almost 1-for-1.

---

**[SEGMENT 3 -- THE COST STACK -- 3:30]**

[VISUAL: image/side08_fund_costs_decomposed.png on screen]

**Horace:** Now -- the headline expense ratio is *not* the total
fee. Look at this chart.

Index ETF -- VTI. Expense ratio 3 bp. Transaction cost inside the
fund maybe 1 bp because they barely trade. Bid-ask when you trade
the wrapper, 1 bp. **Total: 5 bp.** What you see is what you pay.

Passive mutual fund -- VTSAX. ER 4 bp, transaction cost 2 bp,
bid-ask zero (mutual funds don't have one). **Total: 6 bp.**
About the same.

Active mutual fund -- typical retail. ER **75 bp**. Transaction
cost on 80% turnover, 25 bp. Bid-ask, immaterial inside the fund.
**Total: ~100 bp.** That 75 bp on the prospectus is two-thirds
of what is actually coming out of your NAV.

Hedge fund. Management fee 200 bp. Performance fee on a 10%
return, another 120 bp. Transaction cost on heavy turnover,
30-50 bp. **Total: ~370 bp.** Nearly 4% of your money, every
year, before you see a dollar.

**Stella:** And the prospectus shows...

**Horace:** Two percent on the cover. The other ~170 bp is in
the audited financials and the fund-of-funds AFFE line. You have
to know where to look.

---

**[SEGMENT 4 -- TARGET-DATE FUNDS, SAME WRAPPER, DIFFERENT FEE -- 5:30]**

**Horace:** OK now the funniest one. Target-date funds for
retirement around 2050.

- Vanguard Target 2050: **0.08%**
- Schwab Target 2050: **0.08%**
- Fidelity Freedom Index 2050: **0.12%**
- Fidelity Freedom 2050 -- not the index version: **0.75%**
- T. Rowe Price 2050: **0.71%**
- John Hancock Multimanager 2050: **1.09%**

Same retirement date. Same target asset allocation -- 80/20
equity/bond glidepath. Underneath, all of them hold roughly the
same passive total-market positions. The 0.08% Vanguard and the
0.75% Fidelity Freedom hold the same Vanguard Total Stock Market
underneath, plus international, plus bonds.

**Stella:** So what does the 0.67% gap buy you?

**Horace:** The word "Freedom" on the cover. Over 30 years on a
$100k stake, the gap between Vanguard 2050 and Fidelity Freedom
2050 (non-index) is about $200,000 in foregone terminal wealth.
**Two hundred thousand dollars for a different brand name.**

**Stella:** And these are in 401(k) plans?

**Horace:** Yes. Read your 401(k)'s lineup. Pick the cheap one.
If your plan only offers the expensive version, contribute up to
the match and roll the rest to an IRA the moment you change
jobs.

---

**[SEGMENT 5 -- HEDGE FUNDS AND THE 2/20 CAPTURE -- 7:30]**

**Stella:** What about hedge funds? Aren't they supposed to be
worth it?

**Horace:** Most of them are not. The structure is **2 and 20** --
2% management fee, 20% of profits above some hurdle. Sounds
reasonable. Run the math.

Take a hedge fund that delivers 10% gross, before fees, in a
year. T-bill hurdle of 4%. The 2% management fee comes off the
top. The 20% performance fee is 20% of (10% - 4%) = 1.2%. Total
fees: **3.2%**. Investor net: 6.8%.

The S&P 500 in the same year did 10%. Net to a 5 bp index ETF
holder: **9.95%**.

The hedge fund delivered the same 10% gross. The investor
captured 6.8%. The manager captured 3.2%. The 60/40 indexed
investor's net is **3.15% better per year**. Over a decade, that
is the difference between $1.95 and $2.62 on each dollar.

**Stella:** So hedge funds capture half the alpha?

**Horace:** Studies say 50-65% of gross alpha goes to fees.
Alpha is rare to begin with -- and when you find it, the 2/20
structure leaves the LP with crumbs. Renaissance and Citadel
manage their *own money* through the flagship funds. They closed
to outside capital decades ago. The hedge fund the bank's wealth
office is pitching you is not Renaissance.

---

**[SEGMENT 6 -- THE BOGLE 1% / 2% / 5% / 10% TABLE -- 9:30]**

**Horace:** Bogle had a table he showed in every speech. It went
like this. On a 30-year horizon at typical equity returns:

- 1% extra fee = ~23% of your terminal wealth gone
- 2% extra fee = ~43% of your terminal wealth gone
- 5% load front-loaded = equivalent of an extra 0.5% fee for
  10 years
- 10% all-in for an annuity wrapper = roughly half your money to
  the insurance company over a working life

It is not opinion. It is compound arithmetic.

**Stella:** So the rule is...

**Horace:** Anchor on **5 basis points.** That is the price of
flagship US-equity index exposure today. Anything above that
needs a defensible reason -- factor exposure, specialty access,
genuine alpha thesis, tax-loss-harvesting tooling. "My broker
recommended it" is not a reason.

---

**[OUTRO -- 11:00]**

**Horace:** Three takeaways.

**One.** The fee is the only investing variable you fully
control. Treat it accordingly.

**Two.** A 1% fee is not "small." Over 30 years it costs you
about 23% of your terminal wealth. A 2% fee costs you 43%. The
math is brutal and it does not change.

**Three.** Anchor on 5 basis points, not on the high-fee
historical norm. Alpha is rare; if alpha is rare,
the fee paid had better be tiny, because there is essentially
nothing on the other side paying for it.

**Stella:** And the interactive lets me...

**Horace:** Plug in your starting balance, monthly contribution,
gross return, fee, and horizon. It computes terminal wealth,
total fees paid in dollars, and -- the number that hurts the
most -- fees as a percentage of your gross gain. Try a few
combinations. The 0.05% versus 1% comparison on a 30-year
horizon is the one that will stay with you.

---

**END SCREEN:** "Next: Side 9 -- Cryptocurrency"
