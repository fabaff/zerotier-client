"""Get the data from a given network."""
import asyncio

import aiohttp

from zerotier_api import ZeroTier

ZT_HOST = 'localhost'
ZT_API = 'b9678h3ekdeylrfaq316b2oa'


async def main():
    """Sample code to retrieve the data from a ZeroTier controller."""
    async with aiohttp.ClientSession() as session:
        client = ZeroTier(ZT_API, loop, session)

        # Print details of the controller
        await client.get_data('controller')
        print(client.data)

        # Display all available nets
        await client.get_data('network')
        for network in client.data:
            print(network.get('id'))

        # Get details about a network
        await client.get_data('network/{}'.format('0a40c2fcc19db3fd'))
        print(client.data)

        # # Set a new name for an existing network
        # await client.set_value(
        #     'name', 'new name', 'network/{}'.format('0a40c2fcc19db3fd'))
        # await client.get_data('network/{}'.format('0a40c2fcc19db3fd'))
        # print(client.data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
