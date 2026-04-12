"""
Week 37: Leverage Effect -- Stock Return vs Call Option Return
================================================================
Compares the percentage return of holding stock vs holding a call
option for the same underlying price move. Demonstrates how options
provide leveraged exposure.

Output: week37_leverage_payoff.png
"""

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Parameters
# -------------------------------------------------------------------
stock_entry = 100       # bought stock at $100
call_strike = 100       # ATM call
call_premium = 5        # paid $5 for the call
shares = 1              # one share vs one contract for simplicity

# -------------------------------------------------------------------
# Stock price range at expiration
# -------------------------------------------------------------------
stock_prices = np.linspace(80, 130, 300)

# -------------------------------------------------------------------
# Return calculations
# -------------------------------------------------------------------
# Stock percentage return
stock_return_pct = ((stock_prices - stock_entry) / stock_entry) * 100

# Call option P&L
call_pnl = np.maximum(stock_prices - call_strike, 0) - call_premium

# Call option percentage return (based on premium paid)
call_return_pct = (call_pnl / call_premium) * 100

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ---- Left panel: Dollar P&L comparison ---------------------------
ax1.plot(stock_prices, stock_prices - stock_entry, color="#2196F3",
         linewidth=2.5, label="Stock P&L ($)")
ax1.plot(stock_prices, call_pnl, color="#FF5722", linewidth=2.5,
         label=f"Call Option P&L ($) [Premium=${call_premium}]")

ax1.axhline(0, color="grey", linewidth=0.8)
ax1.axvline(stock_entry, color="grey", linewidth=0.8, linestyle=":")

# Shade the option's max loss
ax1.fill_between(stock_prices, -call_premium, call_pnl,
                 where=stock_prices <= call_strike,
                 color="#FF5722", alpha=0.1)

ax1.annotate(f"Max Loss = ${call_premium}\n(Premium Paid)",
             xy=(90, -call_premium), xytext=(83, -15),
             fontsize=9, fontweight="bold", color="#FF5722",
             arrowprops=dict(arrowstyle="->", color="#FF5722", lw=1.2))

ax1.set_title("Dollar Profit / Loss", fontsize=12, fontweight="bold")
ax1.set_xlabel("Stock Price at Expiration ($)", fontsize=11)
ax1.set_ylabel("P&L ($)", fontsize=11)
ax1.legend(fontsize=9, loc="upper left")
ax1.grid(True, alpha=0.3)
ax1.set_xlim(80, 130)
ax1.set_ylim(-25, 30)

# ---- Right panel: Percentage return comparison --------------------
ax2.plot(stock_prices, stock_return_pct, color="#2196F3",
         linewidth=2.5, label="Stock Return (%)")
ax2.plot(stock_prices, call_return_pct, color="#FF5722",
         linewidth=2.5, label="Call Option Return (%)")

ax2.axhline(0, color="grey", linewidth=0.8)
ax2.axvline(stock_entry, color="grey", linewidth=0.8, linestyle=":")

# Example annotation: +10% stock move
stock_at_110 = 110
stock_ret_110 = ((stock_at_110 - stock_entry) / stock_entry) * 100
call_pnl_110 = max(stock_at_110 - call_strike, 0) - call_premium
call_ret_110 = (call_pnl_110 / call_premium) * 100

ax2.annotate(
    f"Stock +{stock_ret_110:.0f}%\nCall +{call_ret_110:.0f}%",
    xy=(stock_at_110, call_ret_110),
    xytext=(stock_at_110 + 5, call_ret_110 + 50),
    fontsize=10, fontweight="bold", color="#FF5722",
    arrowprops=dict(arrowstyle="->", color="#FF5722", lw=1.5),
)

# Leverage ratio annotation
leverage = call_ret_110 / stock_ret_110
ax2.text(0.02, 0.95,
         f"Leverage at $110:\n{leverage:.1f}x stock return",
         transform=ax2.transAxes, fontsize=10, fontweight="bold",
         verticalalignment="top", color="#D84315",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#FBE9E7", alpha=0.9))

# Max loss annotation for call
ax2.axhline(-100, color="#FF5722", linewidth=0.8, linestyle="--", alpha=0.5)
ax2.text(82, -90, "Call max loss = -100%\n(lose entire premium)",
         fontsize=8, color="#FF5722")

ax2.set_title("Percentage Return (Leverage Effect)",
              fontsize=12, fontweight="bold")
ax2.set_xlabel("Stock Price at Expiration ($)", fontsize=11)
ax2.set_ylabel("Return (%)", fontsize=11)
ax2.legend(fontsize=9, loc="upper left")
ax2.grid(True, alpha=0.3)
ax2.set_xlim(80, 130)
ax2.set_ylim(-150, 500)

# -------------------------------------------------------------------
# Suptitle
# -------------------------------------------------------------------
fig.suptitle("Stock vs Call Option: The Leverage Effect",
             fontsize=14, fontweight="bold", y=1.02)

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week37_leverage_payoff.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week37_leverage_payoff.png")
