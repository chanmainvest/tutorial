<function_calls>
<invoke name="view">
<parameter name="filename">C:\Users\hevan\AppData\Local\Temp\tmpqmd__0wo.md</parameter>
</invoke>
</function_calls>
<function_response>
# Week 10: Options Strategies — Covered Calls and Cash-Secured Puts

## Overview

**Host:** Horace
**Duration:** ~18 minutes
**Visual Style:** Clean whiteboard animations with option payoff diagrams

---

## Learning Objectives

By the end of this lesson, viewers will be able to:

- Understand what covered calls and cash-secured puts are
- Know when to use each strategy
- Calculate potential profit, loss, and breakeven points
- Recognize the tradeoffs involved

---

## Script

### [INTRO]

**Horace:** Hey everyone, welcome back! Today we're diving into two of the most popular options strategies for regular investors: the covered call and the cash-secured put.

These are often called "conservative" options strategies — not because they're risk-free, but because they're relatively straightforward and can actually *reduce* your risk compared to just holding stock.

By the end of this video, you'll understand exactly how they work, when to use them, and what the tradeoffs are.

[VISUAL: Title card — "Covered Calls and Cash-Secured Puts"]

---

### [SECTION 1: Quick Options Recap]

**Horace:** Before we dive in, let's do a super quick recap of options basics — just enough to understand today's strategies.

[VISUAL: Split screen — Call option on left, Put option on right]

An **option** is a contract that gives you the *right* — but not the *obligation* — to buy or sell a stock at a specific price, called the **strike price**, before a certain **expiration** date.

A **call option** gives you the right to *buy*.
A **put option** gives you the right to *sell*.

And when you sell an option instead of buying it, you collect a **premium** — that's the income side of these strategies.

[VISUAL: Simple diagram — "Buyer pays premium → Seller receives premium"]

**Horace:** Today, we're focusing on the *selling* side. You're going to be the option seller — the one collecting premium.

---

### [SECTION 2: Covered Call]

**Horace:** Alright, let's start with the **covered call**.

[VISUAL: Whiteboard — "Covered Call = Own Stock + Sell Call Option"]

#### What Is It?

A covered call means you:
1. **Own** at least 100 shares of a stock
2. **Sell** a call option on that stock

You collect a premium upfront. In exchange, you agree to sell your shares at the strike price if the buyer exercises the option.

The word "covered" means your short call is *covered* by the shares you already own — you're not making a naked bet.

[VISUAL: Example setup]

#### Example

Let's say you own 100 shares of a stock currently trading at **$50**.

You sell a **call option** with:
- Strike price: **$55**
- Expiration: **30 days out**
- Premium collected: **$1.50 per share** = **$150 total**

[VISUAL: Payoff diagram — Covered Call]

#### What Can Happen?

**Scenario 1 — Stock stays flat or drops:**
The call expires worthless. You keep the $150 premium. Your shares are still yours.

**Scenario 2 — Stock rises above $55:**
The option is exercised. You sell your shares at $55. You miss out on any gains above $55, but you still collected the $150 premium.

**Scenario 3 — Stock drops a lot:**
The call expires worthless, and you keep the premium. But you're still losing money on the stock itself. The $150 helps offset the loss, but it's not full protection.

[VISUAL: Summary table]

| Scenario | Stock Price at Expiry | Result |
|---|---|---|
| Flat/Down | ≤ $55 | Keep premium, hold shares |
| Up | > $55 | Sell at $55 + keep premium |
| Big drop | Way down | Keep premium, lose on stock |

#### Key Metrics

- **Maximum gain** = Premium + (Strike − Purchase price) × 100
- **Breakeven** = Purchase price − Premium per share
- **Maximum loss** = Purchase price − Premium (stock goes to zero)

[VISUAL: Formula cards]

#### When to Use It

Use a covered call when:
- You're **neutral to mildly bullish** on the stock
- You're **OK selling** the stock at the strike price
- You want to **generate extra income** from your holdings

[VISUAL: "Covered Call Checklist"]

**Horace:** Think of it this way: you're saying, *"I'll take the $150 now, and I'm fine capping my upside at $55."* If the stock rockets to $70, you'll miss those gains. That's the tradeoff.

---

### [SECTION 3: Cash-Secured Put]

**Horace:** Now let's look at the other strategy: the **cash-secured put**.

