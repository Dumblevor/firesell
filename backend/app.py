from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from config.envir import db_URI
...
from flask_cors import CORS
...

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)

bcrypt = Bcrypt(app)

from controllers import customers, products, orders, sellers

app.register_blueprint(customers.router, url_prefix="/api")
app.register_blueprint(products.router, url_prefix="/api")
app.register_blueprint(orders.router, url_prefix="/api")
app.register_blueprint(sellers.router, url_prefix="/api")
