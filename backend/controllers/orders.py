from http import HTTPStatus
from flask import Blueprint, jsonify, request, g
from marshmallow.exceptions import ValidationError
from middleware.secure_route import secure_route

from models.order import OrderModel
from serializers.order_serializer import OrderSchema

router = Blueprint("orders", __name__)
order_schema = OrderSchema()


@router.route("/allorders", methods=["GET"])
# @secure_route
def get_orders():
    orders = OrderModel.query.all()
    return order_schema.jsonify(orders, many=True), HTTPStatus.OK


@router.route("/orders/<int:order_id>", methods=["GET"])
# @secure_route
def get_an_order(order_id):
    order = OrderModel.query.get(order_id)

    if not order:
        return {"message": "order not found"}, HTTPStatus.NOT_FOUND
    return order_schema.jsonify(order), HTTPStatus.OK


@router.route("/neworder", methods=["POST"])
# @secure_route
def create_order():
    order_dict = request.json
    try:
        order = order_schema.load(order_dict)
        
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}
        
    order.customer_id = g.current_customer.id
    order.save()

    return order_schema.jsonify(order), HTTPStatus.CREATED