[VISUAL: Whiteboard — "Cash-Secured Put = Hold Cash + Sell Put Option"]

#### What Is It?

A cash-secured put means you:
1. **Set aside cash** equal to 100 × the strike price
2. **Sell** a put option on a stock you *want* to own

You collect premium. If the stock drops below the strike price, you're obligated to *buy* the shares at that price. But you wanted to buy them anyway — and you're buying at a discount.

[VISUAL: Example setup]

#### Example

A stock is trading at **$50**. You'd love to own it at **$45**.

You sell a **put option** with:
- Strike price: **$45**
- Expiration: **30 days out**
- Premium collected: **$1.00 per share** = **$100 total**

You set aside $4,500 in cash (100 × $45) in case you need to buy.

[VISUAL: Payoff diagram — Cash-Secured Put]

#### What Can Happen?

**Scenario 1 — Stock stays above $45:**
The put expires worthless. You keep the $100 premium. You never had to buy the stock.

**Scenario 2 — Stock drops to $45 or below:**
You're assigned and buy 100 shares at $45. Your actual cost is $45 − $1 = **$44 per share** because of the premium.

**Scenario 3 — Stock crashes:**
You buy at $45 even if the stock is now at $30. That's a significant unrealized loss. The $100 premium helps a little, but it's not much protection.

[VISUAL: Summary table]

| Scenario | Stock Price at Expiry | Result |
|---|---|---|
| Above $45 | > $45 | Keep premium, no shares |
| At or below | ≤ $45 | Buy shares at $44 effective cost |
| Big crash | Way down | Stuck with shares at a loss |

#### Key Metrics

- **Maximum gain** = Premium collected
- **Breakeven** = Strike price − Premium per share
- **Maximum loss** = (Strike price − Premium) × 100 (stock goes to zero)

[VISUAL: Formula cards]

#### When to Use It

Use a cash-secured put when:
- You **want to own** the stock but at a lower price
- You're **willing to be patient** — maybe it doesn't drop and you just collect premium
- You have **cash sitting idle** and want to put it to work

[VISUAL: "Cash-Secured Put Checklist"]

**Horace:** Think of it like this: you're saying, *"I want to buy this stock, but only if it drops to $45. Until then, pay me $100 for the right to sell it to me."*

---

### [SECTION 4: Comparing the Two Strategies]

**Horace:** Now that we've seen both strategies individually, let's compare them side by side.

[VISUAL: Side-by-side comparison table]

| | Covered Call | Cash-Secured Put |
|---|---|---|
| **Starting position** | Own 100 shares | Hold cash |
| **Action** | Sell call | Sell put |
| **Income** | Premium collected | Premium collected |
| **Obligation** | Sell shares at strike | Buy shares at strike |
| **Best case** | Stock stays below strike | Stock stays above strike |
| **Risk** | Stock drops significantly | Stock drops significantly |

**Horace:** Notice something interesting? These two strategies are actually *synthetically equivalent* in certain conditions — a concept from options theory called **put-call parity**. But for practical purposes, the key difference is your *starting position*: stock versus cash.

[VISUAL: "Put-Call Parity" annotation with a brief tooltip]

---

### [SECTION 5: The Wheel Strategy]

**Horace:** Here's a bonus concept that combines both strategies: it's called **the wheel**.

[VISUAL: Circular diagram — "The Wheel Strategy"]

Here's how it works:

1. **Sell a cash-secured put** on a stock you want to own
2. If assigned → you now own shares
3. **Sell a covered call** on those shares
4. If called away → you're back to cash
5. Repeat from step 1

[VISUAL: Wheel cycle animation]

The idea is to continuously collect premium whether you hold stock or cash. It's a popular income strategy, though it has real risks if the stock trends down sharply.

---

### [SECTION 6: Real Risks to Know]

**Horace:** Before you run off to try these, let me be very clear about the risks.

[VISUAL: Warning card — "Real Risks"]

**Risk 1 — Assignment risk:**
You can be assigned early (before expiration) on American-style options. It's rare, but it happens — especially around ex-dividend dates.

**Risk 2 — Opportunity cost:**
With covered calls, if the stock surges, you're capped. You gave up those gains.

**Risk 3 — Stock risk dominates:**
Both strategies don't protect you from a big stock decline. The premium you collect is relatively small compared to a 30% drop.

