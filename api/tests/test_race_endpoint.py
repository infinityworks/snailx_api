import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock

from globals.globals import app
from flask_api import status

from endpoints.races.races import races_endpoint

class MockRace:
    def __init__(self, id, date, status, id_round):
        self.id = id
        self.date = date
        self.status = status
        self.id_round = id_round

class MockRaceParticipants:
    def __init__(self, id, id_snail, id_race):
        self.id = id
        self.id_snail = id_snail
        self.id_race = id_race

class TestRaceEndpoint(TestCase):

    def setUp(self):
        self.client = app.test_client()

    @mock.patch('db.models.Race.get_all_races', MagicMock(return_value=[MockRace(1, "2018-10-10 10:00:00", "RAINED OFF", 1)]))
    @mock.patch('db.models.RaceParticipants.get_race_participants_race_id', MagicMock(return_value=[MockRaceParticipants(1,2,1), MockRaceParticipants(2,1,1)]))
    def test_races_authorized_body(self):

        with self.client as client:
            response = client.get("/auth/token")
            token = response.get_json()['token']
            headers = {'Authorization': token}

        result = client.get('/races', headers=headers).get_json()
        expected_result = [{
            "id": 1,
            "date": "2018-10-10 10:00:00",
            "status": "RAINED OFF",
            "id_round": 1,
            "id_snails": [2, 1]
            }
            ]
        self.assertEqual(result, expected_result)

    @mock.patch('db.models.Race.get_all_races', MagicMock(return_value=None))
    def test_races_no_data_in_db_404(self):
        with self.client as client:
            response = client.get('/races')
            self.assertTrue(status.is_client_error(response.status_code))

    def test_races_unauthorized_body(self):
        with self.client as client:
            result = client.get('/races').get_json()
            expected_result = {
                'status': 'Failed',
                'message': 'Unauthorized'
            }
            self.assertEqual(result, expected_result)

    def test_races_unauthorised_status_code(self):
        with self.client as client:
            response = client.get('/races')
            self.assertTrue(status.is_client_error(response.status_code))




if __name__ == '__main__':
    unittest.main()
