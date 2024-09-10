from flask import request
from werkzeug.exceptions import UnsupportedMediaType
from functools import wraps
from marshmallow import ValidationError

def validate_json_content_type(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            raise UnsupportedMediaType('Content type must be application/json')
        return func(*args, **kwargs)
    return wrapper

def validate_tire_pressure(tire_pressure):
    if len(tire_pressure) != 4:
        raise ValidationError("Tire pressure must have 4 entries.")
    for key, value in tire_pressure.items():
        if not isinstance(value, float):
            raise ValidationError(f"Pressure value for {key} must be a float.")
        if not (0.0 <= value <= 5.0):
            raise ValidationError(f"Pressure value for {key} must be between 0.0 and 5.0 bar.")
