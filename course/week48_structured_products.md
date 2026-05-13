# Week 48: Structured Products — Buffer ETFs, Principal-Protected Notes, and Replicating Them DIY

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Wall Street's most reliable business is repackaging things you could
buy yourself, charging a fee for the wrapping, and selling the result
as a "solution." Structured products are the cleanest 2026 example.
Buffer ETFs and principal-protected notes have grown from a rounding
error in 2018 to over $50 billion in defined-outcome ETF assets and
several hundred billion in retail-distributed structured notes. The
marketing is irresistible — "S&P 500 upside up to a 18% cap, with a
15% downside buffer, over a 12-month period" — and the mechanics,
once you see them, are a strict subset of what Weeks 25 through 30
already taught you.

You need to understand these products for four reasons:

1. **They are aggressively pushed at retail.** Innovator (BUFR
   series), First Trust Cboe Vest (the FT series), and Allianz are
   running television and brokerage-platform campaigns explicitly
   framed at investors who lived through 2008, 2020, or 2022 and now
   want "protection." Your advisor, your 401(k) target-date overlay,
   your in-laws' brokerage statement — you will encounter these. The
   fastest way to evaluate them is to know the option positions
   inside.

2. **The mechanics are *exactly* the option structures from Weeks
   25–30.** Every buffer ETF is a long zero-coupon bond plus a
   bull-call-spread plus a short put — three pieces, all of which we
   priced together in Week 29 with Black–Scholes. Once you see the
   decomposition, the "magic" of the buffer disappears. Alpha is
   rare, and a 79bps fee for arithmetic you can reproduce in your
   own brokerage account is not alpha — it is a convenience tax.

3. **The fees are far higher than the prospectus number.** A buffer
   ETF's headline expense ratio is around 0.79%. The hidden costs —
   bid-ask on the underlying SPX options, the spread between the cap
   the issuer offers and the cap the structure could mathematically
   support, the timing of the quarterly reset — bring the all-in cost
   to roughly 1.5%. A retail principal-protected note from a bank can
   embed 2% to 4% of issuance fees inside the cap, term, and
   credit-spread haircut. The DIY equivalent, executed once a year on
   1-year SPX options, costs around 5 basis points of slippage per
   leg, or ~20bps total. That is a 7-to-30× cost ratio.

4. **The barbell and the tax wrapper still apply.** A barbell sits
   on the *base* of the portfolio (boring
   compounder) plus a small convex sleeve. A buffer ETF tries to
   sell you the *whole portfolio*: capped upside, cushioned
   downside, no convex sleeve. On the tax side, SPX options
   inside a DIY buffer are 1256 contracts — 60/40 long/short tax —
   while a buffer ETF is ordinary CG and the structured note is paid
   out as ordinary income at maturity. The post-tax difference
   compounds.

This lesson teaches the mechanics, the DIY replication, the
realistic fee comparison, and the conditions under which the
packaged product is actually worth its cost.

---

### 2. What You Need to Know

#### 2.1 What a Buffer ETF Actually Owns

A 1-year buffer ETF on the S&P 500 with a 15% downside buffer and an
18% upside cap is, on the inception date, a portfolio of three
positions on the underlying index (SPX or SPY):

1. **Long a 1-year zero-coupon Treasury** (or a synthetic
   equivalent) that returns par at maturity. This guarantees the
   principal delivery before any option payoff is computed.
2. **Long a 1-year bull-call-spread**, struck at-the-money on the
   bottom and 18% out-of-the-money on the top. This is the
   participation: you receive 1-for-1 upside up to the cap.
3. **Short a 1-year put** struck 15% OTM. This is what *finances*
   the spread. The premium you collect on the short put is exactly
   what pays for the long call leg of the spread, which is why the
   cap exists in the first place.

The four legs net out to a payoff that, at expiry, looks like:

- **Index up by more than 18%**: you receive 18%, capped.
- **Index up by 0% to 18%**: you receive the index's return, 1-for-1.
- **Index down by 0% to 15%**: you receive 0% (the buffer).
- **Index down by more than 15%**: you receive (index_return + 15%) —
  the buffer absorbs the first 15%, you take the rest.

![Buffer payoff at 1y: 15% downside buffer + 18% upside cap on SPY at $500. P&L curve traces -30% to +30% spot move. Flat line through buffer zone, then negative slope below buffer floor. Positive slope through participation zone, then flat at cap. Annotations mark buffer floor (-15%), cap (+18%), breakeven, and the four shaded regions: full loss, buffer, participation, capped.](../image/week48_buffer_payoff.png)

