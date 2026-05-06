# Review: course/week24_multi_strategy.md

## Overall Assessment

Week 24 is a useful Level 2 capstone. It pulls beta, factor tilts, long/short, sector rotation, and tactical overlays into one practical portfolio architecture. The core message is mature: most return comes from beta, alpha is rare, and complexity is usually a tax/fee/behavioral trap.

The lesson needs more precision around institutional analogies, retail alpha vehicles, correlation math, and the four-tranche/barbell mapping. Some examples are technically questionable enough to fix before publication, especially the fund examples and the expected-vol calculation.

## Content Critique

- The opening synthesis is strong and gives the reader a clear sense of progression.
- The distinction between beta, smart beta, alpha, and tactical sleeves is useful.
- The statement that alpha is uncorrelated rather than high-return is one of the best lessons in the file.
- The institutional-template section overgeneralizes. Yale/Harvard endowment models, Norway's sovereign wealth fund, and CPP do not all converge on the same 70/10/10/10 beta/factor/absolute-return shape. Use them as broad inspiration, not as identical templates.
- Retail alpha vehicles need tighter classification. BTAL is closer to a beta-against-beta/anti-beta factor strategy than generic alpha. FTLS is long/short equity with market exposure, not necessarily market-neutral. MERFX is merger arb. `JNK-style merger arb` is wrong; JNK is a high-yield bond ETF.
- The expected-vol example should be recalculated. Using the stated 80% beta, 10% factor, 10% alpha weights and correlations does not obviously produce ~12.85% vol if the beta sleeve's vol is 16%. Clarify whether beta is all-VTI or a 60/40 beta sleeve.
- The layered-return logic is strong: the multi-strategy version may earn less raw return but improve Sharpe by lowering vol.
- The three-year alpha-sleeve shutdown test is too short if framed as statistically decisive. Three years can be a review checkpoint, but not proof of skill or no skill.
- The FIRE/barbell example is inconsistent: one place says 70 beta / 5 factor / 10 alpha / 15 cash, another says 30% cash + 50% VTI + 20% concentrated names.
- The script's tax section jumps to long-dated options and margin before L3. Keep it as a preview, not an implementation instruction.

## Cross-Reference And Consistency Issues

- Week 24 correctly previews Week 25 options in the YouTube outro.
- The lesson says the four-tranche framework was sector-cycle in Week 16. Earlier reviews flagged recurring tranche terminology drift; this file should use the canonical SOUL/tranche vocabulary consistently.
- The word "passive core" should be harmonized with SOUL's barbell/tranche architecture.
- Q&A mentions Week 47 and Week 49 future derivative topics. That is fine if those files exist later, but keep future references stable.

## Presentation Improvements

- Add a warning box: institutional models are governance templates, not direct ETF recipes.
- Add a table classifying retail alternatives accurately: market-neutral, merger arb, long/short equity, managed futures, anti-beta, cash/T-bills.
- Add a Sharpe calculation using excess returns over cash, especially because cash yields are now material.
- Add a correlation-matrix visual and explain how correlations rise in stress.
- Add a decision tree for when to stop at pure beta.
- Add an after-tax column to sleeve assumptions.

## YouTube Script Critique

The script has a good shape and a strong humility message. It should be a useful L2 milestone episode.

Specific improvements:

- Fix the retail alpha fund examples.
- Add Stella asking: "Is this worth the complexity if expected return is lower?" That is the heart of the episode.
- Replace the three-year alpha test with a pre-committed review framework that includes process quality, benchmark fit, taxes, and drawdown tolerance.
- Keep options/margin tax management as a preview for L3, with a suitability caveat.
- Make the institutional section less name-droppy and more precise.

## Chart And Visual Feedback

Existing visuals are useful:

- Sleeve-breakdown stacked bar chart.
- Layered-return decomposition chart.

Recommended upgrades:

- Add correlation matrix across sleeves.
- Add expected-return versus expected-vol scatter for archetypes.
- Add fee/tax drag decomposition.
- Add stress-period correlation spike chart.
- Add pure-beta versus multi-strategy drawdown comparison.

## Interactive Demo Feedback

The referenced `course/interactive/week24_strategy_blender.html` is exactly the right tool for this lesson. Students should feel how small alpha sleeves affect expected return, vol, and Sharpe.

Suggested improvements:

- Include cash yield as an explicit input.
- Let users edit sleeve vol and correlations, not only weights.
- Add fees and tax drag sliders.
- Add stress-mode toggle where correlations rise toward 1.
- Add validation that weights sum to 100% and show excess-return Sharpe.
- Add preset archetypes that match the markdown exactly.

## New Interactive Demo Ideas

- Sleeve X-ray: enter ETF tickers and map them into beta/factor/alpha/tactical buckets.
- Alpha-sleeve shutdown simulator.
- Fee/tax drag calculator.
- Stress-correlation simulator.
- Institutional-to-retail translation tool.

## Make It More Entertaining Without Watering It Down

The best dramatic device is the reveal that adding "sophisticated" sleeves can lower expected return. Let Stella build an impressive-looking book, then have the tool show that beta did the work and fees ate the fancy parts.

## Money-Making Usefulness

This lesson can save students money by convincing most of them not to overcomplicate their portfolios. For the minority who can run active sleeves, the useful money lesson is strict sizing and shutdown discipline.

## SOUL Consistency Flags

- Strongly aligned with SOUL's alpha-is-rare principle.
- Needs tighter alignment with the SOUL barbell/tranche terminology.
- Supports the course's practical retail-investor philosophy: complexity is only worthwhile when it improves after-tax, after-fee, behaviorally survivable outcomes.
