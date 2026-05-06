# Review: course/week05_bonds.md

## Overall Assessment

Week 5 is a strong technical lesson. It opens the 60/40 bond sleeve and makes the mechanics visible: cash flows, price, yield, duration, convexity, credit risk, and the 40-year yield regime. The lesson is not boring; it gives bonds narrative stakes by tying four-number contracts to the largest multi-decade trend in modern markets and the 2022 break.

The biggest issue is terminology precision around credit spreads. The lesson calls the chart a credit-spread chart, but the chart description says it plots BAA corporate bond total return minus 10-year Treasury total return. A return differential is not a yield credit spread. Since the lesson is teaching fixed income basics, that distinction matters. The second issue is cross-reference drift: the outro and Q&A point to a Week 6 diversification lesson that does not match the course map, and again refer to Week 13-14 as the barbell.

## Content Critique

- The opening is excellent: "four numbers and a calendar" is memorable and demystifies bonds.
- Add a caveat that the lesson is about plain-vanilla fixed-rate bonds. Callable bonds, floating-rate notes, TIPS, mortgage-backed securities, converts, and structured credit add extra moving parts.
- The price/yield explanation is clear and should work for beginners. The at-par / discount / premium consequences are especially useful.
- The duration section is one of the strongest parts. Connecting 2022's bond loss to duration times yield change is exactly the kind of arithmetic that changes investor intuition.
- The convexity explanation is directionally right, but "a 1% drop in yield raises price by more than a 1% rise lowers it" should specify same starting yield and same absolute yield move. Beginners can otherwise overgeneralize.
- The YTM section should emphasize reinvestment assumption and holding-period mismatch. YTM is the internal rate if held to maturity and coupons are reinvested at the yield; it is not guaranteed realized return if sold early.
- The "credit spreads" section needs correction. A BAA corporate total-return-minus-Treasury total-return series shows realized excess return and crisis underperformance, not the credit spread itself. A true credit spread is a yield difference, such as Moody's BAA yield minus 10-year Treasury yield or option-adjusted spread.
- Saying "spread spikes downward" is also conceptually confusing because yield credit spreads widen upward. If the chart remains a return differential, rename it "Corporate Bond Excess Return vs Treasuries."
- The statement that credit spreads are leading indicators needs support and nuance. Yield spreads can widen before equity bottoms, but the chart described is annual total-return spread, not a daily leading indicator.
- "Bonds are the discount rate of everything" is a strong framing, but technically asset valuation uses risk-free curve plus asset-specific risk premium. Add that small precision.
- Q1 says bond ladders can be built in 15 minutes. That may be true mechanically, but beginners also need to check bid/ask spread, callable status, maturity date, tax treatment, and minimum lot.
- Q2 says ETFs are cheaper and more liquid under ~$100k. For US Treasuries specifically, individual T-bills/Treasuries can be cheap even for smaller accounts at modern brokers. The statement is more true for corporates than Treasuries.
- Q6 includes a time-sensitive April 2026 yield-curve comment. Good for current relevance, but mark it as "as of" and expect it to age.

## Cross-Reference And Consistency Issues

- Q11 again says Week 13-14 is where the barbell chooses short Treasuries, but the course map has Week 13 as long/short and Week 14 as pair trading.
- The YouTube outro says next week is "Diversification done right," and the end screen says "Week 6 — Diversification Beyond 60/40," but the course map has Week 6 as Gold and Commodities as Diversifiers.
- Week 4 already had similar Week 5/Week 14 drift, so this appears to be a recurring outline-update issue.

## Presentation Improvements

- Add a "Plain Bond Contract" diagram: coupon stream plus principal balloon.
- Add a "what changes / what does not change" box: coupon and face stay fixed; market yield and price move.
- Add a worked pricing example with numbers before the formula, then show the formula after the intuition.
- Add a duration cheat sheet by ETF: SHY, IEF, TLT, BND, AGG. This would make the lesson immediately actionable.
- Add a bond-role table: cash parking, recession hedge, liability matching, income, duration bet, credit risk premium.
- Add a "Do not confuse" box: coupon, current yield, YTM, SEC yield, distribution yield.

