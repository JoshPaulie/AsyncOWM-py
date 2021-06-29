import aiohttp
from .city_class import City
from .data_enums import Unit


class AsyncOWMClient:
    def __init__(self, owm_key: str, unit: Unit = Unit.Imperial, country: str = "us"):
        self.owm_key = owm_key
        self.unit = unit
        self.url = self.build_url()
        self.country = country

    def build_url(self):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        url = f"{base_url}?appid={self.owm_key}&units={self.unit.name}"
        return url

    def print_url(self):
        print(self.url)

    async def test_conn(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status == 404:
                    return False
                else:
                    return True

    async def city_by_zip(self, zip_code: int):
        """Returns a City object, searchable by zip code"""
        request = f"{self.url}&zip={str(zip_code)},{self.country}"
        async with aiohttp.ClientSession() as session:
            async with session.get(request) as response:
                json = await response.json()
                return City(json, self.unit)
