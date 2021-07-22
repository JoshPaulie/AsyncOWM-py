from .city import City
from .data_enums import Unit
from .helpers import make_request


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

    async def city_by_city_name(self, city_name: int, state_code: str = None) -> City:
        """Returns a City object, searchable by OWM's City ID"""
        if state_code:
            request = f"{self.url}&q={city_name},{state_code},{self.country}"
        else:
            request = f"{self.url}&q={city_name}"
        return City(await make_request(request), self.unit)

    async def city_by_zip(self, zip_code: int) -> City:
        """Returns a City object, searchable by zip code"""
        request = f"{self.url}&zip={str(zip_code)},{self.country}"
        return City(await make_request(request), self.unit)

    async def city_by_geo_coord(self, lat: float, lon: float) -> City:
        """VERY BUGGY - Returns a City object, searchable by longitude, latitude"""
        request = f"{self.url}&lat={lat}&lon={lon}"
        print(request)
        return City(await make_request(request), self.unit)

    async def city_by_city_id(self, city_id: int) -> City:
        """Returns a City object, searchable by OWM's City ID"""
        request = f"{self.url}&id={city_id}"
        return City(await make_request(request), self.unit)
