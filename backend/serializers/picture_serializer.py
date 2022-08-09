from marshmallow import fields
from app import ma
from models.picture import PictureModel

class PictureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PictureModel
        load_instance = True
        include_fk = True
