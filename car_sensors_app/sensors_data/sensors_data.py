from flask import Blueprint, jsonify, request
from webargs.flaskparser import use_args
from car_sensors_app.models import SensorsData, SensorsSchema, db
from car_sensors_app.utils import validate_json_content_type 
from car_sensors_app.sensors_data import sensors_bp

@sensors_bp.route('/cars', methods=['GET'])
def get_cars_data():
    cars = SensorsData.query.all()
    car_schema = SensorsSchema(many=True)
    return jsonify({
        'success': True,
        'data': car_schema.dump(cars),
        'number_of_records': len(cars)
    })

@sensors_bp.route('/cars/<string:car_id>', methods=['GET'])
def get_car_data(car_id: str):
    car = SensorsData.query.filter_by(car_id=car_id).first_or_404(description=f"Car with VIN {car_id} not found")
    return jsonify({
        'success': True,
        'data': SensorsSchema().dump(car)
    })

@sensors_bp.route('/cars', methods=['POST'])
@validate_json_content_type
@use_args(SensorsSchema, error_status_code=400)
def add_car_data(args: dict):
    car = SensorsData(**args)

    db.session.add(car)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': SensorsSchema().dump(car)
    }), 201

@sensors_bp.route('/cars/<string:car_id>', methods=['PUT'])
@validate_json_content_type
@use_args(SensorsSchema, error_status_code=400)
def update_car_data(args: dict, car_id: str):
    car = SensorsData.query.filter_by(car_id=car_id).first_or_404(description=f"Car with VIN {car_id} not found")
    car.car_id = args['car_id']
    car.temperature_engine = args['temperature_engine']
    car.tire_pressure = args['tire_pressure']
    car.fuel_level = args['fuel_level']

    db.session.flush()
    db.session.commit()

    return jsonify({
        'success': True,
        'data': SensorsSchema().dump(car)
    })

@sensors_bp.route('/cars/<string:car_id>', methods=['DELETE'])
def delete_car_data(car_id: str):
    car = SensorsData.query.filter_by(car_id=car_id).first_or_404(description=f"Car with VIN {car_id} not found")
    
    try:    
        db.session.delete(car)    
        db.session.commit()
    except Exception as exc:    
        db.session.rollback()    
        print(f"Error deleting car data: {exc}")

    return jsonify({
        'success': True,
        'data': f'Car with id {car_id} has been deleted'
    })
