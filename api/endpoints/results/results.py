from flask_api import status

from auth.auth import Auth
from db.models import RaceResult, RaceParticipants, Race
from flask import Blueprint
from globals.globals import app

results_endpoint_blueprint = Blueprint('results', __name__)

@results_endpoint_blueprint.route('/results')
def results_endpoint():
    """GET end point to return races information"""

    auth = Auth(app)
    if not auth.authenticate_request():
        return auth.unauthorized_response()

    race = Race()
    race_participants = RaceParticipants()
    race_results = RaceResult()
<<<<<<< HEAD

    race_query = race.get_all_races()
    
    if race_query:
        json = []

        for each_race in race_query:
            race_id = each_race.id
            snails_results_list = []
            race_participants_by_id = race_participants.get_race_participants_race_id(race_id)
            print("Printing race participants by id:\n\n {}\n\n".format(race_participants_by_id))
            for row in race_participants_by_id:
                race_results_snail = race_results.get_race_result(row.id)
                print("Printing row: \n\n {}\n\n".format(row))
                print("Printing race_results_snail: \n\n {}\n\n".format(race_results_snail))
                print("Next row below...")
                snails_results_list.append({"id_snail": row.id_snail, "position_snail": race_results_snail.position, "time_snail": race_results_snail.time_to_finish, "DNF": race_results_snail.did_not_finish})

            json.append({
                "id_race": race_id,
                "snails": snails_results_list
            })
        return json

    return {
            'status': 'Failed',
            'message': 'Races not found'
        }, status.HTTP_404_NOT_FOUND

=======

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
>>>>>>> b639eaef41bc214f0b7856faca625824a2a8eb10
