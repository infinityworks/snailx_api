from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route("/")
def hello():
    return {"Hello": "World!"}


@app.route('/snails')
def snails():
    """GET end point to return snails information"""
    return {
        "id": 1,
        "name": "Terry",
        "id_trainer": 1,
        "age": 23
    }


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
