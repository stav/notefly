import json

import injector
import quart_injector
from quart import Quart, request
from quart_cors import cors

import notefly.di as di
from  notefly.brokers.interfaces import IBroker

CLIENT_URL = 'http://localhost:5000'

app = Quart(__name__)
app = cors(app, allow_origin=CLIENT_URL)


def configure(binder: injector.Binder) -> None:
    binder.bind(IBroker, to=di.QueueBroker)


@app.post('/')
async def publish(broker: injector.Inject[IBroker]) -> str:
    data = dict(await request.form)
    print('data', type(data), data)

    message = data['message']
    print('message', message)

    await broker.publish(message)
    return json.dumps(data)


@app.get('/sub')
async def subscribe(broker: IBroker) -> str:
    print('setting up', broker)
    app.add_background_task(broker.setup)
    return 'ok'


def run() -> None:
    print('Starting publish service')
    quart_injector.wire(app, modules=[di.QueueModule])
    app.run(port=5001)
