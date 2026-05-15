<function_calls>
<invoke name="view">
<parameter name="path">C:\Users\hevan\AppData\Local\Temp\tmp3vt5i2ed.md</parameter>
</invoke>
</function_calls>
<function_response>
# Week 13: Options Strategies – Covered Calls & Cash-Secured Puts

## Episode Metadata
- **Course**: Chan & Main Invest
- **Week**: 13
- **Topic**: Options Strategies – Covered Calls & Cash-Secured Puts
- **Hosts**: Horace (experienced investor) & Stella (learning alongside the audience)
- **Format**: YouTube educational script (Cantonese-flavored Traditional Chinese target)
- **Duration**: ~15 minutes
- **Prerequisites**: Week 12 (Options Basics)

---

## Learning Objectives

By the end of this episode, viewers will be able to:
1. Explain what a covered call strategy is and when to use it
2. Explain what a cash-secured put strategy is and when to use it
3. Identify the profit/loss profiles of both strategies
4. Recognize real-world scenarios where income-generating options strategies are appropriate

---

## Script

### [SCENE 1 — INTRO]

**Horace:** Hey everyone! Welcome back to Chan & Main Invest. I'm Horace.

**Stella:** And I'm Stella! Last week, Horace walked us through the basics of options — what they are, how they work, the difference between calls and puts. Today we're taking it to the next level.

**Horace:** That's right. Today's episode is all about using options not just to speculate — but to *generate income*. Two strategies: covered calls and cash-secured puts.

**Stella:** And the cool part? These are strategies that long-term, buy-and-hold investors actually use in the real world — not just traders glued to screens all day.

**Horace:** Exactly. So let's jump in!

---

### [SCENE 2 — RECAP: OPTIONS BASICS]

**Horace:** Quick recap from last week. What's an option?

**Stella:** It's a contract that gives you the *right*, but not the *obligation*, to buy or sell a stock at a specific price — the strike price — before or on the expiration date.

**Horace:** Right. A call option gives you the right to *buy*. A put option gives you the right to *sell*.

**Stella:** And the buyer of the option pays a *premium* to the seller.

**Horace:** Exactly. Today, we're going to be on the *selling* side of options — and that's where the income comes from.

[VISUAL: Simple recap diagram — Call vs Put, Buyer vs Seller]

---

### [SCENE 3 — COVERED CALLS]

**Horace:** Alright, let's start with covered calls.

**Stella:** So... what's a covered call?

**Horace:** A covered call is when you *own shares* of a stock, and you *sell a call option* on those shares.

**Stella:** Wait — you're selling someone else the right to buy your shares?

**Horace:** Exactly. And in exchange, they pay you a premium. You keep that premium no matter what.

**Stella:** So you're getting paid while you wait?

**Horace:** That's the idea. Here's a simple example. Let's say I own 100 shares of XYZ stock, currently trading at $50 per share.

**Stella:** Okay.

**Horace:** I sell a call option with a strike price of $55, expiring next month. The buyer pays me $2 per share as a premium. That's $200 in my pocket right now.

**Stella:** And what happens next?

**Horace:** Two scenarios. Scenario one: XYZ stays below $55 at expiration. The option expires worthless. I keep my $200 premium AND my shares.

**Stella:** Nice! Free money!

**Horace:** Well, not completely free — but yes, the premium is yours to keep. Scenario two: XYZ shoots up past $55 — say to $65. The buyer exercises the option. I have to sell my shares at $55.

**Stella:** Even though the stock is worth $65?

**Horace:** Right. I miss out on those gains above $55. That's called *capped upside*. My maximum gain is the $200 premium plus $500 in stock appreciation — from $50 to $55 — so $700 total on a 100-share position.

**Stella:** But I lose the chance to gain from $55 to $65.

**Horace:** Exactly. That's the trade-off. You're exchanging potential upside for guaranteed income now.

[VISUAL: Covered call profit/loss diagram]
[ANIMATION: animation/week13_covered_call.py]

---

### [SCENE 4 — WHEN TO USE COVERED CALLS]

**Horace:** So when does a covered call actually make sense?

**Stella:** When you don't think the stock will shoot up dramatically?

