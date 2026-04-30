# Week 21: Equity Valuation — DCF, Multiples, and the Fed Model

---

## Part 1: Reading Section

---

### 1. Why This Is Important

By Week 21 you can read three financial statements (Week 8), you
understand capital structure (Week 19), and you can tell accounting
earnings from real cash (Week 20). The natural next question — the
one every beginner thinks valuation answers — is: *given all that,
what is the stock actually worth?*

The honest answer is: nobody knows, and the people who claim to know
to the second decimal place are usually selling something. Valuation
is not a measurement; it is a structured argument about the future
in present-value form. You build the argument anyway, because
without it you have nothing to compare price against, and price
without a value reference is just a moving number on a screen.

Four reasons to do this work, even knowing the output is fuzzy:

1. **It anchors decisions to cash, not narrative.** A discounted
   cash-flow model forces you to write down the actual cash you
   expect the business to throw off. If you cannot defend the
   numbers, you cannot defend the position. That alone filters out
   most "story stocks" before they hit your portfolio.
2. **It surfaces the assumptions you would otherwise hide.** A
   stock at 35× earnings is implicitly forecasting 12% earnings
   growth for a decade. The market does not announce that forecast
   on a banner. A reverse DCF makes the implicit forecast explicit,
   and you can ask: *do I believe that?*
3. **It separates "valuation alpha" from regime alpha.** This is
   SOUL #1. Most apparent "value" outperformance over the long run
   is multiple compression risk in disguise — buying things that
   are statistically cheap and waiting for the multiple to mean-
   revert. That works in some regimes, fails in others (1998, 2017,
   2020). Knowing what kind of bet you are actually making is half
   the battle.
4. **It calibrates expectations.** When the S&P 500 trades at a
   Shiller CAPE of 36 — where it is in April 2026 — long-run real
   returns implied by the historical relationship are around 3% per
   year, not 7%. You can still own the index. You should just stop
   pencilling in 7% real to your retirement spreadsheet.

This week covers absolute valuation (DCF, terminal value, sensitivity,
reverse DCF), relative valuation (P/E, P/B, EV/EBITDA, P/FCF, the
Shiller CAPE), and one cross-asset signal — the Fed model — that
compares the earnings yield of stocks against the 10-year Treasury
yield. The hands-on tool at the end is a DCF lab where you move the
sliders and watch the per-share intrinsic value swing.

---

### 2. What You Need to Know

#### 2.1 The Two Schools — Absolute and Relative

Every valuation method falls into one of two camps.

**Absolute valuation** asks: what cash will this business produce
over its life, and what is that cash worth today? The canonical
tool is the discounted cash-flow (DCF) model. You forecast free
cash flow for some explicit period (usually 5–10 years), assume a
steady state after that (the "terminal value"), discount everything
back at a rate that reflects the riskiness of the cash, and divide
by share count. The output is a per-share number you can compare
against the market price.

**Relative valuation** asks: how is this company priced compared
to similar companies, or compared to its own history? The tools are
multiples — P/E, P/B, EV/EBITDA, P/FCF, dividend yield, earnings
yield. You don't need a forecast; you just need a peer group or a
historical range.

Neither school is right or wrong. They answer different questions.
DCF answers "what should I pay?" Multiples answer "what is the
market currently paying for businesses like this?" In practice you
do both and you look at where they disagree, because the
disagreement is where the interesting question lives. If your DCF
says $80 and the market is paying $200 at 40× earnings, the burden
is on you to explain either why the market sees something you don't,
or why the market is wrong. Both happen. Knowing which one you are
betting on is the discipline.

