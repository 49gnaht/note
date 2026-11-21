from shop.pricing import calc_subtotal, calc_vat, calc_total
from shop.shipping import shipping_fee


def fmt(v):
    return f"{v:,}".replace(",", ".") + "đ"


def render_invoice(order):
    sub = calc_subtotal(order)
    lines = [f"HÓA ĐƠN {order.order_id} - {order.customer_name}"]
    for it in order.items:
        lines.append(f"  {it.name} x{it.qty}: {fmt(it.unit_price * it.qty)}")
    lines.append(f"Tạm tính: {fmt(sub)}")
    lines.append(f"VAT: {fmt(calc_vat(sub))}")
    lines.append(f"Phí ship: {fmt(shipping_fee(order.province, sub))}")
    lines.append(f"TỔNG: {fmt(calc_total(order))}")
    return "\n".join(lines)
