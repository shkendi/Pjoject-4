from datetime import datetime, timedelta
import jwt
from sqlalchemy.ext.hybrid import hybrid_property
from app import db, bcrypt
from models.base import BaseModel
# from models.user_gift import UserGiftModel
from config.environment import secret


class UserModel(db.Model, BaseModel):
    __tablename__ = "users"

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)

    password_hash = db.Column(db.Text, nullable=True)

    gifts = db.relationship("GiftModel", backref="users")

    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, password_plaintext):
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)
        self.password_hash = encoded_pw.decode("utf-8")

    def validate_password(self, password_plaintext):
        return bcrypt.check_password_hash(self.password_hash, password_plaintext)

    # ! Create a json web token for the user
    def generate_token(self):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=7),
            "iat": datetime.utcnow(),
            "sub": self.id,  # ! This is the ID of the user.. we can use this later
        }

        token = jwt.encode(
            payload,
            secret,
            algorithm="HS256",
        )
        return token
