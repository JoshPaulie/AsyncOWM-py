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
```

```py
Norman current 87.4
Norman feels like 94°F
Norman coords -97.4841, 35.199
Norman has clear sky
```
## TODO
- `Setup.py`
- Move away from current weather api and use all-in-one api instead
- Country code enums
- Raw temp

### Author's note
This was made as a learning experience, and is my first public package.
