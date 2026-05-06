# Side Lesson 18: Global Markets — The Case For and Against International Diversification

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Open any introductory portfolio textbook and you will find the same
sentence: *the U.S. is roughly 60% of global market capitalization, so
a properly diversified equity portfolio should hold the other 40%
overseas.* It sounds obvious, almost a tautology. This course
disagrees with the conclusion. Side lesson 18 explains the disagreement
and gives you the rule that the rest of the curriculum quietly relies
on.

There are four reasons this is worth a full lesson rather than a
footnote:

1. **The home-bias debate is the single biggest allocation question
   most retail investors will face.** It is bigger than which factor
   tilt to adopt, bigger than active vs passive — because it controls
   roughly forty percentage points of your equity exposure. Getting
   the right answer matters more than almost anything else.
2. **The "rebalance into international" reflex is built on a survivor
   sample.** Modern Portfolio Theory was canonised in the 1950s-1980s,
   when U.S., U.K., German, and Japanese markets all looked roughly
   comparable on the dimensions a textbook cared about (free float,
   accounting, rule of law). That is not the world investors live in
   today. Russia 2022 and China 2021 are not edge cases — they are
   the modal foreign-equity outcome over a long enough horizon.
3. **The U.S.-versus-world performance gap from 2010 to 2024 was not
   noise.** It was a structural divergence in earnings growth, capital
   formation, and corporate governance. The textbook models that
   recommend `40% international` were calibrated on a regime that no
   longer exists.
4. **The course's investable universe rule originates here.** Every other lesson — from week 3's risk-return
   premia to week 24's institutional sleeve template — implicitly
   restricts itself to U.S.-listed securities. This side lesson
   explains *why*, so the rule does not feel arbitrary when it shows
   up in later weeks.

The textbook position is not wrong; it is incomplete. The honest
answer is that international diversification gives you a real
mathematical benefit *if and only if* the foreign markets you buy
share four properties with the U.S.: rule of law, accounting
transparency, minority-shareholder rights, and a deep secondary
market. Roughly half of "international" by index weight does not
clear that bar.

---

### 2. What You Need to Know

#### 2.1 The Map: How Big Is "the World" Outside the U.S.?

The MSCI All Country World Investable Market Index (ACWI IMI) is the
broadest investable equity benchmark on the planet. As of April 2026
its weights look approximately like this:

- **United States — ~60%.** Roughly $55T market cap, with the
  Magnificent-7 alone equal to the entire EAFE index by float.
- **Developed ex-U.S. (EAFE) — ~25%.** Japan ~6%, U.K. ~4%,
  France ~3%, Canada ~3%, Switzerland ~2.5%, plus Germany,
  Australia, Netherlands, Sweden, Hong Kong, Singapore, Spain, Italy,
  Denmark, Belgium, Finland, Norway, Israel, Ireland, Portugal,
  Austria, New Zealand.
- **Emerging markets — ~12%.** China ~25-30% of the EM bucket,
  India ~17%, Taiwan ~16%, Korea ~12%, Brazil ~5%, Saudi Arabia ~4%,
  South Africa ~3%, Mexico ~3%.
- **Frontier — ~3%.** Vietnam, Nigeria, Kenya, Bangladesh, Sri Lanka,
  Romania, Kuwait (until promoted), Pakistan, Morocco. Frontier is so
  small and illiquid that even institutional managers rarely treat it
  as a real allocation.

![Pie chart of global investable equity market capitalization as of April 2026: United States ~60%, EAFE ~25%, emerging markets ~12%, frontier ~3%. The dominance of U.S. cap weight is the headline; emerging markets are smaller than most retail investors estimate.](image/side18_global_market_cap.png)

The key intuition the chart should leave you with: *global market cap
is dominated by one country.* This was not always true — in 1989, at
the peak of the Japanese bubble, Japan was briefly the largest equity
market in the world and the U.S. was a hair behind. Forty years
later, the gap is roughly five-to-one. That regime change matters
more than any backtest.

