from app import db
from models.basemodel import BaseModel


class CategoryModel(db.Model, BaseModel):
    __tablename__ = "categories"

    name = db.Column(db.Text, nullable=False, unique=False)