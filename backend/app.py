from flask import Flask
from flask_sqlaclhemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from config.envir import db_URI

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)

bcrypt = Bcrypt(app)

