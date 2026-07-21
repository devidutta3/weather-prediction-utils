import joblib
import os


def save_trained_model(model):
    """
    Save the trained Linear Regression model.
    """

    os.makedirs("models", exist_ok=True)

    model_path = "models/weather_prediction_model.pkl"

    joblib.dump(model, model_path)

    print("=" * 50)
    print("Model Saved Successfully!")
    print("=" * 50)
    print(f"Model Path: {model_path}")