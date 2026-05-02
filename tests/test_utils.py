from src.utils import compute_total, format_currency


def test_compute_total_no_discount_no_tax():
    assert compute_total(10, 2, 0) == 20.0


def test_compute_total_with_discount():
    assert compute_total(100, 1, 0.1) == 90.0


def test_compute_total_with_discount_and_tax():
    assert compute_total(100, 1, 0.1, tax=0.08) == 97.2


def test_format_currency():
    assert format_currency(1234.5) == "$1,234.50"
