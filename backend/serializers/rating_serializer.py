from marshmallow import fields
from app import ma
from models.rating import RatingModel


class RatingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RatingModel
        load_instance = True
        include_fk = True
