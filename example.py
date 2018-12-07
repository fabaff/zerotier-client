"""Get the data from a given station."""
import asyncio

import aiohttp

from zerotier_api import ZeroTier

ZT_HOST = 'localhost'
ZT_API = 'b9678h3ekdeylrfaq316b2oa'


async def main():
    """Sample code to retrieve the data from a ZeroTier controller."""
    async with aiohttp.ClientSession() as session:
        data = ZeroTier(ZT_API, loop, session)
        await data.get_data('controller')

        print(data.data)
        # if not await data.validate_sensor():
        #     print("Station is not available:", data.sensor_id)
        #     return
        #
        # if data.values and data.meta:
        #     # Print the sensor values
        #     print("Sensor values:", data.values)
        #
        #     # Print the coordinates fo the sensor
        #     print("Location:", data.meta['latitude'], data.meta['longitude'])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
