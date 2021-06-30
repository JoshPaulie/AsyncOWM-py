# An Async, Pythonic, OpenWeatherMap Wrapper

## About
**AsyncOWM-py** is, predictably, an async wrapper for the OpenWeatherMap API written in Python

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Sample usecase

```py
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
```

```py
http://api.openweathermap.org/data/2.5/weather?appid=APIKEY&units=Imperial
Norman feels like 91°F
Norman coords -97.4841, 35.199   
Norman has clear sky
{
  ...
}
```
## TODO
- Setup.py
- More robust classes
- Additional lookup methods other than zipcode
- Add expections for invalid api key, 404 error

### Author's note
This was made as a learning experience, and is my first public package.
