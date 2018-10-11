from flask_api import status
from auth.auth import Auth
from db.models import Round, Race
from flask import Blueprint
from globals.globals import app

single_round_endpoint_blueprint = Blueprint('single_round', __name__)


@single_round_endpoint_blueprint.route('/rounds/<id>')
def snails_endpoint(id):
    """Endpoint to get information for a round with specified id.

    Retrieves the round information in json format for the specified id.

    Args:
        id (int): The id of the requested round.

    Returns:
        JSON: The json representation of the round with specified id.
    """

    auth = Auth(app)
    if not auth.authenticate_request():
        return auth.unauthorized_response()

    round_model = Round()
    query_response = round_model.get_round(id)

    if query_response:
        json = []

        race_model = Race()
        race_ids = race_model.get_round_race_ids(query_response.id)

        json.append(
            {
                "id": query_response.id,
                "name": query_response.name,
                "start_date": query_response.start_date,
                "end_date": query_response.end_date,
                "races": race_ids
            }
        )
        return json

    return {
        'status': 'Failed',
        'message': 'Rounds not found'
    }, status.HTTP_404_NOT_FOUND
