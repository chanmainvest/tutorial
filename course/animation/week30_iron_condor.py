"""
Week 30: Iron Condor Payoff Diagram
=====================================
Shows the classic iron condor payoff with:
  - Max profit zone (between short strikes)
  - Two breakeven points
  - Max loss zones on both wings
  - All four legs labeled

Output: week30_iron_condor.png
"""

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Parameters (all four legs)
# -------------------------------------------------------------------
long_put_strike  = 85    # buy put (lower wing)
short_put_strike = 90    # sell put
short_call_strike = 110  # sell call
long_call_strike  = 115  # buy call (upper wing)

put_spread_premium  = 1.50   # net credit from put spread
call_spread_premium = 1.50   # net credit from call spread
total_premium = put_spread_premium + call_spread_premium  # $3.00

# -------------------------------------------------------------------
# Stock price range at expiration
# -------------------------------------------------------------------
stock_prices = np.linspace(70, 130, 500)

# -------------------------------------------------------------------
# Payoff calculation (iron condor = bull put spread + bear call spread)
# -------------------------------------------------------------------
# Long put payoff
long_put_pnl = np.maximum(long_put_strike - stock_prices, 0)

# Short put payoff
short_put_pnl = -np.maximum(short_put_strike - stock_prices, 0)

# Short call payoff
short_call_pnl = -np.maximum(stock_prices - short_call_strike, 0)

# Long call payoff
long_call_pnl = np.maximum(stock_prices - long_call_strike, 0)

# Total iron condor P&L
iron_condor_pnl = (long_put_pnl + short_put_pnl +
                   short_call_pnl + long_call_pnl + total_premium)

# Key levels
max_profit = total_premium
max_loss_put_side = -(short_put_strike - long_put_strike) + total_premium
max_loss_call_side = -(long_call_strike - short_call_strike) + total_premium
breakeven_lower = short_put_strike - total_premium
breakeven_upper = short_call_strike + total_premium

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6))

# Main payoff line
ax.plot(stock_prices, iron_condor_pnl, color="#1565C0", linewidth=2.5,
        label="Iron Condor Payoff")

# Shade max profit zone
profit_mask = (stock_prices >= short_put_strike) & (stock_prices <= short_call_strike)
ax.fill_between(stock_prices, 0, iron_condor_pnl,
                where=profit_mask, color="#4CAF50", alpha=0.25,
                label=f"Max Profit Zone (${max_profit:.2f})")

# Shade max loss zones
left_loss = stock_prices <= long_put_strike
right_loss = stock_prices >= long_call_strike
ax.fill_between(stock_prices, 0, iron_condor_pnl,
                where=left_loss, color="#F44336", alpha=0.20,
                label=f"Max Loss Zone (${max_loss_put_side:.2f})")
ax.fill_between(stock_prices, 0, iron_condor_pnl,
                where=right_loss, color="#F44336", alpha=0.20)

# Reference lines
ax.axhline(0, color="grey", linewidth=0.8)
ax.axhline(max_profit, color="#4CAF50", linewidth=0.8, linestyle="--", alpha=0.5)
ax.axhline(max_loss_put_side, color="#F44336", linewidth=0.8, linestyle="--", alpha=0.5)

# Strike price vertical lines
for strike, lbl, clr in [
    (long_put_strike,   f"Long Put ${long_put_strike}",   "#7B1FA2"),
    (short_put_strike,  f"Short Put ${short_put_strike}",  "#E91E63"),
    (short_call_strike, f"Short Call ${short_call_strike}", "#E91E63"),
    (long_call_strike,  f"Long Call ${long_call_strike}",  "#7B1FA2"),
]:
    ax.axvline(strike, color=clr, linewidth=1, linestyle=":", alpha=0.7)
    ax.text(strike, max_profit + 0.8, lbl, ha="center", fontsize=7.5,
            color=clr, fontweight="bold", rotation=0)

# Breakeven annotations
for be, side in [(breakeven_lower, "left"), (breakeven_upper, "right")]:
    offset = -8 if side == "left" else 4
    ax.annotate(
        f"BE = ${be:.2f}",
        xy=(be, 0), xytext=(be + offset, -1.5),
        fontsize=9, fontweight="bold", color="#FF6F00",
        arrowprops=dict(arrowstyle="->", color="#FF6F00", lw=1.5),
    )

# Info box
info_text = (
    f"Net Credit: ${total_premium:.2f}\n"
    f"Max Profit: ${max_profit:.2f}\n"
    f"Max Loss: ${abs(max_loss_put_side):.2f}\n"
    f"Risk/Reward: {abs(max_loss_put_side)/max_profit:.1f}:1"
)
ax.text(0.02, 0.35, info_text, transform=ax.transAxes, fontsize=9,
        verticalalignment="top", fontfamily="monospace",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#FFF9C4", alpha=0.9))

# Labels and formatting
ax.set_title("Iron Condor Payoff Diagram", fontsize=14, fontweight="bold")
ax.set_xlabel("Stock Price at Expiration ($)", fontsize=12)
ax.set_ylabel("Profit / Loss ($)", fontsize=12)
ax.legend(loc="lower right", fontsize=9, framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_xlim(70, 130)
ax.set_ylim(-5, 6)

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week30_iron_condor.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week30_iron_condor.png")
