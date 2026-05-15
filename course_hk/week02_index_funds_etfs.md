<function_calls>
<invoke name="view">
<parameter name="path">C:\Users\hevan\AppData\Local\Temp\tmpdl1rt_to.md</parameter>
</invoke>
</function_calls>
<function_response>
# Week 6: Options Basics — Calls and Puts

## Overview
**Course:** From Zero to Investor
**Week:** 6 of 10
**Topic:** Options Basics — Calls and Puts
**Host:** Horace
**Duration:** ~20 minutes
**Level:** Beginner

---

## Learning Objectives

By the end of this lesson, students will be able to:

1. Explain what options are and why investors use them
2. Distinguish between call options and put options
3. Define key terms: strike price, expiration, and premium
4. Describe basic options strategies including covered calls and cash-secured puts
5. Evaluate the risks and benefits of trading options

---

## Script

### Opening Hook (0:00–1:00)

[VISUAL: Horace sitting casually, city skyline background]

**Horace:** Hey everyone! Welcome back. So last week, we talked about bonds — the "safe" part of your portfolio. But today, we're going into the deep end. We're talking about options. And yeah, I know — a lot of people hear the word "options" and immediately think: "That's for Wall Street traders, not me." But stick with me, because by the end of this video, I promise you'll see why even regular investors use options — and how they can actually reduce risk, not just add to it.

[CUT TO: animated title card "Options Basics — Calls and Puts"]

---

### Section 1: What Are Options? (1:00–3:00)

[VISUAL: Horace at whiteboard]

**Horace:** So, what are options? Here's a simple analogy. Imagine you want to buy a house. You find one you love, but you're not ready to commit yet. So you make a deal with the seller: "I'll pay you $5,000 now for the *right* to buy this house at $300,000 anytime in the next 6 months." That's it. You're not obligated to buy — but if the price shoots up to $400,000, you can still buy it for $300,000. And if prices fall? You just walk away. You lose the $5,000, but that's all.

[VISUAL: House illustration with price tags]

**Horace:** That's basically how a call option works in the stock market. You're paying for the *right* — not the obligation — to buy a stock at a specific price, before a specific date.

[ANIMATION: animation/week06_option_analogy.py]

---

### Section 2: Call Options (3:00–6:00)

[VISUAL: Horace standing, charts on screen]

**Horace:** Let's get more specific. A **call option** gives you the right to *buy* a stock at the **strike price** before the **expiration** date.

Here's an example:

> You think Apple stock (currently $150) will rise. You buy a call option with:
> - Strike price: $155
> - Expiration: 30 days
> - Premium: $3 per share (each contract = 100 shares, so $300 total)

[VISUAL: Example table on screen]

| Scenario | Stock Price at Expiry | Your Action | Profit/Loss |
|---|---|---|---|
| Stock rises to $170 | $170 | Exercise the option | ($170 - $155) × 100 - $300 = **$1,200** |
| Stock stays at $150 | $150 | Let it expire | -$300 |
| Stock falls to $130 | $130 | Let it expire | -$300 |

**Horace:** Notice something: your **maximum loss** is always capped at the **premium** you paid — $300. But your **upside is theoretically unlimited**. That asymmetry is why options are powerful.

[CUT TO: graph showing profit/loss curve for call option]

---

### Section 3: Put Options (6:00–9:00)

[VISUAL: Horace at desk]

**Horace:** Now let's flip it. A **put option** gives you the right to *sell* a stock at the strike price before expiration. Put options are often used as **insurance**.

Here's an example:

> You own 100 shares of Apple at $150. You're worried the stock might fall. You buy a put option with:
> - Strike price: $145
> - Expiration: 30 days
> - Premium: $2 per share ($200 total)

[VISUAL: Example table on screen]

| Scenario | Stock Price at Expiry | Your Action | Net Result |
|---|---|---|---|
| Stock drops to $120 | $120 | Exercise the put — sell at $145 | Saved $25/share = **$2,500 protection** (minus $200 premium) |
| Stock stays at $150 | $150 | Let it expire | Lost $200 premium |
| Stock rises to $170 | $170 | Let it expire | Lost $200, but gained on stock |

