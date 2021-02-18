# An Async, Pythonic, OpenWeatherMap Wrapper

## About
**AsyncOWM-py** is, predictably, an async wrapper for the OpenWeatherMap API written in Python

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Sample usecase

```py
import asyncio

from async_owm import AsyncOWMClient as OwmClient

client = OwmClient(owm_key="KEY")


async def main():
    client.print_url()
    norman = await client.current_by_zip(73072)
    print("Norman feels like", norman.feels_like)  # Norman feels like 60°F
    print(f"Norman coords {norman.coord_lon}, {norman.coord_lat}")  # Norman coords -97.4841, 35.199
    print("Norman weather", norman.weather)  #  Norman weather [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]

asyncio.run(main())
```

## Author's note
This was made as a learning experience, and as my first public package.
I will need help writing tests and properly structuring everything.
