# Review: course/side11_retirement_accounts.md

## Overall Assessment

This is a valuable practical lesson for US readers. The wrapper stack, match-first logic, HSA explanation, backdoor Roth overview, five-year-rule section, and RMD section all address decisions that can materially improve household wealth.

The lesson needs more tax-law precision and stronger jurisdiction labeling. It is almost entirely US-specific, so it should not read like universal retirement advice on a multilingual global course site.

## Content Critique

- Add `as of` source labels for every 2026 limit: 401(k), IRA, Roth phaseout, HSA, QCD, §415 cap, catch-up amounts, and RMD ages.
- The 2026 limits look like known 2025 values in several places. If they are projections, label them as projections; if official, cite the IRS notice.
- The lesson says high-earner households can shelter six figures of `pre-tax income`, but mega-backdoor Roth and Roth IRA dollars are after-tax. Rephrase to `tax-advantaged savings capacity`.
- HSA guidance is good, but `HDHP plus maxed HSA is mathematically dominant` is too broad. Premiums, employer HSA contributions, family health needs, out-of-pocket max, and risk tolerance matter.
- Roth-vs-Traditional parity is the biggest conceptual risk. The formulas are correct only when comparing the same pre-tax dollar or assuming Traditional tax savings are invested. A chart comparing `$7,000 per year` into Roth versus `$7,000 per year` into Traditional is not parity under the same cash-flow burden.
- The Roth contribution limit can make Roth economically larger when the investor can pay tax from outside dollars. The lesson should separate `tax-rate arbitrage` from `wrapper-space arbitrage`.
- The no-RMD Roth advantage is real for high-net-worth and estate-planning cases, but `tilts the math toward Roth even at parity` should be caveated because the tax cost still matters.
- Employer match treatment is outdated/too absolute. SECURE 2.0 allows some plans to make employer matching contributions as Roth if the plan permits; many plans still default to pre-tax, but `always Traditional` is no longer universally true.
- The strict stack overstates Tier 3 before Tier 4. For high earners in 32%-37% brackets, maxing Traditional 401(k) may outrank a backdoor Roth IRA depending on expected retirement bracket, state tax, and available cash.
- `Capture the match even with credit-card debt` needs a liquidity/interest-rate/vesting caveat. Usually true, but not absolute.
- The backdoor Roth section should mention SEP/SIMPLE/pre-tax IRA balances in the pro-rata rule and year-end aggregation.
- The `blessed by Congress` wording for backdoor Roth needs source precision or softer language.
- Mega-backdoor explanation is good, but should state that both after-tax contributions and either in-plan Roth conversion or in-service distribution must be allowed, and plan fees matter.
- Roth five-year rules need tighter wording. After age 59.5, conversion-principal penalty rules differ from the Roth earnings five-year qualification rule; `by 59.5 all rules collapse` is too broad if the Roth IRA has not satisfied the earnings five-year clock.
- Inherited Roth IRA distributions are generally tax-free only if qualified/five-year rules are satisfied; otherwise nuance is needed.
- RMD section should note the 1959 birth-year ambiguity/IRS clarification if using precise SECURE 2.0 cutoffs.
- QCDs are available starting at age 70.5, not only when RMDs begin, and the QCD limit needs an as-of source.
- Self-employed Solo 401(k) contribution math should distinguish 25% of W-2 compensation for an S-corp owner from roughly 20% of net self-employment income after the self-employment-tax adjustment.
- Q10 match-versus-taxable math should define the cash-flow basis. A `$5,000` pre-tax 401(k) deferral is not the same out-of-pocket cost as `$5,000` invested in taxable after tax.

## Structure And Formatting Issues

- The reading section follows the correct numbered-section convention.
- Because this lesson is US-specific, the introduction should include a visible `US tax system only` note and suggest non-US readers map the concept to their local pension/tax wrappers.
- Add a compact annual checklist: December 1 match check, HSA receipt archive, Form 8606, backdoor pro-rata check, true-up check, RMD/QCD check.
- Add a decision tree for Roth vs Traditional that includes state-tax move, RMD risk, estate goals, and current cash-flow constraints.

## YouTube Script Critique

The script is practical and has a good promise: `cheapest alpha` is a strong hook. The two-host pacing is clearer than many earlier side lessons.

Needed fixes:

- Clarify that this is US-account content before listing the stack.
- Fix the Roth-vs-Traditional parity explanation so the visual and spoken example compare equal pre-tax dollars or explicitly invest the Traditional tax savings.
- The `with mega-backdoor, cap goes to roughly $85,000` line needs a precise filing-age/family-HSA assumption.
- The interactive walkthrough says total wrapper contribution is `$50,000`, but the optimizer includes employer match and would show a higher total annual contribution under its KPI definition.
- Add a retention beat before the limits: `The most expensive investment mistake is not a bad stock; it is failing to press the free-match button.`

## Chart And Interactive Feedback

`side11_account_optimizer.html` is useful and matches the lesson's central workflow, but it should be labeled as a simplified educational optimizer, not an optimal recommendation engine.

Issues:

- Match modeling assumes a 100% match formula where employee contribution required equals employer match percentage. Common formulas such as 50% on the first 6% require different math.
- HSA is hard-coded to single coverage and ignores family coverage, employer HSA contributions, and age-55 HSA catch-up.
- Roth IRA phaseout uses salary, not MAGI, and has no filing-status selector.
- Mega-backdoor is always available in the optimizer; it needs a plan-permits toggle.
- The model has no 457(b), Solo 401(k), SEP-IRA, spouse IRA, state-tax, vesting, employer true-up, or high-earner Roth-catch-up rule.
- It assumes constant salary, constant savings, constant tax brackets, constant limits, and a fixed 7% return to age 65. Those assumptions should be visible near the output, not only in the caption.
- It treats HSA as fully Roth-like without asking whether the household has enough qualified medical expenses/receipts.
- The strict-priority algorithm should allow a `high current bracket` mode where Traditional 401(k) max can outrank backdoor Roth.

## SOUL Consistency Flags

- Strong alignment with the SOUL emphasis on after-tax return management.
- Calling tax wrappers `cheapest alpha` is effective, but the lesson should clarify that this is legal tax-efficiency alpha, not market alpha.
- The lesson should tie the stack back to portfolio tranches: tax-inefficient income/REIT/bond/premium strategies benefit most from sheltered accounts; qualified-dividend and broad-equity sleeves can often tolerate taxable placement.
