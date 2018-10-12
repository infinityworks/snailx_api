from flask_api import status

from auth.auth import Auth
from db.models import RaceResult, RaceParticipants, Race
from flask import Blueprint
from globals.globals import app

results_endpoint_blueprint = Blueprint('results', __name__)


@results_endpoint_blueprint.route('/results')
def results_endpoint():
    """GET end point to return races information"""

    auth = Auth(app)
    if not auth.authenticate_request():
        return auth.unauthorized_response()

    return results_json()


class ResultRace:

    def __init__(self, id):
        self.id = id
        self.snails = []
        self.json = []

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_json(self):
        return {'id_race': self.id,
                'snails': [snail.get_json() for snail in self.snails]}


class ResultSnail:

    def __init__(self, id, pos, time, dnf):
        self.id = id
        self.pos = pos
        self.time = time
        self.dnf = dnf

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_json(self):
        return {
            "id_snail": self.id,
            "position_snail": self.pos,
            "time_snail": self.time,
            "DNF": self.dnf
        }


def results_json():
    race_participants = RaceParticipants()
    race_results = race_participants.get_race_results()

    races = {}
    if race_results:
        for (race_participant, race_result) in race_results:

            snail = ResultSnail(race_participant.id_snail,
                                race_result.position,
                                race_result.time_to_finish,
                                race_result.did_not_finish)

            if race_participant.id_race not in races.keys():
                races[race_participant.id_race] = ResultRace(
                    race_participant.id_race)

            race = races[race_participant.id_race]
            if snail not in race.snails:
                race.snails.append(snail)

        return [race.get_json() for race in races.values()]

    return {
        'status': 'Failed',
        'message': 'Results not found'
    }, status.HTTP_404_NOT_FOUND
