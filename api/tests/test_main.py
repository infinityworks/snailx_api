from unittest import TestCase
from unittest.mock import patch
from db.models import Snail
import main


class MockSnail:
    def __init__(self, id, name, trainer_id, trainer_name):
        self.id = id
        self.name = name
        self.trainer_id = trainer_id
        self.trainer_name = trainer_name


class TestEndpoints(TestCase):

    def test_races_returns_races(self):
        result = main.races()

        expected_result = {
            "id": 1,
            "date": "15:8:2018",
            "status": 3,
            "id_round": 1,
            "id_snails": [1, 2, 3, 4, 5]
        }

        self.assertEqual(result, expected_result)

    def test_rounds_returns_rounds(self):
        result = main.rounds()

        expected_result = {
            "id": 1,
            "name": "",
            "num_races": 5,
            "start_date": "15:9:2018",
            "end_date": "15:10:2018"
        }

        self.assertEqual(result, expected_result)

    def test_results_returns_results(self):
        result = main.results()

        expected_result = {
            "id_race": 1,
            "snails": [
                {"id_snail": 1, "position_snail:": 3,
                    "time_snail": 600, "DNF": False},
                {"id_snail": 2, "position_snail:": 2,
                    "time_snail": 500, "DNF": False},
                {"id_snail": 3, "position_snail:": 1,
                    "time_snail": 400, "DNF": False},
            ]
        }

        self.assertEqual(result, expected_result)
