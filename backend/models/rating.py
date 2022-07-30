from app import db
from models.basemodel import BaseModel

class RatingModel(db.Model, BaseModel):
    __tablename__ = "ratings"

    rating = db.Column(db.Float, nullable=False, unique=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id", ondelete='CASCADE'), nullable=False)
    comment_owner_id = db.Column(db.Integer, db.ForeignKey("customers.id", ondelete='CASCADE'), nullable=False)