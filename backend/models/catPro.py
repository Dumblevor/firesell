from app import db

catPro = db.Table('catPros',
    db.Column('categoryID', db.Integer, db.ForeignKey('categories.id'), primary_key=True),
    db.Column('productID', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)