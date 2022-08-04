from marshmallow import fields
from app import ma
from models.customer_model import CustomerModel

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CustomerModel
        load_instance = True
        exclude = ("password_hash",)
        load_only = ('email', 'password')

    password = fields.String(required=True)
    