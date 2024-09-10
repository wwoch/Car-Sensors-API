import json
from pathlib import Path
from car_sensors_app import db
from car_sensors_app.models import SensorsData
from car_sensors_app.commands import db_manage_bp
import click
from sqlalchemy.sql import text

@db_manage_bp.cli.group()
def db_manage():
    """Database management commands."""
    pass

@db_manage.command()
def add_data():
    """Add sample data to the database."""
    try:
        cars_sensors_path = Path(__file__).parent.parent.parent / 'samples' / 'cars_sensors_data.json'
        with open(cars_sensors_path) as file:
            data_json = json.load(file)
        for item in data_json:
            car = SensorsData(**item)
            db.session.add(car)
        db.session.commit()
        print('Data has been successfully added to database')
    except Exception as exc:
        print(f"Unexpected error: {exc}")

@db_manage.command()
def remove_data():
    """Remove all data from the database."""
    try:
        db.session.execute(text('TRUNCATE TABLE sensor_data RESTART IDENTITY'))
        db.session.commit()
        print('Data has been successfully remove from database')
    except Exception as exc:
        print(f"Unexpected error: {exc}")
