"""
Free utility script: Download Binance Futures (USDT-M) historical klines to CSV.
Part of the Binance Futures Trading Bot & Event-Driven Backtester showcase.
"""

import csv
import urllib.request
import json
from datetime import datetime, timezone


def fetch_futures_klines(symbol: str = "BTCUSDT", interval: str = "15m", limit: int = 500) -> list:
    url = f"https://fapi.binance.com/fapi/v1/klines?symbol={symbol}&interval={interval}&limit={limit}"
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def save_to_csv(klines: list, filename: str) -> None:
    headers = ["open_time", "open", "high", "low", "close", "volume"]
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for k in klines:
            ts = datetime.fromtimestamp(k[0] / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([ts, k[1], k[2], k[3], k[4], k[5]])


if __name__ == "__main__":
    symbol = "BTCUSDT"
    interval = "15m"
    data = fetch_futures_klines(symbol=symbol, interval=interval, limit=500)
    output_file = f"{symbol}_{interval}_sample.csv"
    save_to_csv(data, output_file)
    print(f"Saved {len(data)} candles to {output_file}")
