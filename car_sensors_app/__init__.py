from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def build_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from car_sensors_app.sensors_data import sensors_bp
    app.register_blueprint(sensors_bp, url_prefix='/api/v1')
    from car_sensors_app.errors import errors_bp
    app.register_blueprint(errors_bp)
    from car_sensors_app.commands import db_manage_bp
    app.register_blueprint(db_manage_bp)

    return app