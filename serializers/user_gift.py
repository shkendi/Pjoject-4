from marshmallow import fields
from app import ma
from models.user_gift import UserGiftModel
from serializers.gift import GiftSchema

class UserGiftSchema(ma.SQLAlchemyAutoSchema):
    gift = fields.Nested("GiftSchema")

    class Meta:
        # ! Need to tell marshmallow to include the foreign
        include_fk = True
        model = UserGiftModel
        load_instance = True
