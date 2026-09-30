## Part 2: YouTube Script

---

**VIDEO TITLE:** Advanced Financial Statement Analysis — DuPont, Cash
Conversion, and the Two Scoring Models Every Stock Picker Should Know

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00 to 1:20]**

**Stella:** Welcome back to Chanmainvest. Week 35. We have spent the
last twenty-something weeks building up the toolkit. Read the
statements, understand capital structure, separate cash from earnings,
discount cash to a fair value, then size with risk metrics. This week
we close the financial-statement-analysis arc with the four wrenches
that professional analysts actually pull out of the box every quarter.

**Horace:** Four tools, two pages of paper, half an hour per company.
DuPont decomposition. Cash conversion cycle. Beneish M-score. Altman
Z-score. None of them generate alpha by themselves. Together they make
up something almost as valuable — a *negative-alpha filter*. They tell
you which positions to think twice about before sizing up.

**Stella:** And we have a hands-on lab at the end of this week's
lesson where you can move sliders and watch the Z-score classification
flip in real time. Let us get into it.

---

**[SECTION 1 — DuPont, 1:20 to 5:00]**

**Stella:** First wrench. DuPont decomposition. Horace, walk us
through the identity.

**Horace:** Return on equity equals net income over equity. That is
the headline number on every annual report. DuPont splits that one
ratio into three. ROE equals net profit margin, times asset turnover,
times the equity multiplier. The middle two cancel algebraically — net
income over equity is mathematically the same thing — but the *split*
is information.

**Stella:** What kind of information?

**Horace:** Margin tells you the *quality of the business*. Turnover
tells you the *intensity of the assets*. Equity multiplier tells you
the *leverage*. Two firms with the same 17% ROE can be radically
different animals.

**[VISUAL: image/week35_dupont_compare.png]**

**Stella:** And the chart on screen now is exactly that comparison
across five very different firms — Apple, Microsoft, Coca-Cola, JPMorgan,
and Ford. Walk us through it.

**Horace:** Start with Apple on the left. Net profit margin around 24
percent. Asset turnover roughly 1.07. Equity multiplier 6.4. Multiply
those out and you get an ROE north of 150 percent. That equity
multiplier looks like leverage but it is mostly the buyback story from
Week 19 — Apple has retired so much equity that the denominator is
unnaturally small.

**Stella:** Microsoft next.

**Horace:** Margin even higher, around 36 percent. Turnover lower at
0.48 because they sit on a huge cash and intangible asset base.
Equity multiplier under 2. ROE in the high thirties. That is what a
clean software business looks like. Margin doing all the work.

**Stella:** Coca-Cola.

**Horace:** Margin 23 percent — brand premium. Turnover under 0.5,
because the brand is on the balance sheet as goodwill. Multiplier 4 —
moderate leverage. ROE in the low forties. Brand businesses always
have this shape. High margin, low turnover, modest leverage.

**Stella:** JPMorgan and Ford are interesting.

**Horace:** Both around 13 to 17 percent ROE — same headline, totally
different paths. JPMorgan: margin 37 percent on revenue, but turnover is
tiny — four cents of sales per dollar of assets. The leverage
multiplier is 11.6, because that is what banks are. They borrow short
and lend long. The ROE is built on leverage. Ford is the opposite:
turnover 0.65, almost twenty times JPM's, but margin only 3 percent.
Leverage 6.6. Same ROE, completely different fragility profile.

**Stella:** And the practical takeaway for an investor?

**Horace:** When ROE moves, ask which leg moved. If margin compressed,
that is a competitive issue. If turnover dropped, that is an asset
build-up issue. If the multiplier rose, that is the capital structure
moving — could be aggressive buybacks like Apple, could be debt-funded
acquisitions, could be losses eating into book equity. Three very
different stories with the same ROE shape.

---

**[SECTION 2 — Cash Conversion Cycle, 5:00 to 7:30]**

**Stella:** Second wrench. Cash conversion cycle.

**Horace:** Three components. DSO — how long customers take to pay.
DIO — how long inventory sits before selling. DPO — how long *you*
take to pay suppliers. CCC equals DSO plus DIO minus DPO. The number
of days a dollar of input spending stays trapped before coming back as
customer cash.