**Risk 4 — Tax complexity:**
Selling options can create short-term capital gains or affect your holding period on the stock. Consult a tax professional.

[VISUAL: Risk summary list]

---

### [SECTION 7: Practical Tips]

**Horace:** Alright, let's wrap up with some practical tips for using these strategies.

[VISUAL: Tips card]

1. **Choose liquid stocks or ETFs** — Options on illiquid stocks have wide bid-ask spreads that eat into your premium.

2. **Start with stocks you already own or want to own** — Don't use these strategies on stocks you wouldn't hold outright.

3. **Use 30–45 day expirations** — This is the sweet spot for time decay (theta). Premium erodes fastest in the last month.

4. **Strike selection matters** — Out-of-the-money strikes are most common. Too close = higher premium but higher chance of assignment. Too far = low premium, not worth it.

5. **Paper trade first** — Practice with a simulated account before using real money.

[VISUAL: Tips list animation]

---

### [OUTRO]

**Horace:** And that's covered calls and cash-secured puts! These are two powerful tools — especially for investors who already have a portfolio and want to add an income layer.

Just remember: options add complexity. They're not magic. Use them only when you understand the tradeoffs.

If you found this helpful, give it a thumbs up and subscribe. Next week, we'll look at vertical spreads — a way to define your risk on both sides.

See you then!

[VISUAL: End card with subscribe button and next video preview]

---

## Supplementary Notes

### Glossary

| Term | Definition |
|---|---|
| Covered call | Selling a call option on shares you already own |
| Cash-secured put | Selling a put option backed by cash to buy shares |
| Assignment | When the option buyer exercises their right, obligating you to fulfill the contract |
| Premium | The price paid/received for an option |
| Strike price | The price at which the option can be exercised |
| Expiration | The date the option contract ends |
| Theta | The rate at which an option loses value over time (time decay) |
| Put-call parity | A financial relationship that links put and call option prices |

### Key Formulas

**Covered Call:**
- Max Gain = (Strike − Entry Price + Premium) × 100
- Breakeven = Entry Price − Premium
- Max Loss = (Entry Price − Premium) × 100

**Cash-Secured Put:**
- Max Gain = Premium × 100
- Breakeven = Strike − Premium
- Max Loss = (Strike − Premium) × 100

### Common Mistakes

1. Selling covered calls on stocks you don't want to sell
2. Using cash-secured puts on stocks you don't actually want to own
3. Ignoring the bid-ask spread when entering/exiting
4. Forgetting about early assignment risk
5. Treating premium income as "free money" — it comes with obligations

</parameter>
</invoke>
</function_calls>
<function_response>
# Week 10: Options Strategies — Covered Calls and Cash-Secured Puts

## Overview

**Host:** Horace
**Duration:** ~18 minutes
**Visual Style:** Clean whiteboard animations with option payoff diagrams

---

## Learning Objectives

By the end of this lesson, viewers will be able to:

- Understand what covered calls and cash-secured puts are
- Know when to use each strategy
- Calculate potential profit, loss, and breakeven points
- Recognize the tradeoffs involved

---

## Script

### [INTRO]

**Horace:** Hey everyone, welcome back! Today we're diving into two of the most popular options strategies for regular investors: the covered call and the cash-secured put.

These are often called "conservative" options strategies — not because they're risk-free, but because they're relatively straightforward and can actually *reduce* your risk compared to just holding stock.

By the end of this video, you'll understand exactly how they work, when to use them, and what the tradeoffs are.

[VISUAL: Title card — "Covered Calls and Cash-Secured Puts"]

---

### [SECTION 1: Quick Options Recap]

**Horace:** Before we dive in, let's do a super quick recap of options basics — just enough to understand today's strategies.

[VISUAL: Split screen — Call option on left, Put option on right]

An **option** is a contract that gives you the *right* — but not the *obligation* — to buy or sell a stock at a specific price, called the **strike price**, before a certain **expiration** date.

A **call option** gives you the right to *buy*.
A **put option** gives you the right to *sell*.

And when you sell an option instead of buying it, you collect a **premium** — that's the income side of these strategies.

[VISUAL: Simple diagram — "Buyer pays premium → Seller receives premium"]

**Horace:** Today, we're focusing on the *selling* side. You're going to be the option seller — the one collecting premium.

---

### [SECTION 2: Covered Call]

**Horace:** Alright, let's start with the **covered call**.