The shape is identical to what you would build by hand from four
SPX options. *That* is the central observation.

#### 2.2 The DIY Replication on 1-Year SPX Options

With SPY at $500 in April 2026, a 12-month buffer with the same 15%
buffer and 18% cap is replicated on SPX (10× the SPY notional, so
strikes are 5000-anchored). Per $50,000 of notional:

| Leg | Action | Strike | DTE | BSM Price |
|---|---|---:|---:|---:|
| 1 | Long zero-coupon T-bill notional | — | 365d | 95.79% par |
| 2 | Long SPX call | 5000 (ATM) | 365d | $310 |
| 3 | Short SPX call | 5900 (+18% cap) | 365d | $48 |
| 4 | Short SPX put | 4250 (-15% buffer) | 365d | $112 |

Net out:

- T-bill cost: $47,895 of $50,000 notional (1y at 4.3%).
- Bull-call-spread debit: $310 - $48 = $262 per share-equivalent.
- Short-put credit: $112 per share-equivalent.
- Net spread cost: $262 - $112 = $150 per share-equivalent ≈ 3.0%
  of notional.
- Add T-bill drag: total = ~$2,255 of explicit cost on $50,000 =
  4.5% of notional consumed by the structure, which is *exactly*
  what makes the cap 18% rather than the 21–22% it would be at zero
  cost.

Total slippage executing all four legs at the mid-point ± typical
retail spreads on 1y SPX options: roughly 5bps per leg × 4 legs =
**~20bps round-trip**, plus ~1–2 commissions per leg. Call it
25bps.

#### 2.3 The Fee Comparison Over 5 Years

Buffer ETFs in the Innovator BUFR series and First Trust Cboe Vest
series charge expense ratios in the 0.79%–0.85% range. Add typical
secondary-market bid-ask of ~12bps and you are at roughly 91bps per
year of explicit cost. Over a 5-year horizon, on a $100,000
starting balance, the wealth gap vs. the DIY equivalent is *not*
small.

![Wealth difference over 5y: BUFR ETF (91 bps/yr) vs DIY (25 bps slippage on a 1y reset, amortized as ~5 bps/yr). Bar chart on $100k starting capital with same gross 6% buffered return: BUFR ends ~$130,300 vs DIY ~$135,200. The $4,900 gap is the convenience tax, compounding.](../image/week48_diy_vs_etf.png)

The gap is ~$4,900 on $100k — roughly 3.7% of the starting balance
— purely from the fee differential. Scale to $500k and that is
$24,500 paid to a fund company for option trades you could place
yourself.

The honest counter-argument: the DIY version requires a Level 3
options account, four execution legs per year on roll dates, and
discipline through a year-long expiry cycle. The fund company is
selling the discipline plus the operational lift. Whether that is
worth 80bps/yr is the real question — and for most retail investors
who can run Week 30's spread builder, the answer is no.

#### 2.4 Principal-Protected Notes and Bank Credit Risk

Principal-protected notes (PPNs) are bank-issued debt instruments,
not ETFs. A typical 5-year structured note from a major US bank in
2026 might promise: "100% principal back at maturity; participation
in the S&P 500 with a 30% cap." On the surface this looks like a
buffer ETF with a longer term and no buffer-floor erosion.

What is buried in the prospectus:

- **Issuer credit risk.** When Lehman Brothers collapsed in 2008,
  investors holding Lehman-issued PPNs received pennies on the
  dollar in bankruptcy — even on notes that explicitly said
  "principal protected." The protection is unsecured senior debt of
  the bank. Stick to US-listed claims you can
  verify. ETFs are bankruptcy-remote; bank notes are not.
- **Embedded fees of 200–400 bps.** The bank prices the note such
  that the all-in expected cost to the investor is 2–4% of notional,
  amortised over the 5-year term. This shows up as a lower cap, a
  longer term, or a wider underlying participation discount.
- **Illiquidity.** PPNs trade rarely on the secondary market. If
  you need cash mid-life, the dealer who issued the note will quote
  a price that bakes in another 1–3% of haircut.
