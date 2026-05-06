# Review: course/week52_integration.md

## Overall Assessment

Week 52 is a strong closing lesson. The IPS frame is exactly the right capstone: students need governance more than one more strategy. The tone is practical, the one-page rulebook concept is memorable, and the tax-location appendix is valuable.

However, this file has several course-level consistency problems and model-risk issues. It calls the course four levels even though the repo/course is structured around five, labels the capstone `L4` after multiple L5 topics, and presents a model allocation/backtest whose sleeves require substantial proxy/backfill assumptions.

## Content Critique

- The IPS framing is excellent: calm-you writing rules for panicked-you is the right behavioral close.
- `The four levels of this course` conflicts with the project structure, which has five levels.
- The title `L4 Capstone` conflicts with the advanced L5 language used in Weeks 49-51 and with the five-level course architecture.
- The model allocation labels the equity sleeve `Global equity`, but the implementation examples are US-only: VTI, AVUV, MTUM. Rename or add explicit VXUS exposure.
- The 35% equity / 25% income / 20% store-of-value / 15% opportunistic / 5% cash model is interesting, but should be framed more explicitly as Horace's house-view portfolio, not a generic recommendation.
- The tail-hedge sleeve says `long-dated SPY puts` but specifies 60-90 DTE. That is not long-dated.
- The 5% tail-hedge sleeve repeats a major Week 47 issue: the claim that 25-30% OTM puts with 1-2% annual drag can pay 30-60% of NAV in a -30% market needs contract math and strike/DTE assumptions.
- The Q&A says a 28-year-old can use 90% VTI / 10% SGOV, while §2.2 says a 28-year-old should probably run 90/10 VTI/AVUV. Reconcile starter allocation guidance.
- The backtest needs much stronger disclosure. It includes ETFs/strategies with limited live history: AVUV, IBIT, JEPI, DBMF/KMLM, and the tail-hedge sleeve. The text should state which series are live, proxy, synthetic, or backfilled.
- The L4 model's reported 2022 worst year of -2.7% is plausible only under specific CTA/tail/BTC assumptions; those should be shown.
- The table uses annual-return volatility and worst calendar year; it correctly notes intra-year drawdowns are larger, but the headline Sharpe should not be overused.
- The rebalancing-premium claim of 0.2-0.5% per year needs a source and caveat. Rebalancing premium depends heavily on volatility, correlations, tax, and drift.
- Tax-location guidance is useful but too categorical in places. Dividend equity in taxable versus tax-deferred depends on current/future tax rates and Roth availability.
- Factor tilts `lean taxable` conflicts with Week 50's advice that AVUV may belong in IRA because of turnover.
- CTA tax treatment should keep the Week 51 nuance: fund-level 1256 distributions are not identical to directly trading futures, and ETF share sales have their own tax treatment.
- The withdrawal section is good, but the 3.7% rigid / 4.5% flexible April-2026 numbers need source/date labels.
- Hyperinflation and capital-controls scenarios are a strong final SOUL-aligned note.

## Cross-Reference And Consistency Issues

- Course level count: Week 52 says four levels; repository and overview pages use five levels.
- L4/L5 labeling: Week 52 title says L4 capstone while Weeks 49-51 are explicitly Level 4/5 or L5.
- Week 47 tail-hedge sizing issues reappear in Week 52.
- Week 48-49 SPY/SPX tax distinctions should be reflected consistently in the tail-hedge implementation.
- Week 50 says AVUV may be IRA-preferred; Week 52 says factor tilts lean taxable.
- Week 51 synthetic CTA proxy concerns carry into the Week 52 backtest.

## Presentation Improvements

- Rename the lesson as full-course capstone or Level 5 capstone unless the level map says otherwise.
- Add a model-assumption appendix for every backtest sleeve.
- Add a `live / proxy / synthetic / backfilled` column to the allocation/backtest table.
- Add a one-page IPS template image before the model allocation.
- Add a tail-hedge contract-sizing table if the lesson keeps the 30-60% NAV payoff claim.
- Add a starter IPS progression: <$100k, $100k-$200k, $200k+, retirement/decumulation.

## YouTube Script Critique

The script lands emotionally. The final `discipline is the alpha` line works.

Specific issues:

- The video title `One Page That Beats Most Hedge Funds` is strong but overclaims. Better: `One Page That Beats Most Retail Mistakes`.
- The script repeats the tail-hedge payoff claim without showing the math.
- The script says the L4 gets through 2022 `flat-to-slightly-positive`, but the reading table says -2.7%.
- The script says the IPS builder uses historical mean and vol of the L4 model; the interactive actually uses sleeve-level assumptions and a simplified variance model.
- The script says 1000 Monte Carlo paths; the interactive uses 600.
- The closing instruction to print the IPS is memorable, but the repo should also make the generated text easy to export or copy if this becomes a real user workflow.

## Chart And Visual Feedback

Existing visuals are important:

- Allocation pie.
- Backtest comparison.

Recommended upgrades:

- Add assumptions table next to the backtest.
- Add `live history begins here` markers for JEPI, AVUV, IBIT, DBMF/KMLM, and any tail-hedge proxy.
- Add max drawdown chart, not just wealth chart.
- Add sequence-of-returns retirement stress chart.
- Add tax-location map visual.

## Interactive Demo Feedback

The `week52_ips_builder.html` interactive is the right tool for the capstone, but it needs assumption and logic fixes.

Issues and improvements:

- Caption says 1000 Monte Carlo paths; code uses 600.
- The script says historical mean/vol of the L4 model; code uses sleeve-level expected returns and vol assumptions.
- The model uses normal annual returns, which understates fat tails and sequence risk.
- The tool does not ask for annual contributions/savings rate, so the retirement projection only compounds the current portfolio. That should be explicit.
- The `Sustainable SWR` card always displays 3.7% when a projection exists, even when the target income is not funded. It should show required withdrawal rate, funded/unfunded status, or flex-rule feasibility.
- Portfolio volatility is computed using independent weighted variances plus a 0.95 adjustment; no covariance matrix is used.
- Tail-hedge allocation appears as a current dollar sleeve, which may confuse premium budget, collateral, and option market value.
- Expected returns for BTC, tail hedges, gold, CTA, and income sleeves are hardcoded and should be surfaced or editable.
- Add a `download/copy IPS` control only if the website UX supports it cleanly.

## New Interactive Demo Ideas

- IPS template editor with explicit account-location map.
- Tail-hedge premium budget and contract-sizing calculator tied to the IPS.
- Retirement contribution planner with savings rate and inflation assumptions.
- Sequence-risk simulator for first five retirement years.
- Backtest assumption inspector showing live/proxy/synthetic status.

## Make It More Entertaining Without Watering It Down

The strongest video framing is a courtroom contract: calm-you signs the document, panicked-you tries to break it, and the IPS says what evidence is required before changing the plan.

## Money-Making Usefulness

This is one of the highest-utility lessons in the course because it converts knowledge into behavior. It can help students make more money by preventing panic-selling, overtrading, tax-location mistakes, and sleeve stacking. The model portfolio and Monte Carlo must be made more transparent so the governance lesson is not undermined by overprecise numbers.

## SOUL Consistency Flags

- Strong SOUL alignment: barbell, tail hedges, stores of value, US-only house view, and written discipline all appear.
- Needs cleaner four-tranche/five-level wording.
- Needs explicit distinction between Horace's house-view allocation and orthodox default advice.
- Tail-hedge and CTA sizing must be corrected so the final capstone does not inherit earlier overclaims.
