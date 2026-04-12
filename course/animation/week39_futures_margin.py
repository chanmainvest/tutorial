"""
Week 39: Futures Margin Mechanics
====================================
Diagram showing how futures margin accounts work over time:
  - Initial margin deposit
  - Daily mark-to-market P&L
  - Maintenance margin level
  - Margin call trigger when equity drops below maintenance

Output: week39_futures_margin.png
"""

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Parameters
# -------------------------------------------------------------------
initial_margin = 10000       # initial margin deposit
maintenance_margin = 7500    # maintenance margin level
contract_value = 50000       # notional value of the futures contract

# Simulated daily P&L over 15 trading days
# (designed to trigger a margin call around day 9-10)
daily_pnl = np.array([
    200, -400, 300, -800, 150,     # days 1-5
    -600, -900, -500, -1200, 800,  # days 6-10 (margin call after day 9)
    400, -300, 600, 200, 500       # days 11-15 (recovery)
])

num_days = len(daily_pnl)
days = np.arange(0, num_days + 1)  # day 0 = deposit day

# -------------------------------------------------------------------
# Compute account equity over time (with margin call top-ups)
# -------------------------------------------------------------------
equity = [initial_margin]
margin_calls = []          # (day, amount) pairs
margin_call_days = []      # for plotting markers

for i, pnl in enumerate(daily_pnl):
    new_equity = equity[-1] + pnl

    # Check if margin call triggered
    if new_equity < maintenance_margin:
        top_up = initial_margin - new_equity  # restore to initial
        margin_calls.append((i + 1, top_up))
        margin_call_days.append(i + 1)
        new_equity = initial_margin  # after top-up

    equity.append(new_equity)

equity = np.array(equity)

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(13, 7))

# Account equity line
ax.plot(days, equity, color="#1565C0", linewidth=2.5, marker="o",
        markersize=6, markerfacecolor="#1565C0", markeredgecolor="white",
        markeredgewidth=1.5, label="Account Equity", zorder=5)

# Fill between equity and maintenance margin
ax.fill_between(days, maintenance_margin, equity,
                where=equity >= maintenance_margin,
                color="#4CAF50", alpha=0.10, label="Above Maintenance")
ax.fill_between(days, maintenance_margin, equity,
                where=equity < maintenance_margin,
                color="#F44336", alpha=0.15, label="Below Maintenance (Danger)")

# Initial margin line
ax.axhline(initial_margin, color="#2196F3", linewidth=1.5, linestyle="--",
           alpha=0.7, label=f"Initial Margin (${initial_margin:,})")

# Maintenance margin line
ax.axhline(maintenance_margin, color="#F44336", linewidth=2, linestyle="-.",
           alpha=0.8, label=f"Maintenance Margin (${maintenance_margin:,})")

# Margin call markers and annotations
for day, amount in margin_calls:
    ax.annotate(
        f"MARGIN CALL\nDeposit ${amount:,.0f}",
        xy=(day, maintenance_margin),
        xytext=(day + 0.5, maintenance_margin - 1500),
        fontsize=9, fontweight="bold", color="#D32F2F",
        arrowprops=dict(arrowstyle="->", color="#D32F2F", lw=1.5),
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFEBEE", alpha=0.9),
    )
    # Show the equity before top-up
    pre_topup = equity[day] - (initial_margin - (equity[day]))
    ax.plot(day, maintenance_margin - 200, "v", color="#D32F2F",
            markersize=12, zorder=6)

# Daily P&L bar chart (secondary, subtle)
ax2 = ax.twinx()
bar_colors = ["#4CAF50" if p >= 0 else "#F44336" for p in daily_pnl]
ax2.bar(days[1:], daily_pnl, width=0.35, alpha=0.25, color=bar_colors,
        edgecolor="none", label="Daily P&L")
ax2.set_ylabel("Daily P&L ($)", fontsize=10, color="#888")
ax2.tick_params(axis="y", labelcolor="#888")
ax2.set_ylim(-3000, 3000)

# Mechanics explanation box
mechanics_text = (
    "Futures Margin Mechanics:\n"
    "1. Deposit initial margin to open position\n"
    "2. Account marked-to-market daily\n"
    "3. If equity < maintenance margin:\n"
    "   --> Margin call: must deposit to\n"
    "       restore initial margin level\n"
    "4. Failure to meet call = forced liquidation"
)
ax.text(0.02, 0.02, mechanics_text, transform=ax.transAxes, fontsize=8.5,
        verticalalignment="bottom", fontfamily="monospace",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#FFF9C4", alpha=0.9))

# Day labels
ax.set_xticks(days)
ax.set_xticklabels([f"Day {d}" if d > 0 else "Open" for d in days],
                   fontsize=8, rotation=45, ha="right")

# Combined legend
lines1, labels1 = ax.get_legend_handles_labels()
ax.legend(lines1, labels1, loc="upper right", fontsize=8.5, framealpha=0.9)

# Labels and formatting
ax.set_title("Futures Margin Account -- Daily Mark-to-Market",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Trading Day", fontsize=12)
ax.set_ylabel("Account Equity ($)", fontsize=12)
ax.grid(True, alpha=0.3)
ax.set_ylim(5000, 12500)
ax.set_xlim(-0.5, num_days + 0.5)

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week39_futures_margin.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week39_futures_margin.png")
