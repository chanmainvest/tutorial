"""
Week 02: Active vs Passive Fund Performance
=============================================
Bar chart showing the percentage of actively managed funds that underperform
their benchmark index over 1, 5, 10, 15, and 20 year periods.
Data is based on SPIVA (S&P Indices vs Active) research findings.

Output: week02_active_vs_passive.png
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Data based on SPIVA research ---
periods = ["1 Year", "5 Years", "10 Years", "15 Years", "20 Years"]
underperform_pct = [60, 75, 85, 88, 92]  # % of active funds that underperform

# --- Create figure ---
fig, ax = plt.subplots(figsize=(11, 7))

# Color gradient: darker red as time period increases (worse for active funds)
colors = ["#FFAB91", "#FF7043", "#F4511E", "#D84315", "#BF360C"]

bars = ax.bar(periods, underperform_pct, color=colors, edgecolor="white", linewidth=1.5, width=0.6)

# Add percentage labels on top of each bar
for bar, pct in zip(bars, underperform_pct):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1.5,
        f"{pct}%",
        ha="center",
        va="bottom",
        fontsize=14,
        fontweight="bold",
        color="#333333",
    )

# --- Formatting ---
ax.set_title(
    "% of Active Funds That Underperform Their Benchmark",
    fontsize=17,
    fontweight="bold",
    pad=15,
)
ax.set_subtitle_text = None  # matplotlib doesn't have subtitle natively
fig.text(
    0.5, 0.91,
    "Source: SPIVA Scorecard (approximate data)",
    ha="center",
    fontsize=11,
    color="gray",
    style="italic",
)
ax.set_ylabel("Underperformance Rate (%)", fontsize=13)
ax.set_xlabel("Time Period", fontsize=13)
ax.set_ylim(0, 105)

# Add a reference line at 50% (coin-flip level)
ax.axhline(y=50, color="green", linestyle="--", alpha=0.5, linewidth=1.5)
ax.text(4.4, 51.5, "50% line\n(coin flip)", fontsize=9, color="green", ha="center")

ax.grid(axis="y", alpha=0.3, linestyle="--")
ax.set_axisbelow(True)

# Add takeaway annotation
ax.annotate(
    "Over longer periods, the vast majority\nof active managers fail to beat the index.",
    xy=(3, 88),
    xytext=(1.5, 55),
    fontsize=11,
    color="#BF360C",
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="#BF360C", lw=1.5),
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFF3E0", edgecolor="#BF360C"),
)

fig.tight_layout(rect=[0, 0, 1, 0.90])

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week02_active_vs_passive.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