- **Tax treatment.** Principal-protected notes are typically taxed
  as ordinary income on the contingent payment at maturity (CPDI —
  contingent payment debt instrument rules), *not* capital gains.
  At a 32% federal bracket plus 5% state, this is a 19-percentage-
  point hit relative to qualified LTCG.

The DIY equivalent for the 5-year note above: a 5-year zero-coupon
Treasury for principal protection, plus 5-year SPX call options for
the upside. Both pieces are bankruptcy-remote (Treasury is the
sovereign, options are CCP-cleared). All-in cost: a tighter cap, no
issuer credit risk, no illiquidity, and 1256-contract tax
treatment.

**Horace's view — I do not buy structured notes.** Bank credit risk
is the unhedgeable risk in a US-equity-centric global portfolio
where the tail-hedge sleeve is supposed to *reduce* exotic
counterparty exposure, not add a new one — and the tax envelope on
a CPDI-classified note is meaningfully worse than the DIY 1256
alternative. The packaged product solves a problem retail investors
do not have. If you cannot place the four legs yourself, hold the
index; if you can, build the structure on Treasuries plus listed
options and keep the bank's profit margin in your own pocket.

The barbell-compatible DIY alternative is concrete and small. For a
5-year horizon: buy a 5-year zero-coupon Treasury sized to your
principal-protection target — that is the safety end of the barbell
expressing itself, with the issuer being the US Treasury rather
than a single bank balance sheet — then buy a 5-year SPX call (or a
small ladder of LEAPs rolled forward) sized to the participation
you wanted. Both legs are bankruptcy-remote, both are publicly
priced, and the call leg gets 1256 60/40 treatment instead of CPDI
ordinary income. The shape is exactly what the structured note was
trying to sell you, with the wrapper cost and the credit risk both
removed.

#### 2.5 The Three Conditions Under Which the Packaged Product Wins

There are situations where buying the wrapper is rational:

1. **Account constraints prevent options.** Many 401(k) plans and
   employer brokerage accounts do not permit options trading at
   all. In a non-options account, the buffer ETF is the only way to
   get the buffered exposure and the 80bps fee is unavoidable.
2. **Discipline failure mode.** If you know yourself well enough to
   suspect you would not actually execute the four-leg roll on the
   anniversary date — or worse, would close one leg early in a panic
   — the fund company is selling you the *commitment* to the
   structure. A buffer ETF cannot be "broken into" mid-period the
   way a self-managed structure can.
3. **Notional below ~$50k.** SPX options have a $100 multiplier.
   Below ~$50k of notional you are forced into SPY options, which
   are more expensive, less tax-efficient (no 1256 treatment until
   they are SPX-cash-settled), and require more contracts. The fund
   company's pooling lets sub-$50k accounts access the SPX-priced
   structure indirectly.

Outside these three conditions, the DIY version is strictly better
on cost and tax. Alpha is rare, and 80bps for an
arithmetic identity is not alpha.

#### 2.6 The Barbell Read on Buffered Products

The barbell view frames the portfolio as a base (boring,
compounding) plus
a small convex sleeve. Buffered ETFs collapse both legs into a
single flat-payoff structure: capped upside, buffered downside,
convex sleeve sold to *finance* the structure (the short put leg).
At the portfolio level this is *anti-barbell*: you have given up
the convex left tail (because the short put leg loses badly past
the buffer) and you have given up the convex right tail (because
of the cap). What remains is the middle of the distribution.

For most retail compounders this is the wrong trade. The middle of
the distribution is what you already get from index funds; the
tails are where the volatility-tail-wags-the-dog effect
compounding shows up. Paying 80bps to *delete* both tails is not
insurance — it is a tactical bet that the index will spend the year
between -15% and +18%. The 1928–2024 base rate for that range is
roughly 55%.

---

### 3. Common Misconceptions

1. **"Buffer ETFs protect my principal."** No — they buffer the
   first 15% of a drawdown over the *outcome period* (typically 1
   year). Below the buffer, you take the full loss minus the buffer
   amount. In a 2008 scenario (-37%), a 15%-buffered product loses
   -22%, not zero.

2. **"The 18% cap is generous because the market rarely returns
   that much."** The 1928–2024 S&P 500 returned more than 18% in
   roughly 36% of calendar years. The cap binds more than 1 in 3
   years.

3. **"Principal-protected notes are safer than ETFs."** They are
   *less* safe in one critical dimension: bank credit risk. ETFs are
   bankruptcy-remote trusts; PPNs are unsecured debt of the issuer.
   Lehman PPNs returned ~9 cents on the dollar in 2008.