[VISUAL: Whiteboard — "Covered Call = Own Stock + Sell Call Option"]

#### What Is It?

A covered call means you:
1. **Own** at least 100 shares of a stock
2. **Sell** a call option on that stock

You collect a premium upfront. In exchange, you agree to sell your shares at the strike price if the buyer exercises the option.

The word "covered" means your short call is *covered* by the shares you already own — you're not making a naked bet.

[VISUAL: Example setup]

#### Example

Let's say you own 100 shares of a stock currently trading at **$50**.

You sell a **call option** with:
- Strike price: **$55**
- Expiration: **30 days out**
- Premium collected: **$1.50 per share** = **$150 total**

[VISUAL: Payoff diagram — Covered Call]

#### What Can Happen?

**Scenario 1 — Stock stays flat or drops:**
The call expires worthless. You keep the $150 premium. Your shares are still yours.

**Scenario 2 — Stock rises above $55:**
The option is exercised. You sell your shares at $55. You miss out on any gains above $55, but you still collected the $150 premium.

**Scenario 3 — Stock drops a lot:**
The call expires worthless, and you keep the premium. But you're still losing money on the stock itself. The $150 helps offset the loss, but it's not full protection.

[VISUAL: Summary table]

| Scenario | Stock Price at Expiry | Result |
|---|---|---|
| Flat/Down | ≤ $55 | Keep premium, hold shares |
| Up | > $55 | Sell at $55 + keep premium |
| Big drop | Way down | Keep premium, lose on stock |

#### Key Metrics

- **Maximum gain** = Premium + (Strike − Purchase price) × 100
- **Breakeven** = Purchase price − Premium per share
- **Maximum loss** = Purchase price − Premium (stock goes to zero)

[VISUAL: Formula cards]

#### When to Use It

Use a covered call when:
- You're **neutral to mildly bullish** on the stock
- You're **OK selling** the stock at the strike price
- You want to **generate extra income** from your holdings

[VISUAL: "Covered Call Checklist"]

**Horace:** Think of it this way: you're saying, *"I'll take the $150 now, and I'm fine capping my upside at $55."* If the stock rockets to $70, you'll miss those gains. That's the tradeoff.

---

### [SECTION 3: Cash-Secured Put]

**Horace:** Now let's look at the other strategy: the **cash-secured put**.

[VISUAL: Whiteboard — "Cash-Secured Put = Hold Cash + Sell Put Option"]

#### What Is It?

A cash-secured put means you:
1. **Set aside cash** equal to 100 × the strike price
2. **Sell** a put option on a stock you *want* to own

You collect premium. If the stock drops below the strike price, you're obligated to *buy* the shares at that price. But you wanted to buy them anyway — and you're buying at a discount.

[VISUAL: Example setup]

#### Example

A stock is trading at **$50**. You'd love to own it at **$45**.

You sell a **put option** with:
- Strike price: **$45**
- Expiration: **30 days out**
- Premium collected: **$1.00 per share** = **$100 total**

You set aside $4,500 in cash (100 × $45) in case you need to buy.

[VISUAL: Payoff diagram — Cash-Secured Put]

#### What Can Happen?

**Scenario 1 — Stock stays above $45:**
The put expires worthless. You keep the $100 premium. You never had to buy the stock.

**Scenario 2 — Stock drops to $45 or below:**
You're assigned and buy 100 shares at $45. Your actual cost is $45 − $1 = **$44 per share** because of the premium.

**Scenario 3 — Stock crashes:**
You buy at $45 even if the stock is now at $30. That's a significant unrealized loss. The $100 premium helps a little, but it's not much protection.

[VISUAL: Summary table]

| Scenario | Stock Price at Expiry | Result |
|---|---|---|
| Above $45 | > $45 | Keep premium, no shares |
| At or below | ≤ $45 | Buy shares at $44 effective cost |
| Big crash | Way down | Stuck with shares at a loss |

#### Key Metrics

- **Maximum gain** = Premium collected
- **Breakeven** = Strike price − Premium per share
- **Maximum loss** = (Strike price − Premium) × 100 (stock goes to zero)

[VISUAL: Formula cards]

#### When to Use It

Use a cash-secured put when:
- You **want to own** the stock but at a lower price
- You're **willing to be patient** — maybe it doesn't drop and you just collect premium
- You have **cash sitting idle** and want to put it to work

