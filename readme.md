# An Async, Pythonic, OpenWeatherMap Wrapper

## About
AsyncOWM is, predictably, an async wrapper for the OpenWeatherMap API written in Python

## Sample usecase

```py
import asyncio

from async_owm import AsyncOWMClient as OwmClient

client = OwmClient(owm_key="KEY")


async def main():
    client.print_url()
    norman = await client.current_by_zip(73072)
    print("Norman feels like", norman.temps.get("temp"))
    print("Norman coords", norman.coords)
    print("Norman weather", norman.weather)
    norman.print_data()


asyncio.run(main())
```

## Author's note
This was made as a learning experience, and as my first public package.
I will need help writing tests and properly structuring everything.
