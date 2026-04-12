<!-- 此檔案需要翻譯為香港繁體中文 -->
<!-- This file needs translation to HK Traditional Chinese -->

# Side Lesson 20: Options Greeks -- A Deep Dive

---

## Reading Section

If delta tells you how much an option's price moves when the stock moves, the higher-order Greeks tell you how delta itself changes, how time decay accelerates, how volatility shifts affect your position, and how interest rates factor in. Mastering these second-order sensitivities -- gamma, rho, charm, vanna, and others -- transforms your understanding of options from a flat, static snapshot into a dynamic, three-dimensional view. These concepts are not just theoretical curiosities. Professional options traders manage risk by hedging gamma, trading vanna, and monitoring charm on a daily basis. For individual investors who use options, understanding these Greeks helps explain why positions sometimes behave in unexpected ways and how to manage complex strategies more effectively.

---

### a) Why This Is Important

**Options Are Non-Linear.** Unlike stocks, where a $1 move in the stock produces a roughly fixed dollar change in your position, options exhibit non-linear behavior. Your profit-and-loss curve bends. Delta changes as the stock moves, time decay accelerates as expiration approaches, and volatility shifts can help or hurt you depending on your position. The higher-order Greeks describe these non-linearities.

**Risk Management.** Professional options traders rarely take directional bets. Instead, they manage "the Greeks" -- ensuring that their portfolio's exposure to each risk factor is within acceptable bounds. Understanding gamma, for example, tells you how quickly your directional exposure changes and whether you need to rebalance. Understanding vanna tells you how your delta exposure shifts when volatility changes.

**Explaining Unexpected Behavior.** If you have ever held an option that barely moved even though the stock moved in your favor, or an option that lost value faster than you expected, the answer almost certainly lies in the higher-order Greeks. Understanding them eliminates the "why did my option do that?" confusion.

**Strategy Selection.** Different strategies have different Greek profiles. Selling options gives you negative gamma (your position gets worse as the stock moves). Buying options gives you positive gamma (your position gets better as the stock moves). Understanding these profiles helps you select strategies that match your market outlook and risk tolerance.

**Income Strategy Refinement.** For investors using covered calls and cash-secured puts (as covered in earlier lessons), understanding gamma and theta interactions helps you choose better strike prices and expiration dates. It explains why short-dated options generate more daily theta decay but carry more gamma risk.

---

### b) What You Need to Know

#### Quick Review of First-Order Greeks

Before diving into higher-order Greeks, let us briefly review the first-order Greeks.

**Delta** measures the rate of change in the option's price relative to a $1 change in the underlying stock. A call with delta of 0.50 gains approximately $0.50 for every $1 the stock rises. Delta ranges from 0 to 1.0 for calls and 0 to -1.0 for puts. At-the-money options have deltas near 0.50 (calls) or -0.50 (puts).

**Theta** measures the rate of time decay -- how much value the option loses each day, all else being equal. Theta is typically negative for option buyers (time decay works against them) and positive for option sellers. Theta accelerates as expiration approaches, with the steepest decay occurring in the final 30 days.

**Vega** measures the option's sensitivity to changes in implied volatility. A vega of 0.15 means the option's price changes by $0.15 for every 1 percentage point change in implied volatility. At-the-money options have the highest vega. Both calls and puts have positive vega -- they benefit from rising volatility.

#### Gamma: The Rate of Change of Delta

Gamma is the most important second-order Greek. It measures how much delta changes when the stock price moves $1.

**Gamma = Change in Delta / Change in Stock Price**

If a call option has a delta of 0.50 and a gamma of 0.05, and the stock rises $1, the new delta is approximately 0.55. If the stock rises another $1, the delta becomes approximately 0.60.

**Key Properties of Gamma:**

- **Gamma is highest for at-the-money options.** ATM options have the most uncertain outcome (they could expire in or out of the money), so their delta is most sensitive to stock price changes.