[VISUAL: "Cash-Secured Put Checklist"]

**Horace:** Think of it like this: you're saying, *"I want to buy this stock, but only if it drops to $45. Until then, pay me $100 for the right to sell it to me."*

---

### [SECTION 4: Comparing the Two Strategies]

**Horace:** Now that we've seen both strategies individually, let's compare them side by side.

[VISUAL: Side-by-side comparison table]

| | Covered Call | Cash-Secured Put |
|---|---|---|
| **Starting position** | Own 100 shares | Hold cash |
| **Action** | Sell call | Sell put |
| **Income** | Premium collected | Premium collected |
| **Obligation** | Sell shares at strike | Buy shares at strike |
| **Best case** | Stock stays below strike | Stock stays above strike |
| **Risk** | Stock drops significantly | Stock drops significantly |

**Horace:** Notice something interesting? These two strategies are actually *synthetically equivalent* in certain conditions — a concept from options theory called **put-call parity**. But for practical purposes, the key difference is your *starting position*: stock versus cash.

[VISUAL: "Put-Call Parity" annotation with a brief tooltip]

---

### [SECTION 5: The Wheel Strategy]

**Horace:** Here's a bonus concept that combines both strategies: it's called **the wheel**.

[VISUAL: Circular diagram — "The Wheel Strategy"]

Here's how it works:

1. **Sell a cash-secured put** on a stock you want to own
2. If assigned → you now own shares
3. **Sell a covered call** on those shares
4. If called away → you're back to cash
5. Repeat from step 1

[VISUAL: Wheel cycle animation]

The idea is to continuously collect premium whether you hold stock or cash. It's a popular income strategy, though it has real risks if the stock trends down sharply.

---

### [SECTION 6: Real Risks to Know]

**Horace:** Before you run off to try these, let me be very clear about the risks.

[VISUAL: Warning card — "Real Risks"]

**Risk 1 — Assignment risk:**
You can be assigned early (before expiration) on American-style options. It's rare, but it happens — especially around ex-dividend dates.

**Risk 2 — Opportunity cost:**
With covered calls, if the stock surges, you're capped. You gave up those gains.

**Risk 3 — Stock risk dominates:**
Both strategies don't protect you from a big stock decline. The premium you collect is relatively small compared to a 30% drop.

**Risk 4 — Tax complexity:**
Selling options can create short-term capital gains or affect your holding period on the stock. Consult a tax professional.

[VISUAL: Risk summary list]

---

### [SECTION 7: Practical Tips]

**Horace:** Alright, let's wrap up with some practical tips for using these strategies.

[VISUAL: Tips card]

1. **Choose liquid stocks or ETFs** — Options on illiquid stocks have wide bid-ask spreads that eat into your premium.

2. **Start with stocks you already own or want to own** — Don't use these strategies on stocks you wouldn't hold outright.

3. **Use 30–45 day expirations** — This is the sweet spot for time decay (theta). Premium erodes fastest in the last month.

4. **Strike selection matters** — Out-of-the-money strikes are most common. Too close = higher premium but higher chance of assignment. Too far = low premium, not worth it.

5. **Paper trade first** — Practice with a simulated account before using real money.

[VISUAL: Tips list animation]

---

### [OUTRO]

**Horace:** And that's covered calls and cash-secured puts! These are two powerful tools — especially for investors who already have a portfolio and want to add an income layer.

Just remember: options add complexity. They're not magic. Use them only when you understand the tradeoffs.

If you found this helpful, give it a thumbs up and subscribe. Next week, we'll look at vertical spreads — a way to define your risk on both sides.

See you then!

[VISUAL: End card with subscribe button and next video preview]

---

## Supplementary Notes

### Glossary

| Term | Definition |
|---|---|
| Covered call | Selling a call option on shares you already own |
| Cash-secured put | Selling a put option backed by cash to buy shares |
| Assignment | When the option buyer exercises their right, obligating you to fulfill the contract |
| Premium | The price paid/received for an option |
| Strike price | The price at which the option can be exercised |
| Expiration | The date the option contract ends |
| Theta | The rate at which an option loses value over time (time decay) |
| Put-call parity | A financial relationship that links put and call option prices |

### Key Formulas

**Covered Call:**
- Max Gain = (Strike − Entry Price + Premium) × 100
- Breakeven = Entry Price − Premium
- Max Loss = (Entry Price − Premium) × 100

