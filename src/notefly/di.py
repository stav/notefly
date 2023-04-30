from injector import Module, provider, singleton

from notefly.brokers import KafkaBroker, QueueBroker
from notefly.brokers.interfaces import IBroker


class QueueModule(Module):
    @provider
    @singleton
    def provide_broker(self) -> IBroker:
        return QueueBroker()
