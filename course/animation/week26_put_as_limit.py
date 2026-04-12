"""
Week 26 - Short Put as a Limit Order Alternative
===================================================
Comparison diagram: Traditional limit buy order vs Short Put,
showing the premium received as an advantage of selling puts.
Output: week26_put_as_limit.png
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

# ---------------------------------------------------------------------------
# 1. Parameters
# ---------------------------------------------------------------------------
current_price = 110       # current stock price
limit_price   = 100       # desired buy price (= put strike)
put_premium   = 4.00      # premium received for selling the put
strike        = 100       # put strike = limit price

stock_range = np.linspace(80, 125, 300)

# ---------------------------------------------------------------------------
# 2. Calculate outcomes for both strategies
# ---------------------------------------------------------------------------
# Strategy 1: Traditional limit buy at $100
# - If stock drops to $100, you buy at $100
# - Effective cost basis: $100
# - No income while waiting

# Strategy 2: Sell $100 put, collect $4 premium
# - If stock drops below $100, you're assigned at $100 but net cost = $96
# - If stock stays above $100, you keep the $4 premium
# - Effective cost basis if assigned: $96

# P&L comparison when owning (or obligated to buy) vs just holding cash
# For limit order: profit only if stock falls to limit and then rises
limit_pnl = np.where(stock_range <= limit_price,
                     stock_range - limit_price,  # bought at limit, value is current
                     0)  # never triggered

# For short put: profit includes premium
put_pnl = np.where(stock_range <= strike,
                   stock_range - strike + put_premium,  # assigned, net of premium
                   put_premium)  # not assigned, keep premium

# ---------------------------------------------------------------------------
# 3. Plot
# ---------------------------------------------------------------------------
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.3)

fig.suptitle('Short Put as a Limit Order Alternative',
             fontsize=16, fontweight='bold', y=0.97)

# -- Panel 1 (top-left): Scenario comparison table/visual --
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('Strategy Comparison', fontsize=13, fontweight='bold')

# Table-like display
rows = [
    ('Current Price', f'${current_price}', f'${current_price}'),
    ('Target Buy Price', f'${limit_price}', f'${strike} (strike)'),
    ('Premium Received', '$0', f'${put_premium:.2f}'),
    ('Effective Cost', f'${limit_price:.2f}', f'${limit_price - put_premium:.2f}'),
    ('Income While Waiting', 'None', f'${put_premium:.2f}/share'),
    ('Obligation', 'None', 'Must buy if assigned'),
]

headers = ['', 'Limit Order', 'Short Put']
for j, h in enumerate(headers):
    ax1.text(1 + j * 3.2, 9.2, h, fontsize=10, fontweight='bold',
             ha='center', va='center',
             bbox=dict(boxstyle='round', facecolor='#E3F2FD' if j > 0 else '#EEEEEE'))

for i, (label, v1, v2) in enumerate(rows):
    y = 8.0 - i * 1.3
    bg = '#f9f9f9' if i % 2 == 0 else 'white'
    ax1.text(1, y, label, fontsize=9, ha='center', va='center',
             fontweight='bold', color='#333333')
    ax1.text(4.2, y, v1, fontsize=9, ha='center', va='center',
             color='#2196F3')
    ax1.text(7.4, y, v2, fontsize=9, ha='center', va='center',
             color='#FF9800')

# -- Panel 2 (top-right): P&L comparison chart --
ax2 = fig.add_subplot(gs[0, 1])

ax2.plot(stock_range, put_pnl, color='#FF9800', linewidth=2.5,
         label='Short Put P&L')
ax2.plot(stock_range, limit_pnl, color='#2196F3', linewidth=2.5,
         linestyle='--', label='Limit Order P&L')

# Shade the premium advantage
ax2.fill_between(stock_range, put_pnl, limit_pnl,
                 where=(put_pnl > limit_pnl), alpha=0.15,
                 color='#FF9800', label='Put premium advantage')

ax2.axhline(y=0, color='black', linewidth=0.8)
ax2.axvline(x=strike, color='gray', linestyle=':', linewidth=1)
ax2.text(strike + 0.5, -18, f'Strike\n${strike}', fontsize=8,
         color='gray', ha='left')

# Premium annotation
ax2.annotate(f'Premium = ${put_premium}\n(kept if not assigned)',
             xy=(115, put_premium), xytext=(108, 12),
             fontsize=9, fontweight='bold', color='#FF9800',
             arrowprops=dict(arrowstyle='->', color='#FF9800'))

ax2.set_xlabel('Stock Price at Expiration ($)', fontsize=11)
ax2.set_ylabel('Profit / Loss ($)', fontsize=11)
ax2.set_title('P&L at Expiration', fontsize=13, fontweight='bold')
ax2.legend(loc='lower right', fontsize=9)
ax2.grid(True, alpha=0.25)

# -- Panel 3 (bottom-left): scenario outcomes --
ax3 = fig.add_subplot(gs[1, 0])

scenarios = ['Stock drops\nto $90', 'Stock drops\nto $100',
             'Stock stays\nat $110', 'Stock rises\nto $120']
limit_outcomes = [-10, 0, 0, 0]  # limit order outcomes
put_outcomes   = [-6, 4, 4, 4]   # short put outcomes (includes premium)

x = np.arange(len(scenarios))
width = 0.35

bars1 = ax3.bar(x - width / 2, limit_outcomes, width,
                label='Limit Order', color='#2196F3',
                edgecolor='white', linewidth=1)
bars2 = ax3.bar(x + width / 2, put_outcomes, width,
                label='Short Put', color='#FF9800',
                edgecolor='white', linewidth=1)

for bar in bars1:
    h = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width() / 2,
             h + (0.3 if h >= 0 else -0.8),
             f'${h:+.0f}', ha='center', fontsize=9, fontweight='bold',
             color='#2196F3')

for bar in bars2:
    h = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width() / 2,
             h + (0.3 if h >= 0 else -0.8),
             f'${h:+.0f}', ha='center', fontsize=9, fontweight='bold',
             color='#FF9800')

ax3.axhline(y=0, color='black', linewidth=0.8)
ax3.set_xticks(x)
ax3.set_xticklabels(scenarios, fontsize=9)
ax3.set_ylabel('Outcome per Share ($)', fontsize=11)
ax3.set_title('Scenario Analysis', fontsize=13, fontweight='bold')
ax3.legend(fontsize=9)
ax3.grid(True, axis='y', alpha=0.25)

# -- Panel 4 (bottom-right): key takeaways --
ax4 = fig.add_subplot(gs[1, 1])
ax4.axis('off')
ax4.set_title('Key Takeaways', fontsize=13, fontweight='bold')

takeaways = [
    ("Premium Income", "Selling puts generates\nimmediate income ($4/share)\nwhile waiting to buy.", '#4CAF50'),
    ("Lower Cost Basis", f"If assigned, effective cost\nis ${strike - put_premium} vs ${strike} with limit.", '#FF9800'),
    ("Trade-Off", "Obligation to buy if stock\ndrops below strike. Cannot\ncancel like a limit order.", '#F44336'),
    ("Best When", "You want to own the stock\nat a lower price and are\nhappy to collect premium.", '#2196F3'),
]

for i, (title, text, color) in enumerate(takeaways):
    y = 0.88 - i * 0.25
    ax4.text(0.05, y, title, transform=ax4.transAxes,
             fontsize=11, fontweight='bold', color=color, va='top')
    ax4.text(0.05, y - 0.04, text, transform=ax4.transAxes,
             fontsize=9, color='#333333', va='top')

plt.subplots_adjust(left=0.05, right=0.95, top=0.93, bottom=0.05,
                    hspace=0.35, wspace=0.3)

# ---------------------------------------------------------------------------
# 4. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week26_put_as_limit.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
