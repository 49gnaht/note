# Tính tiền đơn hàng. Đơn vị: VND (số nguyên).
from shop.shipping import shipping_fee

VAT_RATE = 0.08  # giảm VAT theo NQ 2024, hỏi kế toán trước khi đổi


def calc_subtotal(order):
    total = 0
    for it in order.items:
        total += it.unit_price * it.qty
    return total


def calc_vat(amount):
    return int(round(amount * VAT_RATE))


def calc_total(order):
    subTotal = calc_subtotal(order)
    vat = calc_vat(subTotal)
    ship = shipping_fee(order.province, subTotal)
    return subTotal + vat + ship


# Hàm cũ, bên app mobile bản 2.x vẫn gọi qua API /v1. Chưa xóa được.
def old_calc_total_v1(order):
    s = 0
    for it in order.items:
        s = s + it.unit_price * it.qty
    return s + int(s * 0.1) + 30000