## YouTube Script Critique

The script is concise and teachable. The opening question, "why did the simplest instrument blow up the worst in 2022?" is strong. The duration segment is likely the retention centerpiece because it turns 2022 into one multiplication.

Specific improvements:

- Cold open with a long-bond investor: "I bought safety and lost 30%." Then reveal duration.
- Use an on-screen cash-flow timeline before showing formulas. Beginner viewers will tolerate the formula better after seeing the payments.
- In the credit segment, avoid calling total-return differential a credit spread. Use a real spread chart or rename the visual.
- Let Stella ask: "If I hold to maturity, does the 2022 loss matter?" That would clarify individual bonds versus bond funds.
- Add a cross-border note if mentioning broker tools; non-US investors may face different bond access, minimums, withholding, and currency risks.
- Fix the next-week title in the outro/end screen.

## Chart And Visual Feedback

Existing charts are useful:

- Yield history chart is essential and should be one of the course's anchor visuals.
- Credit/corporate return chart is valuable but mislabeled conceptually.
- A bond price-yield curve is the right visual for the lesson.

Recommended upgrades:

- True credit spread chart: Moody's BAA yield minus 10-year Treasury or ICE BofA OAS series, with recession shading.
- Total return differential chart can remain, but call it corporate excess return versus Treasuries.
- Duration shock table: 2-year, 5-year, 10-year, 20-year, 30-year bonds under +1%, +2%, +3% rate shocks.
- Yield curve animation: 3M, 2Y, 10Y, 30Y over time, showing inversion and un-inversion.
- Bond fund versus individual bond visual: constant-duration fund rolls bonds; individual bond duration declines toward zero.

## Interactive Demo Feedback

The existing `course/interactive/week05_bond_pricer.html` is well matched to the lesson. It has sliders for face value, coupon, maturity, market yield, and payment frequency; it plots the price-yield curve; it reports price, YTM, current yield, Macaulay duration, and modified duration; and it supports multilingual labels and theme changes.

Suggested improvements:

- Add a one-click scenario preset: 2-year Treasury, 10-year Treasury, 30-year Treasury, zero-coupon bond, high-coupon premium bond.
- Add a yield-shock calculator: current price, price after +1%, price after -1%, duration estimate, convexity-adjusted estimate, actual change.
- Add a cash-flow timeline above or below the chart so students see coupons plus face payment.
- Add an individual-bond versus bond-fund mini-toggle: show duration shrinking over time for an individual bond versus staying constant for a fund.
- The chart range starts near 0.1% yield; if teaching zero/negative-rate history, allow 0% and maybe negative yields in an advanced toggle.
- Clarify payment frequency conventions: real-world bonds have day-count conventions and accrued interest; the demo intentionally simplifies.

## New Interactive Demo Ideas

- Bond ladder builder: choose amount, years, and ladder spacing; output maturity schedule, expected annual cash flow, and reinvestment risk.
- Yield curve explorer: drag short, intermediate, and long rates; see how SHY/IEF/TLT-like portfolios respond.
- Credit spread stress lab: choose Treasury/corporate mix and recession spread widening; output drawdown and correlation to equities.
- TIPS breakeven calculator: input nominal yield, TIPS real yield, expected inflation, and see which wins.
- Duration budget tool: user enters portfolio size and maximum acceptable dollar loss for a 1% rate shock; output max duration exposure.

## Make It More Entertaining Without Watering It Down

The lesson should lean into the paradox: bonds are simple contracts but not simple investments. That contrast is entertaining and educational. Use the repeated line: "The contract did not change; the discount rate changed." That is the whole mystery solved.

## Money-Making Usefulness

This lesson can save students from accidental duration risk and bad yield-chasing. The most actionable rule is: before buying any bond fund, know its duration and ask what a 1-2% rate move would do to your dollars. Add this as a highlighted checklist.

## SOUL Consistency Flags

- Strong alignment with SOUL principles #2, #12, #14, and #17.
- Good continuation of the 60/40 regime-break thesis.
- Needs terminology correction around credit spreads versus realized excess returns.
- Fix recurring cross-reference drift around Week 6 and Week 13-14/barbell.
