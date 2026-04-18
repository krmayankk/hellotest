from src.utils import calculate_total, format_currency


def process_order(items):
    """Process a list of order items and return formatted total."""
    total = 0
    for item in items:
        total += calculate_total(item["price"], item["quantity"], item.get("discount", 0))
    return format_currency(total)


def generate_invoice(order_id, items):
    """Generate an invoice string for an order."""
    lines = [f"Invoice #{order_id}", "---"]
    for item in items:
        line_total = calculate_total(item["price"], item["quantity"], item.get("discount", 0))
        lines.append(f"  {item['name']}: {format_currency(line_total)}")
    lines.append(f"Total: {format_currency(calculate_total(sum(i['price'] * i['quantity'] for i in items), 1))}")
    return "\n".join(lines)
