import joblib
import pandas as pd

model = joblib.load("models/weather_prediction_model.pkl")


def predict(data):
    """
    Predict average temperature using the trained pipeline.
    """

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)

    return float(prediction[0])