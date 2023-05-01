import json
import logging

from quart import Quart, request
from quart_cors import cors
from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide

from notefly import Broker
from notefly.brokers.interfaces import IBroker

CLIENT_URL = 'http://localhost:5000'

app = Quart(__name__)
app = cors(app, allow_origin=CLIENT_URL)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".broker"])
    loging_config = providers.Configuration(yaml_files=["./config.yml"])
    broker_service = providers.Singleton(Broker)

    logging = providers.Resource(
        logging.basicConfig,
        level=loging_config.log.level,
        format=loging_config.log.format,
        filename=loging_config.log.filename,
    )


@app.post('/')
@inject
async def publish(broker: IBroker = Provide[Container.broker_service]) -> str:
    data = dict(await request.form)
    message = data['message']
    logging.getLogger('publishing').debug(message)
    await broker.publish(message)
    return json.dumps(data)


@app.get('/sub')
@inject
async def subscribe(broker: IBroker = Provide[Container.broker_service]) -> str:
    logging.getLogger('settingup').debug(broker)
    app.add_background_task(broker.setup)
    return 'ok'


def run() -> None:
    app.container = Container()
    app.container.init_resources()
    logging.info('Starting publish service')
    try:
        app.run(port=5001)
    finally:
        app.container.shutdown_resources()