4. **"The fee is just the expense ratio."** The all-in cost of a
   buffer ETF includes the spread between the cap offered and the
   theoretically achievable cap (typically 50–100bps), the bid-ask
   on the underlying SPX options the fund executes (10–30bps), plus
   the headline expense ratio (~80bps). Total is closer to 1.4%.

5. **"Buffer ETFs reset annually so I always have protection."**
   The reset only protects against losses in the *new* outcome
   period. If the market drops 10% in month 11 and recovers 5% in
   month 12, your *current* buffer absorbs nothing because the
   buffer is measured from the *period start*, not from your peak.

6. **"DIY replication is too complex for retail."** Four legs of
   SPX options, executed once per year on the anniversary date,
   with strikes computable from a Black–Scholes calculator. Week 30's
   spread builder already showed this is Level 3 retail homework.

7. **"The buffer means I can sleep through a bear market."** Until
   the market drops more than 15%, after which every percent down
   is 1-for-1 yours. A -30% year on a 15-buffer product is -15%,
   which is *not* sleeping-well territory.

8. **"Banks would not sell something they expect to lose money for
   the client."** Banks price PPNs with 2–4% of profit baked in.
   They expect to make that profit on average. The client pays it
   either as opportunity cost (a worse cap), liquidity cost (no
   secondary market), or tax cost (CPDI rules).

9. **"Defined-outcome means defined-good-outcome."** The outcome is
   defined; whether it is *good* depends on what the index does.
   The structure is still a directional bet — narrower than a
   long-only equity bet, but a bet nonetheless.

10. **"If I do not need the buffer, I can sell the ETF mid-period."**
    You can, but you receive the secondary-market price, which
    reflects the *current* mark-to-market of the underlying option
    structure — not the "buffer" or "cap" advertised. Mid-period
    holders have no buffer; they have an opaque option exposure.

---

### 4. Q&A Section

**Q1: Why does the cap exist in the first place?**
Because the short-put leg is what finances the bull-call-spread
leg. The premium implicitly received on the short put is fixed by
implied volatility on the buffer strike. That premium is enough to
pay for *some* of the upside spread, but not all of it — so the
upper strike of the spread is set at the level where the math
balances. Higher IV → wider achievable spread → higher cap.

**Q2: Can I get a buffer larger than 15%?**
Yes — there are 20% and 30% buffer products in the Innovator series.
The cost is a lower cap (typically 10–13% on a 30-buffer product).
The deeper buffer requires selling a more-OTM put (less premium)
plus a more-OTM call (less premium received from the sold call leg
of the upper bound), so the achievable cap shrinks roughly linearly.

**Q3: How does this interact with the 1256 tax treatment from
Week 39?**
SPX options are Section 1256 contracts and receive 60/40 long-term/
short-term treatment regardless of holding period. A DIY buffer
implemented on SPX options inherits this — the realized P&L at
expiry or close is taxed at the blended 1256 rate (~21.8% at a 32%
ordinary bracket). A buffer ETF holds the options inside the fund,
so you get *fund-level* tax: ordinary CG on distributions and your
own LTCG/STCG on the ETF shares depending on holding period. PPNs
are taxed as ordinary income under CPDI rules. Ranking from best
to worst at a 32% bracket: DIY SPX (~21.8%) > buffer ETF (LTCG
15–20% on ETF shares, but you pay annual ordinary CG distributions
on internal P&L) > PPN (32%+).

**Q4: What happens if I buy a buffer ETF mid-period?**
You inherit the *remaining* buffer and cap from the period-start
strikes. If the market is already +10% into the period and you buy
in, your effective upside is now the cap minus 10% (i.e. ~8% if
cap was 18%) and your effective buffer is the original 15% buffer
*relative to the period start*, which means you are only protected
if the market drops more than 10% from where you bought. The
labelled "15% buffer" is no longer your buffer.

**Q5: How do I size the four DIY legs to match $50k of buffered
exposure?**
For SPX-anchored: $50k / SPX_level / multiplier = number of SPX
spreads. With SPX at 5000, that is $50k / 5000 / $100 = 0.10
contracts per share — so for cleanest sizing, use $100k notional =
2 contracts of each leg. For SPY: $50k / SPY_price / 100 = $50k /
$500 / 100 = 1 contract of each leg, which works at a single
1-contract scale.

