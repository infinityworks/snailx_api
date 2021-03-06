from flask import request, make_response
import datetime
import jwt
from flask_api import status


class Auth:

    def __init__(self, app):
        self.app = app
        self.secret = app.config.get('SECRET_KEY')
        self.HARDCODED_USER_ID = 1
        self.expired_token = 'Signature expired. Please log in again.'
        self.invalid_token ='Invalid token. Please log in again.'
        self.auth_header_name = 'Authorization'

    def encode_auth_token(self):
        """
        Generates an API auth token.
        Returns:
            bytes -- auth token
        """

        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
            'iat': datetime.datetime.utcnow(),
            'sub': self.HARDCODED_USER_ID
        }

        token = jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )
        return token

    # TODO: change to use user ids and not hardcoded single user.
    def decode_auth_token(self, auth_token):
        """Decodes an API auth token.

        Arguments:
            auth_token {string} -- The string token provided as in Authorization header.

        Returns:
            int -- The user_id of the token.
        """

        try:
            payload = jwt.decode(auth_token, self.secret)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return self.expired_token
        except jwt.InvalidTokenError:
            return self.invalid_token

    def authenticate_request(self):
        req_token = request.headers.get(self.auth_header_name)
        if req_token:
            req_user_id = self.decode_auth_token(req_token)
            # hardcoded single user id for mvp
            if req_user_id == self.HARDCODED_USER_ID:
                return True
        return False

    def unauthorized_response(self):
        responseObject = {
            'status': 'Failed',
            'message': 'Unauthorized'
        }
        return make_response(responseObject), status.HTTP_401_UNAUTHORIZED
