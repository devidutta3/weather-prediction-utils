def check_missing_values(df):
    """Display The Missing Values Are """
    print("The Missing Values Are :")
    print("="*50)
    print(df.isnull().sum())
    print("="*50)

def check_duplicates(df):
    """Display The Duplicates  Values"""
    print("="*50)
    print("Check The Duplicates Data")
    print("="*50)
    print(df.duplicated().sum())
    print("="*50)

def check_data_types(df):
    """Check The  DataTypes """
    print("="*60)
    print("Data Types")
    print("="*60)
    print(df.dtypes)
    print("="*60)