**Stella:** And why does it matter?

**Horace:** Because growth on a positive CCC is a working-capital tax.
Every additional dollar of revenue ties up more cash in receivables
and inventory. Costco, Apple, Amazon at certain points — they run
*negative* CCCs. Suppliers finance their inventory. They are paid
before they pay. Growth on a negative CCC is a cash *machine*. Growth
on a +90-day CCC is a cash *drain*.

**Stella:** What do I watch for?

**Horace:** Two things. First, the *trend*. Three rising quarters of
DSO is the most reliable advance warning of a revenue-recognition
problem. When the receivables grow faster than the sales, somebody is
booking revenue that customers do not feel obligated to pay yet.
Second, *direction versus competitor*. Compare to two named peers in
the 10-K. If your DSO is rising while the peer's is flat, the problem
is company-specific, not industry-wide.

**Stella:** Quick example?

**Horace:** Valeant Pharmaceuticals before its 2015 collapse — DSO
expanded from roughly 35 days in 2012 to over 100 days by 2015.
Receivables tripled while sales doubled. The CCC tripled. The
M-score eventually fired too, but the working capital number
diverged from the competitive set first. As Stella's Week 20 lesson
put it, cash is the fact and earnings are the opinion. CCC is one of
the cleanest readings of that fact.

---

**[SECTION 3 — Beneish M-score, 7:30 to 11:00]**

**Stella:** Third wrench. Beneish M-score.

**Horace:** Daniel Beneish, 1999. Eight one-year-change ratios combined
into a single probit-style composite. The math is uglier than DuPont;
the interpretation is simple. Above minus 1.78, the model classifies
the firm as a *probable manipulator*. Below, probably not.

**Stella:** What is each of the eight ratios capturing?

**Horace:** DSRI — receivables growing faster than sales. GMI — gross
margin deteriorating. AQI — asset quality, capitalised costs piling up.
SGI — sales growth itself, since fast growth tempts management to
smooth. DEPI — slowing depreciation, longer useful lives, lower
expense. SGAI — SG&A growth versus sales. LVGI — leverage trend. TATA
— total accruals, the Sloan piece from Week 20.

**Stella:** Track record?

**Horace:** Roughly 76 percent hit rate on known manipulators in
Beneish's original test set, with about a 17 percent false-positive
rate. It famously fired on Enron in 1997 — three years before the
collapse — and on WorldCom in 1999. It missed Wirecard, because
Wirecard's fraud was not earnings manipulation. It was making up the
cash balance. Different lie, different footprint, no M-score
signature.

**Stella:** So it is a screen, not a verdict.

**Horace:** Exactly. Alpha sources include looking at the right
numbers. M-score tells you *which 10-Ks to actually open and read
first*. When a name lights up, you read it carefully. When it
doesn't, you still read it, just with less urgency. That filtering
function is worth a lot, even if the model itself doesn't catch every
fraud.

---

**[SECTION 4 — Altman Z-score, 11:00 to 14:30]**

**Stella:** Fourth wrench. Altman Z-score.

**Horace:** 1968. Edward Altman at NYU. Multiple discriminant analysis
on 33 bankrupt and 33 non-bankrupt manufacturers. Five ratios, fixed
weights, single number. Z = 1.2 working-capital-to-assets, plus 1.4
retained-earnings-to-assets, plus 3.3 EBIT-to-assets, plus 0.6 market-
equity-to-total-liabilities, plus 1.0 sales-to-assets.

**Stella:** And the cutoffs.

**Horace:** Below 1.81, distress zone — bankruptcy probability in the
next two years is materially elevated. Between 1.81 and 2.99, gray
zone, watch list. Above 2.99, safe zone. Original test set had
roughly 80 to 90 percent accuracy.

**[VISUAL: image/week35_zscore_distress.png]**

**Stella:** Chart on screen. Three trajectories. GE, Ford, Apple.

