from shop.models import Order, OrderItem
from shop.pricing import calc_subtotal, calc_vat, calc_total


def make_order(province="HN", price=100000, qty=2):
    return Order("DH001", "Nguyễn Văn A", province, [OrderItem("SP1", "Áo thun", price, qty)])


def test_subtotal():
    assert calc_subtotal(make_order()) == 200000


def test_vat():
    assert calc_vat(200000) == 16000


def test_total_with_ship():
    assert calc_total(make_order()) == 200000 + 16000 + 20000


def test_total_free_ship():
    assert calc_total(make_order(price=300000, qty=2)) == 600000 + 48000
