import re
from marshmallow import fields, ValidationError
from app import ma
from models.user import UserModel


# ! Here is a function for validating my password
def validate_password(password):
    if len(password) < 8:
        raise ValidationError("Make sure your password is at least 8 characters.")
    elif re.search("[0-9]", password) is None:
        raise ValidationError("Make sure your password contains a number.")
    elif re.search("[A-Z]", password) is None:
        raise ValidationError("Make sure your password contains a capital letter.")


class UserSchema(ma.SQLAlchemyAutoSchema):
    password = fields.String(required=True, validate=validate_password)

    class Meta:
        model = UserModel
        load_instance = True
        exclude = ("password_hash",)
        load_only = ("email", "password")

        # password_confirmation = fields.String(required=True)
		# password = fields.String(required=True, validate=validate_password)


# @validates_schema
# def check_passwords_match(self, data):
#     if data.get("password") != data.get("password_confirmation"):
#         raise ValidationError("Passwords do not match", "password_confirmation")
