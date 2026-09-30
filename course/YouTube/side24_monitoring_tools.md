## Part 2: YouTube Script

---

**VIDEO TITLE:** The Portfolio Dashboard That Actually Works (Side 24)
**RUNTIME TARGET:** ~11 minutes
**HOSTS:** Horace, Stella

---

**HORACE:** Welcome back. Side lesson 24. We've spent fifty-two weeks
designing a portfolio. Today we talk about the boring half — keeping it
running. The tools you actually use to look at the thing once a month.

**STELLA:** And the rule I want viewers to take away first: the tool is
useless without the cadence. Pick a day, run the checklist, close the tab.

**HORACE:** That. So today's plan: four free tools that matter, then the
six-item monthly checklist, then we look at our two images and the
interactive dashboard.

---

**[VISUAL: image/side24_dashboard_template.png]**

**HORACE:** Start with the dashboard image. Four panels. Top-left, wealth
path versus a 60/40 reference — that's your "is the strategy working" line.
Top-right, drawdown — the question is, are you inside your IPS-stated
maximum drawdown number, or have you blown through it? Bottom-left,
asset-class breakdown versus target — that's drift. Bottom-right, fees paid
year to date.

**STELLA:** And every one of those panels can be reproduced in Google
Sheets with `GOOGLEFINANCE` calls. You don't need a SaaS product to see
this.

---

**HORACE:** The four tools.

Tool one: Portfolio Visualizer. Free. The free tier gives you backtest, asset
correlations, factor regression, Monte Carlo, and asset-class data back to
1972. That's the institutional terminal — for retail, free, forever.

Tool two: Morningstar Instant X-Ray. Free with a basic Morningstar account.
This is the overlap detector. Paste your fund list, get back asset-class
breakdown, sector breakdown, top-10 holdings across the whole portfolio, and
pairwise stock overlap.

**STELLA:** Which is the problem most retail portfolios don't know they
have.

**[VISUAL: image/side24_overlap_detection.png]**

**HORACE:** Look at this image. Five funds — VTI, VOO, SPY, QQQ, SCHD.
They feel like five different bets. The heatmap shows the pairwise top-10
overlap. VTI versus VOO: 99% — they are the same fund. VTI versus QQQ:
about 50% — Apple, Microsoft, Nvidia, Amazon, Meta, Alphabet are in both.
VOO versus SCHD: about 30% — even a "value income" ETF shares a third of
the top names with the S&P 500. Average pairwise overlap on this five-fund
portfolio: roughly 60%.

**STELLA:** Which means you are running one concentrated mega-cap bet, paying
four expense ratios for it, and *thinking* you have a diversified portfolio.

**HORACE:** Exactly. The X-Ray catches this in ten seconds. Squinting at
ticker tape doesn't.

---

**HORACE:** Tool three: Empower, formerly Personal Capital. Free aggregator.
Three features matter — the cross-account asset-class view, the fee
analyzer, and the retirement Monte Carlo. The fee analyzer is the killer.
It tells you what sixty basis points compounds to over thirty years on
your *actual* portfolio. That number has talked more retail investors out of
full-service advisors than any blog post.

**STELLA:** Caveat: Empower is a wealth-management lead funnel. They will
call you. Decline politely. The tools stay free.

**HORACE:** Tool four: your brokerage's built-in. Schwab Portfolio Checkup,
Fidelity Portfolio Analysis, Vanguard Portfolio Watch. Use these *for
accounts at that brokerage*. They don't see your spouse's IRA at a different
firm. That's where Empower or the spreadsheet picks up.

---

**HORACE:** Now the workflow most disciplined retail investors actually run
— and it isn't any of those four. It's a Google Sheet. Six columns: ticker,
target weight, target dollars, current dollars, drift in percentage points,
action. Three computed cells: total value, expense-weighted ER, trailing
twelve-month return.

**STELLA:** That's the operating tool. Empower is the audit tool. PV is the
deep-dive tool. X-Ray is the overlap-check tool. Four roles, one each, no
duplicates.

---

**HORACE:** The monthly checklist. Six items.

One. Total return year to date and trailing twelve months versus 60/40. One
sentence in a notes column.

Two. Realised vol and trailing peak drawdown. Inside the IPS number?

Three. Sleeve drift. Each of the seven Week-52 sleeves — within plus or
minus five percentage points of target?

Four. Factor exposures. Quarterly is enough. PV factor regression on your
tilt sleeves. Beta to the named factor still above 0.5? T-stat above 2?

**STELLA:** And if it isn't, that's the half-weight stop-rule from Week 50.

**HORACE:** Five. Fees paid year to date. ER times portfolio value,
prorated. Watch the 401(k) target-date defaults — they slip 0.6% in.

Six. Rebalancing band breaches. Anything over five percentage points gets
actioned *today*. New contributions go to under-target sleeves first.

---

**HORACE:** Now, the interactive. Pick five ETFs from a dropdown of twelve.
Watch the dashboard fill in: asset-class breakdown, sector breakdown,
expense-weighted average, pairwise overlap matrix. Try it.

**STELLA:** Try the all-S&P-500 portfolio first. VTI plus VOO plus SPY plus
IVV plus SCHX. Watch the overlap heatmap go red.

**HORACE:** Then try the model L4 from Week 52. VTI, BND, GLDM, IBIT, DBMF.
Overlap drops near zero, asset-class breakdown spreads across five buckets,
expense-weighted ER comes in around fifteen basis points.

**STELLA:** That's the difference between a portfolio that *looks*
diversified and one that is.

---

**STELLA:** Why monthly though, and not daily? The data is there.

**HORACE:** Because the shape of a modern portfolio is a barbell —
safety on one end, asymmetric speculation on the other, the
four-tranche stack from Week 52 sits exactly in this shape. The
barbell only works if you let the safety end *be* safe. Daily
checking re-introduces the disposition effect from Side 15 into a
sleeve that is supposed to be untouched. And it turns the tail-hedge
sleeve — the small option positions that exist to expire worthless
ninety-five per cent of the time — into a pricing-anxiety machine.
Monthly cadence is the policy that protects the *shape* of the
portfolio from the human running it.

**HORACE:** Closing thought. The point of the dashboard is not to give you
something to look at. It's to give you permission to *not* look — between
review days. The tools watch the bands, you live your life, and on the
fixed monthly day you do the six-item walkthrough. That's the discipline
that compounds.

**STELLA:** Tools without cadence is just a hobby. Cadence without tools is
guessing. You need both.

**HORACE:** Side 24, monitoring tools. That's a wrap.

---
