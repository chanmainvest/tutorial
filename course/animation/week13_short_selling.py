"""
Week 13: Short Selling Mechanics Diagram
==========================================
Step-by-step diagram explaining the mechanics of short selling:
1. Borrow shares from broker
2. Sell borrowed shares at current price
3. Wait for price to drop
4. Buy back shares at lower price
5. Return shares to broker
6. Keep the difference as profit

Output: week13_short_selling.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# --- Create figure ---
fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis("off")

# --- Define the 6 steps ---
steps = [
    {
        "num": "1",
        "title": "BORROW Shares",
        "desc": "Short seller borrows\n100 shares from broker\n(shares they don't own)",
        "color": "#1565C0",
        "light": "#E3F2FD",
        "x": 1.5,
        "y": 8.5,
    },
    {
        "num": "2",
        "title": "SELL at Market Price",
        "desc": "Immediately sell the\nborrowed 100 shares\nat $50/share = $5,000",
        "color": "#2E7D32",
        "light": "#E8F5E9",
        "x": 5.5,
        "y": 8.5,
    },
    {
        "num": "3",
        "title": "WAIT for Price Drop",
        "desc": "Short seller waits,\nhoping the stock price\nwill decline",
        "color": "#FF6F00",
        "light": "#FFF3E0",
        "x": 9.5,
        "y": 8.5,
    },
    {
        "num": "4",
        "title": "BUY BACK Shares",
        "desc": "Stock drops to $30.\nBuy 100 shares back\nat $30/share = $3,000",
        "color": "#7B1FA2",
        "light": "#F3E5F5",
        "x": 13.0,
        "y": 8.5,
    },
    {
        "num": "5",
        "title": "RETURN Shares",
        "desc": "Return the 100 shares\nto the broker,\nclosing the position",
        "color": "#00838F",
        "light": "#E0F7FA",
        "x": 4.0,
        "y": 3.5,
    },
    {
        "num": "6",
        "title": "KEEP the Profit",
        "desc": "Profit = $5,000 - $3,000\n= $2,000 profit\n(minus fees & interest)",
        "color": "#C62828",
        "light": "#FFEBEE",
        "x": 10.0,
        "y": 3.5,
    },
]

box_w = 3.0
box_h = 2.2

# --- Draw each step box ---
for step in steps:
    x = step["x"]
    y = step["y"]

    # Main box
    box = FancyBboxPatch(
        (x - box_w / 2, y - box_h / 2), box_w, box_h,
        boxstyle="round,pad=0.15",
        facecolor=step["light"],
        edgecolor=step["color"],
        linewidth=2.5,
        alpha=0.95,
    )
    ax.add_patch(box)

    # Step number circle
    circle = plt.Circle((x - box_w / 2 + 0.35, y + box_h / 2 - 0.35), 0.28,
                         color=step["color"], zorder=5)
    ax.add_patch(circle)
    ax.text(x - box_w / 2 + 0.35, y + box_h / 2 - 0.35, step["num"],
            fontsize=14, fontweight="bold", color="white",
            ha="center", va="center", zorder=6)

    # Title
    ax.text(x + 0.15, y + 0.55, step["title"],
            fontsize=12, fontweight="bold", color=step["color"], ha="center")

    # Description
    ax.text(x, y - 0.25, step["desc"],
            fontsize=9, color="#333", ha="center", va="center", linespacing=1.4)

# --- Draw arrows between steps ---
arrow_kw = dict(arrowstyle="->, head_width=0.3, head_length=0.15",
                color="#666", lw=2, connectionstyle="arc3,rad=0")

# Step 1 -> 2
ax.annotate("", xy=(5.5 - box_w / 2 - 0.1, 8.5), xytext=(1.5 + box_w / 2 + 0.1, 8.5),
            arrowprops=arrow_kw)

# Step 2 -> 3
ax.annotate("", xy=(9.5 - box_w / 2 - 0.1, 8.5), xytext=(5.5 + box_w / 2 + 0.1, 8.5),
            arrowprops=arrow_kw)

# Step 3 -> 4
ax.annotate("", xy=(13.0 - box_w / 2 - 0.1, 8.5), xytext=(9.5 + box_w / 2 + 0.1, 8.5),
            arrowprops=arrow_kw)

# Step 4 -> 5 (down and left)
ax.annotate("", xy=(4.0 + box_w / 2 + 0.1, 4.0), xytext=(13.0 - 0.3, 8.5 - box_h / 2 - 0.1),
            arrowprops=dict(arrowstyle="->, head_width=0.3", color="#666", lw=2,
                           connectionstyle="arc3,rad=0.3"))

# Step 5 -> 6
ax.annotate("", xy=(10.0 - box_w / 2 - 0.1, 3.5), xytext=(4.0 + box_w / 2 + 0.1, 3.5),
            arrowprops=arrow_kw)

# --- Stock price visualization ---
# Small price chart showing the price drop
price_x = np.array([0, 1, 2, 3, 4, 5])
price_y = np.array([50, 48, 45, 38, 32, 30])

# Position the mini chart
chart_left = 6.5
chart_bottom = 0.5
chart_w = 3.0
chart_h = 1.8

# Background for mini chart
mini_bg = FancyBboxPatch(
    (chart_left - 0.2, chart_bottom - 0.2), chart_w + 0.4, chart_h + 0.6,
    boxstyle="round,pad=0.1",
    facecolor="#F5F5F5",
    edgecolor="#999",
    linewidth=1,
)
ax.add_patch(mini_bg)

# Scale price data to chart area
px = chart_left + price_x / price_x.max() * chart_w
py = chart_bottom + (price_y - 25) / 30 * chart_h

ax.plot(px, py, color="#F44336", linewidth=2.5, marker="o", markersize=5, zorder=5)
ax.text(chart_left + chart_w / 2, chart_bottom + chart_h + 0.15,
        "Stock Price Drops ($50 -> $30)", fontsize=9, ha="center",
        fontweight="bold", color="#C62828")
ax.text(px[0], py[0] + 0.15, "$50", fontsize=8, ha="center", color="#333", fontweight="bold")
ax.text(px[-1], py[-1] - 0.2, "$30", fontsize=8, ha="center", color="#C62828", fontweight="bold")

# --- Title ---
ax.set_title("How Short Selling Works",
             fontsize=22, fontweight="bold", pad=20, color="#333")

# --- Warning box ---
ax.text(14.5, 1.0,
        "WARNING:\nIf the price goes UP\ninstead of down,\nlosses are\ntheoretically\nUNLIMITED.",
        fontsize=9, ha="center", va="center",
        color="#C62828", fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#FFEBEE", edgecolor="#C62828", linewidth=2))

fig.tight_layout()

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week13_short_selling.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
