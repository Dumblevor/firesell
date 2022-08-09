from app import ma
from models.product import ProductModel
from marshmallow import fields
from serializers.comment_serializer import CommentSchema
from serializers.picture_serializer import PictureSchema
from serializers.rating_serializer import RatingSchema
from serializers.seller_serializer import SellerSchema

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance = True
        include_fk = True


    comments = fields.Nested("CommentSchema", many=True)
    seller = fields.Nested("SellerSchema", many=False)
    ratings = fields.Nested("RatingSchema", many=True)
    pictures = fields.Nested("PictureSchema", many=True)