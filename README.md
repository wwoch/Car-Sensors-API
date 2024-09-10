# Car Sensors App

A Flask application to manage car sensor data including engine temperature, tire pressure and fuel level.

## API Endpoints

- **GET /cars**: List all cars data.
- **GET /cars/<car_id>**: Get data for a specific car.
- **POST /cars**: Add new car data (JSON required).
- **PUT /cars/<car_id>**: Update data for a specific car.
- **DELETE /cars/<car_id>**: Delete data for a specific car.

## Database Management

- **Add Data**: `flask db_manage add_data`
- **Remove Data**: `flask db_manage remove_data`

## Validation

- Tire pressure: 4 entries, float values between 0.0 and 5.0 bar.
- Engine temperature: 0 to 100°C.
- Fuel level: 0 to 100%.

- Install packages from `requirements.txt`
```buildoutcfg
pip install -r requirements.txt
```
- Migrate database
```buildoutcfg
flask db upgrade
```
- Run command
```buildoutcfg
flask run
```

**NOTE**

Import / delete example data from `samples/`:

```buildoutcfg
# import
flask db-manage add-data

# remove
flask db-manage remove-data
```