**Q6: Why not just hold SPY plus a long put for the same
protection?**
A long put has *no* cap on the upside but costs 4–5% of notional
per year (for ATM 1y puts). The buffer structure trades the ~5%/yr
put cost for the cap — capping upside at 18% in exchange for not
paying that 5%/yr drag. It is a *different* tradeoff: barbell
(SPY + put) keeps the convex tails at the cost of carry; buffer
collapses the distribution at the cost of tails. If your portfolio
already has a convex sleeve (Week 47's tail hedge), you do not
need the buffer structure on top of it.

**Q7: What is the worst-case outcome on a buffer ETF?**
The market drops to zero. You get max(index_return + buffer, -100%).
On a 15% buffer, you lose 85% of capital. The buffer never
*guarantees* principal — it only absorbs the first 15% of loss.

**Q8: Do PPNs ever make sense?**
Niche cases: an investor with very specific tax circumstances
(e.g., trust structures where the deferral of CPDI matches a
planned liquidity event), or institutional accounts that need a
CUSIP-based debt-instrument wrapper for compliance reasons. For a
typical retail investor in a taxable account, the answer is
essentially never — ETFs and DIY beat them on every dimension that
matters.

**Q9: How do I evaluate a new structured product I have not seen
before?**
Decompose it into its option legs. Every structured product is a
linear combination of zero-coupon bonds plus options on the
underlying. Price the legs in a Black–Scholes calculator (or use
the Week 48 interactive). Compute the all-in cost as
(prospectus_value - sum_of_legs) / notional. If the answer is
greater than 50bps/yr, you are paying a fee high enough that DIY
is strictly better in any account that can trade options.

**Q10: What is the right portfolio role for a buffer ETF?**
For most investors: zero. The middle-of-distribution exposure is
already in the index portion of the portfolio at lower cost. If the
investor is constrained to a non-options account *and*
psychologically needs the floor to stay in the market through a
downturn, allocating 5–15% to a buffer ETF as a behavioural bridge
can be defensible. This is a behavioural product, not a return-
enhancement product.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Structured products decoded — buffer ETFs, principal-protected notes, and replicating them DIY at 1/10 the cost
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00 to 1:30]**

**Stella:** Welcome back. This week's lesson is the one I get the
most questions about from family members. "My advisor just put me
into a buffer ETF — it caps my upside at 18% but protects me from
the first 15% of a drawdown. Should I be excited?" Horace, what
is the right answer there?

**Horace:** The right answer is: that product is three options
and a Treasury bill, and you are paying the fund company 80 basis
points a year to wrap them for you. Before you decide whether
that fee is worth it, you should know what is inside the wrapper.

**Stella:** And you have an opinion about whether it is worth it.

**Horace:** I have an opinion. The opinion is that for anybody
who finished Weeks 25 through 30 of this course, the wrapper is
roughly ten times more expensive than the DIY version. Alpha is
rare, and an arithmetic identity priced at 80 basis
points a year is not alpha — it is a convenience tax on retail.

**Stella:** Let's tear it apart.

---

**[SECTION 1 — What is inside a buffer ETF — 1:30 to 4:30]**

**Stella:** Start with the structure. What does a buffer ETF
actually own on inception day?

**Horace:** Three positions on the index.

[VISUAL: image/week48_buffer_payoff.png]

**Horace:** First, a 1-year zero-coupon Treasury, which gives you
your principal back at maturity. Second, a 1-year bull-call-spread
on the index — long an at-the-money call, short an 18%-OTM call.
That is your participation: you get the index return one-for-one,
capped at 18%. Third, a short 1-year put 15% out of the money. The
premium you collect on that short put is what finances the call
spread.

**Stella:** So the buffer is created by the short put.

**Horace:** Exactly. If the index is down less than 15% at expiry,
the put expires worthless and you keep the premium — that is what
"buffers" the first 15% of loss. If the index is down more than
15%, the put is in-the-money and you take the loss past the
buffer, one-for-one. There is no magic. It is a four-leg option
position.

**Stella:** And the cap?

**Horace:** The cap exists because the short put premium is
finite. That premium pays for some of the call spread, but not all
of it. The upper strike of the spread sits where the math balances
— and that is the cap. Higher implied vol means a higher cap;
lower IV means a lower cap. The level it locks in at issuance is
what you own.

