# Side Lesson 04: Tax Efficiency — Asset Location, Harvesting, and the IRA/401(k) Stack

---

## Part 1: Reading Section

---

### 1. Why This Is Important

For a US household earning between roughly $200k and $750k a year,
**taxes are almost always the largest line item on the lifetime
investment-cost statement**. They beat fund fees, advisory fees, and
trading costs combined — and they do so by an order of magnitude.
At the 32% federal bracket plus a typical 5% state bracket, a balanced
taxable portfolio gives back somewhere between 1.0% and 1.7% per year
in tax drag without anybody noticing, because the brokerage statement
quotes pre-tax. Compound that for thirty years against a 7% real
return and the *after-tax* terminal wealth is 25-40% lower than the
back-of-envelope spreadsheet line.

The good news is that the rules are public, the rates are written
down, and most of the available efficiency is mechanical. You do not
need a tax attorney for the first 80%. You need four moves, in this
order:

1. **Know the schedule.** Long-term capital gains and qualified
   dividends sit on a separate, lower bracket schedule than wages.
   Knowing where you fall on it changes which sleeve of your portfolio
   should live in which account.
2. **Place the right asset in the right account.** A $100,000 BND
   position generates the same pre-tax interest in any account.
   In a brokerage it loses 32%+ of that interest to the IRS every
   April. In a Traditional IRA it loses zero until withdrawal. The
   asset is identical; the *location* changes the after-tax curve.
3. **Harvest losses systematically.** When a position is underwater,
   selling and re-establishing similar exposure crystallises a tax
   loss that offsets gains anywhere else in the portfolio. Most
   retail investors leave this money on the table because the
   wash-sale rule looks scarier than it is.
4. **Stack the accounts in the right order.** Roth, Traditional, HSA,
   401(k), brokerage — each has a different tax treatment on the way
   in, while invested, and on the way out. Filling them in the wrong
   order can cost six figures by retirement.

This lesson is the operating manual for those four moves. The deeper
rule — "the largest unspoken fee is tax; use options and margin to
manage it" — sits at the very end of the stack. Once the easy
structural wins are captured, the marginal dollar of tax efficiency
comes from *how* you hold the position (LTCG holding period, Section
1256 60/40 split, options as deferred income), not from which fund
you bought.

![Three-by-eight grid showing the optimal account location for eight common asset classes across Taxable, Traditional IRA, and Roth IRA columns. Cells are colour-coded green (best location), amber (acceptable), red (worst location). Headlines: bonds and REITs go to Traditional IRA, qualified-dividend stocks stay in Taxable, high-growth assets and crypto go to Roth, MLPs stay in Taxable to avoid UBTI.](../image/side04_asset_location_grid.png)

---

### 2. What You Need to Know

#### 2.1 The 2026 Rate Schedule — The Numbers You Have to Memorise

Three separate schedules govern investment income in the US. Burn the
2026 numbers (post-TCJA-extension) into memory:

**Long-term capital gains and qualified dividends** — held >12 months.

| Bracket | MFJ taxable income (2026) | Single taxable income |
|---|---|---|
| 0% | up to $96,700 | up to $48,350 |
| 15% | $96,701 - $600,050 | $48,351 - $533,400 |
| 20% | above $600,050 | above $533,400 |

On top of that, the **3.8% Net Investment Income Tax (NIIT)** kicks
in above $250k MAGI for MFJ ($200k single). It applies to interest,
dividends, capital gains, royalties, rents, and most passive income.
For a typical professional couple at $300k AGI, the *effective* LTCG
rate is therefore 15% + 3.8% = **18.8%**, not 15%. Above $600k the
top federal rate is 20% + 3.8% = **23.8%**.

**Short-term capital gains** (held ≤12 months) and **non-qualified
dividends** (REITs, most BDCs, many foreign stocks) — taxed as
**ordinary income** at your marginal wage bracket: 22% / 24% / 32% /
35% / 37%. NIIT still applies on top.

**Treasury interest** — federal ordinary income, **state-exempt**.
A 4.2% 10-year Treasury in California is a roughly 4.4% taxable-
equivalent yield; in a 0%-state, the headline 4.2% is the headline.

