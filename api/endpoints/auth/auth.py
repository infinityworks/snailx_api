from flask import Blueprint, make_response
from auth.auth import Auth
from globals.globals import app

auth_endpoint_blueprint = Blueprint('auth', __name__)


@auth_endpoint_blueprint.route('/auth/token')
def auth_token():
    """Endpoint to retrieve an Authorization token.

    Returns:
        JSON -- Containing 'token' key with corresponding Authorization token.
    """

    try:
        auth = Auth(app)
        token = auth.encode_auth_token()
        return make_response({"token": token.decode('utf-8')}), 200
    except Exception as e:
        return e
