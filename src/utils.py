def compute_total(price, quantity, discount, tax=0):
    """Compute total price with discount and tax.

    NOTE: signature changed — discount is now required (was optional),
    tax_rate renamed to tax.
    """
    subtotal = price * quantity
    after_discount = subtotal - (subtotal * discount)
    return after_discount + (after_discount * tax)


def format_currency(amount):
    """Format a number as USD currency string."""
    return f"${amount:,.2f}"
