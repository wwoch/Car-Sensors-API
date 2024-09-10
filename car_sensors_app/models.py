from car_sensors_app import db
from marshmallow import Schema, fields, validate, validates, ValidationError
from car_sensors_app.utils import validate_tire_pressure

class SensorsData(db.Model):
    __tablename__ = 'sensor_data'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.String(16), nullable=False)  # Identyfikator samochodu
    temperature_engine = db.Column(db.Float)  # Temperatura silnika
    tire_pressure = db.Column(db.JSON)  # Ciśnienie w oponach
    fuel_level = db.Column(db.Float)  # Poziom paliwa

    def __repr__(self):
        return f'<Car_id {self.car_id}>' 

class SensorsSchema(Schema):
    id = fields.Integer(dump_only=True) # pominiecie walidacji
    car_id = fields.String(required=True, validate=validate.Length(equal=16))
    temperature_engine = fields.Float(required=True, validate=validate.Range(min=0, max=100))
    tire_pressure = fields.Dict(required=True, validate=validate_tire_pressure)
    fuel_level = fields.Float(required=True, validate=validate.Range(min=0, max=100))
