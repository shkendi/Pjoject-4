from http import HTTPStatus
from functools import wraps
from marshmallow.exceptions import ValidationError
from flask import g, request
import jwt
from config.environment import secret
from models.user import UserModel



def secure_route(route_func):
    @wraps(route_func)
    def decorated_function(*args, **kwargs):
        raw_token = request.headers.get("Authorization")
        if not raw_token:
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        clean_token = raw_token.replace("Bearer ", "")

        try:
            payload = jwt.decode(clean_token, secret, "HS256")
            user_id = payload["sub"]
            user = UserModel.query.get(user_id)

            if not user:
                return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

            g.current_user = user
        except jwt.ExpiredSignatureError:
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED

        except Exception as e:
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

        return route_func(*args, **kwargs)

    return decorated_function


# def secure_route(func):

#     # ! wrap func, so use later
#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         # * get token from request
#         raw_token = request.headers.get('Authorization')
#         # * Check the token exists
#         if not raw_token:
#             return { "message": "Unauthorized" }, HTTPStatus.UNAUTHORIZED
#         # * clean up the token
#         clean_token = raw_token.replace("Bearer ", "")

#         try:
#             # * Get the payload, this has the user id + expiry inside.
#             payload = jwt.decode(
#                 clean_token, # * provide the token
#                 secret, # * the secret we made earlier
#                 "HS256" # * the algo we used to encode the token
#             )
#             # * get the user id from the token (called sub)
#             user_id = payload['sub']
#             # * get the user from the database
#             user = UserModel.query.get(user_id)
#             # * check if user exists
#             if not user:
#                 return { "message": "Unauthorized" }, HTTPStatus.UNAUTHORIZED
#             # * At this point we know the user is authorized!

#         # * This error will happen if the token is expired.
#         except jwt.ExpiredSignatureError:
#             return { "message": "Unauthorized" }, HTTPStatus.UNAUTHORIZED
#         # * This error will happen if anything else went wrong with the token.
#         except Exception:
#             return { "message": "Unauthorized" }, HTTPStatus.UNAUTHORIZED

#         # ! Write our stuff to secure our app.
#         return func(*args, **kwargs)

#     return wrapper
