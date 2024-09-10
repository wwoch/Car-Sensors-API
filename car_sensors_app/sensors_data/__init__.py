from flask import Blueprint

sensors_bp = Blueprint('sensors', __name__)
from car_sensors_app.sensors_data import sensors_data