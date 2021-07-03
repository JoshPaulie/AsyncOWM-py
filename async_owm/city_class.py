from .helpers import pretty_temp
import json


class City:
    """Parses city data from passed json file"""

    def __init__(self, city_json, unit):
        self.name = city_json.get("name")
        self.city_json = city_json

        main = city_json.get("main")
        self.temp_current = pretty_temp(main.get("temp"), unit)
        self.temp_low = pretty_temp(main.get("temp_min"), unit)
        self.temp_high = pretty_temp(main.get("temp_max"), unit)
        self.feels_like = pretty_temp(main.get("feels_like"), unit)
        self.pressure = main.get("pressure")
        self.humidity = main.get("humidity")

        self.timezone = city_json.get("timezone")

        coords = city_json.get("coord")
        self.longitude = coords.get("lon")
        self.latitude = coords.get("lat")

        weather = city_json.get("weather")
        self.weather_id = weather[0]["id"]
        self.weather_main = weather[0]["main"]
        self.weather_description = weather[0]["description"]
        self.weather_icon = weather[0]["icon"]

        wind = city_json.get("wind")
        self.wind_speed = wind.get("speed")
        self.wind_degree = wind.get("deg")
        self.wind_gust = wind.get("gust")

    def print_data(self):
        data = json.dumps(self.city_json, indent=2)
        print(data)