**Municipal bond interest** — federal-exempt; in-state munis are
state-exempt too. Often AMT-exempt depending on the issue.

The single most important consequence is the **rate gap**: in the 32%
bracket, ordinary-rate income loses 37% (32% federal + 5% state) of
every dollar, while qualified-dividend income loses 20% (15% LTCG +
5% state). The gap is *17 percentage points of after-tax yield* on
the same gross dollar. That is the lever asset location pulls.

#### 2.2 Asset Location — The Free Lunch

The principle is one sentence: **hold tax-inefficient assets in
tax-deferred accounts, and tax-efficient assets in taxable
accounts.** Mechanical, not clever. A summary of the eight
canonical sleeves:

1. **Broad US stock index (VTI / SPY).** Yields 1.4%, mostly qualified
   dividends, capital gains realise only when *you* sell. Tax drag in
   a brokerage is roughly 0.3-0.4% per year. **Best location:
   Taxable.** (Roth is acceptable but wastes the rare LTCG advantage.)
2. **Broad international stocks (VXUS / IEFA).** Same yield profile
   plus a *foreign tax credit* of 7-9% of the dividends paid abroad —
   a credit you can only claim if the position is in a *taxable*
   account. Putting VXUS in an IRA forfeits the credit. **Best
   location: Taxable.**
3. **Investment-grade and total-bond ETFs (BND / AGG / VTEB).** Yield
   4-5% in interest, all taxed as ordinary income at federal + state.
   Tax drag in a brokerage at 32% federal + 5% state is roughly 1.6%
   per year on a 4.5%-yielding bond fund. **Best location:
   Traditional IRA / 401(k).**
4. **High-yield corporate bonds (HYG / JNK).** Same problem as IG,
   except the yield is 7-8% and the drag is correspondingly larger
   (~3.0%/yr). **Best location: Traditional IRA.**
5. **REITs (VNQ / SCHH).** Distributions are *non-qualified ordinary
   dividends*. The 20% Section 199A pass-through deduction softens
   the blow to roughly 80% of the marginal rate, but it is still much
   worse than LTCG. **Best location: Traditional IRA**, with Roth a
   close second.
