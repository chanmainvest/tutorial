# Review: course/side09_crypto.md

## Overall Assessment

This is an engaging and mostly well-framed crypto lesson. It does the right thing by treating BTC as a belief/store-of-value asset, not an income asset, inflation hedge, or guaranteed diversifier. The 1-5% sizing frame is sensible for a retail investor who chooses to own it.

The main risks are tax precision, ETF-wrapper precision, and overconfidence around the still-unfinished 2024-2025 cycle.

## Content Critique

- The belief-asset framing is strong and consistent with the course philosophy.
- The opening says BTC had two complete crashes of about -85%, while later sections list three deep drawdowns. Standardize.
- All 2025/April 2026 price, AUM, volatility, correlation, cycle, and ETF figures need source/date labels.
- The 2024-2025 cycle should not be treated as a completed cycle if the lesson is written as of April 2026. A 23% fade does not prove the old -80% flush pattern is gone.
- Spot Bitcoin products are not standard 1940 Act ETFs. They are exchange-traded trust/commodity-style products; call the wrapper precisely.
- `SEC-registered spot ETF` and `SEC-registered custody` language needs care. Coinbase Custody is not the same thing as an SEC-registered fund custodian in the mutual-fund sense.
- The vol math assumes zero correlation between BTC and the rest of the portfolio. Since the lesson later notes BTC-stock correlations around 0.3-0.7 in risk-off periods, the sizing math should include covariance.
- The statement that most of the long-term benefit comes from rebalancing, not buy-and-hold, needs evidence. Rebalancing controls risk, but BTC's historical return level did a lot of the work.
- Kelly sizing on BTC should be heavily caveated for fat tails, non-normal returns, regime breaks, and short sample history.
- Roth placement should add the scarce-Roth-space caveat: high upside belongs in Roth only if the investor accepts the total-loss risk and loss of taxable TLH value.
- The direct self-custody discussion should mention hardware wallet operational risk, seed phrase inheritance, multisig, exchange/custodian concentration, and ETF custodian concentration.

## Tax And Wrapper Issues

- The no-wash-sale rule currently applies to direct crypto because crypto is property, not stock/security. It likely does **not** apply the same way to shares of spot BTC ETFs/trusts, because those shares are securities. This distinction must be explicit.
- The lesson should not imply that IBIT/FBTC taxable trading gets the same immediate rebuy loss-harvesting treatment as direct BTC.
- Spot BTC trusts may have grantor-trust tax details and expense-related coin sales; do not describe them as identical to ordinary equity ETFs without caveats.
- The 2025/2026 Form 1099-DA and broker reporting transition needs source/date labels.
- ETH staking language is confusing: if spot ETH products are not staking due to SEC restrictions, there is no staking income to internalize for holders.

## Structure And Formatting Issues

- The lesson follows the correct format and decimal structure.
- It would be stronger with a table comparing direct BTC, spot BTC trust/ETF, futures ETF, exchange custody, and self-directed IRA custody.
- Add a `do not buy` list: leveraged crypto products, yield platforms, unsecured exchanges, altcoin baskets, and stablecoin savings products.

## YouTube Script Critique

The script has a strong chart-first opening and a crisp headline: `1-5%, Roth, spot ETF, rebalance`.

Needed fixes:

- `Bitcoin for sixteen; fiat for fifty-five` is catchy but oversimplifies fiat-money history. Say post-Bretton-Woods fiat dollar regime if that is the intended comparison.
- The ETF wrapper section should avoid saying spot products are functionally identical to standard ETFs.
- The tax segment must separate direct coin TLH from spot-product share wash-sale treatment.
- `Move BTC from zero to three; CAGR ticks up about a percentage point; vol up thirty bps` should match the interactive's actual model or be softened.
- The cycle-top signal section is useful for trimming, but make it clear this is not a timing system.

## Chart And Interactive Feedback

`side09_btc_sizer.html` is good as a model sandbox, but it should be labeled more clearly as a synthetic model.

Issues:

- The chart is a 12-year deterministic monthly simulation, not the historical 2014-April 2026 backtest shown in the static chart.
- The model uses normal returns, which are a poor fit for BTC's fat-tailed crashes and gap risk.
- The portfolio is effectively rebalanced monthly through fixed weights, while the lesson/script recommend annual rebalancing.
- The `Max drawdown` is a synthetic-path drawdown, not a historical or expected drawdown. Label it.
- A single deterministic seed can make the CAGR/Sharpe look more precise than the assumptions deserve. Use a Monte Carlo distribution or analytical efficient-frontier display.
- Add a visible covariance-aware contribution-to-risk panel, since the whole lesson is about BTC not letting the vol tail wag the portfolio dog.
- Add presets for 2022-style high correlation, zero expected return, -80% BTC crash, and 5% BTC in Roth vs taxable TLH trade-off.

## SOUL Consistency Flags

- Strong alignment with the stores-of-value-as-belief principle.
- Good alignment with barbell sizing and the need to keep speculative right-tail assets survivable.
- The lesson should more clearly say zero allocation is valid under SOUL if the investor does not accept the belief thesis or cannot survive the drawdowns.