A useful warning before we start: as Horace puts it, most "valuation
alpha" is actually multiple-compression risk dressed up as insight
(SOUL #1). Buying something at 12× earnings instead of 22× *can* be
a free lunch — or it can mean you are buying a structurally
deteriorating business at the moment its multiple stops being able
to defend itself. The valuation toolkit doesn't tell you which one.
Cash-flow stability does.

#### 2.2 Discounted Cash Flow — The Mechanics

The DCF formula is one of the few places in finance where the maths
is genuinely simple. Free cash flow each year, discounted at a rate
$r$, summed:

$$ V_0 = \sum_{t=1}^{N} \frac{\text{FCF}_t}{(1+r)^t} + \frac{\text{TV}_N}{(1+r)^N} $$

Three pieces:

**Explicit-period FCF.** You forecast free cash flow for 5–10 years.
"Free cash flow" here means cash from operations minus capex —
the number from Week 20. For a growing business, you start from the
trailing FCF, apply growth rates by year (often a fade — 12% in Y1
sliding down to 4% by Y5), and write down the projection.

**Terminal value (TV).** After the explicit period, the business
keeps existing. You collapse the rest of the future into one number
at year N. Two standard methods:

- **Gordon growth (perpetuity):** $\text{TV}_N = \dfrac{\text{FCF}_{N+1}}{r - g}$,
  where $g$ is a perpetual growth rate. The $g$ has to be lower
  than long-run nominal GDP growth (4–5%) — you cannot grow faster
  than the economy forever — or the formula explodes.
- **Exit multiple:** $\text{TV}_N = \text{FCF}_{N} \times M$, where $M$ is
  some multiple drawn from peers or history (e.g. 18× FCF). Useful
  cross-check; weakness is the multiple itself is a relative-value
  number, so the "absolute" calculation imports a relative
  assumption.

**Discount rate $r$.** This is the weighted average cost of capital
(WACC) for the firm — Week 19's number. For a typical large-cap US
equity, WACC sits in the 7–10% range. For a speculative growth
name, 12–15%. The choice drives the answer more than people
realise.

The terminal value typically accounts for **60–80% of the total
DCF output** for a normal-growth company. That is uncomfortable, and
honest. Most of what you are valuing is the assumption about steady
state.

#### 2.3 Sensitivity — The WACC and g Knobs

Two numbers — the discount rate $r$ and the terminal growth $g$ —
do most of the work in any DCF. Move either by 100 bps and the
intrinsic value can swing 30%. The example below uses a $10/share
starting FCF, growing 6% for five years then 3% terminal, with
sensitivity around $r$ and $g$:

| | $g = 2\%$ | $g = 3\%$ | $g = 4\%$ |
|---|---:|---:|---:|
| **$r = 7\%$** | $238 | $300 | $440 |
| **$r = 8\%$** | $182 | $221 | $290 |
| **$r = 9\%$** | $148 | $174 | $215 |
| **$r = 10\%$** | $124 | $143 | $169 |

Two takeaways: the formula is most violent in the upper-left corner
where $r - g$ is small (the perpetuity denominator goes to zero), and
a "cheap" stock at one $(r, g)$ pair can be expensive at the
neighbouring pair. The honest output of any DCF is not a number; it
is a **range**.

This is also why analyst price targets cluster. Twenty analysts
running the same DCF will output twenty answers within ±10% of each
other — not because the model is precise, but because they all
gravitate to the same defensible $(r, g)$ region. The herd in price
targets is a herd in WACC assumptions.

The hands-on lab at §2.7 lets you turn the knobs and watch.

#### 2.4 Comparable Multiples — The Field Guide

When you don't have the patience for a DCF (or the business is too
complicated for a clean cash-flow forecast), multiples do the job.
Five matter.

**P/E (price to earnings).** Most cited, often misleading. Use
diluted EPS, not basic. Use forward P/E (next 12 months) when you
have analyst estimates you trust, trailing P/E when you don't. A
"normal" S&P 500 P/E sits around 16–17×; the long-run Shiller CAPE
mean (10-year smoothed real earnings) is also about 17. Sectors
diverge: utilities 14–18×, banks 8–12×, consumer staples 18–25×,
software 25–40×. Compare within sector, not across.

**P/B (price to book).** Market cap divided by shareholders'
equity. Useful for banks and insurers because their assets are
already mark-to-market-ish (loans, securities), so book value is
meaningful. Useless for software, brand-led consumer, biotech,
where intangibles are the asset and accounting doesn't capture them.

**EV/EBITDA.** Enterprise value (market cap + debt − cash) over
earnings before interest, tax, depreciation, amortisation. Strips
out capital-structure differences, which is why it is the standard
in M&A. Weakness: EBITDA ignores capital intensity. A company with
EBITDA of $1B and capex of $1.2B has an EV/EBITDA in line with peers
and zero free cash flow. Use EV/EBITDA *with* a separate look at
capex intensity, never alone.

