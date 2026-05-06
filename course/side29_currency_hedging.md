# Side Lesson 29: Currency Hedging — When to Hedge, How to Hedge, and the Cost of Insurance

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Side lesson 18 told you the punchline first: this course's recommended
portfolio is U.S.-listed equities only. So why is there a whole side
lesson on currency hedging? Because **the U.S.-only rule is about
equities, not bonds, and it has exceptions.** The moment you reach
outside the United States for *anything* — an EAFE sleeve, an
international bond fund, a foreign-currency cash deposit, a Swiss
holding company that owns a U.S. ADR — currency arithmetic is back in
your portfolio whether you wanted it or not.

There are four reasons this is worth a full side lesson rather than a
footnote:

1. **The "leave international unhedged" reflex is the wrong default
   for international bonds.** For stocks the conventional wisdom is
   roughly defensible (currency vol ~7-9%/yr is small relative to
   equity vol ~16%/yr, and over 10+ years the FX leg has roughly
   zero expected return). For investment-grade ex-U.S. bonds the
   currency vol *exceeds the asset vol* — a 4% yielding German bund
   with 8% currency volatility is a worse Sharpe ratio than a U.S.
   T-note. If you own non-U.S. bonds and you don't hedge, you have
   accidentally turned a fixed-income sleeve into an FX trade.
2. **Hedging cost is not trivia, it is a measurable price.**
   Covered-interest-parity makes the cost of a one-year currency
   hedge approximately equal to the *interest rate differential*.
   When U.S. T-bills yield 4.3% and Japanese T-bills yield 0.3%, the
   one-year USD/JPY hedge *earns* you about 4 percentage points; when
   euro rates briefly exceeded U.S. rates in 2008-2009, the hedge
   *cost* you ~50bp. Knowing this number turns "should I hedge"
   into a calculation, not a vibe.
3. **Hedged ETFs exist and are cheap.** HEFA (iShares EAFE hedged)
   charges 35bp; HEDJ (Europe hedged) and HEWJ (Japan hedged) are in
   the same range. The hedge mechanic — rolling one-month forwards
   — is not exotic, it is a baked-in feature you can buy or skip
   with one ticker change. The retail toolkit is fully built out.
4. **The dollar regime moves in long swings, not noise.** The DXY
   spent 2002-2008 falling, 2008-2014 ranging, 2014-2022 rising
   sharply, and 2024-2026 retracing. These are *six- to ten-year*
   regimes — long enough that being wrong-footed once costs you a
   chunk of an investing lifetime. You do not have to predict the
   next regime to size around the last three.

This lesson is not telling you to hedge. It is telling you what the
trade-off looks like, where the corner cases are, and which ETFs to
use when you decide it is worth doing.

---

### 2. What You Need to Know

#### 2.1 The Two-Bet Decomposition

Every dollar you put into a foreign asset is two bets:

1. **The local-currency return on the asset** — the stock or bond
   priced in its home currency.
2. **The currency return** — the change in exchange rate between
   that home currency and the U.S. dollar over the holding period.

The exact dollar-denominated return is the product:

$$
1 + R_{\text{USD}} \;=\; (1 + R_{\text{local}}) \times (1 + R_{\text{FX}})
$$

For small returns the cross-product is negligible and the decomposition
is approximately additive: $R_{\text{USD}} \approx R_{\text{local}} +
R_{\text{FX}}$. A worked example: in 2024 the Nikkei 225 returned about
+19.2% in yen terms; the yen depreciated about 11% against the dollar;
the unhedged USD return was therefore $(1.192)(0.89) - 1 \approx +6.1\%$.
A Japanese investor saw +19%, an American who held the same stock
unhedged saw +6%, and an American who held it hedged saw approximately
+19% minus the hedge cost.

The volatility decomposition under the assumption of independent FX
and local returns is:

$$
\sigma^2_{\text{USD}} \;=\; \sigma^2_{\text{local}} + \sigma^2_{\text{FX}}
$$

For an unhedged developed-market equity, this is roughly $16^2 + 8^2 =
17.9\%$ — about 12% higher portfolio vol than the local. For an
unhedged developed-market 7-year bond it is $5^2 + 8^2 = 9.4\%$ — vol
is **double** the underlying. The FX leg matters categorically more for
bonds than for stocks.

