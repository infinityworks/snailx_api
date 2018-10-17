from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
import os


app = FlaskAPI(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print("############# CURRENT CONFIG: " +
      os.environ['APP_SETTINGS'] + " #############")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from endpoints.auth.auth import auth_endpoint_blueprint
from endpoints.snails.snails import snails_endpoint_blueprint
from endpoints.races.races import races_endpoint_blueprint
from endpoints.races.single.single_race import single_race_endpoint_blueprint
from endpoints.snails.single.single_snail import single_snail_endpoint_blueprint
from endpoints.results.results import results_endpoint_blueprint
from endpoints.rounds.rounds import rounds_endpoint_blueprint
from endpoints.rounds.single.single_round import single_round_endpoint_blueprint
from endpoints.results.single.single_result import single_result_endpoint_blueprint


app.register_blueprint(auth_endpoint_blueprint)
app.register_blueprint(snails_endpoint_blueprint)
app.register_blueprint(single_snail_endpoint_blueprint)
app.register_blueprint(races_endpoint_blueprint)
app.register_blueprint(results_endpoint_blueprint)
app.register_blueprint(single_race_endpoint_blueprint)
app.register_blueprint(rounds_endpoint_blueprint)
app.register_blueprint(single_round_endpoint_blueprint)
app.register_blueprint(single_result_endpoint_blueprint)
