import unittest
from globals.globals import app


class TestSnailsEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_snails_without_auth(self):
        with self.app as client:
            response = client.get("/snails").get_json()
            expected_result = {
                'status': 'Failed',
                'message': 'Unauthorized'
            }
            self.assertEqual(response, expected_result)

    def test_get_snails_with_auth(self):
        token = ""
        with self.app as client:
            response = client.get("/auth/token").get_json()
            token = response['token']

        headers = {'Authorization': token}
        with self.app as client:
            response = client.get("/snails", headers=headers).get_json()
            expected_result = {
                "id": 1,
                "name": "Little Gazza",
                "trainer": {
                        "id": 1,
                        "name": "Gazza"
                }
            }
            self.assertEqual(response, expected_result)


if __name__ == '__main__':
    unittest.main()
