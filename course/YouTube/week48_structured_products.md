## Part 2: YouTube Script

---

**VIDEO TITLE:** Structured products decoded — buffer ETFs, principal-protected notes, and replicating them DIY at 1/10 the cost
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00 to 1:30]**

**Stella:** Welcome back. This week's lesson is the one I get the
most questions about from family members. "My advisor just put me
into a buffer ETF — it caps my upside at 18% but protects me from
the first 15% of a drawdown. Should I be excited?" Horace, what
is the right answer there?

**Horace:** The right answer is: that product is three options
and a Treasury bill, and you are paying the fund company 80 basis
points a year to wrap them for you. Before you decide whether
that fee is worth it, you should know what is inside the wrapper.

**Stella:** And you have an opinion about whether it is worth it.

**Horace:** I have an opinion. The opinion is that for anybody
who finished Weeks 25 through 30 of this course, the wrapper is
roughly ten times more expensive than the DIY version. Alpha is
rare, and an arithmetic identity priced at 80 basis
points a year is not alpha — it is a convenience tax on retail.

**Stella:** Let's tear it apart.

---

**[SECTION 1 — What is inside a buffer ETF — 1:30 to 4:30]**

**Stella:** Start with the structure. What does a buffer ETF
actually own on inception day?

**Horace:** Three positions on the index.

[VISUAL: image/week48_buffer_payoff.png]

**Horace:** First, a 1-year zero-coupon Treasury, which gives you
your principal back at maturity. Second, a 1-year bull-call-spread
on the index — long an at-the-money call, short an 18%-OTM call.
That is your participation: you get the index return one-for-one,
capped at 18%. Third, a short 1-year put 15% out of the money. The
premium you collect on that short put is what finances the call
spread.

**Stella:** So the buffer is created by the short put.

**Horace:** Exactly. If the index is down less than 15% at expiry,
the put expires worthless and you keep the premium — that is what
"buffers" the first 15% of loss. If the index is down more than
15%, the put is in-the-money and you take the loss past the
buffer, one-for-one. There is no magic. It is a four-leg option
position.

**Stella:** And the cap?

**Horace:** The cap exists because the short put premium is
finite. That premium pays for some of the call spread, but not all
of it. The upper strike of the spread sits where the math balances
— and that is the cap. Higher implied vol means a higher cap;
lower IV means a lower cap. The level it locks in at issuance is
what you own.

**Stella:** So the chart on screen — 15% buffer, 18% cap, on SPY
at $500 — that flat zone from -15% to 0% is the buffer, then the
diagonal upside to +18%, then the flat cap.

**Horace:** Right. And below -15% the line slopes back down at a
1-to-1 rate. There is no protection past the buffer. A 2008-style
-37% year on a 15-buffer product loses you 22%.

---

**[SECTION 2 — DIY replication on SPX options — 4:30 to 8:00]**

**Stella:** Now the DIY version. With SPY at $500, how do I
replicate the same structure?

**Horace:** Per $50,000 of notional, you trade four legs on
1-year SPX options. Long the at-the-money SPX call at 5000 —
costs about $310 per contract. Short the 5900 SPX call, the +18%
strike — you collect about $48. That is the bull call spread, net
debit $262. Then short a 4250 SPX put, the -15% strike — you
collect about $112.

**Stella:** Net cost?

**Horace:** $262 minus $112 = $150 per share-equivalent, plus the
T-bill leg. On $50k of notional that is roughly $2,255 of total
explicit cost, which is what makes the cap 18% rather than the
21–22% it would be at zero cost.

**Stella:** And the slippage on executing those four legs?

**Horace:** SPX options at 1-year tenor have tight markets. You
can expect about 5 basis points per leg at the mid-point, times 4
legs, so roughly 20 basis points of round-trip slippage, plus a
few dollars in commissions. Call it 25 basis points all-in.

**Stella:** Versus 80 basis points expense ratio plus 12 basis
points secondary-market spread on the ETF — call it 91 basis
points per year.

[VISUAL: image/week48_diy_vs_etf.png]

**Horace:** Over five years on $100k, that is about a $4,900
wealth gap. Scale to $500k and you are paying $24,500 in
convenience taxes for option trades you could place yourself once
a year on the anniversary.

**Stella:** What does the interactive let me play with?

**Horace:** [VISUAL: interactive/week48_buffer_builder.html]
Sliders for spot, buffer percentage, cap percentage, and DTE. The
output shows the net cost — that is the DIY pricing — plus max
profit, max loss, breakeven, and the four underlying option legs
with their individual payoffs charted. You can see immediately
how the cap shrinks if you ask for a deeper buffer.

---

**[SECTION 3 — Principal-protected notes and bank credit risk — 8:00 to 11:00]**

**Stella:** Different product: principal-protected notes from a
bank. How are they different?

**Horace:** Three things. First, they are debt of the issuing
bank, not a bankruptcy-remote ETF wrapper. When Lehman Brothers
went bankrupt in 2008, investors holding Lehman PPNs got about
nine cents on the dollar. The "protection" is unsecured senior
debt — it is only as good as the bank's ability to pay.

**Stella:** Own US-listed claims you can verify.

**Horace:** Right. ETFs are trust structures. Notes are bank debt.
Different beasts.

**Stella:** Second?

**Horace:** Embedded fees. A 5-year PPN typically prices in 200
to 400 basis points of profit for the issuing bank, amortised
over the life. You see this as a worse cap, a longer term, or a
wider participation discount. The fee is not in a prospectus line
item — it is in the structure itself.

**Stella:** Third?

