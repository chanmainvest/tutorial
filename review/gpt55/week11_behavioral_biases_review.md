# Review: course/week11_behavioral_biases.md

## Overall Assessment

Week 11 is one of the most practical lessons so far. The central thesis is excellent: the spreadsheet strategy and the human behavior that must hold it are different things. The move from naming biases to designing systems is exactly right for retail investors.

The lesson should tighten its evidence language around DALBAR, avoid absolute claims about every behavioral rule losing in every backtest setting, and fix cross-reference drift. It also needs slightly more empathy in the YouTube ending: the goal is not to shame the student, but to make them feel protected by good systems.

## Content Critique

- The opening is strong and relatable. The brother-in-law meme-stock example is memorable and useful.
- The DALBAR section is important, but "pure behaviour" is too clean. DALBAR's methodology has critics, and the gap can include cash-flow timing, fund selection, asset-class mix, and measurement choices. Keep the core lesson but add a caveat.
- "The headline finding, replicated every year" should be softened. Say the gap is persistent across many QAIB reports, not mechanically the same every year.
- The 2 to 2.5x loss-aversion framing is good and visually teachable.
- The inheritance test is excellent. Keep it and make it a recurring checklist item in later stock-selection lessons.
- The herding/FOMO section is entertaining and conceptually strong.
- The narrative-fallacy section is valuable because it trains students to distrust daily market explanations.
- The overconfidence section should distinguish normal confidence from sizing error. Confidence is not the enemy; unbounded sizing is.
- The system-design section is the lesson's strongest practical contribution. Consider making it the visible capstone earlier, not only at the end.
- "Every bias rule loses to do nothing" is too absolute. A bad tactical rule usually loses, but some trend-following and risk-management rules can improve risk-adjusted outcomes. The criticism should be of emotional rules, not all rules.

## Cross-Reference And Consistency Issues

- Q9 says the barbell is covered in Week 14, but Week 14 is pair trading in the course map.
- The end screen says next is Week 12: Inflation and the Real Return, but Week 12 is first portfolio. Inflation is a side lesson.
- The barbell explanation introduces long calls and asymmetric bets before the options sequence. That may confuse Level 1 students unless framed as a preview.

## Presentation Improvements

- Add a "bias -> symptom -> system fix" table:
  loss aversion -> panic selling -> rebalancing rule;
  recency -> chasing -> contribution automation;
  anchoring -> cost-basis fixation -> inheritance test;
  overconfidence -> oversizing -> max position rule.
- Add an investment policy statement template.
- Add a one-page drawdown checklist: what to check before selling.
- Add a brokerage-app hygiene checklist: remove daily P/L widgets, turn off push alerts, schedule review frequency.
- Add a tax-aware disposition-effect example: selling winners and holding losers versus harvesting losses and deferring gains.

## YouTube Script Critique

The script is emotionally effective and likely more watchable than a standard behavioral-finance lecture. The opening has a strong hook, and Stella's role keeps the lesson accessible.

Specific improvements:

- Soften "Strategy beats you" to something like "Systems protect you from your worst trading day." It lands less harshly and is more motivating.
- Make Stella push back: "If everyone has biases, is the lesson just that I'm doomed?" This lets Horace pivot to system design.
- Add one dramatic visual sequence: account value after panic exit versus automatic contribution through a crash.
- Add a concrete viewer action: write one forbidden action into an investment policy statement before the next episode.
- Fix the end-screen preview.
- Avoid implying all discretionary adjustment is bad; the course itself teaches regime-aware adjustments later.

## Chart And Visual Feedback

Existing visuals are appropriate:

- DALBAR gap chart is the right money-loss visual.
- Kahneman-Tversky value function is essential for loss aversion.

Recommended upgrades:

- Add a behavior-cost compounding chart: 10% return versus 7% return over 30 years.
- Add a disposition-effect tax chart: sell winners/hold losers versus harvest losers/defer winners.
- Add a portfolio-checking-frequency chart showing probability of seeing a loss daily/monthly/annually.
- Add a market-bottom redemption chart for 2008 or 2020.
- Add an IPS template visual.

## Interactive Demo Feedback

The referenced `course/interactive/week11_bias_simulator.html` is a strong concept. Toggling behavioral actions and comparing them with buy-and-hold is exactly the right way to make the lesson experiential.

Suggested improvements:

- Label rules as "emotional rules" rather than implying all systematic rules fail.
- Add a DCA/automation scenario as a positive system, not only negative behaviors.
- Add drawdown, volatility, and final wealth metrics, not just terminal wealth.
- Add tax drag for selling winners.
- Add a market-stress mode that hides the future path, so users feel the uncertainty at the time of decision.
- Add source/methodology notes for the historical backtest.

## New Interactive Demo Ideas

- Investment policy statement builder with pre-filled triggers and forbidden actions.
- Panic-sell calculator: choose exit and re-entry delay during 2008 or 2020 and see missed recovery cost.
- Portfolio-checking frequency simulator: daily versus monthly versus annual review and probability of seeing red.
- FOMO simulator: chase a hot asset after different trailing-return windows and compare future returns.
- Cost-basis eraser: show a position with and without cost basis visible, then apply inheritance-test logic.

## Make It More Entertaining Without Watering It Down

This lesson can be entertaining because everyone recognizes themselves in it. Use humor through Stella's embarrassment and Horace's realism, but keep the ending empowering: the student is not weak; the system is there because the environment is engineered to trigger weakness.

## Money-Making Usefulness

This is highly money-useful. Avoiding one panic sale, one FOMO chase, or one overconfident oversized position can be worth more than many hours of valuation work. The lesson should end with a concrete assignment: automate one contribution, set one rebalance rule, and write one forbidden action.

## SOUL Consistency Flags

- Strong alignment with SOUL principle #8: irrational can last longer than solvency.
- Strong alignment with SOUL principle #12: liquidation and tax behavior matter.
- The barbell discussion should not be presented as if it is already taught in Week 14 unless the course order changes.
- Make sure system design does not contradict later regime-aware discretion; distinguish rule-based discretion from emotional override.