**Cash-Secured Put:**
- Max Gain = Premium × 100
- Breakeven = Strike − Premium
- Max Loss = (Strike − Premium) × 100

### Common Mistakes

1. Selling covered calls on stocks you don't want to sell
2. Using cash-secured puts on stocks you don't actually want to own
3. Ignoring the bid-ask spread when entering/exiting
4. Forgetting about early assignment risk
5. Treating premium income as "free money" — it comes with obligations
</parameter>
</invoke>
</function_calls>
<function_response>
Here is the file content.
</parameter>
</invoke>
</function_calls>

# 第十週：選擇權策略 — 掩護性買權與現金擔保賣權

## 概覽

**主持人：** 陳馬
**時長：** 約 18 分鐘
**視覺風格：** 簡潔的白板動畫搭配選擇權損益圖

---

## 學習目標

完成本課後，觀眾將能夠：

- 了解掩護性買權與現金擔保賣權的概念
- 知道何時使用各種策略
- 計算潛在獲利、損失與損益平衡點
- 認識其中的取捨關係

---

## 腳本

### [INTRO]

**陳馬：** 大家好，歡迎回來！今天我們要深入探討兩種最受一般投資人歡迎的選擇權策略：掩護性買權和現金擔保賣權。

這兩種策略常被稱為「保守型」選擇權策略——不是因為沒有風險，而是因為它們相對直觀易懂，而且與單純持有股票相比，實際上可以*降低*你的風險。

看完這支影片，你就能完全理解它們的運作方式、適用時機，以及其中的取捨。

[VISUAL: Title card — "Covered Calls and Cash-Secured Puts"]

---

### [SECTION 1: 選擇權快速複習]

**陳馬：** 在進入正題之前，我們先快速複習一下選擇權的基本概念——只需要了解到足以理解今天策略的程度就好。

[VISUAL: Split screen — Call option on left, Put option on right]

**選擇權**是一種合約，賦予你*權利*——但非*義務*——在特定**履約價**、於某個**到期日**之前買入或賣出一支股票。

**買權**讓你有權利*買入*。
**賣權**讓你有權利*賣出*。

而當你賣出選擇權而非買入時，你可以收取**權利金**——這就是這些策略的收益來源。

[VISUAL: Simple diagram — "Buyer pays premium → Seller receives premium"]

**陳馬：** 今天，我們聚焦在*賣方*這一側。你將扮演選擇權賣方——那個收取權利金的人。

---

### [SECTION 2: 掩護性買權]

**陳馬：** 好，我們先從**掩護性買權**說起。

[VISUAL: Whiteboard — "Covered Call = Own Stock + Sell Call Option"]

#### 什麼是掩護性買權？

掩護性買權是指你：
1. **持有**至少 100 股某支股票
2. **賣出**該股票的買權

你預先收取權利金。作為交換，如果買方行使選擇權，你同意以履約價賣出你的持股。

「掩護」這個詞，意思是你的空頭買權部位有你已持有的股份作為*擔保*——你不是在做裸賣操作。

[VISUAL: Example setup]

#### 範例

假設你持有 100 股某支目前交易價格為 **$50** 的股票。

你賣出一個**買權**，條件如下：
- 履約價：**$55**
- 到期日：**30 天後**
- 收取權利金：**每股 $1.50** = **共 $150**

[VISUAL: Payoff diagram — Covered Call]

#### 可能的情況？

**情境一 — 股價持平或下跌：**
買權到期失效。你保留 $150 的權利金。持股依然在你手中。

**情境二 — 股價漲超 $55：**
選擇權被行使。你以 $55 賣出持股。你錯過了 $55 以上的漲幅，但你仍收取了 $150 的權利金。

**情境三 — 股價大跌：**
買權到期失效，你保留了權利金。但你在股票本身上是虧損的。$150 有助於抵消部分損失，但並非完整保護。

[VISUAL: Summary table]

| 情境 | 到期時股價 | 結果 |
|---|---|---|
| 持平／下跌 | ≤ $55 | 保留權利金，持有股票 |
| 上漲 | > $55 | 以 $55 賣出 + 保留權利金 |
| 大幅下跌 | 大幅走低 | 保留權利金，股票虧損 |

#### 關鍵指標

- **最大獲利** = 權利金 +（履約價 − 買入價）× 100
- **損益平衡點** = 買入價 − 每股權利金
- **最大損失** = 買入價 − 權利金（股價跌至零）

