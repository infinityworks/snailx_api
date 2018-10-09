import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock

from endpoints.snails.snails import snails_endpoint


def mock_authenticate_request(return_value):
    return return_value

class MockSnail:
    def __init__(self, id, name, trainer_id):
        self.id = id
        self.name = name
        self.trainer_id = trainer_id


class MockTrainer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class TestEndpoints(TestCase):

    @mock.patch('endpoints.snails.snails.authenticate_request')
    @mock.patch('db.models.Snail.get_all_snails', MagicMock(return_value=[MockSnail(1, "Lil Terry", 1), MockSnail(2, "Lil Gazza", 1)]))
    @mock.patch('db.models.Trainer.get_trainer', MagicMock(return_value=MockTrainer(1, "Terry")))
    def test_snails_returns_snails(self, mock_auth_req):
        mock_auth_req.return_value = MagicMock(response=True)
        result = snails_endpoint()

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

    @mock.patch('endpoints.snails.snails.authenticate_request')
    @mock.patch('db.models.Snail.get_all_snails', MagicMock(return_value=None))
    def test_snails_returns_404(self, mock_auth_req):
        mock_auth_req.return_value = MagicMock(response=True)
        result = snails_endpoint()

        expected_result = 404

        self.assertEqual(result, expected_result)

    @mock.patch('endpoints.snails.snails.authenticate_request')
    @mock.patch('endpoints.snails.snails.unauthorised_response')
    def test_snails_unauthorized(self, mock_auth_req, mock_unauthorized):
        mock_auth_req.return_value = MagicMock(response=False)
        mock_unauthorized.reeturn_value = MagicMock(response={
            'status': 'Failed',
            'message': 'Unauthorized'
        })

        result = snails_endpoint()

        expected_result = {
            'status': 'Failed',
            'message': 'Unauthorized'
        }

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