**Horace:** Exactly. Covered calls work best when:
- You already own the stock
- You're *neutral to mildly bullish* — you don't expect a huge run-up
- You're okay selling at the strike price if the stock gets called away
- You want to generate extra income from a position you're already holding

**Stella:** What if I'm super bullish on the stock?

**Horace:** Then don't sell the call! You'd be limiting your upside for a relatively small premium. Covered calls are for when you think the stock is going to stay relatively flat — or move up *a little*.

**Stella:** Got it. It's like collecting rent on a house you already own.

**Horace:** That's a great analogy! You own the property, you rent it out, you collect income — but if a buyer comes in at the price you agreed to, you have to sell.

[VISUAL: House analogy diagram]

---

### [SCENE 5 — CASH-SECURED PUTS]

**Horace:** Now let's flip it around. Cash-secured puts.

**Stella:** Is this like the opposite of a covered call?

**Horace:** In a way! With a cash-secured put, you *sell a put option* — and you set aside enough cash to buy the shares if you get assigned.

**Stella:** Why would someone sell a put?

**Horace:** Here's the idea. Let's say I *want* to buy XYZ stock — but I'd love to buy it at $45 instead of the current $50.

**Stella:** So you're hoping for a discount?

**Horace:** Right. So I sell a put option with a strike price of $45. The buyer pays me a $1.50 premium — that's $150 on 100 shares. And I keep $4,500 in cash ready, just in case I have to buy those shares.

**Stella:** And what happens?

**Horace:** Scenario one: XYZ stays above $45. The put expires worthless. I keep my $150 premium and my cash. I didn't buy the stock — but I got paid to *wait*.

**Stella:** Love it!

**Horace:** Scenario two: XYZ drops below $45 — say to $38. The buyer exercises their put. I *have* to buy 100 shares at $45 — even though the market price is $38.

**Stella:** Ouch. So I'm buying at a loss?

**Horace:** Well — you wanted to buy it at $45 anyway, right? And your effective cost is even lower: $45 minus $1.50 premium = $43.50 per share.

**Stella:** Oh! The premium reduces my cost basis.

**Horace:** Exactly. Cash-secured puts are a way to get paid while waiting to buy a stock at a price you want.

[VISUAL: Cash-secured put profit/loss diagram]
[ANIMATION: animation/week13_cash_secured_put.py]

---

### [SCENE 6 — WHEN TO USE CASH-SECURED PUTS]

**Horace:** So when does a cash-secured put make sense?

**Stella:** When you want to buy a stock but at a lower price?

**Horace:** Right. It works best when:
- You *want* to own the stock at a lower price
- You're *neutral to mildly bullish* on the stock
- You have the cash available to buy it if assigned
- You're okay owning the stock even if it drops further

**Stella:** What's the risk?

**Horace:** The risk is the stock drops way below the strike price. If XYZ crashes from $50 to $10, you're still buying at $45 — a massive paper loss. The premium barely covers it.

**Stella:** So you need to believe in the stock long-term.

**Horace:** Exactly. Never sell a put on a stock you wouldn't want to own. That's a golden rule.

[VISUAL: Risk warning callout]

---

### [SCENE 7 — SIDE BY SIDE COMPARISON]

**Horace:** Let's put these two strategies side by side.

**Stella:** Great idea!

| | Covered Call | Cash-Secured Put |
|---|---|---|
| **Position** | Own stock, sell call | Hold cash, sell put |
| **Income** | Premium from call sale | Premium from put sale |
| **Obligation** | Sell shares at strike | Buy shares at strike |
| **Best case** | Stock stays flat, keep premium | Stock stays flat, keep premium |
| **Risk** | Missing upside above strike | Buying stock above market price |
| **Ideal for** | Existing stockholder | Wants to buy stock at discount |

**Stella:** So both strategies involve selling options and collecting premiums. The difference is whether you already own the stock or you're trying to buy it.

**Horace:** Perfect summary. And together, these two strategies form a *wheel strategy* — you can cycle between them as stock prices move.

**Stella:** Whoa — what's the wheel strategy?

**Horace:** We'll cover that in a future episode! But the idea is: sell cash-secured puts until you get assigned stock, then sell covered calls on that stock until it gets called away — and repeat.

[VISUAL: Wheel strategy diagram teaser]

---