**Stella:** So the chart on screen — 15% buffer, 18% cap, on SPY
at $500 — that flat zone from -15% to 0% is the buffer, then the
diagonal upside to +18%, then the flat cap.

**Horace:** Right. And below -15% the line slopes back down at a
1-to-1 rate. There is no protection past the buffer. A 2008-style
-37% year on a 15-buffer product loses you 22%.

---

**[SECTION 2 — DIY replication on SPX options — 4:30 to 8:00]**

**Stella:** Now the DIY version. With SPY at $500, how do I
replicate the same structure?

**Horace:** Per $50,000 of notional, you trade four legs on
1-year SPX options. Long the at-the-money SPX call at 5000 —
costs about $310 per contract. Short the 5900 SPX call, the +18%
strike — you collect about $48. That is the bull call spread, net
debit $262. Then short a 4250 SPX put, the -15% strike — you
collect about $112.

**Stella:** Net cost?

**Horace:** $262 minus $112 = $150 per share-equivalent, plus the
T-bill leg. On $50k of notional that is roughly $2,255 of total
explicit cost, which is what makes the cap 18% rather than the
21–22% it would be at zero cost.

**Stella:** And the slippage on executing those four legs?

**Horace:** SPX options at 1-year tenor have tight markets. You
can expect about 5 basis points per leg at the mid-point, times 4
legs, so roughly 20 basis points of round-trip slippage, plus a
few dollars in commissions. Call it 25 basis points all-in.

**Stella:** Versus 80 basis points expense ratio plus 12 basis
points secondary-market spread on the ETF — call it 91 basis
points per year.

[VISUAL: image/week48_diy_vs_etf.png]

**Horace:** Over five years on $100k, that is about a $4,900
wealth gap. Scale to $500k and you are paying $24,500 in
convenience taxes for option trades you could place yourself once
a year on the anniversary.

**Stella:** What does the interactive let me play with?

**Horace:** [VISUAL: interactive/week48_buffer_builder.html]
Sliders for spot, buffer percentage, cap percentage, and DTE. The
output shows the net cost — that is the DIY pricing — plus max
profit, max loss, breakeven, and the four underlying option legs
with their individual payoffs charted. You can see immediately
how the cap shrinks if you ask for a deeper buffer.

---

**[SECTION 3 — Principal-protected notes and bank credit risk — 8:00 to 11:00]**

**Stella:** Different product: principal-protected notes from a
bank. How are they different?

**Horace:** Three things. First, they are debt of the issuing
bank, not a bankruptcy-remote ETF wrapper. When Lehman Brothers
went bankrupt in 2008, investors holding Lehman PPNs got about
nine cents on the dollar. The "protection" is unsecured senior
debt — it is only as good as the bank's ability to pay.

**Stella:** Own US-listed claims you can verify.

**Horace:** Right. ETFs are trust structures. Notes are bank debt.
Different beasts.

**Stella:** Second?

**Horace:** Embedded fees. A 5-year PPN typically prices in 200
to 400 basis points of profit for the issuing bank, amortised
over the life. You see this as a worse cap, a longer term, or a
wider participation discount. The fee is not in a prospectus line
item — it is in the structure itself.

**Stella:** Third?

**Horace:** Tax treatment. PPNs are typically taxed as contingent
payment debt instruments — CPDI rules — which means you accrue
phantom interest annually at ordinary income rates. At a 32%
federal plus 5% state bracket, this is 19 percentage points worse
than qualified LTCG. The DIY equivalent — a 5-year zero-coupon
Treasury plus 5-year SPX calls — gets you 1256 treatment on the
options and Treasury rules on the bond. Cleaner.

**Stella:** Liquidity?

**Horace:** Almost none in the secondary market. If you need cash
mid-life on a PPN, the dealer who issued it will quote you another
1–3% haircut.

**Stella:** So when do PPNs make sense?

**Horace:** Niche cases. Trust structures with specific deferral
needs. Institutional compliance requirements that need a
CUSIP-based debt wrapper. For a typical retail investor in a
taxable account, basically never.

---

**[SECTION 4 — When the wrapper does win — 11:00 to 13:00]**

**Stella:** Are there cases where buying the buffer ETF actually
makes sense?

**Horace:** Three. First, account constraints — many 401(k)s and
employer brokerages do not allow options trading at all. In a
non-options account, the buffer ETF is the only way to get that
exposure and the 80bps fee is unavoidable. Take it.

