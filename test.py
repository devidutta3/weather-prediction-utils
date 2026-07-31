import weather_prediction

print("Package location:", weather_prediction.__file__)
print("Version:", weather_prediction.__version__)

weather_prediction.generate_readme()

prediction = weather_prediction.predict(
    min_temp=25.0,
    max_temp=34.5,
    wind_speed=12.3,
    air_pressure=1012.5,
    elevation=45,
    latitude=20.2961,
    longitude=85.8245,
    rainfall=2.5,
    season="Summer",
    station_name="Bhubaneswar",
    state="Odisha",
    district="Khordha",
    year=2026,
    month_number=7,
    day=27,
)

print("Prediction:", prediction)