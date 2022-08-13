from models.order import OrderModel
from models.orderLine import OrderLineModel

order_list = [
    OrderModel(totalAmount="599", orderStatus="shipped", customer_id=2),
    OrderModel(totalAmount="322", orderStatus="processing", customer_id=1),
    OrderModel(totalAmount="144", orderStatus="done", customer_id=3),
    OrderModel(totalAmount="333", orderStatus="new", customer_id=1)

]

orderline_list = [
    OrderLineModel(product_id=1, order_id=1, quantity=2),
    OrderLineModel(product_id=2, order_id=2, quantity=3),
    OrderLineModel(product_id=3, order_id=2, quantity=4),
    OrderLineModel(product_id=1, order_id=3, quantity=1),
    OrderLineModel(product_id=2, order_id=4, quantity=5)
]