#### 2.2 The Performance Tape, 1990-2024: Two Decades, Two Stories

The textbook case for international diversification leans heavily on
the 2000-2009 "lost decade" — the period when SPY went sideways and
EAFE / EM significantly outperformed. The textbook is right that
this period existed. It is wrong to extrapolate from it.

A cleaner way to look at the same data: the period **1990 through
April 2026** decomposes into roughly three regimes.

- **1990-1999: U.S. dominance.** SPY compounded at about 18% per
  year, EAFE at about 7%, EM at about 11% with the 1997 Asia crisis
  taking a chunk out late. The U.S. tech run made every other equity
  market look slow.
- **2000-2009: International dominance.** SPY -1%/yr (the dot-com
  unwind plus the GFC). EAFE +1%/yr unhedged (helped by a falling
  dollar). EM +10%/yr (the BRIC commodity supercycle). For the only
  decade in modern history, holding ex-U.S. stocks paid.
- **2010-2024: U.S. dominance, hard.** SPY about +14%/yr.
  EAFE about +6%/yr. EM about +4%/yr. The gap was the largest in
  modern data — wider than the 1990s — and was driven by three
  things that may or may not persist: software-eats-world (favours
  the U.S. tech complex), shale (favours U.S. energy independence),
  and dollar strength (penalises unhedged ex-U.S. holdings).

![Wealth path of $1 invested in SPY, EFA, and EEM from 1990 through April 2026, with shaded regime bands. SPY ends near $35; EFA near $5; EEM near $5. The 2000s gap closes, then the 2010s gap re-opens far wider than before.](image/side18_us_vs_world.png)

The honest reading of this chart: **leadership has rotated, and
nobody knows where it goes next.** That is also Horace's first
principle: *alpha is rare; the toolkit is portfolio
construction.* If you cannot predict which region wins the next
decade, the standard textbook response is *own all of them in
proportion to size.* This course's response is different and is
explained in §2.4.

#### 2.3 The Currency Layer

International returns have two components: the foreign-currency
return of the underlying stock, plus the change in the
foreign-currency-to-dollar exchange rate. Over a single year these
two pieces are roughly the same size in volatility — about 7-9%
each — and the FX piece can flip a positive local return into a
negative dollar return or vice versa. 2014-2016 (strong dollar) and
2022 (very strong dollar) hurt unhedged ex-U.S. holdings;
2002-2007 (weak dollar) and 2017 (weak dollar) helped.

You can hedge currency. Vehicles like HEFA (hedged EAFE) and DBEF
buy a rolling forward to neutralise the FX leg. The hedge costs
roughly the interest rate differential — about 1% per year against
the euro, more against the yen when U.S. rates are higher than
foreign rates. Empirically, over 10-year windows the *currency
effect averages close to zero* but adds about 30-40% of the
volatility of unhedged international equity. So the trade-off is
clean: hedge if you care about year-to-year noise, leave unhedged if
you have a 10+ year horizon and want the diversification of holding
non-dollar assets. Most retail-grade research lands at "leave it
unhedged for the equity sleeve."

This course leaves the question moot, because the U.S.-only rule
side-steps it entirely.

#### 2.4 The Political-Risk Premium and the Investable-Universe Rule

The argument the textbook does not make is the one that determines
this course's allocation rule. International equities — especially
emerging-market equities — carry a class of risk that does not show
up in any of the standard sigma / VaR / drawdown statistics: the
risk of *expropriation*. The textbook implicitly assumes you can
always sell.

A short list of times that assumption broke in the last decade:

- **China 2021.** The CCP's "common prosperity" campaign wiped
  about $1.5T off Chinese tech stocks in six months. DiDi was
  delisted from the NYSE within months of its IPO. The for-profit
  tutoring industry was made illegal by regulatory fiat overnight.
  Retail holders of FXI / KWEB watched 50-70% drawdowns with no
  fundamental catalyst — only a policy change.
