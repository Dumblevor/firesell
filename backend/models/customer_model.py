from datetime import datetime, timedelta
from sqlalchemy.ext.hybrid import hybrid_property
import jwt
from config.envir import secret
from app import db, bcrypt
from models.basemodel import BaseModel
from models.order import OrderModel
from models.rating import RatingModel
from models.comment import CommentModel

class CustomerModel(db.Model, BaseModel):
    __tablename__ = "customers"

    name = db.Column(db.Text, nullable=False, unique=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Text, nullable=False, unique=False)
    address = db.Column(db.Text, nullable=False, unique=False)

    orders = db.relationship("OrderModel", backref="customers")
    comments = db.relationship("CommentModel", backref="customers")
    ratings = db.relationship("RatingModel", backref="customers")







    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, plaintext_password):
        encoded_pw = bcrypt.generate_password_hash(plaintext_password)
        self.password_hash = encoded_pw.decode("utf-8")

    def validate_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password_hash, plaintext_password)

    def generate_token(self):

        payload = {
            "exp": datetime.utcnow() + timedelta(days=1),
            "iat": datetime.utcnow(),
            "sub": self.id,
        }

        token = jwt.encode(payload, secret, algorithm="HS256")

        return token