**Horace:** So the put option acted like car insurance — you pay a small premium to protect against a big loss. You hope you never need it, but it's there if things go wrong.

[CUT TO: insurance analogy animation]

---

### Section 4: Key Terms Recap (9:00–11:00)

[VISUAL: Animated glossary cards]

**Horace:** Before we go further, let's lock in the key vocabulary:

- **Strike price**: The price at which you can buy (call) or sell (put) the stock
- **Expiration**: The date the option contract ends
- **Premium**: The price you pay for the option itself
- **In the money**: The option has intrinsic value (e.g., call strike below market price)
- **Out of the money**: The option has no intrinsic value yet
- **At the money**: Strike price equals the current stock price

[ANIMATION: animation/week06_option_terms.py]

---

### Section 5: Basic Strategies — Covered Call & Cash-Secured Put (11:00–16:00)

[VISUAL: Horace at whiteboard, casual tone]

**Horace:** Okay, now I want to show you two beginner-friendly strategies that real investors use all the time — not to gamble, but to generate income.

#### Strategy 1: Covered Call

**Horace:** A **covered call** is when you *already own* the stock and you *sell* a call option against it. You collect the **premium** upfront. Here's the deal:

> You own 100 shares of Apple at $150.
> You sell a call option with strike price $160, expiration 30 days.
> You collect $2 per share = **$200 income**.

If Apple stays below $160, you keep the $200. If it rises above $160, you sell your shares at $160 — not terrible. This strategy lets you earn income on stocks you already hold.

[CUT TO: diagram of covered call payoff]

#### Strategy 2: Cash-Secured Put

**Horace:** A **cash-secured put** is when you *sell* a put option and hold enough cash to buy the shares if assigned. It's a way to potentially buy a stock at a discount.

> Apple is at $150. You want to buy it if it falls to $140.
> You sell a put with strike $140, collect $1.50 per share = **$150 income**.
> If Apple falls below $140, you buy at $140 — but you already collected $1.50, so your effective cost is **$138.50**.
> If Apple stays above $140, you just keep the $150.

[ANIMATION: animation/week06_csp_strategy.py]

---

### Section 6: Risks of Options (16:00–18:00)

[VISUAL: Horace with serious tone, sitting forward]

**Horace:** Alright, let's be real. Options can be risky — especially if you don't know what you're doing. Here are the key risks:

1. **Time decay (theta)**: Options lose value every day as expiration approaches. You're racing against the clock.
2. **Leverage**: Options control 100 shares for a fraction of the cost. This amplifies gains — but also losses.
3. **Implied volatility crush**: After big events (like earnings), implied volatility can drop sharply, reducing option value even if the stock moves the way you expected.
4. **Complexity**: Options have more variables than stocks — price, time, volatility all affect value.

**Horace:** The safest way to start? Stick to the strategies I just showed you — covered calls and cash-secured puts. These are defined-risk strategies that most brokers allow for beginner options accounts.

---

### Section 7: Practical Advice (18:00–19:30)

[VISUAL: Horace relaxed, direct to camera]

**Horace:** Here's my honest take: most long-term investors don't *need* options. But knowing how they work makes you a more complete investor. And if you do want to use them, start small — one contract at a time — and stick to stocks you understand and would own anyway.

Before you trade options:

- [ ] You understand the risks
- [ ] You've paper traded first
- [ ] You're using options on stocks you'd buy anyway
- [ ] You're not using borrowed money
- [ ] Your broker has approved your account for options

---

### Closing (19:30–20:00)

[VISUAL: Horace smiling, outro music]

**Horace:** Alright, that's a wrap on options basics! Next week, we'll talk about **portfolio construction** — how to actually put it all together. See you then!

[CUT TO: outro card with subscribe button, links to Week 5 and Week 7]

---

## Comprehension Questions

