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

**Horace:** Alpha is rare. Most "valuation alpha" is
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
