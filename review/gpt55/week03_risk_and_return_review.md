# Review: course/week03_risk_and_return.md

## Overall Assessment

Week 3 is conceptually strong and educationally important. It turns "risk" from a vague warning into a set of usable distinctions: volatility, drawdown, beta, systematic versus unsystematic risk, time horizon, and risk capacity versus risk tolerance. The lesson also does a good job connecting risk to future course topics like 60/40, rebalancing, options, tail risk, and barbell construction.

The best section is risk capacity versus risk tolerance. That is practical, memorable, and directly money-protective. The fat-tail critique is also directionally right and consistent with SOUL.md, but it needs careful wording so students learn model limits rather than simply learning to mock models.

## Content Critique

- The opening is good: it correctly says the hard part is not buying the index ETF, but holding it through drawdowns.
- "Higher expected return requires higher risk" should be refined to "higher compensated expected return requires bearing risks that the market pays for." Some risks are uncompensated; some high-risk trades have negative expected return.
- The lesson correctly separates volatility from risk. Add a simple example where volatility is helpful: a young accumulator dollar-cost averaging into a falling market.
- The standard deviation section is clear, but every volatility table should state period and data source. Asset-class volatility changes materially depending on window.
- The Bitcoin volatility note is useful, but 15 years of data is too short and regime-dependent. The Q&A acknowledges this; the main table should also mark BTC as young / unstable estimate.
- The equity risk premium section is strong. It should distinguish realized historical ERP from implied forward ERP even more visibly, maybe with a small table.
- CAPM is introduced well as orthodox professional knowledge. Good SOUL fit: teach the model, then say where it fails.
- The systematic/unsystematic risk section is excellent for index-fund logic. It should add that concentrated positions can be rational only when the investor has a real edge, a risk budget, and a sizing rule.
- The drawdown chart text has an internal inconsistency: the prose says "from 1950 onward," but the image caption says monthly data is 1985-2026 and that 1973-74 predates the monthly series. This should be harmonized.
- The 5-sigma discussion is entertaining, but "happens roughly every decade" is too loose unless model and horizon are specified. Better: "Markets produce moves that Gaussian models label impossibly rare with embarrassing regularity."
- The barbell Q&A is valuable, but for Week 3 beginners it may need a preview note: "You are not ready to implement this yet; the point is how to think about risk measurement."

## Presentation Improvements

- Add a one-page risk dashboard at the end: volatility, max drawdown, recovery time, beta, correlation, liquidity, forced-seller risk, tail risk.
- Add a worked example using Stella's portfolio: $10,000 invested, 80/20 allocation, potential dollar drawdown, forced-seller question.
- Use more side-by-side "textbook measure / investor experience" formatting. Example: standard deviation says one thing; drawdown chart says what it feels like.
- Move the "risk capacity vs tolerance" quadrant visually earlier or tease it at the start. It is the most actionable concept.
- Add a glossary box for sigma, beta, covariance, CAPM, ERP, drawdown, recovery time, sequence risk.

## YouTube Script Critique

The script is focused and paced better than Week 2. The title is good because "Five-Sigma Lie" creates curiosity, but the video should be careful not to make the first impression sound anti-math. Horace should be positioned as anti-bad-model, not anti-quant.

Specific improvements:

- Start with a dollar drawdown, not just concepts: "Your $100,000 ETF becomes $60,000. Do you still believe the spreadsheet?"
- Give Stella the skeptical line: "If standard deviation is flawed, why do professionals still use it?" This lets Horace teach model usefulness and limits.
- Use the risk capacity/tolerance quadrant as the emotional centerpiece. The retiree example is very strong and should be dramatized with cash withdrawals on screen.
- Add more visual pattern interrupts in the CAPM/beta section, which is likely the driest part.
- The ending should ask viewers to do one action: calculate whether they would be a forced seller after a 50% equity drawdown.
- The next-week bridge to 60/40 is excellent because it makes Week 4 feel like a real application rather than another topic.

## Chart And Visual Feedback

Existing visuals are good:

- Return distribution histogram with normal overlay is the correct chart for fat tails.
- Drawdown chart is emotionally important and should be emphasized more than volatility.
- Holding-period chart is a good bridge between long-term optimism and sequence-risk caution.

Issues and upgrades:

- Fix the drawdown chart date mismatch in text/caption.
- Add a normal-versus-actual tail zoom. The current histogram may not make tail excess obvious to beginners.
- Add a dollar drawdown chart: show $100,000 falling 50%, then needing 100% to recover.
- Add a rolling 30-year cumulative wealth chart alongside annualized returns. The lesson correctly says time narrows annualized rate but not wealth gap; visualize that.
- Add a risk-capacity matrix graphic with examples in each quadrant.
- Add a correlation heatmap preview for equities, bonds, gold, cash, long vol.

## Interactive Demo Feedback

The existing interactive at `course/interactive/week03_holding_periods.html` is a solid implementation. It includes holding-period presets, a 1-30 year slider, real/nominal toggle, histogram, worst/median/best windows, windows-below-zero statistic, multilingual labels, theme support, and iframe height messaging. This is genuinely useful and matches the lesson's §2.7 promise.

Suggested improvements:

- Add a cumulative wealth panel. Annualized return is abstract; showing $10,000 becoming different end values makes the range more visceral.
- Add a drawdown overlay or worst intra-window drawdown for the selected holding period. A 20-year positive annualized return can still contain a terrifying 50% drop.
- Add a "starting-year spotlight" mode: hover or select a window and show what was happening historically.
- Add a confidence warning: this is US historical data, not a guarantee for every market or future period.
- Improve mobile density by letting stat cards collapse into a horizontal scroll or smaller metric row if text overflows in Chinese.

## New Interactive Demo Ideas

- Forced-seller simulator: enter portfolio size, annual spending need, stock allocation, and drawdown; output whether the investor must sell risk assets to fund spending.
- Risk capacity/tolerance questionnaire: asks objective capacity questions separately from emotional tolerance, then shows quadrant placement.
- Fat-tail simulator: compare normal-distribution simulated returns with historical bootstrapped returns and see how often extreme drawdowns occur.
- Beta explorer: choose assets with beta/correlation assumptions and watch portfolio beta change.
- Recovery math slider: drawdown percentage -> required gain -> years needed at 5%, 7%, 10% return.

## Make It More Entertaining Without Watering It Down

The entertainment should come from exposing the gap between spreadsheet risk and lived risk. Use a recurring device: "What the model says" versus "What your brokerage app shows in red." This keeps the rigor while making the student's nervous system part of the lesson.

## Money-Making Usefulness

This lesson helps students make money by keeping them solvent and invested. Its actionable edge is position sizing: if a 50% drop makes you a forced seller, the position is too large. Put that rule in a highlighted exercise and repeat it throughout the course.

## SOUL Consistency Flags

- Strong alignment with SOUL principle #12: being right is not enough; you must survive.
- Strong alignment with SOUL principle #8: volatility regime awareness matters, though the lesson only previews it.
- Strong alignment with SOUL principle #14 and #17 through the barbell/tail-risk discussion.
- Needs a small caveat that barbell/long-vol implementation is advanced and should not be copied from Week 3 alone.
- Fix the internal drawdown chart date inconsistency.
