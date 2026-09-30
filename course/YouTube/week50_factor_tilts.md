## Part 2: YouTube Script

---

**VIDEO TITLE:** Factor Tilts in Practice — What Vanguard, iShares, and Avantis Actually Deliver
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00-1:00]**

**Stella:** Hey everyone, welcome to Week 50. Today we're closing out the factor investing arc. Week 23 was the academic version — Fama-French, Carhart, the long-short premia. Today is the ETF aisle at Vanguard.

**Horace:** Right. Week 23 was the math. Week 50 is the bill. There's a gap between the two and most retail investors do not realise how big it is. So today we're going to do three things. First, the post-publication decay — what happens to a factor premium after the paper gets published. Second, the seven retail ETFs people actually buy — VTI, VTV, VBR, MTUM, QUAL, USMV, AVUV. Third, how to put them together as a core + tilt.

**Stella:** And we'll end with the honest answer about how much alpha factor tilts actually buy you in 2026. Spoiler — it's smaller than the marketing material says. But it's real.

**Horace:** Mmm. Smaller than they say, bigger than zero. That's most of finance.

---

**[SECTION 1 — POST-PUBLICATION DECAY — 1:00-4:00]**

**Stella:** Let's start with the McLean-Pontiff result from 2016.

**Horace:** OK. McLean and Pontiff took 97 published anomalies, looked at the in-sample performance, then looked at what those same anomalies did after the paper was published. The drop was dramatic. Average premium fell by about 26% from in-sample to post-publication. Out-of-sample-and-post-publication, it fell by about 58%.

**Stella:** So roughly half the headline number disappeared.

**Horace:** Roughly half. And Hou-Xue-Zhang in 2020 — they replicated 452 anomalies — found that 65% of them did not even clear a t-statistic of 3 once you stripped out microcap stocks and equal-weighting tricks.

**Stella:** Why did the decay happen?

**Horace:** Three things at once. First, factor ETFs launched. iShares MTUM in 2013, USMV in 2011, the Vanguard suite in 2018. That brought retail capital to the trade. Second, transaction costs collapsed — decimalisation in 2001, then commission-free trading by 2019. Hedge funds could harvest the same premia at a fraction of the friction Fama and French faced. Third, the long-short capital chasing factors exploded. AQR alone runs about 140 billion dollars across factor strategies.

**Stella:** So the trades got crowded.

**Horace:** Crowded, cheaper to put on, and more competitive. The result is that any factor premium published in a 2003 paper — by 2026 you should expect about half of it to persist.

**Stella:** And that means if you size a factor tilt to the in-sample backtest, you're going to be disappointed.

**Horace:** Crucified. Look at value investors from 2010 to 2020. The HML premium ran negative 4.7% per year in that window. Twelve years of underperformance. Anyone who sized to the 1963-2003 magnitude lost their nerve by year 7 and missed the 2022 snapback.

---

**[SECTION 2 — THE SEVEN RETAIL ETFS — 4:00-9:00]**

**[VISUAL: image/week50_factor_etfs_perf.png]**

**Stella:** Let's go through what you can actually buy. Show the chart.

**Horace:** This is cumulative growth of one dollar from January 2014 through April 2026 in seven ETFs. VTI is the reference — that's the core US total market index, three thousand seven hundred stocks, three basis point expense ratio. The black line.

**Stella:** And then we have six factor tilts.

**Horace:** Right. VTV is Vanguard large-value, four bps. VBR is Vanguard small-value, seven bps. MTUM is iShares momentum, fifteen bps. QUAL is iShares quality, fifteen bps. USMV is iShares min-volatility, fifteen bps. And AVUV is Avantis small-value, twenty-five bps — that one only launched in September 2019.

**Stella:** Look at the spread. AVUV runs away in the late period. MTUM and QUAL beat VTI. USMV trails. VTV and VBR — pure value — trail VTI substantially despite the 2022 snap.

**Horace:** Three observations from this chart. First, single-factor tilts are regime-dependent. USMV did its job in 2018 — it lost less than VTI when VTI dropped. It did its job in 2022 — same story. Then in 2021 it trailed by a lot because high-vol won. That's the trade. You accept tracking error to get drawdown protection.

**Stella:** Second observation?

