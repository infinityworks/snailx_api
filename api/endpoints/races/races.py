from flask_api import status
from auth.auth import Auth
from db.models import Race, RaceParticipants
from globals.globals import app
from flask import Blueprint

races_endpoint_blueprint = Blueprint('races', __name__)


@races_endpoint_blueprint.route('/races')
def races_endpoint():
    """GET end point to return races information"""

    auth = Auth(app)
    if not auth.authenticate_request():
        return auth.unauthorized_response()

    race = Race()
    race_query = race.get_all_races()
    all_race_participants = RaceParticipants()

    if race_query:
        json = []

        for each_race in race_query:
            race_participants = all_race_participants.get_race_participants_race_id(each_race.id)
            snails_id_list = []

            for row in race_participants:
                snails_id_list.append(row.id_snail)

            json.append({
                "id": each_race.id,
                "date": each_race.date,
                "status": each_race.status,
                "id_round": each_race.id_round,
                "id_snails": snails_id_list
            })
        return json

    return {
            'status': 'Failed',
            'message': 'Races not found'
        }, status.HTTP_404_NOT_FOUND
