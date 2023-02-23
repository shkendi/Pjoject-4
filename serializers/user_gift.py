# from marshmallow import fields
# from app import ma
# from models.user_gift import UserGiftModel


# class UserGiftSchema(ma.SQLAlchemyAutoSchema):
#     user_gift = fields.Nested("UserGiftSchema")

#     class Meta:
#         # ! Need to tell marshmallow to include the foreign
#         include_fk = True
#         model = UserGiftModel
#         load_instance = True
