from app import db
from models.basemodel import BaseModel
from models.orderLine import orderLine

class OrderModel(db.Model, BaseModel):
    __tablename__ = "orders"

    totalAmount = db.Column(db.Float, nullable=True, unique=False)
    orderStatus = db.Column(db.Text, nullable=True, unique=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)