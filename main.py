from src.weather_ai.data_loader import load_dataset ,show_dataset
from src.weather_ai.eda import (check_missing_values, check_duplicates,check_data_types)
from src.weather_ai.processing import (drop_columns,convert_date,fill_missing_values)
from src.weather_ai.feature_engineering import (extract_date_features,drop_unused_features,encode_categorical_features)
from src.weather_ai.feature_selection import(split_features_target)
from src.weather_ai.data_split import (split_train_test)
from src.weather_ai.train import (train_model)
file_path = "data/processed/weather_data.csv"

df = load_dataset(file_path)
show_dataset(df)
check_missing_values(df)
check_duplicates(df)
check_data_types(df)

df=drop_columns(df)
df=convert_date(df)
df=fill_missing_values(df)

df = extract_date_features(df)
df = drop_unused_features(df)
print("\nUpdated Columns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())
df = encode_categorical_features(df)

print("=" * 50)
print("Dataset Shape After One-Hot Encoding")
print("=" * 50)
print(df.shape)

print("\nFirst 5 Rows")
print(df.head())
print("After Use The Feature Selection")
print("=" * 50)
X, y = split_features_target(df)

X_train, X_test, y_train, y_test = split_train_test(X, y)

model = train_model(X_train, y_train)