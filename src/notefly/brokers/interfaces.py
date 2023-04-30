from abc import ABC, abstractmethod
from typing import AsyncGenerator


class IBroker(ABC):
    """Broker interface."""
    @abstractmethod
    async def setup(self) -> None:
        ...

    @abstractmethod
    async def publish(self, message: str) -> None:
        ...

    @abstractmethod
    async def subscribe(self) -> AsyncGenerator[str, None]:
        ...
