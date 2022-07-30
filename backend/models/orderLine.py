from datetime import datetime
from app import db


orderLine = db.Table('orderLines',
    # id = db.Column(db.Integer, primary_key=True),
    # created_at = db.Column(db.DateTime, default=datetime.utcnow),
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    db.Column('productID', db.Integer, db.ForeignKey('products.id'),  primary_key=True),
    db.Column('orderID', db.Integer, db.ForeignKey('orders.id'),  primary_key=True)
    # quantity = db.Column('quantity', db.Integer)
)