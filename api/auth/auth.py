from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

auth_blueprint = Blueprint('auth', __name__)