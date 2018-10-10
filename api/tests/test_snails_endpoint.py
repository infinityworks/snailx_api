import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock

from globals.globals import app
from flask_api import status

from endpoints.snails.snails import snails_endpoint


class MockSnail:
    def __init__(self, id, name, trainer_id):
        self.id = id
        self.name = name
        self.trainer_id = trainer_id


class MockTrainer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class TestSnailsEndpoint(TestCase):

    def setUp(self):
        self.client = app.test_client()

    @mock.patch('db.models.Snail.get_all_snails', MagicMock(return_value=[MockSnail(1, "Lil Terry", 1), MockSnail(2, "Lil Gazza", 1)]))
    @mock.patch('db.models.Trainer.get_trainer', MagicMock(return_value=MockTrainer(1, "Terry")))
    def test_snails_authorized_body(self):

        with self.client as client:
            response = client.get("/auth/token")
            token = response.get_json()['token']
            headers = {'Authorization': token}

            result = client.get('/snails', headers=headers).get_json()
            expected_result = [
                {
                    "id": 1,
                    "name": "Lil Terry",
                    "trainer": {
                        "id": 1,
                        "name": "Terry"
                    }
                },
                {
                    "id": 2,
                    "name": "Lil Gazza",
                    "trainer": {
                        "id": 1,
                        "name": "Terry"
                    }
                }
            ]
            self.assertEqual(result, expected_result)

    @mock.patch('db.models.Snail.get_all_snails', MagicMock(return_value=[MockSnail(1, "Lil Terry", 1), MockSnail(2, "Lil Gazza", 1)]))
    @mock.patch('db.models.Trainer.get_trainer', MagicMock(return_value=MockTrainer(1, "Terry")))
    def test_snails_authorized_status_code(self):
        with self.client as client:
            response = client.get("/auth/token")
            token = response.get_json()['token']
            headers = {'Authorization': token}
            response = client.get('/snails', headers=headers)

            self.assertTrue(status.is_success(response.status_code))

    @mock.patch('db.models.Snail.get_all_snails', MagicMock(return_value=None))
    def test_snails_no_data_in_db_404(self):
        with self.client as client:
            response = client.get('/snails')
            self.assertTrue(status.is_client_error(response.status_code))

    def test_snails_unauthorized_body(self):
        with self.client as client:
            result = client.get('/snails').get_json()
            expected_result = {
                'status': 'Failed',
                'message': 'Unauthorized'
            }
            self.assertEqual(result, expected_result)

    def test_snails_unauthorised_status_code(self):
        with self.client as client:
            response = client.get('/snails')
            self.assertTrue(status.is_client_error(response.status_code))


if __name__ == '__main__':
    unittest.main()
