# Review: course/week08_financial_statements.md

## Overall Assessment

Week 8 is practical, investor-focused, and well placed after the portfolio-construction basics. The strongest idea is the twenty-minute reading sequence: revenue trend, operating margin, FCF versus net income, net debt/EBITDA, and capital allocation. That gives students an actual workflow instead of drowning them in accounting vocabulary.

The lesson should tighten a few accounting claims. "Cash is fact" and "revenue is hard to fake" are directionally useful, but both can be manipulated through timing, working capital, receivables, supplier finance, factoring, channel stuffing, and classification choices. The lesson should teach students to trust cash flow more than earnings, but not treat cash flow as magically fraud-proof.

## Content Critique

- The opening is strong: if you cannot read the statements, you are reading a translation of a translation.
- The four investor questions are excellent. Consider repeating them at the end as the core checklist.
- The statement-linking section is clear and should be retained. "Movie / photo / cash bridge" works well.
- The Apple waterfall is a good choice because it shows a high-quality business converting more cash than accounting profit.
- "Revenue is the single hardest line to fake" is too broad. Revenue fraud is one of the classic accounting fraud categories. Better: revenue is central and heavily audited, but still must be checked against receivables, cash collection, deferred revenue, and customer concentration.
- The balance-sheet section should distinguish goodwill from identifiable intangibles. Internally generated brand value is generally not on the balance sheet under US GAAP unless acquired; acquired intangibles and goodwill are different lines/concepts.
- The current-ratio rule needs sector caveats. Some excellent businesses operate with negative working capital; some retailers and subscription businesses can have current ratios below 1 without immediate distress.
- Net debt/EBITDA is useful, but teach that it fails for banks, insurers, early-stage companies, and highly cyclical EBITDA peaks.
- "Free cash flow is what the business could return to all capital providers" needs precision. OCF minus capex is often closer to free cash flow to equity after interest; free cash flow to the firm is a different construct.
- The statement "cash flow is a fact" should be softened. Operating cash flow is harder to fake than earnings, but it can be flattered by working-capital timing, supplier financing, factoring receivables, and underinvesting in capex.
- "Alpha sources include look at cash, not earnings" does not appear as a named SOUL alpha source. Treat this as an accounting-quality discipline rather than a core alpha source unless SOUL.md is updated.
- The stock-based compensation misconception is excellent. It protects students from one of the most common tech-stock accounting traps.

## Cross-Reference And Consistency Issues

- The YouTube end screen says "Next: Week 9 — Equity Valuation Foundations," but Week 9 is Understanding Market Indexes.
- Q9 correctly says valuation begins Week 21 onward, which conflicts with the end-screen implication that valuation is next.
- This is another example of YouTube outro/end-screen drift and should be included in the global audit.

## Presentation Improvements

- Add a "20-minute investor pass" worksheet with five rows and blank fields.
- Add a red-flag table: revenue up but receivables up faster; net income up but OCF flat; buybacks funded by debt; goodwill growing through serial acquisitions; SBC excluded from adjusted EBITDA.
- Add a separate bank warning box earlier. JPM is included in the examples, but banks really are a different accounting animal.
- Add a mini case comparison: high-quality cash converter versus accounting-quality warning sign.
- Add a balance-sheet quality checklist: debt maturity wall, cash, working capital, goodwill, pension/lease obligations.
- Add a "do not use this ratio for" line under current ratio, net debt/EBITDA, and FCF/revenue.

## YouTube Script Critique

The script is clear and useful, but it needs more tension. Financial statements can easily feel like homework; the hook should be about catching the lie before the market does.

Specific improvements:

- Open with a mini mystery: "Company reports record earnings, stock falls 40%. The clue was in cash flow."
- Let Stella ask the beginner question: "Why not just trust EPS?" Horace can then show the Apple EPS/FCF chart.
- Use the Apple waterfall as the main visual. It is concrete and not too abstract.
- Add one fraud/quality example, but keep it short: Enron, Wirecard, or a generic receivables warning.
- The script says four lines, but the reading sequence later gives five checks. Harmonize this: either four key lines plus capital allocation, or five-step pass.
- Fix the next-week end screen.

## Chart And Visual Feedback

Existing visuals are useful:

- Apple waterfall is excellent for connecting income statement to cash flow.
- EPS versus FCF per share chart is a strong accounting-quality visual.
- Common-size table is good but static.

Recommended upgrades:

- Three-statement bridge diagram: net income -> retained earnings; net income -> OCF; capex -> PP&E; debt issuance -> cash/liabilities.
- Accounting red-flag dashboard with green/yellow/red examples.
- Receivables versus revenue growth chart as a classic revenue-quality warning.
- SBC dilution chart: GAAP expense, adjusted EBITDA add-back, share count dilution.
- Debt maturity wall visualization.

## Interactive Demo Feedback

The existing `course/interactive/week08_statement_explorer.html` is useful for comparing Apple, Coca-Cola, and JPMorgan across revenue, net income, OCF, and FCF. It includes common-size FY2024 tables, profile summaries, multilingual labels, and theme support.

Suggested improvements:

- Add balance-sheet metrics. The lesson promises IS, BS, and CF, but the interactive mostly covers IS/CF. Add current ratio, debt, cash, net debt/EBITDA, equity, goodwill/intangibles.
- Add a three-statement view rather than one metric at a time. Students should see net income and OCF/FCF together.
- Add red-flag mode: highlight years where net income and FCF diverge, or revenue grows faster than cash flow.
- Add source/date notes for the hardcoded data.
- For JPM, instead of showing FCF as n/a only, provide bank-specific metrics such as ROTCE, net interest margin, efficiency ratio, and provision for credit losses.
- Add a downloadable/checklist-style reading sequence that students can apply to any company.

## New Interactive Demo Ideas

- 10-K guided reader: click Item 7, Item 8, Item 1A, notes; see what investor question each section answers.
- Quality-of-earnings detector: input revenue, receivables, NI, OCF, capex, SBC; output likely red flags.
- Common-size comparator: pick two companies and compare margins, FCF conversion, debt, and capital allocation side by side.
- Debt maturity wall builder: enter maturities/rates and see refinancing risk under different rate scenarios.
- Adjusted earnings reconciler: start with GAAP net income and toggle common adjustments, including SBC, restructuring, impairment, and acquisition amortization.

## Make It More Entertaining Without Watering It Down

Make financial statements feel like forensic reading. The student is not doing accounting for school; they are reading the company's own confession. The entertainment should come from finding the one line that contradicts management's story.

## Money-Making Usefulness

This lesson helps students make money by avoiding low-quality earnings, debt traps, and fake growth. The highest-impact addition would be a repeatable one-page checklist for every single-stock investment.

## SOUL Consistency Flags

- Good support for SOUL principle #1: if you cannot identify mispricing, you do not have an edge.
- The phrase "alpha sources include look at cash, not earnings" should be reframed unless Horace wants to add it to SOUL.md as a formal alpha source.
- Good alignment with the course's professional-toolkit layer: this is orthodox CFA material translated for retail investors.
- Fix the Week 9 end-screen mismatch.