[VISUAL: Formula cards]

#### 適用時機

在以下情況使用掩護性買權：
- 你對股票的看法是**中性至溫和看多**
- 你**願意**在履約價賣出該股票
- 你想從持股中**產生額外收益**

[VISUAL: "Covered Call Checklist"]

**陳馬：** 這樣想吧：你等於是在說，*「我現在就拿那 $150，而且我可以接受把上漲空間封頂在 $55。」* 如果股票飆到 $70，你會錯過那段漲幅。這就是取捨所在。

---

### [SECTION 3: 現金擔保賣權]

**陳馬：** 現在來看另一個策略：**現金擔保賣權**。

[VISUAL: Whiteboard — "Cash-Secured Put = Hold Cash + Sell Put Option"]

#### 什麼是現金擔保賣權？

現金擔保賣權是指你：
1. **預留現金**，金額等於 100 × 履約價
2. **賣出**你*想持有*的股票的賣權

你收取權利金。如果股價跌破履約價，你有義務以該價格*買入*股份。但你本來就想買——而且是以折扣價買進。

[VISUAL: Example setup]

#### 範例

某支股票目前交易價格為 **$50**。你很希望能在 **$45** 買進。

你賣出一個**賣權**，條件如下：
- 履約價：**$45**
- 到期日：**30 天後**
- 收取權利金：**每股 $1.00** = **共 $100**

你預留 $4,500 現金（100 × $45），以備需要買入時使用。

[VISUAL: Payoff diagram — Cash-Secured Put]

#### 可能的情況？

**情境一 — 股價維持在 $45 以上：**
賣權到期失效。你保留 $100 的權利金。你從未需要買入股票。

**情境二 — 股價跌至 $45 或以下：**
你被指派，以 $45 買入 100 股。由於收取了權利金，你的實際成本為 $45 − $1 = **每股 $44**。

**情境三 — 股價崩跌：**
即使股價現在是 $30，你仍須以 $45 買入。這是相當可觀的未實現損失。$100 的權利金只能提供一點點緩衝，保護相當有限。

[VISUAL: Summary table]

| 情境 | 到期時股價 | 結果 |
|---|---|---|
| 高於 $45 | > $45 | 保留權利金，未持有股票 |
| 等於或低於 $45 | ≤ $45 | 以有效成本 $44 買入股票 |
| 大幅崩跌 | 大幅走低 | 被套牢，持股虧損 |

#### 關鍵指標

- **最大獲利** = 收取的權利金
- **損益平衡點** = 履約價 − 每股權利金
- **最大損失** =（履約價 − 權利金）× 100（股價跌至零）

[VISUAL: Formula cards]

#### 適用時機

在以下情況使用現金擔保賣權：
- 你**想持有**該股票，但希望在更低的價格買進
- 你**願意耐心等待**——也許股票沒有下跌，你就只是收取了權利金
- 你有**閒置現金**想讓它發揮作用

[VISUAL: "Cash-Secured Put Checklist"]

**陳馬：** 這樣理解：你等於是在說，*「我想買這支股票，但只在跌到 $45 時才買。在那之前，付我 $100 作為把它賣給我的權利金。」*

---

### [SECTION 4: 兩種策略的比較]

**陳馬：** 現在我們分別了解了這兩種策略，讓我們並排比較一下。

[VISUAL: Side-by-side comparison table]

| | 掩護性買權 | 現金擔保賣權 |
|---|---|---|
| **起始部位** | 持有 100 股 | 持有現金 |
| **操作** | 賣出買權 | 賣出賣權 |
| **收益** | 收取權利金 | 收取權利金 |
| **義務** | 以履約價賣出股份 | 以履約價買入股份 |
| **最佳情況** | 股價維持在履約價以下 | 股價維持在履約價以上 |
| **風險** | 股價大幅下跌 | 股價大幅下跌 |

**陳馬：** 注意到有趣的地方了嗎？這兩種策略在特定條件下實際上是*合成等價*的——這是選擇權理論中稱為**買賣權平價關係**的概念。但從實務角度來看，關鍵差異在於你的*起始部位*：股票還是現金。

[VISUAL: "Put-Call Parity" annotation with a brief tooltip]

---

### [SECTION 5: 滾輪策略]

