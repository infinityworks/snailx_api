from flask_api import status
from auth.auth import Auth
from db.models import Round
from flask import Blueprint
from globals.globals import app

rounds_endpoint_blueprint = Blueprint('rounds', __name__)


@rounds_endpoint_blueprint.route('/rounds')
def snails_endpoint():
    """GET end point to return rounds information"""

    auth = Auth(app)
    if not auth.authenticate_request():
        return auth.unauthorized_response()

    round_model = Round()
    query_response = round_model.get_all_rounds()

    if query_response:
        json = []
        for row in query_response:
            json.append(
                {
                    "id": row.id,
                    "name": row.name,
                    "start_date": row.start_date
                }
            )
        return json

    return {
        'status': 'Failed',
        'message': 'Rounds not found'
    }, status.HTTP_404_NOT_FOUND
