from shop.models import Order, OrderItem
from shop.invoice import render_invoice


def test_invoice_contains_total():
    o = Order("DH002", "Trần Thị B", "DN", [OrderItem("SP2", "Quần jean", 250000, 1)])
    out = render_invoice(o)
    assert "TỔNG: 300.000đ" in out
