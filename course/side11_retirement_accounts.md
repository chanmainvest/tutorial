# Side Lesson 11: Retirement Accounts — 401(k), IRA, Roth, HSA, and the Optimal Contribution Stack

---

## Part 1: Reading Section

---

### 1. Why This Is Important

The US tax code hands every working household a stack of tax-advantaged
wrappers — a 401(k), an IRA in two flavours, a Roth, an HSA, and (for
some plans) a mega-backdoor channel — and the dollar limits go up
nearly every year. In 2026 the headline numbers are: **$23,500** in a
401(k) ($31,000 if you're 50+), **$7,000** in an IRA ($8,000 if 50+),
**$4,300** in an HSA single ($8,550 family), and a total 401(k) cap of
**$70,000** when you stack employee deferral, employer match, and
after-tax mega-backdoor contributions. Used in the right order, these
wrappers shelter roughly six figures per year of pre-tax income for a
high-earner household.

Four reasons this lesson matters more than any equivalent hour of fund
selection:

1. **The match is a 50-100% guaranteed return.** A 401(k) employer
   match of 50¢ on the dollar up to 6% of salary is a 50% instant
   return on the marginal dollar. No equity strategy on Earth pays
   that. Skipping the match is the single most expensive mistake in
   retail finance, and roughly one in five eligible workers does it
   anyway.

2. **The HSA is the only triple-tax-advantaged wrapper.** Deductible
   going in, growth tax-free, withdrawals tax-free for qualifying
   medical expenses. Save the receipts and reimburse yourself decades
   later and the HSA functions as a stealth Roth IRA with a deduction
   on top.

3. **The Roth-vs-Traditional choice compounds for 30+ years.** Pick
   wrong and the cost is 10-20% of your terminal wealth. The decision
   reduces to one comparison: **your current bracket vs. your expected
   retirement bracket.** Get that comparison right and the rest is
   bookkeeping.

4. **The order matters more than the level.** Two identical earners
   contributing the same total dollars get *different* terminal wealth
   if they fund the wrappers in a different order. The interactive on
   the website ranks the stack and tells you the marginal dollar's
   home.

Horace's deeper view — "tax via options and margin" — sits beneath
this entire lesson: every dollar that lands inside the
right wrapper is a dollar the IRS *cannot* tax, ever, at the right
endpoint. The stack is the cheapest alpha you will ever find — written
into the code, public, mechanical.

![Pyramid diagram of the 2026 contribution priority stack: tier 1 employer match, tier 2 HSA $4,300, tier 3 Roth IRA $7,000, tier 4 401(k) max $23,500, tier 5 mega-backdoor up to $70,000 total, tier 6 taxable brokerage. Each tier sized by typical annual dollar amount with the priority number on the left.](../image/side11_account_stack.png)

---

### 2. What You Need to Know

#### 2.1 The 2026 Contribution Limits — One Page

Every wrapper has a **separate** annual limit. Filling all of them is
not double-counting; it is the optimal stack.

| Wrapper | 2026 limit | 50+ catch-up | Income limit? |
|---|---|---|---|
| 401(k) employee deferral | $23,500 | +$7,500 = $31,000 | none |
| 401(k) total (incl. match + after-tax) | $70,000 | +$7,500 = $77,500 | none |
| IRA (Traditional or Roth) | $7,000 | +$1,000 = $8,000 | Roth phases out $165-180k single / $246-256k MFJ |
| HSA, single coverage | $4,300 | +$1,000 at 55+ | HDHP required |
| HSA, family coverage | $8,550 | +$1,000 at 55+ | HDHP required |
| 457(b) (govt / non-profit) | $23,500 | +$7,500 | sometimes stackable with 401(k) |

Two operational notes. First, the **catch-up** (age 50+) is allowed
only if your plan permits it; almost all do for the 401(k), the IRA
catch-up is statutory. Second, the **HSA** requires you to be enrolled
in a High-Deductible Health Plan (HDHP). If your employer offers a
PPO and an HDHP, the HDHP usually pairs with an HSA — and most years,
for healthy savers under 50, the HDHP plus maxed HSA is the
mathematically dominant choice.

The total 401(k) cap of $70,000 — sometimes called the §415 limit —
is the most under-used dollar in the code. It includes your $23,500
employee deferral, your employer match, and any after-tax non-Roth
contributions your plan permits. The space between (deferral + match)
and $70,000 is the **mega-backdoor Roth lane**: contribute after-tax
dollars into the gap, immediately convert to Roth via in-service
rollover, and another $30,000-$45,000 per year flows into the tax-free
wrapper that is otherwise capped at $7,000.

#### 2.2 Traditional vs. Roth — The Single Decision That Matters

Every wrapper in the stack is one of two flavours.

**Traditional (tax-deferred).** Pre-tax going in (deduction today),
tax-deferred growth, taxed as ordinary income on withdrawal. Think:
"tax break now, pay later."

**Roth (tax-free at the back end).** Post-tax going in (no deduction
today), tax-free growth, tax-free withdrawals after 59½ and a
five-year holding window. Think: "pay now, never again."

The fundamental decision is bracket arbitrage. Hold today's $1 of
contribution constant; the after-tax wealth at retirement is:

$$ W_{\text{Roth}} = (1 - t_{\text{now}}) \cdot (1 + r)^{N} $$

$$ W_{\text{Trad}} = (1 + r)^{N} \cdot (1 - t_{\text{ret}}) $$

The two are **algebraically identical when $t_{\text{now}} =
t_{\text{ret}}$**. Roth wins when your retirement bracket is higher;
Traditional wins when your retirement bracket is lower. The image
below makes the parity visible.

![Bar chart showing terminal after-tax wealth at age 65 from $7,000 per year contributed for 30 years at 7% growth, comparing Roth and Traditional outcomes across four current = retirement bracket scenarios (12, 22, 32, 37 percent). The two columns are equal in every scenario, illustrating the parity condition; an additional panel shows divergence when current and retirement brackets differ by 10 percentage points.](../image/side11_roth_vs_trad.png)

Three working rules.

- **High earner, expecting to spend down hard in retirement → Trad.**
  A 37% bracket today and a 22% bracket at 70 (after Social Security,
  no wages) is a 15-percentage-point arbitrage. Take the deduction
  now, pay the lower rate later.
- **Young, modest income, expecting to be richer later → Roth.** A
  22% bracket at 28 with a 32% expected bracket at 50 is the inverse
  arbitrage. Pay now while the rate is low, lock in tax-free growth
  forever.
- **Don't know? Split.** A 50/50 Roth/Traditional 401(k) hedges the
  uncertainty. The split also gives you "tax diversification" — in
  retirement you choose which bucket to draw from based on each
  year's bracket.

The often-overlooked bonus for Roth: **no Required Minimum
Distributions during the original owner's lifetime**. A 75-year-old
with $2M in Traditional IRAs is forced to withdraw roughly $80,000
each year (taxed at ordinary rates), regardless of need. The same
$2M in a Roth IRA can sit untouched, compounding tax-free, and pass
to heirs. For high-net-worth households, the no-RMD feature alone
tilts the math toward Roth even at parity brackets.

#### 2.3 The Optimal Contribution Stack — Six Tiers

The image at the top of this lesson is the cheat sheet. The logic
under each tier is what makes it stick.

**Tier 1 — Capture the employer 401(k) match in full.** The most
expensive mistake in retail finance is leaving match dollars on the
table. A typical formula is "50% match on the first 6% of salary"
(a 3% gift if you contribute 6%) or "100% match on the first 4%."
Whatever your formula, the marginal return on the dollar that
captures the last bit of match is 50-100% *guaranteed*. No
investment beats that. Even if you have credit-card debt, even if
your plan's fund menu is mediocre, *capture the match first*.

**Tier 2 — Max the HSA if you have an HDHP.** Triple-tax-advantaged.
$4,300 single / $8,550 family in 2026. Pay for current medical out of
cash flow when possible, save the receipts, and let the HSA
compound. After 65 the HSA can be withdrawn for *any* purpose at
ordinary rate (like a Traditional IRA), with the medical-tax-free
option preserved indefinitely. There is no other wrapper in the
code with this profile.

**Tier 3 — Max the Roth IRA (or backdoor it).** $7,000 a year. If
your income is above the phaseout ($165,000-$180,000 single in 2026),
the **backdoor Roth** route still works: contribute non-deductible
to a Traditional IRA, immediately convert to Roth, pay zero tax on
the (zero) gain. The catch is the **pro-rata rule** — if you have
existing pre-tax balances in any Traditional IRA, the IRS treats
every conversion as a proportional mix of pre-tax and after-tax
across all your IRAs. The fix is to roll any pre-tax IRA balances
into your current 401(k) first, leaving the Traditional IRA empty
for the backdoor operation.

**Tier 4 — Max the 401(k) employee deferral up to $23,500.** Whether
you contribute to the Traditional or Roth bucket within the 401(k)
follows §2.2's bracket logic. The employer match always lands in the
Traditional bucket regardless of your election.

**Tier 5 — Mega-backdoor Roth, if your plan permits.** Verify two
plan features: (a) after-tax (non-Roth) employee contributions are
allowed above the $23,500 deferral, and (b) **in-service Roth
rollover** is allowed (sometimes called "in-plan Roth conversion").
If both are present, contribute up to (Total Cap − Deferral − Match)
in after-tax dollars and immediately convert. Math example: $70,000
total cap − $23,500 deferral − $11,500 match = **$35,000 mega-backdoor
lane**. That is $35,000 a year flowing into a Roth wrapper that the
IRA's $7,000 limit would otherwise cap.

**Tier 6 — Taxable brokerage.** The wrappers are full. Now
asset-location and tax via options become the levers.
Side Lesson 4 covers this layer.

The stack is **strict priority**: empty Tier 1 before opening Tier 2,
empty Tier 2 before Tier 3, etc. The interactive on the website
allocates a user-supplied annual cash-flow figure across all six
tiers in this order and reports the projected after-tax wealth at 65.

#### 2.4 The Backdoor and Mega-Backdoor in Detail

**Backdoor Roth IRA (high-income earners).** Required when your
income exceeds the Roth IRA direct-contribution phaseout.

1. Contribute $7,000 (or $8,000 if 50+) **non-deductible** to a
   Traditional IRA. There is no income limit on non-deductible
   Traditional contributions.
2. Convert the entire balance to a Roth IRA, ideally within days of
   the contribution and before any gains accrue.
3. File Form 8606 with your tax return to document the
   non-deductible basis.

The conversion is taxable on any pre-tax basis or accrued earnings;
zero in the clean case. The pro-rata rule (§2.3) makes this messy if
you have other pre-tax IRA balances — clean those out first by
rolling into a 401(k) that accepts incoming rollovers.

**Mega-backdoor Roth (plan-dependent).** A separate operation that
uses the §415 total cap.

1. Verify your 401(k) plan supports **after-tax non-Roth**
   contributions and **in-service rollovers** (look at the SPD or
   call HR).
2. After hitting the $23,500 employee deferral, instruct payroll to
   contribute additional **after-tax** dollars up to the gap between
   (deferral + match) and $70,000.
3. Configure an **automatic in-plan Roth conversion** so each
   after-tax contribution flips to Roth on the next pay cycle. If
   automatic isn't available, do quarterly manual conversions to
   minimise pre-conversion gains.

A plan that allows the mega-backdoor has effectively raised your
annual Roth contribution ceiling from $7,000 to $30,000-$45,000.
For high earners, this is the largest single-wrapper opportunity in
the code.

#### 2.5 The 5-Year Rules (Plural) and Roth Conversion Ladders

There are **two distinct five-year rules** for Roth IRAs, and they
trip up almost everyone.

**Rule A — the five-year holding period for *earnings*.** Before age
59½, your Roth contributions can be withdrawn anytime tax- and
penalty-free. The *earnings* on those contributions are a different
story: to withdraw earnings tax-free, the Roth IRA must be at least
five years old (measured from the *first* Roth contribution to *any*
Roth IRA you own — once the clock starts, it never resets). Otherwise
earnings withdrawals before 59½ are taxable plus 10% penalty.

**Rule B — the five-year holding period for *converted amounts*.**
Each Roth *conversion* starts its own five-year clock. Withdrawing a
converted amount before five years have passed (and before 59½)
triggers the 10% early-withdrawal penalty on the conversion principal.

**Roth conversion ladder.** A retirement-distribution strategy that
exploits Rule B. Steps:

1. Retire early, say at age 50. Begin annual Roth conversions of
   ~$50,000 from your Traditional IRA, paying ordinary income tax on
   each conversion (in the low income-window of early retirement).
2. Wait five years for each conversion to "ripen." A conversion done
   at 50 is withdrawable penalty-free at 55. A conversion done at 51
   is withdrawable at 56. And so on.
3. Starting at age 55, withdraw the *converted principal* annually,
   tax- and penalty-free. (You already paid tax at conversion; it's
   Roth dollars now.)
4. By 59½ all rules collapse — everything in the Roth is fully
   accessible tax- and penalty-free regardless of conversion date.

This is the standard FIRE-movement bridge between early retirement
(50-59) and traditional retirement-account access (59½+). The 5-year
ladder transforms a "locked until 59½" Traditional IRA into spendable
cash starting at 55.

#### 2.6 Required Minimum Distributions (RMDs) — The Back-End Tax

For Traditional 401(k)s and Traditional IRAs, the IRS eventually
collects. **SECURE Act 2.0** (passed 2022) raised the RMD age:

- Born 1951-1959: RMDs begin at **age 73**.
- Born 1960 or later: RMDs begin at **age 75**.

The annual required amount is your prior-year-end balance divided by
the IRS Uniform Lifetime Table life-expectancy factor. At 75 the
factor is ~24.6, so the RMD is roughly **4.1% of the balance** that
year, rising to about 6.1% at 85 and 10% at 92. RMDs are taxed at
ordinary rates.

**Roth IRAs have no RMDs during the owner's lifetime.** Roth 401(k)s
also no longer have RMDs as of 2024 (a SECURE 2.0 change). Inherited
Roth IRAs do have a 10-year payout rule for non-spouse beneficiaries,
but the distributions are still tax-free.

**Penalty for missing an RMD.** SECURE 2.0 lowered the penalty from
50% (savage) to **25%** (still savage), reducible to 10% if corrected
within two years. Set a calendar reminder on December 1st of every
RMD year.

---

### 3. Common Misconceptions

**Misconception 1: "The 401(k) and IRA limits are combined; I can
only contribute one or the other."**

False. They are *separate* limits. A 50-year-old in 2026 can
contribute $31,000 to a 401(k) *and* $8,000 to an IRA in the same
year, totalling $39,000 across the two wrappers — plus HSA, plus
mega-backdoor.

**Misconception 2: "Roth always wins because tax-free growth is
better than tax-deferred."**

It is the same number when current bracket = retirement bracket. The
algebra in §2.2 is exact. Roth wins only when retirement bracket is
*higher* than current bracket.

**Misconception 3: "I make too much for a Roth IRA."**

The income phaseout blocks *direct* Roth contributions. The backdoor
Roth (§2.4) is fully legal and has been blessed by Congress (the 2018
TCJA technical-corrections language explicitly acknowledged it). Most
high earners are using it.

**Misconception 4: "The 401(k) match goes into my Roth bucket if I
elect Roth."**

No. The employer match always lands in the **Traditional** (pre-tax)
bucket regardless of your contribution election. You will pay
ordinary tax on the match dollars at withdrawal.

**Misconception 5: "I should max my 401(k) before capturing the
match — I'll get to the match anyway."**

No. The match is per-paycheck in most plans, with no annual true-up.
If you front-load contributions and hit the $23,500 cap by July, you
forfeit the match for the rest of the year. Spread contributions
across the full 12 paychecks to capture every match dollar.

**Misconception 6: "The HSA is just for medical expenses; I should
use it as a checking account for prescriptions."**

The HSA is an *investment account* with optional medical-expense
withdrawal. Pay current medical out of pocket if your cash flow
allows, save the receipts, let the HSA compound for 30 years, and
reimburse yourself the receipt amount at any time tax-free. The
optimal use of the HSA is to *not* spend it.

**Misconception 7: "Mega-backdoor is only for tech bros at FAANGs."**

It depends on whether your plan supports after-tax contributions and
in-service rollovers. Many plans do (read the SPD or call HR), and
the share is rising as more plans adopt the feature. Public-sector
and small-business plans tend to lack it; mid-large corporate plans
often have it.

**Misconception 8: "I'll convert everything to Roth in retirement."**

Each conversion is taxable as ordinary income in the year of
conversion. Converting $500,000 of Traditional IRA in a single year
will push almost all of it into the 32-37% bracket, plus IRMAA
Medicare surcharges, plus possibly state tax. The mechanical rule is
**convert only enough to fill the next bracket edge each year** —
spread over a decade if needed.

**Misconception 9: "If I leave my employer I lose the 401(k) money."**

Your own contributions are 100% vested (yours forever). The employer
match may be on a vesting schedule (typically 3-6 years graded or
cliff). On separation you can leave the 401(k) where it is, roll it
to your new 401(k), or roll it to an IRA. Don't *cash it out* — that
triggers ordinary tax + 10% penalty + the loss of decades of
compounding.

**Misconception 10: "Roth conversions in retirement are pointless;
I'll never spend the converted amount."**

The point is to **drain the Traditional balance into the Roth wrapper
before RMDs hit at 75**. Each conversion in your low-bracket years
60-74 reduces the future RMD denominator. A $100,000 conversion at 65
in the 22% bracket costs $22,000 in tax and removes ~$4,100/year of
mandatory ordinary-rate withdrawals starting at 75.

---

### 4. Q&A

**Q1: My 401(k) has a $23,500 employee limit and a $70,000 total
cap. What happens between those numbers?**

That gap is the **after-tax non-Roth contribution** lane. If your
plan permits it, you can contribute additional after-tax dollars up
to the total cap, then immediately convert each contribution to Roth
via in-service rollover (the mega-backdoor). If the plan doesn't
permit it, the gap is filled only by employer contributions.

**Q2: I'm 28 and in the 22% bracket. Roth or Traditional 401(k)?**

Almost certainly Roth. At 28 your wage trajectory probably points up,
and 22% is near the bottom of the schedule. Lock in tax-free growth
now while the rate is cheap. Reconsider when your bracket crosses 32%.

**Q3: I'm 52, in the 32% bracket, with $1.5M in a Traditional 401(k)
and $250k in cash. Anything I should be doing?**

Three things. (a) Continue maxing the 401(k) at 32% — Trad probably
right given your bracket. (b) Add $8,000/year to a backdoor Roth IRA.
(c) Investigate whether your plan permits the mega-backdoor —
$35,000+ a year of after-tax-to-Roth at your stage materially
changes the retirement tax picture.

**Q4: I have an old 401(k) from a previous employer and a Traditional
IRA. How do I do a clean backdoor Roth?**

Roll the *Traditional IRA* (and any pre-tax balances) into your
*current* 401(k) first. Most plans accept incoming rollovers from
both other 401(k)s and IRAs. Once your Traditional IRA balance is
zero, the backdoor (non-deductible Traditional contribution +
immediate conversion) is clean: pro-rata applies to a $7,000 base of
$7,000 = 0% taxable.

**Q5: My wife stays home with the kids; can she contribute to an IRA?**

Yes. The **Spousal IRA** rule lets a non-working spouse contribute up
to the IRA limit ($7,000, or $8,000 if 50+) using the working
spouse's earned income, as long as the couple files jointly and the
working spouse has at least that much earned income. The spousal IRA
can be Traditional or Roth, subject to the same income phaseouts.

**Q6: Can I use a Roth IRA to buy a house?**

You can withdraw your **contributions** (not earnings) at any time,
tax- and penalty-free. Additionally, $10,000 of *earnings* can be
withdrawn for a "first-time" home purchase (defined liberally — no
home in the prior 2 years counts) tax- and penalty-free, provided
the Roth has been open at least 5 years. Above that, the early-
withdrawal rules apply.

**Q7: I'm self-employed. What's my retirement-account stack?**

The two main wrappers are the **Solo 401(k)** (employee deferral
$23,500 + employer profit-sharing up to 25% of net SE income, total
cap $70,000 — same as a regular 401(k)) and the **SEP-IRA** (up to
25% of net SE income, capped at $70,000, no separate employee
deferral). Self-employed individuals often pair a Solo 401(k) with a
backdoor Roth IRA. The HSA still applies if you have an HDHP.

**Q8: I'm in a high-tax state (CA, NY, NJ). Does that change the
math?**

Slightly. State income tax adds 5-13% to the ordinary rate,
amplifying the gap between current and retirement brackets *if* you
plan to retire in a no-tax state (FL, TX, NV, WA, TN, NH, SD, WY,
AK). A Californian at the 32% federal + 9.3% state bracket retiring
to Florida arbitrages **9.3 percentage points of state tax** by
choosing Trad over Roth and *also* by deferring conversions until
after the move. Tax-domicile planning is a real lever.

**Q9: At age 75 I'm forced to take RMDs from my Traditional IRA but
I don't need the cash. What do I do?**

Two clean options. (a) Take the RMD as a **Qualified Charitable
Distribution (QCD)** — direct from the IRA to a qualified charity,
counts toward the RMD, and is *excluded from your AGI*. The 2026 QCD
limit is roughly $108,000. (b) Take the RMD as cash, pay the tax,
and reinvest in a taxable brokerage account using Side Lesson 4's
asset-location playbook.

**Q10: What's the actual after-tax benefit of contributing to a 401(k)
match instead of just a taxable account?**

For a 32% bracket worker contributing $5,000 with a 100% match, here
are the dollar paths over 30 years at 7% growth, after-tax at 32%
ordinary withdrawal:

- **Match'd Trad 401(k):** $10,000 contributed → $76,123 future
  value × (1−0.32) = **$51,764**
- **Taxable instead:** $5,000 (after-tax already) → contributing
  $5,000 in taxable, growing at ~5.5% net of tax drag → **$24,800**

The match alone *doubles* the lifetime after-tax outcome. Capture
it.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Retirement Accounts, the Complete Stack — 401(k), IRA, Roth, HSA, and the Optimal Order
**RUNTIME TARGET:** ~13 minutes (side-lesson length)
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Stella:** Welcome back. This is Side Lesson 11. I'm Stella, and
today we're walking through every retirement-account wrapper in the
US tax code, the 2026 contribution limits, and the order in which
you should fund them.

**Horace:** This is the cheapest alpha on this channel. The IRS
publishes the rules. You don't need to predict anything. You don't
need to pick a stock. You follow a six-tier stack and the wrappers
do the work.

**Stella:** And the difference between the right order and the wrong
order, over a 30-year career, is six figures.

**Horace:** Easily. Let's start with the limits.

---

**[SECTION 1: THE 2026 LIMITS — 0:50]**

**Horace:** Five wrappers, separate limits.

**Stella:** 401(k), employee deferral — $23,500. If you're 50 or
older, $31,000.

**Horace:** IRA, Traditional or Roth — $7,000. $8,000 if 50+.

**Stella:** HSA — $4,300 single, $8,550 family. You need an HDHP to
contribute.

**Horace:** And the total 401(k) cap, including employer match and
after-tax contributions — $70,000. That's the §415 limit. Most
people don't realise that number even exists.

**Stella:** They're separate, by the way. You can max all of them in
the same year. A 50-year-old maxing 401(k) plus IRA plus HSA family,
without the mega-backdoor, is shoveling $47,500 into tax-advantaged
wrappers in 2026.

**Horace:** With the mega-backdoor, the cap goes to roughly $85,000
before you start hitting taxable. The wrappers are big.

---

**[SECTION 2: ROTH VS. TRADITIONAL — 2:00]**

[VISUAL: image/side11_roth_vs_trad.png]

**Stella:** This is the one decision that matters. Pull up the
chart.

**Horace:** Four scenarios, current bracket equals retirement
bracket — 12, 22, 32, 37 percent. Roth column and Traditional column.
Starting with $7,000 a year, 30 years, 7% growth.

**Stella:** And in every single bracket, the two columns are equal.

**Horace:** Mathematically identical. That's the parity result. If
your current bracket equals your retirement bracket, Roth and
Traditional give you the same after-tax dollars at the back end.

**Stella:** The right panel shows what happens when they diverge. If
your retirement bracket is 10 points lower than today, Traditional
wins by 10-15%. If it's 10 points higher, Roth wins.

**Horace:** Three working rules. High earner, expecting to spend
down hard in retirement — Traditional. Young, low bracket, expecting
to be richer later — Roth. Don't know — split fifty-fifty.

**Stella:** And one bonus for Roth — no Required Minimum
Distributions during your lifetime. At 75, a Traditional IRA forces
roughly 4% of the balance out every year, taxed at ordinary rates.
Roth doesn't force anything. For high-net-worth households, that
no-RMD feature alone tilts the math toward Roth even at parity.

---

**[SECTION 3: THE STACK — 4:30]**

[VISUAL: image/side11_account_stack.png]

**Horace:** Six tiers. Strict priority. Empty tier 1 before tier 2.

**Stella:** Tier 1 — capture the employer 401(k) match in full. If
your formula is "50% on the first 6% of salary," contribute exactly
6% to capture the maximum match. That's a 50% guaranteed return on
the marginal dollar. Nothing else in finance pays that.

**Horace:** Tier 2 — max the HSA if you have an HDHP. Triple-tax-
advantaged. $4,300 single, $8,550 family. The HSA is the only
wrapper that's deductible going in, tax-free growing, *and* tax-free
coming out for medical. Save the receipts. Reimburse yourself
decades later. It functions as a stealth Roth IRA with a deduction
on top.

**Stella:** Tier 3 — max the Roth IRA. $7,000, or $8,000 if 50+. If
your income is above $165,000 single in 2026, use the backdoor: non-
deductible Traditional contribution, immediate conversion to Roth.
Watch the pro-rata rule.

**Horace:** Tier 4 — max the 401(k) deferral up to $23,500. Pick
Traditional or Roth bucket using the bracket logic from section 2.

**Stella:** Tier 5 — mega-backdoor. If your plan permits after-tax
non-Roth contributions and in-service rollovers, fill the gap
between $23,500 plus your match and the $70,000 total cap. That's
typically another $30,000 to $45,000 a year flowing into the Roth
wrapper.

**Horace:** Tier 6 — taxable brokerage. The wrappers are full. Now
asset location and tax via options become the levers. Side Lesson 4
covers that layer.

---

**[SECTION 4: THE INTERACTIVE — 7:30]**

[VISUAL: interactive/side11_account_optimizer.html]

**Stella:** Pull up the optimiser on the website.

**Horace:** Six inputs. Age, salary, employer match percentage,
current bracket, expected retirement bracket, and your available
annual cash flow for retirement savings.

**Stella:** Output — the dollar amount that goes into each tier in
the right order, the total annual contribution captured, the
employer match captured, and the projected after-tax wealth at age
65.

**Horace:** Try a 35-year-old engineer making $200,000 with a 4%
employer match in the 32% bracket, expecting 22% in retirement, with
$50,000 a year available to save.

**Stella:** Tier 1, $8,000 to capture the match. Tier 2, $4,300 to
the HSA. Tier 3, $7,000 to backdoor Roth. Tier 4, $15,500 more to
the Traditional 401(k) to hit $23,500. Tier 5, $15,200 to mega-
backdoor if available. Total wrapper-side contribution, $50,000 — no
taxable bucket needed this year. Projected wealth at 65, roughly $5
million after-tax.

**Horace:** Move the bracket assumptions and the dollar allocations
to Trad versus Roth shift in real time. Move the salary up to
$300,000 and the match capture goes up. The interactive is the
calculator I want everyone to run before December 31st of every
year.

---

**[SECTION 5: THE 5-YEAR RULES AND THE LADDER — 10:00]**

**Stella:** Two five-year rules for Roth, and they're different.

**Horace:** Rule A — five years from your first Roth contribution
before earnings can be withdrawn tax-free. Once the clock starts, it
never resets.

**Stella:** Rule B — each Roth conversion has its own five-year
clock. Withdrawing converted principal before five years and before
59½ triggers the 10% penalty.

**Horace:** And the Roth conversion ladder — Rule B in action.
Retire at 50. Convert $50,000 a year from Traditional to Roth,
paying ordinary tax in your low-income early-retirement years. Each
conversion ripens five years later. Starting at 55, you withdraw the
conversion principal tax- and penalty-free. By 59½ all rules
collapse.

**Stella:** That's the standard FIRE-movement bridge between early
retirement and traditional account access. Convert at 50, spend at
55. Repeat for nine years.

---

**[SECTION 6: RMDs — 11:30]**

**Horace:** Required Minimum Distributions. Traditional 401(k) and
Traditional IRA force you to take money out — and pay ordinary tax —
starting at age 73 if you were born 1951-1959, or age 75 if you were
born 1960 or later.

**Stella:** SECURE Act 2.0 raised the age. Roth IRAs have no RMDs
during the owner's lifetime. Roth 401(k)s no longer have RMDs as of
2024.

**Horace:** Annual amount is roughly 4.1% of the balance at 75,
rising to 6% at 85. Penalty for missing an RMD is 25%, reducible to
10% if you correct within two years. Set a December 1st calendar
reminder.

**Stella:** And for households with large Traditional balances, the
years between retirement and 75 are a Roth conversion window — drain
the Traditional balance into the Roth wrapper at low brackets before
RMDs hit at full force.

---

**[OUTRO — 12:30]**

**Horace:** Three operational takeaways. One — the limits are
separate, not combined. Max all of them. Two — Roth versus
Traditional is one comparison: current bracket versus expected
retirement bracket. Three — fund the wrappers in the order on the
chart, strictly.

**Stella:** And the bonus — every dollar inside a Roth
wrapper is a dollar the IRS will *never* tax again at the right
endpoint. The stack is the cheapest alpha on this channel. Run the
optimiser, plug in your numbers, and you'll have a one-page action
list for December 28th of this year.

**Horace:** See you next time.

**[END — 13:00]**