### [SCENE 8 — PRACTICAL TIPS]

**Horace:** Before we wrap up, a few practical tips for beginners using these strategies.

**Stella:** Hit me!

**Horace:** One — *only sell covered calls on stocks you're happy to hold long-term*. If you'd be devastated to have it called away, don't do it.

**Stella:** Makes sense.

**Horace:** Two — *only sell cash-secured puts on stocks you'd be happy to own*. If you wouldn't want to hold 100 shares at that price, skip it.

**Stella:** Because you might get assigned!

**Horace:** Exactly. Three — *start with short-dated options*. 30 to 45 days until expiration (DTE) is a popular sweet spot for time decay.

**Stella:** Why?

**Horace:** Options lose time value faster as expiration approaches. Selling options with 30–45 DTE captures that decay efficiently.

**Horace:** Four — *don't try to squeeze out the last few cents*. If your option has lost most of its value early, buy it back and reset. Don't wait for a reversal to wipe out your gains.

**Stella:** Take profits early. Got it.

**Horace:** Five — *know your margin and cash requirements*. Covered calls and cash-secured puts are the "safe" versions. Don't get tempted to go naked without understanding the unlimited risk.

**Stella:** Naked options — that's a topic for another day!

**Horace:** Definitely. For now — keep it covered and cash-secured!

[VISUAL: Tips summary card]

---

### [SCENE 9 — OUTRO]

**Horace:** Alright, that's a wrap on Week 13!

**Stella:** We covered covered calls — pun intended — and cash-secured puts. Two powerful income-generating strategies that real investors use.

**Horace:** If you want to practice without real money, paper trade these strategies first. Most brokers offer paper trading accounts.

**Stella:** And don't forget — options trading does carry risk. Make sure you understand the full picture before using real money.

**Horace:** Next week, we're going deeper into more complex options strategies. We'll look at spreads — vertical spreads, iron condors, and more.

**Stella:** Ooh, that sounds exciting and slightly terrifying!

**Horace:** Ha! It's not as scary as it sounds. Until then — keep learning, keep investing!

**Stella:** See you next week!

[CUT TO: End card with subscribe button, links to Week 12 and Week 14]

---

## Key Concepts Summary

| Concept | Definition |
|---|---|
| Covered Call | Selling a call option on shares you already own |
| Cash-Secured Put | Selling a put option while holding cash to buy shares if assigned |
| Premium | The income received from selling an option |
| Strike Price | The agreed price at which shares can be bought or sold |
| Expiration | The date the option contract ends |
| Capped Upside | Limited profit potential when selling covered calls |
| Assignment | When the option buyer exercises, forcing the seller to act |
| Wheel Strategy | Cycling between cash-secured puts and covered calls |

---

## Discussion Questions

1. You own 100 shares of ABC stock at $80. The stock is at $85 now. Would you sell a covered call at a $90 strike for $2 premium? What are your risks?
2. XYZ is trading at $100. You'd love to own it at $90. Would a cash-secured put at $90 for a $3 premium make sense? What could go wrong?
3. What type of investor (risk tolerance, goals, portfolio size) do you think benefits most from these income strategies?

---

## Visual Assets Required

- [ ] Week 13 Covered Call P&L Diagram
- [ ] Week 13 Cash-Secured Put P&L Diagram
- [ ] Wheel Strategy Teaser Diagram
- [ ] Side-by-side comparison table (graphic version)
- [ ] Practical tips summary card

---

## Notes for Production

- Add Hong Kong market examples (e.g., HSI blue chips, H-shares) as overlays where possible
- Stella's reactions should feel natural — not scripted surprise, but genuine curiosity
- Horace should pause after explaining key concepts to let ideas land
- Consider a "common mistake" callout during Scene 6
</parameter>
</invoke>
</function_calls>
<function_response>
Success
</parameter>
</invoke>
</function_calls>

# 第13週：期權策略——備兌認購期權與現金擔保認沽期權

## 集數資料
- **課程**：Chan & Main Invest
- **週次**：第13週
- **主題**：期權策略——備兌認購期權與現金擔保認沽期權
- **主持**：陳馬（資深投資者）及小魚（與觀眾一同學習）
- **形式**：YouTube 教育劇本（目標語言：粵語風味繁體中文）
- **時長**：約15分鐘
- **先決條件**：第12週（期權基礎）

