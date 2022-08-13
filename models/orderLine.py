from datetime import datetime
from models.basemodel import BaseModel
from app import db

class OrderLineModel(db.Model, BaseModel):
    __tablename__ = "order_lines"

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    quantity = db.Column(db.Integer)

    product = db.relationship("ProductModel", back_populates="orders")
    order = db.relationship("OrderModel", back_populates="products")
    