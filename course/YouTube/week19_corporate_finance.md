## Part 2: YouTube Script

---

**VIDEO TITLE:** Corporate Finance for Investors — Capital Structure,
WACC, Buybacks, and Why Most M&A Destroys Value

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Horace:** Welcome back. Today we're doing corporate finance, but
not the textbook version. We're doing the version a stockholder
needs — the one that tells you whether the CEO you've hired is
allocating your capital well, or quietly burning it.

**Stella:** I always thought corporate finance was for the CFO, not
for me as the holder.

**Horace:** That's the misconception we're going to fix. When you
own a share, you're hiring management to deploy ten dollars of
retained earnings on your behalf for every dollar they paid you in
dividends. Over a decade that's a lot of dollars. Whether they go
into 20% projects or 5% acquisitions is by far the biggest driver
of your long-run return. Bigger than the quarterly EPS beat. Bigger
than the press release.

**Stella:** Bigger than the multiple expansion?

**Horace:** Across a decade, yes. Multiples expand and contract;
capital allocation compounds.

---

**[SECTION 1 — DEBT VS. EQUITY — 1:30]**

**Horace:** Let's start with the most basic decision: how does the
company fund itself? Debt or equity? Two identical pizza chains —
same operating profit, same business — one funded all-equity, one
funded half debt, half equity. In a good year the leveraged owner
earns 18% on their money; the unlevered owner earns 11%. Same
business.

**Stella:** Why doesn't every company just lever up to 90% then?

**Horace:** Because the leveraged owner also goes to zero in the
bad year while the unlevered owner just has a bad year. Leverage
doesn't change the business; it changes the variance of the equity.
The same principle applies — the market can stay irrational longer
than you can stay solvent — and a leveraged equity gets there
faster.

[VISUAL: side-by-side bar chart, "Good year vs. bad year ROE" for
all-equity vs. half-debt firm, showing the wider swing on the
leveraged side.]

**Stella:** So how do firms actually pick?

**Horace:** Stable cash flows can carry more debt. A regulated
utility with predictable revenue can run 50% debt and sleep fine.
A biotech with a binary outcome should run zero. The optimal is
where the marginal tax shield equals the marginal increase in
distress cost.

---

**[SECTION 2 — MODIGLIANI–MILLER — 4:00]**

**Horace:** In 1958 Modigliani and Miller proved capital structure
doesn't matter — in a world with no taxes, no distress, and no
information asymmetry. Real world has all three.

**Stella:** So why do they teach M&M if it's wrong in practice?

**Horace:** Because it tells you exactly which frictions matter.
Tax shield pulls toward more debt. Distress pulls back toward less.
Information asymmetry creates the pecking order — internal cash
first, then debt, equity last as a signal of last resort. M&M is
the baseline; the deviations from it *are* the lesson.

---

**[SECTION 3 — WACC — 6:00]**

**Horace:** Now the formula every analyst memorises. WACC equals
the equity weight times cost of equity, plus the debt weight times
cost of debt times one minus tax. The minus-tax bit is the tax
shield.

[VISUAL: image/week19_wacc_diagram.png — low-leverage tech firm
with WACC ~10.3%, high-leverage utility with WACC ~5.9%, drawn as
stacked weighted contributions.]

**Stella:** So a tech firm has a higher WACC than a utility?

**Horace:** Yes — both because tech has higher business risk so
higher cost of equity, and because tech carries less debt so it
captures less of the tax shield. The utility's 5.9% WACC versus
tech's 10.3% means the utility can greenlight a 7% project that
would be a value-destroyer at the tech firm.

**Stella:** Is WACC the same as the discount rate in a DCF?

**Horace:** When you're discounting free cash flow to the firm,
yes — same number. When you're discounting equity cash flows
directly, you use cost of equity alone, not the blended WACC. That
matching is where most amateur DCFs go off the rails.

**Stella:** And ROIC vs. WACC tells me…

**Horace:** Whether each retained dollar is creating or destroying
value. Above WACC, creating. Below, destroying. Year after year,
that gap is the compounding spread.

[VISUAL: interactive/week19_capital_lab.html — sliders for equity
weight, cost of equity, cost of debt, tax rate; live WACC and
project NPV with comparative bars for AAPL, MSFT, JPM, KO, F.]

---

**[SECTION 4 — BUYBACKS AND THE SILENT COMPOUNDER — 9:00]**

**Horace:** Now the fun part. Let me show you the most aggressive
buyback program in corporate history.

[VISUAL: image/week19_aapl_buybacks.png — Apple share count from
26.5B to 15.4B 2013–2024, plus annual buyback dollars peaking above
$90B.]

