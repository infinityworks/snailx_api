import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock

from globals.globals import app
from flask_api import status

from endpoints.results.results import results_endpoint

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

    @mock.patch('db.models.Race.get_all_races', MagicMock(return_value=
                                                            [MockRace(1, "2018-10-10 10:00:00", "RAINED OFF", 1)]))
    @mock.patch('db.models.RaceParticipants.get_race_participants_race_id', MagicMock(return_value=[
                                                                                        MockRaceParticipants(1, 1, 1), 
                                                                                        MockRaceParticipants(2, 2, 1), 
                                                                                        MockRaceParticipants(3,3,1)
                                                                                        ]))
    @mock.patch('db.models.RaceResult.get_race_result', MagicMock(return_value=[
                                                                    MockRaceResults(1,3,600,False,1), 
                                                                    MockRaceResults(2,2,500,False,2), 
                                                                    MockRaceResults(3,1,400,False,3)
                                                                    ]))
    def test_results_authorized_body(self):

        with self.client as client:
            response = client.get("/auth/token")
            token = response.get_json()['token']
            headers = {'Authorization': token}
        
        result = client.get('/results', headers=headers).get_json()
        expected_result =[{
                "id_race": 1,
                "snails": [
                    {"id_snail": 1, "position_snail:": 3, "time_snail": 600, "DNF": False},
                    {"id_snail": 2, "position_snail:": 2, "time_snail": 500, "DNF": False},
                    {"id_snail": 3, "position_snail:": 1, "time_snail": 400, "DNF": False}
                ]
            }]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
