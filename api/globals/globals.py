from flask_api import FlaskAPI
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
from auth.auth import auth_blueprint
import os


app = FlaskAPI(__name__)
app.config.from_object(Config)
SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from endpoints.snails.snails import snails_endpoint_blueprint


app.register_blueprint(auth_blueprint)
app.register_blueprint(snails_endpoint_blueprint)