1. What is the difference between a call option and a put option?
2. If you buy a call option and the stock finishes **below** the strike price, what happens?
3. What is a covered call and how does it generate income?
4. Name two risks of trading options.
5. Why might a long-term investor use a put option?

---

## Key Vocabulary

| English | Chinese |
|---|---|
| Option | 期權 |
| Call option | 認購期權 |
| Put option | 認沽期權 |
| Strike price | 行使價 |
| Expiration | 到期日 |
| Premium | 期權金 |
| In the money | 價內 |
| Out of the money | 價外 |
| At the money | 等價 |
| Covered call | 備兌認購期權 |
| Cash-secured put | 現金擔保認沽期權 |
| Implied volatility | 引伸波幅 |

---

## Assignments

### Assignment 1: Reflection
Think of a real-world situation (not stock market) where you've paid for an "option" — the right, but not the obligation, to do something. Describe the situation and connect it to the financial concept of an option.

### Assignment 2: Practice Problem

> Apple stock is currently trading at $180. You buy one call option with:
> - Strike price: $190
> - Premium: $4 per share
> - Expiration: 45 days

Calculate:
1. Your maximum loss
2. Your break-even stock price
3. Your profit if Apple trades at $210 at expiry

### Assignment 3: Research

Look up a stock you own (or are interested in owning). Find its options chain and identify:
- An at-the-money call option
- An out-of-the-money put option
- What is the implied volatility for each?

---

*End of Week 6 Script*
</parameter>
</invoke>
</function_calls>
<function_response>
Successfully viewed file
</parameter>
</invoke>
</function_calls>

# 第六週：期權基礎——認購期權與認沽期權

## 概覽
**課程：** 從零開始學投資
**週次：** 第6週，共10週
**主題：** 期權基礎——認購期權與認沽期權
**主持人：** 陳馬
**時長：** 約20分鐘
**程度：** 初級

---

## 學習目標

完成本課後，學員將能夠：

1. 解釋期權是什麼，以及投資者為何使用期權
2. 區分認購期權與認沽期權
3. 定義關鍵術語：行使價、到期日及期權金
4. 描述基本期權策略，包括備兌認購期權及現金擔保認沽期權
5. 評估期權交易的風險與優勢

---

## 腳本

### 開場鉤子（0:00–1:00）

[VISUAL: 陳馬輕鬆坐著，城市天際線背景]

**陳馬：** 大家好！歡迎回來。上週我們講了債券——你投資組合中「較穩陣」的部分。但今日，我們要深入一些。今日講的是期權。我知道——好多人一聽到「期權」這個詞，立刻就會想：「那是華爾街交易員的玩意，同我有咩關係？」但係請跟住我，因為到這個影片結尾，我保證你會明白，為何就連普通投資者也會用期權——以及它其實可以降低風險，而不只是增加風險。

[CUT TO: 動態標題卡「期權基礎——認購期權與認沽期權」]

---

### 第一節：期權是什麼？（1:00–3:00）

[VISUAL: 陳馬在白板前]

**陳馬：** 期權到底是什麼？用個簡單的比喻。想像你想買一棟房子。你找到一間心儀的，但還未準備好正式承諾。於是你同賣家達成一個協議：「我現在付你5,000美元，換取在未來6個月內，以30萬美元購買這棟房子的**權利**。」就係咁。你沒有義務買——但如果樓價漲到40萬美元，你仍然可以以30萬買入。如果樓價下跌？你大可以走人。你損失了5,000美元，但就只係咁。

[VISUAL: 房子插圖，附有價格標籤]

**陳馬：** 這基本上就是股票市場中認購期權的運作方式。你支付的是一種**權利**——而非義務——在特定日期之前，以特定價格買入股票。

[ANIMATION: animation/week06_option_analogy.py]

---

### 第二節：認購期權（3:00–6:00）

[VISUAL: 陳馬站立，螢幕顯示圖表]

**陳馬：** 我們說得更具體一點。**認購期權**賦予你在**到期日**之前，以**行使價***買入*股票的權利。

