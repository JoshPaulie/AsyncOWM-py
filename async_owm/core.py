import aiohttp
from .city_class import City


class AsyncOWMClient:
    def __init__(self, owm_key: str, units: str = "imperial"):
        self.owm_key = owm_key
        self.units = units
        self.url = self.build_url()

    def build_url(self):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        url = f"{base_url}?appid={self.owm_key}&units={self.units}"
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

    async def current_by_zip(self, zip_code: int):
        request = self.url + f"&zip={str(zip_code)},us"
        async with aiohttp.ClientSession() as session:
            async with session.get(request) as response:
                json = await response.json()
                return City(json)
