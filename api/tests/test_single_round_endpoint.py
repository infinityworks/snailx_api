from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock

from globals.globals import app
from flask_api import status


class MockRound:
    def __init__(self, id, name, start_date, end_date):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date


def get_round_ids_side_effect(*id_round):
    if id_round[0] == 1:
        return [1, 2, 3]


class TestSingleRoundEndpoint(TestCase):
    def setUp(self):
        self.client = app.test_client()

    @mock.patch('db.models.Race.get_round_race_ids',
                MagicMock(side_effect=get_round_ids_side_effect))
    @mock.patch('db.models.Round.get_round',
                MagicMock(return_value=MockRound(1,
                                                 "External",
                                                 "Mon, 01 Oct 2018 10:00:00 GMT",
                                                 "Mon, 01 Oct 2018 12:00:00 GMT")))
    def test_single_round_authorized_body(self):
        with self.client as client:
            response = client.get("/auth/token")
            token = response.get_json()['token']
            headers = {'Authorization': token}

            result = client.get('rounds/1', headers=headers).get_json()
            expected_result = {
                "id": 1,
                "name": "External",
                "start_date": "Mon, 01 Oct 2018 10:00:00 GMT",
                "end_date": "Mon, 01 Oct 2018 12:00:00 GMT",
                "races": [1, 2, 3]
            }
            self.assertEqual(result, expected_result)

    @mock.patch('db.models.Race.get_round_race_ids',
                MagicMock(side_effect=get_round_ids_side_effect))
    @mock.patch('db.models.Round.get_round',
                MagicMock(return_value=MockRound(1,
                                                 "External",
                                                 "Mon, 01 Oct 2018 10:00:00 GMT",
                                                 "Mon, 01 Oct 2018 12:00:00 GMT")))
    def test_single_round_authorized_status_code(self):
        with self.client as client:
            response = client.get("/auth/token")
            token = response.get_json()['token']
            headers = {'Authorization': token}
            response = client.get('/rounds/1', headers=headers)

            self.assertTrue(status.is_success(response.status_code))

    @mock.patch('db.models.Race.get_round_race_ids',
                MagicMock(side_effect=get_round_ids_side_effect))
    @mock.patch('db.models.Round.get_round',
                MagicMock(return_value=MockRound(1,
                                                 "External",
                                                 "Mon, 01 Oct 2018 10:00:00 GMT",
                                                 "Mon, 01 Oct 2018 12:00:00 GMT")))
    def test_single_round_no_data_in_db_404(self):
        with self.client as client:
            response = client.get('/rounds/1')
            self.assertTrue(status.is_client_error(response.status_code))

    def test_single_round_unauthorized_body(self):
        with self.client as client:
            result = client.get('/rounds/1').get_json()
            expected_result = {
                'status': 'Failed',
                'message': 'Unauthorized'
            }
            self.assertEqual(result, expected_result)

    def test_single_round_unauthorised_status_code(self):
        with self.client as client:
            response = client.get('/rounds/1')
            self.assertTrue(status.is_client_error(response.status_code))