- **Russia 2022.** After the Ukraine invasion the Moscow Exchange
  was closed to foreign sellers for several months. By the time
  trading reopened, Western sanctions had effectively rendered every
  Russia-listed share worthless to a U.S. holder. Index providers
  marked Russian weights to zero. Roughly $50B of foreign-held
  Russian equity was wiped out — not in a market-driven drawdown,
  but by political fiat. This was the largest single-country
  expropriation event since the Cuban revolution in 1959.
- **Hong Kong 2020-2024.** The National Security Law and subsequent
  capital-control tightening have eroded the rule-of-law premium
  Hong Kong used to carry. Stocks listed there are now pricing
  in mainland-China policy risk that did not exist five years ago.
- **Turkey 2018-2024.** Erdogan's unconventional monetary regime
  destroyed about 90% of the lira's purchasing power. A Turkish
  stock that doubled in lira terms still lost two-thirds in dollars.

The pattern in all four cases is the same: *an event the U.S.-listed
investor could not hedge against, did not show up in the historical
risk model, and could not be unwound at any price.* This is the
political-risk premium, and the standard equity-premium math does
not capture it.

This course's response — the
"investable universe" rule — is to **restrict the entire
recommended portfolio to U.S.-listed equities.** The rule has four
pillars:

1. **Rule of law.** U.S. courts enforce contracts, including against
   the government. The Fifth Amendment takings clause has been
   tested, and it works.
2. **Accounting transparency.** SEC-registered issuers file 10-K
   and 10-Q statements audited under PCAOB oversight. Foreign-private
   issuers reporting under their home regime do not get the same
   audit guarantee.
3. **Minority-shareholder rights.** Delaware corporate law has
   200 years of case law protecting minority holders against
   controlling-shareholder self-dealing. China has none. Russia
   has none. Korea is improving but is not there yet.
4. **Deep secondary markets.** You can sell a U.S.-listed stock at
   a tight bid-ask spread on any trading day in any regime. You
   cannot say that about Vietnam, Nigeria, or Argentina.

The four pillars are *substitutes* for the diversification benefit.
You give up about 40% of the global investable opportunity set; in
exchange you get a portfolio you can actually liquidate in a crisis
and that nobody can confiscate by political decision.

#### 2.5 The Compromise Lane: U.S.-Listed ADRs

Refusing to own EFA / VXUS / VWO does not mean refusing to own
non-U.S. companies. The compromise — the one the rest of the course
quietly assumes — is **U.S.-listed American Depository Receipts
(ADRs).**

An ADR is a U.S.-listed share of a foreign company, registered with
the SEC, custodied by a U.S. bank, and subject to U.S. rule of law.
Buying TSM (Taiwan Semiconductor) on the NYSE is materially safer
than buying 2330.TW on the Taipei exchange — same underlying
business, but the U.S. listing forces SEC reporting, U.S. courts
have jurisdiction, and the shares clear through the same DTC
infrastructure as AAPL.

The shortlist of high-quality ADRs that earn a place in the course's
investable universe:

- **TSM** — Taiwan Semiconductor. Effectively a monopoly on
  leading-edge logic fabrication. The single most important
  semiconductor business on Earth.
- **ASML** — Dutch maker of EUV lithography tools. The only
  vendor of the machines that print every leading-edge chip.
  Listed on NASDAQ since 1995.
- **SAP** — German enterprise-software incumbent.
- **NVO** — Novo Nordisk, Danish maker of Ozempic.
- **TM / SONY / HMC** — high-quality Japanese exporters.
- **SHOP** — Shopify, Canada-domiciled but NYSE-listed.

