def calculate_total(price, quantity, discount=0):
    """Calculate total price after discount."""
    subtotal = price * quantity
    return subtotal - (subtotal * discount)


def format_currency(amount):
    """Format a number as USD currency string."""
    return f"${amount:,.2f}"