**P/FCF (price to free cash flow).** The cleanest of the lot. Free
cash flow is hard to fake (Week 20). For mature businesses, P/FCF
in the 15–25× range is normal. Below 12×, you are either buying
genuine cheapness or a value trap. Above 35×, you are paying
explicitly for growth that may or may not arrive.

**Earnings yield (E/P).** The reciprocal of P/E. A stock at 20×
earnings has a 5% earnings yield. The reason this matters separately
from P/E: it puts equity earnings on the same axis as bond yields,
which is exactly what the Fed model needs (§2.6).

#### 2.5 Shiller CAPE — The Long History

Robert Shiller's cyclically-adjusted P/E (CAPE) takes the S&P 500
price and divides by the average of the last ten years of real
earnings. The smoothing kills the cyclical noise that makes the
trailing P/E spike to absurd levels in recessions (when the E
collapses) and look reasonable at the top of a cycle (when E is at
peak). The chart below plots CAPE from 1881 through April 2026.

![Shiller CAPE 1881-2026, with the long-run mean near 17 and the major peaks and troughs annotated. Peaks at 1929 (~32, just before the Crash), 1966 (~24), 2000 (~44, the dot-com top), 2021 (~38), and current 2026 reading near 36. Troughs at 1921 (~5), 1932 (~6, Depression bottom), 1949 (~10), 1981 (~8, Volcker stagflation low), 2009 (~13, financial crisis bottom). The current level sits in the most expensive 10% of US stock-market history; only 1929 and 1999-2000 were materially more expensive on this measure.](image/week21_cape_history.png)

Two patterns matter.

First, **CAPE mean-reverts on long horizons but is useless as a
short-term timing signal**. CAPE was 25 in 1996, 30 in 1997, 38 in
1998, 44 in 1999, and only peaked in March 2000. Anyone who shorted
the index at CAPE 25 lost their job before they got proven right.
The signal is real on 10-year-forward returns; it is noise on 1-year-
forward returns.

Second, **the 80-year low (1981) and the modern range diverge**.
CAPE in 1981 was around 8 because Treasury yields were 14% — the
cost of capital was crushing equity multiples. CAPE in 2009 was 13
because earnings had collapsed. CAPE in 2026 at 36 is because rates
are 4% and tech-sector earnings dominate the index. The number is
the same metric across the whole history, but the regime supporting
it is wildly different.

Use CAPE as a temperature reading, not a buy/sell signal. When
CAPE is in the top decile of history, expected real returns over
the next decade are mid-single-digits at best. That is the
calibration. It does not tell you to sell.

#### 2.6 The Fed Model — Earnings Yield vs the 10-Year

The Fed model compares the earnings yield of equities (E/P) to the
yield on 10-year Treasuries. The thesis: if E/P is much higher than
the bond yield, equities are cheap relative to bonds, because
their cash-flow yield exceeds the risk-free alternative. If E/P
is below the bond yield, the bond market is offering a better
risk-adjusted deal.

![Fed model spread 1962-2026, defined as S&P 500 cyclically-adjusted earnings yield (1/CAPE) minus 10-year Treasury yield. The line spends most of the 1970s deeply negative (bonds yielded 8-14% while CAPE earnings yield was 4-8%); flips firmly positive after the early 1980s rate peak, peaking around +6 percentage points in 2009 (low rates, depressed earnings yield was still high after the crash). Inverts to roughly -2 percentage points in 2000 (the dot-com top — bonds were a better deal than stocks). April 2026 reads close to zero — earnings yield around 2.8%, 10-year yield around 4.0%, a small negative spread suggesting bonds are the cleaner trade than stocks at the index level.](image/week21_fed_model.png)

Two warnings about the Fed model.

**It is not in any Fed publication.** The name comes from a 1997
Humphrey-Hawkins report chart. Greenspan never endorsed it as a
valuation tool. Practitioners adopted the framework anyway because
it is intuitive.

