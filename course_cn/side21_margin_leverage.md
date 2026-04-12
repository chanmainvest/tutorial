<!-- 此文件需要翻译为简体中文 -->
<!-- This file needs translation to Simplified Chinese -->

# Side Lesson 21: Margin Accounts, Leverage, and Risk

---

## Reading Section

Leverage is the most powerful and most dangerous force in investing. It can amplify your returns when you are right and accelerate your ruin when you are wrong. At its core, leverage means investing with borrowed money -- and the primary mechanism for individual investors to access leverage is the margin account. Understanding how margin works, what regulations govern it, how margin calls operate, and what portfolio margin offers sophisticated investors is essential before you ever consider using borrowed money to invest. More importantly, understanding leverage helps you recognize when others are using it excessively, which is often a precursor to market-wide problems.

---

### a) Why This Is Important

**Leverage Magnifies Everything.** If you invest $100,000 of your own money and the stock goes up 10%, you gain $10,000. If you borrow another $100,000 and invest $200,000, a 10% gain produces $20,000 -- a 20% return on your equity. But a 10% loss also produces a $20,000 loss -- a 20% loss on your equity. And if the stock falls 50%, you have lost your entire investment. Leverage cuts both ways with equal ferocity.

**Margin Calls Can Force Selling.** When you borrow on margin and your positions decline, your broker may demand that you deposit additional funds or liquidate positions. This forced selling happens at the worst possible time -- when prices are falling -- and often locks in devastating losses. Many investors who survived the 2008 financial crisis in the market did not survive the margin calls that came with it.

**Regulatory Framework Matters.** Federal Reserve Regulation T, FINRA maintenance margin requirements, and brokerage-specific house requirements create a layered regulatory framework that governs how much you can borrow and what happens when your account value drops. Understanding these rules prevents nasty surprises.

**Leverage Is Everywhere.** Even if you never use margin, leverage affects you indirectly. Banks use leverage. Hedge funds use leverage. Leveraged ETFs use leverage. Understanding the concept helps you evaluate these instruments and understand systemic risks in the financial system.

**Portfolio Margin Changes the Game.** For sophisticated investors with large accounts, portfolio margin offers significantly more borrowing power by calculating margin based on the actual risk of your portfolio rather than applying fixed percentages to each position. This is a powerful tool but also a more nuanced one that requires understanding.

---

### b) What You Need to Know

#### Cash Accounts vs. Margin Accounts

**Cash Accounts.** In a cash account, you can only buy securities with the money you have deposited. If you have $50,000 in cash, you can buy up to $50,000 in securities. You cannot borrow from the broker, and you cannot sell stocks short. Cash accounts eliminate the risk of margin calls entirely.

Cash accounts also impose the T+1 settlement rule (previously T+2, changed in 2024). When you sell a stock, the cash is not immediately available for a new purchase -- it takes one business day to settle. If you buy a stock with unsettled funds and sell it before those funds settle, you commit a "good faith violation." Three good faith violations in a 12-month period can result in your account being restricted to settled-cash-only trades for 90 days.

**Margin Accounts.** A margin account allows you to borrow money from your broker to purchase securities, using your existing securities as collateral. The broker charges interest on the borrowed amount, typically at rates based on the broker's call rate plus a spread. Margin interest rates vary by broker but generally range from 5% to 12% depending on the amount borrowed and prevailing interest rates.

To open a margin account, you typically need a minimum deposit of $2,000 and must sign a margin agreement. By signing, you agree that the broker can:
- Lend your securities to short sellers.
- Liquidate your positions without your consent if you fail to meet a margin call.
- Change margin requirements at any time.

#### Regulation T: Initial Margin

Federal Reserve Regulation T, established in 1934, sets the initial margin requirement for purchasing securities on credit. The current Reg T requirement is 50%, meaning you must put up at least 50% of the purchase price with your own equity.

**Example:**
- You want to buy $100,000 worth of stock.
- Under Reg T, you must deposit at least $50,000 in cash or marginable securities.
- You can borrow the remaining $50,000 from your broker.
- Your leverage ratio is 2:1 -- you control $100,000 with $50,000 of your own money.

