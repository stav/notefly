import asyncio

from typing import AsyncGenerator

class Broker:
    def __init__(self) -> None:
        self.connections = set()
        print('Broker init', id(self))

    async def publish(self, message: str) -> None:
        print(10, message, self.connections)
        for connection in self.connections:
            print(11, connection)
            await connection.put(message)

    async def subscribe(self) -> AsyncGenerator[str, None]:
        connection = asyncio.Queue()
        print(12, connection, connection.qsize())
        self.connections.add(connection)
        print(13, self.connections)
        try:
            while True:
                print(14)
                yield await connection.get()
                print(15)
        finally:
            self.connections.remove(connection)
        print(16)
