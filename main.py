from src.weather_ai.data_loader import load_dataset ,show_dataset
from src.weather_ai.eda import (check_missing_values, check_duplicates,check_data_types)
from src.weather_ai.processing import (drop_columns,convert_date,fill_missing_values)
file_path = "data/processed/weather_data.csv"

df = load_dataset(file_path)
show_dataset(df)
check_missing_values(df)
check_duplicates(df)
check_data_types(df)

df=drop_columns(df)
df=convert_date(df)
df=fill_missing_values(df)