**Stella:** That's a lot of money.

**Horace:** Over $700 billion across twelve fiscal years. More
than the entire market cap of all but a handful of companies on
Earth. And the share count went from about 26 and a half billion
shares — on the post-split basis — down to about 15 and a half.
That's a 40-plus-percent reduction in the denominator.

**Stella:** So even if Apple's revenue had been flat, EPS would
have grown.

**Horace:** Substantially. The denominator is the silent compounder
nobody tracks. Most retail investors check earnings growth. Almost
nobody pulls up diluted shares outstanding over a ten-year window.

**Stella:** Why don't more companies do this?

**Horace:** Most do try. Most do it badly. Common abuse: the
company announces five billion of buybacks, share count barely
moves, because the firm simultaneously issued four billion of
stock-based comp to executives. The buyback is then merely
offsetting the dilution. The buyback "returns capital to
shareholders" only on the press release. In the actual share
register, the executives got the cash and you got nothing.

[VISUAL: schematic of pie-chart shares-outstanding with buyback
slices removed and SBC slices added, net change near zero.]

**Stella:** How do I detect that?

**Horace:** Pull the 10-K, find diluted weighted-average shares
outstanding, plot it for five years. If it's flat or rising while
buybacks are announced — you're being quietly shorted by the comp
committee. Mechanical check. Takes ninety seconds.

---

**[SECTION 5 — DIVIDENDS VS. BUYBACKS — 12:00]**

**Stella:** Are buybacks just dividends in disguise then?

**Horace:** In a frictionless world, yes — a dollar is a dollar.
Real world adds three frictions. One: tax. In the US, qualified
dividends are taxed each year as you receive them. Buybacks defer
the gain into the capital-gains box, controlled by you. For a
high-bracket taxable holder, that deferral compounds into real
money over decades. Tax efficiency is part
of the toolkit, not a footnote.

**Stella:** Two and three?

**Horace:** Two: price discipline. A buyback below intrinsic value
is a phenomenal trade for the remaining holders. A buyback above
intrinsic value is a wealth transfer from those who stay to those
who leave. Most buybacks are conducted with no explicit valuation
discipline at all. Three: the dilution-offset trap we just talked
about. Same headline, three completely different outcomes for you.

**Stella:** So which should I prefer?

**Horace:** As a US taxable holder in a high bracket, buybacks are
structurally better. As a retiree drawing income from a tax-deferred
account, dividends are worth more. Same firm, different optimal
answer per holder.

---

**[SECTION 6 — M&A — 14:30]**

**Horace:** Last topic. Mergers and acquisitions. The single most
studied corporate event in finance.

**Stella:** And the verdict?

**Horace:** Brutal. Target shareholders gain 20%–30% on average.
Acquirer shareholders lose 1%–5%. Combined value is roughly flat
to slightly negative on announcement. Most M&A destroys value for
the buyer's holders.

**Stella:** Then why do CEOs keep doing them?

**Horace:** Four reasons. Winner's curse — to win the auction you
have to value the target highest, which means you're most likely
to overpay. Integration friction — two ERP stacks, two cultures,
two customer-service ladders, never as cheap as the slide says.
Empire building — CEO comp tracks company size more reliably than
company value. And cycle timing — M&A volume peaks at market peaks,
exactly the wrong moment.

[VISUAL: two-bar chart, target +25% vs. acquirer -3% on
announcement, labelled "average across 50 years of US M&A."]

**Stella:** What do I do when a company I own announces an
acquisition?

**Horace:** Default to sceptical. Read four things. Price paid
versus comparables. Funding mix — cash from the balance sheet is
best, stock at a depressed price is worst. Synergy claim — cost
synergies credible, revenue synergies almost always fiction. Track
record of this management team on prior deals. If three of those
four are unfavourable, trim or hedge.

**Stella:** And the one-line tell?

**Horace:** When the press release uses the word "transformational,"
the existing business is stagnating and they are buying a story.
That word, on its own, is a coin you can pick up.

---

**[OUTRO — 17:30]**

**Horace:** Putting it together. Capital structure shapes the
variance of the equity, not the business. WACC is the hurdle every
project must clear. Buybacks done right are the silent compounder
behind per-share earnings; done wrong, they're a dilution-offset
trap. M&A is where most acquirer equity goes to die. And the one
metric I check first on any large-cap I'm researching — diluted
shares outstanding over five and ten years, against ROIC. Two
columns, ninety seconds, more signal than the entire press kit.

**Stella:** Next week?

**Horace:** Next week, earnings quality and free cash flow — how
to tell whether the reported profit is real cash or accounting.
Direct follow-on to today.

[VISUAL: subscribe outro card]
