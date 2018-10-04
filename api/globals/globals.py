from flask_api import FlaskAPI
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
from auth.auth import auth_blueprint

app = FlaskAPI(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#app components
app.register_blueprint(auth_blueprint)