A second tier is worth caveating because of the political-risk
overlay: **BABA, JD, PDD, BIDU, NIO** are U.S.-listed Chinese ADRs.
They share a U.S. wrapper but the underlying assets are inside
mainland China and inside a Variable Interest Entity (VIE) structure
that has never been tested in a full Chinese expropriation event.
Position-size them like venture bets, not like core equity.

The mechanic to internalise: *the investable universe is defined by
the listing venue, not by where the company does business.* TSM is
in. 2330.TW is out. Both are claims on the same assembly line.

---

### 3. Common Misconceptions

1. **"60% U.S. of world cap means I should own 60% U.S. in my
   portfolio."** This is the textbook recipe. It assumes all 100
   cents on the dollar of global cap are equally investable. They
   are not.
2. **"International is a free diversification benefit because of
   low correlation."** Correlations between SPY and EFA have run
   0.85 in the last decade — high enough that the diversification
   math gives you maybe 1-2% volatility reduction, not the 5%+
   the textbook suggests.
3. **"Emerging markets must outperform because they're growing
   faster."** Decades of data show GDP growth and equity returns
   are essentially uncorrelated. China's GDP grew 10x from 2000-2020
   and the MSCI China index returned about 5%/yr in that span.
4. **"I'm under-diversified if I don't hold VXUS."** You are
   *concentrated in U.S. legal jurisdiction.* That is a deliberate
   choice, not an accident. It is the trade-off, not a mistake.
5. **"Currency hedging is too complicated to bother with."** It is
   bundled into ETFs. HEFA charges 35bp. That is the cost of the
   hedge — usable if you want it.
6. **"Russia 2022 was a one-off."** It was the largest single
   event in the modern era, but China-2021 and Hong Kong's slow
   re-rating since 2020 are the same family of risk. The base rate
   is higher than it looks.
7. **"ADRs are no different from local-listed shares."** They have
   identical economic exposure but materially different legal
   exposure. The U.S. listing is a real protection layer.
8. **"China A-shares are now investable because MSCI added them."**
   MSCI's index decisions are about benchmark coverage; they do not
   confer rule-of-law. The 2017 A-share inclusion did not change
   what happened to retail holders of YY, DiDi, or NTES in the
   2021-2022 crackdown.
9. **"Buying EAFE is safe — it's all developed markets."** EAFE is
   safer than EM but still carries currency risk and concentrated
   single-country risk (Japan was 70% of EAFE in 1989; the U.K.
   was 30% in 2000). Diversification within EAFE is uneven.
10. **"International diversification protects me from a U.S. crash."**
    The 2008 GFC saw EAFE -43% and EM -53% versus SPY -37% — the
    *worst* drawdowns of the three were ex-U.S. The diversification
    benefit fails precisely when you most need it.

---

### 4. Q&A Section

**Q: If I follow the U.S.-only rule, what about TSM, ASML, BABA?
Are those allowed?**
A: TSM and ASML are yes — they are SEC-registered, U.S.-listed,
and you have a Delaware-style claim on the depository shares. BABA
is a maybe — the wrapper is U.S. but the underlying VIE structure
sits inside mainland China and has never been tested by a full
expropriation. Size BABA-class names like opportunistic positions,
not like core equity.

**Q: What about VXUS or VEU as a core holding? Vanguard sells
them precisely for retail.**
A: They are perfectly serviceable products. The course rule is not
that they are bad; it is that the course's risk-return math
deliberately excludes them. If you choose to hold 10-20% in VXUS,
your CAGR will look approximately like the lesson's 1990-2024
chart — i.e. lower than U.S.-only over the last 15 years, higher
in the early 2000s. You are taking the textbook trade.

**Q: What's the right hedge for U.S.-only concentration risk if I
believe the U.S. could underperform for a decade like 2000-2009?**
A: Three answers. First, the four-tranche framework
already includes a stores-of-value sleeve — gold, real assets — that
is currency-agnostic. Second, U.S. multinationals (AAPL, MSFT,
PG, KO) earn 50%+ of revenue overseas, so SPY itself is already
half-international by economic exposure. Third, if you really want
the full FX/region diversification, the cleanest expression is GLD
plus a small commodities sleeve, not VXUS.

