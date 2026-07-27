from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression


def train_model(X_train, y_train):
    """
    Train a Linear Regression model using a preprocessing pipeline.
    """

    categorical_features = [
        "season",
        "station_name",
        "state",
        "district"
    ]

    numerical_features = [
        "min_temp",
        "max_temp",
        "wind_speed",
        "air_pressure",
        "elevation",
        "latitude",
        "longitude",
        "rainfall",
        "year",
        "month_number",
        "day"
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features
            ),
            (
                "num",
                "passthrough",
                numerical_features
            )
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression())
        ]
    )

    model.fit(X_train, y_train)

    print("=" * 50)
    print("Pipeline Model Trained Successfully!")
    print("=" * 50)

    return model