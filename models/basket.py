
from app import db
from models.base import BaseModel

class BasketModel(db.Model, BaseModel):

    __tablename__ = 'baskets'

    name = db.Column(db.Text, nullable=False, unique=True)

    # ! relationship to gifts
    gifts = db.relationship('UserGiftModel', back_populates="basket")