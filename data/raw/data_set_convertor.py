import pandas as pd
df=pd.read_excel(r"data\raw\india_weather_rainfall_data.xlsx")
df.to_csv(r"data/processed/weather_data.csv")
print("csv created Successfully 😉")