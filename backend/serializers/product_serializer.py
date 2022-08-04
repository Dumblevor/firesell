from app import ma
from models.product import ProductModel
from marshmallow import fields


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance = True

    comments = fields.Nested("CommentSchema", many=True)
    seller = fields.Nested("SellerSchema", many=False)
    rating = fields.Nested("RatingSchema", many=False)