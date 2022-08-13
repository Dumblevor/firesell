from http import HTTPStatus
import jwt

from functools import wraps
from flask import request, g
from models.customer import CustomerModel
from config.envir import secret


def secure_route(route_func):
    @wraps(route_func)
    def decorated_function(*args, **kwargs):
        raw_token = request.headers.get("Authorization")
        if not raw_token:
            return {
                "message": "Unauthorized, please check your credentials and try again"
            }, HTTPStatus.UNAUTHORIZED
        clean_token = raw_token.replace("Bearer ", "")

        try:
            payload = jwt.decode(clean_token, secret, "HS256")
            customer_id = payload["sub"]
            customer = CustomerModel.query.get(customer_id)

            if not customer:
                return {
                    "message": "Unauthorized, please check your credentials and try again"
                }, HTTPStatus.UNAUTHORIZED
            g.current_customer = customer

        except jwt.ExpiredSignatureError:
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED

        except Exception as e:
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

        return route_func(*args, **kwargs)

    return decorated_function
