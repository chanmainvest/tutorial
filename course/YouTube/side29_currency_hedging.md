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
