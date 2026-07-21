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

    data = [
        request.min_temp,
        request.max_temp,
        request.wind_speed,
        request.air_pressure,
        request.elevation,
        request.latitude,
        request.longitude,
        request.rainfall,
        request.year,
        request.month_number,
        request.day,
    ]

    prediction = predict(data)

    return {
        "Predicted Average Temperature": prediction
    }