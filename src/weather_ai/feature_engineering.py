import pandas as pd
def extract_date_features(df):
    df["year"]=df["date_of_record"].dt.year
    df["month_number"] = df["date_of_record"].dt.month
    df["day"] = df["date_of_record"].dt.day

    return df


def drop_unused_features(df):
    """
    Drop unnecessary columns.
    """

    columns = [
        "date_of_record",
        "month"
    ]

    df = df.drop(columns=columns)

    return df



def encode_categorical_features(df):
    """
    Convert categorical columns into numerical columns using One-Hot Encoding.
    """

    categorical_columns = [
        "season",
        "station_name",
        "state",
        "district"
    ]

    df = pd.get_dummies(
        df,
        columns=categorical_columns,
        drop_first=True,
        dtype=int
    )

    return df