**Buying Power.** When you deposit $50,000 in a margin account, your initial buying power is $100,000 (2x your equity). However, as your positions appreciate, your equity increases, and your buying power grows. Conversely, as positions decline, your equity decreases, and your buying power shrinks.

**Marginable Securities.** Not all securities are marginable. Generally, stocks listed on major exchanges, most ETFs, and most bonds can be purchased on margin. Penny stocks (under $5), recently IPO'd stocks, and some highly volatile securities may not be marginable or may have higher margin requirements.

#### Maintenance Margin and Margin Calls

Once you have purchased securities on margin, you must maintain a minimum level of equity in your account. This is the maintenance margin requirement.

**FINRA Maintenance Margin.** FINRA (the Financial Industry Regulatory Authority) sets the minimum maintenance margin at 25% of the total market value of the securities in your account. This means your equity (account value minus amount borrowed) must be at least 25% of the total position value.

**Brokerage House Requirements.** Most brokers impose maintenance requirements stricter than FINRA's 25% minimum. Many brokerages require 30-40% maintenance margin for stocks, and even higher for concentrated positions, volatile stocks, or leveraged ETFs. Your broker can change these requirements at any time without notice.

**How a Margin Call Works:**

Let us walk through a detailed example:

1. You have $50,000 in cash and buy $100,000 worth of stock on margin (borrowing $50,000).
2. Your equity is $50,000 / $100,000 = 50%.
3. The stock falls 20%. Your position is now worth $80,000.
4. Your equity is now $80,000 - $50,000 (loan) = $30,000.
5. Your equity percentage is $30,000 / $80,000 = 37.5%.
6. If your broker's maintenance requirement is 35%, you are still above it. No margin call.
7. The stock falls another 10% (30% total decline). Position value: $70,000.
8. Equity: $70,000 - $50,000 = $20,000.
9. Equity percentage: $20,000 / $70,000 = 28.6%.
10. Your broker issues a margin call because you are below the 35% requirement.

**The Margin Call Trigger Price Formula:**

For a long position, the stock price that triggers a margin call can be calculated:

Trigger Price = Purchase Price * (1 - Initial Margin) / (1 - Maintenance Margin)

Using our example with 50% initial margin and 35% maintenance margin:
Trigger Price = $100 * (1 - 0.50) / (1 - 0.35) = $100 * 0.50 / 0.65 = $76.92

So a 23.1% decline would trigger a margin call.

**What Happens During a Margin Call:**

When you receive a margin call, you have limited options:
1. **Deposit additional cash** to bring your equity above the maintenance requirement.
2. **Deposit additional marginable securities** as collateral.
3. **Sell existing positions** to reduce the borrowed amount.
4. **Do nothing** -- in which case the broker will liquidate enough of your positions to restore the maintenance margin. The broker chooses which positions to sell and does so at market prices, which may be unfavorable.

Critical warning: Brokers are not required to give you advance notice of a margin call or time to respond. In fast-moving markets, your broker can liquidate your positions immediately without contacting you. This is spelled out in the margin agreement you signed -- read it carefully.

**Cascading Margin Calls.** During market crashes, margin calls can cascade. As prices fall, margin calls force selling, which pushes prices lower, which triggers more margin calls, which forces more selling. This positive feedback loop amplified both the 1929 crash and the 2008 financial crisis.

#### Short Selling on Margin

Margin accounts also enable short selling -- selling borrowed shares with the expectation of buying them back at a lower price. Short selling has its own margin requirements.

**Initial Margin for Short Sales.** Reg T requires 50% initial margin for short sales. If you short $10,000 worth of stock, you must have at least $5,000 in equity plus the $10,000 proceeds of the short sale in your account.

**Maintenance Margin for Short Sales.** FINRA requires 30% maintenance margin on short positions, though brokers typically require more. Because short positions have theoretically unlimited loss potential (a stock can rise infinitely), brokers are especially aggressive about margin calls on short positions.

**Short Squeeze Risk.** If a heavily shorted stock rises rapidly, short sellers face mounting margin calls. Forced buying to cover short positions can push the stock even higher, triggering more margin calls in a cascade. The GameStop (GME) episode in January 2021 was a dramatic example of this dynamic, where short sellers faced billions in losses as forced covering sent the stock from $20 to over $400.

