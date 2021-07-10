import aiohttp

from .custom_errors import CityNotFoundError, InvalidAPIKeyError, WrongLatitudeError
from .data_enums import Unit


def pretty_temp(temp: int, unit: Unit) -> str:
    """Returns rounded temp with unit and ° symbol"""
    symbol = unit.value[0]
    temp = round(temp)
    temp_str = f"{str(temp)}°{symbol}"
    return temp_str


async def check_request(request):
    """Checks passed URL. Returns json if successful, otherwise raises error"""
    async with aiohttp.ClientSession() as session:
        async with session.get(request) as response:
            city_json = await response.json()
            cod = int(city_json.get("cod"))
            if cod == 404:
                raise CityNotFoundError
            elif cod == 401:
                raise InvalidAPIKeyError
            elif cod == 400:
                raise WrongLatitudeError(
                    "This is a very vague and common error. Try another method of searching for your city."
                )
            elif cod == 200:
                return city_json


class Temp:
    def __init__(self, temp: float, unit: Unit):
        self.temp = temp
        self.unit = unit
        self.pretty = pretty_temp(self.temp, self.unit)

    def __int__(self):
        return int(self.temp)

    def __str__(self):
        return self.pretty

    def __float__(self):
        return self.temp

    def __repr__(self):
        return f"{self.temp}, {self.unit}, {self.pretty}"
