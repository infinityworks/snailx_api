import unittest
from globals.globals import app
from flask_api import status


class TestSnailsEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_snails_without_auth_response_code(self):
        with self.app as client:
            response = client.get("/snails")
            self.assertTrue(status.is_client_error(response.status_code))

    def test_get_snails_without_auth_response_body(self):
        with self.app as client:
            response = client.get("/snails")
            response_json = response.get_json()
            expected_result = {
                'status': 'Failed',
                'message': 'Unauthorized'
            }
            self.assertEqual(response_json, expected_result)

    def test_get_snails_with_auth_response_code(self):
        pass
        # token = ""
        # with self.app as client:
        #     response = client.get("/auth/token")
        #     token = response.get_json()['token']

        # headers = {'Authorization': token}
        # with self.app as client:
        #     response = client.get("/snails", headers=headers)
        #     self.assertTrue(status.is_success(response.status_code))

    def test_get_snails_with_auth_response_body(self):
        pass
            


if __name__ == '__main__':
    unittest.main()
