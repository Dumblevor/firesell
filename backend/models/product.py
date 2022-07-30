from app import db
from models.basemodel import BaseModel
from models.catPro import catPro

class ProductModel(db.Model, BaseModel):
    __tablename__ = "products"

    name = db.Column(db.Text, nullable=False, unique=False)
    price = db.Column(db.Float, nullable=False, unique=False)
    description = db.Column(db.Text, nullable=False, unique=False)
    product_owner_ID = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    
    categories = db.relationship("CategoryModel", backref='products', secondary=catPro)
    comments = db.relationship("CommentModel", backref='products')
    ratings = db.relationship("RatingModel", backref='products')
    orderLines = db.relationship("OrderLine", backref='products')