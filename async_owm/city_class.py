from .helpers import pretty_temp
import json


class City:
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

        coords = city_json.get("coord")
        self.coord_lon = coords.get("lon")
        self.coord_lat = coords.get("lat")

        self.weather = city_json.get("weather")

    def print_data(self):
        data = json.dumps(self.city_json, indent=2)
        print(data)