#### 2.2 What a Hedged ETF Actually Does

A "currency-hedged" ETF holds the foreign basket *and* sells a series
of one-month foreign-currency forwards equal in notional to the basket.
At each month-end the forward expires, the realised FX P&L is settled
in dollars, and a new forward is opened. The mechanical effect: for the
one month between rolls, the dollar return tracks the local-currency
return almost exactly, less a small drag from forward pricing.

The drag is the **interest-rate differential**, which by
covered-interest-parity equals the percentage difference between the
spot rate and the forward rate:

$$
\text{Forward}/\text{Spot} \;\approx\; \frac{1 + r_{\text{foreign}}}
{1 + r_{\text{US}}}
$$

Re-arranged for an annualised hedge cost:

$$
\text{Hedge cost (per year)} \;\approx\; r_{\text{US}} - r_{\text{foreign}}
$$

This is a sign-honest number. If U.S. short-term rates exceed foreign
rates (the situation in April 2026: U.S. 4.3%, EUR 2.0%, JPY 0.5%, GBP
4.0%), the hedge **earns positive carry** of ~2.3% against the euro and
~3.8% against the yen *before* the ETF's expense ratio. If the spread
inverts (the U.S. ZIRP era 2009-2015 against most of the world), the
hedge bleeds carry — but this is rare and shallow, typically 0-50bp
against major currencies.

Three vehicles to know:

- **HEFA** — iShares Currency Hedged MSCI EAFE. 35bp ER. AUM ~$8B.
  The hedged twin of EFA. Pairs cleanly with the unhedged sibling for
  comparison.
- **HEDJ** — WisdomTree Europe Hedged Equity. 58bp ER. AUM ~$2B.
  Tilts toward export-heavy Europe (Siemens, ASML, LVMH, Sanofi).
- **HEWJ** — iShares Currency Hedged MSCI Japan. 35bp ER. AUM ~$0.4B.
  The hedged twin of EWJ.

The 35bp ER is on top of the underlying basket's natural cost. The
hedge mechanic itself adds approximately 5-10bp of frictional cost
(monthly roll, bid-ask on forwards) on top of any carry signal.

![Wealth path of $1 invested 2010 through April 2026 in EFA (unhedged EAFE) versus HEFA (hedged EAFE). HEFA backfilled with EAFE-local returns pre-inception (2014). The two paths diverge in 2014-2015 (hedged wins as USD rallies), reconverge 2017 (unhedged wins as EUR strengthens), separate again 2022 (hedged wins as USD spikes), and finish near each other.](image/side29_hedged_vs_unhedged.png)

#### 2.3 The Long-Run Equivalence Theorem

A robust empirical regularity: over rolling 10- to 20-year windows,
**hedged and unhedged international equity returns are within roughly
10-30bp/yr of each other.** The mechanism is straightforward — over
long enough horizons real exchange rates revert to purchasing power
parity, so the cumulative FX contribution to the unhedged return
averages roughly zero, leaving you with just the asset return either
way.

What does *not* equalise: **volatility and drawdowns.** The hedged
sleeve has consistently lower realised vol (about 16% vs 18% on EAFE
since 2002) and shallower max drawdowns. So the long-run trade-off
collapses to: same expected return, lower vol — i.e., a higher Sharpe
ratio for the hedged sleeve. This is the rare case where there is a
free lunch in the data, and the cost of getting it is just the 35bp ER.

The reason most retail advisors still recommend "leave international
unhedged" is behavioural rather than mathematical. Holding HEFA against
a falling dollar means *underperforming* the headline EFA in a
dollar-bear regime, and clients fire advisors who underperform the
benchmark even when total-return Sharpe is better. Institutional money
that does not have that constraint hedges roughly 50-75% of its
ex-U.S. equity exposure.

#### 2.4 Short-Run: Five Regimes That Mattered

Sub-decade windows are where the hedge/unhedge decision actually shows
up in your statement. The post-1990 record:

- **1995-2002 — strong dollar.** DXY ran from 80 to 120. Unhedged
  ex-U.S. bled relative to hedged. Net cost of being unhedged: ~3-4%
  per year for seven years.
