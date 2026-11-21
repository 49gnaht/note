from dataclasses import dataclass, field


@dataclass
class OrderItem:
    sku: str
    name: str
    unit_price: int  # VND
    qty: int


@dataclass
class Order:
    order_id: str
    customer_name: str
    province: str
    items: list = field(default_factory=list)
