from flask_api import status
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

        print(results_query.id_race_participants)
        race_participants_from_id = race_participants_from_db(results_query.id_race_participants)

        json = {
            "id_snail": race_participants_from_id.id_snail,
            "position_snail": results_query.position,
            "time_snail": results_query.time_to_finish,
            "DNF": results_query.did_not_finish
        }

        base_json.append({"id_race": race_participants_from_id.id_race, "snails": json})

    return base_json


def results_from_db():
    result = RaceResult()
    results_query_response = result.get_all_race_results()

    return results_query_response

def race_participants_from_db(id):
    race_participants_from_id = RaceParticipants().get_race_participants(id)
    print(race_participants_from_id)

    return race_participants_from_id

    # return {
    #     "id_race": 1,
    #     "snails": [
    #         {"id_snail": 1, "position_snail:": 3, "time_snail": 600, "DNF": False},
    #         {"id_snail": 2, "position_snail:": 2, "time_snail": 500, "DNF": False},
    #         {"id_snail": 3, "position_snail:": 1, "time_snail": 400, "DNF": False}
    #     ]
    # }