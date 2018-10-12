import unittest
from globals.globals import app


class MockResult:

class TestResultsEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_results_without_auth(self):
        with self.app as client:
            response = client.get("/results").get_json()
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
            response = client.get("/results", headers=headers).get_json()
            expected_result = {
                "id_race": 1,
                "snails": [
                    {"id_snail": 1, "position_snail:": 3, "time_snail": 600, "DNF": False},
                    {"id_snail": 2, "position_snail:": 2, "time_snail": 500, "DNF": False},
                    {"id_snail": 3, "position_snail:": 1, "time_snail": 400, "DNF": False}
                ]
            }
            self.assertEqual(response, expected_result)


if __name__ == '__main__':
    unittest.main()
