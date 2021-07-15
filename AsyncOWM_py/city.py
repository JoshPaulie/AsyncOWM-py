import json

from .helpers import Temp


class City:
    """Parses city data from passed json file"""

    def __init__(self, city_json, unit):
        """👋🏻 Thanks for checking out my repo! Please let me know how I could improve this class."""
        self.json = city_json
        self.name = self.json.get("name")

        main = self.json.get("main")
        self.temp_current = Temp(main.get("temp"), unit)
        self.temp_low = Temp(main.get("temp_min"), unit)
        self.temp_high = Temp(main.get("temp_max"), unit)
        self.feels_like = Temp(main.get("feels_like"), unit)

        self.pressure = main.get("pressure")
        self.humidity = main.get("humidity")

        self.timezone = self.json.get("timezone")

        coords = self.json.get("coord")
        self.longitude = coords.get("lon")
        self.latitude = coords.get("lat")

        weather = self.json.get("weather")
        self.weather_id = weather[0]["id"]
        self.weather_main = weather[0]["main"]
        self.weather_description = weather[0]["description"]
        self.weather_icon = weather[0]["icon"]

        wind = self.json.get("wind")
        self.wind_speed = wind.get("speed")
        self.wind_degree = wind.get("deg")
        self.wind_gust = wind.get("gust")

        self.dt = self.json.get("dt")

        sys = self.json.get("sys")
        self.sys_type = sys.get("type")
        self.sys_country = sys.get("country")
        self.sys_sunrise = sys.get("sunrise")
        self.sys_sunset = sys.get("sunset")

        self.clouds = self.json.get("clouds").get("all")

        self.visibility = self.json.get("visibility")

    def print_data(self):
        data = json.dumps(self.json, indent=2)
        print(data)
