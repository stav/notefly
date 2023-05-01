"""
This module implements multi-producer, multi-consumer queues using `asyncio`
queues which are designed to be similar to classes of the queue module; but,
asyncio queues are not thread-safe, they are designed to be used specifically
in async/await code.
"""
import asyncio
import logging

from typing import AsyncGenerator

from .interfaces import IBroker


class QueueBroker(IBroker):
    def __init__(self) -> None:
        self.connections = set()

    def __str__(self):
        return f'{self.__class__.__name__} {id(self)} {self.__class__} {len(self.connections)} connections {self.connections}'

    async def setup(self) -> None:
        logging.getLogger('setup').info(self)
        async for message in self.subscribe():
            logging.getLogger('send').debug(f'"{message}"')
            await asyncio.sleep(1)

    async def publish(self, message: str) -> None:
        logging.getLogger('publish').debug(message)
        for connection in self.connections:
            await connection.put(message)
            logging.getLogger('sending').debug(f'"{message}" to {connection}')

    async def subscribe(self) -> AsyncGenerator[str, None]:
        connection = asyncio.Queue()
        self.connections.add(connection)
        logging.getLogger('subscribed').info(self)
        try:
            while True:
                message = await connection.get()
                logging.getLogger('received').info(f'"{message}" for {connection}')
                yield message
        finally:
            self.connections.remove(connection)
