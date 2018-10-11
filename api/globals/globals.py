from flask_api import FlaskAPI
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
import os


app = FlaskAPI(__name__)
app.config.from_object(Config)
SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from endpoints.auth.auth import auth_endpoint_blueprint
from endpoints.snails.snails import snails_endpoint_blueprint
from endpoints.races.races import races_endpoint_blueprint
from endpoints.snails.single.single_snail import single_snail_endpoint_blueprint
from endpoints.results.results import results_endpoint_blueprint

app.register_blueprint(auth_endpoint_blueprint)
app.register_blueprint(snails_endpoint_blueprint)
app.register_blueprint(single_snail_endpoint_blueprint)
app.register_blueprint(races_endpoint_blueprint)
app.register_blueprint(results_endpoint_blueprint)
