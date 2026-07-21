from sklearn.model_selection import train_test_split


def split_train_test(X, y):
    """
    Split the dataset into training and testing sets.
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("=" * 50)
    print("Train-Test Split")
    print("=" * 50)

    print("X_train :", X_train.shape)
    print("X_test  :", X_test.shape)
    print("y_train :", y_train.shape)
    print("y_test  :", y_test.shape)

    return X_train, X_test, y_train, y_test