**Horace:** Momentum and quality beat the market in this window. That's not luck — both factors had multi-year tailwinds. But MTUM had a brutal 2022, down 17% versus VTI down 19% — basically no protection — and a deep relative drawdown in 2016 around the value rotation.

**Stella:** Third?

**Horace:** AVUV. Look at the slope from 2020 onward. Avantis added a profitability screen on top of small-value indexing. The Asness-Frazzini-Israel paper from 2018 showed that profitability-filtered small-value is materially better than pure small-value. AVUV has earned roughly 2 percentage points per year over VBR since launch. The 18 basis point ER differential is paid back many times over.

**Stella:** But the sample is short.

**Horace:** Six and a half years. So treat that 2 percentage point edge as evidence, not gospel.

**Stella:** OK. Let's talk about the implementation gap. Why does VTV give you less than the academic HML?

**Horace:** Six layers of friction. The academic factor is long the cheapest 30%, short the most expensive 30%. VTV is long the cheaper 50% of large-caps, no short side. So the long-only ETF captures roughly 0.5 to 0.7 of the long-short premium just from removing the short leg.

**Stella:** What else?

**Horace:** The universe is narrower — Russell 1000 versus the full NYSE-AMEX-NASDAQ in academic factors. That excludes microcaps, which is where the early SMB premium lived. Rebalance is quarterly or annual versus monthly in academia. And the methodology has cap-weight overlays and buffer rules to keep turnover down. All of that dilutes the exposure.

**Stella:** So what's the realised premium expectation after all that?

**Horace:** If HML's 1963-2024 was 3.8% per year, after the post-publication decay haircut you're looking at maybe 1.9% gross. After the long-only conversion you're at roughly 1.0% to 1.5% per year for a VTV-vs-VTI tilt. That's the real number.

**Stella:** That is much smaller than the brochure number.

**Horace:** Much smaller. But still positive in expectation. Still worth a sleeve, sized appropriately.

---

**[SECTION 3 — CORE + TILT CONSTRUCTION — 9:00-13:00]**

**[VISUAL: image/week50_core_tilt_grid.png]**

**Stella:** OK so how do we actually put this in a portfolio. Show the grid.

**Horace:** Six candidate constructions over 2014 through April 2026. 100% VTI as the baseline. Three 80/20 single-factor tilts — value via VTV, momentum via MTUM, small-value via AVUV. A 60/40 multi-factor with VTI plus four sleeves equal-weight. And an equal-weight all-seven blend.

**Stella:** What jumps out?

**Horace:** Three things. First, the 80/20 MTUM led on annualised return — momentum had two strong years inside the sample, 2017 up 37% and 2024 up 32%. Second, the 60/40 multi-factor delivered the best Sharpe — 0.60 versus 0.56 for 100% VTI. That's the textbook diversification result — own a basket of factors, eat the average premium with less of any single factor's variance. Third, 100% VTI was near the bottom on Sharpe and *last* on drawdown depth.

**Stella:** Last on drawdown depth meaning the deepest drawdown.

**Horace:** Right. VTI drew down about 20% in 2022. The factor blends trimmed that to 12 to 17%. The equal-weight blend cut it nearly in half. Modest. Real.

**Stella:** The honest reading is that none of these blends crushed VTI.

**Horace:** None of them crushed it. The best blend beat VTI on Sharpe by maybe 10 to 15 basis points. That's the post-decay reality. **If you cannot beat 100% VTI by at least 10% on Sharpe over a full cycle, the tilt is not worth the complexity.**

**Stella:** So what's the canonical Level 4 retail core + tilt?

**Horace:** Roughly this — 70% VTI core, then 10% AVUV, 8% MTUM, 6% QUAL, 6% USMV. Total factor sleeve 30%.

**Stella:** Why those weights?

**Horace:** AVUV gets the biggest tilt because the profitability screen has the most credible incremental edge. Momentum gets a meaningful slot because it diversifies value — momentum and value are the classic negatively correlated pair. Quality and low-vol are smaller because their realised premia post-decay are in the 1 to 2% range.

**Stella:** Expected uplift?

**Horace:** 30 to 50 basis points per year over 100% VTI. With tracking error of 3 to 4% per year. Information ratio around 0.10 to 0.15.

**Stella:** That's small.

**Horace:** That's the truth. Anyone selling factor tilts as a 2 to 3% per year uplift is selling the in-sample backtest, not the post-decay expectation.

