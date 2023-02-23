from marshmallow import fields
from app import ma
from models.gift import GiftModel


class GiftSchema(ma.SQLAlchemyAutoSchema):
    comments = fields.Nested("CommentSchema", many=True)
    user = fields.Nested("UserSchema", many=False)

    class Meta:
        model = GiftModel
        load_instance = True
        include_fk = True
