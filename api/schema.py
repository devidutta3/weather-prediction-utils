from pydantic import BaseModel


class WeatherRequest(BaseModel):
    min_temp: float
    max_temp: float
    wind_speed: float
    air_pressure: float
    elevation: int
    latitude: float
    longitude: float
    rainfall: float
    year: int
    month_number: int
    day: int