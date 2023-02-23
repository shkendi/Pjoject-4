
# ! import marshmallow
from app import ma
# ! Model for notes
from models.basket import BasketModel


class BasketSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = BasketModel
        load_instance = True