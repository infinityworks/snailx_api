import unittest
from globals.globals import app
from flask import jsonify
from flask_api import status


class TestAuthEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_auth_get_token_body(self):
        with self.app as client:
            response = client.get("/auth/token").get_json()
            expectedResponse = {'token': response['token']}

            self.assertEqual(response, expectedResponse)

    def test_auth_get_token_status_code(self):
        with self.app as client:
            response = client.get("/auth/token")
            self.assertTrue(status.is_success(response.status_code))


if __name__ == '__main__':
    unittest.main()
