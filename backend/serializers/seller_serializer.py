from marshmallow import fields
from app import ma
from models.seller_model import SellerModel

class SellerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SellerModel
        load_instance = True
        exclude = ("password_hash",)
        load_only = ('email', 'password')

    password = fields.String(required=True)
    