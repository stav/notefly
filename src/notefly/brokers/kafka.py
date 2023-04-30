"""
Apache Kafka is an open-source distributed event streaming platform used
by thousands of companies for high-performance data pipelines, streaming
analytics, data integration, and mission-critical applications.
"""
from typing import AsyncGenerator

from .interfaces import IBroker


class KafkaBroker(IBroker):
    async def setup(self) -> None:
        pass

    async def publish(self, message: str) -> None:
        pass

    async def subscribe(self) -> AsyncGenerator[str, None]:
        pass
