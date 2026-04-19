from src.utils import compute_total, format_currency


def process_order(items):
    """Process a list of order items and return formatted total."""
    total = 0
    for item in items:
        total += compute_total(item["price"], item["quantity"], discount=item.get("discount", 0))
    return format_currency(total)


def generate_invoice(order_id, items):
    """Generate an invoice string for an order."""
    lines = [f"Invoice #{order_id}", "---"]
    for item in items:
        line_total = compute_total(item["price"], item["quantity"], discount=item.get("discount", 0))
        lines.append(f"  {item['name']}: {format_currency(line_total)}")
    lines.append(f"Total: {format_currency(compute_total(sum(i['price'] * i['quantity'] for i in items), 1))}")
    return "\n".join(lines)
