from http import HTTPStatus
from math import prod
from flask import Blueprint, jsonify, request, g
from marshmallow.exceptions import ValidationError
from middleware.secure_route import secure_route

from models.product import ProductModel
from models.comment import CommentModel
from models.rating import RatingModel
from serializers.product_serializer import ProductSchema
from serializers.comment_serializer import CommentSchema
from serializers.rating_serializer import RatingSchema

router = Blueprint("products", __name__)
product_schema = ProductSchema()
comment_schema = CommentSchema
rating_schema = RatingSchema

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


@router.route("/products/<int:product_id>", methods=["PUT"])
@secure_route
def update_product(product_id):
    product_update_dict = request.json
    current_product = ProductModel.query.get(product_id)
    if not current_product:
        return {"message": "Product not found"}, HTTPStatus.NOT_FOUND
    if not g.current_customer.id == current_product.product_owner_ID:
        return {"message": "You are not the product owner"}
    try:
        product = product_schema.load(
            product_update_dict, instance=current_product, partial=True
        )
    except ValidationError as e:
        return {"errors:": e.messages, "messages": "Something went wrong"}
    product.save()
    return product_schema.jsonify(product), HTTPStatus.OK


@router.route("/products/<int:product_id>", methods=["DELETE"])
@secure_route
def delete_product(product_id):
    product = ProductModel.query.get(product_id)
    if not product:
        return {"message": "Product not found"}, HTTPStatus.NOT_FOUND
    product.remove
    return "", HTTPStatus.NO_CONTENT


@router.route("/products/<int:product_id>/comments", methods=["POST"])
@secure_route
def create_comment(product_id):
    comment_dict = request.json
    try:
        comment = comment_schema.load(comment_dict)
    except ValidationError as e:
        return {"errors": e.messages, "message": "Unable to post comment."}
    comment.product_id = product_id
    comment.user_id = g.current_customer
    comment.save()
    return comment_schema.jsonify(comment), HTTPStatus.CREATED


@router.route("/products/<int:product_id>/comments/<int:comment_id>", methods=["PUT"])
@secure_route
def update_comment(product_id, comment_id):
    comment_dict = request.json
    current_comment = CommentModel.query.get(comment_id)
    if not current_comment:
        return {"message": "Comment doesn't exist"}, HTTPStatus.NOT_FOUND
    try:
        comment = comment_schema.load(
            comment_dict,
            instance=current_comment,
            partial=True
        )
    except ValidationError as e:
        return {"error": e.messages, "messages": "Could not update comment."}
    comment.save()
    product = ProductModel.query.get(product_id)
    if not product:
        return {"message": "Product not found"}, HTTPStatus.NOT_FOUND
    return product_schema.jsonify(product), HTTPStatus.OK

@router.route("/products/<int:product_id>/comments/<int:comment_id>", methods=["DELETE"])
@secure_route
def delete_comment(product_id, comment_id):
    comment = CommentModel.query.get(comment_id)
    if not comment:
        return {"message": "Comment doesn't exist"}, HTTPStatus.NOT_FOUND
    comment.remove()
    product = ProductModel.query.get(product_id)
    if not product:
        return {"message": "Product not found"}, HTTPStatus.NOT_FOUND
    return product_schema.jsonify(product), HTTPStatus.OK

@router.route("/products/<int:product_id>/ratings", methods=["POST"])
@secure_route
def add_rating(product_id):
    rating = request.json
    try:
        rating = rating_schema.load(rating)
    except ValidationError as e:
        return {"errors": e.messages, "message": "Unable to add rating."}
    rating.product_id = product_id
    rating.user_id = g.current_customer
    rating.save()
    return rating_schema.jsonify(rating), HTTPStatus.CREATED
    