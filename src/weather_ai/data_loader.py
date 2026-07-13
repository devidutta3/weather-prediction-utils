import pandas as pd
def load_dataset(file_path):
    return pd.read_csv(file_path)

def show_dataset(df):
    print("=" * 60)
    print("First 10 Rows")
    print("=" * 60)
    print(df.head(10))

    print("\n" + "=" * 60)
    print("Last 10 Rows")
    print("=" * 60)
    print(df.tail(10))

    print("\n" + "=" * 60)
    print("Dataset Shape")
    print("=" * 60)
    print(df.shape)

    print("\n" + "=" * 60)
    print("Column Names")
    print("=" * 60)
    print(df.columns)

    print("\n" + "=" * 60)
    print("Dataset Information")
    print("=" * 60)
    df.info()

    print("\n" + "=" * 60)
    print("Statistical Summary")
    print("=" * 60)
    print(df.describe())
