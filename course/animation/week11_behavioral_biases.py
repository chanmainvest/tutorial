"""
Week 11: Emotional Cycle of Investing
=======================================
Shows the classic "emotional cycle of investing" chart with a price line
that rises, peaks, crashes, and recovers. Emotional labels are placed at
key points: optimism, excitement, euphoria, anxiety, denial, panic,
capitulation, depression, hope, relief, back to optimism.

Output: week11_behavioral_biases.png
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Build the price curve that matches the emotional cycle ---
# We construct a smooth curve that rises to euphoria, crashes, and recovers
t = np.linspace(0, 10, 500)

# Piecewise smooth curve using a combination of sine waves and polynomials
price = (
    50
    + 30 * np.sin(t * 0.5 - 0.5)        # General upward then down swing
    + 10 * np.sin(t * 1.2)               # Additional oscillation
    - 0.5 * (t - 5) ** 2                 # Parabolic shape for the crash
    + 15 * np.exp(-0.5 * (t - 8) ** 2)   # Recovery bump
    + 3 * t                               # Slight upward trend
)

# Normalize to a reasonable range
price = (price - price.min()) / (price.max() - price.min()) * 80 + 20

# --- Emotional stages with approximate positions on the curve ---
# (time_position, label, vertical_offset, color)
emotions = [
    (0.3,  "Optimism",      8,   "#4CAF50"),
    (1.2,  "Excitement",    10,  "#8BC34A"),
    (2.3,  "Thrill",        10,  "#CDDC39"),
    (3.1,  "Euphoria\n(Maximum Risk!)", 12, "#FF9800"),
    (4.0,  "Anxiety",       -12, "#FF5722"),
    (4.6,  "Denial",        -14, "#F44336"),
    (5.4,  "Panic",         -16, "#D32F2F"),
    (6.0,  "Capitulation",  -14, "#B71C1C"),
    (6.6,  "Depression\n(Maximum Opportunity!)", -18, "#880E4F"),
    (7.5,  "Hope",          10,  "#7B1FA2"),
    (8.5,  "Relief",        10,  "#1565C0"),
    (9.5,  "Optimism",      10,  "#4CAF50"),
]

# --- Create figure ---
fig, ax = plt.subplots(figsize=(16, 9))

# Plot the price line with a gradient-like effect
ax.plot(t, price, color="#333", linewidth=3, zorder=3)

# Fill under the curve with gradient
ax.fill_between(t, price, price.min() - 5, alpha=0.08, color="#2196F3")

# --- Place emotional labels ---
for time_pos, label, v_offset, color in emotions:
    # Find the closest index in t
    idx = np.argmin(np.abs(t - time_pos))
    px, py = t[idx], price[idx]

    # Determine if label is above or below the line
    label_y = py + v_offset

    ax.annotate(
        label,
        xy=(px, py),
        xytext=(px, label_y),
        fontsize=10,
        fontweight="bold",
        color=color,
        ha="center",
        va="center",
        arrowprops=dict(arrowstyle="->, head_width=0.2", color=color, lw=1.5, alpha=0.7),
        bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=color, alpha=0.85),
    )

    # Dot on the price line
    ax.scatter(px, py, s=60, color=color, zorder=5, edgecolors="white", linewidths=1.5)

# --- Mark the key danger/opportunity zones ---
# Euphoria zone (danger)
euphoria_idx = np.argmin(np.abs(t - 3.1))
ax.axvline(x=t[euphoria_idx], color="#FF9800", linestyle=":", alpha=0.4)

# Depression zone (opportunity)
depression_idx = np.argmin(np.abs(t - 6.6))
ax.axvline(x=t[depression_idx], color="#880E4F", linestyle=":", alpha=0.4)

# --- Formatting ---
ax.set_title("The Emotional Cycle of Investing",
             fontsize=20, fontweight="bold", pad=15, color="#333")
ax.set_xlabel("Time", fontsize=13)
ax.set_ylabel("Market Price", fontsize=13)

# Remove specific tick labels (this is conceptual, not real data)
ax.set_xticks([])
ax.set_yticks([])

ax.grid(True, alpha=0.15, linestyle="-")

# Key insight box
ax.text(
    0.02, 0.02,
    "Investors tend to buy at peaks (euphoria) and sell at troughs (capitulation).\n"
    "The best time to invest is often when it feels the worst.\n"
    "Discipline and a plan help overcome emotional decision-making.",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="bottom",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#FFF9C4", edgecolor="#F9A825", alpha=0.9),
)

fig.tight_layout()

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week11_behavioral_biases.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
