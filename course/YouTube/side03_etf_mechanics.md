## Part 2: YouTube Script

---

**VIDEO TITLE:** Why VTI and VTSAX Are the Same Fund But Pay Different Tax | Side Lesson 3

**RUNTIME TARGET:** ~11 minutes

**HOSTS:**
- **Horace** (teacher): Holding a printout of an ETF prospectus.
- **Stella** (student): Default-passive index investor, taxable account.

---

**[INTRO -- 0:00]**

[VISUAL: Animated logo "Side Lesson 3 -- ETF Mechanics"]

**Horace:** Stella. You own VTI in your brokerage account, right?

**Stella:** Yeah. Like every default-passive person on the
internet told me to.

**Horace:** Good. And your friend who has a Vanguard account
directly -- she owns VTSAX?

**Stella:** Same fund, basically.

**Horace:** Same *portfolio*. Same fee. Same manager. Same
trades. *Different tax outcome over twenty years* -- a few
thousand dollars on a 100,000 starting balance for VTSAX
specifically (which is unusually efficient because Vanguard's
patent lets it share an ETF share class), and tens of thousands
for a typical active mutual fund. The difference comes down to
one structural thing -- in-kind versus cash redemptions -- that
nobody talks about because it sounds like plumbing. Let me show
you.

---

**[SEGMENT 1 -- TWO MARKETS, ONE ETF -- 0:50]**

[VISUAL: image/side03_creation_redemption.png on screen]

**Horace:** Every ETF is two markets stitched together. You see
the **secondary** market on Robinhood -- buy from another
investor, cash for shares, like a stock. The ETF issuer is *not
involved* in that trade.

The **primary** market is hidden. About thirty large
broker-dealers -- Goldman, Citadel Securities, Virtu, Jane
Street -- sign agreements with Vanguard or BlackRock that make
them **Authorized Participants**, APs. Only they can talk
directly to the fund.

**Stella:** And what do they do?

**Horace:** Two things. *Creation*: when VTI is trading above
NAV, an AP buys the basket of underlying stocks, hands the
basket to Vanguard, gets new VTI shares back, and sells them on
the exchange at the premium. The premium is the AP's profit.

*Redemption*: the reverse. When VTI is trading below NAV, the AP
buys VTI cheap on the exchange, hands the shares to Vanguard,
gets the basket of stocks back, sells the basket at fair value.
The discount is the AP's profit.

**Stella:** So they keep VTI's price pinned to its NAV.

**Horace:** Right. And the magic word is "in kind." When the AP
hands over the basket, no cash changes hands between the AP and
Vanguard. That detail is the entire reason VTI is more
tax-efficient than VTSAX. Hold that thought.

---

**[SEGMENT 2 -- THE iNAV TICK -- 2:00]**

**Horace:** While all this is happening, the exchange publishes
an **iNAV** every 15 seconds -- a model estimate of the basket
value updated continuously. It is the reference point against
which the bid and ask are checked. When VTI's price drifts more
than a basis point from iNAV, an AP shows up. The whole loop is
automated and completes in seconds.

**Stella:** And I do not see any of this from my brokerage.

**Horace:** Correct. You see the spread on the order book. The
spread is *thin* -- a basis point -- *because* the AP machinery
is running underneath. Take it away and ETF prices would drift
like closed-end funds.

---

**[SEGMENT 3 -- THE TAX TRICK -- 3:15]**

[VISUAL: image/side03_etf_vs_mf_tax.png on screen]

**Horace:** Now the part that puts dollars in your pocket.

A mutual fund -- VTSAX -- when an investor sells, the fund
sells some stocks to raise cash. Those sales realise capital
gains *inside* the fund. The IRS requires the fund to push those
gains out to *all remaining shareholders* by year-end as a
capital-gain distribution. Loyal long-term holders get a tax
bill they did not ask for.

**Stella:** That sounds awful.

**Horace:** It is. It is the structural flaw of the open-end
mutual fund.

