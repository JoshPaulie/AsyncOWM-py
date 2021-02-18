from dataclasses import dataclass

from .helpers import *
import json


class City:
    def __init__(self, city_json):
        self.name = city_json.get("name")
        self.city_json = city_json

        main = city_json.get("main")
        self.temp_current = pretty_temp(main.get("temp"))
        self.temp_low = pretty_temp(main.get("temp_min"))
        self.temp_high = pretty_temp(main.get("temp_max"))
        self.feels_like = pretty_temp(main.get("feels_like"))
        self.pressure = main.get("pressure")
        self.humidity = main.get("humidity")

        coords = city_json.get("coord")
        self.coord_lon = coords.get("lon")
        self.coord_lat = coords.get("lat")

        self.weather = city_json.get("weather")

    def print_data(self):
        data = json.dumps(self.city_json, indent=2)
        print(data)