**Horace:** Tax treatment. PPNs are typically taxed as contingent
payment debt instruments — CPDI rules — which means you accrue
phantom interest annually at ordinary income rates. At a 32%
federal plus 5% state bracket, this is 19 percentage points worse
than qualified LTCG. The DIY equivalent — a 5-year zero-coupon
Treasury plus 5-year SPX calls — gets you 1256 treatment on the
options and Treasury rules on the bond. Cleaner.

**Stella:** Liquidity?

**Horace:** Almost none in the secondary market. If you need cash
mid-life on a PPN, the dealer who issued it will quote you another
1–3% haircut.

**Stella:** So when do PPNs make sense?

**Horace:** Niche cases. Trust structures with specific deferral
needs. Institutional compliance requirements that need a
CUSIP-based debt wrapper. For a typical retail investor in a
taxable account, basically never.

---

**[SECTION 4 — When the wrapper does win — 11:00 to 13:00]**

**Stella:** Are there cases where buying the buffer ETF actually
makes sense?

**Horace:** Three. First, account constraints — many 401(k)s and
employer brokerages do not allow options trading at all. In a
non-options account, the buffer ETF is the only way to get that
exposure and the 80bps fee is unavoidable. Take it.

**Stella:** Second?

**Horace:** Discipline failure. If you know you are going to
flinch on the roll date, or close one leg early in a panic, the
fund company is selling you the *commitment* to the structure. A
buffer ETF cannot be broken into mid-period the way a self-managed
DIY structure can. For some investors that is genuinely worth
80bps.

**Stella:** Third?

**Horace:** Notional below ~$50k. SPX options have a $100
multiplier — below $50k of notional you get pushed into SPY
options which lose the 1256 treatment and have wider spreads. The
fund company's pooling lets sub-$50k accounts access the
SPX-priced structure indirectly.

**Stella:** And outside those three?

**Horace:** Outside those three, the DIY version is strictly
better on cost and tax. 25bps DIY versus 91bps ETF, with 1256
60/40 tax versus mixed CG. Run the spreadsheet.

---

**[SECTION 5 — The barbell read — 13:00 to 15:30]**

**Stella:** A barbell sits on a boring base plus
a small convex sleeve. Where does the buffer ETF fit?

**Horace:** It does not fit. It is anti-barbell. The buffer cuts
off the left tail at -15% and slopes down again past it; the cap
cuts off the right tail at +18%. What remains is the *middle* of
the distribution.

**Stella:** And the middle of the distribution is...

**Horace:** What you already get from a plain index fund at 3
basis points. Paying 80bps to delete both tails is not insurance
— it is a tactical bet that the index will spend the year between
-15% and +18%. The base rate for that range over 1928 to 2024 is
about 55%. You are paying a fee to be right 55% of the time on a
binary question.

**Stella:** And the volatility tail wagging the dog.

**Horace:** That is the deeper objection. If a small handful of
extreme moves dominate the long-run return distribution, then
deleting both tails systematically caps your geometric compounding
*below* what the index produces over a long horizon. The buffer
ETF's after-fee long-horizon return is mathematically below the
index's by roughly the cap-truncation-loss minus the
buffer-absorption-gain, which empirically is negative for any
horizon longer than five years.

**Stella:** So the products do best when you do not need them.

**Horace:** Correct. They cap the kind of years where you would
have made money anyway, and they buffer years where you can
already afford to lose 15%. The structure is *psychologically*
useful, but that is a behavioural finance question — Week 11 —
not a structural one.

---

**[SECTION 6 — Practical decision tree — 15:30 to 17:00]**

**Stella:** Wrap it up with the decision tree.

**Horace:** Three questions, in order.

**One**: do you have an options-enabled brokerage account with at
least $50,000 of investable capital you want to expose to the
index? If no, the buffer ETF may be your only path — pay the
80bps. If yes, continue.

**Two**: are you willing to execute four SPX option legs once a
year on the anniversary date, and roll on schedule? If no, the
buffer ETF buys you the commitment — pay the 80bps. If yes,
continue.

**Three**: do you actually want to delete both tails of the
distribution from your portfolio? If yes, build the DIY structure
at 25bps. If no — and for most long-horizon investors the answer
is no — skip the structure entirely. Hold the index, allocate a
small sleeve to convex tail hedges (Week 47), and let the dog
wag.

**Stella:** And principal-protected notes?

**Horace:** Skip them. Always. The combination of bank credit
risk, embedded fees, illiquidity, and ordinary-income tax
treatment makes them strictly dominated by a Treasury-plus-SPX-
calls DIY construction in any account that can hold both. Not a
close call.

---

**[OUTRO — 17:00 to 18:00]**

**Stella:** Bottom line?

**Horace:** Most retail "structured products" are DIY-replicable
with options at one-tenth the cost. The fee on the wrapper is a
convenience tax — sometimes worth paying, usually not. The
deeper issue is that the *shape* of the buffered payoff is the
wrong shape for long-horizon compounders. The barbell wants tails;
buffered products delete tails.

**Stella:** So when your advisor pitches you a buffer ETF...

**Horace:** Decompose it. Four legs. Price each leg. Sum the
costs. If the wrapper is more than 50 basis points more
expensive than the DIY version per year and you have an options
account, pass. If the wrapper saves you from yourself, take it.
There is no third answer.

**Stella:** And if the pitch is a structured note?

**Horace:** Pass. Always.

**Stella:** Run the buffer builder, decompose your advisor's
pitch, and see you next week.

[VISUAL: interactive/week48_buffer_builder.html]