**It conflates real and nominal.** The earnings yield is a real
quantity (earnings grow with inflation in the long run). The
Treasury yield is nominal. Subtracting one from the other is a
type error. The signal works best when inflation is stable; it
breaks down precisely when inflation is the dominant variable
(the 1970s, where the Fed model said equities were cheap for a
decade while real returns on stocks were near zero).

Treat the Fed model as one cross-asset reference, not a verdict.
At the April 2026 reading near zero, both stocks and bonds price in
mediocre real returns. There is no obvious arbitrage between the
two — which is itself information.

#### 2.7 Reverse DCF — The Sanity Check

The reverse DCF flips the question. Instead of forecasting cash
flow and computing intrinsic value, you take the *current market
price* as given and ask: what growth rate, at the prevailing
discount rate, makes this price the answer?

You hold $r$, $g$, and starting FCF fixed, and solve for the
growth rate $g_e$ in the explicit period that produces $V_0 =
\text{Price}$. The output is the **growth implied by the price**.

Example: AAPL at $215 with 14.5B shares is a $3.1T market cap.
Trailing FCF is about $109B. If WACC is 9% and terminal growth is
3%, the explicit-period growth implied by the current price is
roughly 5–6% per year over the next decade. Apple has grown FCF
about 9% annualised over the last decade. The implied 5–6% is
reasonable: it bakes in some maturation but not collapse. The price
passes a basic sanity check.

For a richer comparison, run the reverse DCF on a meme stock at a
$50B market cap with no FCF: the implied growth is "infinite from
today's free cash flow." That is the moment you put the model down
and admit you are not valuing this thing on cash.

The reverse DCF is the discipline that separates "buying because
it's cheap on the model" from "buying because the model says
miracles are required." The interactive lab in §2.7 includes a
reverse-DCF readout for each preset stock — try it.

The hands-on tool: see [interactive/week21_dcf_lab.html](interactive/week21_dcf_lab.html).
Move the WACC, growth, and terminal-growth sliders, and watch the
per-share intrinsic value swing for AAPL, MSFT, GOOGL, JPM, and KO.

---

### 3. Common Misconceptions

1. **"DCF gives you a precise number." It doesn't.** It gives you a
   range. The number is precise; the inputs are not. Treat any DCF
   output as ±25% at best.
2. **"A low P/E means a stock is cheap." Not by itself.** Banks,
   tobacco, and oil majors trade at low P/Es structurally because
   of regulatory, terminal, or commodity-price risk. The market
   isn't being stupid; it is pricing in a real future hazard.
3. **"Terminal value is a small piece — most of the value is in
   the explicit forecast." Wrong direction.** TV is typically 60-
   80% of total DCF for a steady-state business. The explicit
   period mostly bridges you to the assumption you actually care
   about: the steady state.
4. **"The Fed model says when to be in stocks vs bonds." It
   doesn't.** It is a rough cross-asset thermometer that ignores
   inflation regime entirely. It told you stocks were cheap in 1972
   and you lost money in real terms for a decade.
5. **"Shiller CAPE is broken because it has been high since 2014
   and stocks went up." It's not broken — the signal is on 10-year
   forward returns, not next-year.** From CAPE 26 in 2014, the
   subsequent decade gave roughly 9% nominal CAGR — well below the
   long-run 10% but consistent with the elevated CAPE.
6. **"P/B is always meaningful." For asset-light businesses (tech,
   consumer brands, services), book value omits 80% of what makes
   the company valuable.** Use it for banks; ignore it elsewhere.
7. **"EV/EBITDA is a 'cleaner' P/E because it strips out capital
   structure." Yes, and it also strips out capex, which is the
   line that separates a real business from a treadmill.** A cement
   producer at EV/EBITDA 8 may be more capital-hungry than a
   software company at EV/EBITDA 25.
8. **"You should buy whatever has the lowest P/E in a sector."
   That's a deep-value heuristic, and it fails the moment one of
   the names is structurally impaired.** Cheap relative to peers
   is meaningful only when the underlying business is comparable.
9. **"Higher discount rate = always more conservative." Almost.**
   A higher $r$ lowers the present value of all future cash, but
   it also lowers TV — which is most of the answer. The
   conservatism is real; the magnitude is usually larger than
   people expect.
