from http import HTTPStatus
from flask import Blueprint, request, g
from marshmallow.exceptions import ValidationError
from models.user import UserModel
from serializers.user import UserSchema
from serializers.user_gift import UserGiftSchema
from middleware.secure_route import secure_route


user_schema = UserSchema()
user_gift_schema = UserGiftSchema()

router = Blueprint("users", __name__)


@router.route("/signup", methods=["POST"])
def signup():
    try:
        user_dictionary = request.json
        user = user_schema.load(user_dictionary)
        user.save()
        return user_schema.jsonify(user)
    except ValidationError as e:
        return {"errors": e.messages, "messsages": "Something went wrong"}
    except Exception as e:
        return {"messages": "Something went wrong"}


@router.route("/login", methods=["POST"])
def login():
    try:
        user_dictionary = request.json
        user = UserModel.query.filter_by(email=user_dictionary["email"]).first()
        if not user:
            return {"message": "Your email or password was incorrect."}
        if not user.validate_password(user_dictionary["password"]):
            return {
                "message": "Your email or password was incorrect."
            }, HTTPStatus.UNAUTHORIZED
        token = user.generate_token()
        return {"token": token, "message": "Welcome back!"}
    except Exception as e:
        return {"messages": "Something went wrong"}


@router.route("/user", methods=["GET"])
@secure_route
def get_user():
    user = UserModel.query.get(g.current_user.id)
    print(user)
    return user_schema.jsonify(user, many=False), HTTPStatus.OK


@router.route('/user_gift', methods=["POST"])
@secure_route
def create_user_gift():

    user_gift_dictionary = request.json

    try:
        user_gift = user_gift_schema.load(user_gift_dictionary)
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}

    user_gift.save()

    return user_gift_schema.jsonify(user_gift), HTTPStatus.CREATED
