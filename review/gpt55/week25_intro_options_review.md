# Review: course/week25_intro_options.md

## Overall Assessment

Week 25 is a strong options foundation. It teaches rights versus obligations, contract size, moneyness, premium decomposition, exercise style, settlement, and the four payoff shapes in a clear sequence. The focus on vocabulary before strategy is exactly right.

The lesson needs several important caveats before readers act on it: account sizing for high-priced ETFs, tax treatment of covered calls/LEAPS/cash-secured puts, the number of upcoming strategy weeks, and the risk that "options as safe capital efficiency" can sound too easy.

## Content Critique

- The right-versus-obligation framing is excellent.
- The 100-share unit explanation is essential and well taught.
- The moneyness tables are clear.
- Premium decomposition is the right central concept for this lesson.
- "Intrinsic value" should not be described as "frozen" too strongly; it is the exercise value at this instant and changes as spot changes.
- The claim that the next six weeks are strategy material is off if Weeks 26-30 are the intended strategy block. That is five weeks after Week 25, or six weeks including Week 25.
- The account-size examples need correction. SPY and QQQ are high-notional ETFs; cash-secured puts on them usually require far more than $5,000 of collateral unless the strike is absurdly far OTM. For smaller accounts, use lower-priced liquid underlyings, spreads, or no options.
- Weeklies are described as Friday-only. In 2026, major index/ETF products have much more frequent expirations, including 0DTE/daily-style listings. Add a short note while still keeping beginners focused on monthlies.
- The LEAPS-as-stock-substitute discussion should stress that capital efficiency is not safety. Deep-ITM LEAPS still have premium at risk, spread/roll risk, IV sensitivity, and expiry risk.
- Covered calls and cash-secured puts are bounded, but they still inherit stock downside and can create assignment/tax surprises.
- The 30-45 DTE premium-selling rule should be framed as a common retail convention, not a universal empirical law. Shorter DTE has faster theta but higher gamma/assignment/tail risk.

## Tax And Implementation Caveats

- The tax-tool section needs US-tax precision. Selling a covered call can create taxable premium income/short-term capital gains and may affect holding period if the call is not qualified.
- Assignment of a covered call is a taxable sale of the stock.
- LEAPS held more than one year may qualify for long-term treatment when sold, but exercising a call generally starts a new stock holding period; verify details before presenting this as tax planning.
- Cash-secured put premium reduces basis only if assigned under US rules. If the put expires, the premium is usually short-term capital gain, not literally a lowered cost basis for a later purchase.
- Non-US readers need a jurisdiction caveat.

## Cross-Reference And Consistency Issues

- The lesson says Weeks 26-30 depend on this foundation, which is correct, but references to "next six weeks" should be clarified.
- Script host labels are all-caps `HORACE`/`STELLA`, while most English scripts use `Horace`/`Stella`. Standardize.
- The interactive link label includes `course/interactive/...` while the actual href is `interactive/...`; not harmful, but standardize presentation.

## Presentation Improvements

- Add a one-contract notional table for SPY, QQQ, AAPL, IWM, and a lower-priced example.
- Add a warning box: cash-secured does not mean small loss; it means fully funded loss.
- Add a tax caveat box before the options-as-tax-tool section.
- Add a table comparing equity options, ETF options, and index options: exercise style, settlement, assignment, tax notes.
- Add a beginner rule: do not sell naked calls; do not sell puts unless you would own the shares.

## YouTube Script Critique

The script is beginner-friendly and should work well as an L3 launch. The premium-decomposition section is the strongest segment.

Specific improvements:

- Correct the strategy-week count.
- Add a live quote example showing total contract cost and notional.
- Let Stella ask whether a deep-ITM LEAPS call is actually "safe." Horace can answer: safer than shallow OTM leverage, not safer than cash.
- Add a tax caveat in plain language.
- Fix the SPY/QQQ small-account sizing example.

## Chart And Visual Feedback

Existing visuals are useful:

- Premium decomposition chart.
- Four payoff diagrams.

Recommended upgrades:

- Add contract-spec visual showing one option controls 100 shares.
- Add moneyness ladder for calls and puts.
- Add settlement-style comparison chart.
- Add time-value decay curve by DTE.
- Add assignment-event flowchart for short calls and short puts.

## Interactive Demo Feedback

The referenced `course/interactive/week25_option_explorer.html` is the right tool. Sliders for spot, strike, DTE, IV, and rate should make the abstract contract concrete.

Suggested improvements:

- Show total dollars per contract, not just per-share premium.
- Show notional exposure and max loss in account-size terms.
- Add covered-call and cash-secured-put overlays.
- Add assignment/settlement warnings depending on American equity option versus European index option.
- Add a toggle for per-share versus per-contract values.
- Add a tax disclaimer note.

## New Interactive Demo Ideas

- Option-chain quote reader quiz.
- Position-size calculator for one contract.
- Exercise versus sell-to-close decision tool.
- Assignment simulator for short calls/puts.
- LEAPS-as-stock-substitute comparison versus shares.

## Make It More Entertaining Without Watering It Down

The best entertaining angle is the "one contract is not one share" reveal. Show Stella thinking a call costs $8.65, then discovering it costs $865 and controls $20,000 of stock. That moment will save viewers real money.

## Money-Making Usefulness

This lesson makes students safer before it makes them richer. That is the correct order for options. The most valuable outcome is preventing contract-size, exercise, and naked-short mistakes.

## SOUL Consistency Flags

- Aligns with SOUL's use of options as expression tools, tax tools, and tranche/barbell mechanics.
- Needs stronger caution that options are expression tools, not automatic alpha.
- Tax and jurisdiction caveats are required before tying options to after-tax return management.
