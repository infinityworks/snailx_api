import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock

from globals.globals import app
from flask_api import status

from endpoints.results.single.single_result import single_result_endpoint

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

    @mock.patch('db.models.Race.get_all_races', MagicMock(return_value=[MockRace(1, "2018-10-10 10:00:00", "RAINED OFF", 1)]))
    @mock.patch('db.models.RaceParticipants.get_race_participants_race_id', MagicMock(return_value=[MockRaceParticipants(1,3,1)]))
    @mock.patch('db.models.RaceResult.get_race_result', MagicMock(return_value=MockRaceResults(1,1,400,False,1)))
    def test_results_authorized_body(self):

        with self.client as client:
            response = client.get("/auth/token")
            token = response.get_json()['token']
            headers = {'Authorization': token}
        
        result = client.get('/results/1', headers=headers).get_json()
        expected_result =[{
                "id_race": 1,
                "snails": [
                    {"id_snail": 3, "position_snail": 1, "time_snail": 400, "DNF": False}
                ]
            }]
        self.assertEqual(result, expected_result)


    @mock.patch('db.models.Race.get_all_races', MagicMock(return_value=[MockRace(1, "2018-10-10 10:00:00", "RAINED OFF", 1)]))
    @mock.patch('db.models.RaceParticipants.get_race_participants_race_id', MagicMock(return_value=[MockRaceParticipants(1,3,1)]))
    @mock.patch('db.models.RaceResult.get_race_result', MagicMock(return_value=MockRaceResults(1,1,400,False,1)))
    def test_results_authorized_status_code(self):
        with self.client as client:
            response = client.get("/auth/token")
            token = response.get_json()['token']
            headers = {'Authorization': token}
            response = client.get('/results', headers=headers)

            self.assertTrue(status.is_success(response.status_code))


    @mock.patch('db.models.Race.get_all_races', MagicMock(return_value=[MockRace(1, "2018-10-10 10:00:00", "RAINED OFF", 1)]))
    @mock.patch('db.models.RaceParticipants.get_race_participants_race_id', MagicMock(return_value=[MockRaceParticipants(1,3,1)]))
    @mock.patch('db.models.RaceResult.get_race_result', MagicMock(return_value=MockRaceResults(1,1,400,False,1)))
    def test_results_no_data_in_db_404(self):
        with self.client as client:
            response = client.get('/results/1')
            self.assertTrue(status.is_client_error(response.status_code))

    def test_results_unauthorized_body(self):
        with self.client as client:
            result = client.get('/results/1').get_json()
            expected_result = {
                'status': 'Failed',
                'message': 'Unauthorized'
            }
            self.assertEqual(result, expected_result)

    def test_results_unauthorised_status_code(self):
        with self.client as client:
            response = client.get('/results/1')
            self.assertTrue(status.is_client_error(response.status_code))
            

if __name__ == '__main__':
    unittest.main()