**Q: Do U.S.-listed ADRs of foreign companies pay foreign
withholding tax?**
A: Yes. The custodian bank withholds at the foreign-source rate
(15% under most treaties, 30% in some cases). In a taxable account
you can claim a foreign tax credit on Form 1116. In an IRA the
withholding is permanent and not recoverable — which is one reason
the course recommends holding international-exposed names in
taxable, not tax-deferred accounts. The tax-location lesson covers this in detail.

**Q: Is VWO different from EEM? Both are emerging markets ETFs.**
A: Same asset class, different index providers. VWO follows FTSE
(includes Korea), EEM follows MSCI (excludes Korea). VWO's expense
ratio is 0.08% vs EEM's 0.70%, which is enough cost difference
to matter. If you do hold EM, VWO is the correct vehicle.

**Q: What about the China A-shares MSCI added in 2018-2019? Are
those any safer than Hong Kong-listed Chinese shares?**
A: They are *less* safe. A-shares trade on the Shanghai and
Shenzhen exchanges and are subject to mainland Chinese law in a way
that even Hong Kong listings are not. The 2017 inclusion was a
benchmark-coverage decision by MSCI, not an accessibility upgrade.
Capital controls limit your ability to sell in a crisis. Hard pass.

**Q: How does the lesson square with Horace's barbell principle?**
A: The barbell says *combine cheap-and-safe + lottery-
ticket + nothing in between.* The U.S.-only rule applies to the
cheap-and-safe leg: VTI / SCHD / TLT — all U.S.-listed. The
lottery-ticket leg is allowed to include non-U.S. names (small TSM
or ASML position) because those are sized like options, not like
core. The middle of the barbell — international index funds at
40% weight — is exactly what the framework rules out.

**Q: What single number would change my mind?**
A: A persistent reduction in the political-risk premium between
the U.S. and the next-largest market (call it Japan or the U.K.).
Concretely: if U.K. corporate-governance ratings, accounting
transparency, and contract enforcement converged with U.S. levels,
plus FX hedging costs collapsed, plus a sustained 20%+ valuation
discount opened, then the trade becomes interesting. None of those
conditions hold today.

**Q: Doesn't the U.S. itself carry political risk? FTC, antitrust,
crypto crackdown, tariff policy?**
A: Yes — the U.S. is not zero-political-risk. But the magnitude
gap is large. Antitrust unwinds are litigated for years and bounded
by the Sherman Act and Delaware case law; they do not look like
the China 2021 crackdown. The course's claim is not "U.S. is
safe" — it is "U.S. is materially safer on the rule-of-law axis
than the alternatives."

**Q: I already own VXUS in my 401(k) and can't easily get rid of
it. What now?**
A: Don't fight your plan. The 401(k) match (the tax wrapper
beats security selection) is worth 50%+ on the dollar; do not
sacrifice that to enforce a 5-percentage-point allocation rule.
If your plan menu offers VXUS but not a clean U.S.-only balanced
fund, hold VXUS in the 401(k) and tilt the *taxable* account
U.S.-only to bring the household total to the target.

**Q: Final question — if I run the global blender in the
interactive panel, what should I expect to see?**
A: Three things. First, almost any plausible U.S.-heavy mix
(70-100% VTI) beats the cap-weighted (60% VTI / 28% VXUS / 12%
VWO) on CAGR over the 1990-2024 backtest, by roughly 1-2% per
year. Second, the Sharpe gap is narrower than the CAGR gap —
international does damp some volatility. Third, the maximum-
drawdown line moves around less than you'd expect: the GFC and
COVID drawdowns hit everywhere. The data argues for more U.S., not
less, even before the political-risk overlay.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** "Why this course is U.S.-only — and the four
filters that pick the rare exceptions."
**RUNTIME TARGET:** ~12 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00-1:00]**

