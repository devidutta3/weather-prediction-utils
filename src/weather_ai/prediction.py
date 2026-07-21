def predict_temperature(model, X_test):
    """
    Predict average temperature using the trained model.
    """

    y_pred = model.predict(X_test)

    print("=" * 50)
    print("Prediction Completed Successfully!")
    print("=" * 50)

    print("\nFirst 10 Predictions")
    print(y_pred[:10])

    return y_pred