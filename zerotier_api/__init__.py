"""A Python Wrapper for accessing the ZeroTier API."""
import asyncio
import logging

import aiohttp
import async_timeout

from . import exceptions

_LOGGER = logging.getLogger(__name__)

WRITABLE_NETWORK = [
    'name',
    'private',
    'enableBroadcast',
    'v4AssignMode',
    'v6AssignMode',
    'mtu',
    'multicastLimit'
    'routes',
    'ipAssignmentPools',
    'rules',
    'capabilities',
    'tags',
    'remoteTraceTarget',
    'remoteTraceLevel',
]

WRITABLE_MEMBER = ['authorized', 'activeBridge', 'ipAssignments']


class ZeroTier(object):
    """A class for handling the data retrieval."""

    def __init__(self, api_token, loop, session, host='localhost', port=9993):
        """Initialize the connection."""
        self._loop = loop
        self._session = session
        self.headers = {'X-ZT1-Auth': api_token}
        self.data = None
        self.url = '{}:{}'.format(host, port)

    async def get_data(self, endpoint):
        """Retrieve the data."""
        try:
            with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(
                    'http://{}/{}'.format(self.url, endpoint),
                    headers=self.headers)

            _LOGGER.debug(
                "Response status: %s", response.status)
            self.data = await response.json()
            _LOGGER.debug(self.data)
        except (asyncio.TimeoutError, aiohttp.ClientError):
            _LOGGER.error("Can not load data from ZeroTier controller")
            raise exceptions.ZeroTierConnectionError()