- **2002-2008 — weak dollar.** DXY dropped from 120 to 71. Unhedged
  *won* by ~3-4% per year. This is the regime that locked in the
  textbook recommendation to leave international unhedged.
- **2014-2016 — strong dollar 2.0.** DXY surged from 80 to 100 over
  18 months as the Fed taper diverged from ECB QE. HEFA outperformed
  EFA by about 9 percentage points cumulative.
- **2017 — weak dollar.** DXY fell 10% as Trump-tax-cut optimism
  faded. Unhedged EFA returned 25%; HEFA returned 17%. The unhedged
  sleeve won by 8 percentage points in a single year.
- **2022 — strong dollar 3.0.** DXY hit 114, the highest since 2002,
  as the Fed hiked 525bp into a global recession. HEFA -7.8%; EFA
  -16.8%. The hedge saved 9 points of drawdown.
- **2024-2026 — dollar retracement.** DXY drifted from 107 to 99.
  Unhedged EFA modestly outperformed. The current April-2026 setup
  is the kind of regime where *neither* side has a clear edge.

The pattern: regimes are long (5-10 years), the magnitudes within them
are large (3-4%/yr cumulative), and they do not telegraph in advance.
That is what makes hedging a real allocation question rather than a
pure "always" or "never."

![Trade-Weighted U.S. Dollar Index (FRED DTWEXBGS, broad goods+services, monthly average) from 1990 through April 2026 with shaded regimes. Five labelled episodes: 1995-2002 strong-dollar, 2002-2008 weak-dollar, 2014-2016 strong-dollar 2.0, 2022 strong-dollar 3.0, 2024-2026 retracement.](image/side29_dxy_history.png)

#### 2.5 The U.S.-Only Carve-Out: International Bonds

The U.S.-only equity rule from side lesson 18 has one quietly important
exception: **if you hold non-U.S. fixed income at all, you should
hedge it.**

The math from §2.1: a 4-5% yielding ex-U.S. investment-grade bond
sleeve has roughly 5% local-price volatility and 8% currency
volatility. Combined, the unhedged sleeve has *more* volatility than
the bond's running yield — meaning the FX leg dominates. You are
holding a vehicle that the marketing material calls "fixed income" but
that behaves like an FX trade with a coupon strapped to it.

Hedged international bond ETFs:

- **BNDX** — Vanguard Total International Bond. 7bp ER. ~$50B AUM.
  Hedged USD. The default if you want any non-U.S. fixed income at
  all.
- **IAGG** — iShares Core International Aggregate Bond. 7bp ER.
  Hedged USD. BNDX's main competitor.

Note both are *hedged by default* at the product level — there are no
significant unhedged international IG bond ETFs trading at meaningful
AUM, because the buyers of these products are the institutions that
already did the math in this section.

The course's actual position: own VGIT / IEF / TLT for duration, and
own BNDX only if you want explicit non-U.S. credit/duration
diversification. For most retail portfolios, the answer is "skip BNDX
entirely; the diversification benefit is small once both vehicles are
USD-hedged duration." But if you do reach for it, do not hold the
unhedged version. There is no scenario in which an unhedged ex-U.S. IG
bond sleeve is the optimal choice for a USD-spending investor.

#### 2.6 Optimal Hedge Ratio: The Decision Tree

You do not have to choose 0% hedged or 100% hedged. The hedge ratio
$h$ that minimises portfolio volatility is given by the regression
coefficient of unhedged return on FX return — which has a closed form:

$$
h^* \;=\; 1 + \rho \cdot \frac{\sigma_{\text{local}}}{\sigma_{\text{FX}}}
$$

where $\rho$ is the correlation between the local-currency asset return
and the FX return. For developed-market equities $\rho$ is typically
slightly positive (about +0.1 to +0.2), so $h^*$ comes out a little
above 1.0 — fully hedge. For commodities and EM equities $\rho$ is
typically negative (the local market sells off when its currency
weakens), so $h^*$ is well below 1.0 — partial hedge or skip.

The pragmatic decision rule the course uses:

