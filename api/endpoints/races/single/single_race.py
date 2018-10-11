from flask_api import status
from auth.auth import Auth
from db.models import Snail, Trainer, Race, RaceParticipants
from globals.globals import app
from flask import Blueprint

single_race_endpoint_blueprint = Blueprint('single_race', __name__)


@single_race_endpoint_blueprint.route('/races/<id>')
def single_race_endpoint(id):
    """GET end point to return a single race's information"""

    auth = Auth(app)
    if not auth.authenticate_request():
        return auth.unauthorized_response()

    race = Race()
    single_race_query = race.get_race(id)

    single_race_participants = RaceParticipants().get_race_participants_race_id(id)

    if single_race_query:
        json = []

        snails_id_list = []
        for row in single_race_participants:
            snails_id_list.append(row.id_snail)

        json.append({
            "id": single_race_query.id,
            "date": single_race_query.date,
            "status": single_race_query.status,
            "id_round": single_race_query.id_round,
            "id_snails": snails_id_list
        })
        return json
        
    return {
            'status': 'Failed',
            'message': 'Snail not found'
        }, status.HTTP_404_NOT_FOUND