#### Pattern Day Trader (PDT) Rule

FINRA's Pattern Day Trader rule applies to margin accounts. If you execute four or more day trades (buying and selling the same security on the same day) within a rolling five-business-day period, you are classified as a pattern day trader and must maintain at least $25,000 in equity in your account.

If your account falls below $25,000, you will be restricted from day trading until you restore the minimum. PDT status provides enhanced buying power of 4:1 for intraday trades (versus 2:1 for overnight positions), but it also carries higher risk.

#### Portfolio Margin

Portfolio margin is a risk-based margining system available to sophisticated investors with accounts exceeding $100,000 (some brokers require $150,000+). Unlike Reg T, which applies fixed percentages to each position, portfolio margin calculates requirements based on the actual risk of your entire portfolio using theoretical pricing models.

**How Portfolio Margin Differs from Reg T:**

- **Risk-Based Calculations.** Portfolio margin uses the Options Clearing Corporation's TIMS (Theoretical Intermarket Margin System) model to simulate the portfolio's profit and loss under various market scenarios (typically +/- 15% moves in the underlying). The margin requirement is the largest potential loss under these scenarios.

- **Hedging Is Recognized.** Under Reg T, owning a stock and a put option on that stock does not reduce your margin requirement -- each position is margined separately. Under portfolio margin, the put option reduces the portfolio's risk, so the margin requirement is lower. This recognition of hedging is portfolio margin's greatest advantage.

- **Lower Requirements for Diversified Portfolios.** A well-diversified, hedged portfolio may require as little as 15-20% margin under portfolio margin, compared to 50% under Reg T. This means significantly more buying power and potentially higher leverage ratios of 5:1 or even 6:1.

**Risks of Portfolio Margin:**

- **Higher Leverage Means Higher Risk.** While portfolio margin recognizes hedging, it also enables far more leverage than Reg T. Excessive leverage under portfolio margin can lead to devastating losses if the portfolio's risk profile changes (for example, if hedges expire or correlations increase during a crisis).

- **Requirements Can Change Quickly.** Portfolio margin requirements are recalculated dynamically. A spike in market volatility can dramatically increase your requirements overnight, potentially triggering a margin call even if your positions have not changed in value.

- **Correlation Assumptions.** The TIMS model makes assumptions about correlations between assets. During crises, actual correlations exceed model assumptions, meaning real losses can exceed what the model predicted.

#### Leveraged ETFs: A Different Kind of Leverage

Leveraged ETFs (like ProShares Ultra S&P 500, ticker SSO, which provides 2x daily S&P 500 returns, or TQQQ, which provides 3x daily NASDAQ-100 returns) offer leverage without a margin account.

**How They Work.** Leveraged ETFs use derivatives (futures, swaps) to deliver a multiple of an index's daily return. A 2x leveraged ETF aims to deliver +2% on a day the index rises 1%, and -2% on a day it falls 1%.

**The Volatility Decay Problem.** Leveraged ETFs reset daily, which creates a mathematical drag called volatility decay. In a choppy, sideways market, a 2x leveraged ETF can lose money even if the underlying index is flat over the period. This is because daily compounding of gains and losses is asymmetric -- a 10% loss followed by a 10% gain does not get you back to even (you end up at 99% of starting value), and this effect is amplified by leverage.

**Example of Volatility Decay:**
- Day 1: Index rises 5%. 2x ETF rises 10%. Index at 105, ETF at 110.
- Day 2: Index falls 4.76% (back to 100). 2x ETF falls 9.52%. Index at 100, ETF at 99.52.
- The index is flat, but the 2x ETF has lost 0.48%.

Over months or years, this decay can be substantial, which is why leveraged ETFs are designed for short-term tactical trading, not long-term holding.

#### Sensible Use of Margin

While this lesson has focused heavily on risks (appropriately so), margin can be used responsibly in certain situations:

