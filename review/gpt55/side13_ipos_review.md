# Review: course/side13_ipos.md

## Overall Assessment

This is a strong, useful anti-hype lesson. It teaches the right instinct: retail investors usually do not receive the IPO first-day pop; they pay it. The SPAC structure explanation is also valuable and fits the course's `alpha is rare` philosophy.

The lesson needs return-definition cleanup, several factual updates, and major alignment fixes between the reading, YouTube script, and interactive.

## Content Critique

- Source/date labels are needed for IPO counts, first-day pop averages, one-year underperformance, lock-up effects, IPO ETF returns, SPAC returns, redemption rates, and direct-listing examples.
- The lesson mixes offer-price, first-day open, first-day close, benchmark-relative return, absolute return, one-year return, and three-year return. Standardize definitions before presenting averages.
- Opening claim says day-one buyers underperform by about `10 percentage points` over the next year, but the chart path from `1.18` open to `0.90` offer-relative implies roughly `-24%` absolute from the retail open before any benchmark comparison.
- §2.3 says average IPO underperformance is `-10% three-year cumulative` with half in the first year, which conflicts with the one-year `-10 percentage points` framing.
- The first-day pop is not `18% of day-one market cap` left on the table. Money left on the table is based on shares sold in the offering times the first-day price change.
- The underwriter-franchise description is directionally right, but `never carry inventory risk` is too strong. Firm-commitment underwriters do take deal/stabilization risk, even if the allocation/pricing process manages it heavily.
- Sell-side quiet-period language needs verification. The old `25 days` framing may be stale after JOBS Act/FINRA rule changes.
- `Retail allocations under 10%` and `IPO access mostly fills cold deals` need source/date labels.
- The Renaissance IPO ETF comparison needs source/date and methodology. Clarify whether SPACs are included/excluded and whether returns are NAV total return.
- SPAC section should mention post-2024 SEC SPAC/deSPAC rule changes and the reduced safe-harbor/projection landscape.
- `PIPE investors usually get $8 or $9` is too broad; many PIPEs were priced at `$10`, while others included discounts, incentives, or forward-purchase structures.
- Direct listing section has factual issues. Slack was not bought for only `$26.79 cash equivalent`; Salesforce paid `$26.79` cash plus Salesforce stock per Slack share.
- `No first-day pop` for direct listings should be rephrased. There is no offer-price allocation pop, but the opening auction can still trade above the reference price.
- Direct listings do not universally have no lock-up; some had modified lock-up mechanics.
- `Wait six months` is a good rule, but the claim that expected return from open to six months is roughly zero conflicts with the lesson's own average path and lab assumptions.
- `Paying down debt is bad` in S-1 use-of-proceeds guidance is too broad; paying down expensive debt can improve solvency and equity value. Insider cash-outs and vague corporate purposes are the bigger flags.
- Q9 Roth IRA placement for IPO bets conflicts with the scarce-Roth-space caveat from Side 04. High variance alone is not enough; expected return and probability of permanent loss matter.
- Misconception 8 says spin-offs are covered in their own side lesson, but the visible side-lesson list does not show a spin-off lesson.

## Structure And Formatting Issues

- Section numbering is correct.
- The lesson is persuasive but sometimes too rhetorically hot. Keep the edge, but make the data definitions boringly precise.
- Add a `return definition box`: offer-to-open, open-to-close, close-to-12-month, benchmark-relative, ETF proxy.
- Add a `SPAC capital stack diagram`: trust cash, sponsor promote, public warrants, redemptions, PIPE, post-merger common.
- Add an S-1 checklist table with valuation, revenue quality, dilution, related-party transactions, lock-up schedule, customer concentration, insider selling, and use of proceeds.

## YouTube Script Critique

The cold open is excellent. It dramatizes the exact behavior the lesson wants to prevent.

Needed fixes:

- The first segment's P&L explanation is confusing. If the allocated investor buys at `1.00` and the terminal price is `0.90`, that investor is down 10% unless they sold into the first-day pop. Separate `flip at open` from `hold one year`.
- The interactive walkthrough says pop `+18%`, drift `-10%`, horizon `12 months`, capital `$10,000` produces allocated `$10,620` and retail `$9,000`. The current lab formula would produce very different numbers.
- The script says the day-one retail buyer is down roughly 24% from `1.18` to `0.90`, but Q10 says retail finishes at about `$9,000` on `$10,000`. Reconcile.
- The SPAC segment uses very strong language. It is engaging, but the data should be precise enough that the rhetoric does not carry the evidence.
- Replace the final `IPO window is for traders` wording with the repository-standard `investors` framing unless discussing actual short-term trading behavior.

## Chart And Interactive Feedback

`side13_ipo_lab.html` teaches the allocation/open-price gap well, but it is currently inconsistent with the reading and script.

Issues:

- Default preset is `2024 avg (+12%)`, but the caption says empirical anchor is `+18%`.
- The lab's terminal calculation is `capital x terminal price / entry price`. With default `+18%` pop and terminal `0.90`, allocated ends at `$9,000` and retail at about `$7,627`, not the script's `$10,620` and `$9,000`.
- The lab does not model benchmark-relative return, even though the reading emphasizes underperformance versus the broad market.
- It does not model an allocated investor selling into the pop versus holding for a year. That distinction is central.
- It forces the path toward `0.90` offer-relative at month 12 for most presets, making the hot/meme presets look deterministic rather than scenario-based.
- Add controls for `allocated flip percentage`, `market benchmark return`, `lock-up month`, `secondary offering`, and `SPAC/deSPAC mode`.
- Add source/date labels for the empirical anchors and a `stylized model` warning.

## SOUL Consistency Flags

- Strong alignment with SOUL's no-penny-stock / no-subscale-casino-tier rule and its skepticism toward crowded retail excitement trades.
- The lesson correctly distinguishes the retail investor's edge from underwriter/institutional allocation advantages.
- Keep the orthodox IPO mechanism and empirical base rates first, then mark Horace's sub-billion/no-IPO rule as his implementation discipline.
