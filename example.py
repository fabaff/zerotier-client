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


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