- **Bridge Financing.** Using margin temporarily while waiting for cash to settle or a deposit to clear, with the intention of paying it off within days.
- **Tax-Efficient Borrowing.** In taxable accounts, borrowing on margin to avoid selling appreciated securities (and triggering capital gains) can make sense if the margin interest rate is low relative to the tax savings.
- **Portfolio Margin for Hedged Strategies.** Sophisticated investors who maintain hedged options portfolios benefit from portfolio margin's recognition of their actual risk profile.

The general principle: margin should be a tool for managing cash flow and implementing hedged strategies, not a tool for amplifying speculative bets.

---

### c) Common Misconceptions

**"I can lose at most the money I invested."** With margin, you can lose more than you invested. If you invest $50,000 of your own money and borrow $50,000 to buy $100,000 in stock, a decline of more than 50% means you owe money to your broker after your entire investment is wiped out. This is the fundamental difference between margin and non-recourse lending.

**"My broker will warn me before liquidating my positions."** While brokers often send margin call notices, they are under no legal obligation to do so before liquidating. In fast-moving markets, your positions may be sold without any warning. The margin agreement you signed grants your broker this right.

**"2x leveraged ETFs will double my long-term returns."** Due to volatility decay and daily rebalancing, 2x leveraged ETFs have not historically delivered 2x of the underlying index's long-term returns. In volatile markets, they can significantly underperform a simple 2x margin position held over the same period.

**"Margin is only risky for traders -- long-term investors are fine."** Long-term investors using margin face the risk that their positions decline significantly during a market crash, triggering margin calls at the worst possible time. Even if the stocks eventually recover, being forced to sell during the drawdown permanently locks in losses. The 2008 crisis destroyed many buy-and-hold investors who used margin.

**"Portfolio margin is safer because it is risk-based."** Portfolio margin provides more accurate risk measurement, but it also enables much higher leverage. Higher leverage means that when the model's assumptions are wrong -- and they will be during extreme events -- the losses are amplified. Portfolio margin is a more sophisticated tool, not a safer one.

---

### d) Q&A

**Q: What is a typical margin interest rate, and how is it charged?**
A: Margin interest rates are typically quoted as an annual rate based on the broker's base rate plus a spread that depends on the debit balance. Interactive Brokers charges among the lowest rates (often around the federal funds rate plus 1-1.5%). Traditional brokerages like Schwab and Fidelity charge higher rates, sometimes 8-12%. Interest accrues daily and is typically charged monthly. There is no set repayment schedule -- you can maintain a margin balance indefinitely as long as you meet maintenance requirements.

**Q: Can I use margin in an IRA or 401(k)?**
A: No. Retirement accounts cannot use margin for leveraged investing. However, some brokers offer "limited margin" in IRAs, which allows you to trade with unsettled funds (avoiding good faith violations) and write covered calls, but does not allow you to borrow to purchase additional securities.

**Q: How do I calculate my effective leverage ratio?**
A: Divide your total position value by your equity. If you own $150,000 in securities and have $100,000 in equity ($50,000 borrowed), your leverage ratio is 1.5:1. A leverage ratio of 1.0:1 means no leverage. Anything above 1.0:1 means you are using borrowed money. Most financial advisors recommend keeping leverage below 1.3:1 if you use margin at all.

**Q: What happens to my margin loan if the broker goes bankrupt?**
A: SIPC (Securities Investor Protection Corporation) protects your securities up to $500,000 (including $250,000 for cash) if a broker fails. However, margin loans are obligations from you to the broker and would still need to be repaid -- likely to whatever entity acquires the broker's business. This is an additional reason to use margin conservatively.

**Q: Are there tax implications for margin interest?**
A: Margin interest is tax-deductible as an investment expense, but only against net investment income (dividends, interest, and short-term capital gains). You must itemize deductions to claim this benefit. Excess margin interest can be carried forward to future years. This tax deductibility partially offsets the cost of margin borrowing for taxable accounts.

**Q: How does margin work with options?**
A: Options have their own margin requirements that differ from stock margin. Selling naked puts requires margin equal to a percentage of the underlying stock value (typically 20% of the stock price minus the option premium, with a minimum). Selling naked calls requires similar margin. Defined-risk strategies (like vertical spreads) have margin requirements equal to the maximum potential loss. Understanding options margin is essential before selling uncovered options.

