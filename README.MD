# 📊 BCA Stock Dashboard — Power BI

Dashboard for analyzing **Bank Central Asia (BBCA.JK)** stock performance based on historical data from January 2023 to December 2025, built using Python and Power BI.

---

## 📌 Quick Overview

A personal data analytics project that combines Python-based data scraping with interactive Power BI visualizations to explore stock price trends, risk metrics, and return behavior of BCA — one of Indonesia's largest banks.

---

## Tech Stack

| Tools | Purpose |
|-------|---------|
| `yfinance` | Scraping historical BCA stock data |
| `pandas` | Data preprocessing & feature engineering |
| `Power BI` | Interactive dashboard & visualization |

---

## Project Workflow

```
yfinance (scraping) → pandas (preprocessing) → Power BI (visualization)
```

1. **Data Collection** — Retrieved historical price data for BBCA.JK using the `yfinance` library (period: January 2023 – December 2025)
2. **Data Processing** — Calculated technical metrics including daily return, 20-day rolling volatility, drawdown, and cumulative return
3. **Visualization** — Built an interactive Power BI dashboard to analyze trends, risk, and overall stock performance

---

## Dashboard Overview

The dashboard consists of several key analytical panels:

- **Historical Closing Price** — Price trend over the full period
- **Cumulative Return %** — Accumulated return from the start date
- **Daily Return Distribution** — Histogram of daily returns
- **Volatility (20D)** — 20-day rolling volatility
- **Drawdown %** — Decline from peak to trough
- **Volume Confirmation** — Volume-based trend confirmation
- **Correlation: Daily Return vs Volatility** — Scatter plot of return vs risk

---

## 🔍 Key Insights

| Metric | Value |
|--------|-------|
| **Total Return** | ~3% (Jan 2023 – Dec 2025) |
| **Average Daily Return** | 0.0029% |
| **Volatility (20D)** | 1.54% |
| **Max Drawdown** | -31.41% |

### Key Findings:

- **Max Drawdown of -31.41%** — BCA experienced a severe peak-to-trough decline over the observed period, likely driven by macroeconomic headwinds such as global interest rate hikes or domestic market corrections. This highlights the importance of risk management even for blue-chip stocks.

- **Cumulative return peaked at ~30%** in mid-period before pulling back to ~3% by end of 2025. This suggests a strong bull phase followed by a prolonged correction — a classic cycle that reflects broader market sentiment shifts rather than company-specific issues.

- **Volatility remained relatively stable** in the 1–2% range throughout most of the period, with noticeable spikes that align with sharp price drops. These spikes indicate short bursts of uncertainty, which then normalized — consistent with BCA's status as a large-cap, fundamentally strong stock.

- **Volume surged during price declines** — This pattern suggests institutional selling pressure during downtrends. High volume on red days is a bearish confirmation signal, indicating that large players were actively exiting positions rather than retail-driven panic.

- **Daily return distribution is approximately normal** but with a slightly heavier left tail (negative skew). This means the probability of extreme negative returns is marginally higher than extreme positive returns — a common characteristic in equity markets during uncertain periods.

- **Weak positive correlation between volatility and negative returns** — The scatter plot shows that on high-volatility days, returns tend to skew negative. This is typical of asymmetric market behavior where fear drives bigger moves than optimism.

---

## License

This project is licensed under the MIT License.

![License](License.svg)

---

## Contact

If you have any questions or feedback, feel free to reach out:
- **Email:** Ayusekar1822@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/ayusekar22/
- **GitHub:** https://github.com/Ayusekar22