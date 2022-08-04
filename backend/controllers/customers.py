from http import HTTPStatus
from flask import Blueprint, request
from models.product import ProductModel
from models.customer import CustomerModel
from serializers.customer_serializer import CustomerSchema
from marshmallow.exceptions import ValidationError

customer_schema = CustomerSchema()


router = Blueprint("users", __name__)


@router.route("/newcustomer", methods=["POST"])
def register_customer():
    try:
        customer_dictionary = request.json
        print("1", customer_dictionary)
        customer = customer_schema.load(customer_dictionary)
        print("2", customer)

        customer.save()
        print("3")
        return customer_schema.jsonify(customer)
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong1."}

    except Exception as e:
        print(e)
        return {"messages": "Something went wrong2."}


@router.route("/customerlogin", methods=["POST"])
def customer_login():
    try:
        credentials_dictionary = request.json
        customer = CustomerModel.query.filter_by(
            email=credentials_dictionary["email"]
        ).first()

        if not customer:
            return {
                "message": "No user associated with this email was found, please check the email entered and try again."
            }, HTTPStatus.NOT_FOUND
        if not customer.validate_password(credentials_dictionary["password"]):
            return {"message": "You are not autorized."}, HTTPStatus.UNAUTHORIZED
        token = customer.generate_token()
        return {"token": token, "message": "Welcome back!"}

    except Exception as e:
        return {"message": "Something went wrong"}
