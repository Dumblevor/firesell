from app import db
from models.basemodel import BaseModel


class OrderModel(db.Model, BaseModel):
    __tablename__ = "orders"

    totalAmount = db.Column(db.Float, nullable=True, unique=False)
    orderStatus = db.Column(db.Text, nullable=True, unique=True)
    customer_id = db.Columnt(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    order_lines = db.relationship("OrderLine")