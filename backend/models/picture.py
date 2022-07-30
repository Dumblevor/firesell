from app import db
from models.basemodel import BaseModel
from models.product import ProductModel


class PictureModel(db.Model, BaseModel):
    __tablename__ = "pictures"

    description = db.Column(db.Text, nullable=False, unique=False)
    url = db.Column(db.Text, nullable=False, unique=False)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id", ondelete='CASCADE'), nullable=False)
    product = db.relationship('ProductModel', backref="pictures")