`[VISUAL: image/side18_global_market_cap.png]`

**Stella:** Okay Horace, every other allocation video on YouTube
opens the same way: "diversify globally, hold VXUS, the U.S. is only
60% of world market cap." But this course does something
different. We don't recommend VXUS. We don't recommend EFA. We
don't even recommend hedged international ETFs. Why?

**Horace:** Because the textbook is calibrated on a world that
doesn't exist anymore. It came out of the 1970s and 80s when the
U.S., U.K., Germany, and Japan all looked roughly like comparable
markets. Today they're not — and the gap has been widening for
fifteen years. That's the conversation today.

**Stella:** And there's a hard rule we're going to give the audience
at the end. The investable-universe rule.

**Horace:** Right. By the end of this you'll know why we wrote it,
what it excludes, and what the small list of exceptions looks like.

---

**[ACT I — THE MAP — 1:00-3:00]**

`[VISUAL: image/side18_global_market_cap.png — pie chart]`

**Stella:** Start with the picture. Global investable equity, April
2026, by region.

**Horace:** Sixty percent United States. Twenty-five percent
developed-markets ex-U.S. — that's EAFE. Twelve percent emerging
markets. Three percent frontier. The U.S. number used to be lower —
forty percent in 1989, when Japan briefly tied us. Today the U.S. is
five times the size of Japan.

**Stella:** And the textbook says: own each region in proportion
to its weight.

**Horace:** Yes. The textbook says hold sixty cents on the dollar
in the U.S. and forty cents overseas. That's the standard recipe.

**Stella:** Why not?

**Horace:** Because the textbook is implicitly assuming all forty
of those overseas cents are equally usable. They're not.

---

**[ACT II — THE TAPE — 3:00-5:30]**

`[VISUAL: image/side18_us_vs_world.png]`

**Stella:** Here's the wealth path. One dollar in 1990, in three
buckets — SPY, EFA, EEM — through April 2026.

**Horace:** Three regimes. The 1990s — SPY runs eighteen percent a
year, EAFE runs seven, EM is wild. The 2000s — SPY actually loses
money for the decade, EAFE goes flat, EM has a commodity boom and
returns ten percent. And 2010 to today — SPY does fourteen percent
a year, EAFE does six, EM does four. The widest gap in modern data,
and it's been the U.S.

**Stella:** So if you'd bought "the world" at fifteen-year-back-test
weights, you'd have given up roughly half your CAGR for the
diversification.

**Horace:** Yes. And the diversification didn't help in the bad
year. Look at 2008 — EAFE was minus forty-three percent, EM was
minus fifty-three, SPY was minus thirty-seven. The international
sleeves drew down *more.*

**Stella:** Which is the punchline, kind of.

**Horace:** It's the math. Correlation between SPY and EAFE has
been about zero-point-eight-five over the last ten years. That gives
you maybe one or two percent volatility reduction from the
diversification — not the five percent the textbook claims.

---

**[ACT III — THE POLITICAL RISK ARGUMENT — 5:30-8:00]**

**Stella:** But the actual reason this course says U.S.-only isn't
the performance argument. It's the political-risk argument.

**Horace:** Right. And this is where the textbook is silent. Standard
risk math — sigma, VaR, drawdown — does not capture *expropriation
risk.* The textbook implicitly assumes you can always sell.

**Stella:** Walk through the cases.

**Horace:** Russia, February 2022. The Moscow exchange closes to
foreign sellers. By the time it reopens, sanctions have rendered
every Russia-listed share worthless to a U.S. holder. Roughly fifty
billion dollars of foreign-held Russian equity is wiped out — not
by a market drawdown, by political decree. Index providers mark
Russia weights to zero.

**Stella:** That's the most dramatic. China?

