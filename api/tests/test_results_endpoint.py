import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock

from globals.globals import app
from flask_api import status


class MockRaceParticipant:
    def __init__(self, id, id_snail, id_race):
        self.id = id
        self.id_snail = id_snail
        self.id_race = id_race


class MockRaceResults:
    def __init__(self, id, position, time_to_finish, did_not_finish, id_race_participants):
        self.id = id
        self.position = position
        self.time_to_finish = time_to_finish
        self.did_not_finish = did_not_finish
        self.id_race_participants = id_race_participants


class TestResultsEndpoint(TestCase):

    def setUp(self):
        self.client = app.test_client()

    @mock.patch('db.models.RaceParticipants.get_race_results', MagicMock(return_value=[(MockRaceParticipant(1, 3, 1), MockRaceResults(1, 1, 400, False, 1))]))
    def test_results_authorized_body(self):

        with self.client as client:
            response = client.get("/auth/token")
            token = response.get_json()['token']
            headers = {'Authorization': token}

        result = client.get('/results', headers=headers).get_json()
        expected_result = [{
            "id_race": 1,
            "snails": [
                {"id_snail": 3, "position_snail": 1,
                 "time_snail": 400, "DNF": False}
            ]
        }]
        self.assertEqual(result, expected_result)

    @mock.patch('db.models.RaceParticipants.get_race_results', MagicMock(return_value=[(MockRaceParticipant(1, 3, 1), MockRaceResults(1, 1, 400, False, 1))]))
    def test_results_authorized_status_code(self):
        with self.client as client:
            response = client.get("/auth/token")
            token = response.get_json()['token']
            headers = {'Authorization': token}
            response = client.get('/results', headers=headers)

            self.assertTrue(status.is_success(response.status_code))

    @mock.patch('db.models.RaceParticipants.get_race_results', MagicMock(return_value=[(MockRaceParticipant(1, 3, 1), MockRaceResults(1, 1, 400, False, 1))]))
    def test_results_no_data_in_db_404(self):
        with self.client as client:
            response = client.get('/results')
            self.assertTrue(status.is_client_error(response.status_code))

    def test_results_unauthorized_body(self):
        with self.client as client:
            result = client.get('/results').get_json()
            expected_result = {
                'status': 'Failed',
                'message': 'Unauthorized'
            }
            self.assertEqual(result, expected_result)

    def test_results_unauthorised_status_code(self):
        with self.client as client:
            response = client.get('/results')
            self.assertTrue(status.is_client_error(response.status_code))


if __name__ == '__main__':
    unittest.main()
