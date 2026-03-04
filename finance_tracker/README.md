# Finance Tracker

A CLI tool that imports bank transactions from a CSV file and generates a monthly income/expense report broken down by category.

---

## Project Structure

    finance_tracker/
    │
    ├── main.py
    ├── schemas.py
    ├── requirements.txt
    ├── sample_transactions.csv
    └── utils/
        ├── categorizer.py
        ├── importer.py
        └── report.py

---

## Setup & Run

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Import transactions from a CSV file
python main.py import --file sample_transactions.csv

# 4. Generate a monthly report
python main.py report --month 2026-02
```

---

## CSV Format

Must include columns: `date`, `description`, `amount`

```
date,description,amount
2026-02-01,Salary,5000.00
2026-02-03,Grocery Store,-120.50
2026-02-10,Netflix,-15.99
```

- Positive `amount` → income
- Negative `amount` → expense
- Transactions are saved to `data/transactions.json` after import

---

## Auto Categorization

Categories are assigned based on keyword rules in `utils/categorizer.py`:

- `salary` → income
- `swiggy` → food
- `amazon` → shopping
- `rent` → housing
- `petrol` → transport
- anything else → others

---
