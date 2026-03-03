import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


class StockAnalyzer:
    def __init__(self, ticker: str):
        self.ticker = ticker.upper()
        self.data = None

    def fetch_data(self, period="1y", interval="1d"):
        self.data = yf.download(self.ticker, period=period, interval=interval)
        if self.data.empty:
            raise ValueError("No data found.")
        print(self.data)
        return self.data

    def add_indicators(self):
        self.data["MA50"] = self.data["Close"].rolling(window=50).mean()
        self.data["MA200"] = self.data["Close"].rolling(window=200).mean()
        self.data["Daily Return"] = self.data["Close"].pct_change()
        print(self.data)
        return self.data

    def calculate_metrics(self):
        avg_return = self.data["Daily Return"].mean()
        volatility = self.data["Daily Return"].std()
        annual_return = avg_return * 252
        annual_volatility = volatility * np.sqrt(252)

        return {
            "Average Daily Return": avg_return,
            "Annual Return (approx)": annual_return,
            "Annual Volatility (approx)": annual_volatility,
        }

    def plot(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.data["Close"], label="Close Price")
        plt.plot(self.data["MA50"], label="50-Day MA")
        plt.plot(self.data["MA200"], label="200-Day MA")
        plt.title(f"{self.ticker} Stock Price")
        plt.legend()
        plt.show()
