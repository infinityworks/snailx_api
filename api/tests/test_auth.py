import unittest
import datetime
import jwt
import time
from auth.auth import Auth
from unittest import mock
from unittest.mock import MagicMock, Mock

from globals.globals import app


class TestAuthBlueprint(unittest.TestCase):

    def setUp(self):
        self.auth = Auth(app)

    def test_encode_auth_token(self):
        token = self.auth.encode_auth_token()
        self.assertIsInstance(token, bytes)

    def test_decode_auth_token_success(self):
        token = self.auth.encode_auth_token()
        self.assertTrue(self.auth.decode_auth_token(
            token) == self.auth.HARDCODED_USER_ID)

    @mock.patch('auth.auth.Auth.decode_auth_token')
    def test_decode_auth_token_invalid(self, mock_auth_decode):
        invalid_token = b'junktokenisinvalid'
        mock_auth_decode.side_effect = jwt.InvalidTokenError

        with self.assertRaises(jwt.InvalidTokenError):
            result = self.auth.decode_auth_token(invalid_token)
            self.assertEqual(result, self.auth.invalid_token)

    @mock.patch('auth.auth.Auth.decode_auth_token')
    def test_decode_auth_token_expired(self, mock_auth_decode):
        expired_token = b'junktokenisexpired'
        mock_auth_decode.side_effect = jwt.ExpiredSignatureError

        with self.assertRaises(jwt.ExpiredSignatureError):
            result = self.auth.decode_auth_token(expired_token)
            self.assertEqual(result, self.auth.expired_token)


if __name__ == '__main__':
    unittest.main()