| Sleeve | Recommended hedge ratio | Vehicle |
| --- | --- | --- |
| U.S.-listed equity | n/a | VTI/SPY |
| U.S.-listed ADRs | 0% | TSM, ASML, etc. |
| Ex-U.S. IG bonds | **100%** | BNDX, IAGG |
| Ex-U.S. developed-market equity | 50-100% | HEFA + EFA mix |
| Emerging-market equity | 0-50% | EEM unhedged or HDEM partial |
| Commodities (priced in USD) | 0% | DBC, PDBC |
| Gold (USD price) | 0% | GLD, IAU |

The 50-100% ex-U.S. equity range is wide on purpose. It reflects that
inside this course's framework you should not have a large ex-U.S.
sleeve at all — and if you do, the choice between 50/50 and 100/0 is
mostly about behavioural tracking-error tolerance, not about
expected returns.

---

### 3. Common Misconceptions

1. **"Hedging is expensive."** When U.S. rates exceed foreign rates
   (the modal regime since 2008), hedging *earns* positive carry.
   The "expense" is just the ETF's own ~35bp expense ratio.
2. **"Hedging is gambling on the dollar."** It is the opposite.
   *Not* hedging is taking a position on the dollar. Hedging removes
   the FX bet so you only own the underlying asset.
3. **"Forward rates predict future spot rates."** They do not. The
   forward rate equals the interest-rate differential by
   covered-interest-parity. Empirically, the spot rate at expiration
   has zero correlation to the forward — the "forward premium puzzle."
4. **"Currency volatility averages out over 10 years."** The
   *cumulative* return contribution averages to roughly zero over 10+
   years. The *volatility contribution* does not — it adds to your
   monthly drawdowns the entire time.
5. **"International bonds give you currency diversification."** They
   give you currency *risk*. If you wanted currency diversification
   you would buy an FX product directly, not bond-FX combo.
6. **"Hedged ETFs are leveraged."** They are not. The forward leg is
   fully collateralised by the underlying basket. Counterparty risk
   exists but is a fraction of a percent of NAV.
7. **"DXY measures the dollar against everything."** It is a
   trade-weighted index of six currencies (EUR 57.6%, JPY 13.6%,
   GBP 11.9%, CAD 9.1%, SEK 4.2%, CHF 3.6%). The Fed's broader
   DTWEXBGS includes 26 trading partners and is what hedging cost
   actually tracks.
8. **"If I'm a long-term investor I don't need to hedge."** Only true
   for ex-U.S. equities, and only because the asset vol dominates the
   FX vol on long horizons. False for ex-U.S. bonds, where FX vol is
   the *larger* component at every horizon.
9. **"Hedging removes the interest-rate-differential pickup."** It
   does the opposite. The differential becomes the hedge carry. You
   cannot collect a higher foreign yield without taking the FX
   exposure that on average kills it.
10. **"Just buy a few foreign stocks directly to keep it simple."**
    You will under-diversify, pay foreign withholding tax, and have
    no easy way to layer a hedge. Use a U.S.-listed ETF (hedged or
    unhedged) for any non-U.S. exposure.

---

### 4. Q&A Section

**Q1: I own VXUS in my 401(k). Should I switch to a hedged
alternative?**
For an equity sleeve held 10+ years the long-run expected returns of
hedged vs unhedged are nearly identical. If your 401(k) offers a
hedged developed-market option at <50bp ER, the Sharpe ratio is
modestly better hedged. If it does not, leaving VXUS alone is fine —
the inferior option is "sell to chase the recent winner." The course
position remains: minimise the ex-U.S. equity sleeve in the first
place.

**Q2: U.S. rates are 4.3% and Japanese rates are 0.5%. Is now a great
time to hedge yen exposure?**
Yes, in a narrow sense — the carry is roughly +3.8%/yr in your favour.
But the carry is *already priced into the forward rate*, which is what
the hedged ETF buys. The carry shows up as the hedge ratio
mechanically working in your favour each month, and is the reason
HEWJ has tracked EWJ-in-yen so closely since the BOJ kept rates near
zero.

**Q3: What is the difference between DTWEXBGS and DXY?**
DXY is the ICE Dollar Index, six currencies, ~58% euro by weight,
launched 1973. DTWEXBGS is the Fed's Trade-Weighted Broad Goods +
Services index, 26 currencies including CNY and MXN, recalibrated
annually. DTWEXBGS is the better measure of the dollar's economic
strength; DXY is the better measure of what financial markets watch
(and what hedged-EAFE ETF managers actually trade).

