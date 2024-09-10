import os
from car_sensors_app import build_app

app=build_app()

os.environ['FLASK_APP'] = 'app'

if __name__ == '__main__':
    app.run()
