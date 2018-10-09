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
        # token = ""
        # with self.app as client:
        #     response = client.get("/auth/token").get_json()
        #     token = response['token']

        # headers = {'Authorization': token}
        # with self.app as client:
        #     response = client.get("/snails", headers=headers).get_json()
        #     expected_result = {'id': 1, 'name': 'Terry',
        #                        'age': 13, 'trainer': {'id': 17, 'name': 'gazza'}}
        #     self.assertEqual(response, expected_result)
        self.pass()


if __name__ == '__main__':
    unittest.main()
