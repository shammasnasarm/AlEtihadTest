import json
from collections import defaultdict
from pathlib import Path

DATA_FILE = Path.cwd() / "data" / "transactions.json"


def generate_monthly_report(month: str) -> None:
    """Generate monthly financial report for the given month"""
    transactions = json.loads(DATA_FILE.read_text(encoding="utf-8")) if DATA_FILE.exists() else []

    monthly = [t for t in transactions if t["date"].startswith(month)]

    if not monthly:
        print(f"=> No transactions found for {month}.")
        return

    total_income: float = 0.0
    total_expense: float = 0.0
    category_totals: dict[str, float] = defaultdict(float)

    for t in monthly:
        amount = float(t["amount"])
        category = t.get("category") or "others"

        if t["type"] == "income":
            total_income += amount
        else:
            total_expense += abs(amount)

        category_totals[category] += abs(amount)

    net_savings = total_income - total_expense

    print(f"\n{'=' * 40}")
    print(f"  Monthly Report — {month}")
    print(f"{'=' * 40}")
    print(f"  Total Income   : ₹{total_income:,.2f}")
    print(f"  Total Expense  : ₹{total_expense:,.2f}")
    print(f"  Net Savings    : ₹{net_savings:,.2f}")
    print(f"\n  Category Breakdown:")
    print(f"  {'-' * 40}")
    for category, total in sorted(category_totals.items()):
        print(f"  {category} ₹{total:,.2f}")
    print(f"{'=' * 40}\n")
