## Part 2: YouTube Script

---

**VIDEO TITLE:** Factor Investing in 2026 — Value, Momentum, Quality, Low-Vol, Size, and Why the Premium Halved
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

[INTRO]

**Stella:** Welcome back. Today we're doing the topic that probably
launched more PhD theses in finance than any other one — factor
investing. Value, momentum, quality, low-vol, size. The five flavours
your wealth manager has been pitching at you, plus market beta, plus
the academic framework that ties them together.

**Horace:** And we're doing it with a hook the textbooks don't lead
with. The premium on every one of these factors has *roughly halved*
since 2003. Half. Compressed. The thing that worked for Fama and
French in their 1992 paper still works in 2026, just at half the
size. We're going to look at why, and what to do about it.

**Stella:** Three things on this episode. One — what factors actually
are, mathematically. Two — the historical premium of each, and the
post-2003 decay story that nobody on the sell-side wants to dwell on.
Three — a hands-on factor-blender lab where you can build your own
multi-factor portfolio and backtest it against the Fama-French data
1963 to 2024.

**Horace:** And as always, where this fits the broader framework.
Factors are alpha lane number five — the structural one. They belong
in your passive core, *not* in your active book. By the end of the
episode you'll know how much of your portfolio should be in factor
ETFs and how much shouldn't.

[VISUAL: image/week23_factor_premia.png]

---

[SECTION 1: WHAT A FACTOR ACTUALLY IS]

**Horace:** Let's start with the definition because it's surprisingly
clean. A factor is not a kind of stock. A factor is a *long-short
portfolio*. You take every US stock, you rank them on some
characteristic — say book-to-market — go long the cheapest decile,
short the most expensive decile, hedge out the market, rebalance
monthly. The monthly P&L of that long-short portfolio is the value
factor. HML, in Fama-French notation. High Minus Low.

**Stella:** And the same construction applies to all of them.

**Horace:** Same construction every time. Rank, long top, short
bottom, equal-weight legs, monthly rebalance. Size is small minus
big — SMB. Momentum is up minus down — UMD. Profitability is robust
minus weak — RMW. Investment is conservative minus aggressive — CMA.
Plus the market factor itself, MKT minus the risk-free rate.

**Stella:** Six factors total in the modern framework.

**Horace:** Five Fama-French plus momentum, which Mark Carhart bolted
on in '97. That's the framework that explains roughly 90% of the
cross-section of US equity returns in 2026. Not 100% — there's still
residual stuff. But 90% means the typical "stock picker's alpha" is
actually a factor exposure with a fancier name.

**Stella:** Let's pull up the chart of historical premia.

[VISUAL: image/week23_factor_premia.png]

**Horace:** This is annualised long-run premium per factor, July 1963
through end of 2024. Market is the biggest at 6.6%, which makes sense
— it's the equity risk premium, the one CAPM was built on. Then
momentum at 7.5% — the only one bigger than market.

**Stella:** Momentum has the biggest factor premium of any of them?

**Horace:** And the biggest drawdown. We'll get to that. After
momentum, value at 3.8%, then investment at 3.3%, profitability at
3.0%, and size at the bottom around 2.4%. Notice size is the
*smallest* premium even though it's the factor that started the
whole literature in 1981 with Banz's paper.

**Stella:** Why is size the smallest?

**Horace:** Two reasons. One, most of the realised "small-cap
premium" turns out to be a small-*value* premium when you double-rank
on size and book-to-market. Size on its own is barely there. Two,
microcap illiquidity makes the academic measurement unreliable —
you can't actually trade the bottom of the size distribution at the
prices the long-short uses.

[SECTION 2: THE FACTOR DECAY STORY]

**Horace:** Now the part that doesn't show up on the BlackRock
marketing deck. Every one of these premia has *compressed* since
2003. Roughly halved.

[VISUAL: image/week23_factor_decay.png]

**Stella:** This is rolling 10-year mean of HML and UMD.

