import os
import joblib


def save_trained_model(model):

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, "models/weather_prediction_model.pkl")

    print("=" * 50)
    print("Pipeline Saved Successfully!")
    print("=" * 50)