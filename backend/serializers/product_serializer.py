from app import ma
from models.product import ProductModel
from marshmallow import fields
from serializers.comment_serializer import CommentSchema

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance = True
        include_fk = True


    comments = fields.Nested("CommentSchema", many=True)
    seller = fields.Nested("SellerSchema", many=False)
    rating = fields.Nested("RatingSchema", many=False)