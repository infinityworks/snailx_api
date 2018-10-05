import unittest
from globals.globals import app
from tests.test_auth import MockAuth
from flask import jsonify
from auth.auth import encode_auth_token


class TestAuthEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_auth_token(self):
        with self.app as client:
            response = client.get("/auth/token").get_json()

            expectedResponse = {'token': response['token']}
            self.assertEqual(response, expectedResponse)


if __name__ == '__main__':
    unittest.main()