---

## 學習目標

完成本集後，觀眾將能夠：
1. 解釋備兌認購期權策略的概念及適用時機
2. 解釋現金擔保認沽期權策略的概念及適用時機
3. 識別兩種策略的盈虧狀況
4. 辨認現實情境中適合使用這些創造收入期權策略的場合

---

## 劇本

### [SCENE 1 — INTRO]

**陳馬：** 大家好！歡迎回到 Chan & Main Invest。我係陳馬。

**小魚：** 我係小魚！上週陳馬帶大家了解了期權的基礎知識——係乜嘢、點運作、認購期權同認沽期權的分別。今日我哋要更上一層樓。

**陳馬：** 係的。今集係要講點樣用期權*創造收入*，而唔單止係投機。兩個策略：備兌認購期權同現金擔保認沽期權。

**小魚：** 最正嘅係？呢啲係長線、買入持有型投資者喺現實世界真正會用的策略——唔係只係成日盯住屏幕嘅交易員先識用。

**陳馬：** 冇錯。咁我哋開始啦！

---

### [SCENE 2 — 重溫：期權基礎]

**陳馬：** 快速重溫一下上週內容。期權係乜嘢？

**小魚：** 係一份合約，賦予你*權利*，但唔係*義務*，喺到期日前或當日以特定價格——行使價——買入或沽出一隻股票。

**陳馬：** 係。認購期權給你*買入*的權利。認沽期權給你*沽出*的權利。

**小魚：** 而期權買家要向賣家支付*期權金*。

**陳馬：** 正係。今日，我哋會站喺期權的*賣方*——收入就係由此而來。

[VISUAL: 簡單重溫圖解——認購期權對認沽期權、買方對賣方]

---

### [SCENE 3 — 備兌認購期權]

**陳馬：** 好，我哋先講備兌認購期權。

**小魚：** 咁……備兌認購期權係乜嘢？

**陳馬：** 備兌認購期權係當你*持有股票*，同時*沽出該股票的認購期權*。

**小魚：** 等等——你係賣咗個期權畀別人買你的股票？

**陳馬：** 正係。而換來的係，對方支付期權金畀你。不論之後發生乜嘢，你都袋住這筆期權金。

**小魚：** 即係話你喺等待期間照樣收錢？

**陳馬：** 就係呢個概念。舉個簡單例子。假設我持有100股 XYZ 股票，現時每股交易價$50。

**小魚：** 好。

**陳馬：** 我沽出一個行使價$55、下個月到期的認購期權。買家每股付我$2期權金，即係即時收$200入袋。

**小魚：** 之後會點呢？

**陳馬：** 兩個情境。情境一：XYZ 喺到期時仍低於$55。期權到期變廢紙。我保留$200期權金，同時繼續持有股票。

**小魚：** 正！免費的錢！

**陳馬：** 唔完全係免費——但係，期權金確實歸你所有。情境二：XYZ 急升至$55以上——例如升到$65。買家行使期權。我要以$55沽出股票。

**小魚：** 即使股票值$65？

**陳馬：** 係。我錯失了$55以上的升幅。呢個叫做*上升潛力受限*。以100股倉位計，最大盈利係$200期權金加上股價由$50升至$55的$500增值——合共$700。

**小魚：** 但我失去了由$55到$65的盈利機會。

**陳馬：** 正係。這就是取捨。你用潛在升幅換取即時保證收入。

[VISUAL: 備兌認購期權盈虧圖]
[ANIMATION: animation/week13_covered_call.py]

---

### [SCENE 4 — 何時使用備兌認購期權]

**陳馬：** 咁備兌認購期權真正適合幾時使用？

**小魚：** 當你唔認為股票會大幅上升的時候？

**陳馬：** 正係。備兌認購期權最適合以下情況：
- 你已持有該股票
- 你對後市*中性至略為看好*——不預期大幅上升
- 你願意以行使價沽出股票（即使被執行）
- 你想從現有持倉中產生額外收入

**小魚：** 如果我非常看好這隻股票呢？

**陳馬：** 那就唔好賣認購期權！你會為了相對少量的期權金而限制自己的上升潛力。備兌認購期權適合你預期股票走勢相對平穩——或*輕微*上升的情況。

