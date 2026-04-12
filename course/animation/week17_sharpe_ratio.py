"""
Week 17 - Sharpe Ratio Visualization
======================================
Two strategies with the same average return but different volatility,
illustrating why the Sharpe ratio matters for risk-adjusted performance.
Output: week17_sharpe_ratio.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# 1. Generate two return series with same mean but different volatility
# ---------------------------------------------------------------------------
np.random.seed(42)
days = 252
t = np.arange(days)

daily_target_return = 0.10 / 252  # ~10% annual return for both

# Strategy A: low volatility (smooth ride)
vol_a = 0.10 / np.sqrt(252)
returns_a = np.random.normal(daily_target_return, vol_a, days)

# Strategy B: high volatility (bumpy ride)
vol_b = 0.25 / np.sqrt(252)
returns_b = np.random.normal(daily_target_return, vol_b, days)

# Cumulative growth of $100
price_a = 100 * np.cumprod(1 + returns_a)
price_b = 100 * np.cumprod(1 + returns_b)

# Compute annualised stats
ann_ret_a  = np.mean(returns_a) * 252
ann_vol_a  = np.std(returns_a) * np.sqrt(252)
ann_ret_b  = np.mean(returns_b) * 252
ann_vol_b  = np.std(returns_b) * np.sqrt(252)
risk_free  = 0.03
sharpe_a   = (ann_ret_a - risk_free) / ann_vol_a
sharpe_b   = (ann_ret_b - risk_free) / ann_vol_b

# ---------------------------------------------------------------------------
# 2. Plot
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Why Sharpe Ratio Matters: Same Return, Different Risk',
             fontsize=15, fontweight='bold')

# -- Left panel: cumulative price paths --
ax = axes[0]
ax.plot(t, price_a, color='#2196F3', linewidth=2,
        label=f'Strategy A (Low Vol)')
ax.plot(t, price_b, color='#FF5722', linewidth=2, alpha=0.8,
        label=f'Strategy B (High Vol)')
ax.axhline(y=100, color='gray', linestyle='--', linewidth=0.8)
ax.fill_between(t, price_a, 100, alpha=0.08, color='#2196F3')
ax.fill_between(t, price_b, 100, alpha=0.06, color='#FF5722')

ax.set_xlabel('Trading Days', fontsize=12)
ax.set_ylabel('Portfolio Value ($)', fontsize=12)
ax.set_title('Cumulative Performance', fontsize=13)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)

# -- Right panel: risk-return scatter with Sharpe slopes --
ax2 = axes[1]

# Plot both strategies as points
ax2.scatter(ann_vol_a * 100, ann_ret_a * 100, s=200, color='#2196F3',
            zorder=5, edgecolors='black', linewidths=1.2)
ax2.scatter(ann_vol_b * 100, ann_ret_b * 100, s=200, color='#FF5722',
            zorder=5, edgecolors='black', linewidths=1.2)

# Labels
ax2.annotate(f'Strategy A\nSharpe = {sharpe_a:.2f}',
             (ann_vol_a * 100, ann_ret_a * 100),
             textcoords="offset points", xytext=(-70, 20),
             fontsize=10, fontweight='bold', color='#2196F3',
             arrowprops=dict(arrowstyle='->', color='#2196F3'))
ax2.annotate(f'Strategy B\nSharpe = {sharpe_b:.2f}',
             (ann_vol_b * 100, ann_ret_b * 100),
             textcoords="offset points", xytext=(15, -30),
             fontsize=10, fontweight='bold', color='#FF5722',
             arrowprops=dict(arrowstyle='->', color='#FF5722'))

# Sharpe ratio lines from risk-free rate
x_line = np.linspace(0, 30, 100)
ax2.plot(x_line, risk_free * 100 + sharpe_a * x_line,
         color='#2196F3', linestyle='--', alpha=0.6,
         label=f'Sharpe A slope = {sharpe_a:.2f}')
ax2.plot(x_line, risk_free * 100 + sharpe_b * x_line,
         color='#FF5722', linestyle='--', alpha=0.6,
         label=f'Sharpe B slope = {sharpe_b:.2f}')

# Risk-free point
ax2.scatter(0, risk_free * 100, s=120, color='green', zorder=5,
            marker='o', edgecolors='black')
ax2.annotate(f'Risk-Free\n{risk_free*100:.0f}%', (0, risk_free * 100),
             textcoords="offset points", xytext=(10, -20), fontsize=9)

ax2.set_xlabel('Annualised Volatility (%)', fontsize=12)
ax2.set_ylabel('Annualised Return (%)', fontsize=12)
ax2.set_title('Risk-Return Diagram', fontsize=13)
ax2.set_xlim(-1, 30)
ax2.set_ylim(0, 18)
ax2.legend(loc='lower right', fontsize=9)
ax2.grid(True, alpha=0.3)

# Summary box
summary = (f"Both strategies target ~10% return\n"
           f"Strategy A vol: {ann_vol_a*100:.1f}%  |  "
           f"Strategy B vol: {ann_vol_b*100:.1f}%\n"
           f"Higher Sharpe = better risk-adjusted return")
fig.text(0.5, 0.01, summary, ha='center', fontsize=10,
         style='italic', color='#555555')

plt.tight_layout(rect=[0, 0.05, 1, 0.95])

# ---------------------------------------------------------------------------
# 3. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week17_sharpe_ratio.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
