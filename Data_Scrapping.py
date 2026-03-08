import yfinance as yf
import pandas as pd

symbol = "BBCA.JK"

print("Fetching data...")

df = yf.download(
    symbol,
    start="2023-01-01",
    end="2026-01-01",
    auto_adjust=False
)

df.reset_index(inplace=True)

# rename biar Power BI friendly
df = df.rename(columns={
    "Date": "date",
    "Open": "open",
    "High": "high",
    "Low": "low",
    "Close": "close",
    "Adj Close": "adjusted_close",
    "Volume": "volume"
})

# 🔥 feature engineering (biar pro)
df["daily_return"] = df["close"].pct_change()
df["ma20"] = df["close"].rolling(20).mean()
df["ma50"] = df["close"].rolling(50).mean()
df["volatility_20"] = df["daily_return"].rolling(20).std()

df.to_csv("bbca_stock.csv", index=False)

print("✅ Saved:", df.shape)