舉個例子：

> 你認為蘋果股票（目前150美元）將會上漲。你買入一份認購期權，條件如下：
> - 行使價：155美元
> - 到期日：30天後
> - 期權金：每股3美元（每份合約＝100股，即總共300美元）

[VISUAL: 螢幕顯示範例表格]

| 情境 | 到期時股價 | 你的行動 | 盈虧 |
|---|---|---|---|
| 股價升至170美元 | 170美元 | 行使期權 | （170 - 155）× 100 - 300 = **1,200美元** |
| 股價維持150美元 | 150美元 | 讓期權到期 | -300美元 |
| 股價跌至130美元 | 130美元 | 讓期權到期 | -300美元 |

**陳馬：** 留意一件事：你的**最大損失**始終上限是你支付的**期權金**——300美元。但你的**潛在回報理論上無上限**。這種不對稱性，正是期權強大之處。

[CUT TO: 顯示認購期權盈虧曲線的圖表]

---

### 第三節：認沽期權（6:00–9:00）

[VISUAL: 陳馬在桌前]

**陳馬：** 現在反過來看。**認沽期權**賦予你在到期日之前，以行使價*賣出*股票的權利。認沽期權通常用作**保險**。

舉個例子：

> 你持有100股蘋果股票，買入價150美元。你擔心股價可能下跌。你買入一份認沽期權，條件如下：
> - 行使價：145美元
> - 到期日：30天後
> - 期權金：每股2美元（總共200美元）

[VISUAL: 螢幕顯示範例表格]

| 情境 | 到期時股價 | 你的行動 | 最終結果 |
|---|---|---|---|
| 股價跌至120美元 | 120美元 | 行使認沽期權——以145美元賣出 | 每股節省25美元 = **2,500美元保護**（扣除200美元期權金） |
| 股價維持150美元 | 150美元 | 讓期權到期 | 損失200美元期權金 |
| 股價升至170美元 | 170美元 | 讓期權到期 | 損失200美元，但股票升值 |

**陳馬：** 所以認沽期權就像汽車保險——你付小額期權金，以防範重大損失。你希望永遠用不上它，但萬一出事，它就派上用場了。

[CUT TO: 保險比喻動畫]

---

### 第四節：關鍵術語回顧（9:00–11:00）

[VISUAL: 動態詞彙卡片]

**陳馬：** 在繼續之前，我們先鞏固關鍵詞彙：

- **行使價**：你可以買入（認購）或賣出（認沽）股票的價格
- **到期日**：期權合約結束的日期
- **期權金**：你為期權本身支付的價格
- **價內**：期權具有內在價值（例如認購期權的行使價低於市價）
- **價外**：期權尚未具備內在價值
- **等價**：行使價等於當前股價

[ANIMATION: animation/week06_option_terms.py]

---

### 第五節：基本策略——備兌認購期權與現金擔保認沽期權（11:00–16:00）

[VISUAL: 陳馬在白板前，語調輕鬆]

**陳馬：** 好，現在我想介紹兩個入門級策略，這些都是真正的投資者常用的——不是用來賭博，而是用來產生收入。

#### 策略一：備兌認購期權

**陳馬：** **備兌認購期權**是指你*已持有*股票，然後*賣出*一份認購期權。你提前收取**期權金**。情況是這樣的：

> 你持有100股蘋果股票，買入價150美元。
> 你賣出一份行使價160美元、到期日30天的認購期權。
> 你每股收取2美元 = **200美元收入**。

如果蘋果股價維持在160美元以下，你保留200美元。如果升破160美元，你以160美元賣出股份——也不算差。這個策略讓你在持有股票的同時，賺取額外收入。

[CUT TO: 備兌認購期權盈虧圖]

#### 策略二：現金擔保認沽期權

**陳馬：** **現金擔保認沽期權**是指你*賣出*一份認沽期權，並持有足夠現金，以便在被行使時買入股份。這是一種以折扣價潛在買入股票的方式。