- **Gamma increases as expiration approaches.** This is critical and counterintuitive. A one-week ATM option has much higher gamma than a six-month ATM option. As expiration nears, delta must converge to either 1.0 (if in the money) or 0.0 (if out of the money). This rapid convergence means gamma -- the rate at which delta changes -- becomes very large.

- **Gamma is always positive for long options.** Whether you buy calls or puts, you have positive gamma. This means delta moves in your favor: when the stock moves up, your call delta increases (you get longer); when the stock moves down, your put delta becomes more negative (you get shorter). Positive gamma is beneficial for directional moves.

- **Gamma is always negative for short options.** If you sell options, you have negative gamma. Delta moves against you: when the stock moves up, your short call delta makes you shorter; when the stock moves down, your short put delta makes you longer. Negative gamma means that large stock moves hurt your position -- the bigger the move, the more it hurts.

**Gamma Risk in Practice:**

The interaction between gamma and theta creates a fundamental trade-off in options trading. Buying options gives you positive gamma (you benefit from large moves) but costs you theta (time decay works against you). Selling options gives you positive theta (you collect time decay) but exposes you to negative gamma (large moves hurt you).

This is why selling short-dated options near expiration can be dangerous despite the attractive theta. The gamma is very high, meaning a sudden large move in the stock can generate losses that far exceed the theta collected.

**Gamma Scalping.** Market makers and professional traders use a technique called gamma scalping (or dynamic hedging) to profit from gamma. They buy options (gaining positive gamma), delta-hedge with the underlying stock, and then profit by continuously rehedging as the stock moves. Each time the stock moves up, they sell shares (locking in gains on their increasing delta). Each time the stock moves down, they buy shares. The profit from this rehedging can offset the theta decay of the options, and in volatile markets, it can generate substantial profits.

#### Rho: Interest Rate Sensitivity

Rho measures the option's sensitivity to changes in interest rates.

**Rho = Change in Option Price / Change in Interest Rate**

A rho of 0.05 means the option's price changes by $0.05 for every 1 percentage point change in interest rates.

**Key Properties:**
- Call options have positive rho (rising rates increase call values because the present value of the exercise price decreases).
- Put options have negative rho (rising rates decrease put values).
- Rho is more significant for long-dated options (LEAPS) and less significant for short-dated options.
- In typical market conditions, rho has the smallest impact of the primary Greeks. It becomes relevant only for long-term positions or during periods of significant rate changes.

**Practical Impact:** During the Fed's aggressive rate-hiking cycle in 2022-2023, rho effects were more noticeable than usual. LEAPS call options received a modest boost from rising rates, while LEAPS puts experienced a drag, beyond what delta and vega alone would explain.

#### Charm (Delta Decay): How Delta Changes with Time

Charm, also called delta decay, measures the rate at which delta changes as time passes, holding the stock price constant.

**Charm = Change in Delta / Change in Time**

**Why It Matters:**

An out-of-the-money call option with 60 days to expiration might have a delta of 0.30. As time passes and the option approaches expiration without the stock reaching the strike, the delta drifts toward zero. Charm tells you how fast this drift occurs.

Conversely, an in-the-money option's delta drifts toward 1.0 as expiration approaches. Charm describes this convergence.

**Practical Implications:**
- If you are delta-hedging a portfolio, charm tells you how much your hedges will drift overnight even if the stock does not move.
- Over weekends and holidays (when time passes but the stock does not trade), charm effects accumulate and can create meaningful delta shifts by the next trading session.
- Charm is most significant for near-expiration options and options near the strike price.

#### Vanna: Delta Sensitivity to Volatility

Vanna measures how much delta changes when implied volatility changes.

**Vanna = Change in Delta / Change in Implied Volatility**

**Why It Matters:**

Vanna explains a phenomenon that confuses many option traders. Suppose you own an out-of-the-money call with a delta of 0.25 and the stock starts falling. As the stock falls, implied volatility often rises (the leverage effect). The rising volatility pushes the option's delta higher through vanna, partially offsetting the delta decline from the stock falling. This is why OTM options sometimes do not lose as much value as expected during sell-offs.

