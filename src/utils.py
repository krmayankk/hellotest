def compute_total(price, quantity, tax_rate=0, discount=0):
    """Compute total price with tax and discount."""
    subtotal = price * quantity
    after_discount = subtotal - (subtotal * discount)
    return after_discount + (after_discount * tax_rate)


def format_currency(amount):
    """Format a number as USD currency string."""
    return f"${amount:,.2f}"
