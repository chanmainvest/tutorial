# Review: course/side02_10k_filing.md

## Overall Assessment

This is a high-value practical lesson. It teaches a real retail edge: disciplined filing reading, EDGAR search, risk-factor comparison, and segment analysis. The Apple example is concrete and likely useful for students.

The lesson needs legal/disclosure precision. It currently treats the 10-K as closer to sworn truth than it really is and repeatedly assumes the first three risk factors are ordered by severity. That rule is too strong and could teach students to skip important disclosure.

## Content Critique

- The lesson's core promise is excellent: retail investors can improve interpretation even without faster data.
- `The SEC requires a public company to tell the truth` and `closest thing... to a sworn deposition` are rhetorically strong but legally too clean. 10-Ks are certified and liability-bearing, but they still contain estimates, omissions, boilerplate, judgment, and sometimes fraud.
- `The information is identical to what hedge funds get` should be narrowed: the 10-K itself is identical; hedge funds may also use expert networks, channel checks, paid databases, alt data, and management access within legal limits.
- `It is the only place where the bad news lives` is too strong. Bad news may first appear in 8-Ks, press releases, litigation dockets, regulator notices, short reports, product data, or later restatements.
- The lesson repeatedly says the first three risk factors are ordered by severity. This is not reliable enough as a rule. Risk factors are often grouped by category and legal drafting convention, not strictly ranked. Better: read the first few, the newly added/changed ones, and the company-specific ones.
- `A 4.02 8-K almost always precedes a stock-price collapse` overstates the base rate. It is serious, but the outcome depends on materiality, timing, and remediation.
- `Going concern... almost every 10-K... followed by bankruptcy, dilutive equity raise, or distressed restructuring within 18 months` needs sourcing or softening.
- Apple Services gross margin is discussed as `60-plus percent versus 35-ish for iPhone`. Apple reports Products gross margin, not iPhone-specific gross margin; avoid implying iPhone gross margin is disclosed directly.
- The `20-F is less detailed` statement is too broad. It is less timely and can use IFRS/home-country frameworks, but many 20-Fs are very detailed.
- The lesson should add a mini-workflow for diffing risk factors year over year, because that is the real edge.

## Structure And Formatting Issues

- The lesson follows the course structure and decimal numbering.
- The two static visuals are well chosen: 10-K anatomy and Apple segments.
- Add a one-page `10-K reading checklist` visual or downloadable worksheet.

## YouTube Script Critique

The video script has strong retention potential because it promises a concrete skill: reading a 10-K in 45 minutes.

Specific issues:

- `The 10-K is sworn disclosure and where the truth lives` should become `where management is most legally constrained`.
- The first-three-risk-factors rule should be revised in the script.
- The script says the interactive `pulls up the most recent 10-K from EDGAR`; the interactive mostly uses hardcoded snapshot data plus an EDGAR link.
- `That alone is an edge` is a good line, but should be framed as a process edge, not guaranteed alpha.

## Chart And Interactive Feedback

`side02_10k_navigator.html` is useful and visually clear, but it needs stronger data labeling.

Issues:

- The company data is embedded and static, with a comment saying sources are most recent 10-Ks as of April 2026. The UI should show this visibly.
- The EDGAR button opens a form-filtered company page, not necessarily the exact filing used for the embedded data.
- Risk-factor text appears summarized by the course, not quoted. This is fine, but should be labeled as author summaries.
- Because the interactive is static, the script should not imply live pulling or automatic updates.
- The `top 3 risk factors` framing should be changed to `selected high-priority risk factors` unless exact order and source text are verified.

## SOUL Consistency Flags

- Strong alignment with SOUL's view that rare retail alpha can come from slow, disciplined reading.
- Needs less certainty around filings as truth and more emphasis on skeptical interpretation.
- Good fit for retail advantage: no benchmark pressure, time to read, no need to trade immediately.
