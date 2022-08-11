from marshmallow import fields
from app import ma
from models.comment import CommentModel


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CommentModel
        load_instance = True

    user = fields.Nested("CustomerShema", many=False)
