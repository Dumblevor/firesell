from http import HTTPStatus
from flask import Blueprint, request
from models.product import ProductModel
from models.seller_model import SellerModel
from serializers.seller_serializer import SellerSchema
from marshmallow.exceptions import ValidationError

seller_schema = SellerSchema()


router = Blueprint("sellers", __name__)


@router.route("/newseller", methods=["POST"])
def register_seller():
    try:
        seller_dictionary = request.json
        print("1", seller_dictionary)
        seller = seller_schema.load(seller_dictionary)
        print("2", seller)

        seller.save()
        print("3")
        return seller_schema.jsonify(seller)
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong1."}

    except Exception as e:
        print(e)
        return {"messages": "Something went wrong2."}


@router.route("/sellerlogin", methods=["POST"])
def seller_login():
    try:
        credentials_dictionary = request.json
        seller = SellerModel.query.filter_by(
            email=credentials_dictionary["email"]
        ).first()

        if not seller:
            return {
                "message": "No user associated with this email was found, please check the email entered and try again."
            }, HTTPStatus.NOT_FOUND
        if not seller.validate_password(credentials_dictionary["password"]):
            return {"message": "You are not autorized."}, HTTPStatus.UNAUTHORIZED
        token = seller.generate_token()
        return {"token": token, "message": "Welcome back!"}

    except Exception as e:
        return {"message": "Something went wrong"}