**Stella:** Second?

**Horace:** Discipline failure. If you know you are going to
flinch on the roll date, or close one leg early in a panic, the
fund company is selling you the *commitment* to the structure. A
buffer ETF cannot be broken into mid-period the way a self-managed
DIY structure can. For some investors that is genuinely worth
80bps.

**Stella:** Third?

**Horace:** Notional below ~$50k. SPX options have a $100
multiplier — below $50k of notional you get pushed into SPY
options which lose the 1256 treatment and have wider spreads. The
fund company's pooling lets sub-$50k accounts access the
SPX-priced structure indirectly.

**Stella:** And outside those three?

**Horace:** Outside those three, the DIY version is strictly
better on cost and tax. 25bps DIY versus 91bps ETF, with 1256
60/40 tax versus mixed CG. Run the spreadsheet.

---

**[SECTION 5 — The barbell read — 13:00 to 15:30]**

**Stella:** A barbell sits on a boring base plus
a small convex sleeve. Where does the buffer ETF fit?

**Horace:** It does not fit. It is anti-barbell. The buffer cuts
off the left tail at -15% and slopes down again past it; the cap
cuts off the right tail at +18%. What remains is the *middle* of
the distribution.

**Stella:** And the middle of the distribution is...

**Horace:** What you already get from a plain index fund at 3
basis points. Paying 80bps to delete both tails is not insurance
— it is a tactical bet that the index will spend the year between
-15% and +18%. The base rate for that range over 1928 to 2024 is
about 55%. You are paying a fee to be right 55% of the time on a
binary question.

**Stella:** And the volatility tail wagging the dog.

**Horace:** That is the deeper objection. If a small handful of
extreme moves dominate the long-run return distribution, then
deleting both tails systematically caps your geometric compounding
*below* what the index produces over a long horizon. The buffer
ETF's after-fee long-horizon return is mathematically below the
index's by roughly the cap-truncation-loss minus the
buffer-absorption-gain, which empirically is negative for any
horizon longer than five years.

**Stella:** So the products do best when you do not need them.

**Horace:** Correct. They cap the kind of years where you would
have made money anyway, and they buffer years where you can
already afford to lose 15%. The structure is *psychologically*
useful, but that is a behavioural finance question — Week 11 —
not a structural one.

---

**[SECTION 6 — Practical decision tree — 15:30 to 17:00]**

**Stella:** Wrap it up with the decision tree.

**Horace:** Three questions, in order.

**One**: do you have an options-enabled brokerage account with at
least $50,000 of investable capital you want to expose to the
index? If no, the buffer ETF may be your only path — pay the
80bps. If yes, continue.

**Two**: are you willing to execute four SPX option legs once a
year on the anniversary date, and roll on schedule? If no, the
buffer ETF buys you the commitment — pay the 80bps. If yes,
continue.

**Three**: do you actually want to delete both tails of the
distribution from your portfolio? If yes, build the DIY structure
at 25bps. If no — and for most long-horizon investors the answer
is no — skip the structure entirely. Hold the index, allocate a
small sleeve to convex tail hedges (Week 47), and let the dog
wag.

**Stella:** And principal-protected notes?

**Horace:** Skip them. Always. The combination of bank credit
risk, embedded fees, illiquidity, and ordinary-income tax
treatment makes them strictly dominated by a Treasury-plus-SPX-
calls DIY construction in any account that can hold both. Not a
close call.

---

**[OUTRO — 17:00 to 18:00]**

**Stella:** Bottom line?

**Horace:** Most retail "structured products" are DIY-replicable
with options at one-tenth the cost. The fee on the wrapper is a
convenience tax — sometimes worth paying, usually not. The
deeper issue is that the *shape* of the buffered payoff is the
wrong shape for long-horizon compounders. The barbell wants tails;
buffered products delete tails.

**Stella:** So when your advisor pitches you a buffer ETF...

**Horace:** Decompose it. Four legs. Price each leg. Sum the
costs. If the wrapper is more than 50 basis points more
expensive than the DIY version per year and you have an options
account, pass. If the wrapper saves you from yourself, take it.
There is no third answer.

**Stella:** And if the pitch is a structured note?

**Horace:** Pass. Always.

**Stella:** Run the buffer builder, decompose your advisor's
pitch, and see you next week.

[VISUAL: interactive/week48_buffer_builder.html]