---

## YouTube Script

[INTRO - 0:00]

[VISUAL: Split screen -- left side shows gains accelerating upward with leverage, right side shows losses accelerating downward]

**Alex:** Imagine you have $50,000 to invest. But what if you could invest $100,000? Or $150,000? Margin accounts make this possible -- by letting you borrow money from your broker to buy more securities.

**Sam:** It sounds great in theory. But leverage is the single most dangerous tool available to individual investors. It has created more financial devastation than any other mechanism. Today, we are covering exactly how margin works, the regulations that govern it, and the very real dangers you need to understand.

[VISUAL: Title card "Margin and Leverage: Power, Risk, and the Rules"]

---

[SECTION 1 - HOW MARGIN WORKS - 1:30]

[ANIMATION: Diagram showing a cash account ($50K buying $50K in stock) vs a margin account ($50K buying $100K in stock, with $50K borrowed from broker)]

**Alex:** In a regular cash account, you can only invest the money you have. Simple. In a margin account, you can borrow money from your broker, using your existing securities as collateral.

**Sam:** The Federal Reserve's Regulation T says you can borrow up to 50 percent of a stock's purchase price. So with $50,000 of your own money, you can buy up to $100,000 worth of stock. Your leverage is 2 to 1.

[VISUAL: Simple math: $50K equity + $50K borrowed = $100K position. Leverage ratio: 2:1]

**Alex:** Now here is what that means for your returns. If the stock goes up 10 percent, your $100,000 position is worth $110,000. Subtract the $50,000 loan, and your equity is $60,000. That is a 20 percent return on your $50,000 -- double the stock's return.

**Sam:** But the reverse is equally true. If the stock falls 10 percent, your position drops to $90,000. Equity becomes $40,000. You have lost 20 percent of your money on a 10 percent stock decline.

[ANIMATION: Two scenarios branching from initial position -- green branch showing amplified gain, red branch showing amplified loss]

**Alex:** And if the stock falls 50 percent? Your $100,000 position is worth $50,000. You still owe $50,000 to the broker. Your equity is zero. You have lost everything. And if it falls further, you actually owe money.

---

[SECTION 2 - MARGIN CALLS - 4:00]

[VISUAL: Phone screen showing a "MARGIN CALL" notification with a declining stock chart in the background]

**Sam:** The most terrifying two words in investing: margin call. When your equity falls below the maintenance margin requirement -- typically 25 to 35 percent of your position -- your broker demands that you deposit more money or securities immediately.

**Alex:** Let us use real numbers. You have $50,000 in equity and $50,000 borrowed, so a $100,000 position. Your broker's maintenance requirement is 35 percent.

[ANIMATION: Declining bar chart showing position value falling, equity shrinking, with a red line at 35% maintenance level]

**Sam:** If the stock falls 23 percent, your position is worth $76,920. Your equity is $26,920. That is 35 percent of the position value -- right at the maintenance line. Any further decline triggers a margin call.

**Alex:** And here is what most people do not realize. Your broker does not have to call you. They do not have to give you time. They can sell your positions -- whichever ones they choose -- immediately, at whatever price the market offers. That is in the margin agreement you signed.

**Sam:** During the March 2020 crash, some investors received margin calls and had positions liquidated within hours. In 2008, it was even worse. The combination of rapid declines and frozen credit markets meant margin calls cascaded through the system, forcing selling that pushed prices even lower.

[VISUAL: 2008 cascading margin call diagram: Prices Fall -> Margin Calls -> Forced Selling -> Prices Fall Further -> More Margin Calls]

---

[SECTION 3 - PATTERN DAY TRADER AND PORTFOLIO MARGIN - 7:00]

[VISUAL: Two-tier regulatory structure showing Reg T for standard margin accounts and Portfolio Margin for advanced accounts]

**Alex:** If you use margin for frequent trading, there is another regulation to know: the Pattern Day Trader rule. If you make four or more day trades in a five-day period, you are classified as a pattern day trader and must maintain at least $25,000 in your account.

