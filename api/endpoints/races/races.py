from flask_api import status
from auth.auth import authenticate_request, unauthorised_response
from db.models import Snail, Trainer, Race, RaceParticipants
from flask import Blueprint

races_endpoint_blueprint = Blueprint('races', __name__)


@races_endpoint_blueprint.route('/races')
def races_endpoint():
    """GET end point to return races information"""

    if not authenticate_request():
       return unauthorised_response()

    race = Race()
    race_query = race.get_all_races()

    # Get the results of RaceParticipants.race_id == race_query.id
    all_race_participants = RaceParticipants()
    #print(race_query)

    if race_query:
        json = []

        for each_race in race_query:
        # creates a list to be populated by the snail ids in the race being queried.
            race_participants = all_race_participants.get_race_participants_race_id(each_race.id)
            snails_id_list = []

            # loops over the race participants with the current race id
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

    return status.HTTP_404_NOT_FOUND