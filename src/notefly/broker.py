import json

from functools import partial

from quart import Quart, request
from quart_cors import cors

from notefly.brokers import Broker

CLIENT_URL = 'http://localhost:5000'

app = Quart(__name__)
app = cors(app, allow_origin=CLIENT_URL)


async def publish(broker):
    data = dict(await request.form)
    print('data', type(data), data)

    message = data['message']
    print('message', message)

    await broker.publish(message)
    return json.dumps(data)


async def subscribe(broker):
    print('setting up', broker)
    app.add_background_task(broker.setup)
    return 'ok'


def run() -> None:
    broker = Broker()
    app.post("/", endpoint="/")(partial(publish, broker=broker))
    app.get("/sub", endpoint="/sub")(partial(subscribe, broker=broker))
    print('Starting publish service')
    app.run(port=5001)