**小魚：** 明白了。就好似收你已擁有房屋的租金一樣。

**陳馬：** 呢個比喻好正！你擁有物業，你出租，你收取租金——但如果買家以你議定的價格出現，你就要賣出。

[VISUAL: 房屋比喻圖解]

---

### [SCENE 5 — 現金擔保認沽期權]

**陳馬：** 好，宜家反過來講。現金擔保認沽期權。

**小魚：** 呢個係備兌認購期權的反面嗎？

**陳馬：** 某程度上係！現金擔保認沽期權係你*沽出認沽期權*——同時預留足夠現金，以便被指派時可以買入股票。

**小魚：** 點解有人會沽出認沽期權？

**陳馬：** 就係呢個概念。假設我*想買* XYZ 股票——但希望以$45買入，而唔係現價$50。

**小魚：** 即係你希望以折扣價買入？

**陳馬：** 係。所以我沽出行使價$45的認沽期權。買家付我$1.50期權金——100股即係$150。同時我預留$4,500現金，以備萬一需要買入股票。

**小魚：** 之後會點呢？

**陳馬：** 情境一：XYZ 維持在$45以上。認沽期權到期變廢紙。我保留$150期權金及現金。我冇買到股票——但我*等待期間有收錢*。

**小魚：** 超正！

**陳馬：** 情境二：XYZ 跌穿$45——例如跌到$38。買家行使認沽期權。我*必須*以$45買入100股——即使市場價格係$38。

**小魚：** 唉。即係我蝕錢買入？

**陳馬：** 不過——你本來就想以$45買入，對嗎？而你的實際成本仲要更低：$45減$1.50期權金 = 每股$43.50。

**小魚：** 哦！期權金降低了我的成本基礎。

**陳馬：** 正係。現金擔保認沽期權係一種方法，讓你在等待以理想價格買入股票的同時收取報酬。

[VISUAL: 現金擔保認沽期權盈虧圖]
[ANIMATION: animation/week13_cash_secured_put.py]

---

### [SCENE 6 — 何時使用現金擔保認沽期權]

**陳馬：** 咁現金擔保認沽期權適合幾時使用？

**小魚：** 當你想以較低價格買入某股票的時候？

**陳馬：** 係。最適合以下情況：
- 你*希望*以較低價格持有該股票
- 你對後市*中性至略為看好*
- 你有足夠現金在被指派時買入股票
- 即使股票進一步下跌，你亦願意持有

**小魚：** 風險係乜嘢？

**陳馬：** 風險係股票大幅跌穿行使價。如果 XYZ 由$50急挫至$10，你仍要以$45買入——造成巨大帳面虧損。期權金根本唔夠補償。

**小魚：** 所以你必須長線看好這隻股票。

**陳馬：** 正係。絕對唔好對一隻你唔願意持有的股票沽出認沽期權。呢係金科玉律。

[VISUAL: 風險警告提示框]

---

### [SCENE 7 — 並排比較]

**陳馬：** 我哋將兩個策略並排比較一下。

**小魚：** 好主意！

| | 備兌認購期權 | 現金擔保認沽期權 |
|---|---|---|
| **持倉** | 持有股票，沽出認購期權 | 持有現金，沽出認沽期權 |
| **收入** | 認購期權沽出所得期權金 | 認沽期權沽出所得期權金 |
| **義務** | 以行使價沽出股份 | 以行使價買入股份 |
| **最佳情況** | 股票橫行，保留期權金 | 股票橫行，保留期權金 |
| **風險** | 錯失行使價以上升幅 | 以高於市價買入股票 |
| **適合** | 現有股票持有人 | 希望以折扣價買入股票者 |

**小魚：** 即係兩個策略都涉及沽出期權及收取期權金。分別在於你是否已持有股票，還是想買入股票。

**陳馬：** 總結得好。而這兩個策略合在一起，形成了*輪動策略*——你可以隨股價變動在兩者之間循環操作。

**小魚：** 嘩——輪動策略係乜嘢？

**陳馬：** 我哋日後會專門講！但概念係：持續沽出現金擔保認沽期權，直至被指派股票，然後對該股票沽出備兌認購期權，直至股票被取走——如此循環往復。

