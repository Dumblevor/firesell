from datetime import datetime
from app import db


OrderLine = db.Table('OrderLine',
    id = db.Column(db.Integer, primary_key=True),
    created_at = db.Column(db.DateTime, default=datetime.utcnow),
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    product_id = db.Column('productID', db.Integer, db.ForeignKey('products.id')),
    order_id = db.Column('orderID', db.Integer, db.ForeignKey('orders.id')),
    quantity = db.Column('quantity', db.Integer)
)