**陳馬：** 這裡有個結合兩種策略的進階概念：它叫做**滾輪策略**。

[VISUAL: Circular diagram — "The Wheel Strategy"]

運作方式如下：

1. **賣出現金擔保賣權**，標的為你想持有的股票
2. 若被指派 → 你現在持有股份
3. **賣出掩護性買權**，標的為那些股份
4. 若股份被買走 → 你回到持有現金的狀態
5. 從第一步重新開始

[VISUAL: Wheel cycle animation]

這個構想是無論你持有股票還是現金，都能持續收取權利金。這是一種廣受歡迎的收益策略，不過如果股票持續向下趨勢，也存在真實風險。

---

### [SECTION 6: 你必須了解的真實風險]

**陳馬：** 在你急著去嘗試這些策略之前，讓我非常清楚地說明風險所在。

[VISUAL: Warning card — "Real Risks"]

**風險一 — 被指派的風險：**
美式選擇權可能在到期前被提前指派。這種情況很少見，但確實會發生——尤其是在**除息日**前後。

**風險二 — 機會成本：**
在掩護性買權策略中，如果股票大漲，你的獲利是封頂的。你放棄了那些漲幅。

**風險三 — 股票風險佔主導：**
這兩種策略都無法保護你免受股票大幅下跌的損失。你收取的權利金相較於 30% 的跌幅來說相當有限。

**風險四 — 稅務複雜性：**
賣出選擇權可能產生短期資本利得，或影響你持有股票的期間計算。請諮詢稅務專業人員。

[VISUAL: Risk summary list]

---

### [SECTION 7: 實用建議]

**陳馬：** 好了，讓我們用一些使用這些策略的實用建議來做個總結。

[VISUAL: Tips card]

1. **選擇流動性高的股票或指數股票型基金** — 流動性差的股票的選擇權有很寬的買賣價差，會侵蝕你的權利金收益。

2. **從你已持有或想持有的股票開始** — 不要在你不願意直接持有的股票上使用這些策略。

3. **使用 30 至 45 天的到期日** — 這是時間損耗（theta）的最佳甜蜜點。權利金在最後一個月衰減最快。

4. **履約價的選擇很重要** — 價外履約價是最常見的選擇。太靠近目前股價 = 權利金較高但被指派的機率也更高。太遠 = 權利金太低，不划算。

5. **先用模擬帳戶練習** — 在使用真實資金之前，先用虛擬帳戶練習操作。

[VISUAL: Tips list animation]

---

### [OUTRO]

**陳馬：** 以上就是掩護性買權和現金擔保賣權的全部內容！這是兩個強大的工具——尤其適合已經有投資組合、想增加收益層次的投資人。

記住：選擇權會增加複雜性。它們不是魔法。只有在你完全理解取捨關係的情況下才使用它們。

如果你覺得這個內容有幫助，請按讚並訂閱。下週，我們將探討垂直價差——一種可以同時限定兩側風險的方法。

下週見！

[VISUAL: End card with subscribe button and next video preview]

---

## 補充資料

### 名詞解釋

| 術語 | 定義 |
|---|---|
| 掩護性買權 | 針對你已持有的股份賣出買權 |
| 現金擔保賣權 | 以現金作為擔保賣出賣權，用以買入股份 |
| 指派 | 選擇權買方行使其權利，迫使你履行合約義務 |
| 權利金 | 選擇權的買入／賣出價格 |
| 履約價 | 可行使選擇權的價格 |
| 到期日 | 選擇權合約的結束日期 |
| Theta | 選擇權隨時間流逝而損失價值的速率（時間損耗） |
| 買賣權平價關係 | 連結買權與賣權價格的金融關係 |

### 關鍵公式

**掩護性買權：**
- 最大獲利 =（履約價 − 買入價 + 權利金）× 100
- 損益平衡點 = 買入價 − 權利金
- 最大損失 =（買入價 − 權利金）× 100

**現金擔保賣權：**
- 最大獲利 = 權利金 × 100
- 損益平衡點 = 履約價 − 權利金
- 最大損失 =（履約價 − 權利金）× 100

### 常見錯誤

1. 對你不願意賣出的股票賣出掩護性買權
2. 對你實際上不想持有的股票使用現金擔保賣權
3. 進場或出場時忽視買賣價差
4. 忘記提前被指派的風險
5. 將權利金收益視為「免費的錢」——它伴隨著義務而來