10. **"Growth stocks should be valued differently because DCF
    doesn't work for them." DCF works fine; the inputs are just
    harder.** What people mean is "I don't trust my own forecast,"
    which is honest. The fix is wider sensitivity bands, not a
    different method.

---

### 4. Q&A Section

**Q1. What discount rate should I use for a typical S&P 500 stock?**
WACC is the right answer; for most large-cap US firms it lands in
the 7–9% band. If you don't want to compute WACC from scratch,
8% is a defensible default. For high-leverage or commodity-cycle
names, push toward 10%; for defensive utilities, 6–7%.

**Q2. How many years should the explicit DCF period cover?**
Five to ten. Five if the business is mature and stable (KO, JNJ).
Ten if the business is in a clear high-growth phase that should
fade to maturity (NVDA, GOOGL). Going past ten is forecasting
performance art; you are pretending to know about regime that
doesn't exist yet.

**Q3. Why does the Gordon growth formula go crazy when $r$ is
close to $g$?**
Because $\dfrac{\text{FCF}}{r - g}$ has a denominator that goes to
zero. Mathematically: a perpetual cash flow growing at rate $g$
discounted at rate $r$ has finite present value only if $g < r$.
If $g \geq r$, the present value is infinite — the cash flows
grow faster than the discount eats them. This is why $g$ in
practice has to be capped at long-run nominal GDP (~4-5%); above
that, you are claiming the firm grows forever faster than the
economy it lives in, which is impossible.

**Q4. What's the difference between P/E and Shiller CAPE in
practice?**
Trailing P/E uses the last twelve months of earnings. CAPE uses
the average of the last ten years of *real* earnings (inflation-
adjusted). The smoothing matters enormously at cycle turning
points: in 2009, trailing P/E spiked above 100 because earnings
collapsed faster than price; CAPE was around 13. CAPE is the more
honest measure across cycles. P/E is the more responsive measure
within a cycle.

**Q5. Should I use forward P/E or trailing P/E?**
Forward, when the analyst estimates are credible (large-cap, well-
covered, low cyclicality). Trailing, when the business is volatile
or estimates have a wide spread. The gap between trailing and
forward P/E tells you the implied growth rate: if trailing is 18×
and forward is 15×, the market is pricing in 20% earnings growth.

