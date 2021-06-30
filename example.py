import asyncio
import os

# This is not a dependency, optional way to load OWM token
from dotenv import find_dotenv, load_dotenv

from async_owm import AsyncOWMClient as OwmClient

load_dotenv(find_dotenv())
client = OwmClient(owm_key=os.getenv("OWM"))


async def main():
    client.print_url()
    norman = await client.city_by_zip(73072)
    print("Norman feels like", norman.feels_like)
    print(f"Norman coords {norman.longitude}, {norman.latitude}")
    print("Norman has", norman.weather_description)
    print(norman.print_data())


asyncio.run(main())
