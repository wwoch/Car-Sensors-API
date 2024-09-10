from flask import Blueprint

errors_bp = Blueprint('errors', __name__)

from car_sensors_app.errors import errors