from app import db
from models.basemodel import BaseModel
from models.orderLine import OrderLineModel

class OrderLineSchema(db.Model, BaseModel):
    class Meta:
        model = OrderLineModel
        load_instance = True
