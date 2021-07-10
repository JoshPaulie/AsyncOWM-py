import asyncio
import os

# This is not a dependency, optional way to load OWM token
from dotenv import find_dotenv, load_dotenv

from AsyncOWM_py import AsyncOWMClient as OwmClient

load_dotenv(find_dotenv())
client = OwmClient(owm_key=os.getenv("OWM"))


async def main():
    norman = await client.city_by_zip(73072)
    # Temps can be returned as float, rounded int, or "pretty" str, which adds the unit and ° symbol
    # If you don't convert, it simply returns the pretty str
    print("Norman current", float(norman.temp_current))
    print("Norman feels like", norman.feels_like)
    print(f"Norman coords {norman.longitude}, {norman.latitude}")
    print("Norman has", norman.weather_description)


asyncio.run(main())
