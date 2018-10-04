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
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e