**Q4: Can I hedge currency exposure myself with futures?**
You can, but it is not worth it. /6E (euro futures) is $125k notional
per contract; rolling quarterly produces tracking error and has tax
treatment under §1256 (60/40 LTCG/STCG, see week 39). For sleeves
under $5-10M, the 35bp HEFA expense ratio is cheaper than the
operational drag of doing it yourself.

**Q5: Why do hedged ETFs sometimes underperform their unhedged twin
even when the dollar is rising?**
Three reasons: (1) the hedge resets monthly, so intra-month FX moves
inside the dollar's overall trend can show up wrong-footed; (2) the
ETF's expense ratio is 30-40bp higher than the unhedged version; (3)
the forward roll incurs small bid-ask costs.

**Q6: The course says U.S.-only. Why are you teaching me how to hedge?**
The U.S.-only rule is about equity recommendations. The carve-outs are (a)
U.S.-listed ADRs (already in U.S. dollars, no FX exposure to hedge);
(b) international IG bonds *if you choose to own them*, where you
should always hedge; (c) the rare investor who insists on a 10-20%
ex-U.S. equity sleeve, where the hedge decision matters. The lesson
exists for completeness, not as a recommendation to add ex-U.S.
exposure.

**Q7: What about emerging-market currencies — INR, BRL, ZAR?**
Most major EM currencies do not have liquid forward markets at retail
sizes. EM-equity ETFs like EEM are unhedged by structural necessity.
The few hedged EM products (HEEM was de-listed in 2018) failed
because EM currency carry against USD is *positive* — i.e., hedging
costs you 3-5%/yr of yield, and the EM equity correlation with EM FX
is strongly negative, meaning the unhedged position partly diversifies
itself.

**Q8: Does Berkshire Hathaway hedge its foreign-currency exposure?**
Famously almost never. Buffett's view is that PPP (purchasing power
parity) reverts on long horizons and the hedge cost over BRK's
multi-decade holding period is therefore a deadweight loss. This is
defensible at BRK's scale and time horizon. It is not defensible for
a retail investor with a 10-year horizon and a finite tolerance for
intra-decade drawdowns.

**Q9: What happens to my hedge when there is a currency crisis?**
The forward leg pays out in dollars at maturity even if the foreign
currency has depreciated 50%. Counterparty risk is small (forwards
are collateralised at major dealers). The bigger risk is that during
the crisis the underlying foreign asset also crashes — the 1998 Asia
crisis hit EM bonds (-30%) regardless of hedge status, because the
local-currency leg was the disaster.

**Q10: Why doesn't covered-interest-parity break in extreme stress?**
It does. In late 2008 USD funding stress widened the deviation from
CIP to several hundred basis points (the "USD basis"). It does not
matter for retail because the hedged ETF's market price reflects the
strain in real-time and you can sell out at NAV without rolling
forwards yourself. It matters for prime brokers running cross-currency
repo books, which is not your problem.

**Q11: How does §1256 tax treatment apply to currency hedges?**
For the *futures* used by some hedged ETFs internally, yes — but the
ETF wrapper handles all of it. Your 1099 from a hedged ETF reports
ordinary distributions and capital gains the same as any other ETF.
You do not see the §1256 mechanics directly. (See week 39 for the
direct-futures version of the same trade.)

**Q12: Is there a "hedged S&P 500" for non-USD investors that I
should know about?**
Yes — IWDA-hedged variants exist on European exchanges, and similar
USD-hedged S&P products exist for Asian investors who want U.S.
equities translated back to home currency. Mirror image of HEFA. Not
relevant if you are a U.S.-domiciled investor (your spending is in
USD), but useful to know if you are advising a non-U.S. friend who
holds U.S. stocks.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Currency Hedging — When the FX Tail Wags the Bond Dog

**RUNTIME TARGET:** ~14 minutes

**HOSTS:** Horace, Stella

---

**[INTRO]**

Stella: Welcome back. Today's side lesson is currency hedging — when
to hedge, how to hedge, and what it actually costs. Horace, you've
been telling us for 28 weeks that this course is U.S.-listed only.
So why are we doing a whole lesson on hedging foreign exposure?

