from flask_api import status
from auth.auth import authenticate_request, unauthorised_response
from db.models import Snail, Trainer
from flask import Blueprint

snails_endpoint_blueprint = Blueprint('snailshw', __name__)


@snails_endpoint_blueprint.route('/snailshw')
def snails_endpoint():
    """GET end point to return snails information"""

    if not authenticate_request():
        return unauthorised_response()

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
