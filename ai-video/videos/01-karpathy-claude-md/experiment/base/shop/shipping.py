# Phí ship theo tỉnh. Đơn từ 500.000đ trở lên được miễn phí ship (chính sách 2025).

FEES = {
    "HN": 20000, "HCM": 20000,
    "DN": 30000,
    "OTHER":   35000,
}


def shipping_fee(province, subtotal):
    if subtotal > 500000:
        return 0
    return FEES.get(province, FEES["OTHER"])
