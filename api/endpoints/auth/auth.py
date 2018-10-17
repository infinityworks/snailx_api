from flask import Blueprint, make_response
from flask_api import status
from auth.auth import Auth
from globals.globals import app
from db.models import User

auth_endpoint_blueprint = Blueprint('auth', __name__)


@auth_endpoint_blueprint.route('/auth/users')
def get_user():
    users = User().get_users()
    if users:
        users_json = []
        for user in users:
            users_json.append({'username': user.username,
                               'email': user.email,
                               'password': user.password})
        json = {'users': users_json}
    return make_response(json), status.HTTP_200_OK


@auth_endpoint_blueprint.route('/auth/token')
def auth_token():
    """Endpoint to retrieve an Authorization token.

    Returns:
        JSON -- Containing 'token' key with corresponding Authorization token.
    """

    try:
        auth = Auth(app)
        token = auth.encode_auth_token()
        return make_response({"token": token.decode('utf-8')}), status.HTTP_200_OK
    except Exception as e:
        return e
