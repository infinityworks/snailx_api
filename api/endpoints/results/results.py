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

    all_races = race_results.get_all_race_results()

    all_json = []
    if all_races:
        for race in all_races:
            all_race_participants = race_participants.get_race_participants_race_id(race.id)
            snail_json = []

            for participant in all_race_participants:
                print(participant)
                result = race_results.get_race_result(participant.id)
                snail_json.append(
                    {
                        "id_snail": participant.id_snail,
                        "position_snail": result.position,
                        "time_snail": result.time_to_finish,
                        "DNF": result.did_not_finish
                    }
                )

            all_json.append(
                    {"id_race": race.id,
                    "snails": snail_json}
            )


        return all_json

    return {'status': 'Failed',
            'message': 'Results not found'
            }, status.HTTP_404_NOT_FOUND


"""
{
    "id_race": 1,
    "snails": [
        {"id_snail": 1, "position_snail:": 3, "time_snail": 600, "DNF": False},
        {"id_snail": 2, "position_snail:": 2, "time_snail": 500, "DNF": False},
        {"id_snail": 3, "position_snail:": 1, "time_snail": 400, "DNF": False},
    ]
}
"""

"""
{
    "id_race": 1,
    "snails": [
        {"id_snail": 1, "position_snail": 1, "time_snail": 5000,"DNF": "false"}
    ]
},
"""