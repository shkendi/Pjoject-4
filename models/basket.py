
from app import db
from models.base import BaseModel

class BasketModel(db.Model, BaseModel):

    __tablename__ = 'baskets'

    # user_gift = db.Column(db.Text, nullable=False, unique=True)
    gift_id = db.Column(db.Integer, db.ForeignKey("gifts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # ! relationship to gifts
    gifts = db.relationship('UserGiftModel', back_populates="basket")
    costumer = db.relationship("UserModel", back_populates="basket")