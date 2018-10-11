from flask_api import status
from auth.auth import Auth
from db.models import Snail, Trainer
from flask import Blueprint
from globals.globals import app

single_snail_endpoint_blueprint = Blueprint('single_snail', __name__)


@single_snail_endpoint_blueprint.route('/snails/<id>')
def single_snail_endpoint(id):
    """GET end point to return single snail information"""
    auth = Auth(app)

    if not auth.authenticate_request():
        return auth.unauthorized_response()

    snail = Snail()
    query_response = snail.get_snail(id)

    if query_response:
        trainer = Trainer()

        query_response_trainer = trainer.get_trainer(query_response.trainer_id)

        return {
                "id": query_response.id,
                "name": query_response.name,
                "trainer": {
                    "id": query_response_trainer.id,
                    "name": query_response_trainer.name
                }
            }

    return status.HTTP_404_NOT_FOUND