[VISUAL: 輪動策略圖解預告]

---

### [SCENE 8 — 實用貼士]

**陳馬：** 結束前，給初學者幾個實用貼士。

**小魚：** 說來聽聽！

**陳馬：** 第一——*只對你願意長線持有的股票沽出備兌認購期權*。如果你無法接受股票被取走，就唔好做。

**小魚：** 有道理。

**陳馬：** 第二——*只對你願意持有的股票沽出現金擔保認沽期權*。如果你唔想以該價格持有100股，就唔好碰。

**小魚：** 因為你可能會被指派！

**陳馬：** 正係。第三——*從短期期權開始*。距到期日（DTE）30至45天是時間值衰減的常用甜蜜點。

**小魚：** 點解？

**陳馬：** 期權越臨近到期，時間值流失越快。沽出30至45 DTE的期權，可以有效捕捉這種時間值衰減。

**陳馬：** 第四——*唔好為了最後幾毫子而戀戰*。如果你的期權提前大幅貶值，就買回平倉，重新部署。唔好等待反轉把你的盈利都蝕光。

**小魚：** 提早止賺。明白。

**陳馬：** 第五——*了解你的保證金及現金要求*。備兌認購期權及現金擔保認沽期權係「安全」版本。在充分了解裸期權的無限風險之前，切勿輕易嘗試。

**小魚：** 裸期權——那是另一天的話題！

**陳馬：** 肯定係。現在——保持備兌及現金擔保就好！

[VISUAL: 貼士總結卡片]

---

### [SCENE 9 — 結尾]

**陳馬：** 好，第13週到此結束！

**小魚：** 我哋講了備兌認購期權——雙關語intended——同現金擔保認沽期權。兩個真實投資者使用的強大創收策略。

**陳馬：** 如果你想在不冒真實資金風險的情況下練習，可以先進行模擬交易。大多數經紀都提供模擬交易帳戶。

**小魚：** 記住——期權交易確實存在風險。在使用真實資金之前，務必充分了解全貌。

**陳馬：** 下週，我哋會深入探討更複雜的期權策略。我哋會研究價差策略——垂直價差、鐵鷹式策略等等。

**小魚：** 哦，聽起來既令人興奮又略有點嚇人！

**陳馬：** 哈！其實唔係想像中那麼可怕。下次見——繼續學習，繼續投資！

**小魚：** 下週見！

[CUT TO: End card with subscribe button, links to Week 12 and Week 14]

---

## 重點概念總結

| 概念 | 定義 |
|---|---|
| 備兌認購期權 | 對你已持有的股份沽出認購期權 |
| 現金擔保認沽期權 | 在預留現金的情況下沽出認沽期權，以備被指派時買入股份 |
| 期權金 | 沽出期權所收取的收入 |
| 行使價 | 雙方議定的股份買賣價格 |
| 到期日 | 期權合約終止的日期 |
| 上升潛力受限 | 沽出備兌認購期權時有限的潛在盈利 |
| 指派 | 期權買家行使期權，迫使賣家履行義務 |
| 輪動策略 | 在現金擔保認沽期權與備兌認購期權之間循環操作 |

---

## 討論問題

1. 你以$80買入 ABC 股票100股。股票現時報$85。你會以$2期權金沽出行使價$90的備兌認購期權嗎？你的風險是什麼？
2. XYZ 現時報$100。你很想以$90買入。以$3期權金沽出行使價$90的現金擔保認沽期權是否合理？可能出現什麼問題？
3. 你認為哪類型的投資者（風險承受能力、目標、投資組合規模）最能受益於這些創收策略？

---

## 所需視覺素材

- [ ] 第13週備兌認購期權盈虧圖
- [ ] 第13週現金擔保認沽期權盈虧圖
- [ ] 輪動策略預告圖
- [ ] 並排比較表（圖形版本）
- [ ] 實用貼士總結卡片

---

## 製作備注

- 在適當位置加入香港市場例子（例如：恒生指數藍籌股、H股）作疊加說明
- 小魚的反應應感覺自然——唔係刻意製造的驚訝，而係真實的好奇
- 陳馬在解釋重點概念後應稍作停頓，讓觀眾消化
- 考慮在第6場景加入「常見錯誤」提示框