**Horace:** GE is the textbook case. Trace the line. 2010, Z around
2.5 — gray zone, recovering from the 2008 crisis. 2012 to 2014, drifts
up toward 2.7. Then 2015, 2016, 2017 — slides through the gray zone
into distress. By 2018, Z below 1.3. That was the year of the dividend
cut and the Power-segment writedowns. The Z-score said "watch this" in
2015 and "this is in trouble" by 2017. The eventual breakup announced
in 2021 surprised nobody who had been tracking the ratio.

**Stella:** And Ford?

**Horace:** Ford has been parked in the gray zone for years. That is
about right for a US automaker — high asset intensity, cyclical
margins, real but manageable bankruptcy risk in any given downturn.
Ford did file for bankruptcy in many of GM's neighbouring years. Z in
the 1.5 to 1.7 band is the home address for a deep-cyclical
manufacturer. It is not a sell signal; it is a *position-sizing*
signal.

**Stella:** And Apple?

**Horace:** Z above 5 the entire stretch. Deeply safe. Brand business
with negligible debt-to-equity and a fortress cash pile. The Z-score
will never tell you when to *buy* a name like Apple, but it confirms
what you already suspected — there is no balance-sheet tail risk in
the position.

**Stella:** Common pitfalls?

**Horace:** Two. First, Z is calibrated for US manufacturers. There
are variants — Z-prime for private firms, Z-double-prime for
non-manufacturers and emerging markets — that change both
coefficients and cutoffs. Use the right one. Second, the *trend*
matters more than the level. A firm at Z = 1.5 and rising is in better
shape than a firm at Z = 2.5 and falling. Slope dominates altitude.

---

**[SECTION 5 — The Interactive Lab, 14:30 to 16:30]**

**Stella:** Let us walk through this week's interactive tool.

**[VISUAL: interactive/week35_fsa_lab.html]**

**Stella:** Two panels. On the left, the Altman Z-score calculator.
You can pick a preset firm — Apple, Microsoft, Ford, GE in 2018, or
Lehman in 2007 — or punch in your own five components. The Z is
computed live, and the band classification on the right flips between
distress, gray, and safe as you move the inputs.

**Horace:** Try the Lehman 2007 preset. Z under 1.0. Distress band, a
year before the bankruptcy. The market did not know; the model did.

**Stella:** On the right, three sliders for DuPont. Net profit margin,
asset turnover, equity multiplier. Watch the resulting ROE. Set
margin 24 percent, turnover 1.0, multiplier 6 — you get an Apple-
shaped ROE in the 140s. Drop the multiplier to 1, ROE collapses to 24.
That is what the buyback story is doing under the hood.

**Horace:** The four locales are wired up — English, Hong Kong
traditional, Taiwan traditional, mainland simplified. Theme switcher
on the page header swaps the chart palette. Embed it directly into
your study notes if that helps.

---

**[OUTRO — 16:30 to 18:00]**

**Stella:** Recap. Four wrenches. DuPont splits ROE into margin,
turnover, leverage. CCC splits days into receivables, inventory,
payables. M-score scores the manipulation footprint. Z-score scores
the bankruptcy probability. Together they are the negative-alpha
filter — they will not find you the next Apple, but they will keep
you out of the next Valeant.

**Horace:** Alpha is rare. The corollary is that
*avoiding negative alpha is cheap*. A two-page diligence sheet costs
you thirty minutes per name. The names you decide *not* to size up
because of what those sheets show you — that is the yield on this
half-hour.

**Stella:** The orthodox framing treats DCF and quality screens as
the place where alpha *comes from* though.

**Horace:** And in my own book that's the wrong framing. The market
is right more often than I am. DCF mostly produces a fair-value
range that overlaps with the current price. This whole toolkit is
defensive — it stops you being on the wrong side of an asymmetric
mispricing the rest of the market has already priced. The real
edges live elsewhere: macro, sector rotation, structural flow,
the occasional tax or instrument-structure advantage. Bottom-up
work keeps you out of the next Valeant. It does not find you the
next Apple. Don't confuse the two.

**Stella:** Next week we move from financial statements into industry
analysis — Porter's five forces, competitive moats, and the kind of
qualitative work that DCF assumptions rest on but rarely justify.

**Horace:** And eventually, in Tranche 3 territory, we put all of this
together into single-name selection. Not yet. First, the rest of the
toolkit.

**Stella:** Until next week.
