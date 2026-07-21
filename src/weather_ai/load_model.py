import joblib


def load_trained_model():
    """
    Load the saved Linear Regression model.
    """

    model = joblib.load("models/weather_prediction_model.pkl")

    print("=" * 50)
    print("Model Loaded Successfully!")
    print("=" * 50)

    return model