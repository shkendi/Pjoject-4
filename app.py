
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# ! Import the plugin
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from config.environment import db_URI
# from models.user_gift import UserGiftModel



app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = db_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ! Instantiate sqlalchemy with our flask app.
db = SQLAlchemy(app)

# ! Instantiate Marshmallow within flask
ma = Marshmallow(app)

# ! Instantiate bcrypt
bcrypt = Bcrypt(app)

from controllers import gifts, users

app.register_blueprint(gifts.router, url_prefix="/api")
app.register_blueprint(users.router, url_prefix="/api")
# app.register_blueprint(UserGiftModel.router, url_prefix="/api")
