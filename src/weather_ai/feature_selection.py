def split_features_target(df):
    """
    Split dataset into Features (X) and Target (y).
    """

    X = df.drop(columns=["avg_temp"])
    y = df["avg_temp"]

    print("=" * 50)
    print("Feature Matrix (X)")
    print("=" * 50)
    print(X.shape)

    print("=" * 50)
    print("Target Vector (y)")
    print("=" * 50)
    print(y.shape)

    return X, y