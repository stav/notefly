"""
This module implements multi-producer, multi-consumer queues using `asyncio`
queues which are designed to be similar to classes of the queue module; but,
asyncio queues are not thread-safe, they are designed to be used specifically
in async/await code.
"""
import asyncio

from typing import AsyncGenerator

class QueueBroker:
    def __init__(self) -> None:
        self.connections = set()
        print('init', self)

    def __str__(self):
        return f'{self.__class__.__name__} {id(self)} {self.__class__} {len(self.connections)} connections {self.connections}'

    async def setup(self) -> None:
        print('setup', self)
        # await asyncio.sleep(1)
        async for message in self.subscribe():
            print(5, message)
            # await websocket.send(message)
            await asyncio.sleep(1)

    async def publish(self, message: str) -> None:
        print(10, message, self)
        for connection in self.connections:
            print(11, connection)
            await connection.put(message)

    async def subscribe(self) -> AsyncGenerator[str, None]:
        connection = asyncio.Queue()
        print(12, connection, connection.qsize())
        self.connections.add(connection)
        print(13, self)
        try:
            while True:
                print(14)
                x = await connection.get()
                print(15, x)
                yield x
        finally:
            self.connections.remove(connection)
        print(16)