**Q6. Is the Fed model a buy/sell signal in 2026?**
No — but it is informative. April 2026 reading is near zero (E/P
~2.8%, 10y ~4.0%). That means cash earnings yield on the index is
*below* the risk-free rate. Historically, that condition has
preceded sub-par 5–10 year equity returns. It does not mean sell;
it means lower your forward expectations and consider tilting a
modest weight toward bonds (consistent with the four-tranche
framework from Week 14, SOUL #13).

**Q7. Why is reverse DCF more useful than regular DCF for big
benchmark stocks?**
Because everyone has already done the regular DCF and the answer is
"price ≈ intrinsic value, give or take 10%." That is not actionable.
Reverse DCF tells you the *implied growth rate* the market has
priced in. Now you can ask whether that growth rate is reasonable
versus history, versus competitors, versus what you think
management can deliver. You're betting on a difference of opinion
about growth, not on an absolute valuation gap.

**Q8. Banks don't fit the DCF mould. What do I use?**
Residual income or P/B-vs-ROE. A bank trading at $1.5\times$ book
when it earns 15% ROE is fairly priced (because $\text{P/B} \approx
\text{ROE} \times \text{P/E}$, and a 10× P/E with 15% ROE pencils to 1.5× P/B).
The cleanest one-number summary for a bank is **ROTCE** — return
on tangible common equity. JPM at 22% ROTCE in FY2024 is structurally
the highest-quality bank in the index, which is why it trades at a
premium to peers.

**Q9. Multiples vary so much across sectors. How do I compare a
software company at 30× to a utility at 15×?**
You don't compare them directly. You compare each within its
sector, and you compare the cross-sector premium ratio across
time. If software-vs-utility usually trades at 1.7× the multiple
and currently trades at 2.5×, you have learned something. The
cross-sector level itself is not the signal; the change in the
ratio is.

**Q10. How does Horace's "alpha is rare" principle apply to
valuation?**
Tightly. Most "valuation alpha" is regime-specific multiple
compression and expansion that flips to the loser of the previous
cycle. The 2000-2010 decade rewarded value because tech multiples
collapsed; 2010-2020 rewarded growth because rates compressed and
tech earnings exploded. Both decades had their crowd of
"valuation experts" who looked smart for a while and then looked
foolish. Genuine, repeatable valuation alpha comes from one
narrow place: businesses that compound faster than the market
discounts, *and* whose multiples don't blow out at the entry. Find
those rarely; the rest is multiple-compression risk in a suit.

**Q11. What should the DCF lab teach me beyond the slider game?**
That the answer depends almost entirely on three numbers — WACC,
terminal growth, and the year-1 starting FCF — and that the same
business can be priced "cheap" or "expensive" by 50% with rounding-
error changes to those inputs. The lesson is humility, not
precision.

**Q12. Is there a case to ignore valuation entirely and just
index?**
Yes — most of the time, for most people. Per SOUL #16, US-listed
equities are the investable universe; per Week 2, the index is the
default. Valuation discipline matters when you are choosing
individual names or deciding whether to tilt the index allocation
up or down at extremes. At CAPE 36, you don't have to sell — but
you do have to lower the return you write into your retirement
plan. That single discipline is worth more than most stock-picking.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Equity Valuation 101 — DCF, Multiples, and the Fed Model | Week 21

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Stella:** Welcome back. This is Week 21, equity valuation. By
this point you've read three financial statements (Week 8), you
know capital structure and WACC (Week 19), and you can tell real
cash from accounting earnings (Week 20). The question we're
finally answering: *what is the stock worth?*

**Horace:** Quick disclaimer first. The honest answer to "what is
this stock worth" is "I don't know, and neither does the analyst
on TV with the price target to two decimal places." Valuation is
a structured argument about the future, expressed in present-value
form. The argument has assumptions. Those assumptions are wrong.
The point of the exercise is to make them visible so you know
what you're betting on — not to produce a number you trust.

**Stella:** Today we cover three things. The DCF — the absolute
valuation method. Multiples — P/E, P/B, EV/EBITDA, P/FCF. And
two long-history overlays: the Shiller CAPE and the Fed model.
The hands-on lab at the end is a DCF you can drive with sliders.

---

**[ACT 1 — DCF MECHANICS — 1:30]**

**Horace:** Discounted cash flow. The maths is the simplest in
finance. Free cash flow each year, discounted at a rate, summed.
Plus a terminal value to capture everything past the explicit
forecast period.

**Stella:** Three inputs. The free cash flow forecast — usually
five to ten years of it. The terminal value — what the business is
worth after the explicit period. And the discount rate — the
WACC from Week 19, which for a typical large-cap US stock is
seven to nine percent.

**Horace:** Terminal value is the part nobody wants to talk
about. Two methods. Gordon growth: take the year-N free cash flow,
multiply by one plus a perpetual growth rate, divide by WACC minus
that growth rate. Or the exit multiple: take year-N free cash
flow times some multiple, like 18 times. Both are guesses dressed
up as formulas.

**Stella:** And the uncomfortable part: terminal value is usually
60 to 80 percent of the total DCF answer. So when somebody says
"I have a DCF model that says this stock is worth $200" — what
they really mean is "I have a guess about the steady state worth
$140, plus a five-year forecast worth $60."

**Horace:** Doesn't mean DCF is useless. It means the discipline
is in the inputs, not the output.

---

**[ACT 2 — SENSITIVITY — 4:30]**

**Stella:** Sensitivity. The two knobs that swing everything are
WACC and the terminal growth rate. Move either by a hundred basis
points and the answer can change 30 percent.

**Horace:** [VISUAL: the §2.3 table on screen.] Same business, same
starting FCF, same five-year growth assumption. Top-left corner,
WACC 7%, terminal growth 4%, intrinsic value $440 a share. Bottom-
right, WACC 10%, terminal growth 2%, intrinsic value $124. The
*business* didn't change; the assumption did.

**Stella:** Which is why analyst price targets cluster. Twenty
analysts running the same DCF will produce twenty answers within
plus or minus 10 percent of each other — not because the model is
precise, but because they all gravitate to the same defensible
WACC and growth pair. The herd in price targets is a herd in
assumptions.

**Horace:** You'll see this live in the lab. We'll get to it.

---

**[ACT 3 — MULTIPLES FIELD GUIDE — 6:30]**

**Stella:** Multiples. The shortcut version of valuation. Five
matter.

**Horace:** P/E. Most cited, most misleading. Use diluted EPS, not
basic. Forward when you trust the analyst estimates, trailing when
you don't. Long-run S&P 500 P/E is about 16 to 17. Sector matters:
utilities 14 to 18, banks 8 to 12, consumer staples 18 to 25,
software 25 to 40.

**Stella:** P/B — price to book. Useful for banks and insurers
where assets are mark-to-market-ish. Useless for software, brand
companies, biotech — where the asset is the brand or the IP and
accounting can't measure it.

**Horace:** EV/EBITDA. Strips out capital structure, which is why
it's the M&A standard. The trap: it also strips out capex. A
cement producer at EV/EBITDA 8 may be more capital-hungry than a
software company at EV/EBITDA 25. Always look at capex intensity
alongside.

**Stella:** P/FCF — price to free cash flow. The cleanest one.
Free cash flow is hard to fake — Week 20 covered why. For mature
businesses, 15 to 25 times is normal. Below 12, either genuinely
cheap or a value trap. Above 35, you're paying for growth that may
or may not arrive.

**Horace:** And earnings yield — the reciprocal of P/E. Stock at
20 times earnings is a 5% earnings yield. Sounds trivial but it
matters because it puts equities on the same axis as bonds. Which
is exactly what we'll need next.

---

**[ACT 4 — SHILLER CAPE — 9:30]**

**Stella:** Shiller CAPE. Robert Shiller, Yale, Nobel 2013. Take
the S&P 500 price, divide by the *ten-year average of real earnings*.
The ten-year smoothing kills the cyclical noise that makes
trailing P/E spike to 100 in recessions and look fine at the cycle
top.

**Horace:** [VISUAL: image/week21_cape_history.png.] CAPE from
1881 to today. The horizontal mean line is at 17. Look at the
peaks: 1929, just before the Crash, 32. 1966, end of the post-war
boom, 24. 2000, dot-com top, 44 — the highest in the entire
series. 2021, post-pandemic stimulus euphoria, 38. Today, April
2026, 36. You're sitting in the most expensive 10 percent of US
stock-market history. Only 1929 and 1999-2000 were materially
higher.

**Stella:** Two patterns to learn. First, CAPE mean-reverts on
long horizons but is useless as short-term timing. CAPE was 25
in 1996, 30 in 1997, 38 in 1998, 44 in 1999. Anyone who shorted
the index at CAPE 25 lost their job before the call worked.

**Horace:** Second pattern: low CAPE doesn't mean the same thing
across regimes. CAPE 8 in 1981 was because Treasury yields were
14 percent — the cost of capital was crushing equity multiples.
CAPE 13 in 2009 was because earnings collapsed. CAPE 36 today is
because rates are 4 percent and tech-sector earnings dominate the
index. Same number, different regime.

**Stella:** Practical use: temperature reading, not a buy/sell
signal. When CAPE is in the top decile, expected real returns
over the next decade are mid-single-digits at best. That's the
calibration you put in your retirement spreadsheet. You don't have
to sell.

---

**[ACT 5 — THE FED MODEL — 12:30]**

**Horace:** The Fed model. Compares the earnings yield of stocks
to the 10-year Treasury yield. Idea: if E/P is much higher than
the bond yield, equities are paying you more than risk-free and
they're cheap. If E/P is below the bond yield, bonds are the
better deal.

**Stella:** [VISUAL: image/week21_fed_model.png.] Spread chart,
1962 to today. Most of the 1970s, deeply negative — bonds
yielded 8 to 14 percent while CAPE earnings yield was 4 to 8
percent. That said "bonds are the cleaner trade." It was right —
real returns on stocks were near zero for the entire decade.

**Horace:** Then the early 80s rate peak, the line flips firmly
positive. Volcker breaks inflation, Treasury yields collapse from
14 to 4 percent over twenty years, and equity earnings yields stay
in the 4 to 8 range. The spread peaks around 6 percentage points
in 2009 — earnings yields elevated post-crash, rates floored.

**Stella:** Then 2000 — the inversion. CAPE peaked at 44, earnings
yield dropped to 2.3%, the 10-year was at 6%. Negative spread of
nearly 4 points. The Fed model said bonds were the cleaner trade.
And the next decade proved it: stocks went sideways for a decade,
bonds outperformed.

**Horace:** April 2026 reading: close to zero. Earnings yield
about 2.8%, 10-year about 4%. Spread about negative 1 point. Not
the 2000 disaster signal but not the 2009 fat-pitch signal either.
A reasonable read: don't expect heroics from either asset over the
next five to ten years.

**Stella:** Two warnings about the Fed model. It's not in any Fed
publication — the name comes from a 1997 chart in a Greenspan
report. And it conflates real and nominal — earnings yield is
real, Treasury yield is nominal. It works best when inflation is
stable; it breaks precisely when inflation is the dominant
variable, like the 1970s. So treat it as one cross-asset reference,
not a verdict.

---

**[ACT 6 — REVERSE DCF & THE LAB — 15:30]**

**Stella:** Reverse DCF. Flip the question. Instead of forecasting
cash flow and computing intrinsic value, take the *current market
price* as given and ask: what growth rate, at the prevailing
discount rate, makes this price the answer? The output is the
**growth implied by the price**.

**Horace:** Quick example. Apple, April 2026, around $215 a share,
14.5 billion shares, $3.1 trillion market cap. Trailing FCF $109B.
At WACC 9% and terminal growth 3%, the explicit-period growth
implied by the price is about 5 to 6 percent a year over the next
decade. Apple has grown FCF about 9 percent annualised over the
last decade. The implied 5–6 is reasonable. The price passes a
basic sanity check.

**Stella:** Now run the same exercise on a $50 billion market-cap
meme stock with no FCF. The implied growth is "infinite from
today's free cash flow." That's the moment you put the model down
and admit you're not valuing the thing on cash.

**Horace:** [VISUAL: interactive/week21_dcf_lab.html.] The lab.
Five preset stocks — AAPL, MSFT, GOOGL, JPM, KO. Each preset has
a starting FCF per share, a current price, and shares outstanding.
You move the WACC, growth, and terminal-growth sliders, and watch
the per-share intrinsic value swing. Bar chart compares intrinsic
to current price for all five names at the current slider settings.

**Stella:** Try this: drop WACC from 9 to 7 — every name goes to
"undervalued by 30 percent." Push WACC to 11, every name flips
"overvalued by 25 percent." That's the exercise. Same business,
same FCF, same growth — different answer because of one
assumption. You'll feel it in your hands within thirty seconds of
playing.

---

**[OUTRO — 17:30]**

**Horace:** SOUL #1 — alpha is rare. Most "valuation alpha" is
multiple-compression risk dressed as insight. The 2000-2010 decade
rewarded value because tech multiples collapsed; 2010-2020 rewarded
growth because rates compressed and tech earnings exploded. Both
crowds had their celebrities. Both got humbled at the regime turn.

**Stella:** Repeatable valuation alpha lives in one narrow place:
businesses that compound faster than the market discounts, and
whose multiples don't blow out at the entry. Find those rarely.
The rest is regime-betting, and regime is unpredictable.

**Horace:** Practical takeaway for April 2026. CAPE 36 — top
decile of history. Fed-model spread near zero. You don't have to
sell the index — per Week 14, the four-tranche allocation
already builds in the bond hedge. But you do have to lower the
real return you pencil into your retirement plan. From the
historical 7% real to the implied 3 to 4 percent real over the
next decade. That single recalibration is worth more than most
stock-picking attempts.

**Stella:** Next week: macroeconomic indicators — GDP, inflation,
employment, the Fed's reaction function, and how to read economic
releases without becoming a CNBC viewer. See you then.

---
