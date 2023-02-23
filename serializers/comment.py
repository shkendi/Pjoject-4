
from marshmallow import fields
from app import ma
from models.comment import CommentModel

class CommentSchema(ma.SQLAlchemyAutoSchema):
    user = fields.Nested("UserSchema", many=False)

    class Meta:
        model = CommentModel
        load_instance = True
