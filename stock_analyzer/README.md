# Stock Analyzer

Fetches historical stock data for any ticker via `yfinance`, computes technical indicators (MA50, MA200, daily return), prints key metrics, and renders a price chart.

---

## Project Structure

    stock_analyzer/
    │
    ├── main.py
    ├── utils.py
    └── requirements.txt

---

## Setup & Run

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python main.py
```

When prompted:

```
Enter stock ticker (e.g., AAPL, TSLA, INFY.NS): AAPL
Enter period (1mo, 6mo, 1y, 5y, max) [default=1y]: 1y
```

---

## Indicators Calculated

| Indicator | Description |
|---|---|
| `MA50` | 50-day moving average |
| `MA200` | 200-day moving average |
| `Daily Return` | Day-over-day % change in close price |

---

## Metrics Printed

- Average Daily Return
- Annual Return (approx) — daily avg × 252
- Annual Volatility (approx) — daily std × √252

---

## Output

A `matplotlib` chart showing Close Price, MA50, and MA200.

---

## Why I use this approach

- `yfinance` is free with no API key required
- `numpy` makes indicator calculations fast and simple
- `matplotlib` is sufficient for a quick visual analysis

---
