"""
Week 10: Business Cycle Phases Diagram
========================================
Circular diagram showing the four phases of the business cycle:
Early Expansion, Mid Expansion, Late Expansion, and Recession.
Each phase is labeled with the sectors that historically perform best.

Output: week10_business_cycle.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# --- Business cycle phases ---
phases = [
    {
        "name": "Early\nExpansion",
        "sectors": "Best sectors:\n- Technology\n- Consumer Discretionary\n- Industrials\n- Real Estate",
        "color": "#4CAF50",
        "light": "#E8F5E9",
    },
    {
        "name": "Mid\nExpansion",
        "sectors": "Best sectors:\n- Technology\n- Industrials\n- Materials\n- Energy",
        "color": "#2196F3",
        "light": "#E3F2FD",
    },
    {
        "name": "Late\nExpansion",
        "sectors": "Best sectors:\n- Energy\n- Materials\n- Consumer Staples\n- Healthcare",
        "color": "#FF9800",
        "light": "#FFF3E0",
    },
    {
        "name": "Recession",
        "sectors": "Best sectors:\n- Consumer Staples\n- Healthcare\n- Utilities\n- Bonds/Cash",
        "color": "#F44336",
        "light": "#FFEBEE",
    },
]

# --- Create figure ---
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(-6.5, 6.5)
ax.set_ylim(-6.5, 6.5)
ax.set_aspect("equal")
ax.axis("off")

# Center of the diagram
cx, cy = 0, 0
radius = 3.8  # Radius for phase placement
box_radius = 1.8  # Half-size of each box

# Draw a circular arrow path in the center
theta = np.linspace(0, 2 * np.pi, 100)
circle_r = 1.6
ax.plot(circle_r * np.cos(theta), circle_r * np.sin(theta),
        color="#BDBDBD", linewidth=2, linestyle="--", alpha=0.6)

# Draw arrowheads on the circle to show clockwise direction
for angle_deg in [45, 135, 225, 315]:
    angle = np.radians(angle_deg)
    x = circle_r * np.cos(angle)
    y = circle_r * np.sin(angle)
    # Tangent direction (clockwise)
    dx = -np.sin(angle) * 0.3
    dy = np.cos(angle) * 0.3
    ax.annotate("", xy=(x + dx, y + dy), xytext=(x, y),
                arrowprops=dict(arrowstyle="->, head_width=0.3", color="#999", lw=2))

# Center label
ax.text(0, 0, "BUSINESS\nCYCLE", fontsize=14, fontweight="bold",
        ha="center", va="center", color="#555",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#999", alpha=0.9))

# --- Draw each phase as a box positioned around the circle ---
# Positions: top-right, bottom-right, bottom-left, top-left (clockwise)
positions = [
    (radius, radius * 0.75),       # Early Expansion (top-right)
    (radius, -radius * 0.75),      # Mid Expansion (bottom-right)
    (-radius, -radius * 0.75),     # Late Expansion (bottom-left)
    (-radius, radius * 0.75),      # Recession (top-left)
]

for i, (phase, pos) in enumerate(zip(phases, positions)):
    px, py = pos

    # Draw rounded box
    box = mpatches.FancyBboxPatch(
        (px - box_radius, py - box_radius), box_radius * 2, box_radius * 2,
        boxstyle="round,pad=0.2",
        facecolor=phase["light"],
        edgecolor=phase["color"],
        linewidth=3,
        alpha=0.95,
    )
    ax.add_patch(box)

    # Phase name (bold, colored)
    ax.text(px, py + 0.9, phase["name"], fontsize=14, fontweight="bold",
            color=phase["color"], ha="center", va="center")

    # Horizontal divider line
    ax.plot([px - box_radius + 0.3, px + box_radius - 0.3], [py + 0.2, py + 0.2],
            color=phase["color"], linewidth=1, alpha=0.4)

    # Sector text
    ax.text(px, py - 0.55, phase["sectors"], fontsize=9,
            color="#333", ha="center", va="center", linespacing=1.4)

    # Draw connecting arrow from center circle to box
    angle_to_box = np.arctan2(py, px)
    start_x = circle_r * np.cos(angle_to_box) * 1.1
    start_y = circle_r * np.sin(angle_to_box) * 1.1
    end_x = px - np.sign(px) * (box_radius + 0.1)
    end_y = py - np.sign(py) * (box_radius + 0.1) if abs(py) > 0.5 else py
    ax.annotate(
        "", xy=(end_x, end_y), xytext=(start_x, start_y),
        arrowprops=dict(arrowstyle="->, head_width=0.15", color=phase["color"],
                        lw=1.5, alpha=0.6, connectionstyle="arc3,rad=0"),
    )

# --- Phase transition labels along the circle ---
transition_labels = [
    ("GDP\nAccelerating", 50),
    ("Growth\nPeaking", -20),
    ("GDP\nDecelerating", -110),
    ("Recovery\nBegins", 160),
]
for (label, angle_deg) in transition_labels:
    angle = np.radians(angle_deg)
    tx = (circle_r + 0.6) * np.cos(angle)
    ty = (circle_r + 0.6) * np.sin(angle)
    ax.text(tx, ty, label, fontsize=8, ha="center", va="center",
            color="#777", style="italic")

# --- Title ---
ax.set_title("Business Cycle: Phases & Sector Rotation",
             fontsize=20, fontweight="bold", pad=20, color="#333")

fig.tight_layout()

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week10_business_cycle.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
