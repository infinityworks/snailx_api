from flask import Blueprint, request, make_response, jsonify
import datetime
import jwt
from flask import current_app as app

auth_blueprint = Blueprint('auth', __name__)
HARDCODED_USER_ID = 1


@auth_blueprint.route('/auth/token')
def auth_token():
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
            'iat': datetime.datetime.utcnow(),
            'sub': HARDCODED_USER_ID
        }

        token = jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )

        return make_response({"token": token.decode('utf-8')}), 200
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def authenticate_request():
    req_token = request.headers.get('Authorization')
    if req_token:
        req_user_id = decode_auth_token(req_token)
        # hardcoded single user id for mvp
        if req_user_id == HARDCODED_USER_ID:
            return True
    return False


def unauthorised_response():
    responseObject = {
        'status': 'fail',
        'message': 'Unauthorised'
    }
    return make_response(responseObject), 401
