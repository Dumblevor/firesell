from models.order import OrderModel

order_list = [
    OrderModel(totalAmount="599", orderStatus="shipped", customer_id=2),
    OrderModel(totalAmount="322", orderStatus="processing", customer_id=1),
    OrderModel(totalAmount="144", orderStatus="done", customer_id=3)
]
