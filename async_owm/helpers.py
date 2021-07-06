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