**Key Properties:**
- Vanna is highest for out-of-the-money options.
- At-the-money options have near-zero vanna (their delta is not very sensitive to volatility changes).
- For calls, vanna is typically positive for OTM strikes and negative for ITM strikes. For puts, the signs are reversed.

**Vanna Flows.** In institutional options markets, "vanna flows" describe how changes in implied volatility cause market makers to adjust their stock hedges, which in turn moves the stock price. As volatility declines (such as after an earnings announcement), market makers' delta hedges shift, often requiring them to buy stock -- which can amplify upward moves. This creates the "vol crush rally" pattern often seen after earnings.

#### Volga (Vomma): Vega Sensitivity to Volatility

Volga (also called vomma) measures how much vega changes when implied volatility changes.

**Volga = Change in Vega / Change in Implied Volatility**

**Why It Matters:**

Volga tells you whether your volatility exposure itself is convex or concave. An option with high volga becomes increasingly sensitive to volatility as volatility rises. This is relevant for:
- Pricing and hedging volatility smiles (the pattern of implied volatilities across different strike prices).
- Understanding why deep out-of-the-money options can explode in value during volatility spikes -- their vega increases as volatility rises (positive volga), amplifying the gain.

#### Speed: Rate of Change of Gamma

Speed measures how gamma changes as the stock price moves.

**Speed = Change in Gamma / Change in Stock Price**

Speed is relevant for understanding how your gamma risk itself shifts as the market moves. It matters most for large portfolios of options where gamma concentration near certain strikes can create sudden exposure changes if the stock moves through those levels.

#### Color: Rate of Change of Gamma Over Time

Color (also called gamma decay) measures how gamma changes as time passes.

**Color = Change in Gamma / Change in Time**

As expiration approaches, gamma concentrates around the at-the-money strike and becomes very spiky. Color describes this concentration process and is relevant for options market makers managing large books of expiring options.

#### Portfolio Management with Greeks

**The Greek Balance Sheet.** Professional options traders view their portfolio as a set of Greek exposures rather than a collection of individual positions. They maintain a "Greek balance sheet" showing:

- Total portfolio delta (directional exposure).
- Total portfolio gamma (exposure to stock price movements).
- Total portfolio theta (daily time decay).
- Total portfolio vega (exposure to volatility changes).

The goal is to keep each Greek within acceptable risk limits while generating positive expected returns, typically from theta collection.

**Delta-Neutral Trading.** Many professional strategies aim to be delta-neutral -- having zero directional exposure. The profit comes from other Greeks:
- **Positive gamma strategies** profit from large stock moves in either direction (paid for by theta decay).
- **Negative gamma strategies** profit from theta collection (paid for by large stock moves).
- **Long vega strategies** profit from rising volatility.
- **Short vega strategies** profit from declining volatility.

**Hedging Higher-Order Greeks.** While retail investors typically only hedge delta (if at all), institutional traders hedge gamma, vanna, and other Greeks using combinations of options at different strikes and expirations. This allows them to isolate the specific risk they want to take while neutralizing others.

---

### c) Common Misconceptions

**"I only need to know delta."** Delta is the most important Greek for understanding directional exposure, but it tells you nothing about how your position behaves as conditions change. Without understanding gamma, you do not know how your directional exposure shifts as the stock moves. Without theta, you do not know how time works for or against you. Delta is necessary but not sufficient.

**"Gamma is always good to have."** Positive gamma means your position benefits from large moves, but it comes at a cost -- theta decay. If the stock does not move enough to offset the daily theta loss, positive gamma positions lose money. Gamma is a trade-off, not a free benefit.

**"Short-dated options are better for selling because they have more theta."** Short-dated options do have more daily theta, but they also have much more gamma. A sudden large move near expiration can generate losses that far exceed the theta collected. Many experienced option sellers prefer 30-60 day expirations as a balance between reasonable theta and manageable gamma.

