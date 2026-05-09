# Code Review

_Generated: 2026-05-09 07:31 UTC — 15 comment(s)_

---

## course/week03_risk_and_return.md

### `@course/week03_risk_and_return.md:L1`
> **Highlighted text:**
> Week 3: Risk and Return — The Two Forces, Honestly Measured
>
> please add howard marks's idea on risk.  i like how he explain risk and add his risk distribution diagram and the idea of no blowing up too.

### `@course/week03_risk_and_return.md:L88-90`
> **Highlighted text:**
> About 68% of years would fall in $[\mu - \sigma,\ \mu + \sigma]$.
> About 95% of years would fall in $[\mu - 2\sigma,\ \mu + 2\sigma]$.
> About 99.7% of years would fall in $[\mu - 3\sigma,\ \mu + 3\sigma]$.
>
> check the math equation in markdown, make sure it use github inline equation format

### `@course/week03_risk_and_return.md:L92-97`
> **Highlighted text:**
> Run that on the actual S&P 500 dataset since 1928 and what you get is this:
>
>
>
> Three things to read off this chart:
>
> change the right tail bar to green

### `@course/week03_risk_and_return.md:L129`
> **Highlighted text:**
>  Equity Risk Premium — The Compensation for Bearing Risk
>
> is there also a term talking about the flip side of it, using equity as baseline, say bond is lagging due to it is risk free - a certainty to lose purchasing power

### `@course/week03_risk_and_return.md:L136-141`
> **Highlighted text:**
> Long-run, post-1928, that number has been roughly 5–7% per year. At a long-run T-bill mean of ~3.4% and a long-run S&P 500 mean of ~11%, the gap is around 7–8 points of nominal return — a gap that compounded over a century turns $1 of T-bills into ~$23 and $1 of stocks into ~$11,000 (in nominal dollars; the real numbers are smaller but the ratio is essentially preserved).
>
> talk about long run stock return % is not useful.  after 1971 the fiat currency and after 2008 the zero interest rate and QE era.   the performance of stock in the money printing era is higher, cite some real numbers.

### `@course/week03_risk_and_return.md:L145-155`
> **Highlighted text:**
> Without it, the asset can't clear. If stocks and T-bills offered the same expected return, no rational investor would hold stocks; everyone would sell into bonds, prices on stocks would fall, and forward returns would rise — until the gap re-opens. Risk premium is not a moral payment for "being brave"; it is the mechanical equilibrium price of clearing the volatile asset.
>
> it is just illogical for stock and t-bills to have the same expected return.  fundamentally they are different thing.  need to mention bond price can be very volatile too.  bond is not any safer than blue chip stock in term of total capital gain.  money lock up in bond wait to maturity is lost opportunity cost too. 

### `@course/week03_risk_and_return.md:L159-170`
> **Highlighted text:**
> The premium is an average over very long horizons. In any single year, stocks routinely under-perform T-bills. The ERP is the compensation for sticking with stocks through the years where T-bills win.
>
> is it true?  stock wins t-bills most of the years, except when in the year that the market crash

### `@course/week03_risk_and_return.md:L178-189`
> **Highlighted text:**
> Systematic (market) risk. Affects the whole economy or whole market: recession, rate moves, inflation, war, pandemic. You cannot diversify this away. Even a perfectly diversified equity portfolio loses 35–55% in a 1929, a 1973–74, a 2008, or a 2020. Systematic risk is what the market pays you to bear via the equity risk premium.
>
> you can diversity away, you just need to hold other asset other than equity.  then you can also hedge the down site, put a lead to later lessons (fill in the exact week)

### `@course/week03_risk_and_return.md:L191-197`
> **Highlighted text:**
> The "free lunch" insight that won Markowitz the Nobel Prize: since unsystematic risk can be eliminated for free through diversification, the market does not pay you to bear it. Holding a concentrated five-stock portfolio gives you much higher total risk than holding the S&P 500, but the expected return is essentially the same as the index (~10% nominal in long-run averages, by definition). The extra volatility is uncompensated. You are taking risk for free.
>
> unsystematic risk is also both side, profit and lose.  holding 5 random stock is not better than holding 500, but I remember I read a research somewhere saying holding 20 is as good as holding 50 (you find the reference)    add MPT and efficient frontier (do we teach it in later weeks?)

