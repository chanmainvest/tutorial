# Review: course/week32_duration_convexity.md

## Overall Assessment

Week 32 is practical, valuable, and well sequenced after the yield-curve lesson. The TLT case study is exactly the right way to make duration feel real: students see that the loss was not mysterious, it was in the prospectus.

The lesson needs several technical and presentation corrections. The biggest issue is a bull-steepener/bull-flattener inconsistency, plus overbroad language about Treasuries not being genuine safety. The interactive is strong but should label its assumptions more explicitly.

## Content Critique

- The opening "how much" frame is excellent.
- The Macaulay duration explanation is clear and accessible.
- The lesson should distinguish more carefully between Macaulay duration as weighted average time and modified duration as price-yield semi-elasticity. The opening says duration "equals" elasticity, which compresses two related but different concepts.
- The TLT case study is the strongest part of the lesson.
- The claim that TLT's 2022 drawdown was worse than the S&P 500 in 2008 should be checked. S&P 500's 2008 total return was roughly -37%, so TLT's roughly -29% total return was not worse on a total-return basis.
- The convexity section is strong but should avoid making positive convexity sound literally free. Investors pay through yield, and term premium/convexity pricing is more complex than a simple discount.
- §2.5 says the 2024 rally was a bull steepener with long rates down faster than short. That is a bull flattener by the Week 31 definitions. A bull steepener means short rates fall faster than long rates.
- The same bull-steepener inconsistency appears in the YouTube script.
- The key-rate duration section is useful, but "Week 31's barbell strategy" could confuse bond barbell construction with SOUL's portfolio barbell.
- Horace's view is philosophically consistent with SOUL but should acknowledge the orthodox case: long Treasuries can still hedge deflationary recession shocks. They failed in 2022 because inflation and real-rate shocks dominated.
- Practical Rule 1 on immunization is useful but should mention nominal versus real liabilities and reinvestment assumptions.
- Q5's line that the Fed had told the market it would hike makes the 2022 short-duration trade sound easier in hindsight than it was. Soften to "the direction was visible; the path and sizing were not."
- Q6's convexity-discount estimate needs a source or a softer label.
- Q11 should clarify that option-adjusted duration is a model-based effective duration under an option-adjusted spread framework, not a wholly separate concept.

## Cross-Reference And Consistency Issues

- Week 31 and Week 32 disagree on bull steepener mechanics. Week 31 is mostly correct: short rates fall faster than long rates.
- Week 32's outro previews Week 33 as credit spreads. This should be checked against the actual Week 33 file.
- The Horace-view critique of long Treasuries should be aligned with Week 5 and Week 31 so the course does not imply long Treasuries are never useful.

## Presentation Improvements

- Add a mini table: Macaulay, modified, effective, key-rate duration.
- Add a "units matter" callout: bps, decimal yield changes, years, DV01.
- Add a one-row correction note explaining why 2022 was inflation/rate shock, not deflation recession.
- Add a side-by-side chart: long Treasuries in 2008/2020 versus 2022.
- Add a retail checklist: find ETF duration, multiply by shock, estimate loss, compare with risk budget.

## YouTube Script Critique

The script has a strong title and a strong viewer promise. The TLT segment should work well because it answers a painful question with one simple calculation.

Specific improvements:

- Correct the bull-steepener wording.
- Add a Stella question: "But didn't long Treasuries save portfolios in 2008?" That would let Horace distinguish deflation hedge from inflation shock.
- Replace "Treasuries are safe is expensive" with "Treasuries are credit-safe, not duration-safe" to keep the message precise.
- Tighten the effective-duration/MBS segment with one simple homeowner refinancing example.
- Use one on-screen formula at a time; the convexity formula may be too dense unless animated.

## Chart And Visual Feedback

Existing visuals are useful:

- Macaulay duration curve by coupon.
- Price-yield curve with duration and convexity approximations.

Recommended upgrades:

- Add TLT 2022 attribution chart: duration loss, convexity gain, coupon carry, realized total return.
- Add duration versus maturity comparison for SHV, IEF, TLT, ZROZ.
- Add key-rate duration bar chart.
- Add inflation shock versus recession shock comparison for Treasuries.

## Interactive Demo Feedback

The `week32_duration_lab.html` interactive is strong and aligned with the lesson. It lets students move maturity, coupon, yield, and rate shock while comparing exact, linear, and convexity-adjusted prices.

Suggested improvements:

- Label that the lab prices a vanilla fixed-coupon bond with semiannual coupons.
- Explain that effective duration matches modified duration here because the cash flows are fixed.
- Add a zero-coupon preset.
- Add an ETF preset row for SHV/IEF/TLT/ZROZ.
- Add a warning when a negative shock hits the near-zero yield floor.
- Add a key-rate shock mode to connect with §2.5.

## New Interactive Demo Ideas

- TLT 2022 replay lab.
- Duration budget calculator for a bond ETF portfolio.
- Key-rate duration hedge builder.
- MBS negative-convexity simulator.
- Equity-duration comparison lab for growth versus value stocks.

## Make It More Entertaining Without Watering It Down

The "look up your fund duration and write it on the wall" ending is memorable. Make it more visual: Stella can type TLT duration into the formula live, then reveal that the 2022 loss was almost pre-written.

## Money-Making Usefulness

This lesson directly helps students avoid hidden duration concentration. It does not tell them which bond to buy, but it gives them the risk calculator they need before buying any bond fund.

## SOUL Consistency Flags

- Strongly aligned with SOUL's critique of passive 60/40 complacency and the post-2022 regime break.
- Needs orthodox-first balance: long Treasuries are not always false safety; they are regime-dependent hedges.
- The safety end of the SOUL barbell should be described as Horace's implementation choice, not a universal fixed-income law.