**"The Greeks are constant."** All Greeks change constantly as the stock price, time, volatility, and interest rates change. Delta changes because of gamma, gamma changes because of speed and color, vega changes because of volga, and delta also changes because of charm and vanna. Options are dynamic instruments, and static analysis is always incomplete.

**"Second-order Greeks do not matter for small portfolios."** While the dollar impact of vanna and charm may be small for a single option position, understanding these Greeks helps explain why your options behave differently than you expected. Knowledge of the higher-order Greeks improves decision-making even if you never formally calculate them.

---

### d) Q&A

**Q: How do I calculate the Greeks for my options positions?**
A: Most brokerage platforms display the Greeks for individual options and for your overall portfolio. Thinkorswim (Schwab), Interactive Brokers, and Tastytrade all show delta, gamma, theta, and vega. For higher-order Greeks, you may need specialized software or options calculators. Websites like OptionStrat and the CBOE options calculator provide free tools.

**Q: What is "gamma exposure" (GEX) and why do traders track it?**
A: Gamma exposure refers to the aggregate gamma held by options market makers at each strike price. When market makers have large positive gamma exposure, they buy dips and sell rallies (hedging their gamma), which dampens volatility. When they have large negative gamma exposure, they sell dips and buy rallies (hedging in the same direction as the move), which amplifies volatility. GEX data (available from services like SpotGamma and SqueezeMetrics) helps traders understand whether market maker hedging will stabilize or destabilize the market.

**Q: How does gamma affect my covered calls?**
A: When you sell a covered call, you are short gamma. If the stock rallies strongly, the call's delta increases toward 1.0, and your position acts increasingly like you do not own the stock (your long stock delta of +1.0 is offset by the call's increasing negative delta). If the stock drops sharply, the call's delta decreases toward zero, and your position acts like you are fully long the stock with no protection. This is the gamma risk of covered calls -- your effective position gets worse in both directions from the entry point.

**Q: What is "pin risk" near expiration?**
A: Pin risk occurs when a stock price is very close to a strike price at expiration. Options near the strike have very high gamma, meaning tiny price movements cause large swings in whether the option expires in or out of the money. For sellers of options, this creates uncertainty about whether they will be assigned. For market makers, the extreme gamma near expiration can create difficult hedging situations. This is why options activity around at-the-money strikes near expiration can cause unusual stock price movements.

**Q: How do professional traders use vanna to predict stock market moves?**
A: Professional traders monitor aggregate vanna exposure to predict how market maker hedging will affect stock prices when volatility changes. When aggregate vanna is large and positive, a decline in implied volatility causes market makers to buy stock to adjust their hedges, pushing prices higher. This helps explain why stocks often rally as implied volatility declines -- it is not just sentiment, it is mechanical hedging flow. Some traders use this as a tactical signal, buying stocks when they expect volatility to decline.

**Q: Is there a simple way to think about the relationship between gamma and theta?**
A: Yes. Think of gamma as the "speed limit" on theta. The more gamma an option has, the more theta you pay (as a buyer) or collect (as a seller). This is because gamma represents the option's sensitivity to movement, and theta is the price you pay for that sensitivity. You can roughly think of it as: gamma represents opportunity (the chance to profit from moves), and theta represents the cost of that opportunity. Market makers earn their living by managing this trade-off efficiently.

---

## YouTube Script

[INTRO - 0:00]

[VISUAL: Dashboard showing multiple Greek values updating in real-time as a stock price moves, with gauges and meters for each Greek]

**Alex:** If you have been following our options lessons, you know about delta -- how much an option moves when the stock moves. But delta is just the beginning. There is a whole world of sensitivities beneath the surface that professional traders track obsessively.

**Sam:** Gamma, rho, charm, vanna -- these sound like characters from a Greek mythology class, but they are actually the keys to understanding why options sometimes behave in ways that surprise you. Today, we are going deep on the Greeks.

[VISUAL: Title card "Options Greeks Deep Dive: Beyond Delta"]

---

[SECTION 1 - GAMMA: THE MOST IMPORTANT SECOND-ORDER GREEK - 1:30]