### `@course/week03_risk_and_return.md:L310-315`
> **Highlighted text:**
> The practical implication: horizon expands what risk you can afford to bear. A 25-year-old with a stable income and a 40-year investment horizon can run a much higher equity weight than a 65-year-old with a portfolio that has to fund the next 25 years of groceries. The 25-year-old has time to wait out a 50% drawdown; the 65-year-old does not.
>
> add a cautionary tale of Japan stock market, the lost 30 years.  or China stock market, still haven't recovery.  Not every stock market always go up.  Add a reminder the stock market has to have some relationship with the real economy long term.  look at historical data only totally missed the point

### `@course/week03_risk_and_return.md:L373-377`
> **Highlighted text:**
> The single most useful question to ask yourself before sizing a position: "If this position dropped 50% next month, would I be a forced seller?" If the honest answer is yes, the position is too large. Cut it until the answer is no, regardless of what your "tolerance" tells you.
>
> what a dumb question.  if I know this position is going to drop 50% next month, I will short it and double my profit.  many textbook say you can't time the market, but the market is actually like a slow train wreck.  the 08 GFC, you can escape if you cash when Bear Stein blow up. the covid crash has almost 2 months the new virus is killing people left and right before the world is shut down.  the recent Trump iran war crash has a few weeks of aircraft carrier moving to middle east.   day to day, the market is random walk.  but decades long macro trend is something you can't miss if you pay attention.

### `@course/week03_risk_and_return.md:L388-395`
> **Highlighted text:**
> Higher risk means higher expected return for the asset class as a whole, on long horizons. It does not mean higher return for any individual position. A single biotech stock is extremely risky and may return nothing if its trial fails. The risk premium applies to diversified bearers of systematic risk; concentrated positions in single names accept enormous idiosyncratic risk that the market does not pay you to bear. Risk and expected return scale together at the asset-class level, not at the single-position level.
>
> you actually want to look for low risk high return, asymmetic trade. 

### `@course/week03_risk_and_return.md:L474-479`
> **Highlighted text:**
> A: To eliminate the unsystematic risk you are not paid to bear. Holding 500 names instead of 5 reduces idiosyncratic risk to nearly zero, leaving the systematic risk that the equity premium is compensation for. The five-stock portfolio has more total risk but the same expected return as the index — the extra risk is the free lunch you are eating in reverse.
>
> 5 stock portfolio never has the same return as the index in reality.  where this example comes from?

### `@course/week03_risk_and_return.md:L484-492`
> **Highlighted text:**
> A: In principle yes — bitcoin's expected return must be high enough to clear at its volatility. In practice, bitcoin's expected return is not knowable from price history alone because the asset is too young and its monetary regime is still being negotiated. Standard risk-premium math uses 100 years of data to triangulate the equity premium; for bitcoin you have 15 years, of which the first 8 were near-zero adoption and the last 7 are the entire price history. Apply the framework, but don't pretend the standard error on the estimate is small.
>
> but equity from 100 years ago or even 50 years ago is very different from equity today.  the market dynamic, monterary policy, tax laws are totally different.  why people keep using 100 years old data?

### `@course/week03_risk_and_return.md:L539-545`
> **Highlighted text:**
> A: For a buyer who is dollar-cost averaging in over years, mild volatility is mildly good (you buy at a discount during dips). For a holder who is sitting on accumulated wealth, volatility is mostly the cost of doing business — not "bad" in expectation, but the emotional load you carry. For a seller in decumulation, volatility is genuinely costly because of sequence-of-returns risk. The same number means different things at different life stages.
>
> with option, volatility is an asset class itself.  cite later week lessons (you figure out the exact week)

---
