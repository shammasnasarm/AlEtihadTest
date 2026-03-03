from datetime import datetime

def compute_stats(jobs):
    today_str = datetime.today().strftime("%d-%m-%Y")
    today = datetime.today().date()
    posted_today = sum(1 for j in jobs if j.get("posted") == today_str)
    expiring_soon = 0
    for j in jobs:
        try:
            last = datetime.strptime(j.get("last_date", ""), "%d %b %Y").date()
            if 0 <= (last - today).days <= 7:
                expiring_soon += 1
        except ValueError:
            pass
    return {
        "total": len(jobs),
        "posted_today": posted_today,
        "expiring_soon": expiring_soon,
    }