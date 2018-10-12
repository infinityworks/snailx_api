from flask_api import status

from auth.auth import Auth
from db.models import RaceResult, RaceParticipants, Race
from flask import Blueprint
from globals.globals import app

single_result_endpoint_blueprint = Blueprint('single_result', __name__)


@single_result_endpoint_blueprint.route('/results/<id>')
def results_endpoint(id):
    """GET end point to return single result information"""

    auth = Auth(app)
    if not auth.authenticate_request():
        return auth.unauthorized_response()

    return single_result_json(id)


class ResultRace:

    def __init__(self, id):
        self.id = id
        self.snails = []
        self.json = []

    def get_json(self):
        return {'id_race': self.id,
                'snails': [snail.get_json() for snail in self.snails]}


class ResultSnail:

    def __init__(self, id, pos, time, dnf):
        self.id = id
        self.pos = pos
        self.time = time
        self.dnf = dnf

    def get_json(self):
        return {
            "id_snail": self.id,
            "position_snail": self.pos,
            "time_snail": self.time,
            "DNF": self.dnf
        }


def single_result_json(id):
    race = Race()
    race_participants = RaceParticipants()
    race_results = RaceResult()

    race_query = race.get_race(id)
    
    if race_query:
        json = []
        snails_results_list = []
        race_participants_by_id = race_participants.get_race_participants_race_id(id)
        print(race_participants_by_id)
        for row in race_participants_by_id:
            race_results_snail = race_results.get_race_result(row.id)
            snails_results_list.append({"id_snail": row.id_snail, "position_snail": race_results_snail.position, "time_snail": race_results_snail.time_to_finish, "DNF": race_results_snail.did_not_finish})

        json.append({
            "id_race": id,
            "snails": snails_results_list
            })
        return json

    return {
            'status': 'Failed',
            'message': 'Races not found'
        }, status.HTTP_404_NOT_FOUND
