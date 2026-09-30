## Part 2: YouTube Script

---

**VIDEO TITLE:** Investment Grade vs Junk — Reading the Credit Curve | Week 33
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

### INTRO (0:00 - 1:40)

[VISUAL: title card "Week 33 — Credit Analysis"]

**HORACE:** Welcome back. Stella, last week we broke down corporate
finance — capital structure, WACC, why a CFO chooses debt over equity.
This week is the other side of that handshake. The lender's side.

**STELLA:** Right. If a CFO issues a bond at Treasury plus three hundred
basis points, *somebody* has to buy it. What is that buyer actually paying
for? That's the whole topic this week.

**HORACE:** Three things. The rating ladder — AAA down to CCC. The default
rates that come with each rung. And the spread — the compensation you
receive for sitting on top of those default rates.

**STELLA:** And then the tape. We'll look at the high-yield spread since
1997. Four panics, and exactly what each one paid you to step in.

[VISUAL: image/week33_default_rates.png — fade in]

---

### SEGMENT 1 — THE LADDER (1:40 - 4:30)

**HORACE:** Let me start with the cliff. Investment grade ends at BBB
minus. Below that — BB plus and lower — is high yield, junk, speculative
grade, whatever you want to call it. Same bond.

**STELLA:** And the cliff is institutional. Pension funds, most insurance
mandates, lots of mutual funds — they can only hold IG. So when a bond
crosses the line down, half its holder base has to sell.

**HORACE:** That's right. It's not credit fundamentals creating the cliff,
it's holder mandates. But the price effect is real — a downgrade across
that line can blow a bond's spread out by a hundred to three hundred basis
points in a session. Fallen angels are a structural alpha source for that
exact reason — the IG universe is forced to sell, the HY universe is
calmly absorbing.

[VISUAL: image/week33_default_rates.png — full screen]

**STELLA:** Look at the chart. AAA, basically zero. AA, two basis points.
A, seven. BBB, eighteen. Then we cross the line — BB jumps to one hundred
sixteen. B, four hundred ten. CCC, two thousand three hundred thirty.

**HORACE:** Each notch isn't adding risk, it's multiplying it. CCC is not
"a bit worse than B." It's six times worse. And those are long-run
averages. In 2008-2009 CCC defaults hit forty-five percent in a single
year.

---

### SEGMENT 2 — RECOVERY AND EXPECTED LOSS (4:30 - 7:30)

**STELLA:** Default isn't zero, though. Where do bondholders end up after
Chapter 11?

**HORACE:** Senior unsecured — the big bucket of corporate debt — recovers
about forty cents on the dollar on average. Secured debt recovers
sixty-five to seventy. Subordinated, twenty-five. Equity, zero.

**STELLA:** So the math an analyst actually does is — probability of
default times one minus recovery — which gives expected loss per year.

**HORACE:** Right. Single B bond. Default probability four-point-one
percent. Recovery forty percent. Loss given default is sixty percent.
Multiply: two-point-five percent expected loss per year.

**STELLA:** And the bond yields, what — Treasury plus four-twenty-five?

**HORACE:** Roughly. So your *expected* excess return after the credit
loss tax is one-eighty basis points. Not four-twenty-five. The other
two-fifty is paying for losses you actually expect to take in a rolling
sample. The one-eighty is the actual reward for bearing the distribution.
That distinction is everything.

---

### SEGMENT 3 — DECOMPOSING THE SPREAD (7:30 - 10:00)

**STELLA:** So when I look at a corporate bond at "two hundred basis points
over treasuries," what fraction is actually compensation?

**HORACE:** Three pieces. Expected loss — that's the credit math.
Liquidity premium — you can't sell this in five seconds like a Treasury.
And risk premium — you have to live through the path, which includes 2008
prints.

**STELLA:** So a BBB at one-thirty over —

**HORACE:** Expected loss is maybe twenty-five basis points. The other
hundred and five is liquidity plus risk premium. Mostly risk premium —
holding through stress with no forced selling.

**STELLA:** And a single B at four-twenty-five?

