from src.weather_ai.data_loader import load_dataset ,show_dataset
from src.weather_ai.eda import (check_missing_values, check_duplicates,check_data_types)
file_path = "data/processed/weather_data.csv"

df = load_dataset(file_path)
show_dataset(df)
check_missing_values(df)
check_duplicates(df)
check_data_types(df)