Horace: Two reasons. First, the U.S.-only rule is
about *equities*. The carve-out is bonds — if anyone watching has
international fixed income in their portfolio, they need to hear the
math we're about to walk through. Second, even within the U.S.-only
universe, you'll occasionally end up with non-USD exposure: a Swiss
holding company, a Japanese ADR with a yen revenue base, a foreign
property. The mental model from this lesson lets you size that risk
honestly.

Stella: So this is the "rare cases" lesson, not the "build a global
portfolio" lesson.

Horace: Exactly. We're not contradicting side 18. We're giving you
the toolkit for the corner cases.

---

**[SECTION 1: THE TWO-BET DECOMPOSITION]**

Stella: Walk me through the math first. I buy a Japanese stock.

Horace: You're making two bets. One on the stock, one on the yen.
The dollar return decomposes as one plus local return, times one
plus FX return, minus one. For 2024: Nikkei was up 19% in yen. Yen
fell 11% against the dollar. So unhedged USD return was 1.19 times
0.89 minus 1, which is +6.1%. The Japanese investor saw 19, the
American saw 6, the gap was the FX leg.

Stella: That's a thirteen-point swing from currency alone.

Horace: In one year, on a developed-market stock. And the
volatilities decompose the same way. Add the variances if the two
legs are roughly independent. For developed-market equity, local vol
is 16, FX vol is 8, total vol is square root of 16 squared plus 8
squared, about 17.9. About 12% higher than the local vol. For an
investment-grade foreign bond, it's 5 squared plus 8 squared, which
is 9.4. The FX leg *doubles* the bond's volatility.

Stella: So for stocks, currency is a side dish. For bonds, it's the
main course.

Horace: That's the punchline. Anyone holding ex-U.S. bonds unhedged
has accidentally turned a fixed-income sleeve into an FX trade. The
ratio of FX vol to asset vol is the only thing that matters here.

---

**[SECTION 2: WHAT A HEDGED ETF DOES]**

Stella: How does a hedged ETF actually work? Like, plumbing-wise.

Horace: It holds the foreign basket — same stocks as EFA — and at
month-end it sells one-month forwards on each foreign currency
weighted to the basket. Forward expires, FX P&L settled in dollars,
new forward opened. Mechanically the dollar return tracks the
local-currency return for that month, give or take a few basis
points.

Stella: And the cost?

Horace: That's the elegant part. Covered-interest-parity says the
forward price equals the spot price times the ratio of one-plus-foreign-rate
over one-plus-U.S.-rate. Re-arranged, the annualised hedge cost is
just U.S. rate minus foreign rate. April 2026 numbers: U.S. T-bill at
4.3%, EUR rate 2.0%, JPY rate 0.5%. Hedging EUR earns +2.3% carry.
Hedging JPY earns +3.8% carry. Plus the ETF's expense ratio of 35bp.
Net positive carry is the modal regime since 2008.

Stella: Wait — the hedge *earns* money?

Horace: When U.S. rates exceed foreign rates, yes. The misconception
"hedging is expensive" assumes a regime where U.S. rates are below
foreign rates. That regime existed briefly — 2008-2009 against the
euro, when EUR rates were 50bp above U.S. rates. Costs were maybe
50bp/yr. Trivial.

Stella: And the products?

Horace: HEFA for EAFE, HEDJ for Europe, HEWJ for Japan. All in the
35-58bp range. BNDX and IAGG for international IG bonds — both
hedged by default at 7bp.

[VISUAL: image/side29_hedged_vs_unhedged.png]

Stella: This chart compares EFA and HEFA from 2010 forward. What do
I see?

Horace: Two divergence-convergence cycles. 2014-2015, USD rallies
from 80 to 100 on the DXY. HEFA outperforms by about 9 percentage
points cumulative. Then 2017, EUR rallies, HEFA underperforms by 8
points in a single year. Then 2022, USD crisis spike to 114, HEFA
saves you about 9 points of drawdown. By April 2026 the two paths
end roughly within a couple percent of each other. Lower vol the
whole way, but the path matters.

---

**[SECTION 3: THE DXY HISTORY LESSON]**

