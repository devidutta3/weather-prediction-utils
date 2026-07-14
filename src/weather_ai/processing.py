import pandas as pd

def drop_columns(df):
    print(df.columns.tolist())

    columns_to_drop = ["Unnamed: 0"]

    df = df.drop(columns=columns_to_drop, errors="ignore")

    print(df.columns.tolist())

    return df


def convert_date(df):
    df["date_of_record"] = pd.to_datetime(df["date_of_record"])

    print("\nDate converted successfully!")
    print(df["date_of_record"].dtype)

    return df

def fill_missing_values(df):

    numerical_columns = [
        "min_temp",
        "max_temp",
        "wind_speed",
        "air_pressure",
        "rainfall"
    ]

    for column in numerical_columns:
        df[column] = df[column].fillna(df[column].median())

    print("\nMissing values filled successfully!")

    return df