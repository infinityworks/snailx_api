from auth.auth import Auth
from db.models import RaceResult, RaceParticipants
from flask import Blueprint
from globals.globals import app

results_endpoint_blueprint = Blueprint('results', __name__)


@results_endpoint_blueprint.route('/results/')
def results_all():
    """GET end point to return results"""

    auth = Auth(app)
    if not auth.authenticate_request():
        return auth.unauthorized_response()

    return results_json(results_from_db())


def results_json(results_query_response):


    base_json = []

    for results_query in results_query_response:

        race_participants = RaceParticipants()
        response_race_participants = race_participants.get_race_participants_race_id(results_query.id_race_participants)

        json = []
        for participants in response_race_participants:
            race_results = RaceResult()
            response_race_results = race_results.get_race_result(participants.id)

            json.append({
                "id_snail": participants.id_snail,
                "position_snail": response_race_results.position,
                "time_snail": response_race_results.time_to_finish,
                "DNF": response_race_results.did_not_finish
            })

        base_json.append({"id_race": participants.id_race, "snails": json})

    return base_json


def results_from_db():
    result = RaceResult()
    results_query_response = result.get_all_race_results()

    return results_query_response


# return {
#     "id_race": 1,
#     "snails": [
#         {"id_snail": 1, "position_snail:": 3, "time_snail": 600, "DNF": False},
#         {"id_snail": 2, "position_snail:": 2, "time_snail": 500, "DNF": False},
#         {"id_snail": 3, "position_snail:": 1, "time_snail": 400, "DNF": False}
#     ]
# }