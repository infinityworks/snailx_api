from flask_api import status
from auth.auth import Auth
from db.models import Snail, Trainer
from flask import Blueprint
from globals.globals import app

snails_endpoint_blueprint = Blueprint('snails', __name__)


@snails_endpoint_blueprint.route('/snails')
def snails_endpoint():
    """GET end point to return snails information"""

    auth = Auth(app)
    if not auth.authenticate_request():
        return auth.unauthorised_response()

    snail = Snail()
    query_response = snail.get_all_snails()

    if query_response:
        trainer = Trainer()
        json = []
        for row in query_response:
            query_response_trainer = trainer.get_trainer(row.trainer_id)
            json.append({
                "id": row.id,
                "name": row.name,
                "trainer": {
                    "id": query_response_trainer.id,
                    "name": query_response_trainer.name
                }
            })

        return json

    return status.HTTP_404_NOT_FOUND