**Horace:** China 2021. The for-profit tutoring industry is made
illegal overnight by regulatory fiat. The Ant Group IPO is canceled
the day before pricing. DiDi is delisted within months of IPO.
Hundreds of billions in foreign-held Chinese tech equity, drawn
down fifty to seventy percent on a policy change. Then Hong Kong's
slow re-rating since the National Security Law. Then Turkey,
where Erdogan's monetary policy crushes ninety percent of the lira
in five years.

**Stella:** So the case isn't "international stocks are bad." It's
"some portion of international cap weight is uninvestable in a way
that doesn't show up in the standard models."

**Horace:** Exactly that. And it's not a small number. China alone
is about a third of the EM index. The portion of global market cap
that fails the rule-of-law test is somewhere between fifteen and
twenty-five percent of the total.

---

**[ACT IV — THE FOUR FILTERS — 8:00-9:30]**

**Stella:** So the rule. The investable-universe rule.

**Horace:** Restrict the recommended portfolio to U.S.-listed
equities. The rule has four pillars.

One — rule of law. U.S. courts enforce contracts, including against
the government. The takings clause has been tested.

Two — accounting transparency. SEC registrants file 10-K and 10-Q
statements audited under PCAOB oversight.

Three — minority-shareholder rights. Delaware corporate law has two
hundred years of case law protecting minority holders.

Four — deep secondary markets. You can sell on any trading day in
any regime. You can't say that about Vietnam, Nigeria, or
Argentina.

**Stella:** And you give up the forty percent of cap weight that's
overseas.

**Horace:** Yes. That's the explicit trade. We are taking
concentration risk in U.S. legal jurisdiction *deliberately.* It is
a feature, not an oversight.

---

**[ACT V — THE COMPROMISE — 9:30-11:00]**

**Stella:** But you do let people own non-U.S. companies. Through
ADRs.

**Horace:** Right. The investable universe is defined by *listing
venue,* not by where the company does business. TSM — Taiwan
Semiconductor — is on the NYSE. SEC-registered. PCAOB-audited.
Custody at a U.S. bank. You have Delaware-flavoured legal claims.
Same chip fab. Different legal wrapper. TSM is in. The Taipei
listing of the same company is out.

**Stella:** Shortlist?

**Horace:** TSM, ASML, SAP, NVO, the high-quality Japanese exporters
— TM, SONY, HMC. SHOP for Canada exposure. A second tier with
caveats: BABA, JD, PDD. They wear a U.S. wrapper but the underlying
VIE structure has never been tested by a full Chinese expropriation
event. Size those like venture bets, not like core.

**Stella:** And the interactive lets people see the trade in action.

`[VISUAL: interactive/side18_global_blender.html]`

**Horace:** Three sliders — VTI, VXUS, VWO — sum to one hundred.
Embedded annual returns 1990 through 2024. Move the dials, see
CAGR, vol, Sharpe, and max-drawdown. Watch the correlation matrix
update in real time.

**Stella:** And the headline you're going to see —

**Horace:** Almost any U.S.-heavy mix beats the cap-weighted mix on
CAGR over the last thirty-five years. The Sharpe gap is narrower —
international did damp some vol. The drawdown line barely moves
because the GFC and COVID hit everywhere. *Even before* you put
the political-risk premium on top.

---

**[OUTRO — 11:00-12:00]**

**Stella:** Three takeaways.

One — global cap weight is sixty-twenty-five-twelve-three.
Two — the textbook recipe of "own everything by weight" was
calibrated on a world where all four corners of the equity map were
roughly comparable. That world is gone.
Three — this course is U.S.-only by deliberate choice, with a small
ADR list as the compromise lane.

**Horace:** And the underlying principle. One — alpha is rare; the
toolkit is portfolio construction. Two — the portfolio you can
actually liquidate is worth more than the portfolio that diversifies
on a spreadsheet but freezes shut in a crisis.

**Stella:** Side eighteen done. Next time — side nineteen.

---
