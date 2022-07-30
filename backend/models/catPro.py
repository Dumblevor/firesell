from app import db

catPro = db.Table('catPro',
    category_id = db.Column('categoryID', db.Integer, db.ForeignKey('categories.id'), primary_key=True),
    product_id = db.Column('productID', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)