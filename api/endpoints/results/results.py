from flask_api import status

from auth.auth import Auth
from db.models import RaceResult, RaceParticipants
from flask import Blueprint
from globals.globals import app

results_endpoint_blueprint = Blueprint('results', __name__)


@results_endpoint_blueprint.route('/results')
def results_all():
    """GET end point to return results"""

    auth = Auth(app)
    if not auth.authenticate_request():
        return auth.unauthorized_response()

    return results_json()


def results_json():
    race_participants = RaceParticipants()
    race_results = RaceResult()
    all_race_results = race_results.get_all_race_results()
    json = []

    if race_results:
        for result in all_race_results:
            response_race_participants = race_participants.get_race_participants_by_id(result.id_race_participants)
            participants_json = get_participants_json(response_race_participants, race_results)
            json.append({"id_race": response_race_participants[0].id_race, "snails": participants_json})

        return json

    return {
            'status': 'Failed',
            'message': 'Results not found'
        }, status.HTTP_404_NOT_FOUND


def get_participants_json(race_participants, race_results):
    participants_json = []
    for participants in race_participants:
        response_race_results = race_results.get_race_result(participants.id)

        participants_json.append({
            "id_snail": participants.id_snail,
            "position_snail": response_race_results.position,
            "time_snail": response_race_results.time_to_finish,
            "DNF": response_race_results.did_not_finish
        })

    return participants_json
