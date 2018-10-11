from flask_api import status
from auth.auth import Auth
from db.models import RaceResult, RaceParticipants
from flask import Blueprint
from globals.globals import app

single_result_endpoint_blueprint = Blueprint('single_result', __name__)


@single_result_endpoint_blueprint.route('/results/<id>')
def single_snail_endpoint(id):
    """GET end point to return single result information"""
    auth = Auth(app)

    if not auth.authenticate_request():
        return auth.unauthorized_response()

    race_participants = RaceParticipants()
    query_response = race_participants.get_race_participants_race_id(id)

    if query_response is not None:
        snails = []
        for row in query_response:
            race_result = RaceResult()
            query_response_race_result = race_result.get_race_result(query_response.id_race_participants)

            snails.append({
                "id_snail": row.snail_id,
                "position_snail": query_response_race_result.position,
                "time_snail": query_response_race_result.time_to_finish,
                "DNF": query_response_race_result.did_not_finish
            })

        return {
            "id_race": id,
            "snails": snails
        }

    return {
            'status': 'Failed',
            'message': 'Results not found'
        }, status.HTTP_404_NOT_FOUND
