import unittest
import sys
sys.path.insert(0, '/vagrant/repos/snailx_api/api')
from globals.globals import app


class TestRaceEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_race_without_auth(self):
        with self.app as client:
            response = client.get("/race").get_json()
            expected_result = {
                'status': 'Failed',
                'message': 'Unauthorized'
            }
            self.assertEqual(response, expected_result)

    def test_get_race_with_auth(self):
        token = ""
        with self.app as client:
            response = client.get("/auth/token").get_json()
            token = response['token']

        headers = {'Authorization': token}
        with self.app as client:
            response = client.get("/race", headers=headers).get_json()
            expected_result = {
            "id": 1,
            "date": "Tue, 05 Sep 2017 09:45:28 GMT",
            "status": "OK",
            "id_round": 1,
            "id_snails": [1,2]
            }
            self.assertEqual(response, expected_result)


if __name__ == '__main__':
    unittest.main()
