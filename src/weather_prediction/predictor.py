import os
import joblib
import pandas as pd

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "weather_prediction_model.pkl"
)

model = joblib.load(MODEL_PATH)


def predict(
    min_temp,
    max_temp,
    wind_speed,
    air_pressure,
    elevation,
    latitude,
    longitude,
    rainfall,
    season,
    station_name,
    state,
    district,
    year,
    month_number,
    day,
):
    data = pd.DataFrame(
        [{
            "min_temp": min_temp,
            "max_temp": max_temp,
            "wind_speed": wind_speed,
            "air_pressure": air_pressure,
            "elevation": elevation,
            "latitude": latitude,
            "longitude": longitude,
            "rainfall": rainfall,
            "season": season,
            "station_name": station_name,
            "state": state,
            "district": district,
            "year": year,
            "month_number": month_number,
            "day": day,
        }]
    )

    prediction = model.predict(data)

    return float(prediction[0])