from http import HTTPStatus

from marshmallow.exceptions import ValidationError
from flask import Blueprint, g, request
# from sqlalchemy import text
from models.comment import CommentModel
from models.gift import GiftModel
# from models.gift_data import gifts_list
# from app import db
from middleware.secure_route import secure_route
# from models.user_gift import UserGiftModel
from serializers.gift import GiftSchema
from serializers.comment import CommentSchema
from serializers.user import UserSchema
# from serializers.user_gift import UserGiftSchema

# ! Instantiate gift schema
gift_schema = GiftSchema()
comment_schema = CommentSchema()
user_schema = UserSchema()
# user_gift_schema = UserGiftSchema()

router = Blueprint("gifts", __name__)


@router.route("/gifts", methods=["GET"])
def get_gifts():
    gifts = GiftModel.query.all()
    print(gifts)
    return gift_schema.jsonify(gifts, many=True), HTTPStatus.OK


@router.route("/gifts/<int:gift_id>", methods=["GET"])
def get_single_gift(gift_id):
    gift = GiftModel.query.get(gift_id)
    # if not gift:
    #     return {"message": "Tea not found"}, HTTPStatus.NOT_FOUND

    return gift_schema.jsonify(gift), HTTPStatus.OK


@router.route("/gifts", methods=["POST"])
@secure_route
def create_gift():
    gift_dictionary = request.json
    gift_dictionary['user_id'] = g.current_user.id

    try:
        gift = gift_schema.load(gift_dictionary)
        gift.save()
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}
    return gift_schema.jsonify(gift)

# ! PUT/PATCH
@router.route("/gifts/<int:gift_id>", methods=["PUT", "PATCH"])
@secure_route
def update_gift(gift_id):
    gift_dictionary = request.json
    existing_gift = GiftModel.query.get(gift_id)

    if not existing_gift:
        return {"message": "No gift found"}, HTTPStatus.NOT_FOUND

    # # ! Add this check whenever we want to make sure the tea is the user's tea that they're trying to update/delete
    # if not g.current_user.id == existing_gift.user_id:
    #     return {"message": "Not your tea!"}, HTTPStatus.UNAUTHORIZED

    try:
        # ! Is this person the tea's owner or not?
        if existing_gift.user_id != g.current_user.id:
            return { "message": "This is not your gift! Get your own gift. ☕️" }, HTTPStatus.UNAUTHORIZED

        gift = gift_schema.load(
            gift_dictionary,
            instance=existing_gift,
            partial=True
        )

        gift.save()
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}
    return gift_schema.jsonify(gift), HTTPStatus.OK

    #     try:
    #     gift = gift_schema.load(gift_dictionary, instance=existing_gift, partial=True)
    # except ValidationError as e:
    #     return {"errors": e.messages, "message": "Something went wrong"}
    # gift.save()
    # return gift_schema.jsonify(gift), HTTPStatus.OK

@router.route("/gifts/<int:gift_id>", methods=["DELETE"])
@secure_route
def remove_gift(gift_id):

    gift = GiftModel.query.get(gift_id)

    if not gift:
        return {"message": "No gift found"}, HTTPStatus.NOT_FOUND
    gift.remove()
    return "", HTTPStatus.NO_CONTENT


# ! Posting a comment
@router.route("/gifts/<int:gift_id>/comments", methods=["POST"])
@secure_route
def create_comment(gift_id):
    comment_dictionary = request.json

    existing_gift = GiftModel.query.get(gift_id)
    if not existing_gift:
        return { "message": "No gift found" }, HTTPStatus.NOT_FOUND

    try:
        comment = comment_schema.load(comment_dictionary)
        comment.gift_id = gift_id
        comment.save()
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}

    return comment_schema.jsonify(comment), HTTPStatus.CREATED


@router.route("/gifts/<int:gift_id>/comments/<int:comment_id>", methods=["PUT"])
@secure_route
def update_comment(gift_id, comment_id):
    comment_dictionary = request.json
    existing_comment = CommentModel.query.get(comment_id)

    if not existing_comment:
        return {"message": "Comment not found"}, HTTPStatus.NOT_FOUND

    try:
        comment = comment_schema.load(
            comment_dictionary, instance=existing_comment, partial=True
        )

    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}

    comment.save()

    gift = GiftModel.query.get(gift_id)

    if not gift:
        return {"message": "Gift not found"}, HTTPStatus.NOT_FOUND

    return gift_schema.jsonify(gift), HTTPStatus.OK


@router.route("/comments/<int:comment_id>", methods=["DELETE"])
@secure_route
def remove_comment(comment_id):
    comment = CommentModel.query.get(comment_id)

    if not comment:
        return {"message": "No comment found"}, HTTPStatus.NOT_FOUND

    comment.remove()
    # gift = GiftModel.query.get(gift_id)
    # if not gift:
    #     return {"message": "Tea not found"}, HTTPStatus.NOT_FOUND

    # return gift_schema.jsonify(gift), HTTPStatus.OK
    return '', HTTPStatus.NO_CONTENT


# @router.route('/user_gift', methods=["POST"])
# @secure_route
# def create_user_gift():

#     user_gift_dictionary = request.json

#     try:
#         user_gift = user_gift_schema.load(user_gift_dictionary)
#     except ValidationError as e:
#         return {"errors": e.messages, "message": "Something went wrong"}

#     user_gift.save()

#     return user_gift_schema.jsonify(user_gift)


# @router.route("/lookup-gifts-vuln/<string:gift_name>", methods=["GET"])
# def lookup_gifts_vuln(gift_name):
#     try:
#         results = db.session.execute(text(f"SELECT * FROM gifts WHERE name LIKE '%{gift_name}%'"))
#         keys = list(results.keys())
#         values = results.fetchall()
#         values = [tuple(row) for row in values]
#         results = [ { key: lst[i] for i, key in enumerate(keys) } for lst in values ]
#         return results
#     except Exception as e:
#         print(e)
#         return {"messages": "Something went wrong"}



# @router.route("/lookup-gifts-sec/<string:gift_name>", methods=["GET"])
# def lookup_gifts_sec(gift_name):
#     try:
#         results = GiftModel.query.filter_by(name=gift_name).all()
#         return gift_schema.jsonify(results, many=True)
#     except Exception as e:
#         print(e)
#         return {"messages": "Something went wrong"}
