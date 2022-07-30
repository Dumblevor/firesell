from app import db
from models.basemodel import BaseModel


class CommentModel(db.Model, BaseModel):
    __tablename__ = "comments"

    content = db.Column(db.Text, nullable=False, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

