import json

from quart import Quart, request
from quart_cors import cors
from dependency_injector.wiring import inject, Provide
from dependency_injector import containers, providers

from notefly import Broker
from notefly.brokers.interfaces import IBroker

CLIENT_URL = 'http://localhost:5000'

app = Quart(__name__)
app = cors(app, allow_origin=CLIENT_URL)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".broker"])
    broker_service = providers.Singleton(Broker)


@app.post('/')
@inject
async def publish(broker: IBroker = Provide[Container.broker_service]) -> str:
    print('publish', broker)

    data = dict(await request.form)
    print('data', type(data), data)

    message = data['message']
    print('message', message)

    await broker.publish(message)
    return json.dumps(data)


@app.get('/sub')
@inject
async def subscribe(broker: IBroker = Provide[Container.broker_service]) -> str:
    print('setting up', broker)
    app.add_background_task(broker.setup)
    return 'ok'


def run() -> None:
    print('Starting publish service')
    app.container = Container()
    app.run(port=5001)
