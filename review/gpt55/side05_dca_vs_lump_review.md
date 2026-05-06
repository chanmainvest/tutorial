# Review: course/side05_dca_vs_lump.md

## Overall Assessment

This is one of the more audience-friendly side lessons. The windfall framing is correct, the behavioral explanation is useful, and the YouTube script has a strong hook.

The lesson needs numerical reconciliation. Several claims conflict with each other, and the interactive does not use actual monthly market history even though the script says it does.

## Content Critique

- The core conclusion is right: lump sum wins in expected value when the risky asset has a positive expected excess return, while DCA can be valuable behavioral insurance.
- The lesson should separate math, empirical data, and behavior more cleanly. `Lump wins about two-thirds of the time` is empirical, not a mathematical identity.
- The expected-cost numbers conflict. §2.2 says 12-month DCA gives up `0.5-0.7%`, while §2.3/Q2/script say average lump outperformance is about `2.3%`. Pick one framework and reconcile the assumptions.
- The equation omits the return on idle cash. The text says uninvested cash earns T-bills around 4.2%, so the formula should include cash yield.
- `60/40 portfolio (expected ~6.5% over cash)` looks too high/unclear. If 6.5% is the total nominal expected return, say so. If it is excess return over cash, the DCA cost should be much larger than 0.6%.
- The lesson says paycheck investing is not DCA in §2.1, then later says paycheck contributions are already DCA. Use one term consistently, such as `systematic paycheck investing`, and reserve `DCA` for windfall deployment.
- Q7 says lower-return assets should have lower lump-sum win rates, but then says bonds had a 70% win rate versus 66% for stocks. That explanation contradicts the numbers.
- The 1929/1937/1973/2008 examples need source verification. The January 1929 one-year `-68%` claim is especially suspect if measured strictly over the next 12 months.
- The 2008 T-bill statement likely overstates the cash-yield improvement. Cash yield in 2008 should not move a 12-month DCA result from roughly -27% to -19% unless a different benchmark/window is being used.
- Q6 is wrong or at least badly phrased. If equities have a positive expected return over cash, delaying sales through DCA-out has higher expected wealth than lump-selling, while lump-selling reduces risk sooner. The lesson says lump-selling has higher expected value.
- The target-allocation line should not say the receiving allocation is simply `SPY` for every apprenticeship investor. It should say broad low-cost target allocation, often broad US equity for young accumulation investors, with age/risk/IPS caveats.

## Structure And Formatting Issues

- The decimal structure is correct and easy to follow.
- The lesson is strongest when it stays with the windfall decision. The passive-consensus/barbell paragraph is useful but slightly long for this side lesson; tighten it so it does not distract from the DCA decision.
- `Procrastination wearing a financial-advisor costume` is memorable, but it may feel a little too scolding for nervous beginners. Keep the wit, reduce the shame.

## YouTube Script Critique

The script has a very good opening because Stella says the exact thing viewers are thinking: leave it in cash while deciding.

Needed fixes:

- Reconcile the DCA cost: the script says `$2,300 on $100k`, while the reading says `$600-$850 on $120k`.
- The script says the interactive uses `exactly the same monthly equity returns that produced actual historical outcomes`; this is false based on the current HTML.
- The 2020 example should be verified against the interactive's synthetic path, because it may not match actual monthly S&P returns.
- The `irrational and solvent beats rational and bankrupt` line is catchy but too extreme for a simple 30% drawdown. `Irrational and still invested beats rational and panic-sold` would be more precise.

## Chart And Interactive Feedback

`side05_dca_lab.html` is engaging, but it is not the historical backtest described in the lesson.

Issues:

- It uses Damodaran annual S&P 500 returns and splits each year into deterministic synthetic monthly returns. That is not actual monthly history.
- It only lets the reader select a start year, not a start month, yet the reading discusses rolling monthly starts and examples like `Oct 1987`.
- Cash earns 0% in the widget, while the reading repeatedly references T-bill yield on idle cash.
- The displayed max drawdown is only the lump-sum path during the deployment window, but the stat label does not make that obvious.
- The synthetic monthly construction can create paths that match annual returns but distort intra-year drawdowns, DCA outcomes, and disaster timing.
- Best upgrade: use actual monthly S&P total-return data, add start-month selection, add a cash-yield input, and label whether returns are nominal/real and price/total return.

## SOUL Consistency Flags

- The apprenticeship-first paragraph is a good SOUL bridge: do not copy the advanced barbell until the toolkit is built.
- The lesson should still teach orthodox target-allocation language first, then explain Horace's US-index apprenticeship and later barbell migration as a house view.
