import asyncio
import os

from async_owm import AsyncOWMClient as OwmClient

client = OwmClient(owm_key=os.getenv("OWMKEY"))


async def main():
    client.print_url()
    norman = await client.current_by_zip(73072)
    print("Norman feels like", norman.feels_like)  # Norman feels like 60°F
    print(f"Norman coords {norman.coord_lon}, {norman.coord_lat}")  # Norman coords -97.4841, 35.199
    print("Norman weather", norman.weather)  #  Norman weather [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]

asyncio.run(main())