6. **TIPS (SCHP / VTIP).** Inflation accruals are *imputed* ordinary
   income each year, even when not received in cash ("phantom
   income"). Holding TIPS in a brokerage account guarantees a tax
   bill on money you have not yet seen. **Best location: Traditional
   IRA / I-Bonds (the I-Bond version defers automatically).**
7. **MLPs and energy partnerships (EPD, MPLX, ET).** Distributions
   are partly return-of-capital (great for taxable) but generate
   K-1s. Inside an IRA, K-1 income above $1,000 triggers UBIT —
   *Unrelated Business Income Tax* — at trust-level rates up to
   37%, and the IRA itself files a separate return. **Best location:
   Taxable. Worst location: any IRA.**
8. **High-growth assets and crypto (small-cap, BTC ETFs, single-name
   speculation).** Returns are dominated by capital gains, which can
   be deferred indefinitely in a brokerage. But because the *expected
   compound return is highest*, every dollar of growth is most
   valuable when it is also tax-free. **Best location: Roth.** A
   Roth-held BTC IBIT or speculative single-stock position
   compounded for 30 years and pulled out at 65 is the most powerful
   single tax move available to a retail investor.

The image at the top of this lesson is the visual summary. Cells in
green are the right location for that asset; red is wrong; amber is
acceptable.

#### 2.3 Tax-Loss Harvesting and the Wash-Sale Rule

Tax-loss harvesting (TLH) is mechanical: any position currently
trading below your cost basis can be sold to crystallise a paper loss,
which then offsets realised gains anywhere else in your portfolio
*and* up to $3,000 of ordinary income per year. Unused losses carry
forward indefinitely. The savings on a typical $1M taxable portfolio
in a normal-volatility year is roughly $3,000-$5,000 / year, which
compounds to **roughly $100k of saved taxes over a 30-year horizon**
on the chart below.

![Cumulative tax-loss-harvesting savings over 30 years on a $1M taxable portfolio with 16% annualised volatility. The annual bar chart shows higher savings in volatile years (2008-style spikes of $12-15k) and modest steady-state harvesting of $2-4k in calm years. The cumulative line crosses $100k around year 25-30. Caption notes the savings assume realised gains are available to offset and the harvest is reinvested into a substantially-not-identical replacement.](../image/side04_tlh_savings.png)

**The wash-sale rule (IRC §1091)** is the only real constraint. If
you sell a security at a loss, you cannot buy "substantially
identical" securities in any account you control (including IRAs and
your spouse's accounts) within **30 days before or after** the sale,
or the loss is disallowed and added to the basis of the replacement.

Three rules of thumb that pass the test in practice:

1. **Pair similar but not identical ETFs.** VTI ↔ ITOT (different
   issuer, different index), VOO ↔ IVV, BND ↔ AGG. The IRS has never
   challenged a swap between two index ETFs tracking *different
   indices* even if the indices are 95%+ overlapping.
2. **Hold the replacement for at least 31 days.** After day 31 you
   may swap back if you prefer the original. Most TLH platforms
   (Wealthfront, Betterment, Schwab Tax-Loss Harvesting) automate
   this round-trip.
3. **Do not buy the same security in your IRA inside the window.**
   This is the most expensive accidental wash-sale: most retail
   investors do not realise the rule reaches across accounts and even
   into spousal IRAs.

The harvest is "free" only at the *gross* level. At the *net* level
you have lowered the cost basis of the replacement, so the saved tax
is really *deferred* tax. The compounded benefit is real (you keep
more invested, longer) but you are not literally erasing the
liability — you are postponing it, ideally until a year you control
the bracket (early retirement, gap year, charitable transfer, or
death-with-step-up).

#### 2.4 Roth Conversions and the Mega-Backdoor Roth

Two advanced moves that compound enormously over a career.

**Roth conversion.** You move money from a Traditional IRA or 401(k)
into a Roth IRA. The conversion is taxable as ordinary income in the
year of the move. The Roth then grows tax-free forever and is not
subject to RMDs (Required Minimum Distributions, currently age 75
under SECURE 2.0). The arithmetic is favourable whenever **your
*current* marginal bracket is lower than your *expected* future
marginal bracket on the same dollar.**

The classic case: a 60-year-old retires with a $1.5M Traditional IRA
and waits until age 75 RMDs force ~$60k/year of distributions on top
of Social Security. Those forced distributions get taxed at the 22%+
bracket. Instead, the retiree converts $50k/year between ages 60 and
70 in the *low-income* gap years, paying 12-22% on the way in and
zero on the way out. The lifetime tax bill drops by 5-10 percentage
points on the converted amount.

**Mega-backdoor Roth.** A subset of 401(k) plans allow *after-tax*
(non-Roth) contributions on top of the regular $23,500 employee
limit, up to the combined $70,000 (2026) annual addition cap. Those
after-tax dollars can be immediately rolled — *in-plan* or to a
Roth IRA — into Roth status, putting up to **$46,500 of extra Roth
money** into the system every year. The catch: only ~50% of plans
support the in-plan conversion, and the rules are an HR-department
question, not a tax-attorney one. If your plan supports it, this is
the single highest-leverage tax move in the US system.

#### 2.5 The HSA — The Triple-Tax Account

The Health Savings Account is the only US account that is **tax-free
on the way in, tax-free on growth, and tax-free on the way out**
(provided withdrawals are for qualified medical expenses). 2026
contribution limits: $4,400 single / $8,750 family. The HSA is
available only if you are enrolled in a qualifying high-deductible
health plan (HDHP).

The high-leverage move is to **fund the HSA, invest it in a
total-stock-market fund, and pay current medical expenses out of
pocket** — saving the receipts. After 30 years of compounding the
HSA can be $300k+, and you can reimburse yourself for the *old*
medical receipts at any time, tax-free. This converts what looks
like a healthcare account into a stealth Roth IRA with no income
limits, no contribution caps tied to wages, and no required
distribution age (HSA distributions for non-medical expenses after
65 are taxed as ordinary income — same as a Traditional IRA — so
the worst-case downside is "Traditional IRA").

The HSA is the *first* dollar in the contribution stack for any
investor with access to it. Even before the 401(k) match.

#### 2.6 The Account-Filling Order

The full priority stack for a new dollar of savings, in 2026:

1. **401(k) up to the employer match.** A 100% return on day one is
   not negotiable.
2. **HSA to the limit, if eligible.** Triple tax treatment.
3. **401(k) up to the $23,500 employee limit.** Traditional or Roth
   depending on your bracket — Roth if current bracket ≤ expected
   future, Traditional otherwise.
4. **Backdoor Roth IRA, $7,000.** For high earners above the direct
   Roth income limits (single MAGI > $165k, MFJ > $246k in 2026).
5. **Mega-backdoor Roth, up to $46,500 if your plan supports it.**
6. **Taxable brokerage account.** Once the tax-advantaged caps are
   exhausted, the taxable account holds the residual — which is
   exactly where the asset-location and TLH discipline does its
   work.
7. **529 plan**, contemporaneously with steps 1-6, for any
   college-bound dependents — the limit varies by state but $10-15k
   per beneficiary is the typical sweet spot.

#### 2.7 Withdrawal Order — Distribution-Side Tax Planning

The accumulation order has a mirror on the distribution side. The
canonical retirement-withdrawal sequence:

1. **Required Minimum Distributions first**, if any (Trad IRA after
   age 75, inherited IRAs).
2. **Taxable account next.** Assets sold from the taxable account
   benefit from the basis you have built up (and any losses you
   harvested). Capital gains realisation is deliberate — you can pick
   high-basis lots and stay in the 0% LTCG bracket if your taxable
   income is under the threshold.
3. **Traditional IRA / 401(k) third.** Withdrawals are ordinary
   income; control the bracket by keeping annual draws under the
   next-bracket boundary.
4. **Roth last.** The Roth grows tax-free with no RMDs and no tax on
   withdrawal. Holding it last maximises tax-free compounding and
   leaves it for late-life expenses, charitable transfers, or
   inheritance (where heirs get 10 tax-free years under SECURE 2.0).

A subtle and powerful variant: in the gap years between retirement
and age 75 (or earlier Social Security claiming), keep ordinary
income low and use those years to **convert Traditional → Roth** (per
§2.4) while withdrawing from the Taxable account for living expenses.
This is the single most-effective lifetime tax-management move
available to early retirees.

#### 2.8 Tax via Options and Margin

Once steps 2.2-2.7 are mechanical, the marginal dollar of
tax-efficiency comes from *how* you hold the position. There are
four exposure-level moves:

- **Use Section 1256 contracts (SPX / NDX index options, /ES
  futures, /MES, /MNQ).** These are taxed at 60% LTCG / 40% STCG
  *regardless of holding period* — a blended top rate of about 26.8%
  vs. 37% for short-term equity options. For active option writers
  this is a 10pp blanket discount.
- **Cover instead of selling.** If a stock has a $200k embedded gain,
  don't sell to reduce exposure — overlay a short call (covered call)
  or a collar (long put + short call). You collect premium or pay
  little, the delta drops, and the embedded gain stays unrealised.
- **Replace shares with synthetic longs.** A long-call + short-put
  at the same strike replicates 100 shares but uses ~10x less capital.
  Selling the underlying shares while holding the synthetic *crystallises
  the tax loss* if underwater (subject to wash-sale considerations on
  the synthetic — get a tax pro to bless the structure) and frees the
  capital for other uses.
- **Box spreads and portfolio-margin loans.** Borrow against the
  portfolio at sub-Treasury rates, use the cash, and never sell. The
  position keeps compounding tax-free until you eventually sell or
  step-up at death.

These are the moves that separate "good" from "exceptional" after-tax
returns over a 30-year horizon. They are not necessary to capture
80% of the available efficiency — the §2.2-2.7 stack handles that —
but they are how you close the last 20% of the gap.

---

### 3. Common Misconceptions

**1. "All dividends are taxed the same way."** Wrong. Qualified
dividends from US C-corps held >60 days are taxed at LTCG rates.
REIT distributions, BDC distributions, MLP guaranteed payments, and
most foreign dividends are *non-qualified* and taxed as ordinary
income.

**2. "I can deduct my full investment loss against income."** Only
$3,000 per year against ordinary income ($1,500 if MFS). Larger
losses offset realised gains first, then carry forward indefinitely
against future gains.

**3. "Bonds in Roth are smart because they're 'safe.'"** Backwards.
Bonds yield ordinary income, which gets the worst tax treatment.
Putting them in Roth wastes the Roth's tax-free growth on the
*lowest-expected-return* asset in your stack. Bonds should sit in a
Traditional IRA, where the income is deferred to a low-bracket
retirement year.

**4. "TIPS and I-Bonds are the same thing."** They are not. TIPS in
a brokerage account generate phantom-income tax bills annually on
the inflation accrual. I-Bonds defer the tax to redemption. Hold
TIPS in IRAs only; I-Bonds anywhere is fine.

**5. "I need to wait 30 days *after* selling to buy back the same
security."** It is 30 days *before* and 30 days *after* — a full 61-day
window centred on the sale. And it includes the IRA, the spousal
IRA, and any joint account.

**6. "Roth is always better than Traditional."** False. Roth wins
when your *current* marginal bracket is *lower* than your *retirement*
marginal bracket. Most high earners in their peak years are in 32-37%
brackets; Traditional contributions deduct at that rate, and the
withdrawal in retirement is often at 22-24%. Traditional wins in that
case.

**7. "MLPs in an IRA are fine because IRAs don't pay tax."** They
trigger UBIT — Unrelated Business Income Tax — at trust rates, the
*highest* rates in the code. If your MLP K-1 reports more than $1,000
of UBTI, your IRA itself files Form 990-T and pays tax. Keep MLPs
out of any tax-advantaged account.

**8. "Tax-loss harvesting permanently eliminates the tax."** It
defers it. The replacement security has a lower basis equal to your
original cost minus the harvested loss. When you eventually sell the
replacement, the gain is bigger by exactly the amount you harvested.
The benefit is the time value of money on the deferred tax, plus the
optionality to realise in a low-bracket year (or never, via step-up
at death).

**9. "Roth conversions are pointless if my future bracket is lower."**
Yes — that is exactly the case where you should *not* convert. Run
the bracket comparison every year. Convert in years when current <
future; do nothing in years when future ≤ current.

**10. "The HSA is a healthcare account; it has nothing to do with my
investments."** The HSA is the most powerful tax-advantaged
*investment* account in the US system. The healthcare label is a
historical artefact. If your HSA is in a "saving account" earning
0.05%, you are leaving the triple-tax benefit on the table.

---

### 4. Q&A

**Q1: I'm 35, in the 24% bracket, with a $400k taxable account, $150k
Trad IRA, and $50k Roth IRA. Where do my new contributions go?**

A: Stack order: 401(k) match → HSA → 401(k) Trad up to limit (24%
deduction is solid) → backdoor Roth IRA → mega-backdoor if available
→ taxable. Inside the existing balances, move bonds and any REIT
positions out of the taxable account into the Trad IRA, and put
broad-market index funds and international stock into the taxable.
Use the Roth for any speculative high-growth exposure (small-cap,
crypto ETF, growth single names).

**Q2: How much TLH alpha can I realistically expect?**

A: Empirically, 30-60 bps per year of after-tax alpha on a balanced
stock portfolio at a 32% federal + 5% state bracket. The benefit
declines as the cost basis of the portfolio rises (after a long
bull run there is less left to harvest), and spikes in volatile
years like 2008 and March 2020 ($15k+ on a $1M book in a single
tax year). Cumulative over 30 years: roughly $100k on a $1M
starting balance, depending on the path.

**Q3: I'm above the Roth IRA income limit. Can I still contribute?**

A: Yes, via the **backdoor Roth IRA**: contribute $7,000
non-deductibly to a Traditional IRA, then immediately convert it to
Roth. The conversion is tax-free if you have no other pre-tax
Traditional IRA balance (the *pro-rata rule* is the only trap — it
does not apply if your only Traditional IRA balance is the one you
just funded). For 401(k)s above the $23,500 employee limit, the
mega-backdoor Roth is the analogous move.

**Q4: When does Roth-conversion math work?**

A: Run the comparison once a year. If your *current* marginal
bracket on the converted dollar is lower than your *expected
retirement* marginal bracket on the same dollar (after counting
Social Security, pensions, and RMDs), convert. If higher, don't.
The most reliable conversion years are early-retirement gap years
(60-70) where ordinary income is low and you can fill the 12%/22%
brackets cheaply.

**Q5: Are municipal bonds always better than Treasuries in a taxable
account?**

A: Compare the **tax-equivalent yield**: muni yield ÷ (1 - federal
bracket - state bracket if in-state). At 32% federal + 5% state,
a 3.5% in-state muni has a TEY of 3.5% / (1 - 0.37) = **5.55%**.
A 4.2% Treasury has a TEY of 4.2% / (1 - 0.32) = **6.18%** (state
exemption already applied). Treasuries win in this case. The
crossover is usually at the 35-37% federal bracket.

**Q6: Can I tax-loss harvest in my IRA?**

A: No — there are no taxes inside the IRA, so there are no losses
to harvest. Worse, an IRA purchase of the substantially-identical
security can *trigger* a wash sale on the loss you took in the
taxable account, disallowing the deduction permanently (the basis
adjustment cannot be applied to an IRA position).

**Q7: What about state income tax — does it change asset location?**

A: Yes, materially. Treasuries are state-exempt, so in a high-tax
state (CA 13.3%, NY 10.9%, HI 11%) the case for holding Treasuries
in *taxable* gets stronger because you save state tax that an IRA
doesn't otherwise charge. Munis become more attractive than
Treasuries above the 35% federal bracket in 0%-state states, and
above 32% in high-state states.

**Q8: What is "phantom income" on TIPS and why does it matter?**

A: TIPS' principal adjusts for CPI inflation each month. The IRS
treats that adjustment as taxable ordinary income in the year it
accrues, even though you receive the cash only at maturity. In a
brokerage you owe tax annually on imputed income; in an IRA the
adjustment is irrelevant because nothing inside the IRA is taxed
until withdrawal. TIPS belong in an IRA.

**Q9: I have a $200k embedded gain in AAPL. Tax cost to sell is
$40k+. How do I reduce exposure without selling?**

A: Three options. **Covered call** — sell a 30-delta 60-DTE call,
collect 1-2% premium, keep the gain unrealised, give up some
upside (Week 27). **Collar** — buy a 25-delta put + sell a
25-delta call, paid for by the call premium, locks in a band
without realising gain (Week 30). **Synthetic-short overlay** —
short an equivalent index future against the position to hedge
market beta only; idiosyncratic AAPL exposure remains. Each
removes exposure without crystallising tax. Tax via options.

**Q10: Should I prioritise Roth or HSA contributions?**

A: HSA first — it is triple-tax (deductible going in, tax-free
growth, tax-free withdrawals for medical), better than either Roth
or Traditional. Then 401(k) up to the match. Then Roth or Roth
401(k) depending on bracket math. The HSA's only catch is that
non-medical withdrawals before 65 incur a 20% penalty plus
ordinary tax — after 65 the penalty is waived, leaving worst-case
"Traditional IRA" treatment.

**Q11: How does the 3.8% NIIT work in practice?**

A: It applies to the *lesser* of (a) net investment income, or (b)
MAGI above the threshold ($250k MFJ / $200k single). At $300k MAGI
with $40k of investment income, you owe 3.8% × min($40k, $50k) =
$1,520. The fix is the same as for any tax: either reduce
investment income (asset location), reduce MAGI (Traditional 401(k)
contributions), or do both. The practical effect is to push the
*real* LTCG rate to 18.8% / 23.8% for affected households.

**Q12: What does the Tax Optimizer in this lesson actually do?**

A: It takes your federal bracket, state rate, taxable / Trad / Roth
balances, and current age. It computes (1) the optimal asset-class
location for each of eight standard sleeves; (2) projected after-tax
wealth at age 65 under reasonable growth assumptions for each
account type; (3) a suggested annual TLH harvest target based on
your taxable balance and assumed equity volatility; and (4) a
suggested annual Roth-conversion amount sized to fill your current
marginal bracket without crossing the next break. It is not tax
advice — it is a back-of-envelope sanity check on the moves
described in this lesson.
