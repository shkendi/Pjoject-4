
from app import db
from models.base import BaseModel
# from models.user import UserModel


class UserGiftModel(db.Model, BaseModel):
    __tablename__ = "users_gifts"

    gift_id = db.Column(db.Integer, db.ForeignKey("gifts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

#     # ! Add relationships to the GiftModel and NoteModel.
#     # ! back_populates is telling you which model to create relationship with.
    # gifts = db.relationship("GiftModel", back_populates="users_gifts")
    # users = db.relationship("UserModel", back_populates="gifts")
    customer = db.relationship("UserModel", back_populates="basket")
    gift = db.relationship("GiftModel", back_populates="customers")