**Horace:** Right. The blue line is HML — the value factor's rolling
10-year premium, ending year by year. From the 1970s to about 2002,
that line averages 4 to 6%. Then it falls off a cliff. The rolling
10-year ending 2020 is *negative*. Negative. The academic value
factor lost money on average across the 2010s.

**Stella:** And the orange line — momentum.

**Horace:** Momentum's a different shape. The factor has a long-run
mean of 7-8%, and you can see that's where it sits for most of the
history. But notice the cliff in 2009. That's the momentum crash —
the 2009 single-year UMD drawdown was roughly 45% as the market
V-bottomed off the GFC lows and the previously-losing junk stocks
ripped higher. One year ate the next decade.

**Stella:** Why are all the premia compressing?

**Horace:** Three theories, all probably true. First — *publication
arbitrage*. The moment a factor gets written up in the Journal of
Finance, capital flows in to harvest it, the long leg gets bid up,
the short leg gets sold down, and the spread compresses. The
peer-reviewed paper is the obituary of the trade. Second —
*intangibles*. Book-to-market is a 1963 measure designed for an
industrial economy. It penalises asset-light tech firms whose value
is in non-capitalised R&D, brand, network effects. HML reads them as
"expensive" when on a corrected basis they're not. Third —
*central-bank liquidity*. Zero rates compress dispersion. Everything
trades together. Nothing is cheap or expensive any more.

**Stella:** So is factor investing dead?

**Horace:** It's not dead. It's smaller. The premium is still
positive — just half what it was. And the cost of harvesting it has
dropped even faster than the premium. In 2003 you paid a hedge fund
2-and-20 to run leveraged factors. In 2026 you click QUAL or AVUV
for 15 to 25 bps. So the *net* premium to the retail investor is
roughly the same as the *net* premium to the hedge-fund client was
in 2003. Cheap beta ate expensive alpha.

[SECTION 3: THE 2007 QUANT QUAKE]

**Horace:** Brief callback to Week 14 because it matters here. The
canonical case study in factor crowding is the August 2007 quant
quake.

**Stella:** Walk us through it.

**Horace:** Every leveraged long-short shop in 2007 — AQR, Renaissance,
Goldman GEO, dozens of mid-tier — was running essentially the same
factor portfolio. Long value, long momentum, long quality, short the
opposites. Levered five to eight times for risk-target purposes.
Then the week of August 6, somebody — probably a multi-strat fund
forced to deleverage to meet redemptions in their credit book —
started unwinding the standard factor portfolio in size.

**Stella:** And because everyone owned the same book —

**Horace:** Nobody on the other side. By Friday August 10 the
standard quant factor portfolio was down 25%. Three years of premium,
gone in four days. The S&P moved one percent. Retail never noticed.

**Stella:** What's the lesson for retail factor investing in 2026?

**Horace:** The blow-up was a *leverage* and *redemption* story, not
a factor story. Unleveraged retail factor ETFs don't have daily
VaR-driven stop-outs. They can sit through a quant unwind and just
take the temporary mark. The risk to retail is *forgone return*
— factors compress further — not catastrophic loss.

[SECTION 4: THE 2026 RETAIL ETF MENU]

**Stella:** Let's run the menu.

**Horace:** Five tickers cover the main factors, total ER under 25
bps. VLUE for value at 8 bps. MTUM for momentum at 15 bps. QUAL for
quality at 15 bps. USMV for low-vol at 15 bps. AVUV for combined
small-value-quality at 25 bps. IWM or IJR for size at 19 or 6 bps.

**Stella:** A retail investor can replicate the entire FF5+momentum
framework for under 20 basis points all-in?

**Horace:** Easily. And here's the bigger-picture angle. Factors are
the structural mispricing alpha lane — the academic factor premium
is the most arbitrageable subset. They
belong in tranche one or tranche two of your portfolio. The passive
core, with maybe a 10-30% tilt to factors. They do *not* belong in
your active concentrated book. The reason they pay less than they
used to is precisely because they're the easy lane — the lane that
doesn't require discomfort, doesn't require holding through hated
positions, doesn't require being early. Anything that easy gets
arbed.

