# Big Picture Trading (Patrick Ceresna) — Consolidated Course Notes

## Orientation: The Instructor, the Corpus, and the Method

**Patrick Ceresna** is a derivatives and macro educator, co-founder of Big Picture Trading, chief instructor for the TMX/Montreal Exchange (the Canadian derivatives exchange), a Chartered Market Technician (CMT), and a regular hedged-equity/derivatives strategist on the MacroVoices podcast — where the *Eurodollar University* series with Jeffrey Snider and Chris Cole's portfolio work were compiled — and co-host of The Market Huddle with Kevin Muir. His career, as he tells it in the material: he came up on the CIBC (Canadian Imperial Bank of Commerce) trading floor in 1998–99, straight out of university during the tech bubble. The bank gave a first-year employee a $20,000 line of credit; he went all-in on tech stocks — "the exact same way that everyone's all in on Bitcoin today" — and "got my face ripped off." He calls that blowup one of the best things that ever happened to him, because it made **risk management his life obsession**: conviction is not a risk-management strategy — "you need an insurance policy that protects you from yourself." He spent almost a decade at CIBC in multiple trading roles, about five of those years trading a **$50 million pool dedicated to option writing** alongside a portfolio manager, and across a 20-year trading career he estimates **60–70% of all the money he has made came from premium harvesting** — more than from market timing.

Recurring co-presenters in the material: **Luke** (Director of Member Services — logistics, audience questions, and co-teacher of the writing bootcamp), **Massil** (platform tutorials for TradingView and Interactive Brokers), **George Gammon** (Rebel Capitalist — co-host of the Dragon Portfolio and gold webinars), and **Kevin Muir** (The Macro Tourist — co-host of the Trading Masters program, whose free module on trade sizing is reproduced here).

**What the corpus covers.** The course spans: (1) money and macro foundations — what money is, the fiat system, the eurodollar/shadow-banking system, Ray Dalio's economic machine, the Dragon Portfolio, and historical money lessons; (2) complete options education — the Options Bootcamp (introduction, pricing, Greeks, application), the Options Master Program (contract specifications, pricing, volatility, time), Options Fundamentals, the Option Writing Bootcamp (covered calls and put selling), and Options for Income; (3) the strategy playbook — ratio call spreads, calendar straddles, diagonal spread bootcamp, the volatility-trading toolkit, synthetics, and hedged macro positions; (4) a full gold-and-commodity options program — the volatility skew, gold collars, hedging physical gold, repair strategies, asymmetry systems, and the commodity/gold cycle model; (5) risk, sizing, and the crash playbook — master-trader mindset, Kelly-based sizing, breakout trading, short-term hedging, trade repair, the tactical portfolio, and downturn strategies; and (6) platform tooling — TradingView and Interactive Brokers (including the Volatility Lab and Probability Lab), plus the foundational lesson on why stop-loss orders fail.

**The method in one line.** **Macro fundamentals are the center of the universe** — they drive market conditions, which drive corporate fundamentals, which "technically manifest themselves on the chart." Technical analysis bridges macro story to trade (it answers *when* the move is underway, *where* it goes, and *how* to structure it — Ceresna's toolkit: measured moves, Fibonacci retracements, volume profile, moving averages, wedge/breakout patterns). **Options are the strategic overlay** — not for day trading, but to build asymmetry and manage timing error across cycles that play out over months.

The governing quote, which Ceresna uses repeatedly (attributed to **George Soros**): *"It's not whether you're right or wrong that is important, but how much money you make when you're right and how much you lose when you're wrong."* The whole course is machinery for **asymmetric trades that lose small and win big** — "paper cuts and home runs." Two cultural rules of the desk: in markets "we never say we're wrong, we always say we're early" (Ceresna notes the two are the same, but the mindset matters in commodities, where a boom genuinely does eventually follow every bust), and **no position is buy-and-forget** — trades are rolled, adjusted, and repaired as the cycle proves the entry early.

---

# Part I — Money, Macro and the Economic Machine

## 1. Money and Currency: What Money Is and How We Got Here

<!-- Source video: "Module 1 - Money and Currency (720p with 25fps).mp4" -->

Ceresna treats this module as the foundation for everything else: to understand how markets and macro forces interact, go back to the root — what money actually is and how the system we live in came to exist. Almost nobody has the foundational anchors of how today's money works.

### The functions and properties of money

Money has **three primary functions**:

1. **Medium of exchange** — an intermediary between buying and selling goods, services, and labor.
2. **Unit of account** — the yardstick in which everything is priced.
3. **Store of value** — what you hold shouldn't lose value while held, so you can exchange it later.

Money must be **portable**, **durable** (food spoils, so it fails as a store of value), and, most importantly, **fungible** — interchangeable, one dollar the same as any other. This is why real estate can never be money: every property is unique, failing fungibility.

Money was created as a **social contract** to replace barter — a way to settle debts, labor, goods, and services. Across most of human history the dominant monies were **precious-metal coins** (gold, silver, platinum); salt and seashells were the exceptions. As early as the sixth century, **paper notes backed by gold** appeared: claim checks on gold in a vault — lighter to carry, easier to store, harder to steal than carts of bullion.

### A brief history of monetary systems

Central banks to this day own vast gold reserves backing their currencies, even though the gold is no longer exchangeable for them. China still refuses to export a single ounce of domestic gold production — all of it stays with citizens or the state.

- **Classic gold standard era, 1816–1913** (pre-WWI), with variants even inside it. In the US Civil War the Confederacy issued cotton-backed paper while the North printed **greenbacks** ("Lincoln dollars") — pure fiat issued directly by the US Treasury, no central bank involved, backed by nothing.
- **WWI and after.** Countries abandoned gold to fund the war; the Versailles era produced many hybrid arrangements. England's staying on gold contributed to its Great Depression; the US confiscated gold during its own.
- **Pre-Fed America.** Through the 1800s, thousands of small banks issued **private bank notes** circulating as local money — like a personal check with "cash" written at the top and a dollar value assigned: a bearer note anyone could pass along and spend. There was often no centralized money at all.
- **Gold- and silver-backed paper.** Old US currency said it outright: the $10 bill read "in gold coin payable to the bearer on demand"; another was "one silver dollar," convertible on demand, issued by the Treasury. (Ceresna notes, as an aside, the conspiracy theory linking JFK's silver-backed Treasury notes to his assassination — "I don't know whether I believe it... but it's an interesting story.") Today's dollar, yen, Canadian and Australian dollars are all **fiat** — "just a Federal Reserve note." Recommended reading: any Niall Ferguson history of money.

### Bretton Woods 1944: designing the postwar order

To understand today's system, go back to WWII. Much of Europe's gold fled to the United States (Poland, famously, smuggled its entire reserve out ahead of Hitler, who purged gold from every vault he reached). Britain and others paid their wartime debts **in gold**. The US lost lives, but economically it emerged the massive beneficiary and a global powerhouse.

In 1944, before the war was even won, the Anglo-American alliance met at **Bretton Woods** to design a new world order built on a monetary base. The two architects:

- **John Maynard Keynes** (Britain) — the famous economist whose frameworks are still actively touted. He pushed for the creation of the **IMF** and **World Bank** (both born at Bretton Woods and still with us) and for a one-world currency for international trade and multilateral clearing called the **Bancor**. The Bancor never came into existence; Ceresna's tease is that today's eurodollar system is its functional equivalent.
- **Harry Dexter White** (US), senior aide to Treasury Secretary **Morgenthau**. The Americans saw that Britain was essentially bankrupt and unable to pay its debts to the US, and deliberately used that leverage. Their quiet agenda: **dismantle the British imperial preference** (the preferential Commonwealth trading bloc covering roughly a quarter of the world — Canada, Australia, India and more), and build a **US-centric, gold-based system**. They disliked global "Bancor" money; they believed gold had to remain the settlement asset for international imbalances.

White outmaneuvered Keynes — dividing the labor so Keynes ran the World Bank while White oversaw the IMF and the currency arrangements, then pushing through the language making the **US dollar (backed by US gold) the world reserve currency**. Keynes only noticed a week after the conference ended. The episode is chronicled in *The Battle of Bretton Woods*. The system that resulted: most of the world's gold sat on US soil; the dollar was convertible to it; every other nation held dollars in reserves as the equivalent of holding gold; and the dollar became the global clearing currency for trade. This era is also where the petrodollar system's roots lie.

For nearly 30 years (1940s–1970s) the US ran **massive trade deficits deliberately, to distribute dollars abroad** — the world needed dollar supply for trade and reserves. This is why 1970s pop culture was obsessed with Fort Knox: the vault at the center of the monetary world.

**Why Bretton Woods failed.** It required universal participation. The Soviets attended mainly to secure a large IMF rebuilding loan, then backed out; China left when it went communist. The **Cold War, in this telling, was not primarily an arms race but a clash of two monetary systems** — communist central planning versus the Western dollar-gold system. Richard Nixon made his name as a young congressman on the House Un-American Activities Committee, which accused **Harry Dexter White of being a Soviet spy** (with legitimate evidence; White died before trial) — and he denounced the "Morgenthau Plan," Bretton Woods, from day one.

### The Nixon shock and the birth of the fiat era

By Vietnam (the theater of that monetary clash) and the guns-and-butter spending before it, Nixon believed the US was genuinely **losing** to the USSR and that the gold peg was handicapping America — it prevented controlling money creation. The system was visibly unraveling: **France demanded gold conversion for its dollar reserves, literally sending warships to collect it.** In 1971 Nixon unilaterally terminated dollar-gold convertibility — the **Nixon shock** — ending Bretton Woods and rendering the dollar pure fiat overnight. The logic: let the bankers off the leash and America could win the Cold War.

Important: in the five to ten years before 1971, the **eurodollar system** had already been born — the mechanism by which banks supplied the world with dollars without the Treasury printing them and exporting them via trade deficits. After further negotiations (the **Smithsonian Agreement**, then the **Jamaica Accords**), the modern **free-floating fiat currency system** emerged. Before that there was no such thing as forex trading — every currency was pegged against the dollar with periodic adjustments, much like China's managed float today.

### How fiat money actually works

- Governments declare **legal tender**: you cannot refuse the currency in payment, and taxes must be paid in it. That is what makes it "the" currency. It has no fixed value, no intrinsic backing; its function is facilitating payment.
- Treasuries and central banks create **physical cash and coins** — the bill in your wallet is a bearer instrument. But **the vast majority of new money supply is created by the private sector**, in the money-center banks, as **deposits — units of debt** created against nothing but reserve ratios.
- A quote Ceresna anchors this with, from *Money Facts*, a pamphlet of the US House Banking and Currency Committee: **"Every circulating Federal Reserve note represents, in actuality, a $1 debt to the Federal Reserve System."**
- The key insight: **money creation and allocation have been outsourced from the public sector to the private sector.** Governments effectively say "we don't know how to properly allocate money," and delegate creation and distribution to private banks, which compete for deposits (reserves) and then compete to lend to creditworthy borrowers. Run the best bank, attract the most deposits, build the most reserves, create the most credit — become the largest bank.
- The shock observation: **the government neither controls the money supply nor its allocation.** In Canada, the Bank of Canada signs a five-year agreement with the elected government covering monetary policy and inflation targets — after which the elected government has no say. Central banks are autonomous; they represent the commercial banks and system stability, not the government of the day.
- Banks still operate under rules: Basel Accords (Basel III), Dodd-Frank, capital-adequacy and stress tests, liquidity and reserve requirements, asset classifications determining lending capacity. Governments regulate — often with poor transparency — while central banks autonomously create and manage the infrastructure the banks operate in.

### Fractional reserve lending: the multiplier in one example

The **monetary base** = commercial banks' reserves on deposit at the central bank (the central bank is "a bank for banks") + physical cash and coin in circulation. When a bank needs notes and coin, it issues debt against them and takes delivery.

Ceresna's simplified loop (he stresses the real system is far more complex; this is the overhead view):

1. **Ann** deposits **$1,000,000** at Bank A. She believes she has $1M.
2. Bank A, holding reserves, creates a **$900,000 mortgage** for **Joe** — it literally types $900,000 into his account and hits enter. It did not take the money from another depositor; it created credit against its reserves.
3. Joe buys a house from **Sally**, who deposits the **$900,000 check at Bank B**. Bank B cannot know this was newly created credit — it treats it as brand-new money.
4. Now Ann and Sally both believe they hold their full balances. **Money supply: $1.9M. Credit outstanding: $900,000.** All from one original million.

Then the interest drain: Joe pays, say, **$25,000/year** in mortgage interest. That money leaves the closed loop (imagine this repeating across trillions of transactions), so money supply shrinks to $1,875,000. Bank A must create new credit to keep money in the system — a **$20,000 car loan to Tom** — bringing supply to **$1,895,000** while total debt outstanding rises to **$920,000**.

**Punchline: more credit, less money supply.** This is the core observation behind Ceresna's persistent **deflationary lean** — versus the inflationary camp at MacroVoices — because the gap between debt growth and money-supply growth is the heart of assessing inflationary versus deflationary risk.

### Cash is a sliver; credit is the system

Physical cash is **less than 3% of the total stock of money**; roughly **97% is private bank credit money** — electronic balances created as deposits. Consequences:

- **The single most dangerous thing to a central bank is a bank run** — everyone demanding cash at once would collapse the system, because the cash doesn't exist for more than ~3% of the claims.
- This is also the seed of **gold bugs**: the disenchanted conclude "gold is real." Ceresna's stance is deliberately neutral: understand the system; don't be tainted in either direction.

The US numbers he cites: monetary base **$0.14T → ~$3.5T**; credit-driven money supply **$1.5T (1980) → $13T (2016)**; total bank-created debt **$4T → $66T**. The gap between money supply and credit is the "leakage" — money supply cannot grow as fast as credit. Since gold's removal, money supply has expanded unprecedentedly, central banks openly manipulate asset prices (QE targeting asset prices and rate levels), and the debt mountain is serviceable only at historically low rates. It is no coincidence that hyperinflation hit in the 1970s — the fiat system's infancy, when nobody understood what to trust — followed by one of the greatest real-estate inflations from the 1970s to the present.

## 2. The Eurodollar System

<!-- Source video: "EuroDollar University (540p with 25fps).mp4" -->

**Eurodollar University** is a four-part MacroVoices interview series — host **Erik Townsend** questioning **Jeffrey Snider** of Alhambra Investment Partners — compiled by Patrick Ceresna into one video with the slide deck embedded. Snider's thesis: the global monetary system evolved, over decades, into something that exists in the shadows, outside official statistics, definitions, and even official *understanding* — and until you understand what actually happened, you cannot know where we are now.

### What "eurodollar" means — and doesn't

The term is **not technically precise**. Snider uses it as a catch-all for a radical monetary evolution: away from a system based on **deposits of dollars** toward an **interbank system of ledger balances and traded bank liabilities** — offshore *and* wholesale. The conventional definition ("a US-dollar deposit at a bank outside the US") captures only the early stage. His formulation: *"There is no thing called a eurodollar. It's a figment... a phantom. All it is is a system of banks trading liabilities."*

### Before eurodollars: bankers' acceptances

Global trade needs a way to mediate between distinct currency systems — a Japanese firm trading with Sweden can't conveniently hold kronor. The first elegant solution was the **bankers' acceptance**: a bearer instrument, like a cashier's check, **fully reserved up front** (funds deposited before the acceptance was written), then tradable between banks. The **Federal Reserve was founded in 1913 with establishing a dollar acceptance market among its first tasks**; through the 1910s–20s most seasonal variation in the Fed's balance sheet was buying and selling acceptances. The inefficiency: requiring deposits up front.

### Birth of the eurodollar market, 1950s

There is no precise start date. The widely told story: sterling was a co-reserve currency under Bretton Woods, but **sterling crises and the 1956 Suez crisis** made transacting in sterling difficult. Dollars already sat offshore for assorted reasons — one story has **the Soviet Union placing dollars in Swiss banks** to avoid confiscation by US authorities. London merchant banks simply switched from sterling acceptances to **eurodollars** — and the key improvement was that eurodollar claims **required no cash deposits up front**; they could be "derivative claims on derivative claims." A second driver: **Regulation Q** capped the interest US banks could pay depositors, while London, Zurich, Montreal, or Tokyo paid market rates — so global dollar holders followed the yield offshore.

### Milton Friedman and the bookkeeper's pen

Officialdom was oblivious: in **1960, across 17 FOMC meetings producing 941 pages of discussion, "eurodollar" was not mentioned once**; 1961, once (the year of the Triffin discussion); 1962, fifteen times; by **December 1968, 28 times in a single meeting**, and **62 times by April 1969**. Even by 1969 the known offshore market was roughly **$30 billion (1969 dollars)** — enormous for the time.

Milton Friedman's famous **1971 article** opened with a senior international financial official being asked where eurodollars come from and answering with balance-of-payments flows and central-bank reserves — which Friedman called **"complete nonsense."** His answer: **the source of eurodollars is the bookkeeper's pen** — interbank trades of ledger balances, not currency, not gold, not suitcases of cash.

Friedman's worked example: an **oil sheik** moves his **$1 million CD from Morgan Guaranty** (New York) to **Bank H of London** (which holds its own dollar account at Morgan Guaranty). Bank H keeps a 10% liquidity reserve and lends **$900,000 to UK Ltd** for trade with US firms, paying them with a check drawn on Bank H's Morgan Guaranty account. Result: the **US domestic money supply is unchanged**, but the **world supply of dollars has increased by $900,000** — created out of thin air. In the second-round example, the chain extends through further trades (a Russian timber deal and onward), leaving the world with **$9 million of dollar claims tracing back to a single $1 million check**. Aggregate this and you get Friedman's ~$30 billion — **"a fractional reserve system taking place outside of a fractional reserve system"** — occurring in the 1960s, while the gold standard was still nominally in force.

### Triffin's dilemma and the 1960 default

Robert Triffin identified the tension built into Bretton Woods from the start: the dollar was the global reserve currency, so **any growth in world trade required growth in offshore dollar supply** — but every dollar created beyond US gold reserves weakened the gold backing the system was supposed to guarantee. Supplying the world's money and maintaining gold convertibility are set in opposition. Townsend's gloss: reserve-currency status is a license to borrow and spend beyond belief without the consequences any other issuer would face.

Snider's stronger claim: the gold-exchange standard contained the weakness from 1944 — central banks could, and actively did, **circumvent the protocols meant to keep the dollar and sterling within their value bands, using swap transactions and eurodollars to run domestic monetary policy**. Central bankers never wanted to be constrained by gold. By the mid-1950s the gold backing was increasingly fiction. In his words, the system **"actually defaulted in 1960, not 1971"** — 1971 was merely when the fiction was officially abandoned.

### The missing money era of the 1970s

- **1974, FOMC records**: open-market desk manager **Charles Coombs** argued the Fed should **scrap M1 as a money-supply indicator** — no longer valid — move to M2, and anticipate needing an M3. The monetary system had become unrecognizable to the very authorities meant to define and control it. This during the Great Inflation.
- Princeton economist **Stephen Goldfeld** wrote the famous paper *"The Case of the Missing Money"*: money-demand forecasts persistently short of actual demand — **something else was satisfying the economy's demand for money**, and he couldn't characterize what.
- The candidates identified by the late 1970s: the **repo market** and **money market funds**. Repo's official treatment was chaos: the Comptroller of the Currency treated repos as collateralized loans in 1957, reversed to purchase-and-sale in 1964, and *Union Planters v. U.S.* (1969) ruled repos must be judged case-by-case. Yet in spring **1979 the New York Fed found corporations writing checks against segregated repo accounts** — repo already acting monetarily.
- Snider's framing: the money wasn't missing — **the official definition of money was**. "Missing money = wholesale": bank liabilities traded between banks (and corporations) that functioned as money but sat outside the aggregates.
- Partial explanations of the Great Inflation Snider accepts: **Allan Meltzer's "even keel" policy** (reserves injected ahead of Treasury auctions during Vietnam/Great Society deficits — and never removed) and the **Samuelson–Solow "exploitable Phillips curve"** ideology, demolished by Milton Friedman's Nobel-recognized work. But these aren't comprehensive; the eurodollar/wholesale dimension is essential, since the Great Inflation was global.

### Collateral becomes currency: the Salomon Brothers affair

The early-1990s proof that collateral had become money: trader **Paul Mozer**, bidding for Salomon Brothers, bid **more than 100% of Treasury auctions** — in June 1990 taking down the entire ~$8 billion auction. The Treasury's Deputy Assistant Secretary **Michael Basham** told him to stop; a **35% rule** (named derisively after Mozer) was created; he kept going. In **August 1991** the Treasury threatened to suspend Salomon from the auction process — a death sentence — prompting **Warren Buffett's** rescue: intervention with the Treasury Secretary, testimony before the House and Senate, and a two-page letter to shareholders published in October 1991 in the Wall Street Journal, New York Times, and Financial Times. The press called it "Mozer's inept little scam" because the profits were trivial — nobody could see the point. A **January 1992 joint investigation** (SEC, New York Fed, NYSE, NASD, OCC and others) found the real answer: sampling **98 dealers, every one was overbidding for GSE mortgage-backed auction paper**; some kept **two sets of books** to do it.

Why? **The repo market.** Repo had become a dominant part of bank funding, and repo is a collateralized loan — so **"on-the-run" collateral** (just-auctioned Treasuries, the most pristine available) was gold dust. **Rehypothecation** is the multiplier: the same security pledged again and again to multiple counterparties, so collateral itself becomes **currency-like**. Banks broke rules flagrantly to obtain it. The same dynamic — with MBS as the collateral — matured into the 2007–08 **run on collateral**. By the early 1990s the offshore market's scale was visible: the 1992 sterling crisis that made George Soros famous showed currency volumes **dwarfing anything any central bank could muster** — the Bank of England was simply overwhelmed — and the New York Times marveled that daily currency turnover exceeded the market value of the ten largest American companies.

### Greenspan the accidental genius

Contemporaries called Greenspan the maestro. Snider's reading: even Greenspan's most famous speech — the 1996 **"irrational exuberance"** remarks — was really about **missing money**: correlations on both the money-demand and money-supply sides had "long ago gone way off the rails." Unable to define money, the Fed slid into **discretionary federal-funds-rate targeting** (it has never stated when it switched). Because inflation stayed well behaved, everyone credited policy — but that's **correlation mistaken for causation**. The anomalies — the dot-com bubble and the housing bubble starting under the "Great Moderation" — don't fit, and point to the eurodollar system, not the Fed, as the true liquidity engine. The 1995 inflection in stocks, housing, and falling volatility coincides with the eurodollar system maturing into its final form (see RiskMetrics below).

### The Basel Accords: the risk-bucket machine

Because money itself had become undefinable, bank regulation shifted from the **liability side** (can you meet depositors?) to the **asset side** (are you a good bank or a bad bank?). The original Basel Accords — drafted in the 1980s, adopted in the US early 1990s — carved bank assets into **four risk buckets** with an **8% capital** requirement against risk-weighted assets:

| Bucket | Assets | Capital needed on $1B |
|---|---|---|
| 100% | Commercial loans, unqualified mortgages | $80M |
| 50% | Qualified mortgages, A-rated MBS/ABS | $40M |
| 20% | Higher-rated securities, guaranteed claims | $16M |
| 0% | Cash, Treasuries/sovereign debt | $0 |

The loophole from day one: pair any 100%-bucket asset with **"claims or guarantees" from "qualifying" entities** (initially GSEs like Fannie Mae and Freddie Mac) and it drops buckets — the capital charge falls. In 1995 **J.P. Morgan released RiskMetrics**, its proprietary catalog of asset-class risk behavior (the origin of popular Value-at-Risk), giving the industry quantitative cover for bucket assignments. **The same capital ratio could hide radically different leverage.**

Snider's stylized walkthrough: Bank A lends $40 (interbank/repo) to Bank B.

- Bank B buys **unqualified mortgages** (100% bucket): capital ratio falls 10% → **7.14%**, leverage 14:1.
- **Qualified mortgages** (50%): ratio → 8.33%, leverage still 14:1.
- **AA/AAA MBS** (20%): ratio → 9.25% — barely distinguishable from before.
- **Treasuries/cash** (0%): ratio stays 10% while leverage still rises.

So banks chose assets for the *bucket*, not the risk. Then the derivatives layer: if **Bank A writes Bank B $40 of gross-notional credit default swaps** on the mortgages, they move from the 100% to the **20% bucket** — capital ratio 9.25% at 14:1 leverage on otherwise risky loans, for a trivial premium. Crucially, **gross notional stays off Bank A's balance sheet** — only the market value shows, in the notes, bilateral and bespoke, with no visibility into who or why. Repeat with a second $40 interbank loan and Bank B reaches **18:1 leverage at an 8.62% capital ratio**; Bank A funds itself from **Bank C** (a Japanese bank or money-market fund holding yen), which obtains dollars through an **off-balance-sheet currency swap with Bank D**. Every element is simultaneously a hidden money multiplier **and a potential failure point** — which is what 2007–08 delivered, and why the Fed, "not set up to intervene in these spaces," failed time and again during and after the crisis.

### LTCM and off-balance-sheet accounting

**LTCM** was the pioneer of running almost everything off balance sheet, using present-value-of-future-cash-flows accounting on derivatives. At the September 1998 rescue meeting, **Greenspan asked for LTCM's balance sheet; Fed vice chair McDonough answered there was no point — "there's nothing on there that is of any use. It's all off balance sheet."** Wall Street's takeaway was not caution but emulation: "LTCM just did it wrong. We'll do it right."

### Real-world proof: Primus, AIG, and Gramm-Leach-Bliley

- **Primus** — founded by **Tom Jasper**, who practically invented the modern standardized interest-rate swap in 1985 and became ISDA's first chairman. At the 2004–05 peak of the housing mania Primus had written roughly **$13.5–14 billion of gross-notional CDS across 535 entities** — all in the footnotes; the balance sheet showed only market values. Roughly **$600 million of cash and investments, net of about $200 million of debt — about $400 million of capital behind $13.5 billion of guarantees**. Primus failed in 2009 — not from paying claims, but because the probability of ever paying shifted and the thin capital couldn't support it.
- **AIG** — transformed from an insurance company into a money-dealing company: regulatory-capital-relief CDS (its **2007 annual report** states the buyers were primarily European banks seeking capital relief) plus **securities lending** (rehypothecation of its portfolio). Its failure was **liquidity, not solvency**: rising modeled volatility in 2007–08 triggered collateral calls it couldn't meet. When the Fed took over the AIGFP portfolio it **never lost a nickel — it made about $4 billion**. The issue was never default; it was volatility and margin. Paulson was right that an AIG failure would have been catastrophic.
- **Gramm-Leach-Bliley (1999)** — sold to the public as one-stop financial shopping for consumers. The real motive: **Citigroup** (merging with Travelers) wanted the deposit bank inside the shadow banks' balance-sheet leverage game; repealing **Glass-Steagall** removed the last legal barrier between depository and shadow banking. **Hank Paulson**, who lobbied for the repeal as Goldman's head, then ran the cleanup as Treasury Secretary.

### Parabolic derivatives and the Fed's powerlessness

OCC call-report data show credit derivatives — and interest-rate derivatives — going **parabolic through the 2000s**, with **zero response to the Fed's tightening that began June 2004**. The lesson: **the Federal Reserve is not the center of the monetary system**. The eurodollar system evolved entirely outside it — cross-border derivative trades between American and European banks, European banks supplying offshore dollars to Japan — and by the time the Fed sensed something was wrong it was too late. Banks believed the system had been tested (1997–98) and assumed a Fed liquidity backstop if ever needed: minimal reported risk combined with monumental actual risk.

### How big it got, and why it matters now

- **BIS, October 2009**: global banks' offshore claims grew from about **$10 trillion in 2000 to $34 trillion by end-2007** — an enormous expansion of cross-border credit creation "in a place that wasn't supposed to exist."
- The eurodollar boom stoked **both** the US housing bubble **and** emerging-market "hot money" bubbles — which is why German banks were failing on housing in Florida, California, and Arizona.
- Officials and economists still, in Snider's words, **deny eurodollars are money**; the working assumption is that the US is a closed monetary system. Janet Yellen analyzes money without any of this existing in the model.
- Post-2008 QE disappointed in the US, Europe, and Japan because the eurodollar system itself was collapsing: **"once it started to fall apart, there was no stopping it."** The weak global recovery is a monetary problem the Fed cannot fix while it believes it sits at the center of money creation.
- Snider's closing: *"You can't know the future without studying the past... If you don't understand what happened 10 years ago, let alone 50 years ago, you don't really know where we are or why we are where we are."*

## 3. The Dragon Portfolio (with George Gammon)

<!-- Source video: "DragonPortfolioGammonJune262020 (1080p with 25fps).mp4" -->

A June 26, 2020 webinar: **Patrick Ceresna** (Big Picture Trading) with **George Gammon** (Rebel Capitalist), translating Chris Cole's Artemis Capital Management report — ***The Allegory of the Hawk and the Serpent*** ("you've got to do it — it's free, it's online") — into a portfolio a retail investor can actually run.

### The framework: the serpent and the two wings of the hawk

- **The serpent** = secular periods of financial stability: short gamma builds, the market stays perpetually in trend with low volatility, and the regime self-cannibalizes in its late stage — corporate buybacks, passive investing, demographic declines feeding the loop. Everything that has worked for the last 40 years is serpent behavior.
- **The hawk** = the period of secular change, with two wings:
  - **Left tail — the deflationary deleveraging.** Asset-price deflation: savings wiped out, liquidity gone, stocks and real estate imploding together. The 1930s Depression and 2008–09 are the canonical examples.
  - **Right tail — the inflationary deleveraging (financial repression).** The goal is to inflate the debt away — flood the system with money — and even when asset prices rise substantially, **your standard of living does not improve**. Example: 1972–74, when the market fell more than 50% in nominal terms — far worse in real terms.
- Cole's spirit: build a portfolio that survives **100 years of these alternating wings**.

**The open debate** (with Harley Bassman on MacroVoices the day before): does inflation produce asset-price inflation? In the 1970s it did not (stagflation); in other episodes it did. Which one we get is the big question. The extreme case — **Weimar Germany**, or Venezuela today — shows nominal equity gains are an **illusion** if the denominator (the currency) is being diluted: you had to hedge the currency to keep anything. Gammon's favorite illustration: US housing since 1900, inflation- and size-adjusted, was **flat to the mid-1990s** — it protected you from inflation but earned no real return.

### Why the traditional 60/40 dies

Cole's cycle map: **1929–46** secular decline; **1947–63** secular rebirth — actually one of the best-documented **financial-repression** periods (the world crushingly over-indebted from WWII, Treasury yields pinned below natural levels to inflate away the debt — bonds did poorly); **1964–83** stagnation (rates rising, bonds terrible); **1984–2007** secular boom (bonds' great bull market — and, via the rates correlation, one of the greatest real-estate booms). Bonds only hedged well in the deflationary wing. Today we sit at the **lower bound** — the rates tailwind that powered 60/40 for forty years is missing for the next secular phase (10+ years).

Ceresna's call: we are more likely entering a **financial-repression rebirth than a 1970s echo**, because the system cannot service higher rates. Gammon's debt math from the US Debt Clock: **total US credit stock ~$79 trillion** (all levels — government, corporate, personal) with **~$3.8 trillion of annual interest**; in 2008 it was ~$50 trillion of stock and ~$3.9 trillion of interest — **debt up $30 trillion, interest unchanged**. If rates merely returned to 2008 levels, the payment shock would be a disaster. Gammon: developed governments are **"a subprime borrower in 2006 with an adjustable-rate mortgage."** The ways out of debt: grow, raise taxes, default, inflate, or austerity — austerity "crossed off in about two seconds" (no politician will impose it unless imposed from outside, Greece-style); realistically, inflate and repress.

And **"buy the dip"**: Cole shows that across the last five secular cycles it would have gone bust in three of them. Secular periods run 20–30+ years; when the regime shifts, it is significant.

### Construction philosophy: anti-correlation, negative carry, and the amateur's test

- You are looking for **anti-correlated assets** to smooth the whole. Counterintuitively, accept **negative carry**: the hedge "does nothing" (or bleeds a little) while everything else works — *that is it working*. "If your portfolio is doing everything right, the options component should be doing nothing."
- Brent Johnson's test for any fund: ask **"what is going up in your fund?"** — if the answer is *everything*, it's too risky.
- **Portfolio construction is not trading.** Traders want the right side of the trend; portfolio managers build something they don't touch often and let time work.

### Cole's optimal allocation — and the retail translation

Cole's backtested optimum: **24% equity, 18% fixed income, 21% long volatility, 18% commodity trend, 19% gold.**

The critical interpretation: **"21% long volatility" is an allocation to a volatility fund's delta-dollar exposure — not 21% of your cash into options.** That would be "insanity" at retail and could get zeroed. Evidence: in Nancy Davis's IVOL fund, only about **4% of investor cash** is in the actual option positions — the rest sits in bonds. The retail target: **option positions delivering roughly $20,000 of delta-dollar volatility exposure per $100,000 portfolio.** Equity can run overweight (30% vs 24%) because the option overlays embed the left-tail hedge.

### The $100,000 build (Interactive Brokers; retail-accessible products only — no ISDA/OTC access assumed)

| Sleeve | Implementation |
|---|---|
| Equity 30% | 100 shares SPY (~$30,000). Round lots make the option overlays clean. International investors may substitute their domestic market in domestic currency. |
| Gold 20% | ~120 shares GLD (~$20,000). Gammon personally holds 10% physical in a safe ("KISS"); Ceresna prefers keeping it in-account to trade options around it. Gold miners are highly correlated to bullion — you can mix them into the gold sleeve, but they are *not* equity diversifiers ("gold miners behave nothing like the S&P 500 much of the time"). |
| Bonds ~18–19% | ~400 shares **IVOL** ($10–11k) + ~100 shares **BND** (~$8k). |
| Commodity trend | Currently short: short 300 DJP (~$5k) + short 200 USO (~$5k); flip long on the bullish moving-average crossover. Cap total commodity exposure ~$20k (Cole's sizing assumed commodity volatility). |
| Currency trend 20% | Long 200 FXE (~$20,000) on the current signal. |
| Cash | ~$20,000 residual — swings with the trend sleeves. |

**Why IVOL is the bond sleeve**: Nancy Davis's Quadratic ETF is ~**86% TIPS** (roughly 2–3% inflation-protected income, about seven cents a month in the example) plus **constant-maturity swaps** — instruments retail investors can't touch — that function as **call options on a 2s10s steepening**: if long-end yields blow out in an inflation scare, the curve steepens (short end pinned by the Fed) and the fund "makes a shitload of money." In other words, **long bond volatility is built into the bond allocation** — it covers part of the volatility sleeve for free. Plain bonds at the zero bound offer little asymmetry: some convexity left if the long end drops another percent toward zero (a 10%+ price move), but as a hedge they are a **diminishing diversifier**. (Elsewhere in the course IVOL is described as 87% SCHP — the Schwab TIPS ETF; both figures are his live descriptions of the same sleeve.)

**Why currencies get oversized**: commodities run ~**25% implied volatility** (DJP) versus ~**7.4%** for the euro (FXE). Cole's 18–19% trend allocation was sized at commodity volatility, so a currency trend sleeve can run **larger** — $20k currency + $10–20k commodity ≈ the same volatility-adjusted hedge as Cole's sleeve.

**Static vs dynamic sleeves**: SPY, gold, and the bond allocation are **locked allocations — rebalanced by weight only (e.g., quarterly), zero market timing**. The commodity trend, currency trend, and volatility overlays are **100% market-timing sleeves**.

### Trend following: the rules and the psychology

- Cole's backtest was deliberately simple: a **50-day moving average on a broad commodity basket — long above it, short below it.** Nothing else.
- Ceresna's objection: a raw 50-day MA whipsaws — on USO it produced an "epic rinse cycle" of in-and-out signals. His fix: a **40/50-day moving-average crossover filter** (exponential or simple — roughly equivalent), reducing the churn to a handful of signals a year. Target: **no more than two to four decisions a year.** (This same 40/50 EMA crossover becomes the commodity-trend signal of the Tactical Portfolio in Part V and is saved as a TradingView indicator template in Part VI.)
- Execution style is personal: make it **black-and-white at the daily close**, or **leg in** — change 50% of the allocation on the cross and the rest after two confirming closes. Either way, **accept the fake-outs**: they are the price of riding the 80% USO decline. "Trend following is blackjack — it's rules-based." If your bias says the dollar rallies but the system says long the euro, you follow the system: that's the point of backtesting.
- **Renko alternative**: 45-degree blocks sized by a 14-period average true range. The chart speeds up when markets trend (2008 printed a dense column of blocks; 2019 almost nothing) and goes silent in ranges — it removes noise by refusing to print when price doesn't move. Add a 10/20 moving average on the Renko for clean signals. "If you like it, use it; if not, use the 50-day."
- **Contango doesn't sink trend followers**: ETF roll costs punish perpetual longs, but a trend follower is short half the time (positive carry in contango) and long half the time — over the cycle it washes out.
- Product substitutions are fine as *stylization*: XOP (energy equities) tracked the oil trend well ("no bull market in gold miners while gold crashes"), and deep-in-the-money **puts replicate shorts** when borrowing is hard or margin-constrained (two USO $32 puts ≈ the delta dollars of shorting 200 shares for ~$1,000 outlay). But Cole tested the *commodities themselves*, not producers.
- **Psychology is the binding constraint**: run a system you don't fully believe in and you *will* abandon it at the first drawdown. Backtest it, personalize it, and only then will you hold discipline through the chop.

### Long volatility — without buying insurance

Cole models "active long volatility" as buying volatility **in the direction of the market after a move greater than 5% on a rolling three-month basis** — and he explicitly distinguishes it from portfolio insurance or tail hedging: it "foregoes continuous protection for more dynamic hedging to lower costs." Ceresna's critique: that signal would have **failed you spectacularly in February–March 2020** — by the time the 5% three-month trigger printed, volatility had already exploded. His retail simplification: **apply the same moving-average filter to the S&P** — buy downside volatility/gamma when below the 50-day, right-tail gamma when above it. And never confuse this with continuous put-buying, which "taxes your performance like car insurance you never crash into."

Three demonstrated overlays (sized **per 100 shares of SPY**; roll quarterly; **never hold a backspread to expiration** — the max-loss "V" only exists at expiry):

1. **VIX call backspread** — e.g., the **30 x 40 for October**: sell one 30-strike call (~$840 credit), buy two 40-strike calls (~$1,000), ≈ **$200 net debit**. If volatility normalizes (bull market), it expires nearly worthless — a $200 tax. If VIX blows to 50+, it pays explosively. **Max pain is VIX pinned near 40 into expiry**: the $10-wide spread = **$1,000 per combo** if held to the bell. You are long gamma (+$4.50 vs –$2 portfolio gamma). Logic: volatility either collapses (new bull) or skyrockets (new bear leg) — flatlining at 40 is the least likely state. Why October: this is a portfolio, not day-trading — Cole rebalances monthly/quarterly; give the trade 3+ months of runway. (See Part III's volatility-trading section for why Ceresna nonetheless warns most retail investors away from VIX options themselves.)
2. **SPY put backspread at ~zero cost** — sell one November 307 put (~$25, ~$2,500 credit), buy two November 270 puts (~$12 each, ~$2,500). The **skew** is the price of admission: low-strike puts price near **50% implied volatility versus ~30 at-the-money** — "the market rises on an escalator and drops in an elevator," so crash insurance always carries worse. Accept it and buy near zero cost: a routine pullback expires worthless for nothing; a March-style crash pays big. **Worst case: the market flatlines right at the short strike while volatility normalizes** — a couple thousand dollars — though being long vega, a vol spike pays even before the level moves. People don't hedge 10% drops ("you just hold"); you insure the 30–40% events.
3. **Upside participation** — calls are structurally cheaper than puts, so for right-tail exposure above the 50-day: buy a November 320 call for ~$12 (≈ $12,000 of delta dollars), then **sell a higher call (~$400) and optionally the covered call on the 100 SPY shares (~$400)** to offset the carry; a call backspread works too.

**Sizing**: it's about **aggregate delta-dollar exposure** — two to three volatility positions per 100 SPY shares; a **1x2 SPY ratio spread**; up to a **5x10 VIX backspread**. Scale everything with portfolio size (5x at $500k). Use SPY (American-style, small) for $100k accounts; SPX (European, cash-settled, much larger) optional. Roll systematically every ~3 months; **monetize immediately on extraordinary moves** — an S&P drop of 500–1,000 points or a VIX spike to 50–60: "you don't look a gift horse in the mouth." Cole's own 70-year rolling-straddle test (on MacroVoices) showed positive carry — but the point of the volatility sleeve was never income; it is **diversification that pays when everything else goes wrong**.

### Q&A and debate points

- **Why deflation wipes out savings**: only if your savings are held *in assets*. Cash is king in deflation — but crushed in inflation, and you don't know which wing is coming. Hence the barbell.
- **Advisors**: most run model portfolios and won't customize. Accredited investors can simply allocate to a Cole-style long-vol fund directly.
- **Versus Harry Browne's Permanent Portfolio**: raised by the audience; the hosts admitted they hadn't studied it and deferred the comparison.
- **Modern portfolio theory / efficient frontier**: backtested in the one regime that favored it (1982–2007) and it assumes correlations hold. In liquidity crunches **correlations go to one** — "when shit hits the fan, everything hits the fan all at once" — and **"liquidity is a coward": there when you don't need it, gone when you do.** Cole's project is engineering genuinely anti-correlated sleeves instead. March 2020, when everything sold off at once, was the live proof.
- **Minimum size**: a Dragon portfolio with $10–20k is **overkill**. A young saver's wealth engine is income and savings rate; the deposits *are* the wealth creation. A 30% drawdown on a $10k all-equity account is survivable — "take a line of credit, double down, ride the other side." The real audience: retirees with $250–500k of life savings who must weather the storm. Learn it small, deploy it large.

## 4. The Economic Machine: Ray Dalio's Template

<!-- Source video: "How The Economic Machine Works by Ray Dalio (1080p with 24fps).mp4" -->

This module is Ray Dalio's famous 30-minute animated explainer, *"How the Economic Machine Works,"* included as third-party foundational context (the transcript is the video's narration) — the template Dalio credits with helping him anticipate and sidestep the 2008 crisis.

### Transactions and the three forces

- **The economy is the sum of its transactions.** A transaction: a buyer exchanging **money or credit** with a seller for **goods, services, or financial assets**. Total spending (money + credit) divided by quantity sold = **price**. A market = all buyers and sellers of one thing; the economy = all transactions in all markets.
- The biggest buyer and seller is **government** — two parts: the **central government** (taxes, spends) and the **central bank** (unique: it controls money and credit via **interest rates and printing money**).
- Three main forces drive everything: **(1) productivity growth, (2) the short-term debt cycle (~5–8 years), (3) the long-term debt cycle (~75–100 years).** Layer them on top of each other for a template for tracking the economy.

### Credit mechanics

**Credit is the most important and least understood part of the economy** — the biggest and most volatile. When a lender and borrower agree on a promise to repay **principal plus interest**, credit is created **out of thin air** — by any two people — and instantly becomes **debt**: an asset to the lender, a liability to the borrower; both disappear when the loan is repaid. High rates suppress borrowing; low rates expand it.

A **creditworthy** borrower has two things: **ability to repay** (income relative to debt) and **collateral** (assets to sell if they can't). The engine: **one person's spending is another person's income** — spending rises, incomes rise, creditworthiness rises, borrowing rises, spending rises more. Self-reinforcing, and therefore cyclical.

The bar-tab analogy: paying cash settles the transaction immediately; buying the beer on credit starts a tab — you and the bartender just created an asset and a liability out of thin air, and nothing settles until the tab is paid. Scale: **US credit ~$50 trillion versus money ~$3 trillion** — *"most of what people call money is actually credit."*

### Productivity versus credit

Without credit, the only way to spend more is to produce more — a smooth productivity line. Credit lets you **consume more than you produce** when you borrow and **forces you to consume less than you produce** when you repay: **borrowing is pulling spending forward from your future self**, and any time you borrow, you create a cycle. Hence Dalio's split: **productivity matters most in the long run** (it doesn't fluctuate much), **credit matters most in the short run**. Credit is not inherently bad: bad when it finances overconsumption that can't be repaid (a TV), good when it allocates resources to production that generates the income to repay (a tractor that harvests more crops).

### The short-term debt cycle

Expansion: credit-fueled spending grows faster than production → prices rise → **inflation** → the central bank **raises rates** → borrowing falls, debt service rises → spending slows → **deflation** and **recession**. If the recession is severe and inflation is no longer a problem, the central bank **lowers rates** → the next expansion. The cycle is **controlled primarily by the central bank** and repeats every **5–8 years** — each cycle ending with **more growth and more debt**, because people push it: the human inclination to borrow rather than repay.

### The long-term debt cycle and the deleveraging

Define the **debt burden = debt / income**. Over decades, debts rise faster than incomes; lenders lend even more freely because *lately* everything has been great — incomes rising, assets soaring, the stock market roaring. Buying goods and financial assets with borrowed money en masse = a **bubble**; rising collateral keeps everyone looking creditworthy. At some point **debt repayments grow faster than incomes** → spending cut → incomes fall → creditworthiness falls → borrowing falls → the spiral reverses. **The long-term debt peak: US 2008, Japan 1989, US 1929.**

A **deleveraging** follows: spending cut, incomes fall, credit disappears, asset prices drop, banks get squeezed, stocks crash, social tensions rise. Borrowers dump assets into a falling market; collateral values drop; credit dries up further. **The difference from a recession: interest rates can't save the day — they're already at 0%** (US in the 1930s and 2008). Lenders realize the debts are too large ever to be repaid; borrowers feel crippled. **Lenders stop lending; borrowers stop borrowing.** The economy itself has become not creditworthy.

**The four ways debt burdens come down — present in every deleveraging in modern history:**

1. **Cut spending** (austerity). Paradox: because one person's spending is another's income, incomes fall *faster* than debts are repaid — **the debt burden gets worse**. Deflationary and painful; unemployment rises.
2. **Reduce debt** — defaults and **restructuring** (lenders get paid less, later, or at lower rates: "lenders would rather have a little of something than all of nothing"). When borrowers default, the lender's "asset" evaporates — people discover **much of what they thought was wealth isn't really there** (the bar tab that never gets paid). Bank runs, depression, also deflationary.
3. **Redistribute wealth**. Deficits explode (falling tax receipts + rising unemployment spending); funding them means taxing the wealthy — resentment on both sides; social disorder can follow, within and between countries. In the 1930s this **led to Hitler, war in Europe, and depression in the US**.
4. **Print money**. Rates are already at zero; printing is **inflationary and stimulative** — used to buy **financial assets and government bonds** (the Fed printed **over $2 trillion** in 2008). The asymmetry that forces cooperation: the **central bank can print but only buy financial assets**; the **central government can buy goods and services and put money in people's hands but can't print**. Central-bank purchases of government bonds fund deficits and stimulus, raising incomes — and lowering the economy's total debt burden.

**The beautiful deleveraging**: balance the three deflationary levers against the inflationary one so that **debts decline relative to income, growth stays positive, and inflation isn't a problem**. Printing money is *not* inflationary **if it offsets falling credit** — a dollar of money-spending moves prices exactly like a dollar of credit-spending. The arithmetic requirement: **income growth must exceed the interest rate on the debt** — at 100% debt-to-income with 2% interest and 1% income growth, the burden never shrinks; print enough to push income growth above the interest rate. The danger is abuse, because printing is easy: Weimar Germany in the 1920s. Done right, it takes roughly a **decade ("lost decade")** for debt burdens to normalize, followed by the **reflation** phase as creditworthiness returns.

**Dalio's three rules of thumb:**
1. **Don't have debt rise faster than income** — the burdens will eventually crush you.
2. **Don't have income rise faster than productivity** — you'll eventually become uncompetitive.
3. **Do all you can to raise productivity** — in the long run, that's what matters most.

Most people — including most policymakers — don't pay enough attention to these.

## 5. Historical Lessons: John Law, the Mississippi Bubble, and the Disney Money Shorts

<!-- Source videos: "John Law and the Mississippi Bubble (360p with 23fps).mp4"; "Scrooge McDuck and Money 1967 (360p with 29fps).mp4"; "Walt Disney Chicken Little 1943 (240p with 25fps).mp4" -->

These are **third-party films included deliberately by the course**: a documentary-style animated short on John Law, plus two Disney educational shorts — *Chicken Little* (1943) and *Scrooge McDuck and Money* (1967). Their money-history, inflation, and crowd-psychology teaching is summarized below.

### John Law and the Mississippi Bubble — the economics of the story

The setup: **Louis XIV borrowed most of the gold in France** (Versailles among other splurges). When he died, "the rich were poor and the poor were poorer, and they wanted their money back." The new king was five years old, so the **Regent** ruled — and tried two fixes: (1) repay creditors with **IOUs (government bonds)**, which satisfied nobody because everyone suspected the cupboard was bare; (2) **devalue the remaining gold coinage**, which brought commerce almost to a standstill.

Enter **John Law**, the Scottish economist who had spent 20 years traveling Europe studying currency systems. His proposal: **paper money** — a bank where people deposit gold and receive banknotes, receipts that are "just as good as gold" but far more convenient. The notes became so popular the Regent proclaimed them **the official currency of France** — which also put the government's hand on the printing press. The film's key economic line: **"The Regent didn't understand that a paper currency must represent real wealth. But John Law did."**

Law's magnificent dream: develop **Louisiana** — "rich in diamonds, gold, furs, rubies" — via a **company whose shares could be bought with the Regent's IOUs**. The venture itself never got off the ground — "it remained an undeveloped swamp" — but **the shares were the thing**: a secondary market in paper money, prices skyrocketing, every new share issue besieged by crowds. The trading street was gated at both ends — **one gate for the nobility, one for everyone else** — flung open at 8 a.m. daily; some made fortunes **renting their backs out as writing desks**; and the mania coined a new word: **millionaire**.

The unraveling is a checklist of every failure mode of paper systems:

- **The convertibility test.** One January morning a wealthy prince presented his paper for gold — it took **three wagons** to carry away. The truth emerged: **there was only enough gold to match one-fifth of the paper in circulation**. Word spread; the conversion stampede began.
- **Edicts instead of credibility.** Devalue gold (to stop conversions); declare printing money illegal; declare selling gold illegal; close the bank; have the company buy back shares — **paid for with more printed money** (Edict 3 disregarded); then Edict 8: gold coin itself is illegal.
- **Breaking the guarantee.** Prices rose so insanely that Law was forced to break his promise — notes worth **half their face value** — turning Paris into "a thief's paradise." Gold was re-legalized, and in the final stampede **15 people were crushed to death**. The mob turned on Law; he fled and slipped across the border in disguise — broke, never to set foot in France again.
- The **four-year reign of paper money** that began so successfully ended in utter disaster — the first of the "rags to riches to rags" stories. Immediately after, England's **South Sea Bubble** repeated the pattern with shares in the riches of South America.

Lessons: paper money must represent real wealth; convertible notes work until convertibility is seriously tested (a 20% gold cover cannot survive a run); royal edicts cannot repeal confidence; and coercive legal-tender measures (banning gold) accelerate collapse rather than preventing it.

### Scrooge McDuck and Money (1967) — money history and household economics in brief

Disney's educational short has Uncle Scrooge teach Huey, Dewey, and Louie what money is:

- **Money must circulate**: "Like the ocean currents control the world's weather, circulating money controls the economy." Idle money is stranded — it can't be eaten, worn, or used.
- **A pocket history of money**: Roman soldiers paid in salt (*salarium* — the root of *salary* and "worth his salt"); **pieces of eight** cut into **bits** (hence "two bits"); tiny Greek **obols** carried in the mouth; the stone wheels of Yap; barter needing a **standard of value** (a knife priced at 3.5 goats), then metals, then the coin, then **paper backed by the government's name**, then **credit** ("payment deferred") — with the warning that "when spending grows so easy, it's hard to save a dime."
- **Scale and inflation**: a billion dollars stacked reaches ~**800 times the height of the Washington Monument**; a six-foot ribbon of bills would girdle the earth — walking it nonstop, about **32 years**. On paper money's hidden tax: your hat full of bills buying what your childhood piggy bank used to — **"what you can buy with what you've got, that's what counts."**
- **Economics = household management** (from the Greek): the **budget** — income as a pie with a piece for everything: rent, installments, taxes ("taxes are the funds governments must get to run their households"), and **always save a slice for yourself**. Wealth came from making "the little slices grow" — putting money to work, and investigating the facts before investing (the nephews buy a share for $1.95 plus a three-cent fee).

### Chicken Little (1943) — a fable of crowd psychology

Not a money film — its inclusion is about panic, propaganda, and herd behavior. **Foxy Loxy** cannot raid the fortified farmyard directly (the fence, the locks, the farmer's shotgun), so he works by the book — literally, his psychology manual: **"To influence the masses, aim first at the least intelligent"; "If you tell a lie, don't tell a little one — tell a big one"** (the sky is falling); **"Undermine the faith of the masses in their leaders"** (a whispering campaign portraying level-headed Cocky Locky as corn-pickled and dictatorial); and **"By the use of flattery, insignificant people can be made to look upon themselves as born leaders"** — whereupon the flattered fool, Chicken Little, leads the flock into the fox's cave. When a chick protests the ending, the narrator answers: **"Don't believe everything you read, brother."** Market moral: doom narratives travel fastest through the least informed, and the loudest newly crowned "leader" is usually working for the fox.

---

# Part II — Options Foundations

<!-- Sources: Options Bootcamp Parts 1-4; Options Master Program Modules 01-05; OptionsFundamentals; OptionsforIncome; Option Writing Bootcamp -->

The foundations are taught twice in the corpus — once as the four-part **Options Bootcamp** (introduction, pricing, Greeks, application) and once as the five-module **Options Master Program** (introduction to options, contract specifications, contract pricing, understanding volatility, understanding time) — plus the standalone **Options Fundamentals** session, the **Option Writing Bootcamp**, and the **Options for Income** service material. This Part merges them into one treatment: mechanics, pricing, volatility, time, Greeks, and then the two income/writing programs.

## 1. What an Option Is: Rights, Obligations, and Counterparties

<!-- Sources: Options Bootcamp Part 1; Options Master Program Module 01; OptionsFundamentals; Option Writing Bootcamp; Investing Smarter: Pitfalls of Stop Loss Orders -->

An option is a **contract between two counterparties to do business in the future** rather than today. In the stock market you buy or sell shares outright; an option lets two individuals contract now for a transaction that may happen later. The **buyer** pays a **premium** and acquires a **right**; the **seller/writer** receives the premium as income and undertakes an **obligation**. Every option is defined by two parameters: a **strike price** (the specific contractual price) and an **expiration date** (the specific period of time, after which the right dies) — and in the overwhelming majority of cases each contract controls **100 shares** of the underlying (options on futures settle against one futures contract instead — a later refinement).

Ceresna's core teaching device is to keep returning to this rights-and-obligations foundation: when sizing trades or wondering why an option's price moved, always go back to "what exactly am I buying or selling at that fundamental level." He also stresses that a retail investor can be **either counterparty** — there is no rule that says a retail account may only buy options. If a premium looks too expensive to buy, that is precisely the instinct that can make selling it attractive. Two counterparties with opposite views on the same contract is what makes a market; market makers often just sit in the middle as delta-neutral middlemen clipping the spread.

### Calls and puts: a reciprocal pair

There are exactly two types of options. A **call option** is the right to *buy* the underlying at a fixed price; a **put option** is the right to *sell* it at a fixed price. Mathematically they are valued the same way — they are reciprocals of each other, with the same time-decay and volatility characteristics in opposite directions. In every transaction: the buyer's only capital at risk is the premium paid; the seller is obligated to deliver (call) or take delivery (put) at the strike if exercised, and keeps the premium either way.

### The truck option: an over-the-counter option in miniature

Ceresna's founding example, told in every introductory session with drifting figures (a $20,000 truck with one month of rights in one telling; a $10,000 Hummer with two months in another — the mechanics are identical). The canonical version: he mentions thinking of selling his truck for **$20,000**. Luke knows the truck lists for well above that on Auto Trader, so instead of buying it outright he offers Patrick **$500 cash for the right to buy the truck at $20,000 any time over the next month**; Patrick must guarantee the $20,000 price and cannot sell to anyone else in the meantime. Deal. Patrick now has **$500 of income** he can spend immediately ("I could have bought myself a new iPad... paid my rent") while Luke holds the call.

Luke lists the truck at $25k; a buyer offers **$23,000**. Luke exercises, pays Patrick $20,000, flips for $23,000 — but made **$2,500 profit, not $3,000**, because the $500 premium is sunk. And if Luke had discovered the chassis was rusted through and the truck was only worth $15,000, he would simply **walk away**, losing $500 instead of losing $5,000 by overpaying for the truck. That asymmetry — capped downside, open upside, and a paid-for decision window — is the entire point of an option. In one later retelling (the stop-loss webinar), comparables were $30,000, Luke's flip was $24,000, and the net was $3,500 — same story, same lesson.

A private handshake like this is an **over-the-counter (OTC)** contract, and OTC trading carries real counterparty risk — default, credit, fraud, insolvency. Institutions still trade this way (Carl Icahn's Herbalife call was an OTC deal with a specific market maker, so he carried counterparty risk). The 2008 Lehman failure is the reference case for why OTC is fragile: when banks might fail, every direct bilateral deal becomes suspect.

### Workshop examples: calls and puts from the bootcamps

**Apple call — Jackie and Peter.** Jackie is bullish Apple, doesn't own it, and wants risk-managed participation. Peter owns Apple, sees limited near-term upside, and wants extra cash flow. Stock at **$160**; they transact the **$170 strike** call at **$2/share**. Jackie pays **$200** (a debit — the right to buy at $170). Peter receives the **$200 as income**, collateralized against shares he owns — this is **covered call writing**. (The Master Program retells the same structure as **Jane and John**: Apple at **$250** on March 2nd, a **$250 strike call expiring April 17th** — six weeks — for **$8/share**; Jane pays $800, John collects $800 and owes 100 shares at $250 if exercised.)

**Sunoco put — Doug and Amy.** (Stock trading around **$31** — one transcript garbles it as "$131," but the strike of $30 and Amy's $29.30 break-even pin it to the low 30s.) Doug owns SUN and fears downside; he buys the **$30 put at $0.70/share = $70** per contract, locking a guaranteed exit price. Amy doesn't own the stock, thinks it cheap, and sells the put as a **premium harvester**: she keeps 70 cents of income; her **break-even is $29.30** — a level she's happy to own the stock at even if it dips below temporarily.

**Apple put — John and Jane again.** Same two participants, opposite trade. **John** owns Apple long-term and wants to lock in a sale price as insurance without selling. **Jane** would love to own Apple but wants to accumulate at lower prices while earning income. They agree on a **$240 strike put** (stock at $250), April 17th expiry, **$5** per share. John pays **$500** for the right to sell 100 shares at $240; Jane receives the $500 and is obligated to buy them at $240 on demand. If assigned, Jane's effective cost is $240 minus the $5 collected = **$235 break-even**. The choice of role — insurance buyer (hedging) or insurance seller (income plus accumulation) — depends on where you think your edge is.

### The "mulligan," insurance, and freedom from diversification rules

Ceresna's three favorite framings for why options beat out-and-out stock for an entry:

1. **A call is a mulligan in golf** — a second shot at your first entry. If the trade turns out to be early, you took a small loss but you're "not stuck with a stock that you have to dollar-cost average or manage a big loss on. You can walk away and rediscover where the entry was."
2. **A put is car insurance.** Nobody buys car insurance hoping to crash; you buy a put to *contractually secure a guaranteed sale price*. (Car insurance literally *is* a put: you are the premium payer, the insurer underwrites the obligation, the car's value is the underlying; total the car and the insurer buys the clunker for replacement value — "you're buying a put option on your vehicle.") Puts can also speculate on the downside — "buying insurance on something you don't own" — but their classic use in this course is the **protective put**.
3. **Knowing your worst case frees you from modern portfolio theory.** MPT manages risk through diversification and uncorrelated assets. Ceresna: if a put removes catastrophic loss, "I can have half of my account in one trade. There's nothing wrong with that, because the put option has removed all the risk of catastrophic loss." The practical payoff he reports from his own trading: he stopped losing sleep — and un-hedged stock positions breed the anxiety that causes impulsive exits, because "it's that anxiety that causes impulsive moves where you get out or you do something that you didn't want to do."

Stops approximate the protection, but with a real hedge "you already know what your worst scenario is," so you can let the position breathe. (The full case against stop-loss orders — volatility stop-outs, gap slippage, stop clustering — is in Part VI, Section 4.)

### Exchanges, clearing corporations, and counterparty risk

- There must be **a buyer for every seller**; each new handshake creates **one unit of open interest**. Closing both sides removes one unit. Buyer and seller positions are always mirror images — a zero-sum pairing, one long, one short, per unit of open interest.
- Retail trades **exchange-traded** options. The **clearing corporation makes options fungible** (interchangeable between traders — "I can buy an option from Luke and sell it to Jerry"), so retail has **no counterparty risk** and never needs to know who was on the other side. The clearing corporation guarantees settlement, backed by the brokerage margin system (your broker is responsible for ensuring clients can honor their deals). Exercise instructions flow from your broker to the clearing corporation, which overnight assigns the obligation to some short holder via allocation/lottery methods.
- **Liquidity is contracted.** The exchange pays **market makers** (broker-dealer firms) to provide an active bid and ask at all times, even in fast markets when spreads widen.
- Order-entry vocabulary that follows: both counterparties in a new trade are *opening* (one **buy to open**, one **sell to open**); unwinding is **buy to close / sell to close**.
- The only retail-relevant counterparty failure is a full 2008/Lehman-systemic event; your broker manages your direct margins.

### Market makers, spreads, and the liquidity rule

An option's theoretical price comes out of a math equation (six variables — see Section 3). Market makers — up to **10 or 20 competing on one stock**; you might see Wolverine on the bid and Citadel on the ask, or a retail order on one side — quote a **spread around that theoretical value**: theo $1.25 might be shown as **$1.20 bid / $1.30 ask**. Two rules of thumb:

- **"Market makers will always provide you liquidity, but they may not always provide you the best price for that liquidity."** Fills land somewhere in the middle of the spread; you can always work for mid (another retail order may cross you, or a dealer may be happy to de-risk at breakeven). Demanding a fill at theo means asking the dealer to work for free — they won't sustain that business.
- **Spreads widen in fast markets.** After a 2018-style vol spike, a chain might show $0.80/$1.40. Dealers face hedging uncertainty in fast markets, so the spread is their risk cushion. In such conditions trade only the most liquid chains — SPY keeps respectable spreads while a low-volume mid-cap chain blows out.

The practical corollary: **the shorter your trading horizon, the more liquidity and tight spreads matter** (hourly swing trading, breakouts). For a six-month positional trade where the option is a risk-management vehicle, being right on direction matters far more than the spread. Market making is enormous business — dealers run complex hedging algorithms (Ceresna recalls a Timber Hill market maker, Steve, publishing roughly a million option quotes, all algorithmically generated rather than hand-priced), and dealer **gamma exposure on the S&P 500** alone can reach the hundreds of billions of dollars at certain times. Market makers get villainized, but they are paid by the exchange to make sure there is always a buyer or seller when you want one.

## 2. Contract Specifications and Mechanics

<!-- Sources: Options Master Program Module 02; Options Bootcamp Part 1; Option Writing Bootcamp; Options Master Program Module 01 -->

### The 100 multiplier and per-share quotes

Nearly all equity and ETF options control **100 shares**. Quotes are **always per share**: an option quoted at $0.84 costs **$84**; quoted at $2.00 costs **$200**. You must learn to operate in 100-share increments (10 contracts hedge 1,000 shares) — no odd lots when pairing stock with options. Ceresna: "99.9% of the things you'll ever trade have a 100 multiplier," but know the exceptions:

- **Crude oil (CL) options** sit on a 1,000-barrel future: a $1 option costs **$1,000** and controls 1,000 barrels.
- **TSX 60 index options** (Canada) have only a **10** multiplier.
- Options on futures generally inherit the future's multiplier (one gold futures contract is **100 oz** — ~$130,000 notional).

The stock price fluctuates constantly; the **strike price never changes** ("a line in the sand"), and the amount of time in the contract is fixed. These elements are rock-solid once the contract exists — only the option's market value moves.

### Expiration cycles

- **Front month and next month always exist.** Every option-eligible stock always shows a one-month and two-month monthly option, expiring the **third Friday** of the month (e.g., March 20th and April 17th in the running example).
- **Each stock is assigned one quarterly cycle** beyond that: January/April/July/October (JAJO), or February/May/August/November (FMAN), or March/June/September/December (MJSD). Example: stock XYZ on cycle 2 shows March 20, April 17, then May 15, August 21, November 20. When May becomes the front month, **June options appear immediately** — the Monday after the April expiry, XYZ suddenly has a June series. You cannot choose a stock's cycle.
- **Weeklies** have exploded in availability: commonly about **five weeks** of weekly expirations on liquid names, priced with exactly the same math, rolling forward about five weeks at a time; beyond that you use monthlies. On SPY, weeklies exist on **Monday, Wednesday, and Friday**, plus mid-week expirations going out many weeks. Some chains run years out — you can buy **five-year options on crude oil futures**.
- **LEAPS / long-term options**: one- and two-year expirations, mostly **January** in the US (in Canada, typically March). A new January series (e.g., 2023) generally appears around **August**, once the front January has less than six months left and is effectively a shorter-term option. Long-dated can go much further on some indices — **Euro Stoxx 50 options list strikes out to 2027**, a decade.

### American vs European style

- **American style** — the vast majority (almost every stock and ETF option, e.g. SPY): exercisable **at any time**, settling in the **physical delivery** of shares. Ceresna demonstrates on Interactive Brokers: long a GLD $125 put with GLD at $122 and a month left, he right-clicks, hits **Exercise**, and on Monday the 100 GLD shares are gone from the account, sold at **$125**, not $122. Exercising forfeits any remaining time value, but the right is guaranteed by the clearing corporation. For writers this creates the **early-assignment risk**: sell a three-month covered call and you can be exercised two months in (which he does not view as a bad outcome — you did sell at your chosen price — but it is a live possibility).
- **European style** — predominantly index and volatility options where the underlying is impractical to deliver (e.g. SPX): exercisable **only on expiration day** and **cash-settled** — "if you crash your car, the insurance company just sends you a check... they don't send you a new car"; intrinsic value simply appears as cash in the account. Key nuance: European style does **not** mean illiquid or locked-up — you can buy and sell SPX options any day; only *exercise* is restricted to expiration. If long a European put for protection, you cannot early-exercise it; you sell it back into the market instead.
- The quick test: ask "if exercised, what would be delivered?" A stock or ETF delivers shares (American); a volatility or cash-index option can only pay cash (European). On a chain, brokers shade the ITM side (Interactive Brokers uses light blue); the shading flips sides between calls and puts because the directions are reciprocal.

This is the instrument behind **Warren Buffett's index put sales**: the $4.9 billion premium he collected on long-dated puts on the S&P 500, Nikkei, FTSE, and Euro Stoxx 50 — roughly **$37 billion of notional downside** — could never be early-exercised against him, and at expiry he owes only a **cash payout** of intrinsic value, like an insurance claim, never physical delivery of indexes. (Ceresna notes the Euro Stoxx puts remained in the money, so part of that premium will eventually be paid back — and that he personally thinks short-term compounding by rolling shorter options beats selling 15–20-year puts, though Buffett's structure was smart. He also refuses to replicate it at market peaks: recording this near the top of a nine-year bull market, he will not do his own index put-selling "what Warren Buffett did in 2007.")

**VIX options** are "a completely different game" — they are options on **VIX futures**, not the spot index, with a peculiar skew and premium structure (treated fully in Part III, Section 3).

### Volume versus open interest

- **Volume** is simply how many contracts of that line traded **today**. It does **not** measure liquidity — a chain can be tightly quoted on a strike with little same-day volume, because a market maker hedges the whole book on the stock and doesn't care which strike you trade.
- **Open interest (OI)** is the number of contracts actually **in existence** at that strike. A brand-new series starts at zero volume and zero OI; one unit of OI is created only when a buyer and seller open against each other (buyer +10, seller −10). OI tells you the real outstanding exposure — Ceresna shows an SPY chain with roughly **762,000 contracts open at the 250 strike** on a near-zero-volume day. Closing trades cancel OI; transfers of ownership do not. (Strike clusters of open interest can read as potential magnets, support, or resistance — the IBKR tooling in Part VI displays them.)

### Paper trading: use it, then leave it

Recommended practice platform: the **CBOE Virtual Trader** (free registration via cboe.com → tools and resources) — live-market data on a 5–10 minute delay, full option-chain and order-entry simulation. Ceresna's rule from training thousands of traders: paper trade only long enough to learn the logistics of order entry (sell to open / buy to close second nature), then go live **small**. Two traps:

1. People get stuck paper trading for six months to a year and "can never make that transition."
2. "What you do with paper money is never what you'll end up doing with real money... I have yet to meet someone that is able to replicate" paper results live — fake money has no emotional triggers (up $200 in paper: "let's see what happens"; up $200 real: "I'm going to just take it").

Start transacting with real money as soon as possible at small size, because the emotional experience *is* part of the education — "you really got to get to know yourself." Then repeat the full cycle — open, manage, close, review: "just repetition... is practice."

## 3. How Options Are Priced

<!-- Sources: Options Bootcamp Part 2; Options Master Program Module 03; OptionsFundamentals; Option Writing Bootcamp -->

### Options are priced on probabilities

Nobody knows what a stock will do; the option market **prices probabilities**. Option values are computed, not guessed. The market's standard is the **Black-Scholes** model (the foundation all other pricing models build on; transcripts garble it as "black Schultz"), which was built for European settlement — variants adjust for American-style early exercise and dividends (binomial and other models), but fundamentally everything prices the same way, from **six variables**:

1. **Underlying price** — the live price of the stock, ETF, commodity, or currency; changing every second.
2. **Strike price** — the fixed "line in the sand"; the distance between price and strike drives the probability of exercise and thus the premium.
3. **Time to expiration** — more time means more probability the anticipated move happens. Saying "Apple will be a $400 stock" is meaningless without a horizon: $400 in 30 days is a minuscule probability; $400 within two years might be a reasonable 20–30%.
4. **Volatility** — the risk adjustment; it decides how expensive the option is (full treatment in Section 4).
5. **Dividends** — all known dividends are **discounted forward** into the option price, removing dividend arbitrage.
6. **Interest rates** — the risk-free rate, discounted to remove the arbitrage of synthesizing long stock and earning interest on the proceeds.

Market makers run these through pricing algorithms to get a **theoretical value** and quote bid/ask around it; changes in **implied volatility** are how supply and demand move individual option prices. Stocks have one key variable (the price); options add the extra layer — multiple variables constantly tugging at the price at once, "what the implied volatilities are [and] how much time decay... is decaying." Ceresna's verdict once you absorb that: "options are one of the most amazing resources out there."

**The pricing-simulator worked example** (October 2019 bootcamp). Inputs: $100 stock, 2% interest rates, $0 dividend, **20% implied volatility**, November expiration (~45 days), **$100 at-the-money call** → theoretical value **$2.84** ($284 per contract). A market maker would quote, say, **$2.80 bid / $2.90 ask** around that. Now a market crash hits, everyone wants options, and the dealer raises implied volatility to deter buyers: at **25% IV** the same option is worth **$3.52**, quoted maybe **$3.50/$3.60**. Only one variable changed. (The VIX is simply this implied-volatility input measured across the S&P 500.)

### Intrinsic value versus time value: the beginner's biggest obstacle

An option's price decomposes into **intrinsic value** (a real equity stake in the underlying; it does not erode with time — only moves with delta) and **time value** (the rental cost of using the option; **inevitably erodes to zero by expiration**). An option can be pure time value, or time value plus intrinsic value — never intrinsic value alone.

- **Intrinsic value (call)** = stock price − strike, floored at zero. **(Put)** = strike − stock price, floored at zero. Just the distance between stock and strike, measured in opposite directions — hence calls and puts as reciprocals.
- **Time value** = option premium − intrinsic value. This portion decays to zero; intrinsic does not.

Bootcamp illustrations (kept from both courses; several use the same underlying numbers):

- Stock $20, **$15 call** trading at **$6.50** → $5 intrinsic (buy at 15, sell at 20) + **$1.50 time value**.
- Reciprocal: stock $20, **$25 put** trading at **$5.95** → $5 intrinsic + **$0.95 time value** (synthetically short $5 of equity). If the stock sits at $20, that $5 cannot decay — only the $0.95 bleeds at theta.
- **Micron at $44.21**, July **$40 call** at **$7.65** → ≈$4.20 intrinsic + **$3.45 time**. If Micron merely sat still into July, the option would still be worth $4.20 on expiration day; only the time value bleeds. If Micron crashed below $40, the $4.20 of equity exposure is lost — "that was stock-price driven. That wasn't time decay."
- **Micron July $50 put** at **$8.50** → $5.80 intrinsic (buy at 44.20, sell at 50) + the remainder time value.
- **SPY at 255.16**: the **245 call** at **$11.17** = $10.16 intrinsic + ~$1.00 time; the **250 call** at **$6.52** = $5.16 intrinsic + ~$1.36 time; the **260 put** at **$5.00** = $4.84 intrinsic + only $0.16 time; the **265 put** carries ≈ **$9.84 intrinsic**; the **252 put** at **$1.26** is **all time value**.
- Meanwhile the **245 put at $0.60** is the market pricing roughly a **12–13% probability** of any intrinsic value — i.e. an **88% chance of expiring worthless**. That's *why* it's 60 cents and not $2.

**The probability lens on time value:** an out-of-the-money 10-cent call is 10 cents because the market is pricing roughly a **5% chance** it finishes in the money (95% chance of expiring worthless) — "you're wasting your time" if you call it cheap. The premium is the market's probability-adjusted worth of the contract. Why would anyone sell you a $250 right on a $255 stock? Because the market maker doesn't care which strike you want — as long as the time value compensates, every strike correctly prices its own probability.

**The rookie mistake:** comparing premiums across strikes — "this one's 25 cents, that one's $4, so the cheap one must be better, I can buy more." Ceresna calls this flatly naive: the $4 option may be almost all intrinsic value (an equity stake), while the 25-cent option may actually carry *more* time premium per unit of exposure. Size positions by risk and probabilities, not by option price. Intrinsic value is "an equity stake in the stock" — buying an in-the-money call is literally buying part of the company.

### In the money, at the money, out of the money

The lingo simply locates the stock relative to the strike: **at the money (ATM)** = strike nearest the stock price (all time value; occasionally a few cents intrinsic); **in the money (ITM)** = has intrinsic value (calls: stock above strike; puts: stock below strike); **out of the money (OTM)** = no intrinsic value, pure time premium. His narrative example: buy the 100 call at 100; a rally to 120 makes it ITM with $20 intrinsic; a crash-earnings drop to 95 leaves it OTM by $5.

### Dividends and interest rates

**Dividends** are discounted into option prices, because otherwise an arbitrage would exist: buy the stock, sell a covered call, buy a protective put, collect the dividend with all risk hedged. The market kills this by making **calls slightly cheaper and puts slightly more expensive** by roughly the dividend, making the "free dividend collar" a zero-net trade. Simulator demonstration: an ATM $100 put, one month out, prices at **$2.72**; add a **$1 quarterly dividend** before expiry and the put jumps to **$3.25**, while the covered call at the same strike **falls** (e.g., $2.88 → $2.69). Mechanically: on the ex-dividend date the stock opens lower by the dividend (a $50 stock paying $1 opens at $49), so calls over the ex-div date lose about that amount and puts gain it; as the ex-date approaches, the ATM call–put spread equals the dividend. The dividend is visible dramatically in high-yielders (8–10% yields on some energy/mortgage vehicles), where it visibly shifts where put-call parity sits. A practical consequence: a **put seller is synthetically compensated for the dividend** through richer put premiums, so the common belief that covered calls beat put selling "because I keep the dividend" is already priced away.

**Interest rates** are the risk-free rate discounted to remove the arbitrage of synthesizing long stock and earning interest on the proceeds. They were a non-factor during the zero-rate era (recording-era rates had collapsed toward zero), and still barely matter for 30-, 60-, 90-day options. They dominated in the era of 10% rates, where a swing to 6% or 14% materially moved prices — and they matter greatly again for **long-dated options**: Euro Stoxx 50 options list strikes out to 2027 — a decade. If European rates went 0% → 2–3%, "suddenly the option is behaving like a 10-year treasury bond," with large price swings from discounting ten years of interest. (He references the Harley Bassman MacroVoices interview on long-dated option discounting and the asymmetry negative rates create.) Note the borrow-cost wrinkle: the Beyond Meat "mispricing" he cites came from expensive short borrow feeding into put pricing via the rate input — the fed funds rate is the simple everyday proxy.

## 4. Volatility

<!-- Sources: Options Master Program Module 04; Options Bootcamp Part 2; OptionsFundamentals; Option Writing Bootcamp -->

### Historical versus implied volatility

**Historical volatility (HV)** measures how much the stock has actually moved in the past — the starting point for the market's guess, backward-looking. **Implied volatility (IV)** is the market's price-discovered estimate of **future** volatility embedded in option premiums — forward-looking, quoted annualized off ~30-day options, readable as "IV close" on any brokerage options chain. If participants feel vol is underpriced, they buy options in size; dealer exposures get unbalanced and options reprice; the process settles at the equilibrium IV everyone will trade at. IV is, in effect, **all market participants voting** on how volatile something is — it is what makes a stodgy stock's options cheap and a high-beta name's options expensive.

Ceresna's core teaching: stock price, strike, time, dividends, and the risk-free rate are fixed inputs market participants cannot change. "The only one element that is within the control of market makers and participants is how much volatility premium they pay within an option." Hence his dictum: **volatility is the adjustment for risk**. A company may have realized only 10% volatility over the last 30 days, but "if the company has an earnings announcement next week, the market doesn't give a shit about what it did in the last 30 days" — implied vol jumps for the event.

**Implied volatility as the supply/demand clearing mechanism.** If everyone wants calls and nobody will sell them, calls are effectively too cheap for the risk; IV expands, sellers get paid more, buyers must pay more, until buyers and sellers balance. Market makers are **like sports bookies**: price the game right and money flows evenly on both sides while the house clips the spread; price it wrong and they warehouse risk, so they move the line. A dealer stuck with a book full of short puts in a crash (everyone and their grandmother buying protection, no sellers) raises IV to discourage further buying and attract sellers.

This is why the 2017–early-2018 short-vol complex (Chris Cole's and MacroVoices' work) was called a **mispricing**: relentless call- and put-selling suppressed implied vols, making it "incredibly cheap to go long vol... and very unrewarding to be the seller." By the time of the bootcamps (2020), "vols have gone through the roof and now we're in a period where selling options has actually got some interesting opportunities."

**Is anything ever really "mispriced"?** A *mis*pricing is an opinion — "the market is arguably always right pricing based on supply and demand... my opinion may be that it's mispriced, but the market is saying no, that's the right price." The continuous right-pricing process is what creates the **options skew**. Ceresna is explicit that skew is **not gouging** — if options were overpriced, arbitrageurs would sell them all day; the skew is the market right-pricing tail risk for current circumstances.

### The probability distribution and one standard deviation

Option prices encode a **probability distribution**. Textbook version is a symmetrical bell curve: ±1 standard deviation covers **~68.2%** of expected outcomes (34% each side), leaving roughly **16% in each tail** (some modules round this to ~14%). Real markets show a skewed, lopsided shape (he demonstrates with Interactive Brokers' Probability Lab on the S&P 500 — see Part VI).

Worked examples:

- A **$50 stock** with a one-standard-deviation range of **$45–$55** means the options are priced so there is a **68% probability** the stock stays within $45–$55, with roughly **16% tails** on each side.
- **The implied-vol calculator** (Fundamentals session): on a $100 stock at **20% IV**, one year ≈ **260 trading days** (an audience member, Lori, corrects to 252 — Ceresna concedes the point; the answer barely changes). 20% IV means a **68% probability the stock is within $80–$120 in a year**, with tail possibilities at $60 or $140. Divide down using the **square root** of time to get the implied one-month, one-week, one-day ranges — which is why short-dated options are *relatively* more expensive per unit of time: ranges don't scale arithmetically. Raising IV from 20% to 25% widens the one-month range from about **$5.82 to $7**, and that is exactly what took the ATM call from **$2.84 to $3.52**.
- When the **VIX spikes, the curve widens** — the market re-signs one standard deviation at, say, **$42–$58**, and the same option might go from **$1.50 to $1.75 to $2.00**. When volatility contracts, the expected range narrows (say $47–$53) and premiums shrink. Long-vol traders (Ceresna names Eric Peters and Chris Cole) harvest the widening via **vega**; the danger is owning options into contraction.

### Skew and fat tails

Real curves are not symmetrical. The **S&P 500** — and most stocks with market correlation — shows a **fat left tail**: implied volatility **rises as strikes go down** and **falls as strikes go up**. Markets rise slowly and systematically ("up the escalator") but crash fast through liquidity events ("down like an elevator"), so downside puts are persistently more expensive and the implied curve skews down-and-out. **Gold** conversely carries a fatter **right** tail (the full precious-metals skew, with numbers, is Part IV Section 2 — it is the engine behind every gold structure in the course). Strike-by-strike, each option's implied vol differs (the vol smile/skew): implieds on the **wings rise** because participants and market makers know outlier moves happen more often than a pure normal distribution implies.

### Expansion and contraction

- **Expanding volatility**: the bell curve stretches **wider and taller** — the $5 band becomes an $8 band (one SD now $42–$58), and in a crash, IV going from the teens to **above 50** blows the curve out so far that options become "ridiculously expensive."
- **Contracting volatility**: the curve shrinks (one SD down to, say, $47–$53); OTM options get "crazy cheap."

For the option **writer**, expanding IV is the enemy (short options mark against you even if the strike ultimately holds) and **contraction is the friend** — premium sold into high IV profits as the curve normalizes. For the buyer of straddles/strangles, you want the opposite.

### The VIX and regime-based strategy selection

The **VIX** is the 30-day at-the-money implied volatility on the S&P 500. Its defining characteristic: **vol expands when the S&P falls and compresses when it grinds higher** — hence the persistent equity put skew.

Practical playbook by regime:

- **Low-IV periods** — calls and puts are historically cheap. Tactically favorable to simply **buy calls or puts** (cheap convexity if the market turns more volatile than priced). Also the natural home for **straddles and strangles** — long-volatility structures used, in Ceresna's practice, to catch market tops — but only when premiums are cheap, since you're buying both sides and only one can pay.
- **High-IV periods** — options are expensive, so express direction with **volatility-neutral structures**: **debit spreads** ("probably the single most popular way, in my mind"), plus **directional butterflies and condors**. Caveat: crashes are exactly when multi-leg structures fail operationally — liquidity dries up, every leg's bid/ask widens, and a 3–4 leg trade gets "taxed" on the spreads just when you need it most.

### Comparing implied to historical

Overlay IV against 30-, 100-, and 200-day HV: where the IV line sits above or below the HV lines tells you how much premium you're paying versus the stock's realized past. On individual names, IV spikes ahead of events while HV sits still — the classic pre-**earnings** run-up in implied vol while the historical line doesn't move. IV also builds for pending announcements, M&A, and macro shocks (coronavirus-type liquidity events bigger than any single stock).

## 5. Time and Time Decay

<!-- Sources: Options Master Program Module 05; Options Bootcamp Part 2; Option Writing Bootcamp; OptionsforIncome -->

### Time value is the price of uncertainty

Time value is the **cost of carry**. The more time an option has, the more probability the position has of being right — so **time value is a function of unpredictability**. The buyer *rents* the right and "the rent is literally being paid real time" — hold an option for a day and a day's worth of decay is gone; that uncertainty shrinks every day toward expiration. Symmetrically, the seller is *selling* time and collecting the premium as income. More time = more probability: if Apple is going to $200, a six-month call has a far better chance of being right than a one-month call, so it costs more. **Time decay is not linear — it accelerates exponentially** into expiration; on expiration Friday you can watch time value decay to zero intraday until only intrinsic value remains.

### Why decay is non-linear

Unlike car insurance — which refunds pro-rata if you cancel half-way (six months paid, six months rebated) — **option time decay is not linear**, because the probability content of remaining time adjusts. A 12-month option held three months still contains nine months of "a lot can happen." Decay's **acceleration comes in the tail**: decisively in the final three months, and especially the final month and final week. This relationship is clearest on **at-the-money options**, which hold the most time value and decay the most — and it assumes the option *stays* at the money; a fast move re-prices everything through delta.

### The 45-day sweet spot — and a different philosophy

Many theta-harvesters cite the **~45-day window** as the sweet spot where decay per day is best. Ceresna acknowledges the math (price collapse is most rapid in the final stretch) but flags that he runs a **different philosophy** — a **delta-influenced** approach detailed in Sections 8–9: he prefers writing **longer-dated** options (two to three months and beyond) at great strikes and lets directionality do the work, so the position suits investors who are not full-time screen-watchers. In his vocabulary, **two to three *weeks* is short-term; two to three months is not** — sub-one-month writing is the full-time-management tier. He contrasts himself with friends like manager Gareth Ryan, who deliberately sells very short-dated options to harvest the steep end of the decay curve — a legitimate school, but one that demands near-full-time active management.

### Long-dated versus short-dated carry: the square root of time

Premium does **not** scale linearly with days — it scales roughly with the **square root of time**, so short-dated options are *relatively* more expensive per day. Snapshot of SPY $255 options: a **4-day at ~$0.80**, a **32-day at ~$2.44**, a **60-day at ~$3.60**, then 95/123/151-day series. The 4-day costs a third of the 32-day despite one-eighth the time. Holding-period comparison, all else equal: over a month, the 60-day option loses only about **$1.15** of value, while the 32-day option loses its **entire $2.44**. Long-dated options therefore carry a much smaller day-over-day **negative carry** — "how much it costs me to rent the stock through the option versus owning the stock itself." The offset: short-dated options carry far more **gamma** (explosive responsiveness near the strike), which is precisely why some strategies want them.

### Deep ITM versus ATM behavior

Once an option holds large **intrinsic value**, most of its price is an equity stake in the stock; the small residual time value decays gently. A **deep ITM call behaves much more like the stock** than like an option. The contrast class: a **short-term ATM option is "all of the Greek components on crack"** — delta, gamma, vega, and theta all wild and whipsawing. Match the instrument to the job: if you want stock-like participation, buy deep ITM; if you want leveraged sensitivity, short-dated ATM delivers it — with the corresponding violence.

## 6. The Greeks, One by One

<!-- Sources: Options Bootcamp Part 3; Options Master Program Modules 03-05; OptionsFundamentals; Option Writing Bootcamp -->

### What the Greeks actually are

If the option price is an algebra equation in six variables, then **isolate five of them, change one, and measure the effect on price — that is a Greek**. The five evaluated in the course: **delta, gamma, vega, theta, rho**. Mapping to the pricing variables: delta ← stock price; theta ← time; vega ← volatility; rho ← interest rates; and **gamma, the odd one out, is the second derivative — the rate of change of delta**. There is no Greek for dividends — they are announced, known, and simply discounted. Dealers use the Greeks to compute aggregate exposure (how much stock to trade to be delta neutral, how much gamma they carry into expiry); retail investors should use them to understand **why they picked a particular strike and expiry**. Ceresna frames the payoff: "you should expect an option to behave" a certain way once placed, and the delta in particular "tells us a phenomenal story" about that behavior.

### Delta — participation rate, and the case for being a "delta trader"

**Definition:** the change in option price per $1 change in the underlying. A **0.90 delta** call rises ~90 cents if the stock rises $1; a **−0.45 delta** put falls 45 cents per $1 rally (which is why puts lose when stocks rise).

Worked examples (the $50-stock example is the bootcamp standard, repeated across courses):

- $50 stock, 30-day option priced **$2.32**, delta **0.53**. Stock instantly $50 → $51: option ≈ **$2.85**. Stock $50 → $49: option ≈ **$1.79**. (All else equal — ceteris paribus — which never quite holds live; time erodes and vol moves.)
- In the simulator, a $100 stock June call at **$2.88** moves to **$3.47** on a $1 pop — ~$0.60 of participation, i.e., delta ~0.60 at that moment.
- Live chain: S&P at ~2,711, the 2710 strike 27 days out shows delta **0.508** — a 10-point index move moves the option ~$5.
- **Live Micron walkthrough** (stock $44.20): the **$44 call**, 26 days out (March 16), ask **$2.17** ($217), delta **0.54**. A $1 pop to $45.21 → option ≈ **$2.70**. If your target is **$46** ($1.80 up), the delta tells you in advance to expect roughly **$3.15–$3.20** — about a $1 profit, **~50% return on the option for a $2 stock move**. That pre-computable payoff is why delta matters for planning.

Because most investors already think in terms of "the stock will go up/down," directional forecasting is effectively **delta trading**. Ceresna's confession of style: "I predominantly [am] more of a delta trader because I take that top-down view of macro... I believe certain things will happen — dollar will go up, treasury bonds will go down, gold will rally or sell off." The vast majority of options traders are delta-driven, using the option as a vehicle for a directional forecast; a minority sophisticated crowd trades the other variables (volatility, gamma) instead. Big Picture's house approach sits in the first camp: macro → technicals → options as implementation.

**Delta and synthetics (his specific teaching angle).** The **higher the delta, the more you're buying a synthetic stock**:

- **ITM Micron $40 call at $4.90** = $4.20 intrinsic + $0.70 time, **delta 0.80**. "If Micron shot up to $48, this $5 option is going to be worth north of $8" — nearly dollar-for-dollar with the stock.
- **OTM Micron $48 call at $0.73**, delta **0.25**: nice percentage math if right, but only 25 cents of participation per $1 stock move.
- **The extreme:** SPY at 273, one week out, **deep-ITM $200 call at $73.56** (~$73 intrinsic) — **delta 1.00**. "You did not even buy an option. You synthetically bought the market" — it moves dollar-for-dollar with SPY.

**Rule-of-thumb delta bands (his answer to "what counts as high delta"):** split into thirds — **low < 33, middle 33–66, high > 66**.

### Gamma — how fast your delta changes

Delta is not constant: as a call goes deeper in the money delta approaches 1; further out of the money it approaches 0. **Gamma is the rate of that change** — the second derivative. Shorter-term options have much bigger gamma, so their deltas swing violently as price approaches the strike, while long-dated options' deltas drift.

**The simple rule: the shorter the option, the higher the gamma.** A one-week option's delta is incredibly volatile; a **two-year LEAPS has very small gamma** — "a far calmer experience," with delta barely moving per $1 of stock. A delta-one (maxed-out deep ITM) option has effectively **zero gamma** — a $1 move doesn't change its delta. Beginner anchor: short-dated = high gamma = wild; long-dated = low gamma = calm.

Fundamentals-session simulator proof: the same $100 strike call dated **October vs November vs April** — the October curve snaps from delta 0 to delta 1 almost immediately, the April curve takes a long, gradual journey. And in the payoff diagram, as the stock climbs from 100 toward 107–110 the option's delta walks from 53 → 57 → 88 → ~1, the option's line converging onto the stock's 45-degree line: **the more right you become, the more the option behaves like the stock** — the "beautiful asymmetry" he exploits catching commodity cycles. Downside: at $95 the option behaves like only **29 shares** — losses decelerate as you're wrong, and "we cannot lose more than the premium we paid." That is **convexity**.

**Why it matters for hedging (his angle):** when buying protection on a stock position he buys **very short-term options deliberately, because he wants gamma to explode** if he's wrong — the hedge should go from 50-delta to near-100-delta almost immediately and start removing nearly all the risk.

**Market-level gamma:** when Chris Cole talks about "huge short gamma exposure in the marketplace," the mechanics are that the premium-selling, short-vol complex suffers accelerating losses as the market moves against it, and dealers/funds short gamma must chase the market; he cites the MacroVoices chart book showing that vol up just 50% with SPY down just 5% would detonate roughly **$500 billion** of implicit and explicit short exposure across risk-parity and related funds. Quants like **Marko Kolanovic and Charlie McElligott** track aggregate market gamma for exactly this reason; for a market maker, big gamma means being forced to trade long/short at a faster and faster pace.

### Vega — the price of volatility itself

**Definition:** option price change per **1 percentage point** of implied volatility. Vega cuts both ways (buyers gain what sellers lose).

Worked examples:

- $50 stock, 30-day option at **$2.06**, IV **35%**, **vega $0.06**. IV goes 35% → 36%: option = **$2.12**. "Even without the stock changing, the person who owned that option made six cents" — a percentage return purely from volatility expansion. Contraction works against you identically.
- In the simulator, a **$2.88** option at 25% IV becomes **$2.99** at 26% IV — **vega $0.11, i.e., $11 per contract** (×100 multiplier).

**The Walmart earnings case study** shows vega in the wild. With earnings two days before a monthly expiration, the short May options' IV rocketed from ~40% to ~70% into the print (44% on May 11, 59% May 14, ~71% May 15), while the June (28%) and July (23%) series rose more modestly. The moment earnings were out — the unknown became known — **all series collapsed back to ~20–22%**, Walmart's normal long-term IV. Sellers of premium into the event harvested the contraction; buyers of the cheap post-event options got normal pricing again.

Two applications Ceresna stresses:

- The **"earnings hand grenade"** risk: selling into every earnings announcement guarantees, over time, catching an outlier move. The school of managers who do it deliberately accepts occasional grenades because the inflated vol premium pays them well on average — and if they wanted the stock long-term anyway, short-term noise is tolerable.
- For premium writers generally: sell **high** IV with room for mean reversion, so contraction works in your favor; straddle/strangle buyers want the opposite.

**His angles:** this is why traders buy **long straddles in low-vol periods** — long call + long put are both long vega, a "synthetic long vol"; IV jumping 10% → 15% lifts both legs regardless of direction. Conversely, **short vega is where short-vol traders blew up**: "as soon as vol normalized in any way, they would have a huge impact at the rate of vega." Vega also ties back to the standard-deviation picture: expanding IV = the market pricing a wider expected range; owning options into that repricing *is* the trade. (Audience Q&A: implied volatility affects puts and calls alike — with skew adjustments for fat tails on either side.)

### Theta — the daily rent

**Definition:** the **cost of carry for one day** — how much value a long option bleeds holding from today to tomorrow. Example: the same **$2.06**, 30-day option with **theta $0.04**: tomorrow, at 29 days, it's worth ≈ **$2.02**.

Flip sides: an option **writer is long theta** — "every day you sit on your hands and you do nothing, you're profiting," which is the engine of the entire options-for-income methodology; it's why Buffett-like sellers let theta do the work on multi-year index puts. Theta accrues even while you may be losing on delta — the net decides profitability, but the structural cash flow belongs to the writer. He tells long-option holders to make it a habit to look up their daily cost to carry. And he notes that **spread traders are partly in the theta-mitigation business**: pairing long theta and short theta legs means you decay only at the **net difference**, so a directional bet doesn't drown in rent.

### Rho — the sleeper variable

**Definition:** option price change per 1 point of interest-rate change. At zero rates it was irrelevant; for 30–90 day options it still is ("if you trade very short-term options, you don't really have to care about rho" — a one-week SPY credit spread has nothing to fear from a 25 bp hike). A short-term option with a **2-cent rho**: rates 3% → 4% over its life = **+2 cents**.

It matters for **long-dated options**: 10 years of discounting makes a 1% rate move material, exactly like bonds — a 30-year bond moves $5 on a 50 bp rate change while a 2-year barely twitches. A two-year option has two years of interest baked in; a 30-day option only 30 days. His live example: long-dated **Euro Stoxx 50 puts** (retail can write them out to ~10 years) priced with European rates at zero — if Europe normalizes to 2%, ten years of discounted rate rise creates a large drag on the short put, a P&L move driven purely by central-bank policy. Know it's a variable for LEAPS-scale trades; don't make it a daily obsession.

### Tools: simulator and probability calculators

- **Position simulator**: input all six variables (e.g., $100 stock, 2.25% three-month T-bill, zero dividend, 25% IV), pick type/expiry/strike, and the model prices the option (June put = **$2.72**). Sliders decay time, move IV, move price — the fastest way to internalize what each variable does. With correct inputs it reproduces live market prices closely.
- **Put-selling probability calculator**: input stock ($10), strike ($9, ~1 month out), premium (20 cents), IV (30%), expected return (1%) → output: the market is pricing roughly a **10% chance of assignment** and a 90% chance the put expires worthless — a 2% one-month return on risk. Remember the caveat: this is the probability *priced in*, not the probability that occurs; options reflect all known information, and what actually happens always differs.
- **"Expected return" input**: just the mechanism for discounting the opportunity cost of capital (use the risk-free rate or your own assumption; zeroing it out is acceptable).

## 7. Application: Choosing Strategies and Building Trades

<!-- Sources: Options Bootcamp Part 4; OptionsFundamentals (exercise/assignment) -->

### The three methodologies — and how to pick yours

Big Picture publishes trades in **three distinct buckets**, and Ceresna's loudest structural warning is **do not mix them**:

1. **Breakout trades** — technical, short-term price moves; typically live **2–6 weeks**. "Not day trading" — doable with a full-time job, but it rewards being proactive intraday.
2. **Hedge/position trades** — big directional macro narratives held **half a year to multiple years**; options duration is sized to the trade's expected life.
3. **Income trades** — theta-driven option writing; sell premium with a high probability of full profit and let time decay pay you daily.

Style selection is driven by **account size and expectations** (a $20,000 account making 5% is unimpressed; a $2 million account making 5% lives off $100k), by **time available** (can you watch the market intraday or not?), and by **personality** ("what gets you excited"). His guidance: with $1 million and a full-time job, income writing is "a perfectly viable thing"; retired and screen-attached all day, breakout trading fits; if you can't watch intraday, lean income + hedged positions and use phone alerts for targets. There is no formula — "I wish I could give you a rule of thumb... you stylize it based upon your personality."

**The anti-mixing sermon:** trading is like entrepreneurship — you can run any business you want, but each needs its own business plan. The classic identity crisis: a short-term trade goes against you and it's suddenly "a great company, I'll just hold and see it through" — as he quotes the Wall Street adage, **"what's the definition of a long-term holding? It's a short-term trade you're losing on."** Traders "switch over to being Warren Buffett" only when losing. Don't.

### Breakout trader: the activation rule

The watch list is not a trade list. The arbiter of whether a breakout setup is **active**:

- **Bullish setup: the stock must be above its 20-day moving average** (closing basis) to be considered active.
- **Bearish setup: the stock must be below its 20-day moving average** — he names American Express and Nike as live bearish watch-list names of the moment.

Publish a bullish idea while it sits under its 20-day, and "if you go and open the trade preemptively and the stock never gets above its 20-day, we never considered it an active opportunity." Targets come from the technical work (Fibonacci projections and measured moves — the technical masters toolkit): e.g. Micron target **$46**, measured move **$48–55**; AT&T target **$40–43**.

### How to express a breakout trade (the ladder of sophistication)

1. **Plain stock with stop losses** — allowed, not recommended.
2. **Buy (or short) the stock with a protective option — his strong recommendation for beginners.** Long setup: stock + protective put. Short setup: short stock + protective call (a short is minus-100 shares; a call's right to buy returns you to zero, so it caps the short).
3. **Hail Marys — explicitly warned against for first-timers:** "dirt cheap" out-of-the-money calls whose odds of expiring worthless will "get a really bad taste in your mouth on the first round of trading."
4. **Advanced:** debit spreads, deep-ITM high-delta synthetics — fine for experienced members; "there's no right way... the Patrick Ceresna way and the wrong way, which is the way you're doing it. That's never... don't ever get the impression that I ever want to talk that way." ("I've trained thousands of traders and I've never met two of you that trade the same.")

### Live trade 1 — Micron: the rolling-hedge blueprint

Published Feb 7–8 (2020) around $43.88. Ceresna's actual position:

- **Bought 2,000 shares, average $42.82 (~$85,000 position).**
- Bought the **Feb 16 (weekly) $43 put for $0.90 = $1,800**. Guaranteed sale at $43 vs $42.82 cost = **+18 cents locked**; total risk capped at **$1,800** on an $85k position.
- When Micron ran toward **$45**: sold the $43 put, bought the **Feb 23 $44.50 put for ~$0.90**. Now the guaranteed sale of $44.50 vs $42.82 basis = **+$1.70/share locked**. Cumulative hedge spend **$1.80** vs **$1.70** locked gains → **the trade is now risk-free**: worst case ≈ break-even, best case full upside to the $46/48–55 targets.
- His instruction to members: **do the initial roll-up very quickly and make every breakout trade risk-free as fast as possible** — "you have all of the upside of the stock, and if the whole thing doesn't work... you've mitigated the risk to pretty much zero."

On hedge cost: "the option's eating 50 cents on the dollar into our profit" — but that's precisely why the position can be sized at 1,000–2,000 shares where an unprotected trader might size 500. Give back part of the profit, win on size. And premium is "right priced" per the underlying's volatility: Coca-Cola implies mid-to-low teens; **Micron implies ~35%** because it swung **44 → 38 → 45 within two weeks** — you pay more for a stock capable of $5 swings.

### Live trade 2 — Netflix: the numbers of a risk-free winner

Not officially published (he wanted to balance the portfolio's shorts; he told members Wednesday it was the long to watch if they wanted one). His trade: **1,000 shares at $260 (~$260,000)**; ATM **Feb 16 put for ~$3+**; after the spike above **$275**, locked gains with a **one-week $277.50 put costing $5.70** (=$5,700). Total burned on puts across rolls: **~$10,000** (including ~$4,000+ lost on the original put). Stock profit at the time: **+$18,000**; net guaranteed profit: **~$8,000**, with every dollar of upside above $277.50 still live. "There is nothing that can happen to Netflix that will prevent me from walking away with $8,000 profit. No gap slippages, no intraday liquidity event, no news event."

### Stops vs puts: the Laurie exchange (worth quoting)

A member (Laurie) asks: isn't the covered put about overnight gap risk — wouldn't a stop with 1–2 ATR or moving-average support do? Ceresna's answer is the fullest statement of his philosophy:

- Without the put you must **size smaller** and accept **slippage**: "the market is always searching for pain points. It's always looking for where are all the stops sitting... and they're guns for it." An intraday whip hits the stops, rips the other way, and you're knocked out of a trade that then works.
- With the put: "I have 100% certainty... I'm only ever 50 cents on the dollar better ahead of the game" — the hedge cost is the entire price of removing gap, liquidity, and news risk.
- Sizing math: a stop-based Netflix trader might have held 300–400 shares (stop width forces it); the put method held 1,000.
- Even a "loose" technical stop (below the Fibonacci retracement at ~255) sat **$20–30 below** the stock — versus a **$5 option** that removed all of it.
- Luke's psychological addendum: watching price bleed toward your stop is exactly when "I've never been in a good place" emotionally; the option "gives you breathing room." Ceresna: with stops "you are directly fighting liquidity"; with the put you have bought the right to choose your exit in advance — the Netflix 278 → 270 → back-to-278 whipsaw "was inconsequential to me."

**Accounting rule for hedges:** track your cumulative protection spend in a little journal and mentally **mark the hedge at zero** from day one. The platform may show the Micron put "up $165" or the Netflix put down from $5.70 to $4.50 — irrelevant; the put exists to force the sale at the strike. And when computing real P&L, **all protection costs must be subtracted** (Netflix: +$18,000 stock, −$6,000-ish cumulative puts).

### The math that makes breakout trading work: lose small, win big

Ceresna's deliberately simplified equation: average loser **−$1,000**, average winner **+$3,000**. At an **awful 40% win rate** (10 trades: 4 wins, 6 losses): losses $6,000; wins $12,000; **net +$6,000**. "It is not about always being right and never wrong. It's when we're wrong, we lose small, walk away. When we're right, we go for the big one." The mantra he wants burned in: **"paper cuts and home runs."** Calibrating expectations: breakout trader ran roughly a **57–58% success rate to target zones over the last year** — "easiest to just think about it [as] half the trades work and half of them don't," which "releases you emotionally from thinking that every trade has to be a winner." If you keep losing big and taking profits early, "you're not getting the most important element of this entire trading methodology."

### Live walkthrough 3 — AT&T: a fresh breakout in the simulator

Setup: AT&T just closing above its 20-day around **$37.14** (inverted head-and-shoulders; pullback held the Fibonacci retracement zone; targets $40–43). The construction he demos:

- Buy **1,000 shares (~$37,000)**.
- One-week $37 put = **$0.30** ("literally, think of a 30-cent stop loss" — equivalent to exiting at $36.70); two weeks (Mar 2) = **$0.53**, fillable ~**$0.50**.
- Buy **10 puts** (one per 100 shares) for **$500**. Max risk ≈ **$600** (50 cents premium + ~14 cents to the strike).
- If AT&T pops to **$38**: sell the $37 put (~recover 10–20 cents), buy the **$38 put** for another $0.40–0.50 — now ~**$0.86–$1.00 of locked capital gain pays for the next tranche of protection**: "I've made AT&T a completely risk-free trade... I have all of the upside of AT&T and can't lose a penny."
- If instead it chops at $36.50 into March: "is that really a breakout? To me, we're wasting our time" — eject via the put, take the 30–50 cent loss, find a stock that's moving.

On loss-taking (Nick's question: walk away at −25%?): don't overthink mark-to-market — **define absolute risk at entry, size to it, and let the trade happen**. "The more you try to overanalyze the short term... you may actually end up just noising yourself out of the trade." With a defined $600 max on AT&T there is nothing to manage for two weeks.

On premium burn (Laurie: what if the stock goes flat before expiry?): roll **before** time decay goes to zero, maybe give it an extra week — but "we don't dilly-dally... if two weeks are passing and it's not going active, what message does it send you? That your assumption... was wrong." A losing breakout trade is exactly "we rolled the put a couple weeks, theta ate the trade, we hit the eject button." And the offset: one $30,000 Netflix covers three $3,000 premium-burn losses nine times over.

**Hard rule:** the rolling-short-term-hedge technique is **for breakout trades only**. "Do not do this for long-term trades... the surest way over the long-term for this not to work is burning premium every single week on a position you intend to hold for a very long time frame." For position trades, size protection to duration — his example: the **TLT** position with a June 120 put, **collared** with a covered call and carrying a **25-cent monthly dividend** for positive carry that defrays the hedge.

### Live walkthrough 4 — American Express: the bearish mirror

Watch-list short, pending a close below the 20-day. If you act early anyway: **short 500 shares at $96.79 (~$50,000)** and buy **five $97 protective calls**. One-week ATM ≈ **$1.00**; two weeks quoted $1.30–1.70, fill ~**$1.55**. Expensive-looking — until you note AXP swung **100 → 87 → 98 within two weeks**: $1.00–1.50 is proportionate insurance for the next $10 leg. Note the gamma logic: an ATM weekly starts at ~**50 delta but approaches delta 1 super fast** if the stock drops — "that's the whole point of gamma trading... very low cost" for a two-week window. (Max risk ≈ premium paid on five contracts — roughly $775 at $1.55; one transcript's "$550" is arithmetically inconsistent with five contracts at $1.55.)

### Exercise, assignment, and the synthetic toolkit

**Exercise mechanics (Fundamentals session).** American-style options can be exercised at any time: he demos submitting an exercise instruction through Interactive Brokers on a **Wheaton Precious Metals October $27 put** with the stock at **$26.80** — the instruction goes to the clearing corporation and 1,000 shares would be sold at $27 overnight. Doing so there would be "a stupid idea" because the option still held **60 cents of time value** you'd forfeit — exercise only captures intrinsic; selling the option captures both. (Some brokers require a phone call; IB does it by ticket.) Index options (SPX, the S&P 500; he also groups Canadian index options) are **European**: exercise only at expiration, cash-settled. Covered-call writers should also think about **early assignment** risk on short calls — he flags it in advance for the GDX "synthetic option write" diagonal (Part III): what happens if your short call is exercised early while you hedge with only a long call.

**Synthetics recap from the application material:**

- **Deep-ITM high-delta option = synthetic stock** (the SPY delta-1.00 call; the 0.80-delta Micron $40 call).
- **Long straddle = synthetic long volatility** (both legs long vega, starting near delta-neutral; gamma shifts the balance as the market moves).
- **Advanced combinations** (iron condors and beyond) exist to neutralize delta and isolate theta or another variable — the province of the masters program.
- **Collars** (long put financed by short call) are the long-term holder's hedge-cost solution (full treatment: Part IV).
- **Delta-adjusted hedges:** to make a six-month hedge delta-equal rather than price-guaranteed, you'd hold roughly **20 puts per 1,000 shares**, trimming 20 → 16 → 13 as deltas change — "a very sophisticated game that I'm not opposed to more sophisticated traders doing." But note the alternative: one $2 six-month $37 put on AT&T guarantees the exit price even while marking only ~50 delta day-to-day — you must decide whether you want an **absolute hedge** (guaranteed sale price) or a **delta-equal hedge** (dollar-for-dollar mark-to-market); for most long-term positions you only want catastrophe insurance (the $40 stock falling to $25 costs you $2 instead of $15).

### Q&A gems from the application session

- **Combo orders vs legging (Christian):** IB's TWS lets you enter a married stock+option combo at a net debit — perfectly fine — but liquid names leg in with "almost no slippage"; he usually legs in. Not a right/wrong.
- **Dividend mechanics (Michael):** ex-div drop; calls cheaper, puts richer; the dividend is arbitraged out of collars (Section 3).
- **Counterparty risk in a crash (Dave):** counterparty exposure exists only on the **sell side** (buyers prepay). OTC/ISDA deals carry real counterparty risk; exchange-traded risk is removed by clearing corporations. The only retail-relevant failure is a full 2008/Lehman-systemic event. Your broker manages your direct margins.
- **Delta-neutral example (Michael):** a straddle starts delta ~0 (+50 call delta / −50 put delta) and is really a **gamma** position; his own book stays delta-biased because it's macro/direction-driven. (Trivia from Michael: delta, gamma, theta, rho are Greek; **vega is not** — Ceresna conceded he didn't know its origin.)
- **Canadian options (Laurie):** he discloses his TMX/Montreal Exchange instructor role; the US market is ~10x Canada's, so US chains are far more liquid, but Canadian options are still made by **US market makers** (Wolverine in Chicago, Timber Hill in Connecticut) on the same pricing machinery — just thinner open interest and wider spreads. Verdict: don't run the weekly-rolling breakout method on Canadian options; **do** use them for longer-term hedged positions and asymmetry. Platform: Interactive Brokers covers Canadian, US, London, Japanese markets — the reason the program recommends it to members worldwide. For a plain **US-dollar hedge** from Canada: US-dollar options on the Montreal Exchange ($10,000 per contract), or the FXC ETF, or options on futures.
- **Selling premium on beat-down utilities (Joe/Sid on Southern Company):** Southern wasn't above its 20-day so it wasn't an active breakout — Ceresna himself had taken a shot, rolled protection up to **$44.50**, and was stopped out Friday "with a small net loss"; he'll re-enter on a close above the 20-day. But Southern *is* a fine **income** candidate: sell puts at strikes where exercise means owning high-yield dividend payers cheap; or use the **XLU** if you'd rather not take single-company risk (similar premiums). His spread idea on Southern at $43.44: a **45/40 credit-style spread collecting ~$3 against ~$1 of downside hedge = $2 of in-the-money premium on a $5-wide spread**, with exercise giving you a ~$43 cost basis — about a dollar cheaper than market.

## 8. Options for Income

<!-- Sources: OptionsforIncome; Options Bootcamp Part 4 -->

### What the income book is

Options for income is **theta harvesting**: sell options with an "incredibly high probability of expiring for a full profit," and make money every day by doing nothing. It is, by Ceresna's account, the firm's **most consistent service** — "sometimes we get a hand grenade that shows up in the portfolio like Goldman Sachs did to us last year, but beyond that... we just harvest an income." The signature structure: **sell long-dated puts on stocks you want to own at strikes you want to own them, and spend a sliver of the premium on cheaper-dated hedges** against a crash.

The cardinal rule of put writing: **"I only ever sell puts on something I'm willing to own."**

### The Exxon workbook trade (with a short-dated tail hedge)

Stock at **$68**. Sell the **$55 put, 469 days out, at $3.00**: "you can sell me ExxonMobil at 60 or 55 all day long and I'll take it." Then buy the **December $55 put at $0.27** as a tail hedge. On 10 contracts: roughly **$2,900 premium in**, **$270 out** for the hedge (sim version: collect $2.77, pay $0.20, **$2,500 net credit**).

Why hedge at all — the crash simulation: two months later Exxon gaps to **$45**.

- **Without** a vol spike, the book is actually **up ~$1,000** even though the stock crashed 30%+ — the December hedge pays.
- **With** vol jumping to 49, the mark near the strike worsens: down about **$12,000 on the short puts vs up close to $10,000 on the hedge — net ~−$2,400**. Vega expansion means the hedge "doesn't do a perfect job," but compare the alternative: naked, you'd be staring at a six-figure loss, a possible margin call, and "hav[ing] to convince ourselves how amazing Exxon is over the long term because you now know you're going to get stuck owning it."
- And the recovery asymmetry: take profits on the $55 hedge at the $45 low, and if Exxon rallies 45 → 55, you are **$10,000 better off than if you'd never hedged**.

**The hedge's job definition (a recurring teaching point):** the December $55 put is *not* there to protect the trip from $68 to $55 — near the strike the long-dated short put will lose faster than the short-dated hedge gains (same phenomenon as the Deere call position that had members panicking as the stock approached its previous high). It exists to protect the move **through $55 toward $45**. You are deliberately **"forfeiting a part of our income to remove the risk of catastrophic loss."**

**Hedge maintenance:** when a position's hedge nears expiry, extend it if the trend still argues for protection — with Exxon at $68 and trending down, "it is probably prudent... to extend a new $60 put hedge out for the rest of the year." If instead the stock double-bottoms and rips (his $75-by-March scenario) with the position in good profit, you can simply stop buying hedges.

### The Johnson & Johnson trade: "crisis insurance in the middle of a hurricane"

During the 2020 crash (J&J ~$150 down to ~$130), the income book **sold naked January (one-year) 110 puts**. He names the two criticisms himself: (1) the vol spike was concentrated in short-dated options, so long-dated writes weren't sold at peak IV; (2) naked is naked if the market keeps crashing. His answer: they were **selling crisis insurance in the middle of a hurricane** — being paid enormous premium to promise a price ($110) they were happy to own J&J at.

The risk-management overlay: with the stock spiking back, buy **near-the-money April protection for ~$0.45**. Structurally this is a **calendared hedge**, not a credit spread — same strike, different expirations. It cannot remove vega risk (and leaves a little delta risk, since the long-dated short put expands faster out of the money than the short-dated long put), but it **eliminates intrinsic-value loss** inside the hedge window: J&J dropping to $110 might cost ~$2, but it can no longer cost $10 if it crashes to $100.

The arithmetic as taught: sell 10 naked puts for **$3,500**; spend ~**$1,000** (45 cents here, another tranche later) on protection → **~$2,500 net premium with catastrophe insured**.

**Rolling the hedge up:** when J&J bounced 130 → 133/134, switching the protection from the 110 to the **115** cost only **~$0.15–0.20** (~$200 on the position). Now the insurance kicks in at 115 while the obligation sits at 110 — "if Johnson & Johnson is going to crash, I might as well crash a lot, because that way the insurance is going to make me a pile of money more than I'm losing" — after which you reposition at better prices. Macro template note: if the correction followed precedent and took the S&P to 2,500, he'd expect **two or three more of these exact trades** — long-dated writes with short-dated hedges.

### 45-day writing versus long-dated directional writes

Section 5 records the industry's 45-day rule of thumb. Ceresna's contrarian approach is **delta-influenced** — he writes long-dated at great strikes and lets directionality do the work. His worked comparison, **Yamana Gold**:

- With the stock near **$2.50**, he sold the **$2.50 put out to 2021 for $0.50**. A 45-day $2.50 put paid "a nickel or a dime."
- Yamana rallies to **$3.40**: a new 45-day $2.50 put now pays **zero** — you'd have to chase risk by writing 3.00–3.50 strikes.
- If Yamana reaches $4 with three more months gone, his 2021 $0.50 put can likely be **bought back for ~$0.10 in January or February — 11 months early**. "I would have made more income premium by being directional with the income write... than selling short-term 45-day options."

He's explicit this is style, not dogma: "if you prefer just writing those shorter-term options... all power to you. Go for it... I like selling these longer-dated ones. That's my big picture style."

**On targeting IV:** he doesn't. "Volatility is just right pricing" — AT&T in the teens, Tesla at 50% — because you only need a *relative* move (AT&T $2–3 vs Tesla $30–50) to earn the same percentage return: "it's about the opportunity rather than targeting the vol." Confirmation tools (moving averages, zigzag, RSI, stochastics) come from the technical masters toolkit; **Fibonacci work is the core** of his process.

### Seasonality: the gardening rule

Income harvesting is **seasonal, like planting a garden**: "if you try to plant your garden in the middle of winter, you're going to have a hard time" — you can build a heated greenhouse, but the natural season is spring. Translation: a bear market is the hardest income environment (writing into falling knives), and the easiest income of the cycle comes **emerging out of a bear market**. Going into the 2020 bear he cautioned members: don't overdo income writing — but reviewed the open book as still largely valid: **Exxon** still good, **Cameco** still great, **Newmont** (re-position to 2021), **Barrick** (go to 2021), **Agnico Eagle** ("Annalie" in the transcript) still loved even in the money, **Yamana** still great, a Canadian gold name the transcript garbles ("Then Canada" — likely Centerra) still great, **Deere** still great, **Synovus** still great, the **Goldcorp diagonal** still on; **AT&T** was simply going to expire as a full profit. *(One name is marked unclear per the fidelity rule.)*

### Position sizing for income

Two legitimate methods, pick one and be consistent:

1. **Size by obligation:** decide how much stock you could be *put*. If 10 Exxon contracts could put 1,000 shares ($60,000 at the $60 strike) to you and that's too much exposure, the trade is too big.
2. **Size by crash-scenario risk:** the modeled disaster loss on 10 contracts was ~$2,400; if your tolerable worst case is $1,000, write ~**4 contracts**.

Either way, the hedge spend comes out of the premium, and the goal stays constant: consistent cash flow with the catastrophic tail amputated.

## 9. The Option Writing Bootcamp: Covered Calls and Put Selling

<!-- Sources: Option Writing Bootcamp; Options Master Program Modules 01-05 -->

The bootcamp's stated thesis: the "meat and potatoes" of option writing are two straightforward strategies — **covered call writing** and **put selling** — and everything about when to do them, what to do them on, and how to evaluate the trade. (Credit spreads, calendar hedging, and more advanced structures are explicitly deferred to the Master's Program; naked call writing is explicitly not covered.)

### The writer's framework — and the instructor's track record

Ceresna frames premium selling as the **"stock rental business"**: you are paid cash, up front, "as real as a dividend," for taking on an obligation you may or may not have to honor. His credibility claims as stated in the material: almost a decade at CIBC in multiple trading roles, about five of those years trading a **$50 million pool dedicated to option writing** (covered calls and put selling) with a portfolio manager; across a 20-year trading career he estimates **60–70% of all the money he has made came from premium harvesting**, more than from market timing. He is nonetheless blunt about cyclicality: recording this near the top of a nine-year bull market with suppressed implied volatilities, "this is unfortunately not the ideal time" to load up on the strategy — the asymmetry returns after the market's freak-out and the accompanying recession.

A recurring distinction runs through the whole session: **retail investors can be either counterparty**. Market makers often sit in the middle as delta-neutral middlemen clipping the spread, but the ultimate counterparties of every contract can both be retail investors with different views — that is what makes a market. The bootcamp's own examples: **Jackie** (bullish, buys an Apple $190 call for $4.50, 30 days, Apple at $189 — pays $450) versus **Peter** (owns Apple, collects the $450); **Doug** (owns Sunoco at $27, buys the $25 put for $1.00 as insurance, 30 days) versus **Amy** (willing to accumulate Sunoco at $25, collects the $100 and waits).

### Covered call writing

Mechanics: you must **physically own the shares** — "covered" means you can deliver them if exercised (without shares you'd be naked, which is out of scope here). You sell to open calls against your stock, choosing the strike **you** would be happy to sell at: "If you don't want to sell your Apple stock at 190, don't sell the 190 covered call." Key practical points:

- The stock does **not** have to be newly purchased — a holding owned untouched for five years can be covered-call written tomorrow. There is no required linkage between stock purchase and option sale.
- You can write against **part** of the position — sell 5 calls on 1,000 shares to leave half the upside open, tailoring to your view.
- The premium is credited **immediately** and is yours to keep regardless of what the stock does — the certainty trade-off Ceresna calls **"bird in hand versus two in the bush."** You forgo upside above the strike in exchange for cash now; the stock might have run from 55 toward 70, or gapped back down to breakeven by expiry — the writer's $6,700 was banked either way.
- Early exercise can pull the obligation forward on American-style options (sold three months, assigned at two) — acceptable, since you sold at your chosen price.

**Worked example — Micron:** own 1,000 shares at $54.70 ($54,700 of stock; buyable fresh or long-held). Sell the **October $55 call** (about five months out) at **$6.70** → **$6,700 cash collected immediately** — roughly a **12% cash flow in five months, ~30% annualized**, obtainable without needing the stock to rise or timing anything. Alongside: the accounting reality that the short calls appear as a negative market-value liability that decays at theta, while your cash balance jumps by the exact credit (demonstrated live: $686,324 → $688,102 on a $1,790 Disney credit — withdrawable cash).

**Yield-enhancement ladder — Disney (owning 1,000 shares bought at ~$101, stock ~$104):** August (91-day) options paid **$3.55 at the 105 strike** (~3.5% for three months), **$1.78 at 110** (just under 2%), and ~**1% at 115**. The systemic version: writing ~1% per quarter far out of the money adds ~4% annualized cash on top of, say, a 4% dividend — turning Disney into a **7–8% yielding vehicle while retaining all upside up to the strike**.

### Put selling (cash-secured)

Mechanics: you collect premium for the obligation to **buy** shares at the strike if put to you. "Is put selling dangerous? I don't think so — **leverage** is dangerous." The two are constantly conflated: a $100,000 account that immediately sells $250,000 of at-the-money Apple put obligation is running 2.5× leverage on one name with no diversification — *that* is the danger, not the put per se. Buffett-style put selling he calls **super conservative**: willing owner, using puts as an accumulation mechanism at prices he chose (Coca-Cola at $35, Burlington Northern in the mid-70s — versus his later index puts, which Ceresna notes *were* implicitly levered since $37B of notional wasn't fully cash-collateralized).

**Worked example — Disney:** stock at **$104.34**; the **three-month $100 put** at **$2.40**. Sell 10 puts → **$2,400 collected now** — a **2.4% return in three months (~10% annualized)** for agreeing to buy at ~$5 below market: "I don't really like it at 104, but I'd be more than happy to buy it at 100." If assigned, 1,000 shares land at a **$97.60 break-even**. Uses: income on range-bound-to-bullish names, **dollar-cost-averaging an existing loser** (own Disney from $110, sell the $100 put to lower average cost while being paid to wait), or fresh accumulation at a discount.

**The synthetic-identity point (exam-grade):** covered calls and cash-secured puts are **mathematically and synthetically identical** — overlay the two risk graphs and they match: full downside of stock ownership (already owning it, or becoming obligated to own it), capped upside, premium collected up front. So "covered calls are conservative, put selling is risky" is self-contradictory. Respect position size and leverage and put selling is a conservative income tool.

**Trade selection at the put level — the strike-through-support logic:** Disney's 52-week range was $116–$96. Selling the August $100 put at **$2.39** put the break-even near **$97.50**, essentially **on the major support line that held all year** — "the best price of anybody who bought the stock in the last one year." Alternatives on the same chain: the 97.5 put at $1.66, the 95 put at $1.14–$1.16 (assignment only at fresh 52-week lows, about half the premium). Both the strike and the expiry are choices (one, three, six months, a year — even years on some index options; Buffett went 15–20, an option retail lacks but which Ceresna thinks is beaten by shorter-term compounding anyway).

### The two approaches to selecting what to write on

Macro context comes first: know the market cycle, the liquidity cycle, and the VIX/volatility cycle before sizing. In stable, risk-on phases you can size bigger with fewer hedges; into risk periods you shrink size, favor defensive asset classes, and pay for hedges. Timing note from the session: even if stocks rally into the summer (their short-term call at the time), selling long-dated options at **12–13% implied vol** late in a bull market means enduring a distribution phase that will test your resolve — sell short-dated at that stage or wait. And when the bear market arrives, premium selling doesn't die — it **migrates asset classes**: bonds and gold become the attractive premium-harvesting underlyings while equities are being hammered.

Then two complementary selection styles, which Ceresna refuses to rank ("right or wrong, good or bad"):

1. **Sell premium at attractive price levels near major support** — on names already "bled out" and oversold where further downside is diminishing. His examples across sessions: AT&T, Gulfport, Disney. The put break-even landing at support (the Disney $97.50 math) is the template.
2. **Sell premium into a trending stock** — e.g., Apple breaking to fresh 52-week highs: momentum makes it likely the stock leaves the strike behind quickly, letting you realize the premium fast and compound by rolling. Members are shown combining this with the breakout-trading service: if the breakout rips, short puts below harvest quickly.

### Sizing, margin, and obligation awareness

The bootcamp's hardest warnings cluster here:

- **Always do the obligation math before selling**: contracts × 100 × strike = the stock you may be forced to buy. Buffett published in his annual letter that his index puts put $37 billion of equities at risk — he knew his number. "The biggest error a beginner can make is not knowing the obligations they've undertaken" — then the market moves, the portfolio whipsaws, and they blame options. "It wasn't the option that was risky. It was you that was risky."
- **Margin is a trap.** IB asked only **~$23,000 of margin** to collateralize ten Disney $95 puts — a **$95,000 obligation**, roughly 25%. Traders who keep selling up to their margin never see the true exposure. The discipline: "Sell puts only on things you're willing to own and at prices you're willing to own them at," and hold the cash to take delivery (cash-secured) if that's your standard.
- **Match return targets to risk honestly.** Want 30% a year? That requires either short-term compounding (a full-time job) or substantial leverage on longer positions. Want a conservative extra **2–3% yield enhancement** to double a dividend stream? Available with essentially no new risk. Choose deliberately.
- **Psychology follows the discipline**: if you would genuinely be happy buying Disney at 100 with a $97.50 basis, assignment is a non-event. If not, don't sell it.

### Managing the position and assignment

- The short option sits on the books as a **negative market-value liability** that fluctuates with price, volatility, and time; the received cash is real and spendable. Anchor on the contract, not the daily mark: "I'm prepared to own another 1,000 shares of Disney at $100 — and if it never gets there, I made a $2,400 dividend."
- **Assignment on American-style options can come early** (covered call assigned mid-life). Ceresna treats assignment as a success path — you sold at your price and were paid — not a failure.
- **Assignment is accumulation**: shares arrive at strike; your break-even is strike minus premium ($97.60 on the Disney puts); that basis can dollar-cost-average an existing line or start a new one. The put-selling-then-calling-off-owned-shares loop (accumulate via puts at support, then write covered calls on what you accumulate, as Buffett did with Coca-Cola/Burlington Northern) is presented as the natural combination of the two strategies.
- Closing is the mirror image: buy to close the short option (reciprocal of the buyer's sell to close), at whatever market value the liability has reached.
- If you want to keep harvesting while capping the obligation instead of owning, that's the **credit-spread** family — deferred to the advanced material.

### Extending to options on futures

Ceresna shows his live gold trade: a **naked put sold on gold futures**, collecting **$6,700** for the obligation to take gold at **$1,350/oz** between then and **February** of the following year (currently ~$1,700 underwater on a dollar rally). The added complications:

- **Multipliers follow the futures contract**, not 100 shares — one gold futures contract is **100 oz** (~$130,000 notional); crude oil is 1,000 barrels.
- **You settle against a futures contract, not spot**, and the term structure matters: gold showed natural **contango** (May contract $1,289 while the February 2019 futures — the actual settlement reference — stood at $1,315, and five-year-out contracts priced ~$1,500 on storage/carry), whereas crude oil was in **backwardation** (long-dated futures at $50 against $70 spot — meaning long-dated option strikes key off $50, not $70). The payoff: commodity options extend to **five-year maturities**, enabling Buffett-style long-dated put writing that equity options rarely offer.
- The **pricing math is identical** — same six variables, same delta/gamma/vega behavior; it's a derivative on a derivative, nothing conceptually new.
- His sequencing advice for learners: master options on stocks first; use the **GLD ETF** as the gold proxy before touching futures; the futures-options step comes when it comes.

### Bootcamp Q&A notes worth keeping

- Dividends are discounted into premiums (the $2.72 → $3.25 put demo in Section 3); put sellers are synthetically paid the dividend, closing the would-be arbitrage.
- "Expected return" in calculators is just the discounting/opportunity-cost input; zero is acceptable.
- Short-term vs longer-term in his vocabulary: **two to three weeks is short-term; two to three months is not short-term**. Sub-one-month writing is the full-time-management tier (Section 5).
- Implied volatility hits puts and calls equally, modulo skew.
- Use the paper-trading account until order entry (sell to open / buy to close) is second nature; size down — he runs 10-lots on a ~$1M demo; a small account runs 1-lots on identical logic.

---

# Part III — Strategy Playbook

<!-- Sources: The Ratio Call Spread; Trading Calendar Straddles; 2020-04-14DiagonalSpreadBootcamp; Trading Volatility Bootcamp; BuildingSynthetics; HedgedPositions -->

## 1. Ratio Call Spreads

<!-- Sources: The Ratio Call Spread (720p with 25fps).transcript.md; Trading Volatility Bootcamp (1080p with 25fps).transcript.md (upside call-ratio example, vol-structure nuances) -->

**What it is.** Sell one call (usually at or near the money) and buy two calls at a higher strike, in the same expiration month on the same underlying. The 2:1 ratio must be same-expiry so one short call offsets one long call for margin purposes; the extra long call is the "wing" that gives the trade its upside. Many brokers can't book a native ratio, so Ceresna's equivalent entry is to place a 1:1 call *credit* spread and then use the collected credit to buy an additional call — same risk profile, same result.

**The market outlook it fits.** Ceresna is explicit that "very few times is it actually ideal to open the ratio call spread — most market conditions are not ideal." All four conditions must line up:

1. **Implied volatility is relatively low.** The trade is long vega (long volatility). If you open it after a vol spike and vol normalizes, the vega contraction hurts you.
2. **Big upside potential.** The break-evens sit higher than a plain call's, so you need to believe in a *large* move (he says a few hundred S&P points, not "up 50 points to 2850" — for a modest view, a debit spread is the better tool).
3. **Severe downside risk if you're wrong.** The strategy's raison d'être: you want to keep participating in an advance you expect to end badly, without getting destroyed by the ending.
4. **Low probability of a long sideways consolidation.** The *greatest* risk of the trade is not a crash but the market staying flat-to-slightly-higher; you must assign below-average odds to that.

The January 2018 webinar was built on exactly that setup: a parabolic melt-up in the S&P 500 (weekly chart acceleration, targets discussed of 3,000–3,300, Erik Townsend even floating another 1,000 points), late-cycle conditions (103 months into a business cycle vs. a post-WWII average of 69 months peak-to-peak and ~58 trough-to-peak; by mid-2019 it would be the longest expansion since WWII), and a Fed that — per a ~100-year Bank of America Merrill Lynch chart of Fed history — "raises rates as long as it can until some financial event forces it to stop." Supporting sentiment data (Morgan Stanley QDS estimates): rolling 10-day net demand for S&P futures at 7–8-year peaks; customer SPX *call* holdings at the 100th percentile (normally customers are net short calls from covered-call writing); customer *put* holdings at the 0th percentile — "nobody cares about insuring the downside." The analogy Ceresna kept drawing: the Dow's 1986–87 arc (a ~20% 1986 rise from ~1,500–1,600 to ~2,000, then a +30% melt-up to ~2,600 by mid-1987 that wiped out its entire year's gains in the October crash), and Bitcoin's 2017 blow-off (~$19,000–20,000, then $11,000, briefly under $10,000). The Bob Farrell principle, as Kevin Muir (The Macro Tourist) framed it: markets rising parabolically very rarely correct sideways — the correction is proportional to the rise.

**Worked construction example (the canonical one).** January 18, SPY at 279 (he uses SPY for simplicity; SPX or futures options work identically for those who prefer European settlement):

- Sell one March 16 279 call (at the money): collect **$5.00** ($500 credit).
- Buy two March 16 284 calls (out of the money) at **$2.95** each: pay $5.90.
- Net outlay: **$0.90 debit ($90 per 1×2)**.

Strike choice is flexible: sell the 278 instead ($5.90 credit) and it's a zero-cost trade; buy 285s at $2.50 and it's a net credit. His rule of thumb for picking the long strikes: choose calls costing roughly **half the credit** collected on the short call. More time to expiration raises the break-evens; less time leaves you more exposed to being early — he chose ~2 months deliberately. Even at a $90 outlay, the broker holds spread margin (as if it were a 279/284 credit spread), so capital committed exceeds the debit.

**At expiration (as taught on the risk graph):**

- Market crashes (SPY ≤ 279 at expiry): the spread expires worthless and you lose only the **$90 debit** — zero if opened at zero cost. A plain call buyer who paid ~$5 loses the full $500.
- Maximum loss: **$590** (the $500 strike width + $90 debit), and it occurs at exactly **284 on expiration day** — the short call is $5 against you, the longs haven't caught up.
- Upside: above 284 the extra long call makes the position net long — participation accelerates without cap.
- Trade-off vs. the plain call: the call becomes profitable sooner; the ratio needs a bigger move. That is the price of the crash protection.

**Management rule #1 — never hold to expiration.** The single most emphasized point: *"By closing the trade early, you never risk max loss."* The $590 worst case exists only if you're still holding at expiration. Commit to closing **at least one to two weeks before expiry**. Two weeks out, the live risk graph is a sloped U — max drawdown only a few hundred dollars on the same position, and the P&L line crosses into profit at a much lower price than the expiration graph implies. Held this way, the trade's realized risk/reward is dynamically better than anything Google-able.

**Management rule #2 — size up to compensate.** Because the early-exit rule structurally slashes risk, you can run more 1×2 units than you could run naked calls, restoring the upside participation you gave up. His simulator comparison (SPY 279, ~10% implied vol, ~2% risk-free rate), six weeks into the trade with 16 days left:

| Scenario (SPY, 16 days before March expiry) | 10 long 279 calls ($4,720 outlay, ~$280,000 notional) | 10×20 ratio 279/284 ($500 debit + $5,000 margin) | 15×30 ratio 279/284 ($750 debit) |
|---|---|---|---|
| Flat at 279 (pure theta) | −$2,290 | −$1,500 | −$2,300 |
| At 282 (the ratio's max-pain zone) | improving | −$1,700 | −$2,500 |
| Crash to 250 | −$4,700 (total loss) | **−$500** (the debit) | **−$750** |
| Melt-up to 300 | +$16,500 (~300%) | +$10,750 | +$16,000 |

The 15×30 size earns the same melt-up payoff as the naked calls ($16,000) with a worst case of ~$2,500 (flat-to-282) versus the call buyer's $4,700 total loss on a crash. "We cannot get badly hurt, and if the market melts up we can make big money" — Luke Jaster's summary of why the trade gave him more peace of mind than anything he'd traded.

**Volatility exposure.** The position is long vega, same as any net-long-call structure. From the 15×30 at 282 with a −$2,500 mark: vol 10% → 9% deepens the loss to −$2,800; 9% → 8% to −$3,200; vol spiking 10% → 13% *shrinks* the loss to −$1,300. Hence condition #1: open it only when implied vol is at the bottom of its range, so contraction risk is minimal and any vol expansion is a bonus. (A long call has the same vega — this isn't unique — but the ratio's flat-market carry makes the vol input matter more.)

**When it does NOT fit.** The textbook trap: buying a ratio call spread right before earnings (his example: Micron). Demand pumps call and put implieds into the print, then volatility normalizes afterward — criterion #1 is violated and you take a big vega hit even if direction is kind. Likewise, in a post-spike high-vol regime the fat out-of-the-money call skew forces the long strikes much farther away, gutting the payoff geometry (see Section 3). One nuance from the March 2020 bootcamp: even in high vol, if the *call* skew slopes downward (ATM calls priced at richer vol than OTM calls — the S&P's normal shape), a call ratio is still reasonable, because you're selling expensive ATM vol and buying cheaper wing vol.

**Mirror image — the ratio put spread.** Short one at-the-money put, long two lower puts: same logic for a downside thesis with the same worst case (a modest, pinned-in-the-range loss) and explosive payoff in a crash. Vega is long here too — "all long options are exposed to vol risk; all short options benefit to the reciprocal" (Ceresna, in Q&A). During the January 2018 melt-up he personally held a ratio put spread as well: if the market kept ripping he lost almost nothing, but he was covered for the liquidity event. In March 2020 he framed the *call* ratio as the mirror hedge for his short: sell the ATM call, buy 2–3 OTM calls, and if the market keeps crashing the hedge costs nothing while keeping the recovery tail alive.

**Worked example from the March 2020 regime.** Believing the coronavirus crash could be "blown off" into a face-ripping rally: out to July, sell the 300 strike SPY call for ~$18–19 and buy three 325 calls at ~$18 — a **zero-cost 3:1 ratio call spread**. If the S&P keeps falling, the trade costs nothing to hold; if the market fully recovers, the three long calls deliver the right-tail blowout. (He noted at the time that his own published hedged short could eventually be paired with exactly this.)

**Early assignment.** Only a real risk at ex-dividend dates or when the short leg is deep in the money with no time value left — and then the long legs immediately offset it economically. The practical problem is only for small accounts without margin to temporarily carry the assigned shares.

## 2. Calendar Straddles and Diagonal Spreads

<!-- Sources: Trading Calendar Straddles (1080p with 30fps).transcript.md; 2020-04-14DiagonalSpreadBootcamp (1080p with 25fps).transcript.md; HedgedPositions (1080p with 25fps).transcript.md (straddle management in a decline) -->

Both structures share one architecture Ceresna uses everywhere: an **anchor** position plus an **adjusting wing** that gets rolled. In a calendar straddle the anchor is a long-dated put; in an income diagonal the anchor is a long-dated option; the wing is always the short-dated leg you tactically manage.

### The calendar straddle (catching a top while respecting the trend)

**Definition.** A plain straddle buys a call and a put at the same strike and expiry — delta near zero, double premium, accelerated theta burn, and (in his words) one of the two legs is always wrong. He says he normally *avoids* straddles entirely. The **calendar straddle** keeps the same strike on both legs but **mismatches the expirations**: buy a short-dated call and a long-dated put (for a bearish top-catching thesis; the mirror works for a bottom).

**Why this shape.** The goal is 100% to catch the coming decline; the call is a *synthetic hedge* on being early. The short-dated option carries much higher **gamma** — in his live April 2019 example, the April call's gamma was ~$0.04 vs. ~$0.02 on the July put, so the call's delta (and P&L) moves at roughly twice the pace of the put's. If the market keeps rallying after entry, the fast call pays you for being wrong; and short-dated gamma is also why dealer hedging distorts markets into big expiries (the quadruple-witching effect, as Charlie McElligott writes about) — which he wants working *for* him.

**The three entry conditions** (this is why he said no throughout January–February 2019 and yes in April):

1. You anticipate a **meaningful directional move** — either direction.
2. You believe it's **imminent** — late enough in the move that it fires within your option window. (His standing view: the 2019 rally was a bear-market rally that would run ~3–4 months into April/May, then the September–December 2018-style decline would resume; Jeffrey Gundlach at DoubleLine was publicly calling for a retest of the lows.)
3. **Volatility is low.** The straddle his members opened for ~$12 would have cost $15–20 during the January/February vol (VIX 18–19 after the December spike to 37). Long a call *and* a put, you're already fighting theta on both legs — don't let vega be a second enemy.

**Worked example (the published trade).** April 2019, SPY ~279: buy the **April 18 282 call** and the **July 19 282 put**, 10×10, never ratioed (he keeps the published version clean). Cost ≈ **$12.00 per combination** (simulator at 14% IV: call $4.19 + put $7.84) = $1,200 per 10-lot, with each straddle controlling ~$28,000 of market exposure.

**Risk profile as taught:**

- You never hold to the July expiry, so "100% max loss" (what risk calculators show) never applies.
- The ugly scenario is a **pinned market**. If SPY closed April 18 at exactly 279, the April call dies and you're down ~**$500** (~40% of the $1,200) with the July put as remainder value. That max loss exists only at that one exact price — at 282 the drawdown is only ~$400.
- Add vega: each 1-point drop in implied vol costs ~1 vega point; vol 14 → 12 turns the worst case into ~**$600** per combination by April. That is the honest worst case: roughly half the outlay.
- Why "pinned" is an outlier bet: at SPY 279 with 14% IV, the one-standard-deviation (68%) implied move is **$2.42 per day, ~$5.42 per week (~2%), $11 per month**. The roll trigger is ~$5 — inside the one-week implied range. Betting on no $5–6 move in a month is, in his words, "truly an outlier."

**Management — the roll-up loop.** Roll roughly **every $5 SPY move**, closing the whole straddle and reopening at the new at-the-money strike, and if enough time has burned off, push the call leg to the next weekly expiry so there's always enough runway. Each roll costs ~nothing (small profit or small loss) because the short-dated call's gamma outruns the put's theta.

- **Being early (rally):** simulator case — 12 days pass, SPY grinds to 285 (halfway to the 290 target): the straddle is down only ~$137 (breakeven at the vol-12 setting he actually used). Close it, reopen at 285. In the December 2017 live version he rolled **at a profit each time**: entered at SPY 268 (January call + March put), market ripped ~7–8% over a month, first roll on January 23 for a **$1.75 profit**, then 268 → 274 → 279 → 283, each roll profitable — and then the February 2018 flash crash paid the long put. The September 2018 top was caught the same way (that one with slower rises and not every roll profitable).
- **Being right (crash):** market nose-dives to 235 (the Gundlach retest) with vol spiking to 30: the $1,200 outlay marks at **$4,500 — +$3,400**. The short-dated call expires toward zero quickly; the long put does the work. Worst case ~$600 vs. that payoff is the asymmetry.

**The one structural difference vs. Chris Cole's straddles** (Section 3): this is a *market-timing* trade — mismatched expirations, actively rolled. Cole's is a *systematic tail hedge* — matched expiries, held on a clock. Don't confuse the two.

### Diagonal spreads (anchor + income wing)

**Why the short leg pays.** Short-dated options are disproportionately expensive per day. Ceresna's Johnson & Johnson demonstration (145 strike): a 3-day call costs **$2.85**; a 31-day call (10× the time) only **$6.30** (~2.2×); a 66-day call just **$7.95** (+$1.65 for another month). Market makers set daily implied vol and scale it by the square root of time (the "rule of 16," per Steve Sosnick of Interactive Brokers), so per-day premium is richest at the front. Sell that front premium against a long-dated anchor and the anchor pays for itself.

**Income diagonal — long call anchor (the GDX example).** Owned in the Options for Income portfolio since September: buy a long-dated LEAPS call as a *synthetic stock position*, then write short-term calls against it like a covered-call writer.

- GDX at $31.45. Anchor: **January 2021 LEAPS call, bought $5.77–5.80**, now worth $8.50–8.75 — capital appreciation just like owning shares, "a synthetic covered-call strategy with a fraction of the risk and a fraction of the capital outlay." The anchor's delta was ~0.78 — behaving like a **$25,000** GDX position.
- Wing: sold the weekly ~32 call for **$0.70** income. Rules are pure covered-call discipline: never sell the next call until the current one expires or is closed; sell out of the money so you're not called away; roll *up and out* if it goes in the money (e.g., close the April 32 for $0.60, sell the May 37 for ~$0.60–0.65 — reopening the upside for ~flat), but since the mandate is income, the preferred roll is the one that extracts credit (close at $0.60, sell the May 35 at $1.10 → **+$0.50**). A resting limit order at your target credit can work: as expiry nears, theta shrinks the short option and the roll fills.
- On a profitable expiry, sell the next month's OTM call (e.g., May 34.50 for ~$1.20 = $1,200) and repeat against the same anchor.

**Income diagonal — long put anchor (the AT&T "put-me" diagonal).** Buy a long-dated OTM put as both insurance and collateral, then sell short-dated puts for income; assignment risk is capped by the anchor.

- Anchor: **20 June $25 puts on AT&T at $1.41 = $2,800** — removes *all* loss risk below $25 on stock that would be put to you. His framing: what kills premium sellers is buying at 30 and watching it go to 15 and stay there; the anchor deletes that scenario.
- Income ledger in the COVID-vol environment (started ~March 26): sold the March 27 $29 put for **+$880**; the April 3 $30 put for **+$2,260**; rolled it (extracting an extra **$0.57**) and it expired at full profit; sold the April 17 $30 put for **+$1,000**. ≈ **$5,000 harvested in ~3 weeks**, with two months of writes still ahead. Fantasy case (his word): $1,000/week to June = $14,000 gross, **$11,500 net** of the $2,800 insurance.
- Max risk: the strike width — $5 × 20 contracts = **$10,000**, and only if AT&T implodes and *stays* down with no further writes possible. Every premium collected reduces that max risk.
- **Crash playbook:** if AT&T gaps to 27 and free-falls toward 21, you're assigned at $30 — fine: let it happen, then monetize the June 25 put, now worth $5+ ($4 intrinsic plus crash-inflated time value), bringing the effective cost basis to ~$25 or less net of all premium collected. When it snaps back you're actually long-and-winning. "We'd find a way to make money even then."
- **What to run it on:** boring, range-bound, unloved names with fat implied vol — AT&T was chosen precisely because nobody cares about it; Wells Fargo (swinging 26–33 with big premiums) is another candidate: buy ten July 25 puts at **$1.60 = $1,600**, immediately sell the ~$30 put for ~$0.70 (**~$600–700 income**). Avoid hot runaway names — you lose the window to roll. Sell the strike closest to the money (the 30.5 when the stock is 30.8).
- **Margin:** entered as a true diagonal combo, the broker charges only **spread margin** — the width between strikes (e.g., $5,000 collateral for ten $5-wide WFC diagonals) — so the position can't be margin-called out of existence in a crash. You still want size you could actually take delivery on; the standing intention is always to roll before assignment (e.g., April 17 → April 24 for a $0.45–0.50 credit).

**Directional debit diagonal (the SPY bearish version).** Same architecture, but the goal is direction, not income: the anchor *is* the trade and the wing merely pays the carry.

- Anchor: **ten July 280 SPY puts at $20.48 = $20,482** (rolled up from 275) — the core expression of the next bear leg, at a 0.44 delta a **$127,000 synthetic net short**, growing toward $250,000–280,000 as delta approaches −1. "We have no intention of losing this position."
- Wing: sell short-dated OTM puts collateralized by the anchor to offset the anchor's theta and vega burn: sold the April 17 265 put for **$4.75**, closed it a week later at $0.44 → **+$4,300**; rolled down/out to the April 24 260 for another **+$1.00 (+$1,000)**. Net cost of the anchor: $20,482 → ~$15,700 → ~**$14,700 ($14.73/contract break-even)** — and keep chipping until "the spidey senses" say the crash is underway; then pull the wing and ride the long put through the decline.
- If the market rips to 3,000 instead: the July 280 put (~$20 OTM) is still worth ~$12–13, all harvested income is kept, and the net damage is ~$3,000–4,000 — which continued harvesting keeps shrinking.
- If the market *gaps* down (SPY 250 overnight): the short 265 put builds $10+ of intrinsic and the structure behaves like a debit spread capped at the strike width — so **roll down and out immediately** (265 → 250 plus two weeks → 240/230). And if all of this is too fancy: "just buy the put and hold it — you'll just eat the carry."

## 3. Trading Volatility (the Long-Vol Toolkit)

<!-- Sources: Trading Volatility Bootcamp (1080p with 25fps).transcript.md -->

**The why.** This bootcamp unpacked Chris Cole's (Artemis Capital) MacroVoices thesis of the hundred-year portfolio: a standard 60/40 is badly positioned for the big deflationary and inflationary impulses; the resilient shape pairs long equity (roughly a quarter to a third of the portfolio — "he's not getting rid of the equity") with commodity trend-following (CTA) and **long volatility**. The key distinction Ceresna hammered: this is not hedging a rainy day but "hedging for a **rainy decade**." A VIX spike from 15 to 50 in one week pays once; if vol then sits at 35–50 while the market keeps bleeding lower, a VIX-position holder has no remaining hedge. Long-vol *structures* have to keep paying through the whole regime.

**Why he won't trade VIX products.** VIX options are options on **VIX futures**, not the spot index. His live example (VIX spot 48.52): the June VIX future traded at **25**, so June put–call parity lived at the 25 strike (~$4 call ≈ $4 put) — while the "at-the-money" 50 strike showed a $0.60 call against a $25 put. April's parity sat near 31. The term structure (first month 39.62, then 35, 31, then June at 25) was in backwardation during the crash; normally it's in **contango**, which is the negative carry that bleeds these products. Trading VIX options therefore means betting on the *shape and migration of the futures curve* — "not a game for beginners, not a game for intermediate traders… there are some really smart people who trade volatility; leave it to them." Same verdict on **UVXY** (ProShares 2× VIX futures): betting on the October 2019→March 2020 crash with it meant riding it from ~$28 down to ~$10 — wiped out **67%** — before the payoff, and even after the VIX doubled you weren't back to break-even until the final gap. Contango bleed owns you in calm periods.

### Tool 1 — the rolling straddle (Chris Cole's portfolio hedge)

**Construction.** Against the long equity sleeve (his $1M example holding ~$294–300K of SPY): buy an **at-the-money straddle with ~9–12 months of duration**; the combined starting delta is ~zero (his live numbers: +$155 call delta dollars vs. −$144 put). After ~6 months — with ~3 months of life left — **close it and reopen a fresh ~9–12 month straddle**. That's the whole system: systematic, mechanical, never re-centered intraday.

- **Why the clock matters:** option decay is non-linear — it accelerates exponentially into expiry — so rolling at the 90-day mark never pays the steepest part of the theta curve. The hope is that six months of market movement builds enough intrinsic value in one wing to roll at ~break-even; when a genuinely "redonkulous" move arrives (a 30–40% crash, or an inflationary face-ripping rally), the deep wing explodes and pays for the equity drawdown. Backtested (Cole's work): a long straddle produced positive carry for the greater part of 70 years, including through the Great Depression and the 1970s — both deflationary and inflationary tails.
- **Max loss discipline:** even here, the U-shaped max loss exists only at expiration exactly at the strike; Cole in practice closes at 90 DTE, so the realized drawdown is the shallower pre-expiry dip, not the full premium.
- **Do NOT monetize and re-center on a spike.** Asked whether Cole would have taken straddle profits and re-struck at the money during the March 2020 crash: "Absolutely not." Re-centering returns the position to delta zero and defeats the entire purpose — you *want* the wings to go deep in the money and stay there while equities are destroyed. Only the calendar roll happens.
- **Entry pricing matters — buy the first one cheap.** At SPY 300 and 270 DTE: at 25% implied vol the ATM straddle is ~$50 (call ~$26 + put ~$25; his sim printed $29 + $25), with expiration break-evens at **250 and 350**; at VIX 12 the same straddle is ~$24 (call ~$13 + put ~$11) — **half price**. The one-year implied range: 75 SPY points (225–375) at 25 vol vs. 36 points (264–336) at 12. His home-buying analogy: get your *first* straddle on in a cheap-vol environment; rolling later in expensive vol is fine because you're swapping one expensive straddle for another, like trading up from a house you bought cheap. Starting a rolling program after vol has doubled is the mistake.

### Tool 2 — ratio spreads as tail gamma (the low-carry long-vol vehicle)

**The idea.** "If you're hedging for a rainy decade you need to be **long gamma**, long gamma with a very low carry cost — and the ratio spread is the number-one way I'm aware of to own a shitload of gamma on the wing." Structure (put version): short 1 at-the-money put, long 2–3 far out-of-the-money puts, near zero cost, same expiry. When calm, the position costs ~nothing and the deltas roughly offset; when the crash comes, gamma blows the net delta out and the long wings print.

**Worked example — AMD (his live position).** Opened with AMD near $58: sold one **July 57.50 put at $6.53** (+$653 credit, "think of it as income") and bought **three July 47 puts at $2.50** (−$749) — a **~$100 debit per 1×3**. (A 2:1 version would have been a small credit; "whether it's a small debit or small credit, it has almost no carry cost.") He banked partial profits as AMD fell through ~$42.

- Payoff shape: flat/zero cost if AMD *rallies* — the long wings are free left-tail insurance; the only true max-loss point is expiration pinned between the strikes (~48 on his graph, where the short put is deeply underwater and the longs haven't caught up) — which is exactly why the standing rule is **never hold a ratio spread to expiration; close with at least a month of time left**.
- Gamma accounting: short 57.50 put gamma ≈ −$0.02; each 47 put ≈ +$0.02, ×3 = +$0.06 — times the 300 share multiplier, structurally **net long gamma**. Live consequence: with AMD selling off, net delta dollars were already −$2,500 (synthetically short) and would keep compounding toward roughly −$15,000 in a continued crash, while the long puts' delta contribution maxes out around +$5,000. That self-reinforcing shortening *is* "being long gamma" — the position gets more bearish exactly as the tail arrives. At the time of the class the trade was +$500 on the ~$100 outlay.

**The skew problem — when you cannot open these.** In the March 2020 crash the S&P's left tail was brutally fat: ATM puts (~297 strike) priced at ~30% implied vol ($21 for the ATM put), the 250 strike at **50–60% implied**, the 200 strike at **60–100% implied**. To structure a zero-cost 2:1 you must sell the expensive ATM and buy wings so far away (≈SPY 260 / S&P 2,600, 105 days out in June) that you'd need a crash *toward 2,000* for the big payoff — "an extraordinary move beyond 260 just to pay off." High implied vol also forces 7–9 dollar strike gaps where 3–5 dollars used to do. Verdict: **don't open put ratios after vol has spiked** — the asymmetry is gone (that asymmetry existed in January 2020, which is when these should have been opened); in that regime plain **debit spreads** are the compelling tool instead.

**Where Cole's "active management" comes in.** Hunt for correlated assets whose vol surfaces are *not* fat-tailed — individual stocks, sector ETFs (his XLK check showed the same spike/fat-tail shape as the index, so look elsewhere) — and buy the tail gamma where it's mispriced and cheap to carry, so it pays when the whole market "starts to shit the bed." His own live example: the **LQD** 2:1 put ratio (corporate-credit tail) was early and wrong — LQD rallied to $134 — yet still sat profitable, and a fresh version (e.g., September ATM ~34 put) remained available, though crash-widened bid/ask spreads made new entries ugly. That's the other market-maker behavior to respect in crashes: they *raise* implied vol (to be paid on the short side) *and* widen spreads (cushion against getting steamrolled), so new long-vol entries are always worst-priced exactly when the fear peaks.

**Both tails.** A long-vol fund buys right-tail gamma too, because inflationary regimes blow out the upside (his example: Abenomics — deliberate yen debasement and the Nikkei's explosion). The upside version is the mirror ratio call spread (Section 1's July 300/325 zero-cost 3:1 S&P example, which the flat call skew and lower long-dated vol made cheap). The IVOL ETF (Nancy Davis, Quadratic) came up as a real-world cousin: long *bond* volatility via OTC derivatives on top of an 87% SCHP (TIPS) sleeve — finally paying as rate vol spiked and the curve steepened.

**Carry, in one picture.** Between the strikes the position has a shallow negative "belly" (the max-loss zone) but near-zero cost everywhere else — which is the entire point: insurance you don't notice paying for. And the standing sizing caveat: the true tail payoff is convex, so express it in sizes where the belly loss is trivial relative to the portfolio.

## 4. Building Synthetics

<!-- Sources: BuildingSynthetics (1080p with 25fps).transcript.md -->

**Who this is for.** Ceresna splits his audience into two archetypes: those with money who want to *keep* it, and those with small accounts who want to *juice* returns. The plain hedged-stock trade serves the first; synthetics — same exposure, a fraction of the capital — serve the second. "This is not for everybody, and I'm not encouraging gambling, but it is a legitimate way to leverage."

**The mathematical identity.** A long call is a synthetic for **long stock + protective put**. His Amgen demonstration: 300 shares at $195 (~$58,500) plus 195-strike puts showed **~$30,000 of net delta dollars** ($58K stock minus ~$28K put); three October 195 calls at $3.60 (~$1,000 total) showed the *same* ~$30,000 delta dollars. Identical exposure, 98% less capital.

**But psychology differs, and he deliberately teaches the stock-plus-put form.** When you own shares, your attention is on the stock and the put reads as a stop-loss; when you own the call, the screen shows "−40%" the moment premium decays and almost everyone fixates on that percentage. Same P&L, different behavior. (And "each of you is as unique as your fingerprint" — if calls suit your temperament, that's not wrong.) There are also mechanical questions a naked call raises that the stock+put form answers naturally: how do you "roll up" a call when the stock rallies? The hedged-stock playbook has explicit answers:

**The hedged-stock playbook (the Breakout Trader method).**

- Enter the stock and buy a ~17-day at-the-money put (published on a Tuesday, ~2 weeks to expiry). Breakout trades resolve in **2–6 weeks** (sometimes 8): Amgen's last comparable run took 28–36 days; if you're wrong, it usually shows within a couple of weeks.
- **The target-one roll — his favorite adjustment:** when the first target hits, close the original put and buy the put at the new price. AbbVie example: bought at $71 with $71 puts (~$1 each); at the $74 target, swap to the $74 put (~$1). Total put spend $2, guaranteed sale price $74 → **$3 locked gain minus $2 = a risk-free trade** with 100% of the upside still attached. Amgen version: target 200, roll the 195 put to a 200 put — the original $1,000 risk becomes zero.
- **Why a put and not a trailing stop:** a stop at 195 gets *gapped through* — an earnings print, a Trump tweet — and fills far below; the put is a contractually **guaranteed sale price**. Same intent, no gap risk.
- **Extension rolls when nothing happens:** if the put is expiring worthless and the chart still looks right, buy more time rather than exit — AbbVie's $74 put at $0.02 could be rolled one week for ~$1.05 or two weeks for ~$1.45 (≈$800–870 per 6 contracts); against the $7 measured-move target (74 → 82) that's ~5:1 upside-to-cost on the extension. Alternative style for the cheapskate: buy a far strike ($71) put for $0.47 (~$280 for 6) that only guarantees a break-even exit. Both are fine — stylize to your own temperament.
- **If nothing happened, ask why before extending:** weak tape that will resolve later is a reason to give it time; a broken setup is a reason to move on. And don't micromanage the entry — an intraday rejection off the 61.8% retrace is noise; the entry is just a level where you *discover* whether the breakout works. If Amgen never beats 195, it's a failed trade: exit cheaply and find the next one.

**The leveraged synthetic long.** The small-account version of the same trade: replace the shares with a **deep in-the-money, ~0.90-delta call at least ~6 weeks out** (it needs enough time to keep behaving like stock), then add the same short-dated protective put.

- Amgen construction: **November 170 calls at ~$27** (~0.90 delta; ~$8,000 for three — work the wide spread on deep ITM options) plus the **October 195 puts**. The 170 call + 195 put lock **$25 × 300 = $7,500 of guaranteed intrinsic value**; total outlay ~$8,000–9,000; worst-case risk ~**$1,500**; controlled upside ~**$54,000**.
- Simulator comparison of the same Amgen thesis: shares + puts (outlay ~$59,000) — crash to 170: stock −$7,500, put +$6,500, net **−$1,000**; full measured move to 225: +$9,000 − $1,000 = **+$8,000**, a ~13–15% return. Synthetic (outlay ~$8,700): pullback to 180: call −$4,000, put +$3,500, net **−$765**; move to 225: **+$7,900 — roughly a 100% return** on capital at risk, with slightly wider spreads as the friction.
- **The theta question, answered:** yes, you pay decay on both legs — but the deep ITM call's premium is almost all intrinsic. The November 170 call at $25.76 with the stock at 195 carries only **$0.76 of time value**: your theta burn is on 76 cents, not $25.76. The extra time premium on the synthetic *is* the price of the leverage — "it doesn't come for free."

**The philosophy underneath** (his own summary of the whole method): "When we're wrong, we lose very little. When we're partially right, we get the chance to not lose anything at all. And when we're right, we make big money."

## 5. Hedged Positions (Macro Trades with Option Asymmetry)

<!-- Sources: HedgedPositions (1080p with 25fps).transcript.md -->

**The mandate.** Hedge-positions trades run **1–12 months, sometimes multiple years** (his standing examples: a uranium position and IVOL that members would still find in the portfolio a year later). They are the opposite pole from Breakout Trader: not the short-term squiggles, but an expressed **macro fundamental belief**, with market timing attempted at the turn, and options as the mechanism that builds the asymmetry. The formula in one line: macro narrative → technically observed timing → option structure for asymmetry.

**Tail hedges are allowed to do nothing — that's the design.** The IVOL example: 87% of that ETF's cash sits in SCHP (the Schwab TIPS ETF), so the hedge bought was **SCHP $55-strike protective puts** against catastrophic TIPS-side loss. Members asked why the hedge "wasn't working" during a few red days: check the **delta dollars** — IVOL behaved like ~$52,000 of stock while the puts behaved like only ~$5,000 short. A tail hedge is *supposed* to be a small short that stays small until the underlying breaks; only if SCHP crashed below 55 would the puts' delta dollars explode to ~$30,000–40,000 and behave like a real hedge. Little-to-no immediate response is the feature, not the bug.

**Managing a calendar straddle through a real decline (the live SPY example).** His September-2019-top straddle, into the October 2019 selloff and snapback:

- **Roll the short call down** to the October 11 288 strike (members' fills varied: 285, 290, 294). The original call, bought at **$3.59**, was now worth **$6.30** — the short-dated gamma did exactly what it was bought for, exploding in the v-shaped rally.
- **Convert the long put into a debit spread:** sell the 260 put against the 302 put (collected ~$4, **+$1,000**) as vol contracted and price moved away from the strike. The put leg's open profit had receded from ~$6–7K to ~$3K, but the call + short-put combo had added ~$3.5K — the first leg of the decline was fully banked.
- **Read the position in delta dollars:** puts behaving like a **−$190,000** market short; the call + short put adding **+$265,000** of synthetic long — net *long*. Translation: if the snapback kept going, the position would keep *making* money on the combo faster than the puts bled. The hedge had become a bet on more upside, which is why the next adjustment was due.
- **The adjustment zone (technical timing):** on the 4-hour chart, the Fibonacci confluence around S&P 2940 with the 78.6% retrace at ~2960 lining up on the lows — "odds are the adjusting trade is right in here." Mechanics: sell the 288 calls (~**+$2,600–2,700**), buy 293 calls; take the $1,000 profit on the 260 put (the "tactical" choice — re-sell it on the next leg down) or hold it to expire and treat the $4 as cost reduction; either is legitimate. Result: a locked **$9 of intrinsic** (302/293) and net delta dollars back to **−$40,000** — properly short again for the next leg.
- **His roadmap at the time:** one more leg lower, a rally into December/January, then the real sell-off — "the really big money is a 2020 story."

**Entry discipline for late arrivals.** Members who saw the snapback and wanted in were told the math honestly: the original trade went on at ~14–15 implied vol; a fresh at-the-money straddle (October 293 call ~$4.70 + January 293 put) cost **$15+**, and a mere normalization of vol back to 14 would mark it to ~$12.50 *before any time decay*. Chasing a move has worse risk/reward than the published entry by construction. If you must participate, do it with **one or two contracts** for the education of managing it — "this is not the go-heavy moment."

**Expressing a macro bottom with a hedge.** The Schlumberger setup (at $31.84, sitting on its previous major low, with no technical confirmation yet — "that's why you need the hedge"): three legitimate expressions of the same view — (1) buy the stock and buy the November $32.50 put (~$2) or $30 put ($0.94) to remove catastrophic risk while the bottom proves itself; (2) replace the stock with a **January 2021 $30 LEAPS call at $5** — $2 of intrinsic, a guaranteed $30 purchase price, and a delta that contracts as the stock falls, so being early costs ~$0.60 on the dollar instead of $1.00; or (3) a short-dated call purely as an entry mechanism. Same view, three risk geometries — choosing among them *is* the craft.

**One standing observation worth keeping.** The "bizarro world" of bad-is-good markets (weak data → Fed cuts → rally) had persisted for years, and his warning came with it: the crowd trade of "bad news is bullish" ends the day bad news becomes bad news again — which is precisely the scenario every structure in this document is built to survive.

---

# Part IV — Gold and Commodity Options

<!-- Sources: AsymmetricStrategiesToRepairAndLeverageYourGoldHoldings; How to Leverage Gold Like a Pro (even if you hate risk); How to Find Asymmetry on Your Favourite Commodity Stocks; Using Options to trade Commodity Cycles; HedgingPhysicalGoldAug212020; TradingGoldCollarsAug172020; GOLD CYCLE - April 16 2021 LIVE Webinar -->

## 1. Why Own Gold: The Investment Rationale as Taught

<!-- Sources: Asymmetric strategies to Repair and Leverage Your Gold Holdings (w/ George Gammon); How to Leverage Gold Like a Pro (even if you hate risk) -->

### Gold as insurance, miners as speculation

**George Gammon's** framing (co-host of the gold webinar): gold is an **insurance policy** — comparing it to Bitcoin or stocks misses the point of what it does in a portfolio. Gold **miners** are something completely separate: a **speculative play with good asymmetry**, to be bought when unloved and out of favor. **Luke** co-hosts the commodity-cycles webinar as the "leveraged investor" in the worked examples.

Gammon's portfolio logic: own gold (he sizes it around 10% of net worth in the worked examples) purely as insurance against monetary disorder; do **not** judge it by Bitcoin's or stocks' returns, because that is not its job. Gold miners are a separate allocation — a speculation where the asymmetry is the attraction. The time to buy speculations is when they are maximally unloved: at the time of the webinar, financial media was "Bitcoin, Bitcoin, Bitcoin" after the new Bitcoin ETF launch, and **nobody was talking about gold** — which reminded him of uranium before March 2020, coal a year before its move, and oil in November before its run. Ceresna's counter-observation: he had just spoken at the New Orleans Investment Conference and "all the pros are talking about gold" — Jim Rickards, Danielle DiMartino Booth (over dinner), Brent Johnson, Jim Grant (on a panel) — but the **mainstream** media is not. That combination (insiders interested, public asleep) is the early-inning fingerprint. On sentiment, Ceresna is blunt: the only thing that drives sentiment is **price level**. Rising prices make everyone find stories explaining why things are amazing; falling prices make everyone go quiet and make excuses (e.g., "Bitcoin is taking gold's money flow"). "**There is only one cure for the sentiment of gold, and that's higher gold.**"

### The gold-miner cycle numbers behind the bull case

The GDX (gold miners ETF) data used at the time: 13–14 months of consolidation, down about **37%** from the prior peak — versus an average miner decline of roughly **9 months and ~40–42%** off the highs. So the drawdown was already typical-to-mature in both time and depth. Technical structure supported "correction within a bull market that started in 2018": the decline was roughly a **50% Fibonacci retracement** of the prior advance, and **volume profile** showed a solid base of buying below (the dark bands marking the price levels where ~70% of volume transacted), with price still trading above that base on a monthly chart. The **measured move** projection from the consolidation pointed back to the prior highs — aligning with the 2011 highs — i.e., GDX from ~$30 back to ~$60, about **+100%**. Historically, across the nine previous completed corrections, the average recovery rally lasted about **11 months and roughly doubled GDX**. Ceresna's caveat, repeated so it is not misused: "There are no guarantees... don't stop managing risk because Patrick said it's going to double." These are quantitative averages of past cycles, not a promise.

### Gold's macro role: the dollar, not CPI charts

Ceresna pushes back on the standard overlay-of-real-rates analysis (the real-yield framework he *does* use appears in Section 8): look at the biggest picture first — **gold is priced in U.S. dollars**, and its biggest cycles line up with dollar purchasing-power cycles. From 2000 to 2008 the dollar lost about **50%** of its value against other currencies; over the same period gold went from **$250** an ounce to breaking $1,000 and on toward $1,500. At the time of the webinars the dollar had been relatively strong for about three months, which he saw as the drag on gold; the real gold cycle arrives "when real inflation emerges during a cycle of dollar weakness," likely coinciding with the big monetary-policy shift. His sequence expectation: markets are in a taper-and-tightening phase; eventually a risk-off cycle "will spook the Fed," policy pivots, and — as it has "numerous times" before — gold will be there. A Bloomberg interview in which the former Goldcorp CEO called for **$3,000 gold** "in a matter of months" is cited as an example of the kind of thesis Ceresna does *not* personally endorse but which defines the scenario in which upside skew trades pay off.

### On manipulation — a strong contrarian opinion

Ceresna, speaking to a hard-money audience, deliberately contrarian: "I call bullshit on someone who says it's in the best interest of the Fed to manipulate" gold and silver. The gold and silver markets have become **so small relative to the financial system** that manipulation is not worth the Fed's effort — "I would argue that manipulating Bitcoin would be far more in their best interest." When gold and silver finally move, paper and physical "go screaming higher" together. Suppression arguments repeat the uranium experience: when uranium traded below its cost of production, everyone explained it with manipulation stories; in the end supply and demand prevailed — and holding a commodity below the price that clears supply for too long simply distorts the market and "creates that much bigger of a bull market on the other side."

### Physical metal vs. portfolio gold — and why the distinction matters for options

Ceresna is careful to split the audience. If you are a hard-money investor who must hold **physical** coins and bars because the insurance is against system failure — "I'm not even going to try to argue against that." But if your gold sleeve is a **portfolio insurance/diversifier allocation** — the way Chris Cole's Dragon portfolio holds close to **20%** gold exposure as a long-run diversifier — then the *insurance function* can be replicated or extended with option structures for a fraction of the capital, and those structures are the subject of Sections 3–7 (hedging the truly un-optionable physical is Section 4). Silver gets the same treatment: its monthly chart shows a prolonged bear market and an extended base retested in the COVID crash, so "the silver bull market never really legitimately started until the post-COVID period" — only about a year old at the time — and if silver "blasts off," $35–$40 (from ~$22–23) "probably by late 2022, 2023" is in range. Silver, even more than gold, exhibits the skewed option pricing described next.

## 2. The Precious-Metals Volatility Skew: The Engine Behind Every Structure

<!-- Sources: Asymmetric strategies to Repair and Leverage Your Gold Holdings (w/ George Gammon); How to Leverage Gold Like a Pro (even if you hate risk); How to Find Asymmetry on Your Favourite Commodity Stocks; TradingGoldCollarsAug172020 -->

### Options are priced off probability distributions

An option's price, "in its purest form," is the market's estimate of the **probability that the option will make money**; the single biggest determinant is **implied volatility (IV)** — the market's forward estimate of how far the underlying can travel. Two facts most retail holders miss:

- **IV is not one number per security.** The VIX, for example, measures only the closest **at-the-money strikes ~30 days out** on the S&P 500. Implied volatility actually differs at *every strike and every expiry*.
- **IV defines a probability cone.** One standard deviation of the implied distribution contains **~68%** of the expected outcomes. Example used: GDX at $18 with IV 27.7% implied a 68% one-year range of roughly **$13–$23**.

You do not need to forecast IV to use skew — you only need to acknowledge that it exists and ask which direction it is tilted.

### The normal (equity) skew: fat left tail

On the S&P 500 — and most stocks with market correlation — implied volatility **rises as strikes go down** and **falls as strikes go up**: the "fat left tail" (the check-mark shape). Two sessions' worth of worked numbers:

- With the market at ~328 (SPY), a protective put ~10% out-of-the-money (~295) is priced near **20% IV** across the February/March/June expiries, while a covered call ~10% out-of-the-money is priced near **10% IV**. Consequence: a put can cost **two-plus times** the income you collect selling the matching call.
- With SPY at $338: the 350 strike call trades at 14–16% implied and pays only **$4** (a strike $12 higher); a put $12 lower (326) costs **$7.25** at 22% implied; at the 300 strike puts price near **30%** (29.4%). The SPY "zero-cost collar" is therefore sell the 350 call for $4, buy the 307 put for $4 — **$12 of upside against $30 of downside, a payoff ratio of 0.38**. "This is just brutal... 3% upside but a 9% downside is an awful payoff profile. And this is why opening a collar on the stock market is just something most people don't do."

Consequence: in normal equities, **collars have no asymmetry** — the insurance costs more than the premium you harvest, so there must be a separate tactical reason to run one. The market-structure reason for the skew is the old adage: **markets rise on an escalator and drop on an elevator** — gradual grind higher, violent breaks lower — so downside options must price the violence.

### The gold/silver skew: fat RIGHT tail

Gold (and silver, and the gold miners) is the bizarre exception: implied volatility **rises as you go further out-of-the-money on the CALL side** — gold "skews for a right-tail crash *upside*" (a U-shaped skew with the right side lifting immediately). Worked numbers at the time:

- GLD at $146.58: a put ~5% OTM (the 139) priced near **10% IV**, while calls 5–10% OTM priced at **14–17% IV**.
- On silver (SLV at $22.70), the January 2023 chain showed IV **rising with every dollar strike** from 29 up through the low 30s and beyond.
- On Agnico Eagle, at-the-money IV was 32–33% with the right tail reaching **~50%**.

Two reasons Ceresna gives: (1) gold is **negatively correlated to risk** — in a sell-off, upside calls on gold become the crisis asset everyone wants, so market makers price them rich; (2) gold's physical analogue: its worst left-tail events are slow bleeds, while its explosive events are *upside* (monetary crises, inflation breaks) — so the options market prices the right tail rich. The **term structure of gold futures is in contango** — forward prices above spot (spot ~$1,550 at the snapshot) because the future price must carry storage, insurance, and financing — which further flatters the economics of holding upside calls.

### What the skew makes possible

Because out-of-the-money calls on precious metals pay "exorbitant" premium while downside puts are comparatively cheap, three families of trades become structurally favorable in gold/silver that simply do not pay in the S&P 500 or large-cap equities:

1. **Near-zero-cost collars** (sell rich upside calls, buy cheap downside puts) — Section 3.
2. **Long-dated far-OTM bull-call debit spreads** that replicate what institutions call **digital options** (small stakes, 10:1 to 20:1 payoffs) — Section 5. This is the retail expression of what Chris Cole describes as right-tail insurance.
3. **Repair strategies** on underwater miner positions, financed cheaply by the same rich call premium — Section 6.

One more structural tailwind for dated collars: put–call parity for a 6–12 month collar anchors at the **forward** price, not spot, which further tilts the collar math in the seller-of-calls/owner-of-puts favor. All of this applies to the precious-metal miners as well as the metals themselves.

## 3. The Gold Collar: Leverage with a Defined Worst Case

<!-- Sources: Asymmetric strategies to Repair and Leverage Your Gold Holdings (w/ George Gammon); How to Leverage Gold Like a Pro (even if you hate risk); TradingGoldCollarsAug172020 -->

A **collar** is a hedge wrap: own the underlying, **sell a covered call above** to collect income that **pays for a protective put below**. The slogan is "limit the downside and limit the upside," with the correction that the upside is not truly capped — it is **managed** (below). Gold is one of the few assets where a zero-cost collar has a *favorable* payoff shape; on most stocks it does not (Section 2).

**The macro premise** (from the August 17, 2020 collar webinar): **financial repression** — "a period from which governments and central banks attempt to create inflation in order to fix the massive and sheer amount of debt in the system; they want to inflate it away, which basically means they need to suppress interest rates at levels that are much lower than the prevailing rates of inflation." The asset that performs best under financial repression is **gold**, so a strong allocation to gold and gold miners belongs in a good asset mix — underscored by Warren Buffett's just-announced Barrick Gold stake: "even our cherry Coke loving octogenarian is jumping onto the bandwagon."

**The 100%-allocation story.** On a San Francisco Silver and Gold Summit panel with **Grant Williams, Brent Johnson, Cal Everett and Marin Katusa**, Katusa asked how much gold every investor should hold; the panel answers ranged **10–20%** of a portfolio. Ceresna's answer was deliberately bolder: "I actually have 100% of the value of my investment portfolio long gold... But I am collared on my gold holding, which allows me to manage my risk." The book he demonstrates: a **5,700-share GLD position**, original purchase ~$125 → ~$700,000 cost, now worth over $1,000,000 (+$350,000) — "enough profit for most people to make a meaningful change in your lifestyle." His point: the question is not the percentage of the portfolio, it is whether risk is managed.

### The reference trades (from both webinars)

**Published GLD collar, January 16, GLD at $146.58:**

| Leg | Structure | Detail |
|---|---|---|
| Underlying | Long GLD | Basis $146.58 |
| Downside | Buy June **139 put** | ~5% OTM; cost ≈ **$1.05** |
| Upside | Sell June **165 call**, covered | ~13% OTM; income ≈ **$1.00** |
| Net cost | Small debit | "Very close to no cost" |

Outcomes: maximum loss **~5%** (basis falls to the 139 guaranteed sale price plus the tiny debit); upside to **+13%** (to the 165 cap). This is the Soros shape in one trade: lose ~5%, win up to ~13%, at roughly zero carry. The skew is what makes the strike pairing possible — the 5%-OTM put at ~10% IV costs about the same as the 13%-OTM call at 14–17% IV, which would never be true in an equity index.

**August 17 GLD collar, GLD near $187, ~60 days to October expiry:**

- **Put leg:** buy the 177/178 put (about 5% out of the money) for ~**$2.74–$2.75** — insurance removing all loss beyond a 5% decline.
- **Call leg:** sell the 200 strike call (~$13–14 higher) for ~**$2.90**.
- **Net cost: zero.** Upside to 200 (~$13) exceeds the protected downside (~$10) — a positively skewed, zero-carry position.

Simulator caveat (taught openly): the position simulator assumes constant volatility (his run used 21% and GLD 185), so it cannot show the skew — there the same 3-lot collar showed a small debit (~$1.60 collected per call, ~$500, versus ~$886 paid for the puts, ~$400 net). That is a modelling artifact, not the live economics.

**The leveraged collar: a $250,000 gold position with ~5% risk** (the scaled-up version from the Gammon webinar). Setup: George already holds ~10% of net worth in physical gold; he now wants meaningful *additional* gold exposure in the trading account, risk-defined.

| Leg | Structure | Detail |
|---|---|---|
| Underlying | Buy **1,500 GLD** (~$250,000 notional) | GLD ≈ **$169** |
| Downside | Buy 15 protective puts, strike **160** (~5% OTM, ~235 days / ~8–9 months, June) | Cost **$6,800** |
| Upside | Sell 15 covered calls, strike **185** (~10% OTM) | Income **$5,300** |
| Net cost | ≈ **$1,500** (~$1/contract) | |

Outcomes: below 160, the guaranteed sale price locks the worst case at roughly the 5% line ("it might as well go down a lot" — the hedge is already paid for); between 160 and 185 both legs expire worthless and you simply keep 1,500 GLD at the original basis; above 185 the shares are called away at +10% unless you roll. Ceresna's framing: the upside (10%) is **twice** the defined downside (5%) on a near-zero-carry position — asymmetry "beyond the break-evens."

**The leveraged-versus-diversified comparison** (a $100,000 portfolio in the simulator):

| | Investor 1 — "textbook" | Investor 2 — collared and leveraged |
|---|---|---|
| Allocation | 10%: 55 GLD shares ≈ $10,000 | 50%: 300 GLD shares ≈ $55,000, bought up on margin |
| Hedge | none | 3× Oct 177 puts + 3× Oct 200 calls (≈zero cost live) |

- **Upside (GLD to $200 in 15 days, vol constant):** Investor 2 is up ~$3,000. Investor 1 would need GLD at roughly **$260** — gold up several hundred dollars an ounce — to earn the same $3,000.
- **Downside (GLD to $150, back to its February level — "not out of the realm of impossibility"):** Investor 1 is down ~$1,900. Investor 2 — carrying **5.5x the gold exposure** — is down only ~$2,800, versus ~$10,000 unhedged. The collar absorbs everything beyond the first ~5%.

### Why a collar changes the *experience* of a gold drawdown

In 2016 and again in 2018, GLD went through distribution cycles of **$20–25 (15–18%)**. "At some point gold is always vulnerable" to one of these, and for the unprotected holder that is when commitment gets tested — "that knot in your stomach... should I just get out?" The collar holder is in a different psychological state: if GLD crashes $25–26, from ~$146 to ~$120, the put lets you **sell everything at 139 and buy it back at ~120, improving your cost basis by ~$19**, on a hedge that cost nothing to open. You end up *cheering* the crash — "have you ever been fully invested... and then started cheering for it to go down?"

**The monetization move** (the piece he says "almost everybody takes for granted"): the 177 put is a **contractual right to sell at 177 even though the market is 150**. In the crash scenario:

1. Exercise the puts → ~$50,000 cash lands in the account. Total damage on the way down: ~$2,800.
2. Buy back all 300 shares at $150.
3. You now own the same gold with **all of the upside from $150**, having paid only $2,800 for the entire round trip — and the collar itself cost zero to carry.

"When we are hedged... it'll be the first time in your life that you're actually cheering for your gold to go down. Because if it ain't going to go up, it might as well go down a lot so you could sell it at a higher price and buy it all back at a much cheaper price." One tax note from Q&A: if selling the shares would trigger capital gains you don't want, **don't exercise — sell the put itself** into the crash (his example: a $7,400 put profit) and monetize the protection while keeping the shares.

### Managing the collar when gold runs

- **The rule: never let the position be lost to the short call.** "We never allow our position to be lost... It's the only curse I wish upon all of you — that the security is moving so fast to the upside that you're running into problems with your covered calls because you're making too much money on your stock." (Elsewhere: "the problem you have is that you're making too much money too quickly — it's a curse I wish upon all my members.")
- The covered call is sold at a "tactical level" where, on balance of probabilities, it expires worthless. If gold rallies too fast and GLD approaches the short strike, the action is a **roll-up**: close the 165 call, sell a 175 call (or close the 185, sell a 190/195; in the August session, approaching 200, buy the call back — marked ~$1.25 sold → $1.57, a ~$300 loss — and **sell a new call at 210 or 215**). The roll takes a debit/loss on the short leg, but it is absorbed by a large unrealized gain on the shares and re-opens upside on the underlying. "We're never going to make a dollar-for-dollar delta long with collars. We're always going to be taxed to some degree for being hedged. But as long as we're managing those losses by rolling the calls, we can consistently be leveraging the gains."
- Roll **before** the call goes in the money — and yes, they would roll an in-the-money call too.
- **The put leg:** rolling it is optional; "it all depends on what you're trying to achieve with the collar. I don't want to claim that there's one right way."
- If expiry lands **between the strikes** (e.g., GLD at 183), both legs simply expire and you keep the shares at their original basis. If the goal was ever to exit, assignment across the line realizes the capped gain by design.
- **Longer-dated collars** (e.g., ~200 days out to March on the GDX) are fine and can be near zero cost — roughly $6 lower (a 36 strike put ~$2.80) financed by a ~53 strike call (~$3.00) gives $10 of upside against $6 of downside — but you lose flexibility: gold can make "extraordinarily big moves" in six months, so expect more frequent adjustment trades.

**Max-loss accounting** (Q&A): maximum loss on a collared position = the strike gap plus the put premium. Example: $185 GLD with the 177 put costing ~$3 → worst case **$11 per share ($1,100 per 100 shares)** no matter how far GLD collapses (crash to $100: down $8,000 on stock, up $7,000 on the hedge).

### The same collar works on silver; it works (less dramatically) on miners

- **SLV at $25.60, October expiry:** a ~10%-lower put (23 strike) costs ~$1.30; the 31 strike call pays ~$1.20 — a near zero-cost collar with **all risk removed below 23 and all upside to 31**, a payoff ratio of **2.16** ("twice as much upside as downside, for zero cost").
- **GDX:** the skew is not as asymmetric but still right-tailed. Example: the ~$4-lower 38 strike put costs $1.30 while the 50 strike call collects $1.13 — a **15–20 cent debit** for $7.50 of upside versus $4 of downside.

### The philosophical point: the collar replaces diversification

Diversification is "the most accepted thing in the financial industry for managing risk," and Ceresna does not dismiss it — it genuinely removes unsystematic risk. **But it also dilutes returns**: owning 20–50 things that are half going up and half going down lands performance "right down the middle." Defined-risk options offer the alternative: **take a full-sized, high-conviction position — "go all in on gold," even $500,000 of exposure on a $100–200k account — with the worst case defined at ~5%**, and let the position sizing come from the hedge rather than from spreading capital thin. The one non-negotiable: a high-conviction position must carry an exit that prevents being zeroed, because "our brains convince us that our ideas are always the best."

**Entry doctrine** (from the August Q&A): members arriving after the run-up asked whether to buy at these levels. His answer: "No, it is not too late to buy. You absolutely can buy up here, but you must be hedged, because the downside risk if we get caught in a correction is considerable." Don't wait for the perfect entry: "If you keep waiting for a perfect entry, then gold might run away without you being in... the collar is doing your risk management for you." If a pullback worries you, spend a little more for **closer-to-the-money protection**, so that a correction can be monetized into an improved cost basis. His closing caution: he remains very bullish gold, but it "has lost its asymmetry" — new positions at this stage carry downside risk "that is no longer small... this is a far more important time to be doing this at this stage in the market cycle."

### Collar Q&A — captured in full

- **Hedging a $100,000 basket of 10 miner stocks (Scott):** buy $100,000 notional of GDX protection — the GDX correlates tightly with the miners (an overlay of Newmont and Barrick tracks in line). "Just do it dollar for dollar and I wouldn't bother to make it more confusing," delta-adjusting only as a refinement of index hedging.
- **Short selling versus puts (Christopher):** outside that session's scope (collars and debit spreads); the master's programs cover direction-bear structures.
- **Total risk on a 177 put against $185 GLD (Michael):** covered in the max-loss accounting above.
- **Avoiding the taxable sale (Michael):** don't exercise — sell the put into the crash, keep the shares.
- **What if GLD blows through the call strike (Rick):** they actively roll before the money — approaching 200, roll 200 → 210, "always taking a small loss on the call to continue to participate on the upside"; yes, even an in-the-money call gets rolled.
- **Synthetic ownership via high-delta calls (Eric):** "absolutely... will work the same way" — buying LEAPS on gold is "one of our core strategies" (Section 7).
- **Do you pick strikes by volume? (Michael):** No. The 42 strike showed ~2,480 open contracts and ~600 traded that day with ~5-cent spreads; in-the-money spreads widen but proportionally similar. "In the end, the market makers are providing ample liquidity. You don't need to go to the specific strike that has the largest volume in order to get a good fill" — you get liquidity across the whole chain or nowhere, unless you are trying to cross with another retail order inside the dealer spread.
- **Collar around a deep-ITM call (Eduardo/Eric):** yes; the synthetic behaves identically to stock (see Section 7).
- **Which expiry for the collar (John):** the tenor of the trade — want a 2–3 month collar, use the 2–3 month options.
- **LEAPS on gold (Michael):** yes, "we do that a lot. That's one of our core strategies." Longer-dated collars are acceptable but demand more active management.
- **How does an ATM put's 50 delta become 90–100? (Michael):** gamma — the delta changes at the rate of gamma as the underlying moves; the pace depends on the option's duration.
- **Hedging CEF (Sprott gold+silver closed-end fund):** put GLD options against it, same proxy logic as Section 4.
- **Companion strategy:** the fat right tail also upgrades the plain **call debit spread** (bull call spread) — see Section 5.

## 4. Hedging Physical Gold (Hedging What Has No Options)

<!-- Source video: HedgingPhysicalGoldAug212020 (1080p with 25fps).transcript.md -->

Ceresna's problem statement, from his August 21, 2020 special webinar: most Big Picture Trading members own gold in forms that **have no options chain** — physical coins or bars in a safe, bank-allocated metal, the Sprott Physical Gold Trust (PHYS), or a home-country ETF bought in a non-US currency (e.g., Canadians buying the iShares gold ETF in Canadian dollars). Yet nearly every hedging technique requires options on the very product you own. This was, he said, "the single most commonly asked question" he receives. Everything below also applies to silver, and all structures are built on **GLD options as the proxy hedge**.

### Step 1 — Decide whether you need a hedge at all

Before any structure, answer two diagnostic questions:

1. **How much gold do you own relative to your net worth?**
2. **Are you leveraged on that gold?**

His thresholds and examples:

- **A few coins in a home safe, bought with cash, a modest allocation (under ~10–20% of net worth): no hedge needed.** "The idea that one would need to hedge some sort of like physical coins... is just not necessary in that circumstance."
- **A Dragon Portfolio context** (Chris Cole's portfolio, with gold ~20% as a core diversifier): hedging the gold allocation is "arguably unnecessary," because the allocation exists for its correlations to the other assets — unless you have a tactical reason to believe there is immediate risk at that moment.
- **Real members own 50%+ of net worth in gold** because they believe the financial system is compromised and gold is the ride-through asset.
- **Other members borrowed to buy gold** — second mortgages, lines of credit. The moment debt is involved, hedging "suddenly becomes far more important."

His bottom line: "I have no problem with members being leveraged up on gold. Just know when you need to be hedged on it." A practical mental exercise: write down every worst-case scenario and its dollar outcome; if any single outcome makes you uncomfortable, that is the trigger to hedge.

### Step 2 — Define exactly which risk you are hedging, and when

The hedge must be matched to a stated scenario. His menu:

- Remove **all** risk of loss.
- Hedge a specific feared drawdown (e.g., gold back to $1,500, a 20–30% drop).
- Ignore the first 10% down, but remove everything beyond it.
- Hedge **only** the first 10% drop, then self-insure below (the rationale: physical bullion has no "goes to zero" equity-style risk, so at some lower price you no longer fear loss).
- **Trend-arbiter hedging:** stay unhedged while gold is above its 50-day moving average; buy the hedge only while it trades below. This is "very much a primitive version of what CTAs do when they're trend following," but it avoids burning perpetual insurance premiums in an uptrend — if gold runs to $2,500, $3,000 or $5,000, it spends most of the cycle above that moving average, and you pay for insurance only during sustained distribution periods.

### The proxy-hedge principle: hedge any gold with GLD

The products in his demonstration account:

| Product | What it is | Position shown | Options? |
|---|---|---|---|
| GLD | US gold ETF, deep liquid options chain | the hedging vehicle | Yes |
| PHYS | Sprott Physical Gold Trust (allocated storage) | 3,300 sh @ $12.10 = $40,000, now $15.33 = $50,000 | No |
| CGL | iShares gold ETF, Toronto Stock Exchange, bought in CAD | 5,000 sh @ C$13.25 = C$66,000, now C$80,000 | No |
| (mentally) | physical coins/bars in a safe | — | No |

Two Canadian nuances he flags: the iShares product with the **"HDG" (hedged)** suffix hedges out the currency, so despite the CAD purchase price it tracks **US-dollar gold performance** almost one-for-one with GLD; **MNT** (Canadian Royal Mint Reserve) is **not** currency-hedged, so it adds a CAD-gold layer on top of the gold price. Overlaying the charts, PHYS and the hedged CGL both track GLD almost perfectly — they are economically the same exposure, so **you buy the insurance on GLD regardless of which wrapper you own**.

On **gold futures** as the hedge instrument: it works, but adds a layer of complexity — contracts expire (his example: October contract's last trading day October 28), the term structure is in **contango** (forward prices above spot), the contract is **100 oz** (your hedge size must fit 100-oz increments), and, for example, "the October options are settling the December futures contract." Verdict: "nine out of 10 of my members should generally stray away from it."

### Why you generally do NOT sell the call leg against non-optionable gold

- Sell 2 GLD calls, one week out, 187 strike, against 200 GLD shares: $200 of income with **zero margin** — the shares collateralize it, so it is a covered call.
- Sell the same GLD calls against PHYS or CGL: the broker cannot see matching shares of the settlement vehicle and treats the calls as **naked**, demanding margin (his example: **$10,145**). You are economically covered — "if you sell the right amount of calls against the right amount of physical you have, you're still covered" — but you do not own the deliverable shares, so the margin stands. This is why hedgers of non-optionable gold generally **buy** insurance rather than financing it with short calls.
- **Call credit spreads** against the physical are possible but unattractive because of the right-tail skew: an October 200-by-220 call spread collects about $1.77 (with the 220 wing costing $0.50); a 210 short strike collects about $0.90. You are working for $1.00–$1.50 of credit while carrying $10–$20 of spread margin, and the far strikes are bid at 28–31 implied while the 190s/200s sit at 23–24. It is "an income strategy... that isn't a hedging strategy" — it caps upside and removes no downside.

### Structure 1 — OTM put tail insurance: remove all risk beyond the first 10%

*Scenario: "I'll take a 10% pullback; remove everything worse."*

- **Legs:** buy roughly 90-day GLD puts struck about 10% below spot. With GLD at $182, the November 165 put costs about **$2.10 — just over 1% of position value for three months**.
- Optional cost trim: make it a **165/150 put debit spread**, cutting the cost from $2.10 to about $1.50.
- **Sizing (the CGL example):** C$80,000 ≈ US$60,000 at an exchange rate near 1.30. Each GLD option covers 100 shares ≈ $18,000 of exposure, so the C$80K position is a ~325-GLD-share equivalent → **buy 3 GLD puts** (about $626 total). Over-hedge with 4, under-hedge with 2. The $50K PHYS position also sizes to about 3 puts (slightly over-insured). Expect small settlement/currency drift between the CAD wrapper and the USD hedge.
- **Simulator walk-through** (300 GLD shares = $54,000): at 165 the bullion is down ~$5,000 and the insurance is roughly flat (the first 10% is your deductible). In a crash to 140, the bullion is down ~$12,000 while the puts are up ~$7,000 — "you said, I'll take the first $5,000 or first 10% risk. But after that, the insurance policy essentially removes all the risk of further loss."

### Structure 2 — One-year "forget you own it" insurance

Same tail-risk design, 392 days out (September 2021 expiry, 165 strike): about **$8 per share, roughly 4.4% of position value for the year**. "That's not necessarily cheap... but for that cost, you essentially can remove all risk of loss and just walk away and not even worry about it."

### Structure 3 — Put debit spread: hedge only the first 10%, self-insure below

*Scenario: "Gold went too far too quickly; I want to lock in profits through a pullback but accept the deeper downside" — rational because bullion has no equity-style wipe-out risk, so "at some stage becomes a downwards boundary where you no longer fear the risk of loss."*

- **Legs:** buy the at-the-money 182 put (~$6.25) and sell the 165 put (~$0.95) → net ≈ **$5.30, roughly $500 per combination; three combinations ≈ $1,500**.
- At expiry at 165: the spread is worth $17.00 — the hedge earns ~$3,500 while the bullion is down $5,000.
- For a **dollar-for-dollar** hedge, match delta: step up to a **4-by-4** (four spreads against 300 shares-equivalent) → at 165 the spread gains ~$5,000 against the ~$5,000 bullion loss.
- Strike-selection rule (from Q&A): **work backwards** — pick the strikes from the scenario you want removed, not from the chain.

### Structure 4 — The put backspread: near-zero-carry crash insurance (advanced)

His preferred advanced tool is "trailing a backspread put hedge on the GLD... it's essentially a zero cost and it removes a left tail risk of a spectacular crash in gold. And so long as gold goes higher, a backspread will cost you nothing."

- **Legs (his example, 1,000 GLD shares ≈ $182,000):** sell 10 at-the-money 182 puts, buy 20 out-of-the-money 170 puts — the same shape as the backspreads he runs on stocks like Apple (Part I, Dragon overlays).
- **Carry:** near zero net cost; the only margin is the 170-to-182 spread width, carried as though it were a credit spread.
- **If gold rallies to 210:** you lose nothing on the insurance while the bullion runs.
- **The risk zone is the middle:** e.g., 47 days before the December expiry with GLD near 170 — down ~$12,000 on the bullion plus roughly $2,000 to exit the backspread. That mid-range pinch is the trade's point of maximum loss.
- **In a crash to 140:** down ~$40,000 on the gold, but the backspread makes ~**$20,000**.
- **Sizing rule (from Q&A):** size the short options equal to the position; buy **double** the further-OTM longs. For a non-optionable holding (a member's 1,200 shares of PHYS), first dollar-match to the GLD-share equivalent, then apply the same 1x-short / 2x-long structure.

### Loading gamma instead of delta (the vault owner's refinement)

For someone with, say, 150 oz in a vault asking how to buy cheaper tail risk and "load up on it": compare 10 at-the-money 182 puts versus 20 out-of-the-money 170 puts. The ATM package behaves like an **$86,000 synthetic short**; the 20 OTM puts behave like a **$99,000 synthetic short** — nearly the same starting delta for twice the contracts. The OTM package is **buying gamma**: once gold falls to 170, it hedges a $160,000 synthetic short versus only $116,000 for the ATM package. Same starting protection, accelerating protection in a crash, lower upfront cost — but he reserves this for his "more sophisticated members."

### Hedging Q&A — captured in full

- **Taxes (Robert):** profits earned on the hedge sit in a trading account and are taxable — you must account for hedge gains at tax time even though the physical position may be unrealized.
- **Backspread sizing (Scott):** short options = position size; longs = double, further out of the money; size identically when proxy-hedging PHYS/CGL.
- **Selling call credit spreads against physical gold (MT):** it is an income strategy, not a hedge — the fat right tail means bad risk-reward on the short calls, it caps your upside, and it "hasn't removed any of the downside risk."
- **Choosing put strikes (Kyle):** decide what you want hedged first (e.g., "the first 10% down"), then the out-of-the-money strike is 10% below spot — "you have to work backwards."
- **Quote discrepancies (Lynn):** Yahoo Finance versus Vanguard quotes checked against Interactive Brokers — in line, just delayed data.
- **Hedging synthetic positions (Michael):** step back — "things don't always need to be hedged." With a healthy portfolio allocation, no hedge is needed; tactically hedge only when you own too much, have big profits to protect, and don't want to sell.
- **Cheaper loaded tail risk (Gary):** the delta/gamma comparison above (10 ATM vs 20 OTM) is the technique; "it's a puzzle you're trying to solve of what risk do you think is really there and what's the best way for you to remove that risk at the lowest possible cost."
- **PHYS sizing (Esteban, 1,200 shares):** divide position value by the GLD share price to get the GLD-share equivalent, then size the structure (for a backspread: shorts matched to that equivalent, longs doubled further OTM).

## 5. Leveraging the Upside: Skew Debit Spreads and the 2:1 Ratio

<!-- Sources: Asymmetric strategies to Repair and Leverage Your Gold Holdings (w/ George Gammon); TradingGoldCollarsAug172020 -->

### Long-dated far-OTM bull-call spreads (the "digital" insurance trade)

Thesis example: it is "entirely within the realm of reason" that, under the right monetary circumstances, silver doubles (SLV from ~$22–23 to $40–45). The skew lets you buy that scenario for pocket change:

- **Structure 1 (30×40):** Buy January 2023 (≈450 days) SLV **30 call** for **$1.50**; sell the **40 call** for **$0.80**. Net **$0.70** ($70/contract) for **$10 of upside** — better than a 10:1 payoff, with a hard floor: you cannot lose more than $0.70.
- **Structure 2 (30×50):** Same 30 call, sell the **50 call** for ~**$0.50–0.55**. Net ~**$1.00** for **$20 of upside** — a ~20:1 payoff. Demonstrated with 10 contracts: $1,500 paid, $500 collected, **$1,000 at risk**. If silver reaches $45 within ~300 days, the position is worth ~**$15,000** (delta dollars grow from ~$7,600 synthetic-long to ~$60,000).

Why the market pays this: at a *flat* 36 vol the 50-strike silver call would price ~**$0.11**; the live market pays ~**$0.50** because of the right-tail skew. On the S&P the same spread "wouldn't even be a nickel." Institutions build these as OTC **digital options** ("put up a dollar, it can pay 20"); retail replicates them with long-dated debit spreads. Going out further is possible: a 30×40 into 2024 (**816 days**) cost $2.80 against $1.60 — about **$1.00 for a $10 payoff** — with the caveat of wider markets and more patient fills.

**How to think about it:** if you own gold as *portfolio insurance* against inflation/dollar collapse, a far-OTM spread is a second-order insurance policy on the insurance. The car-insurance analogy: you pay $1,000; if nothing happens, it expires "no different than your car insurance expires because you didn't crash your car"; if gold doubles because the scenario hit, it pays 10–20× "in a huge way." Position it against the Bloomberg-style $3,000-gold theses. If gold's rise proves *slow and orderly* instead, these expire worthless — they are crisis instruments, not core exposure.

**The bull-call spread on miners** (from the collar webinar — the same skew upgrades the plain debit spread, which on normal stocks rarely pays enough on the short call):

- **Legs:** buy the October 44 GDX call for $2.75, sell the October 48 call for $1.50 → **$1.25 net for a $4-wide spread**; break-even 45.25; **risk $1.25, reward $2.75**.
- Why it works: "you're getting a much higher volatility premium on the out-of-the-money calls, and you're paying a smaller volatility premium for the at-the-money ones."
- Simulator run (GDX $42.50, ~50% vol): if miners crash to $30–33, the share owner loses $1,000 per 100 shares ($10,000 per 1,000), while the spread's loss is **capped at the ~$1,200 outlay** — and that $1,200 was replicating roughly **$50,000 of GDX exposure**. If GDX reaches 50 near expiry, the spread pays ~**$2,700**. Beginners see "200% return on risk"; his framing: the point is small-capital-outlay participation in a large notional position, not percentage-chasing.
- **Why not a backspread instead? (Les's question):** counterintuitively, backspreads are favorable when out-of-the-money calls are *cheap*; with gold's fat right tail the OTM calls are expensive, so "outright debit spreads actually have better payoff profiles in these circumstances."
- Calendars can enhance the structure (Sal's question), but that is advanced material beyond the session.

### The 2:1 call/put ratio: stock replacement with double upside (Newmont)

The leveraged-upside workhorse, demonstrated as live trades on **Equinox Gold and Newmont Mining**. Newmont context: it had just rallied ~$21 (**+40%**) in ~80 days on the prior leg, then declined ~30% over ~150 days — versus an average miner drawdown of ~**42%** — so downside was judged "marginal" while the analog projected a possible repeat toward the mid-70s. The trade at Newmont ≈ **$58**, January expiry (~90 days):

| Leg | Structure | Detail |
|---|---|---|
| Downside | Sell 10 Jan **60 puts** @ **$4.10** | Income ≈ **$4,100** |
| Upside | Buy 20 Jan **60 calls** @ **$2.22** | Cost ≈ **$4,500** |
| Net | Small debit | Live ≈ **$300–400**; the 10 puts carry ≈ **$21,000** of margin — roughly the same outlay as the margined stock buyer |

Outcome comparison at January expiry, versus owning 1,000 shares at $58.35:

| Scenario | Stock owner | 2:1 ratio | Reading |
|---|---|---|---|
| Flat at $58.35 | $0 | ≈ **−$2,000** | Obligation struck at 60 → break-even $60 vs 58.35 |
| Crash to $45 | **−$13,000** | **−$15,000** | Same dollar-for-dollar downside, just ~$2,000 worse (strike gap) |
| Rally to $75 | **+$16,000** | **+$30,000** | Controls 2,000 shares above 60 — **double the profit** |

The design principle in Ceresna's words: "give me the downside risk as though I was the owner of the stock, but give me the upside potential that I'm twice as leveraged... two shares upside potential for one share downside risk." The live version, opened for **under $1,000**, carried **~$104,000 of delta dollars** — synthetic long Newmont. Note this is explicitly a **stock-replacement strategy with stock-market-style risk**: the short puts are a genuine obligation to own the shares at 60, so it belongs in a different risk class from the debit spreads above. Time-decay economics are what make it viable — the put income offsets the decay on twice as many calls, so the position carries at near-zero cost and the only real exposure is the $60 pivot.

### Sizing is the risk control

From Gammon: if a $15,000 drawdown breaches your risk profile, **do not open 10** — "if you can tolerate a $1,500 drawdown, then do only two contracts long with one contract short." Size the ratio to your tolerance; the structure is scalable proportionally.

## 6. Repairing Underwater Gold Positions

<!-- Sources: Asymmetric strategies to Repair and Leverage Your Gold Holdings (w/ George Gammon) -->

### Repair or cut? The decision rule

Cutting an outright loss is justified in only two cases: (1) it was an **active/technical trade** — a chart-pattern trade that simply failed; or (2) the **fundamentals have soured** on the company. But if you bought a good company early and it is merely cheaper — "Wheaton at $37 was just as good a stock as it was at $45" — repairing is the no-brainer. "We never say we're wrong in trading; we always just say we're early" — the repair strategies are how "early" gets converted back to profitable without new capital.

### Repair style 1: the put-financed call (Wheaton Precious Metals)

The war story: Ceresna bought **2,000 shares of Wheaton Precious Metals at ~$45 (~$90,000)** three to four months before the webinar, expecting the miner turn. Within two weeks the stock "wiped out from 45 bucks down to almost 35" — a ~20% drawdown to the prior low. Plain dollar-cost averaging would have required **$70–80,000 of new cash** to add 2,000 shares. Instead:

- **Bought the November 19-expiry $37 calls** — a contract guaranteeing the right to buy an additional 2,000 shares at $37. This is "dollar-cost averaging" with a defined, financed commitment instead of a cash outlay today.
- **Financed the calls by selling $35 puts** — "either I'm going to buy the shares at $35, or the $37 call gives me all of the upside."

Result at the time of the webinar: still **−$5,600 on the stock**, but **+$8,000+ on the repair** — the combined position already net profitable even though the original entry was months early and badly underwater. That is the whole objective: "to find some way of getting back to being profitable... even if you were early."

### Repair style 2: covered call + bull-call spread (Agnico Eagle)

The traditional template, built live for an attendee ("Art") holding 1,000 shares of Agnico at an **$80** average cost, trading ~**$58–60** (−$21,000). Expiry choice matters: a near-dated chain has no premium at the strikes you need, so a $5–7 dip can be repaired with the front month, but a deep hole like this requires **February+ expiries** where the skew pays. Agnico's ATM IV was 32–33% with the right tail out to ~50%.

| Leg | Structure | Cash |
|---|---|---|
| Keep 1,000 shares (basis $80) | — | — |
| Sell 10 Feb **75 calls** (covered) | income | **+$500** |
| Buy 10 Feb **65 calls** | debit | **−$2,000** |
| Sell 10 Feb **75 calls** (spread leg, against the longs) | income | **+$500** |
| **Net outlay** | | **−$1,000** |

Outcome at February expiry versus doing nothing (need +$20,000 to break even):

- **Rally to $75:** stock-only is still **−$5,000** (needs another $5). The repair is already at break-even (~+$20,000 recovered; ~+$26,000 measured in the simulator including option P&L) — roughly **$10,000 better**, and break-even arrives ~$10/share sooner.
- **Unchanged at $58:** repair loses exactly its cost, **−$1,000**.
- **Back to the lows at $50:** stock-only −$8,000; repair −$9,000 — the same loss plus the repair's cost.

So the shape is: risk **$1,000** to recover **$10,000 faster**, with the worst case capped at the repair's cost. Two coverage notes: 10 short calls are collateralized by the shares and 10 by the long calls — **nothing is naked** in any scenario. And it works *because* of the gold-miner skew: "in the traditional equity markets, because the right-tail skew is downward-sloping, these repair trades are very hard to do."

### Active management of a repair: rolls, assignment, and the exit question

- **If the stock approaches the short strike too fast:** "the curse I wish upon all of you." Roll the covered calls **up** (75 → 80) or **out and up** — the demonstrated **diagonal roll** replaced February 75s with May 80s at a **net credit of ~$0.25**, reopening upside on the 1,000 shares. Master's-program students are taught a full toolkit of these adjusting trades.
- **If your goal is to exit the position entirely:** do nothing and let assignment across the line at 75 blow you out at a **$5,000–10,000 profit** (versus the starting −$20,000).
- **If you want to keep the shares long-term:** you must actively close the 10 *covered* calls before assignment; the 10 spread calls settle against the long calls on their own, and you keep most of the repair's benefit.
- Beginners' note on the parallel GLD collar (from the Q&A): if expiry lands between the strikes, both legs expire and the shares remain at their original basis; trouble above the short strike is handled with the roll-up of Section 3.

## 7. Asymmetry as a System: Gamma, the Three Investors, and Repositioning

<!-- Sources: How to Find Asymmetry on Your Favourite Commodity Stocks (Using Options the Right Way); Using Options to trade Commodity Cycles; GOLD CYCLE - April 16 2021 LIVE Webinar; Asymmetric strategies to Repair and Leverage Your Gold Holdings -->

### Delta, gamma, and why option losses decelerate

A stock is a **delta-one** instrument: the payoff graph is a 45-degree line, a dollar up / dollar down. A long call's graph flattens as the stock falls below the strike and steepens to the same 45-degree line as it rises deep in the money:

- **The more you are right, the more the option behaves like the stock** — delta climbs from its starting value toward 1.0, and in a big rally the option participates nearly dollar-for-dollar.
- **The more you are wrong (or early), the slower you lose** — delta decays toward 0, so each further dollar down costs less than the last. The Q&A phrasing: slippage on the way down happens **"at the rate of delta."**

This is **buying gamma**. It "sounds too good to be true — it would be, if it was free. For this privilege, we pay a premium": the **theta** carry. Long-dated options (LEAPS, 1–2 years) have slower theta, so they "behave much more like the underlying security" than short-dated options — which is why this system is built on them. Big Picture Trading has been rolling long-dated GDX calls since 2017–18 as core positions, using them to hold the miner theme "without any of the short-term market-timing problems that short-term traders have." His risk-philosophy line, worth quoting: "I don't consider options to be risky. I consider leverage to be risky. It just so happens that options can create a ridiculous amount of leverage."

### Implied volatility vs. measured cycles: the mispricing argument

Set the implied one-standard-deviation cone against the measured cycle statistics (Section 8):

- **XOP** (energy ETF) at $22.23, IV **31.2%** → implied one-year range **$15–$29**. But XOP's average cycle gain is **+81%** — from the ~$20 low, an average rally reaches **~$36** (which also sits at the 61.8% Fibonacci retracement of the whole decline), and historical rallies of +100–200% occurred. Upside cone too small → **calls arguably mispriced cheap relative to realized cycles**.
- **GDX** at $18, IV **27.7%** → implied range **$13–$23**, versus average cycles of roughly **−45% / +89%**. Historical proof-of-concept: the January $18 call bought near the September 2018 low went from **$2.55 to $12.50** at the peak of the 12-month, +80% rally.

The honest caveat from Ceresna: these were measured from exact high to exact low; nobody catches either end; the exercise builds perspective, not a market-timing signal.

### The three investors: A (stock), B (conservative options), C (leveraged options)

The core teaching device, run twice (and reprised nearly verbatim in the April 2021 gold-cycle webinar, Section 8):

**Run 1 (from the asymmetry bootcamp).** $20,000 account, GDX at $18.15, January 2021 $18 call at **$2.55** (~14% of underlying, 492 days). A: buys 1,000 shares ($18,150), rest in cash. B: buys **10 calls** ($2,550) — the same 1,000-share control — parks **$17,450** in a money-market fund; at any moment he can exercise into 1,000 shares at $18. C: buys **15 calls** ($3,825), parks $16,175; controls 1,500 shares without margin.

- **Up ~90% to $35:** A +$16,150. B ends "not much different" — slower out of the gate (starting delta ~0.5–0.6) and nine months of theta, but by the top the calls behave like stock; B captures the majority of A's profit on $2,550 of capital at risk. C makes **~$22,000** — leverage rewarded when right.
- **Unchanged:** A ~flat (GDX pays ~$0.20/year in distributions). B and C burn theta, partially offset by ~2% money-market interest on the cash. "There should be no confusion: we pay premium for the asymmetry."
- **Down to $10** (−45%): A is −$8,000 (account down to $11,850) and needs a ~**100% rally** just to break even; to average down he must find **new money** (~$10,000) or margin. B and C lose only the premium — options near zero — but still hold **$16,000–17,450 of cash**.

**Run 2 (from the cycles webinar; identical in the April 2021 webinar's reprise).** $30,000 account, GDX at $28.35, January 2021 $29 call at **$3.10** (~10% of underlying, 363 days, 28% implied). A: 1,000 shares + $1,650 cash (~$28,350 outlay). B: 10 calls ($3,100), ~$26,900 cash. C (Luke): 15 calls ($4,650), ~$25,000–25,350 cash, controls **~$43,000–43,500** — the option route to being 1.5x long without a margin loan.

- **Up 94% to $55:** A grins all the way (delta one) — ~$26,000. B starts slower — "I'm fighting the premium" (up only $2,900 on the first leg) — but from $45 to $55 "participated for almost a full $10 rise" and finished with the majority of A's profit: **~$23,000 on a $3,100 risk unit**. C: **+$34,000–35,000, over 100% on the account**.
- **Flat:** theta burn; option may expire worthless; A loses only opportunity cost.
- **Down 47% to $15:** A **−$13,000**, account nearly halved — "that knot in your stomach" every resource investor knows (his example: anyone holding U.S. Steel through its two-month, $14.50→$8.50, −40% slide). B's loss is **defined at $3,000** no matter how far GDX falls; C's at ~$4,650 — and B's loss is smaller than A's *at every price level* on the way down. "Even though Investor C made more money on the upside than Investor A, they also lost less money than Investor A when wrong."

The general lesson: A, B, and C make comparable money when right; B and C lose a fraction when wrong — and, crucially, retain the cash to act.

### Repositioning: dollar-cost averaging without new money

This is the second, tactical layer of asymmetry, "beyond the delta." Because the option buyer's cash sits in a money-market fund while the option's delta decays to zero, being "spectacularly early" leaves the full dry powder intact at the true bottom:

- **Answering the "aren't you leveraging into something that's not working?" objection:** no — with the calls zeroed, the position sits at **delta zero**; re-entering restores the *original intended exposure*, it does not add leverage on top of a losing position (C's re-entry restores his 1.5x target rather than exceeding it). Do not confuse re-entry with doubling down: holding losers *and* adding new positions is **pyramiding** — a different strategy for different capital.
- **The XOP walkthrough** ($22,000 account; January 2021 $22 call at **$3.05**, ~34–35% vol, 399 days; starting delta **0.57**, delta dollars $12,500 vs the stock investor's $21,900): up to $35 after ~300 days → stock +$13,000, calls +$10,130 with delta ~1.0 (the $3,000 premium is the whole difference); flat → **$1,500** of theta; down to $13 → stock **−$9,000**, calls −$3,000 with $19,000 intact. The call buyer then buys ~1,500 shares-equivalent of **$13-strike** calls with money already on hand. When the average +80% recovery carries XOP back toward $22, the repositioned investor is whole — while the share buyer who "averaged down" with new cash or margin is still −$9,000.
- **The live Occidental Petroleum (OXY) example:** bought the $50 LEAP after a drop, calling a bottom. Wrong/early. Alert 1: close the 50s, reopen at $45. Alert 2: close the 45s, buy the $40s. Each roll cost about $2-and-change per leg versus the stock owner's $5 — total ~$4+ lost versus $10 — with no new capital, and the position now holds "a guaranteed purchase price of Occidental at 40" with all the upside above it.
- **Why one year of time, not two:** the average commodity cycle resolves in under a year (Section 8), so "within a year I'm either going to be spectacularly right or spectacularly wrong" and will be repositioning anyway; paying for the extra year (the January 2022 $22 XOP call was $4.40 vs $3.05) is usually wasted premium. If six months pass with no resolution, **roll forward** — closing one option and opening the next — and note the rule: **always add time on a roll**, because a fresh positioning at the bottom needs ~9+ months of runway for the average up-cycle. (Holding the old calls *while* adding new ones is **pyramiding** — viable only with excess capital and total conviction in the boom-bust. A Q&A note: "a roll is always close-then-open"; do not keep the old strike *and* buy the new one.)
- **The GDX repositioning math (run 2):** at $15, B's $27,000 buys ~**1,800 shares-equivalent** (18 calls at the $15 strike) versus his original 10; C's $25,350 at his standing 150% leverage target buys **25 contracts** (~$37,500 control) versus his original 15. Both now have "all the upside from $15" — having lost only their original premium — "without experiencing a 50% wipeout" and without the emotional drag of feeding fresh money into a painful position. When the average +100% recovery comes, each account is worth $40–50,000 *despite having been a year early and dead wrong first*. Ceresna contrasts this with serial dollar-cost averaging in commodities (Section 8.5).

**The COVID roll — repositioning in practice** (April 2021 webinar). In early 2020 they were long these same GDX LEAPS at **$28 strikes**. The coronavirus crash took GDX down to **$16**. What they did: "we rolled down and repositioned all of our GDX LEAPS and our silver LEAPS," so the fund captured the entire recovery off the low — the convexity having capped the loss on the way down and the retained cash having funded the re-entry. "You can try to manage [the cycles] just by trading delta-one positions using technical analysis, or you could take advantage of the convexity of the option itself." Hence his maxim: **"You don't have to catch the cycle. It's all about repositioning on the cycle."**

**The live trade: January 2023 LEAPS as a stock replacement** (April 2021 webinar). That week they had re-adjusted the published cycle trades out to **January 2023 LEAPS**:

- **Position: GDX January 2023 $34 strike call, published at $6.40** (GDX near $36, implieds ~32%, 644 days to expiry). The same adjustment was made to the **silver** trade and to **Kirkland Lake**.
- **Why 2023 and not 2022 (with nine months still left)?** Because the option is used as a **stock replacement** for a full cycle, not a timing instrument. If the bottom is a muddle-through — perhaps an inverted head-and-shoulders, with the bull really starting June/July — a 2022 option would enter the new cycle with only six months of life, and by the *next* routine correction (September/October) would be down to about three months: "we're messing around with trying to time a bigger cycle... while we're trying to manage a short-term option... I don't think it's worth all of that stress." Owning 2023 gives a year and a half plus of time and removes the expiry-timing problem entirely.
- **Simulator comparison** (GDX $36, 32% vol; Investor A: 1,000 shares = $36,000; Investor B: 15 at-the-money $36 calls = $9,000 outlay, each holding ~$40K):
  - **Carry cost:** 290 days forward, stock and vol unchanged → **$1.55/share of decay, ≈ −$2,300** on the LEAPS.
  - **Wrong by a full down-cycle (GDX −40%+ to $21):** stock −$15,000; **LEAPS only −$8,800** — the leveraged investor loses far less than the unleveraged shareholder, and still has the cash to reposition (as in the COVID roll).
  - **Right by a full up-cycle (GDX to $65):** stock +$29,000; **LEAPS +$35,000**.
  - Summary asymmetry: "we lose less when we're wrong and have all of this cash to reposition... when we're right, we're going to make more money. And I love that. That's my favorite way to trade."

**The Freeport-McMoRan war story.** The delta-path lesson he "literally just closed": after the coronavirus crash, with Freeport-McMoRan down at **$8 a share (April–May 2020)**, they went long the **$8-strike LEAP for $2.54** and closed it at **$30 — "over a thousand percent return on this LEAP," which he calls "the best trade we ever had at Big Picture Trading."** In the tracker, the LEAP's **delta-dollar** column matched the stock exactly — "the more right we are, the more the option actually behaves like the stock. And yet, if we were dead wrong about that position, that risk was very specific and limited." (He is careful to add he is *not* forecasting a 1,000% move in the GDX — the position is the illustration of the structure, not the magnitude.)

### The zero-cost synthetic long (Yamana Gold, Fluor)

A structure that converts the skew into a free option on direction. Yamana Gold at **$3.73**, IV ~50%:

| Leg | Structure | Cash |
|---|---|---|
| Buy 100 Jan-2021 **$4 calls** @ **$0.67** | upside on 10,000 shares | −$6,700 |
| Sell 200 Jan-2021 **$3 puts** @ **$0.34** | obligation on 20,000 shares | +$6,800 |
| **Net** | | **≈ $0** |

Outcomes: above $4 — **100% of the upside on 10,000 shares-equivalent** (the stock investor's $37,000 of exposure); below $3 — **put 20,000 shares at $3** (a deep-value scale-in at a level chosen in advance); between $3 and $4 — both legs expire and the trade cost nothing. "Either I get stuck owning 20,000 shares at three, or I have all the upside above four" — a "synthetic dollar-cost average" with zero carry. Variations: sell a *lower-strike* put (the $2.50 strike at ~$0.17 premium) if you prefer a cheaper obligation level and an actual net debit instead of zero cost. The same shape was the live position in **Fluor (FLR)**: all the upside above **20**, or put the stock at **12.50** — a level justified by breakup value ("an absolute no-brainer"). The iron rule: **never do this on a stock you are not willing to own, and not at prices you are not willing to own it at.**

### Junior miners have no options — the stock *is* the option

Options are listed mainly on ETFs and large-cap miners. For the speculative juniors (the example discussed: Newfoundland Discovery Corp — "essentially penny stocks"), Ceresna's framing: these stocks are **already options** — the floor is zero, and being right means 10-to-20-baggers (50 cents to $10). So treat every speculative junior *as* an option position: sized so it can go to zero, because any of them can — "if they end up scoring, it could be a 20-bagger." Do not try to hedge or leverage them with options; they do not have any, rightfully so.

## 8. The Commodity and Gold Cycle Model

<!-- Sources: Using Options to trade Commodity Cycles; How to Find Asymmetry on Your Favourite Commodity Stocks; GOLD CYCLE - April 16 2021 LIVE Webinar -->

### The cycle database: definition and measured statistics

Ceresna hand-measured (spreadsheet, "old school"; a scanning tool may be built for members later) every boom-bust cycle on a panel of resource names. **Cycle definition, exactly two criteria:** the move must be **greater than 20%**, and it must last **more than two months** — 20% "has been universally accepted as being the arbiter of a bull and bear market," and the length filter removes one-day liquidity events and flash crashes so only sustained trends count. He describes the counting as working like a parabolic SAR. Trough-to-peak is a bull cycle; peak-to-trough is a bear cycle; measurements run exact high to exact low, which is why the averages are upper bounds on what a human can capture.

The wider panel (measured at the commodity-cycles webinar):

| Instrument | Data since | Cycles | Avg advance | Avg decline | Extremes |
|---|---|---|---|---|---|
| **Teck Resources** (TECK) | 1997 | 17 | ~9 months, **+242%** (~+150% excl. outliers) | ~7.5 months, **−50%** | 7 advances ≥ +100%, 3 ≥ +750%; 6 declines > −50%, twice ≈ **−90%** |
| **Cameco** (uranium) | 1995 | 15 | ~10 months, **+151%** | ~9 months, **−45/46%** | high-quality, low-cost Western producer |
| **Encana** (incl. the move to the U.S. / rename to Ovintiv) | — | 13 | ~8 months, **+114%** | ~6 months, ~**−50%** | — |
| **Schlumberger** (Halliburton similar) | 1981 | 27 | ~10 months, **+80%** | ~7 months, **−36%** | longest sample |
| **XOP** (SPDR oil & gas E&P ETF) | 2006 | 10 | ~10 months, **+81%** | ~6 months, **−41%** | −69% in 5 months (2008); ~−60–65% in ~8 months (2015–16) |
| **GDX** (gold miners) | 2006 | 8 | ~9.6 months, **+89%** | ~9.5 months, ~**−45%** | last two cycles longer and shallower (−32%, then +80% in 12 months) |

**The April 2021 gold-cycle webinar's GDX run** measured **nine cycles** since GDX's 2006 creation (the count and averages differ slightly from the earlier session's table — different measurement runs, both presented as-is): average advance ~**11 months / +99%**; average pullback ~**8.8 months / −42%**, with three selloffs worse than **−50%**. His explicit caveat: "This is not my forecast that we buy exactly at the bottom and sell exactly at the top... This is simply looking at peak-to-trough and trough-to-peak measurement of each cycle."

**The pattern that drives the whole method: average cycle length is under a year in both directions** — declines roughly 6–9 months, advances roughly 8–11 months — "it doesn't matter whether we were talking uranium, energy, gold miners." That is precisely why **one-to-two-year LEAPS fit**: one option can span a full down-cycle *and* the up-cycle that follows. And the reason the swings exist at all is the resource paradox: at the commodity peak, earnings look best and the stocks look cheapest on P/E — right before mean reversion crushes earnings; at the trough, earnings are zero or negative and the stocks look "expensive" — right before they are "stupidly cheap." Hence the truism Ceresna loves: **"a bear market is the author of a bull market, and a bull market is the author of a bear market"** — nowhere more evident than in commodities, whose boom-bust amplitude you otherwise only see in semiconductors. Demand itself never disappears: "we need commodities in the world... unless you're trading buggy whips."

### Reading where you are in the cycle

- **Late-stage decline (the entry zone for LEAPS).** Signals used at the time: XOP **8 months into a −40%** decline (vs. a 6-month/−41% average) → "late stages of finishing the downward cycle," with the honest caveat that 2008 and 2015–16 both produced −60%+ legs, so a further washout to ~$13 (−60% from the $20 low) must be survivable — which is exactly what the option structure buys. GDX: 13–14 months down ~37% vs. the 9-month/~40% norm. Technically: **declining wedges / bottoming formations**, **completed measured moves** (the prior decline's length projected forward — U.S. Steel's drop had reached its completed measured move, with overshoot risk to $8), double-bottom retests at prior lows.
- **Early recovery:** the average rally is 8–11 months; targets extend from the measured move (XOP to ~$36; GDX to ~$60; gold's upside targets then **$1,700–1,750**; a natural-gas breakout leaving "room for $7.50"; silver's retest of its prior high with the trade already in the profit-taking zone).
- **Correlation watch:** through the period, short-term lows in the euro / tops in the dollar and bonds lined up with short-term swing highs in gold — worth tracking for exits.

### Which structure for which part of the cycle

- **At a late-stage decline (timing uncertain):** long-dated ATM/slightly-ITM calls (or call spreads), sized to the "conservative" A/B model — exposure equal to the shares you would actually buy, ~10–15% premium, remainder in cash. The structure exists to survive one more leg down; the repositioning playbook (Section 7) handles that leg if it comes.
- **If the timing call was early:** roll down (to the discovered tactical low) and **always roll out in time** — you want 9+ months of runway left when the new up-cycle starts, because "we don't want to be day-trading these options... you want to be long that option and just ride it." Check the position every couple of weeks; this is a months-scale method, not screen-watching.
- **At the up-cycle:** the gamma does the work — delta accelerates toward 1.0 and the option pays like stock. Profit-taking discipline is the mirror of entry: "if we're up 100% over the course of a half a year to a year — that's a great time to be massively taking profits and reducing position sizes." Conversely, the **worst time to bail** on a long-term miner holding is mid-decline, at the cycle's floor.
- **When upside runs into your short strikes (collars/spreads):** the roll-up/diagonal-roll toolkit of Sections 3 and 6.
- **Leverage, if at all, through structures rather than margin:** Investor C's extra contracts come with the same defined worst case — the loss is capped at premium even at 1.5x target exposure.
- **Strike-ladder note:** large resource names (e.g., Exxon) trade in $5 strike increments, which gives natural **action points** for adjusting trades as the cycle moves.

### The April 2021 gold-cycle webinar: macro drivers, sentiment, and the timing call

Delivered Friday, April 16, 2021 — "the best buying opportunity we've seen in years" — the same quantitative cycle presentation he had given at the San Francisco Silver and Gold Summit, the Vancouver VRIC conference, and the Orlando Money Show.

**Macro driver 1: real yields and financial repression.**

- **Definitions:** nominal yields embed inflation and inflation expectations; **real yields** are the return on capital net of inflation. The best tracker of 10-year real yields is the yield on **TIPS** (Treasury Inflation-Protected Securities) — "charting the yields on TIPS is the chart of real yields" — retrievable from **FRED** (the St. Louis Fed database). Note his chart plots the *inverted* TIPS yield, so a falling line is rising real yields.
- The **gold–real-yield inverse correlation** is "very distinct" and long-standing — every macro guest on MacroVoices or Market Huddle points to it. The analytical task is placing the present moment on that chart.
- Where things stood in April 2021: real yields had upticked from lows **below −1%** and were "gravitating toward **minus half a percent**."
- The house theme: **financial repression** — "to right-size the debt within the system, one of the easiest ways to correct indebtedness is simply to inflate it away, and one of the ways to do so is to run negative real interest rates for sustained periods of time," whether via explicit **yield curve control** or simply the Fed "pinning the front of the curve."

**The 1978–1980 lesson: rising nominal rates do not kill gold.** Looking at nominal yields back to 1978–1980: gold and 10-year yields **rose together** through gold's great run. The bond market "got its face ripped off," yet gold rallied — because **inflation was running hotter than interest rates could keep up with**, keeping real yields repressed and negative. Lesson: do not assume that rising/weak bonds mechanically mean weak gold; the variable that matters is the real yield, not the nominal one.

**What would actually be bearish: the hawkish Fed.** The genuinely bearish scenario is a Fed that **normalizes policy and lifts the front end**. He jests about Powell being replaced and "Peter Schiff put in as Fed governor," but the point stands: a big hawk tightening policy is the most bearish case for gold. The base case he trades on: the **eurodollar market was pricing no Fed move for a couple of years** — front-end rates near zero "for the foreseeable future" (the view of guests like Jeffrey Snyder). The more dovish the Fed and the less responsive to hot inflation prints, the more gold is "the net benefactor." His call on the April 2021 real-yield uptick: "I do not believe real yields are going to go positive. I'm a seller on that idea. And therefore, this entire short-term rise in real yields, I think is simply presented one of the most compelling buying opportunities that we have seen in a while."

**Macro driver 2: cheap option volatility.** On the December 2021 gold futures contract, charting the **constant 50-delta implied volatility of calls**: implieds had fallen **back to pre-COVID levels**. That matters for expression — "we want to always try to ideally buy options at a period where volatilities are on the lower end of the spectrum; you don't want to get crushed by a vega implosion." Low implieds made option-based cycle trades cheap to initiate.

**Where the cycle stood in April 2021 — timing and price targets.** The current cycle peaked at **$45-and-change in August 2020**; as of the webinar the GDX was **210 days** into a correction of about **−33%** — so far a little shorter and shallower than the average. If this were an average-length, average-depth correction, the trough would land **in the $26–$30 zone around July**. Can another leg lower be ruled out? No — a rejection off $36 into one more measured leg down "would not be out of the character of the cycle." The point of the model is not precision: 7+ months off the highs and a correction "more than sufficient" versus prior bull-market pullbacks puts you "much closer to the buying opportunity," so **you position ahead of the turn rather than wait for confirmation**. **The timing call: "I strongly believe this second quarter of the year is the turn point — whether it's right here in the second week of April, or whether May or June emerges... this is the window to act upon this opportunity."** (The GDX also pays about two $0.20 dividends over the LEAPS' life, a minor pricing input to the option models.)

**Sentiment gauges at the cycle bottom:**

1. **Hulbert Gold Newsletter Sentiment Index:** at the April 2021 read, sentiment was "incredibly negative." His cycle maxim: "at the bottom of a gold cycle you can't convince anyone to buy it... the best buying opportunities come when you buy when no one else wants to."
2. **Gold Miners Bullish Percent Index:** built on classic **point-and-figure** charting — it computes, across all gold mining stocks, how many are on a bull signal versus a bear signal. He marks the bottom of its range as the **buy zone** (red) and the top as the **sell zone** (green). It had printed down to **25**, entering the oversold zone where buy signals typically emerge. Context and caveat: in the 2013–2015 bear market it went to **literally zero** — not one miner on a bull signal — but "it never gets that bearish in the middle of a bull market"; readings of 5% or 0 require a genuine bear market, and he is "a seller on the idea" that it prints that extreme here.

### The macro overlay: the bust-then-boom setup (2020 version)

The live setup at the time of the 2020 cycles webinar: COVID-19 was crushing demand and driving commodities to "stupid, crazy cheap," while the policy response — "a huge fiscal spend" to restart the global economy — was set to ignite the recovery leg. The referenced call is **Marko Kolanovic's J.P. Morgan note** (circulated via Zero Hedge): a "massive bubble" in defensives, bond proxies, and long-duration growth as falling rates bid them up; "this is simply unsustainable... this bubble will likely collapse. And this time it is not different"; rotate into **value, commodity stocks, and emerging markets**. Ceresna endorses the rotation call ("right from J.P. Morgan, not some fringe analyst") but disputes Kolanovic's COVID-peak timing ("which I call BS on") — hence the whole point of the options layer: the *destination* is highly probable, the *when* is not, and long-dated gamma is how you hold a right call through wrong timing. His expectation for the turn: "as soon as the algos sniff that we have crested," the rotation out of defensives into cyclicals "is going to be fast and it's going to be hard."

### What NOT to do

- **Do not dollar-cost average down through a commodity bear.** The Teck cautionary path: $70 → $30 ("it's got to be good value, I'll average down") → $20 → $10 → $2, each tranche requiring new cash, each deepening the pain. "Throwing good money after bad" is financially and emotionally brutal — Luke's image: "like giving money to a teenager." The option route achieves the same scale-in *with the cash you already withheld*, after the delta on the first attempt has decayed to zero.
- **Do not believe you will catch the exact bottom or top.** The statistics were measured extreme-to-extreme; they are perspective, not a claim.
- **Do not treat the cycle table as a market-timing tool.** It tells you what *typical* looks like (and that an 8-month, −40% move is already atypical in length) — it does not call the turn.
- **Do not confuse re-entry with doubling down.** Repositioning restores original intended exposure from delta zero; it does not stack leverage on a loser. Holding losers *and* adding new positions is pyramiding — a different strategy for different capital.
- **Do not run these on names without option chains** (juniors) and **do not wander into options on futures** (e.g., natural gas) without dedicated education — a futures contract is already a derivative, so options on it are a "second derivative": different multipliers, term structure, convexity, calendar spreads.

## 9. Live-Market Craft: Worked Names, Q&A Wisdom, and Warnings

<!-- Sources: How to Find Asymmetry on Your Favourite Commodity Stocks (Using Options the Right Way); Using Options to trade Commodity Cycles; Asymmetric strategies to Repair and Leverage Your Gold Holdings; How to Leverage Gold Like a Pro -->

**Live examples beyond the core structures** (prices/vols as of the sessions):

- **U.S. Steel:** −40% ($14.50 → $8.50) in ~70 days, at a completed measured move; January 2021 $10 call at **$1.55** (53 vol, 329 days). The 10k-account version: A buys $9,120 of stock; B buys 10 calls ($1,500) with $8,500 in cash; C buys 15 ($2,300), $7,700 in cash. Starting delta **0.53**: a $1 stock move lifts the option ~$0.50–0.55; as delta climbs through 0.75–0.80, C's 1,500-share control overtakes A's delta dollars entirely. High vol is "rightfully so" for a stock that can halve in two months — and it is precisely that premium environment that pays the long call buyer in the recovery. Analog target range for the recovery: $14–17.
- **Cameco:** $10 call, 329 days, **$0.90** at ~35 vol — "a very reasonable" entry; two months earlier, near the washout, the $7 calls were "almost too good to turn up." Long Cameco in the portfolio; Ceresna is "a big fan of this uranium storyline."
- **Ovintiv (former Encana):** ~$15, ~50 vol; $15 call $3.50, $17 call $2.80 — same LEAP-at-the-bottom treatment.
- **Exxon Mobil:** one-year $3.60 call at a ~$60 stock, only ~**20% vol** — "almost being given away" for a name whose prior up-cycle rallied $20; possibly down to $55 first, but the $5 strike ladder gives clean adjustment points.
- **Canadian equivalents:** XEG (the Canadian energy ETF, ~$9) settles long-dated options to March; a March 2021 $9 call cost ~**$0.90** (~10% premium, **20 vol** — cheaper than XOP's 34–35 vol). Note XEG is closer in character to **XLE** (the broad energy ETF, ~20 vol) than to XOP (pure E&P, higher vol). Cycle stats had not been measured for it.
- **Natural gas equities:** SandRidge had fallen $19 → $2, "priced for bankruptcy" — at $2, "the stock itself is an option" (double on the bounce), but it has no long-dated chain; Range Resources is the popular equity proxy; the front natural-gas futures contract blew through 5.85 (losing Ceresna a bet with Kevin at The Market Huddle) out of a bull wedge with room to $7.50.
- **Yamana Gold** (small-cap example, ~$3.74, ~50 vol): $4 call ~$0.67; if wrong about the gold bull, the stock "can go from $3.75 to $2 in six months at the snap of your fingers" — the LEAP caps that at the premium and the repositioning captures the real low.

**Q&A wisdom (frequently the most practical material):**

- **Slippage on the way down happens "at the rate of delta"** — each further leg lower costs the option holder less than the last; that is the whole comfort of rolling down.
- **A roll is always close-then-open.** Do not keep the old strike *and* buy the new one (that is pyramiding).
- **Sell premium against your theta?** A legitimate style choice for advanced members; Ceresna keeps published trades simple long-call structures. "I've trained thousands of traders and never met two who trade the same."
- **On exiting a LEAP early:** yes, these are actively managed in the alert services — rolling and adjusting all the way; never buy-and-forget. The layering is always macro → timing → options.
- **The simulator is the on-ramp.** The most intimidating thing about options is not knowing what a trade will do before you do it; the simulator lets you plug in price, vol, and time and *watch* each scenario resolve. "Once you can see it, options become emotionally easier."
- **Emotion is the real enemy:** "once you get emotional, you stop making good decisions." Judge the position against the cycle thesis, not the daily P&L of a single option.
- **Junior miners without chains** are traded as options themselves (Section 7).

---

# Part V — Risk, Sizing, and Crash Playbook

<!-- Sources: Module 01 - Thinking Like a Master Trader; FREE MODULE - Risk, Randomness and Trading Sizing; BreakOutTrading; Short Term Hedging; Patrick's Favourite Trade Repair Strategy; 2021-02-19BPTTacticalPortfolio; How to Profit from a Market Crash; StrategiesThatGiveYouAnUnfairAdvantageInAMarketDownturn-Cleaned -->

## 1. The Master Trader Mindset: Markets, Liquidity and Statistical Advantage

<!-- Sources: Module 01 - Thinking Like a Master Trader (1080p with 30fps).transcript.md; How to Profit from a Market Crash (1080p with 30fps).transcript.md -->

**The market is marked to market — and that creates an illusion.** The price on your screen is simply what the last person paid. Ceresna's standing example: Apple, with roughly $1.3 trillion of market capitalization and hundreds of millions of shares outstanding — if one share prints at $330 at the close, every brokerage account marks all those shares at $330. This creates **perceived paper profits**: everyone believes their shares are worth that price *until they all try to sell*, at which point they "put the market down on themselves." A mutual fund "up 10% on the year" is a nearly useless number, because the manager never actually sold; in a crash that 10% evaporates because it was never real. Money is made only by **converting paper profits to real profits through the act of selling** — and very few investors ever get to sell at the best price. During the 2020 run Apple traded near $330 and $1.3 trillion of investors believed their shares were worth $330, but only a small fraction could actually sell there; the moment everyone else tried, the stock went to $260, "because that's actually where the active market is." The point of a trading program is to identify the windows where you get to be one of the few who transact at the most favorable prices.

**Price is a function of liquidity.** When asked "why is the stock down today?", the honest answer — "there were more sellers than buyers" — sounds glib but is literally true; the narrative is usually invented *after the fact* to justify the move. Any asset's price is a function of: the inventory of stock available, the motivation of sellers to liquidate, the money available to buy, and the motivation of buyers to get in. The market is a perpetual price-discovery process, and part of technical work is understanding where in that liquidity cycle the market currently sits.

**Statistical advantage comes in two flavors.** Most traders seek advantage through **probability of winning** ("I want to be right 60–70% of the time"). The course teaches that the more reliably manageable advantage is the **risk-reward proposition — the payoff profile**: lose small, win big. The casino analogy: the house wins 52% of hands versus the player's 48% — a small enough edge that a player can randomly win five hands in a row, and the casino doesn't care, because a thousand players will collectively put a million dollars on the tables today and the edge *must* emerge over a large sample. Trading is the same: **winning and losing streaks come in clusters**; short-term randomness is unavoidable as long as you have a genuine statistical edge.

**Herd behavior is the raw material.** Markets are made of emotionally driven investors who behave like a herd. In early 2020 the market kept rallying while the coronavirus clearly worsened in China, because each investor looked around, saw nobody else selling, and concluded the news didn't matter — then everyone realized at once that it *was* worse, and the collective stampede produced one of the biggest one-week drops in history. Fear and greed move investors in waves; measuring those waves through price action, market structure and Fibonacci proportionality is where the technician's edge lives.

**Three core rules of thinking like a master trader:**

1. **You don't need to know for sure what will happen next.** You only need an advantage in knowing what is *most probable*, or an implementation that creates **asymmetry** (small defined risk, large potential gain).
2. **Truly accept that anything can happen.** A trader who genuinely believes they will be right disregards risk management ("I don't need to manage risk on my gold position because gold is going higher"). Only when you accept you could be wrong do you actually respect and manage risk.
3. **Base every decision primarily on risk and money management.** If anything can happen, position sizing and risk definition — not the forecast — must be the anchor.

**The trifecta applied.** The macro → fundamentals → technicals → options layering (stated in the Orientation) is the credo — borrowed from Leonardo da Vinci: *"learn how to see, realize that everything connects to everything else."* Pure CFA-style analysts look only at corporate fundamentals; pure technicians only at charts — "not wrong, but not the holistic picture." Within the trifecta: **macro is the why**, **technicals are the roadmap** (when the move occurs and where it goes — the bridge that turns a macro story from guests like Mark Yusko or Luke Gromen into an implementable trade; Ceresna is a CMT), and **options are the tool** for building asymmetry into the implementation. Cautionary example: **Suncor in 2014** had a beautiful technical uptrend and beautiful fundamentals (pristine balance sheet, great management, cash flows, dividend history), yet oil went from over $100 to $26, the macro change destroyed the fundamentals, and the trend wiped out half the company's value.

## 2. Risk, Randomness and Position Sizing

<!-- Sources: FREE MODULE - Risk, Randomness and Trading Sizing (1080p with 30fps).transcript.md; Module 01 - Thinking Like a Master Trader (1080p with 30fps).transcript.md -->

Kevin Muir and Patrick Ceresna chose trade sizing as the free module of their Trading Masters program because it is the mistake beginners make most: trading too big, varying trade size inconsistently, and never adjusting for volatility — then being destroyed not by a bad method but by the **randomness of the trade sequence**.

**The bag of marbles.** To make an edge concrete, the module replaces coin tossing with a bag of marbles: **white marbles are winning trades, black marbles are losing trades**, drawn with replacement so the probabilities never change. Opening exercise: bet $1,000 on a $5,000 account, fixed bet, 50/50 bag. Question: in 100 draws, what is the probability of experiencing **five consecutive losses** at some point? Answer: **81%** — shockingly high even to a professional. Their spreadsheet (win rates 90% down to 10%; streak lengths down the rows) shows, for a 50% win rate over 100 draws:

| Streak length (losses in a row) | Probability of occurring at least once in 100 draws |
|---|---|
| 2 | ~100% |
| 3 | ~100% |
| 4 | 97.3% |
| 5 | 81% |
| 8 | 17% (about the odds of rolling a six on a fair die) |

The lesson: even with a great trade plan you will hit stretches where nothing works — randomness in the sequence, not proof your method broke. **"Nature is much more streaky than we ever give it credit for."** The perceived equity curve (smooth up-and-to-the-right) is not what success looks like; the real curve is jagged with deep drawdowns, and **the magnitude of those swings is a function of trade sizing**.

**Gambler's ruin.** Even the biggest trader — Carl Icahn, Stanley Druckenmiller — has a limited bankroll, while the market's is unlimited. Play a negative or even game long enough and a losing streak inevitably takes you to zero. The **Martingale betting system** (doubling up after each loss until a win recovers everything) *accelerates* ruin rather than preventing it — the player runs out of money or nerve, or the casino refuses the too-large bet. It is named for an 18th-century journalist-gambler "and all-around scoundrel" who ran the system using the money of his mistress, whom he called his Martingale. The professional's goal is the opposite: a system that survives drawdowns so your edge can express itself over the long run.

**The Kelly Criterion — history and math.** John Kelly Jr. was a WWII naval air force flyer with a physics degree from the University of Texas who joined Bell Labs. In 1954 the Supreme Court ruled TV game shows were not illegal gambling; a flood followed, including **The $64,000 Question** — a correct first answer won $1, prizes doubled each round (with jumps from $512 to $1,000 to keep amounts round), and one wrong answer lost everything. People gambled on the contestants, one entrepreneur arbitaged the East Coast/West Coast broadcast delay ("early high-frequency trading"), and news of that scheme inspired Kelly's 1956 work on optimal bet sizing.

**The formula:**

> **Kelly % = (Payoff ratio × Win% − Loss%) ÷ Payoff ratio**, where payoff ratio = average win ÷ average loss (in dollars).

Worked examples from the module:

| Scenario | Win % | Payoff profile | Kelly calculation | Kelly % |
|---|---|---|---|---|
| Marble edge | 70% | $1 win : $1 loss | (1 × 0.70 − 0.30) ÷ 1 | **40%** |
| High win rate, bad payoff | 60% | $1 win : $2 risk | (0.5 × 0.60 − 0.40) ÷ 0.5 | **−20% → do not bet** |
| Balanced | 60% | 1 : 1 | (1 × 0.60 − 0.40) ÷ 1 | **20%** |
| Low win rate, great payoff | 40% | $2 win : $1 risk | (2 × 0.40 − 0.60) ÷ 2 | **10%** |

The negative-Kelly case is the killer insight: a trader who wins *more often than he loses* can still be a losing proposition if the dollar losses swamp the wins. Ceresna saw this constantly at Learn2Trade among intraday S&P ("Spooz") day traders: quick to grab a couple hundred dollars of profit but leaving stops wide — losing big, winning small, never making progress. Fixing it requires the math *and* the discipline to execute stops.

Kelly's own origin experiment shows humans are bad at this: given a coin known to land heads 60%, when people traded it for real, **28% went bust, only 21% achieved the optimum payout, and over 25% bet everything on the first toss.**

**The simulations** (100 random draws per scenario, $100,000 account):

- **60% win / 1:1 payoff at full Kelly (20% risk per trade):** account grew to **$600,000+** — but between roughly the 13th and 20th trades came a run of **7 consecutive losses**; from a peak around $160,000–180,000 the account fell to **$20,000** — one losing trade from zero. Later, from the 40th to 60th trade it fell $300,000 → $200,000. At 25% sizing that account would have been finished. Full Kelly maximizes growth, but the near-wipeout and the emotional turmoil are inherent.
- **40% win / 2:1 payoff at full Kelly (10%):** $100,000 grew past **$300,000**, ending just over **$200,000** — but with a sequence in which **16 of 17 trades were losses**. Expect this; it will happen.
- **Half Kelly (5%):** roughly a **100% return** ($100k → ~$200k), but the account still drew down from **$105,000 to $55,000** (≈50%). At a 40% win rate, ten consecutive losses has a **20%** probability in 100 draws — 1 in 5.
- **Tenth Kelly (1% risk per trade):** $100,000 → over **$120,000**; worst drawdown **$106,000 → $94,000** across a 24-trade stretch with only 6 winners and 18 losers. Unpleasant but survivable — "you live to fight another day." The 1%-per-trade figure is the industry's most common rule of thumb because you can be wrong a lot: ten straight losses at 1% only takes you to $90,000.

**Sizing rules that follow:**

- **Never exceed Kelly.** Kelly is a *ceiling* — the growth-maximizing, not risk-minimizing, answer. Realistically you should be nowhere near it.
- **Size is personal.** A retiree trading a nest egg should be far below Kelly; a salaried entrepreneur running a $5,000 speculative account can rationally go closer to it.
- **Use Kelly to rank strategies.** If strategy A computes a 10% Kelly and strategy B a 20%, don't size the inferior one double the superior one.
- **Expect the greats' win rates.** Soros and Druckenmiller run win rates only in the high 50s / low 60s — meaning even they routinely endure the losing streaks the marble table says are inevitable.
- **Be the house, not the gambler.** Take a small edge methodically so that over a large sample chance washes out and probabilities dominate. And respect genuine randomness: in January 2020 the Iranian escalation moved markets in a way nobody had calculated — your methodology must absorb events nobody forecast.

## 3. The Breakout Trading Method

<!-- Sources: BreakOutTrading (1080p with 25fps).transcript.md; Short Term Hedging (540p with 25fps).transcript.md -->

Breakout trading is the trade-issuance methodology of the Breakout Trader watch list. Its foundation: **markets move in ebb and flow**, and those waves have measurable proportionality (Fibonacci). When a market in a primary uptrend corrects, that correction creates the moment from which you can **build asymmetry** — manage risk down to a small amount while retaining potential gains many times larger. The whole creed: **"learn to lose small and win big"** — when wrong you take a paper cut; when right, extraordinary gains. The technique can be run without options (plain stop losses), but the house style combines the technical setup with an options hedge. (The service-side rules — the 20-day activation filter, the expression ladder — are Part II, Section 7.)

**The technical pattern.**

1. **Measure the impulse.** Take the rally from significant low to significant high. Example: SLV rallied $13.35 → $18.35, a $5 move.
2. **Expect a ~50% retrace.** Half of $5 is $2.50, so the 50% Fibonacci retracement line sits $2.50 below the high — "if the rally was $5, a natural pullback is about half the prior rise if the trend is still intact."
3. **Corrections often come in zigzags** — two distinct waves down before the trend resumes. Deeper corrections approach the 61.8% zone, the **"kill zone,"** into the buy zone when reversal candles confirm the stall.
4. **Project the next leg as a measured move.** The next rally tends to be directly proportional to the first: project the first leg's length out from the correction low (measuring the entire previous move, lowest low to highest high). These **technical extension** levels define the profit-taking zones.

**Worked examples.**

- **Wheaton Precious Metals:** November–April rally of $10. Expected pullback: $5. Actual: $5.50 — essentially a clean 50% retrace (straight down, no real zigzag). Original breakout entry filled at **$19.54** — bought in the pullback zone, not at the highs. Projection: $10 measured move from ~$20 → **$30**; the stock then completed the exact symmetrical move. At session time it was correcting toward the ~$25.50 (50%) area, premised on trend resumption.
- **Amgen (live trade construction):** a ~$39–40 rally off the July low; pullback of ~$22 — deeper than 50%, into the 61.8% kill zone, with reversal candles. Prior major highs cluster around **$210**, so the profit-taking zone must **envelop the previous high** (an adjusting trade belongs at major overhead resistance before any $230 target), with **target one at a round number with liquid option strikes — $200–205** — and a stretched zone to $205–225.
- **Walgreens:** the honest counter-example — a flag-formation breakout that failed. Roughly half of breakout trades don't work; the method's economics do not require them to.

**The 50-50 math exercise.** Assume you are no better than a coin flip on every trade. Ten trades: five losers with an average loss of $1,000 (−$5,000), five winners with an average gain of $3,000 (+$15,000) → **net +$10,000**. Being right only half the time is fully compatible with strong profitability — "it doesn't matter if you're right or wrong. It's about how much you make when you're right and how little you lose when you're wrong" (the Soros motto quoted in-session).

**Implementation — stock plus a short-dated protective put.** The Amgen execution (entry ~$195):

- A sensible stop loss sits below the previous low / fib zone — at least **$7 away (~$188)**. Tightening to $3 guarantees you get noised out: at 22% implied volatility, Amgen's **one-week one-standard-deviation implied range was ±$6** ($189–$201) — a normal one-day swing stops you out instantly.
- Instead: buy a **14-day put at your entry strike ($195, October 18 expiry) for $3.50** — a guaranteed exit at $195 and **two weeks to find out whether the breakout is real**. Failures (like Walgreens) declare themselves fast; you exit with the premium as total cost, never gap-exposed through earnings or a headline ("this little drop could be a Trump tweet").
- **Size every trade to the same risk (~$1,000 in the demo), regardless of conviction.** Demo: ~300 shares (~$58,000–60,000 of stock) plus 3 protective puts ≈ $1,000 of premium = $1,000 of defined maximum risk; exercising the puts at any moment guarantees exit at $195.
- If it works, potential is $20–40 of upside (the double-top retest at the prior high already gives 2:1; the full measured move 4:1+) against the defined risk. Three months of protection is unnecessary — the short hedge *is* the admission "I'm giving this trade two weeks to prove itself," and defined risk is what permits bigger sizing and real conviction.

**Miscellaneous doctrine.** The technical approach is **not founded on implied volatility** — IV merely reflects options-market sentiment and is "often mispriced"; volatility tools like Bollinger bands are legitimate alternatives, but the retracement measurements don't use implied ranges. A self-observed quirk: the trades members dislike most somehow keep turning into the biggest winners — crowd affection for a trade seems to reduce its odds.

## 4. Short-Term Hedging with Protective Puts

<!-- Sources: Short Term Hedging (540p with 25fps).transcript.md; BreakOutTrading (1080p with 25fps).transcript.md -->

This session (a live Interactive Brokers bootcamp, circa mid-2019) walks through buying protection, rolling it, and monetizing it — the operational half of the breakout method.

**Choosing the put: strike and duration.** Existing position: 100 shares of GLD (gold bullion ETF) worth ~$12,000, with dollar-rally risk to gold over the next month. The June monthly **$125 put cost $1.27 ($127)** — full insurance of every dollar of downside for a month. The **$122 put cost $0.37 ($37)** — crisis-only insurance, $90 cheaper but with a $3 deductible. Neither is "right": decide whether $0.90 is worth paying to remove $3 of additional risk — protection amount is a personal variance tolerance. Expirations: weeklies, monthlies, and quarterlies (Sep/Dec/Mar, out to January 2020 on gold) — for short-term trades you rarely need to go past a weekly or the next monthly. Individual names work the same at 1 contract per 100 shares (Agnico Eagle at ~$57: June $56 put at ~$1.20). A **married put** is buying the shares and put simultaneously; on an existing position buy the put alone, "buy to open," at a limit mid-spread rather than market.

**Rolling the hedge.** Amazon example: 100 shares bought at **$1,436**, now ~$1,600 (+~$17,000). Previously a long-dated **July $1,580 put** was bought for ~$7,000 — spending $7k of the $17k profit to guarantee a $10,000 minimum while keeping 100% of upside. Rolling is closing one option to replace it with another: close the 1580 (~$51) and buy the **$1,600 put (~$61.40)** for ~$10 net — "like moving your stop loss higher." The guaranteed sale price walked up $1,435 → $1,580 → $1,600 as the stock rallied; cumulative protection cost was roughly $70 of premium (partly recoverable in residual value when the trade ends).

**Short-term protection.** For a trade expected to resolve in weeks, don't buy months: an at-the-money **May 25 $1,605 put on Amazon cost $25** — two weeks of total downside removal on a stock that had gapped $100 in a day, for $25/share.

**Monetizing the put in a drop** — the core management skill. If Amazon drops from ~$1,605 to **$1,450**, the $25 put's intrinsic value is **at least $155**, plus a little time value. Sell it: paid $25, collect $155+, so **net +$130 on the hedge** while the stock is down $150+. Lean that $130 against cost basis — breakeven drops from ~$1,435 to **~$1,300** — then buy a fresh ~$25 put at the lower strike if protection is still wanted; on a rebound to $1,600 you've clawed back $130 and still capture the rally. Live Apple example: holding the **$177.50 put** into a drop, Ceresna monetized **over $15** of put value at the lows, bought a new **$160 put**, and captured the entire rebound — about $2 + $2 + $2 ≈ $6 of puts over the sequence. "It costs money to buy puts, end of story — but I did not lose money on the drop, and I made the whole way back up."

**Full worked example — Disney (the breakout + hedge template).** Setup: double-bottom formation with the stock back above its 20-day moving average for four-plus sessions — a fresh breakout candidate at ~$101.69.

- Buy **1,000 shares at $101.69** (~$100,000).
- Two-week protection choice: the **$101 put costs $1.21**, the **$102 put costs $1.67–1.70**. Do the true math: the 101 put leaves a $0.69 deductible (stock can fall from 101.69 to 101 before insurance pays), so total worst case = $1.21 + $0.69 ≈ **$1.90/share ($1,900)**. The 102 put costs $1.70 but guarantees a sale **above** your cost — a locked-in $0.31 gain — so worst case = $1.70 − $0.31 ≈ **$1.40/share ($1,400)**. Minimizing maximum loss, the $102 put is ~$500 less risk than the $101 put. Buy 10 × the $102 put (~$1,650–1,680).
- Simulator check (19.5% IV): crash the stock to $95 or $90 and the position's loss freezes at ~**$990–1,000** — the stock's $11,000 loss is offset by the put's $10,000+ gain. At a $106 breakout, the put expires worthless (−$1,300) but the stock is +$4,300 → **net +$3,000**: $1,000 risk for ~$3,000 of reward, the standing "lose small, win big" profile.
- Versus a stop-loss user: a stop below the prior lows (~$97) risks ~$4,000; a tight stop at $99 gets triggered in the noise for a **$2,500 realized loss**, after which the stock reverses and rips back to $102 — the stop user is out, the put holder "was never knocked out; this was just noise."

**Synthetic stock: the deep in-the-money call.** A high-delta deep-ITM call *is* a synthetic long — protect it exactly like stock. Example: Disney **June $95 call at $7.45** ($6.75 intrinsic; **delta 0.87**, high gamma, approaching 1 on the upside). Ten calls ≈ $7,000 outlay replacing ~$10,000 of stock, plus the same $102 put. New math: intrinsic $7 + time ~$0.45 + put $1.68 ≈ **$9.13 total outlay, max risk ~$2/share (~$2,000)** — the price of leverage and a higher percentage return (the call is worth ~$11 if Disney rips to $106). Caveats: (1) deep-ITM strikes have **wide spreads** (a Disney weekly $90 strike quoted 10.55 × 12.80 — you bleed profitability fighting for mid-fills; only do this where ITM liquidity is good); (2) on a synthetic you *sell* the put rather than exercise it (no stock to deliver); (3) this is the standard technique for **Canadian registered accounts (RSPs etc.)** where margin is prohibited — long ITM call + protective put = synthetic leverage inside a registered plan; (4) a put **debit spread** (buy the ATM put, sell a lower strike) is the more advanced partial hedge — removes part, not all, of the downside (covered in a Montreal Exchange options-education presentation).

**Other executions from the session:** American Express at target-one ($102) — 1,000 shares with a two-week $102 put at ~$1.30 ($1,300 defined risk) to ride toward $105–110. Deutsche Bank at $13.88 — a would-be breakout over $14 targeting $14→17: 5,000 shares ($70,000) with 50 two-week **$14 puts at $0.45 (~$2,250)** capped risk at ~$2,000 against $10,000–15,000 of potential; the cheaper $13.50 put (~$0.20) leaves a 40-cent deductible. Agnico Eagle on a measured-move projection to 48–50: just buy the at-the-money protection. Pedagogical rule: **beginners run the trade as stock + hedge**; graduate to spreads and synthetics later.

## 5. The Trade Repair Playbook (Patrick's Favourite)

<!-- Sources: Patrick's Favourite Trade Repair Strategy (720p with 25fps).transcript.md -->

Everything in repair strategy starts with **choosing your goal**, because the goal determines the structure. There are exactly three:

1. **Exit:** get out at break-even, or at a far smaller loss, without adding downside risk — you no longer want the stock, just a dignified exit.
2. **Hold, break even faster:** you like the stock long term and want to recover to break-even sooner.
3. **Hold and add at better prices:** long-term holder willing to dollar-cost average, but only at *favorable* prices.

**Why not just dollar-cost average?** Ceresna is blunt: buying delta-one shares into a falling position is "throwing good money at a losing position that traps that money." A holder who averaged Peloton down 90% just bought more losses all the way down. Worse, if you are fully invested, averaging requires **margin** — borrowing to add as the position keeps falling, with account-zeroing risk. In a bear-market backdrop (Fed tightening, liquidity draining, recession risk — the 2022 context of the session) there is no guarantee a dip makes you a rock star in three months. Options repair can fix a position **without more cash and without margin** (beyond any uncovered debit). (The gold-specific repair templates — put-financed calls, covered-call-plus-spread — are Part IV, Section 6.)

### Strategy 1 — Exit via the 1×2 ratio call spread ("get out at break-even")

**Construction:** to 100 long shares, **buy 1 at-the-money call and sell 2 out-of-the-money calls** (the 2:1 ratio is the standard), structured to be as close to **zero cost** as possible. The short calls are *not naked* — as MacroVoices' host (Erik) first observed, the position decomposes into a **covered call on your 100 shares plus a bull call spread**; there is **no margin requirement beyond any net debit**.

**Putting it together — the Walmart example:** investor buys 100 shares at **$132** on an earnings dip; the next day Target's miss wipes another **$12** off Walmart — down **$1,200**. Repair: buy the **June $122 call**, sell **two June $127 calls** (zero cost). Outcomes:

- **Stock keeps falling:** the ratio spread expires worthless — the repair cost nothing, and you still only own the original 100 shares (the dollar-cost averager who doubled down to a $126 average is sitting on ~**$5,000** underwater, twice the shares, needing a **20–30% rally** just to break even).
- **Stock rebounds to $127** (the short strike), not $132: at expiration the spread's value has offset the remaining $500 stock loss — **break-even at $127 instead of $132**. The repair raises the *probability* of a clean exit because the required rally is smaller. You accept **assignment and exit at ~break-even**.
- **Upside is capped above the short strike:** at $130 you make no more than at $127 — acceptable *only if you genuinely want out*.

**Simulator template ($100 stock, 35% IV, cost basis $110, down $1,000):** buy the June **100 call for $3.73**, sell **two 105 calls at $1.83 ($366)** → net cost ~$0. Payoff at expiration: 45° loss line below (same as stock), a *steeper* gain line from 100 to 105, then flat. At **$105** you've recovered the $500 stock loss plus $500 of spread profit = the full $1,000 back — break-even at 105 instead of 110. At $110 you're still only +$1,000. Timing note: the full payoff exists **only at expiration** — with 13–15 days left a bounce to the short strike is not yet break-even; you must hold to expiry and let the covered call take the shares.

### Strategy 2 — Hold via the debit (bull call) spread ("break even faster, keep the stock")

If you refuse to lose the shares, either (a) run the same 1×2 but **actively roll up or close one of the two short calls** before it can take the stock, or (b) simpler: **marry a plain debit spread** — buy 1 ATM call, sell 1 OTM call, accepting a small debit.

**Why a spread rather than a naked long call in a sell-off:** volatility spikes when markets drop. A 30-day call priced at **$2.29 at 20% IV costs ~$4.00 at 35% IV** — you'd be buying at peak vega, exposed to losing on the option from **vol contraction** even as the stock recovers. The spread's short call offsets equal vega, cutting both cost and that vol-collapse risk. Payoff: the stock's 45° downside is unchanged; on the rebound the spread gives a **steeper, more immediate gain up to the short strike**, reaching break-even much sooner.

**The SLV COVID-crash illustration:** long-term silver holders watching the margin-call liquidity event crush SLV, believing a V-shaped snapback was absurdly overdue, could marry a bull call spread (e.g., the **12→15** region) so the break-even point arrives far earlier on the snapback.

**Costs, stated honestly:** the demo spread cost ~**$189–200**, raising break-even by that amount; if nothing happens you expire down the debit. Compare at $105 with a $100 basis down $1,000: the spread-married holder is **+$500 stock + ~$800 spread ≈ $1,300 recovered** — nearly what the dollar-cost averager makes (+$1,000 on 200 shares) — but at $90 the DCA trader is **−$2,000** while the spread holder is only **−$1,189** (stock loss plus small debit). A debit spread also moves at its **net delta** early on and only reaches maximum value at expiration — a sharp V-bounce won't pay the full spread width instantly.

### Strategy 3 — Dollar-cost average at better prices: the put-financed spread

For the holder willing to add shares — but only at attractive levels — **finance a debit spread by selling a put at your desired add-price.** Walmart example (stock at **$119**): buy the **125/130 call spread** (125 call at $1.61, sell the 130 at $0.66 → ~$1 debit per $5 width, a 4:1 structure); sell the ~**$108 put for ~$1** (the 105 put was $0.64, the 110 $1.20) → **zero cost**. Outcomes:

- **Rebound:** e.g., the 38% retracement back toward $132 — you cash in a call spread that cost nothing, massively improving break-even.
- **Collapse below $108:** you are *assigned* and buy 100 more shares — averaging down, but at **$108, not the prevailing $119**; the extra downside risk exists only below 108, and it's the averaging you were willing to do anyway.
- **Skew tailwind:** in drops the left tail of the volatility skew fattens, making put premiums richer — sell even farther-OTM strikes for the same income. And if the stock drifts away from $108, the $1 put bleeds toward **10–15 cents within a week** on vol contraction — buy it back and bank the difference. The one disadvantage: the short put **requires margin** (the obligation to buy).

### Timing, failure, and exits

- **When to execute:** at the tail end of a *symmetrical* measured move. The gold example on the 4-hour chart: a $150 decline, a flag, then **$70 down over 5 days followed by $70 down over ~4.5 days** — symmetry complete at the Fibonacci-extension "red zones" where bounces are most probable. That is the tactically ideal moment to open the upside spread.
- **If you're wrong:** the worst case is the debit (or zero on the 1×2). Close the whole combination near break-even and **re-execute a fresh spread at the lower level** — "like a mulligan in golf." In the Walmart template, a 1×2 opened and the stock dropping to $90 within five days: close the entire spread at ~zero, eat only the stock's loss, open the new **90/95 spread** and try again — multiple controlled stabs at finding the bottom.
- **Exits:** hold to expiration for the designed payoff (spreads reach maximum only at expiry); close early only to avoid unwanted assignment. **Match the spread's expiration to the realistic bounce window** — expecting the rebound in two weeks means the two-week spread, not four-to-six weeks.

## 6. The Tactical Portfolio (Launched February 19, 2021)

<!-- Sources: 2021-02-19BPTTacticalPortfolio (1080p with 25fps).transcript.md -->

A fully tracked model portfolio on a **$1 million simulated account**, right-sized by each member (a $100,000 account runs one-tenth the sizes). Design principles: **leg into positions over weeks/months rather than blanket-launching into an extreme market** (launch moment: S&P in a bull run, Russell near-parabolic, dollar in full bear mode, commodities at extremes, crude at $60, gold selling off hard); **review weekly** (15+ minutes every Monday — "most portfolios adjust quarterly, but if a crazy move happens, what business do we have waiting for quarter-end?"); keep it **as static as possible** outside those moments; choose the temperament — "dragon-style or All-Weather-style." Audience: real portfolios of roughly **$100,000 to $100 million** — sub-$50k accounts hunting for upside kick should not copy it one-for-one.

### The long-term (never market-timed) sleeves

**Equity — 25%, broad ETFs only, never individual stocks.** Only ever rebalanced to target weight, never timed; all hedging happens in the tactical sleeve. Launch tranche (~$153,000 of the eventual $250,000+):

- **RSP (S&P 500 Equal Weight) — 5%** (~400 shares, ~$54,000). Equal-weight chosen deliberately: in a rising-rate environment the largest-cap, highest-multiple names (the FAANG block) are the most vulnerable, so equal-weighting all 500 should outperform the cap-weighted index.
- **URTH (global developed markets) — 5%** (~400 shares, ~$47,000).
- **EEM (emerging markets) — 5%** (~900 shares, ~$50,000).
- Remainder (~10%) added tactically as the market reveals direction. Non-US members can substitute ~3% domestic equity + 2–3% RSP.

**Tactical income & bonds — up to 20%.** Launch (~$110–115,000):

- **IVOL — 5%** (~1,700 shares, ~$49,000): the TIPS-based expression; "zero interest in owning TLT" at that moment given rate risk.
- **REM (mortgage REIT ETF) — 3%** (~1,000 shares, ~$30,000): a basket of Annaly-type mortgage REITs yielding ~10%; if you can't buy the ETF, buy **Annaly (NLY)** directly.
- **AMLP (midstream MLP ETF) — 3%** (~1,100 shares, ~$30,000); substitute **Magellan** and other top holdings if the wrapper is inaccessible — open the ETF, buy its top components when the ETF itself can't be owned.
- A **put-writing income ETF** was deliberately deferred until a volatility spike made premium-harvesting attractive.

**Gold & silver — 15% static** (~$100,000 GLD / ~$50,000 SLV; 10/5 split), placed at once because gold had gotten "cheap enough that we have no business market-timing it." May be run unhedged (the launch choice) or with a **rolling collar** "if that's better for your sanity" (collar mechanics: Part IV, Section 3). Stopping at 15% rather than Chris Cole's ~20% gold weight leaves room to **juice to 25% tactically** — adding another ~$100,000 long gold "whenever gold is decisively in trend." Any liquid gold/silver ETF works worldwide; nothing is special about GLD/SLV except liquidity.

### The tactical sleeves

**Commodity trend following — 5% uranium + 5% GNR** (broad natural-resource equity ETF), ~$100,000 at launch, both in confirmed bull phase, plus ~$50,000 to add. Signal: a **40/50-day exponential moving average crossover** (exponential used, simple fine). Why paired MAs: the 50-day alone is a good primary-trend gauge but whipsaws when tested for a week; requiring the 40/50 crossover smooths the flip (the same filter from the Dragon Portfolio, Part I). Alternatives welcome (e.g., the turtle approach — new 6-week or 8-week highs/lows) if you feel an edge. **Structural wrinkle:** go *long* commodities through commodity **equities** (extra alpha from the Freeport-McMoRan-versus-copper effect) because futures-based ETFs carry perpetual **contango drag**; when flipping *short*, short the futures/ETFs themselves so contango works *for* you. Explicitly excluded: crypto — "no tulips in our portfolio."

**Long volatility — up to 25%, three expressions at launch:**

- **SPY calendared straddle — 5 contracts** (the exact structure of Part III, Section 2): delta-neutral at inception with ~$150,000+ of delta-dollar exposure either way; the portfolio's standing long-vol proxy.
- **GLD bull call spread 200/250 — 6 contracts (~$100,000 of tail):** cost **$3** (200 call ~$4, sell the 250 at ~$1.35), paying **$50 if gold explodes higher** — "an absolute no-brainer" right-tail lottery ticket (the Part IV skew spread, section 5). Registered-account holders who can't sell the short leg: buy the far-OTM calls outright and eat the extra premium.
- **TLT call backspread — 10 × 5** (sell ~10 at-the-money **143 calls at ~$10**, buy ~5 **155 calls at ~$5**; "10,000 in, 10,000 out" ≈ **zero net cost**): the portfolio's **deflationary-impulse insurance**. This portfolio is long commodities, long equities, long inflation trades — the thing that "kiboshes" it is a deflationary shock sending bonds screaming higher, so rather than own TLT, buy the right tail of TLT. If bonds keep dying it expires worthless; if bonds blast off it pays massively. (Fill discipline: work the mid — don't cross a 9.30 × 10.25 market as the demo did.)

**Adaptation notes.** Registered/retirement accounts can't run the short-option structures — replace equity ETFs with **~90-delta deep-ITM call synthetics** (e.g., an EEM July 45 call at ~$15, wide spreads requiring mid-price fills) and **size them as delta-one exposure**; accept "deemed disposition" tax consequences versus never-forced-to-sell ETFs. European members substitute domestic equity and local gold/silver ETFs. Stylize the trend signal, not the risk framework.

## 7. Downturn and Crash Strategies

<!-- Sources: How to Profit from a Market Crash (1080p with 30fps).transcript.md; StrategiesThatGiveYouAnUnfairAdvantageInAMarketDownturn-Cleaned (1080p with 23fps).transcript.md -->

A downturn portfolio wants at least one position that **moves inversely in a tail event** — a hedge that compensates for losses or produces outright profit when the portfolio's other components break. The course compares the three hedging structures it has actually run — **straddles/strangles (actively managed), backspreads, and debit spreads** — and explains why the standing choice migrated from the first to the last. (Context: Logica's Wayne runs an actively managed long-straddle program designed as a sleeve inside something like the Dragon portfolio.)

### Long straddles and strangles

**Straddle:** simultaneous purchase of an at-the-money call and put. Properties: **double vega** (extra-sensitive to volatility changes), starting delta ≈ 0, a **higher break-even** (two premiums), maximum loss if the underlying is unchanged, and profit on the wings — and you can profit **with no price movement at all** if implied volatility jumps. **Strangle:** same trade with separated strikes — less capital outlay, bigger move required. **Duration doctrine:** constant long-vol managers buy longer-dated structures and roll before the final months, avoiding the steepest **theta burn**.

**Ratioed strangle (the skew trade):** index call wings are cheap relative to the ATM, so buying 3× OTM calls against 1 put costs about the same as a pure straddle but carries far more upside delta. Demo: a 10-lot S&P 445 straddle starts at **$232,000 delta-dollars**; a **30×10 ratioed strangle** (3× the OTM calls) costs about the same (~$1,500 vs $1,300 per unit in the simulator at 13% IV, ~447 strike, October expiry) yet starts at **$329,000 delta-dollars** — a synthetic long bias for free.

**Simulator outcomes (S&P ~447, 13% IV, 20-day windows):** vol falling 13 → 10: both structures **lose money with zero price change** (the core vega risk). Vol spiking to 20: **+$700 on a $1,300 outlay with no price move** — a direct volatility bet, superior to VIX calls (whose pitfalls are Part III, Section 3). A −10% crash to 400: both make **~+$3,000** — the ratioed strangle gives up nothing. A rally to 464: the ratioed strangle **outperforms** on the extra OTM call gamma. The price: an unchanged market bleeding theta daily — with vol at 10 and 24 days of decay, a straddle is "essentially completely worthless." That decay profile is why the standing hedge moved to debit spreads.

**As a portfolio hedge:** ~$134,000 of SPY (300 shares) + a 3-lot straddle. In a 10% correction with vol jumping to 25: stock −$14,000, straddle +~$10,000 → **net −$4,000** instead of −10%. In a 20% crash (S&P 370) the loss **does not get worse** — the put leg is fully in the money. Active management (Logica-style) market-times the internal swings — selling calls into rallies, re-weighting delta-dollars between wings.

### Call backspreads (right-tail / melt-up structures)

**Construction:** sell at-the-money calls, use the credit to buy 2–3× as many out-of-the-money calls. Demo: sell 10 S&P 447 calls for a **$5,940 credit**, buy 30 456 calls for ~$6,000 → near **zero cost**. Payoff: **no risk if the market falls** (keep the small credit) and *unlimited* profit in an explosion higher; the only risk is a **modest rally** landing near the short strike at expiration (the V-shaped red zone — max loss around 455 after 24 days). Overlaid on 100 shares of SPY (~$44,000): a drop to 420 adds **no option loss**; a grind to 455 leaves you net profitable (stock gains exceed the spread's max loss); a melt-up to 480 adds ~**+$1,500** of option profit on top of ~+$3,000 of stock — the standard structure for "juicing" a bullish book's right tail, the same structure Tian Yang of Variant Perception described buying on MacroVoices.

**Why the skew makes call backspreads cheap:** implied vol is not one number. On the S&P, an OTM 425 put might be priced at **20 vol** while an OTM 460 call prices at **10 vol** — and vol is *the* price driver: the same 30-day ATM option is ~$5 at 10 vol and ~$10 at 20 vol. Because you sell the higher ATM vol and buy the *cheap* call wing, the market lets you buy **three calls for the price of two** (live $3 vs the simulator's constant-vol $6).

**Put backspreads — the crash tool with a warning:** mirror the construction for the left tail. But skew forces the short put **farther and farther out of the money** to reach zero cost, creating two problems: you need an *extraordinary* downside move to pay, and the structure interferes with vega during the decline. Verdict: **if you genuinely forecast a 50%-in-two-months crash, accept no substitute — the put backspread carries at zero and pays enormously on the tail.** For a **10–20% correction** it cannot build enough intrinsic value to behave as a hedge — which is why the standing choice for a garden-variety correction is the debit spread.

### Put debit spreads — the standing correction hedge

**Construction:** buy the higher-strike put, sell a lower-strike put, same expiry (a vertical). Benefits: the short leg **hedges vega** (long and short vega combined — you survive vol normalization from, say, VIX 26 back to 15 without the "slam" a naked put eats), slashes theta carry, and defines the worst case at the small net debit so the bulk of capital stays on the sideline and the trader stays calm. Going out-of-the-money with both strikes buys asymmetric payoffs: the demo **SPY 255/245 bear put spread at 261.50** cost **$2** ($5.00 debit − $3.00 credit) per $10 of width, controlling **$25,000 of notional downside per contract**; at expiration with both legs in the money it's worth $10 (an 8:1 max), and a move to $6 mid-course is already a **200% return**. Timing caveat: with the template showing room to bounce 100–150 points first, opening it immediately "just because the webinar says so" is wrong — the setup waits for the upper zone.

**Skew makes it cheaper than it looks:** the constant-vol simulator priced a December SPY 430/400 put spread at **$4.80 − $0.50 = $4.30 net**; the live market charged ~**$10.37** (18–19 vol) for the 430 but paid ~**$2** for the 400 (priced at **24 vol** on the fat left tail) — the skew income cut the hedge cost by roughly **$1,000** across the 4-contract position versus constant-vol pricing. Skew systematically rewards put-spread hedgers.

**Management rules.** There is **no rule that the hedge must be 1:1 with the shares** — the demo over-hedged 200 shares with 4 spreads deliberately. And there is **no rule you hold the original strikes**: when a real drop is underway, **widen the spread** (roll the short put lower) so both legs don't end up in the money while the market nose-dives. The roll is **vol-neutral** — you close the high-vol short option and sell the new lower strike at equally elevated vol, so the adjustment works even with the VIX screaming from 15 to 30. Cost example: rolling the December short leg from the 400 ($5.45) to the 380 ($3.65) — widening protection from 30 to 50 points — cost only **$2**. In the sim, a fast vol-spike drop to 400 took the 200-share book from −$9,000 to **−$4,000** with the OTM spread still on its gamma path. And note: hedges are usually **not held to expiration** — "it's about the rate of the hedge," the delta/gamma path while time value remains.

### The crash playbook (the February 2018 "How to Profit from a Market Crash" case)

**Setup recognition at the top.** The January 21 ratio-call-spread webinar (Part III, Section 1) had flagged: (1) an **acceleration in slope** on the weekly S&P chart — the parabolic signature Bitcoin shows before corrections; (2) retail inflow into S&P futures; and (3) Morgan Stanley flow data showing **customer S&P call buying at the 100th percentile** (customers are normally net call *sellers* via covered-call yield programs) while **put buying sat at the 0th percentile** — effectively nobody hedging. "When everyone gets on the wrong side of the boat, the boat tips over" — with the short-vol complex as the fuel.

**First question: correction or bear market?** Bear markets come with economic slowdowns, preceded by **yield-curve inversions** and deteriorating leading indicators. With no slowdown evidence, the working assumption was *correction* — a **mean-reverting secondary move within a primary trend**. The template's first assumption is always stress-tested: if it breaks, the entire template is discarded.

**The template grid.** Mark the top (**T**); draw the **−10%** and **−20%** lines; mark **T+30 and T+60 calendar days** (calendar, not trading, days). The live market: just over 10% down intraday (less on closes), about two weeks past T. Now walk through history — if the assumption "this is just a correction" is right, the current drop should rhyme with past corrections:

**Historical corrections (the walk through history):**

| Correction | Pre-top structure | First decline | Bounce | Full retest / end |
|---|---|---|---|---|
| **2016** | ~2-month topping formation (Nov–Dec) | ~2 weeks, ~10% | ~50% retrace of the drop | Full retest at ~5–6 weeks |
| **2015** | ~5-month sideways distribution (Mar–Aug) | 3 days, 10–12%, incl. a ~7% single day | 2–3 weeks, ~50% retrace | Double-bottom retest at ~5–6 weeks |
| **2011** | ~5-month top (head-and-shoulders shape) | **9 days, 20%** | ~50% retrace | Full double-bottom at ~7–8 weeks |
| **2010 "flash crash"** | **None** — only correction with no topping formation; ~20% rally in the prior 2 months (~1050→1200+) | One-day ~10% plunge (circuit-breaker rules rewritten after) | 3-day bounce, then renewed selling | Bottom only at ~**9 weeks** |
| **2007** | 1–2 month topping formation | 2 weeks down | 3 days retracing ~half, then a second sell wave | ~4 weeks total — the shortest |

The 2007 episode matters most: it is the only **late-business-cycle** correction in the sample, triggered by **Bear Stearns disclosing two subprime hedge funds wiped out** (the bailout recap was Bear's undoing) — yet the S&P **still made higher highs by October 2007**, and the real bear began only in the October–December window. The analogy drawn in early 2018: the **short-vol blow-up may be "the subprime of this time,"** and per Chris Cole the short-gamma unwind "could take years" — yet even a regime change doesn't preclude new highs first.

**The pattern and the scenarios.** First-wave bottoms within two weeks are common, but **every correction lasted at least four weeks and up to nine** — buying the first bounce is historically buying too early. The template's base case: a **~50% retrace** (~100 S&P points), media declaring the dip bought, retail suckered back in — "then the rug gets pulled" into a full **retest of the low around early-to-mid March**; the alternative is a symmetrical measured move toward **~2,400**; a 20% correction "I wouldn't count on it." (A running joke with a real use: Ceresna's vacations cluster at major turning points — his booked March break, **March 10–16**, put the likely resolution window in mid-March.)

**The emotional rinse cycle** (the behavioral engine behind the template): the drop produces the "what the f—" moment → a +200-point bounce produces "I missed the bottom, buy, buy, buy" → the next flush leaves the chaser a deer in headlights → a later stabilization produces "it's over, back to buy-and-hold" → the final leg down produces capitulation ("the bear market is beginning, get me out") — precisely the compelling **buy-the-dip moment**. Years of dip-buying conditioning guarantee at least one more full cycle; and per 2007, even a changed regime can still print higher highs before the true bear.

**Trading the template:** scalp the bounce while **hedging longs into the rally**; build new asymmetric downside positions as price enters the upper zones; at the lower zone buy the dip with **core longs hedged against the swing volatility** of the bottoming process. Luke's testimony on why the structure matters: trading 2008 alone meant the full emotional roller coaster, no sleep; the structured SPY trade was "boring" — put it on, wait, exit small if wrong, win big if right.

**The trade that actually paid — the calendared straddle.** Through the low-vol regime (SPY options at **9–10% implied**), while publicly running ratio call spreads, the member book was positioned for the drop via **rolled calendared straddles**: on **December 28**, buy the **January call + March put** at the 268 strike. Logic: a parabolic market will either rip or tank — no range — so the *short-dated* call supplies the gamma to profit immediately on a rip while the *long-dated* put has the duration to survive a full correction. Each rip → take the straddle profit (short call outperforms the put's loss) and re-straddle higher: **268 → 274 (Feb/Apr) → 279 → 283**, ending long the **April 283 put at sub-10% vol** plus a short-term February call hedge when the crash arrived — "a windfall."

**What dies when vol spikes — and what replaces it.** After the event, SPY straddles were ~**50% more expensive**; a vol normalization (guests' consensus floor around VIX 15, per Devin Anderson) would compress any long-vega structure; ratio spreads need wider strikes to reach zero cost (extraordinary moves to pay) and carry vega-compression risk. Three rules for the new regime: (1) **be vega-hedged** — debit spreads; (2) **have a directional bias** — the worst idea in high vol is a range-selling iron condor; (3) **respect that elevated short-term IV is arguably fair**: the S&P had moved **100 points in two hours**, so 30%+ short-dated implieds simply price reality. Ceresna put $2 into a **same-day-expiry (Feb 9) SPY call as a directional entry vehicle** and the stock swung $8 within two hours — the option "was not the wrong price." Same logic for Apple: after 180 → 150 in two weeks, a two-week option pricing a retrace to 165–170 is worth $3, not $0.50.

**Skew as a strategy map.** A stock's "average" implied (Apple 20%) hides the structure: OTM puts at ~30% vol, OTM calls at ~10% — the skew shows where the herd's hedging demand sits. **U-shaped skews** (gold; also TLT, long treasuries) mean both wings carry rich premium — collars execute cleanly, and debit spreads both ways buy lower-vol and sell higher-vol. The **S&P's fat-left-tail skew** in a post-shock market makes downside insurance uber-expensive outright — so short the next leg via **put debit spreads** (collect the inflated vol on the short put), while the cheap right wing favors simply **buying calls** for upside (a bull call spread only to mute vega against a vol-compressing rally). The TLT U-shape, plus the macro case, was the stated reason for excitement about the **TLT buy-on-dip**.

---

# Part VI — Platforms and Tools

<!-- Sources: 2021-05-25TradingViewTutorial; Interactive Broker Tutorial - Basic; Interactive Broker Tutorial - Advanced; Interactive Brokers - Option Tools Tutorial; Investing Smarter_ Pitfalls of Stop Loss Orders -->

## 1. TradingView: Chart Setup and Daily Workflow

<!-- Source: 2021-05-25TradingViewTutorial (1080p with 23fps).transcript.md (Patrick Ceresna with Massil) -->

Big Picture Trading charts in TradingView and executes in Interactive Brokers. Ceresna's style is deliberately narrow — one candle chart, Fibonacci drawn a specific way, a favorites hotlist — while Massil mapped the wider platform. What follows is the practical workflow as taught.

### Chart layouts, saving, and theme

- **New chart layout** (center dropdown) starts a generic chart labeled "unnamed"; rename and save it. Saved layouts toggle from the same dropdown.
- **Turn autosave on** — every change then saves automatically; with it off you save manually (the only way to discard changes).
- **Dark/light theme**: right-click the chart → Color Theme.
- Any template resets to factory defaults from chart settings ("restart from ground zero").

### Chart properties: candles, status line, scales, events

Opened with the wheel-shaped **chart properties** icon.

- **Symbol tab**: candle body colors (Ceresna: deep green/deep red instead of default neon), **black borders and wicks**, and uncheck the horizontal **close-price line** — "some people like that; I don't."
- **Status line**: description vs. ticker, open-market status, OHLC values — how much the top line carries.
- **Scales/appearance**: price-scale labels, date format; pre/post-market session dividers (not applicable to S&P futures, which have no pre/post sessions).
- **Trading tab**: only matters if you link a live brokerage. Stated limitation: **Interactive Brokers cannot connect** to TradingView — only MetaTrader-compatible platforms can.
- **Events tab**: **D** (dividend) and **E** (earnings) markers under the bars, plus optional "earnings breaks" (red lines showing each report's reaction). Ceresna calls the breaks overkill — D/E markers suffice.

### Symbol search, timeframes, and chart types

- Enter a symbol via the ticker box **or just start typing** over the chart. Search filters by **market type** — essential for ambiguous tickers: "GE" is both General Electric (stocks) and the eurodollar future (futures); filter to stocks / futures / forex / CFDs / crypto.
- The symbol box accepts **arithmetic** — add, divide, or multiply tickers to chart spreads and ratios.
- **Timeframes**: star favorites for the toolbar (Ceresna: 1h, 4h, D, W). Everything from 1-second to monthly plus custom ranges; some gated by tier.
- **Chart style**: candles are the default; Heikin Ashi, Renko, and point-and-figure (X/O box sizing) sit in the same dropdown — masters-program material.

### Compare, indicators, and indicator settings

- **Compare** overlays other securities and auto-switches the axis to **percentage gain from a zero baseline** — overlay Alphabet, Apple, Facebook against Microsoft and relative performance is immediate (session example: Google the outperformer, Apple the laggard). Remove with the X; the chart reverts to price when the last overlay goes.
- **Indicators dialog**: star favorites for one-click access (Ceresna's: distance from moving average, MACD, momentum, SMA, EMA). **Volume Profile (volume by price)** lives here and needs a paid tier — a technical-masters staple.
- **Built-ins vs. community scripts**: all standard TA ships built-in; user-programmed indicators appear as add-ins.
- Adding the same indicator repeatedly stacks copies in new colors; each copy's gear sets its own **period** (example stack: 10/20/50/200), **source** (default close), **style** (color, thickness, transparency, optional offset), and **save as default** so future copies keep that look.
- **Indicator timeframe**: pin an indicator to a timeframe other than the chart's — e.g., a *daily* 50-period MA while viewing the *weekly* chart. Default is "same as chart."
- Remove any indicator via the X on its legend line.

### Alerts: on indicators and on price

- **Alert on an indicator**: hover the legend → three-dot menu → Add Alert. Conditions: crossing up/down, less-than, entering/exiting a channel. Delivery: **app notification** (phone), pop-up, or **email**. **Name the alert** so the notification is self-explanatory — the taught example: "commodity trend bear crossover" for the tactical portfolio's 40/50-DMA signal (Part V, Section 6).
- **Alert on price**: the Alerts dialog. The taught pattern is the **channel alert**: "exiting channel" with upper/lower bounds (e.g., Microsoft above 255 or below 245) catches breakouts and breakdowns; "entering channel" flags price reaching a Fibonacci or profit-taking zone. Fire once or every time. The channel box draws on the chart and can be **dragged to new levels and confirmed** as zones move.
- Active alerts and trigger history log under the **alarm-clock panel** (right side); old alerts are deletable there.
- Alert counts are tier-limited (below).

### The financials tab: charting fundamentals

Financials plots **fundamental data as a chart series** against price: market cap (Microsoft approaching $2 trillion), P/E, price-to-book, EV/beta — essentially any income-statement, balance-sheet, or cash-flow field. Worked read: Microsoft's P/E ~34 at recording vs. as low as 23 at the 2000 crash. With Compare overlays, ratios can be compared across the compared names too. Ceresna's admission: he under-uses it, but any fundamental anchor can be charted over full history.

### Indicator templates and Ceresna's saved presets

Save any indicator set as an **indicator template** (Templates → Save Indicator Template, name it — e.g., "9 MA with MACD"); templates sit alphabetically in the dropdown, apply in one click, and are deletable. His two working presets:

1. **50 and 200-day EMA** — his constant reference pair.
2. **40 and 50-day DMA crossover** — pre-saved because this crossover *is* the tactical commodity-trend signal.

Division of labor: chart appearance lives in the chart layout; indicators and financial ratios live in indicator templates.

### Bar replay, multi-chart layouts, and top-bar utilities

- **Bar Replay**: pick a start date; the chart truncates there; play advances candle by candle at chosen speed through the *actual* subsequent price action. Ceresna's use is psychological — rehearse holding a breakout day by day and audit your own reactions without risk.
- **Select layout**: multi-chart grids (2 charts on Pro, up to 8 on Premium). The taught example is the **macro dashboard**: S&P e-minis, Nasdaq, dollar index, euro, Bitcoin, crude, gold, treasury bonds — one page, quick macro read. Each panel takes its own symbol/timeframe; scroll-zoom resizes; save and the grid reopens identically.
- **Camera button** screenshots the chart; **Publish** pushes an annotated chart to the community; **undo/redo** recovers deletions.

### Drawing tools and saved defaults

- **Cursor selector**: crosshair, dot, or plain arrow (Ceresna: plain arrow). Adjacent **eraser** deletes whatever you click.
- **Trend-line family**: angled lines, horizontal/vertical lines, arrows, rays and extensions. **Star favorites** and they appear on a floating quick-access bar (his: trend line, arrow, ABCD zigzag, ghost feed, circle, rectangle, Fibonacci retracement).
- **Editing**: click a drawing (endpoints appear), **double-click** for settings — text, style, color, thickness — and **save as default** so every future trend line or Fibonacci draws your way. This is how Ceresna's non-default Fibonacci styling (his colors, extended right only, never left) is replicated.
- **Info line**: a trend line can display bar count, angle, and price distance of the move it spans.
- **Advanced geometry**: pitchforks, Gann lines and boxes; Ceresna's core tools stay the **Fibonacci retracement and extension**, occasionally **Fibonacci time extensions**.
- **Housekeeping**: right-click empty space → **Remove drawings** wipes everything; the **lock** control freezes drawings so panning doesn't drag them (unlock to edit/delete).
- **Also available**: rectangles, circles, arcs, text, notes, callouts, arrow marks, a **head-and-shoulders overlay** fitted to price, and the **Elliott corrective wave** — the ABC zigzag used to illustrate corrections.

### Analysis drawings: risk/reward, forecast, ghost feed, bar patterns, ruler

- **Long/short position tool**: plots entry/stop/target and prints the **risk/reward ratio** (example: 3.5). This is Ceresna's visual definition of "a stock has run too far" (Deutsche Bank example): when remaining upside vs. downside risk is only marginally favorable, the trade is one mean-reverting correction from a bad payoff.
- **Forecast**: project a price change over a stated number of days — built for options traders to verify **they bought enough time**.
- **Ghost feed**: draw a projected replica of the chart's future path.
- **Bar patterns**: capture a real history segment and project a mirrored/repeated copy forward — e.g., lay the December correction pattern out to reason Deutsche Bank could pull back toward $14 before rolling higher. The ABC variant computes the first extension of the second leg after a retracement.
- **Ruler/measure**: prints bar count, point change, and percentage — example: Bitcoin down 49% in 11 days.
- **Icons/stamps**: novelty markers (the running joke: an airplane or space shuttle on a Bitcoin chart at vacation prices).

### Watchlists and the right-side panels

- **Watchlist groups**: subcategory lists — Canadian stocks, energy, all gold miners, the full S&P 500, an S&P 100, imported "fallen angel" and event-monitor lists. Newer builds support **section headers inside a list** (right-click → add section): the tactical-portfolio list splits into equities, income bonds, precious-metals trend following.
- **Colored flags** categorize: the **green list** is the breakout-trade watchlist (Electronic Arts, Microsoft, etc.); eye-catching names mid-scan get flagged to a **red list** to revisit.
- **Rapid-fire scanning**: click the first symbol and step through every chart with the spacebar or down-arrow — the workflow for sweeping the S&P 100.
- **Top-down method**: macro landscape first, then sectors, then stocks within sectors; a scan yields a 10–15-name short list, of which one or two get published.
- **Import/export**: lists import/export from CSV or text — load all 500 S&P names at once.
- **Details pane**: shrink the panel and select a ticker for company name, sector (MicroStrategy: technology — internet software/services), daily range, volume, market cap, dividend yield, earnings beat/miss history, income, and a short business write-up.
- **Right-side panel stack**: alert log, per-symbol **news**, **data window** (header statistics in one box), **hot lists** (biggest percentage movers per exchange), **calendar** (economic events on top, earnings below), and **My Ideas** — save an annotated chart with notes, shareable publicly.

### Subscription tiers: what you actually need

Free basic plan; Pro and Premium add capacity: roughly **5 indicators per chart** on entry tiers up to **25** at the top; **2 charts per layout** (Pro) up to **8** (Premium); **server-side alerts** from ~10 through 40 and **400** by tier; **volume profile** arrives with Pro. Real-time data for some markets carries separate exchange fees — the plan-comparison page has the matrix. Ceresna's honest sizing: he runs Premium because he broadcasts for a living, but "I could probably make all my trades the same way with the basic package" — Pro is the practical floor for volume profile and multi-chart layouts. His verdict: no other charting service compares — accept no substitute.

## 2. Interactive Brokers: Platform Essentials

<!-- Sources: Interactive Broker Tutorial - Basic.mp4 (720p with 23fps).transcript.md; Interactive Broker Tutorial - Advanced.mp4 (720p with 25fps).transcript.md (both presented by Massil) -->

BPT charts in TradingView and executes in **IBKR Trader Workstation (TWS)**, Classic view — the layout seen in the morning "Where's the Trade" webinars. Massil teaches it in three passes: basic functionality, advanced layout tools, and (next section) the option tools.

### Account opening and the web portal

- At account opening, **declare prior options experience** — that you have traded options and have good or extensive knowledge — or IBKR will not approve options trading.
- The **web portal** shows portfolio performance over time (percent or dollars); **net liquidity** (account value if everything were liquidated); positions with market value, average price, unrealized P&L; **allocation by asset class, sector, and industry** (a balance check for long-term portfolios); **Transfer & Pay** for deposits/withdrawals and for **transferring positions in from other brokers with average cost basis intact** (no sell/rebuy); and **Performance & Reports** for tax documents, statements, custom reports. Trading from the web is possible but not recommended.

### TWS: Mosaic vs. Classic

First login offers two defaults. **Mosaic**: order-entry tab, chart panel, news, order/trade activity, with a linked monitor — "day traders like to have that window open at all times"; stepping down the watchlist with the down-arrow drives the linked chart and order ticket. **Classic TWS**: the BPT standard — charts live in TradingView, so Classic provides the account window, quote monitors, and option tools.

### The Account tab: balances, margin, and the liquidation ladder

- **Net liquidation value** — what everything would fetch if sold now.
- **Equity with loan value** — margin account: total cash plus loan value of holdings. Cash account: only **settled cash** shows.
- **Cash / settled cash** — actually available to invest.
- **Initial margin requirement** — required to *open* new positions.
- **Maintenance margin requirement** — required to *keep* positions without forced liquidation.
- **Available funds** — equity with loan value minus initial margin; the tradeable number.
- **Excess liquidity** — the margin cushion before liquidation. The number to watch: it **turns yellow** below roughly a 10% cushion (act: deposit or close positions) and **red** at/below zero — then IBKR will **liquidate positions for you** if you do not act, with email warnings en route.
- **Buying power** — moves position by position because margin rates are set per stock (broker/regulators). Taught examples: a 30%-margin stock costs $30 of capital per $100 of stock; a 75%-margin name (the "riskier blockchain miner" vs. "safe Apple" contrast) requires $75 per $100.

### Currency conversion through FX Trader

A Canadian trading US equities converts CAD→USD (reverse for a US investor buying Canadian names). Path: search the currency → **Forex → IDEALPRO** → accept the prompt to open the **FX Trader** → **slide the pair** onto an order line → buy USD/sell CAD with limit or market order and a size (worked example: $25,000). Per-currency balances show on the account tab. Owned positions can be **dragged from the account window onto whichever page** they belong to.

### Placing and closing equity orders

- Enter the ticker, pick the exchange (Apple on NASDAQ), pick **Stock**, Buy or Sell.
- Order types taught: **limit** (typed or adjusted on the price ladder — example: 50 shares at a $149.49 limit), **market** (prevailing price), **mid** (bid/ask midpoint), **Day** (cancels unfilled at day-end), **GTC** (live until filled at the limit or canceled).
- Holding a position adds a **Close** button that pre-fills size and a limit exit; edit the quantity to sell less.
- Option positions add a **Roll** button — the mechanism behind "watching Patrick roll the SLV income": carry the position forward a week in one action instead of close/reopen.
- Standing rule: for options, **always use limit orders** — market orders give away pricing.

### Option chains and OptionTrader settings

- From a ticker, open derivatives → Options: the chain shows implied volatility per expiry and strikes both sides, color-coded — **blue = in the money, black/dark = out of the money** (calls and puts alike).
- **OptionTrader** (top navigation bar) shows the same chain in the trading panel. Two settings encode real rules:
  - **Expiries**: only monthlies show by default. Click **More** and enable **weeklies and quarterlies** — the less-traded near expiries the income strategies use.
  - **Strikes**: new accounts default to ~10 strikes (~5 per side). Massil's setting: **All**, or a custom 20–25.
- Clicking any option loads it onto an order line for a limit order.

### Building multi-leg strategies: separate legs vs. Strategy Builder

- **Leg by leg** (Apple May 155/160 bull call spread): buy the 155 call, sell the 160 call as two tickets with separate limits, units matched, transmit both. Advantage: **tactical flexibility** — roll the short strike or take profit on the long leg independently.
- **Strategy Builder** (OptionTrader → Trading → Strategy Builder): add each leg, set side and ratio (the builder assumes long both strikes — flip the short leg), **add to quote panel**, drag the combined instrument onto a TWS page; the 155/160 spread prices ~$2.29 as one ticket. Advantage: **one trade, lower commissions** — but the structure is locked; both legs open and close together.
- Ratio example via the builder (CVS ~$97.98, May 13): sell one 100 call, buy three 103 calls — a **3:1 ratio call spread** — openable for a small credit (~$0.20), starting near zero P&L, making money exponentially above the upper strike, the three long calls funded by the short lower strike.

### Pages, group headers, and column layouts

- **Pages** (tabs across Classic TWS): one per strategy sleeve via **+** — BPT's set: breakout trades, options for income, long-term options, commodity cycles.
- **Group headers**: right-click a row → create group header ("Long-term options", "Commodity cycles") with sub-headers (energy plays, precious metals, technology). File existing positions by dragging from the Account window's positions list (Cameco under energy; gold names under precious metals).
- **Column layouts**: rebuild Ceresna's set from the category tree — **Financial Instrument**; **Bid/Ask** (sizes optional); **Change %**; from Position & P&L: **Position, Average Price, Cost Basis, Market Value, Unrealized P&L**; from Greeks: **Delta, Delta Dollars**; **Dividend Yield**; **Implied Volatility**. The full tree is enormous (futures, bonds, fundamentals like EBITDA and P/E), so separate layouts per purpose are encouraged. Internal logic: position × average price = market value; cost basis vs. market value = unrealized P&L. Hover a header to insert/remove; drag to reorder; Apply/OK.

### A custom linked workspace (advanced layout)

- New page via **+**; a **green overlay** means edit mode; the **green padlock** (top right) locks and saves the layout — the closing rule: "this is what I want to wake up to every single morning." Unlock to modify.
- Add windows from **New Window**: a **Quote Monitor** (header group "BPT positions/watchlist" — Amazon, Apple, Mosaic, Nutrien, EA, CVS, TSX names), an **Option Chain** beside it, **Volatility Over Time** under the chain, a chart.
- Option-chain panel settings mirror OptionTrader's rules: prefer **Tab view** (expiries as tabs) over List view (one long scroll); strikes custom 20–25 or All; add **Delta** and **Implied Volatility** columns to the chain itself (hover a header → insert/remove).
- **Group windows (green chain icon)**: every linkable window shows a chain glyph; a missing/broken chain means that panel won't follow. Fix: window dropdown → Group → assign the same group number. Then walking the quote monitor flips chain, volatility panels, and chart together; clicking one strike updates strike-specific panels. This linkage is "the magic" of the custom page.
- Other windows: **Portfolio** (open positions, P&L, cash by currency — for low-position-count investors) and the **Watchlist** tool (dense ~18-ticker grid with last/change that also feeds the event calendar's filtering).

### Scanner, fundamental explorer, and calendars

- **Advanced Market Scanner** (Scanners → General Tools): instrument (global/US stocks, bonds), location (e.g., NYSE only, excluding NASDAQ/ARCA/AMEX), then stacked **filters** — ESG, fundamentals, technicals, option metrics, volume, price. Taught build: US stocks **below their 100-day EMA** (threshold 0%) **with volume over $500 million** — a first attempt at $50 billion returned nothing (size the floor sanely); $500M gave a short list (Duke Realty 5% below its 100-day EMA; Roblox 54% below). Presets: top percent gainers/losers, most active. Use case: pre-building a list that triggers when names cross a technical condition.
- **Fundamental Explorer** (Information Systems): any ticker (demo: Roblox) → company profile, key ratios, financials, analyst ratings and reports, major owners; tabs for key ratios, impact analysis, financials, news, valuation.
- **Calendars** (Information Systems): **economic calendar** (CPI prints, central banks) and **event calendar** (corporate events), navigable forward and back, filtered to **your portfolio and watchlist tickers** — never miss an event on a company you follow. (The second reason the Watchlist window matters.)
- **Analyst research** (Subscribe section): bundled/paid feeds — Benzinga, Refinitiv, Simply Wall St, Seeking Alpha articles, Stock Traders Daily, filings services.

## 3. Interactive Brokers: The Volatility Lab and the Probability Lab

<!-- Sources: Interactive Brokers - Option Tools Tutorial.mp4 (720p with 25fps).transcript.md (Massil); option-tool previews inside Interactive Broker Tutorial - Advanced.mp4 (720p with 25fps).transcript.md -->

Options are BPT's primary implementation tool, so the option tooling gets its own tutorial: the **Volatility Lab** (volatility analysis) and the **Probability Lab** (strategy scoring against implied probabilities).

### The Volatility Lab: layout and views

Open via **New Window → Advanced Option Tools → Volatility Lab**. One analysis screen, three tabs — **Implied Volatility**, **Historical Volatility**, **Industry Comparison** (everything below from the May 13, 2022 recording, Apple the workhorse at ~$150–155 after the vol spike). Operational caveat: the lab **cannot be linked** to the watchlist (no green-chain grouping — type the ticker manually) and is meant to be opened, analyzed, and closed rather than pinned; each constituent tool exists separately under the option tools and *can* be locked into a saved layout.

### The five implied-volatility windows

1. **Implied volatility (lookback)** — IV over time per selected expiry (x time, y IV; add/remove expiries via + — e.g., swap June for October and January 2024; lookback two months to a year or custom). Lessons: near-expiry IV sits low historically and **ramps into expiration**; in spring 2022's volatility even Apple's 2024 LEAPS IV was bid up. A shaded backdrop plots the underlying's actual price.
2. **Volatility profile** — implied vs. historical side by side (IV = what the market prices; HV = what was realized). Gear icon switches to **Volatility Profile Comparison**, overlaying peer IVs: Apple (white) vs. the XLK tech-sector ETF (yellow — lowest of the set), Microsoft, Twitter, Facebook (highest). Application: with a 1–3 month sector view, compare candidates and **buy the option carrying the least volatility** — less premium for the same move is a greater return.
3. **Multi-expiry skew** — the vol smile per expiration: nearer expiries steeper, longer-dated flatter and more stable across strikes (Ceresna's recurring observation). Controls: change expiries; strike window (default three standard deviations; show all; zoom to a custom 125–200); and the **as-of date** — a month back, the same expiry shows a flatter skew, isolating how skew conditions changed.
4. **Time-lapse skews** — the skew's evolution: today's curve overlaid with curves from dates you add (one month ago; a custom date like January 5). Taught use: seeing the skew change **before and after an earnings period**.
5. **Open interest** — open interest (mode-toggle to traded **volume**) per strike per expiry; gear overlays puts and calls on one line or splits them into two charts. Strike clusters read as potential magnets, support, or resistance (advanced-tutorial example: ~7,000 contracts at one $25 strike).

### Historical volatility view and industry comparison

The **Historical Volatility** tab re-houses the profile and time-lapse skew larger, with IV (white) vs. HV (orange) across a one-year span plus rolling **30-day and 150-day average** HV lines. The **Industry Comparison** tab is the expanded comparison mode: add/remove comps or type a ticker; pick the period (one week/month/year); each underlying's price top right; skews compared directly (Facebook's whole skew shifted up by its elevated vol); volatility profiles compared over time.

### The standalone option tools (from the advanced tutorial)

Every lab window also exists individually — this is how you pin them: **Option Analytics → Volatility Skew** (multi-expiry skew alone), **Volatility Over Time → Historical Volatility**, **Option Volume by Strike** — all groupable/linkable in a saved layout. Two more from the advanced tour: **Interactive Analytics** — a chain whose cells show every Greek per strike instead of prices — and the **Implied Volatility Viewer**, another skew rendering. Interpretive points: longer-dated options carry flatter, more stable skews; implied volatility tends to be **hiked into expiration** (Roblox: IV ~100 a week before the May 20 expiry, then skyrocketing — pinning uncertainty); **historical volatility is backward-looking** (realized, e.g., past 30 days), **implied forward-looking** (the vol market makers price in).

### The Probability Lab: reading the market's distribution

Open via **New Window → Option Analysis → Probability Lab**. It exploits the Black-Scholes link between a stock's price and its quoted options to display the **market-implied probability distribution** per expiry (demo: Apple, August 2022): "an 8% chance the stock finishes between 150 and 155," roughly the same for 155–160, tapering toward the wings. Far strikes carry low assigned probability — precisely why selling there earns what it does.

- **Editing the distribution**: if your view contradicts the market — the demo: a tech bounce you believe lands Apple in 165–180 — drag the bars up (e.g., raise 165–170 to ~8.5%) to build **your forecast**. Red = your distribution; blue = the market's.
- **Strategy scanner**: IBKR auto-generates candidate structures and scores them — by default on **market-implied** probabilities; switch the basis to **my forecast** to rescore against your distribution. Readouts per structure: probability of profit, maximum return, maximum loss, breakevens, full payoff chart below. The auto-picked demo — buy one Apple August-19 145 call, sell four August-19 180 calls (a 1×4) — showed 41% probability of profit, 367% maximum return, an **undefined (infinite) maximum loss**, breakevens ~150.49 and ~189.17, max profit if pinned at 180: the teaching example of high-probability structures with unbounded tail risk.

### The Probability Lab: building and scoring your own strategy

The **Strategy Adjustment / Order Entry** panel is the "playground": construct any spread strike by strike and watch it price and score live. Taught build: the house **bull call spread** — buy the 170 call, sell the 180 call (August expiry), quoted $1.35–$1.48, fill ~$1.56. Scorecard:

| Metric | Market-implied basis | Under the edited forecast |
|---|---|---|
| Probability of profit | 18% | 25% |
| Max profit | $844 | $844 |
| Max loss | $156 (defined) | $156 |
| Max return / max loss | 541% / 100% | same |
| Risk/reward | 5.41 | 5.41 |
| Breakeven at expiry | $171.56 | $171.56 |

The teaching point: risk/reward geometry is invariant to your opinion — only **probability of profit** changes. Use the market-implied read to test whether a planned structure is "too hopeful"; recognize the flip side: when your conviction genuinely contradicts the market's distribution, the low market-assigned probability is exactly what makes the payoff asymmetric if you're right.

## 4. The Pitfalls of Stop-Loss Orders — and the Options Alternative

<!-- Source: Investing Smarter_ Pitfalls of Stop Loss Orders (1080p with 30fps).transcript.md (Patrick Ceresna with Luke Jaster, director of member services; first of the "Investing Smarter" series) -->

The most complete argument in the corpus: why the retail default — the stop-loss order — fails on three structural grounds, why the two standard escapes (dollar-cost averaging, diversification) carry their own traps, and how Ceresna replaces stops with options so the same position is held with defined risk. His stated credentials: twenty years trading and a CMT in technical analysis.

### The lens: macro drives fundamentals, which manifest technically

The series motto: **"Learn how to see — realize everything connects to everything else."** Macro fundamentals are the center of the universe: they drive market conditions, which influence corporate fundamentals, which manifest technically on the charts. Single-facet specialists — chart-only technicians, CFAs dissecting only balance sheets — are "not wrong, but it's not the holistic way" (the full trinity statement is the Orientation and Part V, Section 1).

The canonical illustration: **Suncor in 2014** — every bottom-up box checked (pristine balance sheet, great management, properties, cash flows, dividend history, a beautiful technical uptrend) — and the stock still lost half its value in a downtrend, because a macro variable (oil from over $100 to $26 a barrel) changed the conditions that destroyed the fundamentals. The BPT trinity follows: **macro** (why), **technicals** (what and where), **options** (implementation). The preamble matters here because technicals earn their keep as the *implementation and management* layer — timing, targets, trade management — and technical traders overwhelmingly manage risk with **stop losses** (fundamental buy-and-holders mostly don't; heavy stop users are the leveraged and the signal-driven). Auditing the stop is auditing the standard risk layer of technical trading.

### Two premises about market behaviour

1. **Prices move on order flow and liquidity.** In an illiquid instrument, one large sell order walks the price down through levels looking for buyers — price discovery *is* that search. Even in very liquid names, short-term seller/buyer imbalances show up in price. A meaningful share of short-term price variance is **completely outside the investor's control** — the anchor for everything that follows.
2. **News flow and market responsiveness matter; markets have personalities.** Company events (earnings) and market-wide events trigger short-term volatility that can hit a stop. Identical headlines get opposite treatment across regimes: in the months before this webinar (2022), "almost every news is sold" — good or bad, the response was distribution; in **2017** there was no such thing as bad news — everything rallied, every dip was bought, a self-reinforcing positive feedback loop. Recognizing the current personality is part of position management.

### The anchor: Apple's implied-volatility math

The whole lesson anchors on one real number set — Apple (AAPL, Nasdaq), Friday close **$184.10**, implied volatility **19.7%**. Definitions: **historical volatility** looks backward (what the stock did); **implied volatility** is the market's forward anticipation, quoted annualized off ~30-day options, readable as "IV close" on any brokerage options chain.

- One-day, one-standard-deviation expected move = price × IV ÷ √(trading days/year) ≈ **$2.25**.
- Under a normal distribution (acknowledged simplification — real markets have fat tails and skew), **68% of days** see moves of $2.25 or less. May, with 23 trading days, should hold about **16 days** inside the range and about **7 tail days** beyond.
- Monthly scale: 1σ ≈ **$10.55** → a 68% band of **$173.55–$194.65**, ~16% probability below the floor, ~16% above.

Nobody knows what Apple will do; this is only what buyers and sellers collectively imply. But it is the objective yardstick any stop placement must be judged against. Remember: **$2.25 a day, $10.55 a month.**

### Pitfall 1: your stop lives inside normal volatility

Buy at $184.10, place a "responsible" stop at **$175** on some technical metric. Apple drifts down over three weeks, tags $175, knocks you out — then reverses to your target. The verdict from the math: the $184→$175 move **was not an outlier** — it sits inside the market-implied one-standard-deviation range (the monthly band's floor was $173.55). The stop sat at an **emotional pain point** — "the amount I'm not willing to lose" — an arbitrary price. Ceresna's phrasing: *"We're just asking and inviting the market to come and take our money from us."* Corollary: the shorter your timeframe (day trading, intraday swings), the tighter your range, and the likelier ordinary order-flow noise tags the stop before the real move. "You think you are doing right by yourself by using stops... but in the end, the placement of the stop was not really logical at all."

### Pitfall 2: gap slippage — a stop is a trigger, not a price

A **gap** is price jumping between levels without trading through them — $50 at one close, $55 on the next morning's first print. A stop-loss order is **not a guaranteed price; it is a trigger price** — once triggered, the broker liquidates **at the best available price**, which in a fast market can be far through your level.

The Apple continuation: bought at $184.10, stop at $175 in your head — "my risk is $9.10." The stock dips to $176 (no trigger), recovers to $180–182, then an event lands over a weekend. The absurd taught example — Tim Cook hit by a bus — gives way to the realistic ones: a presidential tweet alleging Apple is too big a monopoly and threatening regulation (algorithms react instantly), or an earnings shock. Monday the stock **opens at $169**: it never traded $175; the order fills at the best bid, $169 — and hesitation means $167, then $163. Believed maximum loss: $9. Actual: **$15 and climbing**. Gap slippage means stop-loss risk includes losses *larger than designed*, precisely at the event horizons where stops are most relied upon.

### Pitfall 3: stop clustering and the pain point

Technical traders converge on the *same* toolkit — previous lows, popular moving averages — so everyone's "support" and everyone's stops pile into one zone. In the Apple example: the previous low at **$164.47**, the 200-day moving average at **$163.43** — an overlapping cluster of resting sell stops just below. That is exactly where price went: Apple temporarily broke to a lower low *and* through its 200-day, tripping the whole cluster and forcing everyone out **at the worst possible spot**, before reversing.

On "stop hunting": Ceresna once resented the image of sophisticated players gunning for retail stops; his mature reframe is personal responsibility — *"It's my responsibility not to put my stop loss in a stupid spot."* The mechanism is structural, not conspiratorial, and he cites his MacroVoices interview with commodity trader **Eric Peters**: **"The market always seeks to discover the pain point — the point where the liquidity is."** A cluster of stops *is* liquidity; price is drawn to it. Meanwhile the average investor learned from a book or a YouTube guru that "you're not a trader unless you put stops" — with no context for *where* — and thereby positions too tight, in the wrong areas, leaving the trade a worse long-run chance of working than no stop discipline at all.

### Escape route 1: dollar-cost averaging

The natural response — "stops are a fool's game, I'll just buy and hold" — leads to the retail favorite: averaging down. Taught example: Apple at $184.10 falls $24 to $160; buy double the shares; 100 at $184 plus 100 at $160 averages about **$172.05**, so breakeven is $172 rather than $184. On a genuine blue chip it feels airtight. The dissected assumptions:

- **The emotional core**: it is human nature to refuse to admit a mistake. Rather than cut the loss, the averaging-down investor *gambles* — **doubling the risk to fix the original error**. Sometimes it pays; everyone has such a story.
- **Assumption 1 — the price you paid was "right" and the stock must return to it.** Bitcoin counterexample: it traded $18,000–19,000 at the end of the year, then fell to $10,000. Averaging down at $10,000 needs only ~$14,000 to break even — *if* $18,000 was the right price. "What if the intrinsic value is actually zero?" (explicitly not his forecast — a boundary case exposing the assumption). The position can go $10,000 → $5,000 → $2,000, and the averager has converted a small, manageable loss into **good money thrown after bad** — a monstrosity of risk in a position they refuse to sell.
- **The General Electric warning**: a stock *everyone* considered blue chip bled from the $20s–$30s down to $12 — roughly half its value — and anyone averaging down the whole way absorbed enormous losses on the premise that "GE has always been great."
- DCA "has its shortcomings, and we just have to accept that to be true" — sometimes it works, but as a *system* it embeds the doubling-down failure mode. (The commodity-cycle version of this warning — never average down through a resource bear — is Part IV, Section 8.)

### Escape route 2: diversification

The other modern-portfolio-theory foundation: spread positions so no single company event hurts. The taught image: a miner's operation floods and the stock halves — concentrated, that's devastation; across many holdings, noise. Genuinely the core MPT mechanism for removing **unsystematic, company-specific risk**. But two shortcomings, as stated:

- **Diversification dilutes returns.** Hold 30, 40, 50+ uncorrelated things and no single winner moves the portfolio; one position's gain is cancelled by another's decline. Return ends up depending on the whole market's tide — "you're not going to make it from any special positioning in any one of the stocks."
- **Diversification is a full-time job.** Managing targets, profits, losses, and replacements across dozens of positions overwhelms individual investors — the honest justification for outsourcing money management.

Both escapes fail on inspection — and here Ceresna positions his method as deliberately unorthodox: *"If you manage your money the same way everyone else does, then it's almost impossible to create alpha."* The industry's default rulebook is itself the alpha-killer.

### The professional alternative: puts as trade insurance

How does a professional run a large, concentrated, high-conviction position without stops, without averaging-down discipline, and without 50-position diversification? **Options — specifically, buying puts as insurance on equity owned.**

### Options in one lesson: the two car/truck analogies

An option is a **contract between two counterparties** (both can be retail — no market maker required): the **buyer holds a right**; the **seller took a premium and undertakes an obligation**.

- **Call option** — the right (not obligation) to *buy* at a fixed price for a fixed period. The truck example (Part II, Section 1) in this session's telling: Patrick offers his truck at $20,000; Luke knows Auto Trader shows comparables at $30,000, so instead of paying outright he pays **$500 for a one-month right to buy at $20,000**. Patrick gets $500 either way and holds the truck a month; Luke gets a month to flip. He finds a buyer at $24,000, exercises, nets $4,000 minus the $500 premium = **$3,500**. If the truck proves a lemon worth $15,000, Luke walks away losing only the $500 — the right was his; the obligation sat with Patrick.
- **Put option** — the reciprocal: the right to *sell* at a fixed price for a fixed period. It **acts as an insurance policy**. Car insurance *is* a put: you (premium payer) are the buyer; the insurer underwrites the obligation; the car's value is the underlying; total the car and the insurer buys the clunker for replacement value. "You're buying a put option on your vehicle." The same structure insures a stock's downside. Though puts are famous as crash speculation, this method uses them **as protection on positions owned**.

### The Apple insurance trade, step by step

The centerpiece is a **live trade from Ceresna's account**, first shown on an April 6 webinar and carried through this session. Resize freely: 100 shares instead of 2,000 scales every number by twenty.

1. **Entry with insurance from day one.** 2,000 shares at **$173.37** (~$346,000). Days later the stock is down $4.31 at $168.49 and the position ~$10,000 underwater — shown *live* on the April 6 webinar alongside the fix: he held an **April 13-expiry, $172.50-strike put costing $2.38/share (~$4,760)** — a guaranteed right to sell every share at $172.50 no matter where the stock traded. Insurance ≈ 1.4% of the position for two weeks of total downside removal.
2. **Rally — roll the insurance up to lock profit.** Apple climbs ~7–8 days to $177–178. The April put expires unused ($2.38 sunk — "like car insurance you didn't need"). He immediately buys a new two-week put at the **$177.50 strike for ~$2** — now the *profit* is guaranteed: ~$4+ of capital gains locked against ~$4 of cumulative insurance.
3. **The crash that would have stopped everyone out.** A supplier disappoints on earnings, the Street assumes iPhone X disappointment, and Apple drops **$15+ in four sessions, $178 to ~$162**. No panic required — the guaranteed $177.50 sale price carries **none of the three stop-loss pitfalls**: no volatility stop-out, no gap slippage. Instead of selling stock, he **monetizes the insurance**: sells the put, extracting its **$15 of intrinsic value** ($177.50 right vs. $162 price). Arithmetic: $2 + $2 premiums paid, $15 collected → **net +$11 on the insurance**; against the $173 entry, adjusted cost base **$162 — exactly where the stock trades**. The entire drawdown cost nothing.
4. **Re-insure lower.** A new put into the first week of May, **$160 strike, ~$2**. Honest risk accounting: adjusted base $162, insurance at $160 → ~$2 capital at risk plus ~$2 premium = **~$4/share, ~$8,000 on 2,000 shares** — the trade's maximum pain point (~$400 scaled to 100 shares).
5. **Risk-free into earnings.** Days before the report the stock recovers from $160 to **$168 an hour before the close** — ~$6 of gains over the $162 base. He pays ~$3 (elevated event vol) for a **$167.50-strike put**: gains locked, and the position enters the announcement **unable to lose anything while keeping all upside**. Process point: you cannot *start* a trade risk-free — you engineer it there by staging insurance as gains accrue.
6. **The gap up — add size, not anxiety.** Apple beats and **gaps to $175** (the event gap now works *for* the insured holder — the same force that inflicts gap slippage on stop users). He buys **another 2,000 shares** and immediately hedges all **4,000 shares** with a $172.50 put. "All of my profits were paying for all the puts."
7. **The melt-up.** News that **Warren Buffett is buying huge stakes of Apple** rockets the stock to **$184**; he closes puts on the way up and carries a fresh **$180-strike put costing $1.52 (~$6,000)** into the following week. At Friday's close: up **$44,000** on the equity, average cost showing $173, and — thanks to the $15 monetization — actually **ahead net on all insurance bought and sold**. One week of guaranteed-sale protection on 4,000 shares for $6,000, downside fully insured, upside 100% intact.
8. **The asymmetry tally.** If Apple reaches $200 in the following weeks, the position makes **~$100,000** (explicitly a scenario, not a forecast). The worst the trade *ever* could have cost, at its maximum-pain moment, was ~**$8,000**. His summary: there is no holy grail and insurance is a real recurring cost — but a trade risking $8,000 to potentially make $100,000 **is the definition of asymmetric**, and creating asymmetry is the actual job.

### What the method buys you: asymmetry, emotion, conviction

1. **Asymmetry** — a defined, pre-paid worst case against open-ended upside (the $8,000 / $100,000 structure).
2. **Emotional control** — uncertainty is what triggers the get-out/get-in churn that makes investors their own worst enemy; a guaranteed sale price removes the trigger. The insurance doesn't just cap losses — it prevents the emotion-driven trades that stops and unprotected drawdowns provoke.
3. **Conviction and size** — under a stop-and-diversify regime the same idea would have been 300–400 shares, sized down so stop noise couldn't hurt. Managing risk through options let him hold **4,000 shares** — real size, real conviction, real money from the same idea.

---

# Appendix: Key Rules and Parameters

<!-- Consolidated from the quick-reference sections of all eight digests; duplicates merged. -->

## Money, macro and portfolio allocation

| Area | Rule / framework | Parameters |
|---|---|---|
| Modern money | Where money comes from | <3% physical cash; ~97% bank credit created as deposits against reserves; governments neither control money supply nor its allocation |
| Inflation/deflation | Ceresna's tell | Watch the gap between credit growth and money-supply growth; credit outrunning money = deflationary risk |
| Bretton Woods | 1944 architecture | Dollar (gold-backed) = world reserve currency; IMF + World Bank created; Bancor rejected; US dismantled British imperial preference; Nixon shock 1971 ended convertibility |
| Eurodollar | Definition | Offshore + wholesale interbank dollar liabilities; source = "the bookkeeper's pen"; Bretton Woods functionally defaulted 1960 (Snider) |
| Basel buckets | Capital ratios | 100/50/20/0 risk weights at 8% capital; CDS guarantees drop buckets; gross notional stays off balance sheet |
| Shadow system size | BIS Oct 2009 | Offshore bank claims $10T (2000) → $34T (end-2007) |
| Dalio | Three forces / deleveraging | Productivity growth; cycles of 5–8 and 75–100 years; four levers (austerity, defaults/restructuring, redistribution, printing); beautiful deleveraging = income growth > interest rate with inflation contained |
| Dragon allocation | Cole's optimum | 24% equity / 18% fixed income / 21% long vol / 18% commodity trend / 19% gold; 21% vol = delta-dollar exposure of a fund, not cash into options |
| Dragon retail build | $100k version | 30% SPY (100 sh), 20% GLD (120 sh), ~19% IVOL (400 sh) + BND (100 sh), trend sleeves short/long via 40/50-day EMA crossover (DJP/USO commodities ~10%, FXE currency ~20% — vol-adjusted), ~20% cash; static sleeves rebalanced quarterly, timing sleeves rules-based |
| Long vol overlays (Dragon) | Per 100 SPY shares | 1x2 SPY put backspread at ~zero cost; up to 5x10 VIX call backspread (~30x40, ~$200 debit); target ~$20k delta-dollar vol exposure per $100k; roll quarterly; never hold backspreads to expiry; monetize on extraordinary moves (S&P −500 to −1,000 pts, VIX 50–60) |
| Tactical portfolio (Feb 2021) | Weights | Equity 25% (RSP/URTH/EEM; never timed) · Income up to 20% (IVOL 5, REM 3, AMLP 3, put-write deferred) · Gold/silver 15% static, to 25% in trend · Commodity trend 5% uranium + 5% GNR on a 40/50-day EMA crossover · Long vol up to 25%: SPY calendared straddle, GLD 200/250 call spread ($3 for $50), TLT 10×5 call backspread (~0 cost, deflation insurance). Review weekly; rebalance, don't trade, the long-term sleeves |

## Option contract mechanics

- **Contract**: buyer = right, seller = obligation; premium paid up front; strike and expiry fixed at inception; 1 contract = 100 shares (equity/ETF); quotes always per share (×100 for dollars). Exceptions: CL crude options = 1,000 barrels; gold futures options = 100 oz; TSX 60 index = 10.
- **Exercise styles**: American = exercise any time, physical delivery (SPY; early-assignment risk for writers); European = exercise only at expiry, cash settlement (SPX and index/vol options; Buffett's $4.9B/$37B-notional index puts). European ≠ illiquid — you can always trade in and out; you cannot early-exercise.
- **Expiries**: front + next month always exist (third-Friday monthlies); one quarterly cycle per stock (JAJO / FMAN / MJSD); ~5 weeks of weeklies on liquid names (SPY: Mon/Wed/Fri); LEAPS mostly January (US)/March (Canada), new series listed ~August when the front January falls under 6 months; long-dated out to a decade on some indices (Euro Stoxx 50 to 2027), five years on crude.
- **Volume ≠ liquidity**; open interest = contracts in existence (SPY example: ~762,000 contracts at one strike). Order flow: buy/sell to open; buy/sell to close.
- **Fills**: land mid-spread around the theoretical price; spreads widen in fast markets; liquidity matters in proportion to trading horizon; always use limit orders for options.

## Pricing and value decomposition

- **Six inputs**: stock price, strike, time, rates, dividends, volatility. Vol is the only market-controlled input: **volatility is the adjustment for risk**. Black-Scholes family; dealers tweak for American exercise.
- **Value split**: call intrinsic = max(stock − strike, 0); put intrinsic = max(strike − stock, 0); time value = premium − intrinsic; time value → 0 by expiry (exponentially accelerating); intrinsic is an equity stake that only moves with delta. Never call a 10-cent option "cheap" — it's priced ~95% to expire worthless.
- **Dividends**: discounted forward; calls cheaper, puts richer by ≈ the dividend; put sellers are synthetically paid the dividend.
- **Rates**: negligible for 30–90 day options at low rates; dominant for long-dated (Euro Stoxx 2027 strikes behave like a 10-year bond on rate moves).
- **One SD ≈ 68% probability**; IV → range via square root of time (20% IV on $100 = $80–120/yr; Apple $184.10 at 19.7% IV → ±$2.25/day, ±$10.55/month).

## Volatility

- HV = realized past; IV = market's forward vote; ±1 SD ≈ 68.2%, ~16% per tail; equity index = fat left tail, gold = right tail (details in Part IV).
- VIX = 30-day ATM implied on S&P; vol up = market down (and vice versa).
- **Regime playbook**: low IV → outright calls/puts, straddles/strangles; high IV → debit spreads (his favorite), directional butterflies/condors (mind multi-leg spread widening in crashes). Sell high IV, harvest contraction; expansion is the writer's enemy.
- Regime events: IV ramps into earnings/expiry then collapses to the baseline (Walmart: May IV 40% → 70% into the print, all series back to ~20–22% after). Elevated short-dated IV after a shock can be fair pricing.

## Time

- Decay non-linear; accelerates in the final 3 months/month/week; clearest on ATM options.
- **~sqrt(time) premium scaling**: 4-day SPY option $0.80, 32-day $2.44, 60-day $3.60; 60-day loses ~$1.15 in a month vs the 32-day's full $2.44.
- 45-day theta-harvest sweet spot is the common rule; Ceresna prefers 2–3+ month (or longer) writes — in his vocabulary two to three *weeks* is short-term.
- Deep-ITM ≈ stock (tiny residual time value); short-dated ATM = "Greeks on crack."

## Greeks

- **Delta** = $ change per $1 of stock (0.53 example: $2.32 → $2.85 on +$1). Bands: low <33, mid 33–66, high >66; high delta = synthetic stock; delta-1.00 = fully synthetic market.
- **Gamma** = rate of change of delta (higher short-dated; delta-1 = zero gamma; buy short-dated protection so gamma explodes in your favor; dealer/complex short gamma is the crash accelerant).
- **Vega** = $ per 1 IV point ($2.06/35%/6¢ example; $2.88 +$0.11 per vol point); long straddle = synthetic long vega; sellers want high IV + contraction.
- **Theta** = 1-day carry ($2.06 → $2.02 at 4¢ theta) — the writer's positive carry; spreads pay theta on the net difference only.
- **Rho** = rate sensitivity; matters only long-dated (Euro Stoxx 10-year puts at zero rates vs normalization to 2%). No Greek exists for dividends.

## Income and writing

- **Never mix the three methodologies**: breakout (2–6 weeks, technical), hedged position (6 months–years, macro), income (theta).
- **Income rules**: only sell puts on stocks you'll own; hedge long-dated writes with cheap short/medium-dated puts (Exxon: $3 collected / $0.20–0.27 hedged; J&J: naked Jan 110s + ATM April protection at $0.45, rolled to 115 for ~$0.20); the hedge protects the move *through* the strike, not to it; harvest seasonally — hardest in bear markets, easiest coming out of them; size by stock obligation or by modeled crash loss (~$240/contract on the Exxon example).
- **Writer's discipline**: know your obligation (contracts × 100 × strike); cash-secure it or consciously lever; margin (~25% of obligation) is not your risk measure; put breakeven = strike − premium — place it on major support (Disney: $100 strike, $2.39, basis ~$97.50 in a $116–$96 range); covered call ≡ cash-secured put synthetically; premium is real cash ("as real as a dividend"); assignment is the accumulation path; leverage, not put-selling per se, is what's dangerous; target 2–3% conservative yield enhancement or accept the full-time job/leverage that 30%/yr demands; late-cycle at 12–13% IV, keep writes short-dated or migrate to bonds/gold.
- **Two selection styles**: (1) premium at major support on oversold names (AT&T, Gulfport, Disney); (2) premium into momentum/breakouts (Apple at 52-week highs) for fast realization and rolling.
- **Options on futures**: multipliers follow the future (gold 100 oz); settle against the future, not spot; respect contango/backwardation; master equity options first, use GLD as the gold proxy.

## Strategy structures

- **Never hold to expiration** — the universal rule. Ratio call spreads: close ≥1–2 weeks early. Calendar straddles: roll or exit, never ride to the long leg's expiry. Ratio spreads (put or call): close ≥1 month early. Cole's rolling straddle: roll at 90 days remaining on a ~9–12 month straddle.
- **Vol gates for entries**: open long-vega structures (ratios, straddles) only at the bottom of the implied-vol range; after a vol spike use debit spreads instead of ratios; never open put ratios into a fat left-tail skew (measured extremes: 50–60% IV at S&P 250 puts, 60–100% at the 200 strike, vs ~30% ATM); a downward-sloping *call* skew keeps call ratios viable even in high vol; never open straddles/ratios right before an earnings print.
- **Entry checklists**: ratio call spread = low vol + big upside potential + real crash risk + low odds of sideways; calendar straddle = directional move expected + imminent + cheap vol; diagonal income = boring, range-bound, high-IV underlying + long-dated anchor + near-the-money weekly sales.
- **Roll triggers**: calendar straddles roll ~every $5 SPY (inside the $5.42 one-week / $11 one-month implied ranges at 279 and 14% IV); ratio call spreads — no roll unless the thesis persists; diagonal income wings roll up-and-out for credit or at expiries; the SPY bear diagonal rolls its wing down-and-out immediately on a gap lower; track anchor cost on a running ledger ($20,482 → $15.7K → $14.7K).
- **Risk anchors**: ratio call spread max loss = strike width + debit, only at the short strike at expiry (SPY example: $590 at 284; crash loss = the $90 debit alone); calendar straddle honest worst case ≈ half the outlay ($500–600 per $12 straddle); AT&T put-me diagonal max risk = strike width ($10,000 on 20 contracts), shrinking with every write; AMD 1×3 put ratio: ~$100 carry, free on the upside.
- **Sizing logic**: lower structural risk justifies larger size (15×30 ratio ≈ naked-call upside with worst case ~$2,500 vs $4,700); late entries get 1–2 contracts, never full size; tail hedges sized so the carry belly is trivial.
- **The delta-dollar lens**: value every leg in delta dollars, not percentages — stock+put vs call equivalence (~$30K both ways on Amgen); IVOL $52K vs $5K hedge; SPY straddle −$190K puts vs +$265K combo; GDX anchor 0.78 delta = $25K; SPY put anchor 0.44 delta = $127K.
- **Premium structure facts**: per-day premium is richest at the front (J&J 145 call: $2.85 for 3 days, $6.30 for 31, $7.95 for 66 — the "rule of 16"); market makers in crashes raise IV and widen spreads simultaneously, so new long-vol entries are worst-priced at peak fear.
- **VIX products**: VIX options settle VIX futures (parity lives at the future, not spot; term structure usually contango = carry bleed); UVXY rode $28 → $10 (−67%) before its 2020 payoff — leave vol-products to specialists.
- **The asymmetry credo**: lose very little when wrong; convert partially-right trades to risk-free (the target-one put roll-up: AbbVie $71→$74 locking $3 for $2 of puts); make big when right (calendar straddle $600 worst vs $3,400 on the 235/vol-30 case; AMD $100 outlay vs blowout tails; Apple insurance trade worst case ~$8K vs ~$100K scenario).

## Gold and commodity options

- **Cycle measurement**: cycle = move **>20%** lasting **>2 months**; measure exact high↔low; averages are ideals, not catchable. Panel averages: declines ~6–9 months / −36% to −50%; advances ~8–11 months / +80% to +242%; GDX (two runs): 8 cycles ~9.6 mo/+89% vs ~−45%, and 9 cycles ~11 mo/+99% vs ~8.8 mo/−42%. Almost all cycles resolve in **under a year** → buy 1 year+ of time; expect repositioning within a year, so rarely pay for two.
- **Macro gates for gold**: watch 10-year real yields via TIPS (FRED) — gold's key inverse correlation; the bearish scenario is a hawkish Fed lifting the front end, not rising nominal rates (1978–80: gold and yields rose together while inflation outran them); financial repression (negative real rates, YCC or front-end pinning) is gold's friendliest regime; buy optionality when implied vol is low to avoid vega implosion.
- **Sentiment gauges**: Hulbert Gold Newsletter Sentiment (deeply negative = bottoming); Gold Miners Bullish Percent (≤25 = buy zone; sub-5 or 0 only in true bear markets, e.g., 2013–15).
- **Skew**: gold/silver/miner skew is fat RIGHT tail (OTM calls 14–50% IV vs ~10% ATM/puts) — the reverse of equities (fat left tail; puts cost 2×+ call income; SPY collar payoff ratio 0.38 = no edge). Contango/forward pricing further flatters dated gold collars.
- **Collar**: long underlying + OTM put + covered call, near-zero net cost. References: GLD 146.58 / June 139 put ($1.05) / June 165 call ($1.00) → max loss ~5%, cap +13%; GLD ~$187 / 60-day: 177 put ($2.74) + 200 call ($2.90) ≈ zero; leveraged: 1,500 GLD @169, 160 puts ($6,800) vs 185 calls ($5,300) → ~5% risk for ~10% cap; SLV: 23 put ($1.30) / 31 call ($1.20), ratio ~2.16; GDX: 38 put ($1.30) / 50 call ($1.13), 15–20¢ debit. Crash = exercise (or sell) the put, rebuy lower; rally = roll the call up/out for a debit absorbed by share gains; max loss = strike gap + put premium (185/177/$3 → $11/share).
- **Hedging non-optionable gold** (hedge with GLD options, sized by dollar-match): position value ÷ (GLD price × 100) = contracts (C$80K ≈ US$60K ≈ 3; $50K PHYS ≈ 3). Tail insurance: ~90-day puts ~10% OTM ≈ ~1% per quarter; ~1 year ≈ ~4.4%; debit-spread variant (165/150) trims $2.10 → $1.50. First-10% hedge: put debit spread (182/165 ≈ $5.30/combo; 4-by-4 for dollar-for-dollar). Advanced zero-carry hedge: put backspread — short 1× ATM, long 2× further OTM (10×182 / 20×170); margin = spread width; max pain mid-zone; gamma variant: 2× OTM puts ≈ 1× ATM starting delta but accelerate in a fall. Do not sell calls against PHYS/CGL/metal (margined as naked, ~$10K example); call credit spreads are income, not hedges. Trend-arbiter variant: hedge only while below the 50-day MA.
- **Skew debit spreads (digitals)**: long-dated far-OTM bull-call spreads — SLV 30×40 = $0.70 for $10 (≈14:1); 30×50 = $1.00 for $20 (≈20:1); GDX Oct 44/48 for $1.25 (risk $1.25 vs $2.75). Insurance-on-the-insurance; expires worthless in a slow grind; backspreads are NOT preferred with an expensive right tail.
- **2:1 ratio stock replacement**: sell 1 OTM put : buy 2 same-strike calls (Newmont: 10× Jan 60 puts @$4.10 vs 20× Jan 60 calls @$2.22; ~$300–400 net; ~$21K margin). Downside ≈ stock owner; upside = double. Size to tolerance (1-lot if needed).
- **Repair**: cut only on failed technical trades or broken fundamentals; repair "early." Style 1 — put-financed call at the averaged price (Wheaton: Nov 37 calls vs 35 puts; −$5,600 stock turned net positive). Style 2 — covered calls + same-strike bull-call spread (Agnico: 10× Feb 75 covered +$500; 10× Feb 65 −$2,000; 10× Feb 75 +$500; net −$1,000; recovers ~$10/share of break-even; nothing naked; roll up/diagonal 75→80 Feb→May ~$0.25 credit). Generic equity repair (Part V): goal 1 exit = zero-cost 1×2 ratio call spread; goal 2 hold = debit spread; goal 3 add = put-financed spread.
- **Zero-cost synthetic long**: buy 1 ATM call : sell 2 lower puts at matching premium (Yamana: 100× $4c @$0.67 vs 200× $3p @$0.34 ≈ $0). Above strike = full upside; below lower strike = put shares at a pre-chosen value level; between = free. Only on stocks you want to own, at prices you want to pay.
- **Repositioning/LEAPS**: keep the allocation in cash, hold exposure via LEAPS as stock replacement (Jan 2023 $34 GDX calls at $6.40 in April 2021); if early, roll down and always out in time (9+ months runway) — restoring, not adding, exposure (OXY $50→$45→$40; loss ~$2/leg vs stock's $5; COVID roll at $16); theta is the cost of convexity (~$1.55/share ≈ $2,300 over ~290 days on the 15-lot); lose less when wrong ($8,800 vs $15,000 at GDX $21), make more when right ($35,000 vs $29,000 at $65). "You don't have to catch the cycle. It's all about repositioning on the cycle."
- **Discipline**: conviction without an exit is how accounts die (CIBC $20k line-of-credit story); defined-risk structures let you concentrate instead of diversifying; take profits hard when +100% within 6–12 months; never bail mid-decline at the cycle floor; roll = close then open; no day-trading these — review every couple of weeks; junior miners without chains are themselves options (size to zero).

## Risk, sizing and mindset

- Price is mark-to-market; unrealized gains are paper until sold. Price = liquidity; narratives justify moves after the fact. Anchor on the payoff profile: **lose small, win big**. Accept anything can happen — only then do you respect risk.
- **Streak math**: 50% win rate ⇒ 5 straight losses in 100 trades with 81% probability; 8 straight with 17%; 4 straight with 97.3%.
- **Kelly %** = (payoff ratio × win% − loss%) ÷ payoff ratio: 70%/1:1 → 40%; 60%/1:2 → negative (don't trade); 60%/1:1 → 20%; 40%/2:1 → 10%. Never exceed Kelly; practice runs half-Kelly (still ~50% drawdowns) down to tenth-Kelly (1% per trade — the industry default). Negative Kelly on a high-win-rate book = losses bigger than wins: fix the payoff profile first.

## Breakout method and short-term hedging

- **Pattern**: rally → ~50% retrace (deeper into the 61.8% "kill zone" with reversal candles) → measured-move projection of the first leg. Profit-taking zone envelops the prior high; target one at round option strikes.
- **Activation** (service rule): long only above the 20-day MA; short only below it. Watch list ≠ active.
- **Implementation**: stock + short-dated protective put (long) / short stock + short-dated protective call (short). Two weeks to prove a breakout; ~$1,000 defined risk, same size every trade; no Hail Marys while learning; define absolute dollar risk at entry (AT&T ~$600) and never mix a short-term trade into a long-term hold. Never roll weekly protection on a position trade — size hedges to duration or collar them (TLT: June 120 put + covered call + $0.25/month dividend).
- **Hedge choice math**: an ITM put guaranteeing a sale above cost can beat the cheaper OTM put even at higher premium (Disney: $102 put ≈ $1.40 true risk vs $1.90 for the $101 put). Check the 1-week 1SD (≈ spot × IV × √(1/52)) before placing tight stops. Roll the put up as the stock rises; **monetize into drops** (sell the inflated put, lower cost basis, rebuy cheaper protection). Accounting: mark hedges at zero; subtract all protection costs from P&L.
- **Expectations**: lose $1,000 / win $3,000 at a 40% win rate = +$6,000 per 10 trades; "paper cuts and home runs"; breakout hit rate ~57–58% to target — half the trades not working is the plan, not a failure.

## Crash playbook

- **Top signals**: slope acceleration (parabolic); retail inflows extreme; call buying 100th percentile / put buying 0th percentile. "When everyone gets on the wrong side of the boat, the boat tips over."
- **Correction template**: no slowdown/yield-curve inversion → correction, not bear. First low inside 2 weeks; total duration historically 4–9 weeks with a ~50% retrace bounce then a full retest — don't buy the first bounce. 2007 precedent: even a late-cycle shock (Bear Stearns subprime funds) still printed higher highs before the real bear.
- **Tool selection**: genuine crash forecast → put backspreads (zero carry, tail payoff); 10–20% correction → put debit spreads (vega-hedged; skew makes them cheaper than constant-vol sims suggest); low-vol regime → calendared straddles and ratio call spreads; high-vol regime → vega-hedged debit spreads, directional bias mandatory, no iron condors, respect elevated short-dated IV as fair.
- **Hedge management**: hedges need not be 1:1; widen put spreads into a crash (vol-neutral roll — 400→380 cost only $2); hedges are usually not held to expiration — "it's about the rate of the hedge."
- **Skew guide**: U-shaped skew (gold, TLT) → collars and both-way debit spreads; S&P fat left tail → put debit spreads to short, outright calls to go long.
- **Emotional rinse cycle**: drop → chase the bounce → flush → relief → capitulation (the actual buy point). The structure, not the forecast, carries you through it.

## Tools and platforms

- **TradingView must-dos**: autosave on; star timeframe/indicator/drawing favorites; save indicator templates (50/200 EMA; 40/50 DMA crossover = commodity-trend signal); save drawing defaults (double-click → save); channel alerts for breakout/fib zones, named for the signal they protect; mind tier limits (~5–10 → 40 → 400 alerts; volume profile needs Pro).
- **Scanning workflow**: watchlist groups + colored flags (green = breakout setups, red = revisit) + spacebar rapid-flip; top-down: macro → sector → stock → 10–15-name short list → 1–2 published.
- **IBKR essentials**: declare options experience at account opening or approval is denied; watch **excess liquidity** (yellow below ~10% cushion → act; red at zero → forced liquidation); always limit orders for options; enable weeklies/quarterlies and widen strike display in OptionTrader; separate legs = per-leg flexibility, Strategy Builder = one ticket and locked structure; group windows via the green-chain icon and lock the layout (green padlock).
- **Option analytics**: nearer expiries = steeper skews; LEAPS flatter; IV rises into expiry; compare IV across peers and buy the lowest-vol underlying for a directional view; Probability Lab workflow — read market-implied distribution → edit to your forecast → score on both bases; risk/reward is invariant, probability of profit is not.
- **Scanner sizing rule**: sane volume floors — $50B returned nothing; $500M on "US stocks under their 100-day EMA" produced a workable short list.

---

# Appendix: Source Map

<!-- Maps every source video in the corpus to the part/section of this document where its material lives. -->

| Source video | Where its material lives |
|---|---|
| Module 1 - Money and Currency (720p with 25fps).mp4 | Part I §1 |
| EuroDollar University (540p with 25fps).mp4 | Part I §2 |
| DragonPortfolioGammonJune262020 (1080p with 25fps).mp4 | Part I §3 |
| How The Economic Machine Works by Ray Dalio (1080p with 24fps).mp4 | Part I §4 |
| John Law and the Mississippi Bubble (360p with 23fps).mp4 | Part I §5 |
| Scrooge McDuck and Money 1967 (360p with 29fps).mp4 | Part I §5 |
| Walt Disney Chicken Little 1943 (240p with 25fps).mp4 | Part I §5 |
| Options Bootcamp Part 1 - Introduction (720p with 25fps).mp4 | Part II §1, §2 |
| Options Bootcamp Part 2 - Pricing (720p with 25fps).mp4 | Part II §3, §4, §5 |
| Options Bootcamp Part 3 - Greeks (720p with 25fps).mp4 | Part II §6 |
| Options Bootcamp Part 4 - Application (720p with 25fps).mp4 | Part II §7, §8 |
| Options Master Program Module 01 Introduction to Options (1080p with 30fps).mp4 | Part II §1, §2, §9 |
| Options Master Program Module 02 Contract Specifications (1080p with 30fps).mp4 | Part II §2 |
| Options Master Program Module 03 Contract Pricing (1080p with 30fps).mp4 | Part II §3 |
| Options Master Program Module 04 Understanding Volatility (1080p with 30fps).mp4 | Part II §4 |
| Options Master Program Module 05 Understanding Time (1080p with 30fps).mp4 | Part II §5 |
| OptionsFundamentals (1080p with 25fps).mp4 | Part II §3, §4, §6, §7 |
| OptionsforIncome (1080p with 25fps).mp4 | Part II §8 |
| Option Writing Bootcamp (720p with 25fps).mp4 | Part II §1, §2, §3, §4, §5, §6, §9 |
| The Ratio Call Spread (720p with 25fps).mp4 | Part III §1; Part V §7 (top signals, Morgan Stanley flow data) |
| Trading Calendar Straddles (1080p with 30fps).mp4 | Part III §2; Part V §7 (the calendared straddle that paid in Feb 2018) |
| 2020-04-14DiagonalSpreadBootcamp (1080p with 25fps).mp4 | Part III §2 (diagonals) |
| Trading Volatility Bootcamp (1080p with 25fps).mp4 | Part III §1, §3 |
| BuildingSynthetics (1080p with 25fps).mp4 | Part III §4 |
| HedgedPositions (1080p with 25fps).mp4 | Part III §2, §5 |
| AsymmetricStrategiesToRepairAndLeverageYourGoldHoldings (720p with 25fps).mp4 | Part IV §1, §2, §3, §5, §6, §7 |
| How to Leverage Gold Like a Pro (even if you hate risk) (1080p with 30fps).mp4 | Part IV §1, §2, §3 |
| How to Find Asymmetry on Your Favourite Commodity Stocks (Using Options the Right Way) (1080p with 25fps).mp4 | Part IV §2, §7, §8, §9 |
| Using Options to trade Commodity Cycles (1080p with 30fps).mp4 | Part IV §7, §8, §9 |
| HedgingPhysicalGoldAug212020 (1080p with 25fps).mp4 | Part IV §4 |
| TradingGoldCollarsAug172020 (1080p with 25fps).mp4 | Part IV §2, §3, §5 |
| GOLD CYCLE - April 16 2021 LIVE Webinar (1080p with 23fps).mp4 | Part IV §7, §8 |
| Module 01 - Thinking Like a Master Trader (1080p with 30fps).mp4 | Part V §1, §2 |
| FREE MODULE - Risk, Randomness and Trading Sizing (1080p with 30fps).mp4 | Part V §2 |
| BreakOutTrading (1080p with 25fps).mp4 | Part V §3, §4 |
| Short Term Hedging (540p with 25fps).mp4 | Part V §3, §4 |
| Patrick's Favourite Trade Repair Strategy (720p with 25fps).mp4 | Part V §5 |
| 2021-02-19BPTTacticalPortfolio (1080p with 25fps).mp4 | Part V §6 |
| How to Profit from a Market Crash (1080p with 30fps).mp4 | Part V §1, §7 |
| StrategiesThatGiveYouAnUnfairAdvantageInAMarketDownturn-Cleaned (1080p with 23fps).mp4 | Part V §7 |
| 2021-05-25TradingViewTutorial (1080p with 23fps).mp4 | Part VI §1 |
| Interactive Broker Tutorial - Basic.mp4 (720p with 23fps).mp4 | Part VI §2 |
| Interactive Broker Tutorial - Advanced.mp4 (720p with 25fps).mp4 | Part VI §2, §3 |
| Interactive Brokers - Option Tools Tutorial.mp4 (720p with 25fps).mp4 | Part VI §3 |
| Investing Smarter_ Pitfalls of Stop Loss Orders (1080p with 30fps).mp4 | Part VI §4 (options primer echoes in Part II §1; stop-vs-put theme across Parts II and V) |

