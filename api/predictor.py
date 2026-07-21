import joblib

model = joblib.load("models/weather_prediction_model.pkl")
def predict(data):
    prediction = model.predict([data])

    return prediction[0]