**Stella:** And anything that requires discomfort —

**Horace:** Stays paying. That's why "buying what passive flows have
abandoned" — the contrarian sector trade, week 16 territory — is
still a 5%+ alpha lane while the academic factor portfolios are at
2-4%. Discomfort is the moat.

[SECTION 5: THE LAB]

**Stella:** Let's go to the interactive.

[VISUAL: course/interactive/week23_factor_blender.html]

**Horace:** Five sliders — your weights to MKT, SMB, HML, UMD, RMW.
The constraint is they have to sum to 100. The lab embeds the annual
Fama-French series 1963 to 2024 — 62 years of data — and runs your
chosen blend through it. Output is cumulative wealth, max drawdown,
Sharpe ratio.

**Stella:** And there are presets.

**Horace:** Four. Pure Value — 100% HML. Pure Momentum — 100% UMD.
Quality plus Low-Vol — equal-weight RMW and a low-vol proxy. And
GMO 60/40-style — Jeremy Grantham's classic value-tilt blend.

**Stella:** Click pure value first.

**Horace:** Now look at what happens. Wealth grows nicely from 1963
to 2007. Then the line goes flat. Twelve years of dead money.
That's the rolling-10-year HML decay we showed earlier in the
chart.

**Stella:** Now pure momentum.

**Horace:** Beautiful upward line — and a nasty 2009 cliff. The 45%
calendar drawdown is right there in the wealth curve. One year ate
five years.

**Stella:** Now the GMO blend — 50% market, 30% value, 10% quality,
10% momentum.

**Horace:** Smoother. Sharpe is better than any single-factor sleeve.
That's the point. The factors aren't perfectly correlated, so a
blend gets diversification on top of the average premium. Value and
momentum in particular are *negatively* correlated — when one's
suffering the other is usually doing fine. That's the most useful
pairing for a retail blend.

**Stella:** What's your recommended allocation for somebody starting
fresh in 2026?

**Horace:** Sixty percent in VTI as the cap-weighted core. Then ten
percent each in AVUV, MTUM, QUAL, USMV. Total ER under 12 bps,
exposure to all six factors at modest weights, cap-weighted core
dominant. Annual rebalance, hold for a decade-plus, don't sell when
one of the tilts is having a bad five years. That's the discipline
the strategy requires.

**Stella:** And if somebody can't sit through a five-year drawdown
of one of their tilts?

**Horace:** Don't tilt. Own VTI. The factor premium isn't worth
selling at the bottom and missing the rebound. If you can't hold
through pain, the cap-weighted index is the better product for you.

[OUTRO]

**Stella:** Recap. Factors are long-short portfolios built from
ranked stock characteristics. The Fama-French 5 plus momentum
explains 90% of the cross-section. Long-run premia: market 6.6%,
momentum 7.5%, value 3.8%, investment 3.3%, profitability 3.0%, size
2.4%. All of them have compressed since 2003 — roughly halved — for
publication-arbitrage and intangibles-mismeasurement reasons. The
2007 quant quake was about leverage and redemptions, not factors per
se. Retail factor ETFs in 2026 deliver the academic premium at under
25 bps. Use them as a 10-30% tilt on a cap-weighted core, not as a
replacement for it.

**Horace:** And the structural-alpha framing. Factors are the
structural alpha lane — the most systematic, the most scalable, and
the most arbed.
They belong in your passive core. The lane that pays *more* — the
lane the academic literature can't write a clean paper about — is the
contrarian one. Buying what passive flows have abandoned. We did that
in week 16 with sectors and we'll do it again in later weeks.

**Stella:** Next week we move from factor investing to the broader
question of style boxes — large-versus-small, growth-versus-value,
and the 9-cell Morningstar grid that organises most of the US equity
mutual fund universe. See you there.
