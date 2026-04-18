from src.utils import compute_total, format_currency


def daily_summary(orders):
    """Generate a daily sales summary."""
    grand_total = 0
    for order in orders:
        for item in order["items"]:
            grand_total += compute_total(item["price"], item["quantity"], discount=item.get("discount", 0))
    return f"Daily total: {format_currency(grand_total)}"
