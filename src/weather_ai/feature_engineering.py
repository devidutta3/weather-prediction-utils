def extract_date_features(df):
    """
    Extract year, month, and day from date.
    """

    df["year"] = df["date_of_record"].dt.year
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

    return df.drop(columns=columns)

# Do NOT perform One-Hot Encoding here.
# The Pipeline in train.py will handle categorical encoding.