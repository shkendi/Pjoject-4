from app import db
from models.base import BaseModel
# from models.comment import CommentModel
from models.user_gift import UserGiftModel

class GiftModel(db.Model, BaseModel):
    __tablename__ = "gifts"

    name = db.Column(db.Text, nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    in_stock = db.Column(db.Boolean, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


    comments = db.relationship("CommentModel", backref="gifts", cascade="all, delete")
    # user = db.relationship("UserModel", backref="gifts")
    customers = db.relationship('UserGiftModel', back_populates="gift")