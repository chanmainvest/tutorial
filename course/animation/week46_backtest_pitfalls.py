"""
Week 46 - Backtest Pitfalls: Overfitting
==========================================
Shows two equity curves to illustrate overfitting:
  - In-sample (training period): smooth, impressive upward curve
  - Out-of-sample (live trading): choppy, mediocre, realistic
Highlights the danger of curve-fitting to historical data.
Output: week46_backtest_pitfalls.png
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------------------------------------------------------------------
# Generate equity curves
# ---------------------------------------------------------------------------
np.random.seed(21)

# Time axis
days_in_sample = 252 * 3    # 3 years in-sample
days_out_sample = 252 * 2   # 2 years out-of-sample
total_days = days_in_sample + days_out_sample

# In-sample: overfitted strategy looks great (high Sharpe, smooth)
in_sample_returns = np.random.normal(0.0008, 0.005, days_in_sample)
# Make it smoother and more upward
in_sample_returns = np.convolve(in_sample_returns, np.ones(5)/5, mode="same")
in_sample_returns += 0.0004  # extra drift
in_sample_equity = 100 * np.exp(np.cumsum(in_sample_returns))

# Out-of-sample: same "strategy" falls apart (low Sharpe, choppy, drawdowns)
out_sample_returns = np.random.normal(0.0001, 0.012, days_out_sample)
# Add a big drawdown
out_sample_returns[60:120] -= 0.003
out_sample_returns[200:230] -= 0.004
out_sample_equity = in_sample_equity[-1] * np.exp(np.cumsum(out_sample_returns))

# Combine
equity_full = np.concatenate([in_sample_equity, out_sample_equity])
days = np.arange(total_days)

# Benchmark (buy and hold): steady growth
benchmark_returns = np.random.normal(0.0003, 0.01, total_days)
benchmark_equity = 100 * np.exp(np.cumsum(benchmark_returns))

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 6))

# In-sample period
ax.plot(days[:days_in_sample], equity_full[:days_in_sample],
        color="#4CAF50", linewidth=2.2, label="Strategy (In-Sample)")

# Out-of-sample period
ax.plot(days[days_in_sample-1:], equity_full[days_in_sample-1:],
        color="#F44336", linewidth=2.2, label="Strategy (Out-of-Sample)")

# Benchmark
ax.plot(days, benchmark_equity, color="#9E9E9E", linewidth=1.5,
        linestyle="--", alpha=0.7, label="Benchmark (Buy & Hold)")

# Vertical line separating in-sample / out-of-sample
ax.axvline(x=days_in_sample, color="#FF9800", linewidth=2, linestyle="--", alpha=0.8)
ax.text(days_in_sample + 10, equity_full.max() * 0.95,
        "In-Sample | Out-of-Sample\nBoundary",
        fontsize=10, color="#E65100", fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF3E0",
                  edgecolor="#FF9800", alpha=0.9))

# Shading for periods
ax.axvspan(0, days_in_sample, alpha=0.04, color="green")
ax.axvspan(days_in_sample, total_days, alpha=0.04, color="red")

# Period labels
ax.text(days_in_sample * 0.5, equity_full.max() * 0.15,
        "TRAINING PERIOD\n(overfitted to noise)",
        fontsize=11, ha="center", color="#2E7D32", alpha=0.7, fontweight="bold")
ax.text(days_in_sample + days_out_sample * 0.5, equity_full.max() * 0.15,
        "LIVE TRADING\n(reality hits)",
        fontsize=11, ha="center", color="#C62828", alpha=0.7, fontweight="bold")

# Warning box
props = dict(boxstyle="round,pad=0.5", facecolor="#FFEBEE", edgecolor="#F44336", alpha=0.9)
warning = "Overfitting: A strategy that looks\nperfect in backtest often fails live."
ax.text(0.98, 0.05, warning, transform=ax.transAxes,
        fontsize=10, ha="right", va="bottom", bbox=props, color="#C62828")

# Formatting
ax.set_xlabel("Trading Days", fontsize=12)
ax.set_ylabel("Portfolio Value ($)", fontsize=12)
ax.set_title("Backtest Pitfall: In-Sample vs Out-of-Sample Performance",
             fontsize=14, fontweight="bold")
ax.legend(fontsize=10, loc="upper left")
ax.grid(True, alpha=0.3)

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week46_backtest_pitfalls.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
