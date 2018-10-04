from globals.globals import app
from db.models import Snail

@app.route("/")
def hello():
    return {"Hello": "World!"}


@app.route('/snails')
def snails():
    """GET end point to return snails information"""
    snail = Snail()

    #snail.add_new_snail(1, 13, "Terry")

    query_response = snail.get_snail(1)

    if query_response:
        json = {
            "id": query_response.id,
            "name": query_response.name,
            "age": query_response.age,
            "id_trainer": 15

        }

        return json

    return False # TODO RETURN 404 ERROR CODE


@app.route('/races')
def race():
    """GET end point to return race information"""
    return {
        "id": 1,
        "date": "15:8:2018",
        "status": "played",
        "id_round": 1,
        "id_race_participants": 1
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


@app.route('/results')
def results():
    """GET end point to return results"""
    return {
        "id_race": 1,
        "id_snail": 1,
        "position": 1,
        "time": "400",
        "DNF": False
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