> 蘋果股價為150美元。你希望在跌至140美元時買入。
> 你賣出一份行使價140美元的認沽期權，每股收取1.50美元 = **150美元收入**。
> 如果蘋果跌破140美元，你以140美元買入——但你已收取1.50美元，所以實際成本只需 **138.50美元**。
> 如果蘋果維持在140美元以上，你只需保留那150美元。

[ANIMATION: animation/week06_csp_strategy.py]

---

### 第六節：期權的風險（16:00–18:00）

[VISUAL: 陳馬神情認真，身體前傾]

**陳馬：** 好，我們說說實話。期權可以很危險——尤其是在你不清楚自己在做什麼的情況下。以下是主要風險：

1. **時間值損耗（Theta）**：期權每天都在隨著到期日臨近而貶值。你是在跟時鐘賽跑。
2. **槓桿**：期權以極低的成本控制100股股份。這會放大盈利——但同樣放大虧損。
3. **引伸波幅收縮**：在重大事件（如業績公布）後，引伸波幅可能急劇下降，即使股價按你預期方向移動，期權價值也可能縮水。
4. **複雜性**：期權的變數比股票更多——股價、時間、波動性都影響其價值。

**陳馬：** 最安全的入門方法？堅持我剛才介紹的策略——備兌認購期權和現金擔保認沽期權。這些是風險有限的策略，大多數經紀商都允許初級期權帳戶使用。

---

### 第七節：實用建議（18:00–19:30）

[VISUAL: 陳馬放鬆，直視鏡頭]

**陳馬：** 說說我的真實看法：大多數長線投資者其實不*需要*期權。但了解其運作原理，會讓你成為更全面的投資者。如果你真的想使用期權，從小做起——每次一份合約——並專注於你了解、且無論如何也願意持有的股票。

在你交易期權之前：

- [ ] 你了解相關風險
- [ ] 你已先進行模擬交易
- [ ] 你將期權用於你願意買入的股票
- [ ] 你沒有使用借來的資金
- [ ] 你的經紀商已批准你的帳戶進行期權交易

---

### 結尾（19:30–20:00）

[VISUAL: 陳馬微笑，片尾音樂響起]

**陳馬：** 好了，期權基礎就到這裡！下週我們將討論**投資組合構建**——如何將所有知識融合起來付諸實踐。下週見！

[CUT TO: 片尾卡，附訂閱按鈕及第五週和第七週連結]

---

## 理解測驗

1. 認購期權與認沽期權有何分別？
2. 如果你買入認購期權，而股價在**低於**行使價的情況下到期，會發生什麼事？
3. 備兌認購期權是什麼？它如何產生收入？
4. 說出期權交易的兩項風險。
5. 為何長線投資者可能會使用認沽期權？

---

## 關鍵詞彙

| 英文 | 中文 |
|---|---|
| Option | 期權 |
| Call option | 認購期權 |
| Put option | 認沽期權 |
| Strike price | 行使價 |
| Expiration | 到期日 |
| Premium | 期權金 |
| In the money | 價內 |
| Out of the money | 價外 |
| At the money | 等價 |
| Covered call | 備兌認購期權 |
| Cash-secured put | 現金擔保認沽期權 |
| Implied volatility | 引伸波幅 |

---

## 作業

### 作業一：反思
想想現實生活中（非股票市場）你曾為一個「期權」付費的情況——即擁有做某事的權利，但沒有義務。描述該情況，並將其與期權的金融概念聯繫起來。

### 作業二：練習題

> 蘋果股票目前以180美元交易。你買入一份認購期權，條件如下：
> - 行使價：190美元
> - 期權金：每股4美元
> - 到期日：45天後

計算：
1. 你的最大損失
2. 你的損益平衡股價
3. 如果蘋果在到期時以210美元交易，你的盈利

### 作業三：研究

找出你持有（或有興趣持有）的一隻股票。查閱其期權鏈，找出：
- 一份等價認購期權
- 一份價外認沽期權
- 兩者各自的引伸波幅是多少？

---

*第六週腳本完*