import aiohttp
from .custom_errors import CityNotFoundError, InvalidAPIKeyError, WrongLatitudeError
from .city_class import City
from .data_enums import Unit


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


class AsyncOWMClient:
    def __init__(self, owm_key: str, unit: Unit = Unit.Imperial, country: str = "us"):
        self.owm_key = owm_key
        self.unit = unit
        self.url = self.build_url()
        self.country = country

    def build_url(self) -> str:
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        url = f"{base_url}?appid={self.owm_key}&units={self.unit.name}"
        return url

    def print_url(self):
        print(self.url)

    async def test_conn(self) -> bool:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status == 404:
                    return False
                else:
                    return True

    async def city_by_zip(self, zip_code: int) -> City:
        """Returns a City object, searchable by zip code"""
        request = f"{self.url}&zip={str(zip_code)},{self.country}"
        return City(await check_request(request), self.unit)

    async def city_by_geo_coord(self, lat: float, lon: float) -> City:
        """VERY BUGGY - Returns a City object, searchable by longitude, latitude"""
        request = f"{self.url}&lat={lat}&lon={lon}"
        print(request)
        return City(await check_request(request), self.unit)

    async def city_by_city_id(self, city_id: int) -> City:
        """Returns a City object, searchable by OWM's City ID"""
        request = f"{self.url}&id={city_id}"
        return City(await check_request(request), self.unit)
