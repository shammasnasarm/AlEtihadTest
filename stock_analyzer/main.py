from utils import StockAnalyzer


def main():
    ticker = input("Enter stock ticker (e.g., AAPL, TSLA, INFY.NS): ")
    period = input("Enter period (1mo, 6mo, 1y, 5y, max) [default=1y]: ") or "1y"

    analyzer = StockAnalyzer(ticker)

    print("\nFetching data...")
    analyzer.fetch_data(period=period)

    print("Adding indicators...")
    analyzer.add_indicators()

    print("\nCalculating metrics...")
    metrics = analyzer.calculate_metrics()

    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    print("\nDisplaying chart...")
    analyzer.plot()


if __name__ == "__main__":
    main()