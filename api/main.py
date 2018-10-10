import sys
sys.path.insert(0, '/vagrant/repos/snailx_api/api')
from globals.globals import app
from db.models import Snail, Trainer, Race, RaceParticipants
from auth.auth import authenticate_request, unauthorised_response
from flask_api import status


# @app.route('/races')
# def races():
#     """GET end point to return race information"""

#     if not authenticate_request():
#        return unauthorised_response()

#     race = Race()
#     race_query = race.get_race(1)
#     # Get the results of RaceParticipants.race_id == race_query.id
#     all_race_participants = RaceParticipants()
#     race_participants = all_race_participants.get_race_participants_race_id(race_query.id)

#     if race_query:
#         # creates a list to be populated by the snail ids in the race being queried.
#         snails_id_list = []
#         # loops over the race participants with the current race id
#         for row in race_participants:
#             snails_id_list.append(row.id_snail)
#         json = {
#             "id": race_query.id,
#             "date": race_query.date,
#             "status": race_query.status,
#             "id_round": race_query.id_round,
#             # TODO iterate over snails
#             "id_snails": snails_id_list
#     }
#         return json

#     return 404


@app.route('/rounds')
def rounds():
    """GET end point to return round information"""
    return {
        "id": 1,
        "name": "",
        "num_races": 5,
        "start_date": "15:9:2018",
        "end_date": "15:10:2018"
    }


@app.route('/races/results')
def results():
    """GET end point to return results"""
    return {
        "id_race": 1,
        "snails": [
            {"id_snail": 1, "position_snail:": 3, "time_snail": 600, "DNF": False},
            {"id_snail": 2, "position_snail:": 2, "time_snail": 500, "DNF": False},
            {"id_snail": 3, "position_snail:": 1, "time_snail": 400, "DNF": False},
        ]
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