**Sam:** Now, for more sophisticated investors, there is portfolio margin. This is a fundamentally different system. Instead of applying a flat 50 percent initial margin and 25 to 35 percent maintenance to every position, portfolio margin calculates your requirement based on the actual risk of your entire portfolio.

[ANIMATION: Comparison showing Reg T treating each position independently vs Portfolio Margin evaluating portfolio-level risk with correlations and hedges]

**Alex:** If you own a stock and a protective put on that stock, Reg T margins both positions separately -- as if the put does not exist for margin purposes. Portfolio margin recognizes that the put limits your downside, so it requires less margin.

**Sam:** This means portfolio margin can offer significantly more leverage for hedged portfolios -- sometimes 5 to 1 or even 6 to 1, compared to 2 to 1 under Reg T. But that extra leverage is a double-edged sword.

**Alex:** Portfolio margin requirements are recalculated dynamically. A spike in market volatility can dramatically increase your requirements overnight, even if your positions have not changed. Investors who were comfortable at 4 to 1 leverage on a quiet Tuesday might face a margin call on a volatile Wednesday morning.

---

[SECTION 4 - LEVERAGED ETFs - 9:30]

[VISUAL: Comparison chart showing actual 2x ETF performance vs theoretical 2x returns over a year]

**Sam:** There is another way to get leverage without a margin account: leveraged ETFs. These funds use derivatives to deliver a multiple of an index's daily return. A 2x S&P 500 ETF aims to go up 2 percent when the S&P goes up 1 percent, and down 2 percent when it falls 1 percent.

**Alex:** Sounds straightforward, right? But there is a hidden problem called volatility decay. Because leveraged ETFs reset daily, the compounding math works against you in choppy markets.

[ANIMATION: Simple example -- Index goes up 10%, then down 10%. Starting at $100: After up 10%, index is at $110. After down 10%, index is at $99. 2x ETF: After up 20%, at $120. After down 20%, at $96. The index lost $1, but the 2x ETF lost $4.]

**Sam:** Over a short period, this effect is small. Over months or years, it can be devastating. A 2x leveraged S&P 500 ETF held for a full year might return significantly less than twice the S&P 500's return -- or even lose money when the index is positive -- if the market was volatile.

**Alex:** This is why leveraged ETFs come with warnings that they are designed for short-term trading, not long-term investing. If you want long-term leveraged exposure, a margin account (with careful risk management) is actually more predictable than a leveraged ETF.

---

[SECTION 5 - USING LEVERAGE RESPONSIBLY - 11:30]

[VISUAL: "The Responsible Leverage Framework" with bullet points]

**Sam:** After all these warnings, is there ever a good reason to use margin? Yes, but the situations are limited.

**Alex:** First, temporary bridge financing. Using margin for a few days while waiting for cash to settle or a transfer to arrive is low-risk and often sensible. You are not speculating -- you are managing cash flow.

**Sam:** Second, tax-efficient borrowing. If you have large unrealized gains, borrowing on margin instead of selling appreciated stock can defer capital gains taxes. The margin interest (which is tax-deductible) may cost less than the tax bill from selling.

**Alex:** Third, as part of a hedged options strategy under portfolio margin. If you are running a market-neutral, hedged portfolio, portfolio margin recognizes your hedges and provides appropriate leverage.

[VISUAL: Leverage risk spectrum: Safe (no leverage) -> Moderate (1.1-1.3x for specific purposes) -> Risky (1.5-2x speculative) -> Dangerous (2x+ concentrated bets)]

**Sam:** But here are the rules if you use margin. Never use more than 1.3 to 1 leverage for long-term positions. Always know your margin call trigger price. Keep a cash reserve outside your brokerage account that you can deposit quickly if needed. And never use margin for speculative, concentrated bets.

**Alex:** The graveyard of investing is full of people who were right about the direction but wrong about the timing, and margin did not give them enough room to survive the gap between. Do not be one of them.

[VISUAL: End card with channel logo and "Next: Commodities Investing"]

**Sam:** Next time, we are exploring the world of commodities -- energy, metals, agriculture, and how to access these markets. See you there.

[END - 13:30]