**HORACE:** About two-fifty expected loss, one-seventy-five premium. HY's
premium is smaller as a fraction. You're being paid more in absolute terms
but less in relative terms.

**STELLA:** Until panic.

**HORACE:** Until panic. Then everything inverts.

---

### SEGMENT 4 — THE TAPE (10:00 - 13:30)

[VISUAL: image/week33_hy_spread_history.png]

**HORACE:** This is the ICE BofA US High Yield index option-adjusted
spread, FRED ticker BAMLH0A0HYM2. Daily, since 1997. It's the credit
market's vol index.

**STELLA:** Long-run average around five-twenty. Below three-fifty is
"reach for yield." Above one thousand is real panic.

**HORACE:** Four panics on this chart. 2002 — telecom and accounting
fraud, WorldCom, Enron. Spread to one thousand. 2008 — Lehman, money
market freeze, no bid. Spread to twenty-one-eighty in November. The
all-time wide. 2020 — COVID. Spread to eleven hundred in mid-March,
round-tripped in ninety days when the Fed said they'd buy ETFs. 2022 Q4 —
fastest Fed hiking cycle in forty years, six hundred wide.

**STELLA:** Each one of those was a buying opportunity.

**HORACE:** Every single one. Behavioural alpha at work. And the
volatility tail wags the dog — when credit is screaming, equities are
about to follow. The 2008 spread peak was November 2008. Equities
bottomed March 2009. Credit led by four months.

**STELLA:** And April 2026?

**HORACE:** Right around five hundred. Boring. Fairly priced. Neither
buy-with-both-hands nor reach-for-yield. Wait.

---

### SEGMENT 5 — THE INTERACTIVE (13:30 - 16:30)

[VISUAL: interactive/week33_credit_pricer.html]

**STELLA:** Open the credit pricer. Six sliders — maturity, coupon,
Treasury yield, credit spread in basis points, default probability, and
recovery rate.

**HORACE:** Let's load the 2008 panic preset. Ten-year. Six percent coupon.
Four percent Treasury. Eighteen-hundred-bps spread. Six percent default
probability. Forty percent recovery.

**STELLA:** Implied price — about sixty-eight cents on the dollar.
Credit-adjusted YTM — twelve percent. Expected return after default losses
— still about nine percent per year.

**HORACE:** Nine percent per year for ten years, on a portfolio that's
down thirty cents on entry. That's what panic prints. The *forward*
expected return is enormous. But you have to be holding already, or
willing to step in when nobody else will.

**STELLA:** Now slide spread back to four hundred. Default probability
back to two percent. Recovery up to forty-five.

**HORACE:** Implied price about ninety-seven. Credit-adjusted YTM six
point six percent. Expected return after losses about five point four.
Boring. April 2026. Run the barbell — don't stretch for fifty basis points
in junk when the curve isn't paying you.

**STELLA:** And the breakeven default rate?

**HORACE:** That's the killer feature. It tells you what default rate
you'd need for the bond to *just* break even versus Treasuries. If
breakeven is double the historical rate, you're being well paid. If it's
at the historical rate, you're getting fair odds. If it's below, you're
paying for credit risk and not being compensated. Use that one metric as
your filter.

---

### OUTRO (16:30 - 18:00)

**STELLA:** Recap. Rating ladder, AAA to CCC. Default rates non-linear,
zero at the top, twenty-three percent at the bottom. Recovery forty
percent for senior unsecured. Spread equals expected loss plus liquidity
plus risk premium. And the high-yield tape since 1997 is the cleanest
behavioural-alpha tape in the bond market.

**HORACE:** Three takeaways. One, never buy HY under four hundred bps.
That's complacency. Two, always buy HY over eight hundred bps with size —
every panic since 1997 has been a two-year trade. Three, use ETFs, not
single names. Alpha is rare; single-name credit alpha is the rarest form,
dealers eat retail in that game. Use HYG, JNK, LQD. The ETF wrapper is
your edge.

**STELLA:** Next week we move from credit risk to liquidity risk. Same
family of questions, different lens.

**HORACE:** See you next week.

[VISUAL: end card with week 33 / 34 thumbnails]
