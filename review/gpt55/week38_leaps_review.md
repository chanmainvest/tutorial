# Review: course/week38_leaps.md

## Overall Assessment

Week 38 is a strong continuation of the options leverage arc. The lesson explains why long-dated options behave differently from short-dated speculation, and the theta curve is a good anchor for students.

The main issues are precision and payoff mechanics. Several statements make LEAPS sound cleaner or more self-financing than no-arbitrage pricing allows. The PMCC payoff description is too simplified, and the interactive has mismatches with the lesson/script.

## Content Critique

- The lesson correctly emphasizes that LEAPS are ordinary options with a longer time scale.
- The theta explanation is useful, but the $1/\sqrt{T}$ rule should be framed as an approximation, mainly for the volatility/extrinsic term. Rates, dividends, moneyness, and deep-ITM behavior can change the result.
- The intro says LEAPS have expirations more than one year out, while §2.1 says CBOE convention is more than nine months. Harmonize the definition.
- The tax section is much better than Week 37's loss wording, but state-tax and broker/reporting caveats still need softening.
- "Options are the most tax-efficient leverage" should remain a thesis, not a blanket rule. PMCC short calls, Section 1256 index options, exercise, wash sales, constructive sales, and account type all matter.
- The PMCC payoff description says profit is capped flat above the short strike because every dollar of upside is offset by the short call. At the short-call expiration, the long LEAPS still has residual time value and delta less than or near 1; the shape is not always a clean covered-call plateau.
- The PMCC max-loss description mixes short-call-expiration and LEAPS-expiration horizons. At the short call's expiration, the LEAPS may retain substantial residual value; max loss equal to net debit is a final-expiration concept or an extreme collapse scenario.
- The rule that the short call strike must be above the LEAPS strike is directionally good for PMCC risk hygiene, but the explanation about "avoiding a calendar that pays a debit" should be tightened.
- The "LEAPS is roughly self-financing" claim needs put-call-parity and dividend caveats. Freed-cash carry is real, but rates/dividends are embedded in the option price.
- The SPY roll-cost estimate of 4-6% of notional needs a source or recalibration.

## Cross-Reference And Consistency Issues

- Week 37 previewed poor-man's covered call next week; Week 38 is named LEAPS and includes PMCC as one strategy, so the transition partly works but the filename/title mismatch may still confuse navigation.
- Week 38 previews Week 39 as broken-wing butterflies and ratio spreads; verify the actual Week 39 file before publishing.
- The tranche mapping again needs course-wide consistency: stock replacement as L1, PMCC as L2, married LEAPS as L3 may be fine, but it should not conflict with the four-tranche framework elsewhere.

## Presentation Improvements

- Add a clear timeline diagram for PMCC: long LEAPS expiry, short-call cycles, roll point, tax year boundary.
- Add a "same trade, different horizon" table: at short-call expiry versus LEAPS expiry.
- Add a box explaining when PMCC behaves like covered stock and when it behaves like a diagonal spread.
- Add a no-arbitrage caveat: LEAPS reduce capital outlay but do not make financing free.
- Add a liquidity checklist for LEAPS rolls.

## YouTube Script Critique

The script has good pacing and a strong Stella/Horace exchange. The PMCC section is likely to attract views because it has a practical income angle, but it needs a little more danger and specificity.

Specific improvements:

- Replace "essentially free leverage" with "low daily theta leverage, but not free leverage."
- Add a Stella objection: "If this is so clean, why doesn't everyone replace stock with LEAPS?"
- Explain assignment and forced closing in one simple PMCC scenario.
- Avoid saying the LEAPS-PMCC is the cleanest example of tax-efficient leverage without immediately caveating short-call tax noise.
- The married LEAPS example says a 95-strike put, but the interactive default appears to use the same short-leg slider default of 110%.

## Chart And Visual Feedback

Existing visuals are valuable:

- Theta curve.
- PMCC payoff.

Recommended upgrades:

- Re-label the PMCC payoff as "at short-call expiration" and show residual LEAPS value explicitly.
- Add a second PMCC payoff at LEAPS expiration to distinguish horizons.
- Add a theta-as-percent-of-premium chart, because the lesson correctly notes that low dollar theta can still be high percentage theta for low-delta options.
- Add a vega shock chart for 24-month LEAPS.

## Interactive Demo Feedback

The `week38_leaps_lab.html` interactive is useful, but it should be revised before being treated as an operating tool.

Issues and improvements:

- The model excludes dividend yield even though dividend risk is a central part of the lesson.
- The chart shows P&L at the short-leg expiration, but max loss is displayed as the full net debit for LEAPS/PMCC/married structures. At short-leg expiration, that can be inconsistent because the long LEAPS still has residual value.
- The married LEAPS + put mode uses the short-leg strike slider; the default is 110% of spot, while the script describes a 95-strike put. That creates a material mismatch.
- Add separate controls/defaults for PMCC short-call strike and married-put strike.
- Add actual delta, vega, theta, and extrinsic value by leg.
- Add warning states when short-call strike is too close to the LEAPS strike or when net debit exceeds vertical width.
- Add assignment-risk notes for PMCC.
- Add a horizon toggle: short-leg expiry, LEAPS expiry, and roll date.

## New Interactive Demo Ideas

- PMCC assignment simulator.
- LEAPS roll calendar with tax holding-period tracker.
- Dollar theta versus percentage theta comparator.
- Vega-crush lab for 24-month options.
- PMCC strike selector showing upside cap, credit, delta, and assignment probability.

## Make It More Entertaining Without Watering It Down

This video could open with a provocative comparison: "100 shares costs $10,000; a PMCC costs $2,350. Which one is actually riskier?" Then reveal that the answer depends on sizing and what happens to the freed capital.

## Money-Making Usefulness

Week 38 has high practical value, especially for students who already understand covered calls. The key is preventing students from sizing by premium and accidentally creating a much larger total risk exposure.

## SOUL Consistency Flags

- Strong alignment with SOUL's options-as-expression-tool and tax-aware leverage themes.
- Needs a stronger warning that redeployed freed capital increases total portfolio risk.
- Tranche mapping should be standardized across Weeks 24, 34-38.
