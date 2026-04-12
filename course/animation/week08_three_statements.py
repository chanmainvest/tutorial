"""
Week 08: Three Financial Statements - Flow Diagram
====================================================
Visual diagram showing how the three core financial statements connect:
- Income Statement -> Balance Sheet -> Cash Flow Statement
Key flows: Net Income -> Retained Earnings, Depreciation adds back to CF,
CapEx reduces cash and increases assets, etc.

Uses matplotlib patches and arrows to create a clear flow diagram.

Output: week08_three_statements.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# --- Create figure ---
fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis("off")

# --- Helper function to draw a box with title and items ---
def draw_statement_box(ax, x, y, width, height, title, items, color, title_color):
    """Draw a rounded box representing a financial statement."""
    # Main box
    box = FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.15",
        facecolor=color,
        edgecolor=title_color,
        linewidth=2.5,
        alpha=0.9,
    )
    ax.add_patch(box)

    # Title bar
    title_box = FancyBboxPatch(
        (x, y + height - 0.7), width, 0.7,
        boxstyle="round,pad=0.1",
        facecolor=title_color,
        edgecolor=title_color,
        linewidth=0,
        alpha=0.95,
    )
    ax.add_patch(title_box)

    # Title text
    ax.text(x + width / 2, y + height - 0.35, title,
            fontsize=13, fontweight="bold", color="white",
            ha="center", va="center")

    # Item text
    for i, item in enumerate(items):
        ax.text(x + 0.25, y + height - 1.1 - i * 0.45, item,
                fontsize=10, color="#333", va="center")

# --- Draw the three statements ---
# Income Statement (left)
draw_statement_box(ax, 0.5, 5.5, 4.5, 4,
    "INCOME STATEMENT",
    ["Revenue", "- Cost of Goods Sold", "= Gross Profit", "- Operating Expenses", "- Depreciation",
     "= Operating Income", "- Interest & Tax", "= Net Income"],
    "#E3F2FD", "#1565C0")

# Balance Sheet (center)
draw_statement_box(ax, 5.8, 5.5, 4.5, 4,
    "BALANCE SHEET",
    ["Assets:", "  Cash + Receivables", "  PP&E (net of deprec.)", "  Inventories",
     "Liabilities:", "  Debt + Payables",
     "Equity:", "  Retained Earnings"],
    "#E8F5E9", "#2E7D32")

# Cash Flow Statement (right)
draw_statement_box(ax, 11.2, 5.5, 4.3, 4,
    "CASH FLOW STATEMENT",
    ["Operating CF:", "  Net Income", "  + Depreciation", "  +/- Working Capital",
     "Investing CF:", "  - Capital Expenditures",
     "Financing CF:", "  +/- Debt / Dividends"],
    "#FFF3E0", "#E65100")

# --- Draw connecting arrows ---
arrow_style = "Simple,tail_width=2,head_width=12,head_length=8"

# Arrow 1: Net Income -> Retained Earnings (Income Statement -> Balance Sheet)
arrow1 = FancyArrowPatch(
    (5.0, 6.0), (5.8, 6.6),
    arrowstyle=arrow_style,
    color="#1565C0",
    alpha=0.7,
    connectionstyle="arc3,rad=0.15",
)
ax.add_patch(arrow1)
ax.text(5.4, 6.7, "Net Income\nflows to\nRetained Earnings",
        fontsize=8, color="#1565C0", ha="center", fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#1565C0", alpha=0.8))

# Arrow 2: Net Income -> Cash Flow (Income Statement -> CF Statement)
arrow2 = FancyArrowPatch(
    (4.0, 5.5), (12.5, 5.5),
    arrowstyle=arrow_style,
    color="#FF6F00",
    alpha=0.5,
    connectionstyle="arc3,rad=-0.5",
)
ax.add_patch(arrow2)
ax.text(8.0, 3.2, "Net Income is\nstarting point for\nOperating Cash Flow",
        fontsize=9, color="#FF6F00", ha="center", fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#FF6F00", alpha=0.8))

# Arrow 3: Depreciation add-back (Balance Sheet -> CF Statement)
arrow3 = FancyArrowPatch(
    (10.3, 8.0), (11.2, 7.8),
    arrowstyle=arrow_style,
    color="#2E7D32",
    alpha=0.7,
    connectionstyle="arc3,rad=-0.1",
)
ax.add_patch(arrow3)
ax.text(10.7, 8.5, "Depreciation\nadds back to CF\n(non-cash charge)",
        fontsize=8, color="#2E7D32", ha="center", fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#2E7D32", alpha=0.8))

# Arrow 4: Cash from CF -> Balance Sheet Cash
arrow4 = FancyArrowPatch(
    (13.5, 9.5), (8.0, 9.5),
    arrowstyle=arrow_style,
    color="#9C27B0",
    alpha=0.5,
    connectionstyle="arc3,rad=-0.3",
)
ax.add_patch(arrow4)
ax.text(10.7, 10.2, "Ending Cash Balance\nupdates Balance Sheet",
        fontsize=9, color="#9C27B0", ha="center", fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#9C27B0", alpha=0.8))

# --- Title ---
ax.set_title("How the Three Financial Statements Connect",
             fontsize=20, fontweight="bold", pad=20, color="#333")

# Subtitle
fig.text(0.5, 0.02,
         "The three statements form a closed loop: Net Income feeds into both "
         "the Balance Sheet (via Retained Earnings) and the Cash Flow Statement (as starting point).",
         ha="center", fontsize=11, color="#555", style="italic",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#F5F5F5", edgecolor="#999"))

fig.tight_layout(rect=[0, 0.05, 1, 0.96])

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week08_three_statements.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
