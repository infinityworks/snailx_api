from flask_api import status
from auth.auth import Auth
from db.models import RaceResult
from flask import Blueprint
from globals.globals import app

results_endpoint_blueprint = Blueprint('results', __name__)


@results_endpoint_blueprint.route('/races/results')
def results_all():
    """GET end point to return results"""

    auth = Auth(app)
    if not auth.authenticate_request():
        return auth.unauthorized_response()

    return results_json(results_from_db())


def results_json(query_response):

    print("QUERY!! " + str(query_response))

    array = []

    for query in query_response:

        if query.did_not_finish == 'False':
            dnf = False
        if query.did_not_finish == 'True':
            dnf = True
        if query.did_not_finish == '':
            dnf = False

        json = {
            "id_snail": query.id,
            "position_snail": query.position,
            "time_snail": query.time_to_finish,
            "DNF": dnf
        }

        array.append(json)

    return array


def results_from_db():
    result = RaceResult()
    query_response = result.get_all_race_results()

    return query_response



    # return {
    #     "id_race": 1,
    #     "snails": [
    #         {"id_snail": 1, "position_snail:": 3, "time_snail": 600, "DNF": False},
    #         {"id_snail": 2, "position_snail:": 2, "time_snail": 500, "DNF": False},
    #         {"id_snail": 3, "position_snail:": 1, "time_snail": 400, "DNF": False}
    #     ]
    # }