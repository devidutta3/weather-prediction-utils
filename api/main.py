from fastapi import FastAPI
from api.schema import WeatherRequest
from api.predictor import predict

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Weather Prediction API is running successfully!"
    }


@app.post("/predict")
def predict_weather(request: WeatherRequest):

    data = {
        "min_temp": request.min_temp,
        "max_temp": request.max_temp,
        "wind_speed": request.wind_speed,
        "air_pressure": request.air_pressure,
        "elevation": request.elevation,
        "latitude": request.latitude,
        "longitude": request.longitude,
        "rainfall": request.rainfall,

        "season": request.season,
        "station_name": request.station_name,
        "state": request.state,
        "district": request.district,

        "year": request.year,
        "month_number": request.month_number,
        "day": request.day,
    }

    prediction = predict(data)

    return {
        "Predicted Average Temperature": prediction
    }