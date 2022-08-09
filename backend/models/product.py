from app import db
from models.basemodel import BaseModel
from models.order import OrderModel
from models.orderLine import OrderLineModel
from models.catPro import catPro
from models.rating import RatingModel
from models.comment import CommentModel
from models.product_category import CategoryModel
from models.picture import PictureModel


class ProductModel(db.Model, BaseModel):
    __tablename__ = "products"

    name = db.Column(db.Text, nullable=False, unique=False)
    price = db.Column(db.Float, nullable=False, unique=False)
    description = db.Column(db.Text, nullable=False, unique=False)
    
    product_owner_ID = db.Column(db.Integer, db.ForeignKey("sellers.id", ondelete='CASCADE'), nullable=False)
    
    categories = db.relationship("CategoryModel", backref='products', secondary=catPro)
    comments = db.relationship("CommentModel", backref='products', cascade="all, delete")
    ratings = db.relationship("RatingModel", backref='products',  cascade="all, delete")
    pictures = db.relationship("PictureModel", backref='products',  cascade="all, delete")

    orders = db.relationship("OrderLineModel", back_populates="product")