ETFs sidestep it. Look at this chart -- same portfolio, same
fee, 100k invested in 2005, taxable account at a 20% combined
LTCG rate. After twenty years VTI is a few thousand dollars
ahead of VTSAX -- about half a percent of terminal wealth. That
looks small because VTSAX is *itself* unusually tax-efficient
(it shares a share class with VTI under Vanguard's structure).
For a typical *active* mutual fund the same exercise produces
tens of thousands of dollars of drag.

**Stella:** Where does that come from?

**Horace:** Section 852(b)(6) of the IRC. When the AP redeems
ETF shares for the underlying basket, that is an in-kind
transfer -- *not* a sale. No fund-level capital gain. And the
sponsor gets to choose *which* tax lots to hand over -- naturally
the lowest-cost-basis lots, with the biggest embedded gains.
Those gains leave the fund permanently and silently.

**Stella:** So VTI flushes its appreciated stock out to the APs
and never realises a gain?

**Horace:** Exactly. VTI has distributed essentially zero
capital gains in its entire history. VTSAX has distributed gains
in 2000, 2008, 2018, and a few others. Same portfolio.
Different wrapper.

**Stella:** Then why would anyone hold VTSAX?

**Horace:** Inside an IRA or 401(k), there is no tax to shelter,
and VTSAX has features ETFs do not -- auto-reinvest to the
penny, dollar-amount contributions instead of share amounts. So
in a *tax-deferred* account, VTSAX is fine. But in a *taxable*
brokerage account, default to the ETF. Always.

---

**[SEGMENT 4 -- PREMIUM/DISCOUNT IN STRESS -- 5:30]**

**Stella:** What about when the wheels come off? March 2020?

**Horace:** Great example. On 12-13 March 2020, LQD -- the big
investment-grade bond ETF -- printed at a 5% discount to NAV.
HYG was at 6%. MUB was at 8%.

**Stella:** That sounds like the ETF broke.

**Horace:** That is what everyone said at the time. Here is
what actually happened. The bond market itself froze. Bid/ask
spreads on individual bonds blew out from 5 cents to a
dollar-plus, and many bonds simply stopped trading. The "NAV" of
the bond ETF was calculated off stale dealer quotes that did not
reflect what anyone could actually transact at.

The ETF *kept trading*. The ETF price was a real, transactable,
two-sided market. And the post-mortem -- by BlackRock, ICI, the
SEC, the Fed -- concluded that the ETF prices were a *better*
estimate of fair value than the official NAVs. The ETF did
exactly what it should have done: led price discovery on a
frozen underlying.

**Stella:** So the discount was not a bug.

**Horace:** It was the ETF wrapper doing its job. When the Fed
announced the corporate-bond facility on 23 March, the discounts
closed and the ETFs led the recovery up. Anyone who panic-sold
LQD at -5% bought back in five days later at NAV plus 8%.

---

**[SEGMENT 5 -- CEFs ARE NOT ETFs -- 7:30]**

**Stella:** Sometimes I see PIMCO funds quoted at -10% to NAV
"persistently." Are those ETFs?

**Horace:** No. Those are **closed-end funds**. Same exchange
wrapper category, completely different animal.

A CEF issues a fixed share count once at IPO. *No AP machinery.*
*No creation. No redemption.* When supply and demand drift, no
arbitrageur can pull the price back. CEFs trade at -5% to -15%
discounts persistently, sometimes for years. PIMCO HY CEFs,
BlackRock muni CEFs, Eaton Vance balanced CEFs all live in this
range.

**Stella:** Is that good or bad?

**Horace:** Neither inherently. It just means: never buy a CEF
at NAV -- wait for the discount. And recognise that the CEF
discount can stay where it is for years. One legitimate alpha
source is "structural mispricings institutions cannot touch."
Buying CEFs at -10% to -15% discounts during stress is a
small but legitimate one. But it is not the same game as buying
VTI.

The point: same wrapper category, different mechanism,
completely different price behaviour. Do not confuse them.

---

**[SEGMENT 6 -- WRAPPER CHOICE IS A TAX-LOCATION CHOICE -- 9:00]**

**Stella:** OK so what is the rule?

**Horace:** Two rules.

One. In a *taxable* brokerage account, prefer the ETF wrapper
over the equivalent mutual fund. VTI over VTSAX. IVV or VOO over
VFIAX. BND over VBTLX. The in-kind redemption tax shelter
compounds.

Two. Inside an IRA or 401(k), the wrapper choice is a wash. Pick
whichever is more convenient for your platform -- and inside
Vanguard's own platform that is often the mutual fund because of
auto-reinvest and dollar-amount contributions.

The fee gap between index ETFs and index mutual funds is closed.
VTI and VTSAX are both 0.04%. The wrapper choice in 2026 is no
longer about cost. It is about *where the account lives*.

---

**[OUTRO -- 10:30]**

**Horace:** Three takeaways. APs run the plumbing -- that is why
ETF prices stay glued to NAV. In-kind redemptions are how ETFs
quietly flush out capital gains and stay tax-efficient -- that
is why VTI ends up ahead of VTSAX after twenty years in a
taxable account. And when an ETF prints at a discount during
stress, ask whether the underlying market is functioning before
you conclude the ETF is broken -- almost always the ETF is right
and the NAV is stale.

**Stella:** And the interactive lets me play with all of this?

**Horace:** Pick an ETF -- VTI, SPY, QQQ, JEPI, SCHD, VNQ -- and
the panel shows you AUM, expense, yield, premium-discount
history, and the after-tax-cost ratio versus a comparable mutual
fund. Click around for five minutes. The plumbing will start to
feel familiar.

---

**END SCREEN:** "Next: Side 4 -- Tax-Efficient Investing"