[VISUAL: image/side29_dxy_history.png]

Stella: This is the long view of the dollar. 1990 through April 2026.

Horace: Five regimes. Strong-dollar 1995 to 2002, peak around 120 on
the broad index. Weak-dollar 2002 to 2008, all the way down to 71 —
this is the textbook's case for unhedged. Range-bound 2008 to 2014.
Strong-dollar 2.0 from 2014 through 2016 — the Fed taper / ECB QE
divergence. Then the 2022 spike to 114 on the rate-hike cycle. Now
2024-2026 retracement. The point: regimes are *long*. Five to ten
years. Magnitudes are big — three to four percent per year. And
they don't telegraph in advance.

Stella: So the strategic question is "which regime are we entering
now."

Horace: That's the bet you're making whether or not you realise it.
The hedge ratio decision is the only way to size that bet
deliberately.

---

**[SECTION 4: THE BOND CARVE-OUT]**

Stella: Section 2.5 of the reading is the operational punchline.
What's the rule?

Horace: If you hold any non-U.S. investment-grade bond, hedge it.
100% hedged. BNDX or IAGG, both 7bp. There is no scenario where
unhedged ex-U.S. IG bonds are the right answer for a USD-spending
investor.

Stella: And the rest of the matrix?

Horace: U.S. equity — not relevant, you're already in dollars. ADRs
— already in dollars, nothing to hedge. EM equity — the correlation
between the local market and the local currency is so negative that
the unhedged position partly diversifies itself; 0 to 50% hedge is
defensible. Commodities priced in USD, gold priced in USD — already
in dollars. Developed-market ex-U.S. equity if you insist on owning
it — 50 to 100% hedge, and within this course's framework you
shouldn't have a large sleeve of it anyway.

Stella: Let me push back. The textbook says "leave international
unhedged for the equity sleeve." Is the textbook wrong?

Horace: The textbook is right on long-run expected returns and wrong
on Sharpe. Hedged and unhedged converge on total return over 10-20
years. Hedged has *lower vol* the entire time. Higher Sharpe. The
reason advisors recommend unhedged is behavioural — clients fire you
for tracking error, not for low Sharpe. Institutional money that
doesn't have that constraint hedges 50-75%. Follow the institutions,
not the retail brochure.

---

**[SECTION 5: THE INTERACTIVE]**

Stella: Walk through the interactive lab.

Horace: Four sliders: foreign-asset weight in your portfolio,
expected USD trend, foreign rate, U.S. rate. The lab gives you four
outputs: hedged return, unhedged return, hedge cost or carry, and
the volatility-minimising hedge ratio. Drag the foreign rate below
the U.S. rate and you'll see the carry flip positive — that's the
modal 2026 regime. Drag the USD trend strong-positive and the
unhedged path collapses; drag it negative and unhedged wins. Drag
the foreign-asset weight to zero and the whole calculation goes to
zero because there's nothing to hedge.

Stella: What's the takeaway from playing with it?

Horace: Two things. First, the hedge-cost line is approximately
linear in the rate differential — that's covered-interest-parity
made visible. Second, the optimal hedge ratio is mostly insensitive
to your *expectation* of the dollar — it's driven by *volatility*,
not by directional view. People think hedging is a bet on the
dollar. The math says hedging is a bet on *less variance*.

---

**[OUTRO]**

Stella: Synthesise it for me. Three rules.

Horace: One — for U.S. equity and U.S.-listed ADRs, hedge ratio is
zero because there is nothing to hedge. Two — for ex-U.S.
investment-grade bonds, hedge ratio is 100% always; the FX leg is
bigger than the asset leg. Three — for ex-U.S. developed-market
equity, the answer is 50 to 100% if you have to own it, but per the U.S.-only
rule you mostly shouldn't.

Stella: And the cost.

Horace: Approximately the interest-rate differential. April 2026,
that's positive carry of 2-4% per year against the major foreign
currencies. Hedging is not just free — for the modal regime since
2008 it has been a small positive carry. The 35bp ETF expense ratio
is a rounding error against that.

Stella: Side lesson 30 next.

Horace: That's the capstone — survivorship bias and the things that
have *not* been said in this course. See you there.

[END]
