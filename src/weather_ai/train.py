from sklearn.linear_model import LinearRegression as lr

def train_model(X_train,y_train):
    model=lr()
    model.fit(X_train,y_train)
    print("=" * 50)
    print("Model Training Completed Successfully!")
    print("=" * 50)

    return model