from http import HTTPStatus
from flask import Blueprint, jsonify, request, g
from marshmallow.exceptions import ValidationError
from middleware.secure_route import secure_route

from models.product import ProductModel
from serializers.product_serializer import ProductSchema

router = Blueprint("products", __name__)
product_schema = ProductSchema()

@router.route("/allproducts", methods=["GET"])
def get_products():
    products = ProductModel.query.all()
    return product_schema.jsonify(products, many=True), HTTPStatus.OK


@router.route("/products/<int:product_id>", methods=["GET"])
def get_a_product(product_id):
    product = ProductModel.query.get(product_id)

    if not product:
        return {"message": "Product not found"}, HTTPStatus.NOT_FOUND
    return product_schema.jsonify(product), HTTPStatus.OK


@router.route("/newproduct", methods=["POST"])
@secure_route
def create_product():
    product_dict = request.json
    try:
        product = product_schema.load(product_dict)
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}
        
    product.product_owner_ID = g.current_customer.id
    product.save()

    return product_schema.jsonify(product), HTTPStatus.CREATED

