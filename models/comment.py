from app import db
from models.base import BaseModel


class CommentModel(db.Model, BaseModel):
    __tablename__ = "comments"

    content = db.Column(db.Text, nullable=False)

    # ! ForeignKey tells you which column to point at (gifts.id)
    # ! so that every comment points to a specific unique gift.
    # ! You usually give it the primarykey of a table, e.g. gifts.id
    gift_id = db.Column(db.Integer, db.ForeignKey("gifts.id"), nullable=False)