[ANIMATION: A speedometer showing delta, with gamma as the needle showing how fast the speedometer is changing]

**Alex:** Let us start with gamma, because it is the most important Greek after delta. If delta tells you how fast your option price changes, gamma tells you how fast delta itself changes.

**Sam:** Think of it like driving a car. Delta is your speed. Gamma is your acceleration. A delta of 0.50 means you are going 50 miles per hour. A gamma of 0.05 means for every $1 the stock moves, your speed increases by 5 miles per hour.

[VISUAL: Car analogy: Delta = Speed, Gamma = Acceleration, with option values changing alongside]

**Alex:** Here is why this matters. If you buy an option with a delta of 0.50 and a gamma of 0.05, and the stock goes up $1, your delta becomes 0.55. Now you are making more money per dollar of stock movement than before.

**Sam:** And if the stock goes up another dollar, delta becomes 0.60. Then 0.65. The option is accelerating in your favor. This is the beauty of positive gamma for option buyers -- the more the stock moves in your direction, the faster your profits grow.

[ANIMATION: Profit curve showing non-linear acceleration of gains for long option position vs linear gains for stock position]

**Alex:** But here is the flip side. If you are selling options, you have negative gamma. The stock moves against you, and your losses accelerate. The more it moves, the faster you lose.

---

[SECTION 2 - THE GAMMA-THETA TRADEOFF - 4:00]

[VISUAL: Balance scale with "Gamma (Movement Opportunity)" on one side and "Theta (Time Decay Cost)" on the other]

**Sam:** Now here is the fundamental trade-off in options trading. Gamma and theta are enemies. You cannot have one without paying for it with the other.

**Alex:** If you buy options, you get positive gamma -- you benefit from big moves. But you pay for it through negative theta -- time decay erodes your option's value every day.

**Sam:** If you sell options, you get positive theta -- you collect time decay like a landlord collecting rent. But you pay for it through negative gamma -- big moves hurt you, and the bigger the move, the worse it gets.

[ANIMATION: Two scenarios playing out side by side:
Left: Option buyer -- stock moves big, gamma kicks in, profits exceed theta losses
Right: Option buyer -- stock stays flat, theta drains value day after day]

**Alex:** This is why selling options feels great in calm markets. Theta drips into your account every day like a dividend. But when the market suddenly moves -- and it always does eventually -- negative gamma can wipe out weeks or months of theta in a single session.

**Sam:** The sweet spot for option sellers is usually 30 to 60 days until expiration. You get decent theta, but gamma is not yet extreme. Selling options with only a week to expiration gives you amazing daily theta but dangerously high gamma.

[VISUAL: Chart showing gamma and theta curves as a function of days to expiration, with the "danger zone" near expiration highlighted]

---

[SECTION 3 - VANNA AND CHARM - 6:30]

[VISUAL: Three-dimensional surface showing how delta changes with both stock price AND implied volatility]

**Alex:** Now let us move to the more exotic Greeks. Vanna measures how delta changes when implied volatility changes. And it explains something that confuses a lot of option traders.

**Sam:** Have you ever held an out-of-the-money call, the stock barely moved, but the option still gained or lost significant value? That is often vanna at work.

**Alex:** Here is how it works. Say you own an OTM call with a delta of 0.25. Suddenly, implied volatility spikes -- maybe bad news hits the market. Normally, you would think rising volatility helps you because your option has positive vega. And it does. But vanna also pushes your delta higher. Your 0.25 delta option might become a 0.35 delta option, making your position more sensitive to the stock's movements.

[ANIMATION: OTM call option with delta arrow growing as IV increases, showing the vanna effect]

**Sam:** In institutional markets, these vanna effects drive what traders call "vanna flows." When implied volatility drops -- like after an earnings announcement -- market makers have to buy stock to adjust their delta hedges. This buying pressure pushes stocks higher. It is one reason why stocks often rally after the uncertainty of an event passes.

