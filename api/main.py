from globals.globals import app
from db.models import Snail


@app.route('/snails')
def snails():
    """GET end point to return snails information"""
    snail = Snail()
    query_response = snail.get_snail(1)

    if query_response:
        json = {
            "id": query_response.id,
            "name": query_response.name,
            "age": query_response.age,
            "trainer": {
                "id": 17,
                "name": "gazza"
            }
        }

        return json

    return False  # TODO RETURN 404 ERROR CODE


@app.route('/races')
def races():
    """GET end point to return race information"""
    return {
        "id": 1,
        "date": "15:8:2018",
        "status": 3,
        "id_round": 1,
        "id_snails": [1, 2, 3, 4, 5]
    }


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