---

**[SECTION 4 — SIZING AND DISCIPLINE — 13:00-15:30]**

**Stella:** Let's do sizing rules. You said three.

**Horace:** Rule one — size the tilt to half the academic premium. If the paper says 4%, expect 2%. Apply that to the sleeve weight to get expected portfolio uplift.

**Stella:** Rule two?

**Horace:** Annual rebalance. Not quarterly, not when it feels right. Calendar-based, every January, with tolerance bands of plus-or-minus 5 percentage points around target weights. Annual is the sweet spot — captures multi-year mean reversion without paying transaction cost on multi-month trends.

**Stella:** And rule three.

**Horace:** Five-year stop. If a factor tilt has a rolling 5-year information ratio below zero against VTI, and you cannot articulate a *structural* reason — meaning something has changed about the factor's source of return — cut the tilt by half. Not by 100%. Half. Factor decay is path-dependent. The factor that just had a 5-year drought is also the factor most likely to mean-revert.

**Stella:** That's a hard rule to follow. Selling at the bottom is psychologically brutal.

**Horace:** It's not selling at the bottom. It's reducing risk after the thesis has been weakened by half a decade of evidence. If the factor never returns, you've cut your loss. If it mean-reverts, you still have half the position.

**Stella:** What about asset location?

**Horace:** Factor sleeves go in IRA where possible. They have higher turnover than VTI — 5 to 30% versus 3 to 5%. That distributed capital gain in a taxable account is a 20 to 40 basis point per year tax drag for a 30% sleeve at a 32% bracket. Move it to IRA, the drag goes to zero. Location-not-allocation.

**Stella:** And the interactive — let me plug it.

**Horace:** Yeah. Below this video on the lesson page is the tilt builder. Seven sliders, one per ETF. Sum to 100. It runs a 2014-2024 monthly backtest and reports CAGR, vol, Sharpe, max drawdown. Try the 100% VTI line first — that's your baseline. Then try a 70/30 with whatever factor mix you like. See how hard it is to beat the baseline by a meaningful Sharpe margin.

---

**[SECTION 5 — THE BARBELL READ AND OUTRO — 15:30-18:00]**

**Stella:** Where do factor tilts fit in the barbell view?

**Horace:** Two answers. For a Level 1 to 3 portfolio — Weeks 8 through 36 — factor tilts are the wrong tool. The 30 to 50 basis point uplift does not justify the operational complexity, the rebalance discipline, or the tracking error psychology. Use 100% VTI or VOO core. Save the cognitive bandwidth for the things that matter more — savings rate, asset location, debt paydown.

**Stella:** And for Level 4?

**Horace:** A 20 to 30% factor sleeve is one of the few "active" trades that survives the default-passive filter. *Because* the post-decay premium is positive, supported by economic theory, and implementable in long-only ETFs at low cost. Even here, the right sizing is small. Factor tilts complement the alpha sleeve — long-vol, options overlays, trend following — they do not replace it.

**Stella:** The honest summary.

**Horace:** Real, but small. Big enough to justify a 20 to 30% sleeve in a Level 4 portfolio. Small enough that the discipline of rebalance and the willingness to hold through 5-year droughts matter more than the choice of factor mix.

**Stella:** Alright. Three takeaways.

**Horace:** One — post-publication decay is real. Roughly half the in-sample premium persists. Size accordingly.

**Stella:** Two — long-only retail ETFs deliver about 0.5 to 0.7 of the academic factor exposure. So the realised premium expectation, after the decay haircut and the long-only conversion, is roughly 1.0 to 1.5% per year per factor.

**Horace:** Three — core + tilt is the right architecture. 70% VTI core, 30% factor sleeve diversified across two to four factors, annual rebalance, IRA-located, with a 5-year information ratio stop. Expected uplift is 30 to 50 basis points per year. Information ratio of 0.10 to 0.15.

**Stella:** And the meta-lesson.

**Horace:** Alpha is rare and hard-won. Most "factor alpha" sold at retail is repackaged beta. The genuine post-decay premium is real, small, and earned by the discipline of holding through the bad years. Same lesson as the rest of this course.

**Stella:** Next week — Week 51 was managed futures, this is the wrap of the factor arc. See you in Week 51's review section. Bye!

**Horace:** Bye.

---