**Alex:** Then there is charm, which is how delta changes with time. An out-of-the-money option's delta drifts toward zero as expiration approaches. Charm tells you how fast this drift happens.

[VISUAL: OTM call option delta declining over time as expiration approaches, with charm as the slope of the decline]

**Sam:** Charm matters most over weekends and holidays. If you are delta-hedged going into a Friday and the stock does not move over the weekend, your delta has still changed by Monday morning because two days of charm have accumulated. Professional traders adjust for this, which is one reason why Monday mornings can have unusual options-related trading activity.

---

[SECTION 4 - PORTFOLIO GREEK MANAGEMENT - 9:00]

[VISUAL: "Greek Dashboard" showing a sample portfolio with aggregate delta, gamma, theta, and vega values]

**Alex:** Professional options traders do not think about individual options. They think about their entire portfolio as a set of Greek exposures.

**Sam:** Imagine a dashboard with four gauges. Delta -- your directional exposure. Gamma -- your exposure to big moves. Theta -- your daily time decay income or cost. Vega -- your exposure to volatility changes.

[ANIMATION: Dashboard gauges for a delta-neutral, negative gamma, positive theta, short vega portfolio -- typical for option sellers]

**Alex:** An option-selling portfolio might show: delta near zero (market-neutral), negative gamma (hurt by big moves), positive theta (collecting daily income), and negative vega (hurt by rising volatility). That is the profile of strategies like iron condors and short strangles.

**Sam:** A long options portfolio shows the opposite: positive gamma (benefits from big moves), negative theta (paying daily time decay), and positive vega (benefits from rising volatility).

**Alex:** The art of portfolio management is keeping each Greek within your risk tolerance while generating positive expected returns. If your gamma gets too negative, you might buy some options to bring it back. If your vega gets too positive, you might sell some to reduce it.

[VISUAL: Risk management example showing a position that exceeds gamma limits and the adjustment trade to bring it back in line]

**Sam:** For individual investors, you do not need to manage Greeks this precisely. But understanding the concepts helps you recognize when your options portfolio is exposed to risks you did not intend. If you sold a bunch of puts and your gamma is very negative, you know that a sharp market drop will hurt you disproportionately. That awareness alone is valuable.

---

[SECTION 5 - GAMMA EXPOSURE AND MARKET IMPACT - 11:00]

[VISUAL: GEX chart showing aggregate market maker gamma exposure at different stock price levels]

**Alex:** Let us end with something fascinating -- how gamma affects the entire stock market, not just individual options.

**Sam:** Options market makers hold enormous positions. Their aggregate gamma exposure at different stock price levels actually influences how the market behaves.

**Alex:** When market makers have positive gamma overall, they buy stocks when the price falls and sell when it rises. This acts like a shock absorber, dampening volatility. It is one reason why the market can feel "pinned" near large option strikes -- market maker hedging activity pushes the price back toward the strike.

[ANIMATION: Ball rolling in a valley near a strike price, with positive gamma walls on either side pushing it back toward the center]

**Sam:** But when market makers have negative gamma -- often after selling a lot of put options to hedgers -- they have to sell when the stock falls and buy when it rises. This amplifies moves instead of dampening them. Markets with negative gamma exposure tend to be more volatile and prone to sharp selloffs.

[ANIMATION: Ball on a hilltop, with negative gamma slopes accelerating movement away from the center in either direction]

**Alex:** This is why some traders track aggregate gamma exposure data. When dealer gamma flips from positive to negative, it can signal that volatility is about to increase -- because the mechanical hedging flows that normally stabilize the market are now destabilizing it.

**Sam:** You do not need to trade based on gamma exposure data as a retail investor. But understanding this mechanism helps explain why markets sometimes move sharply for no apparent fundamental reason -- it is often the Greeks at work behind the scenes.

[VISUAL: End card with channel logo and "Next: Margin and Leverage"]

**Alex:** Next time, we are covering a topic that can make or break your investing journey -- margin accounts, leverage, and the regulations that govern them. See you there.

[END - 13:30]
