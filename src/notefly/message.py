import asyncio
import json

from functools import partial

from typing import AsyncGenerator

from quart import Quart, render_template, request
from quart_cors import cors

from notefly.brokers import Broker

CLIENT_URL = 'http://localhost:5000'

is_setup = False

app = Quart(__name__)
app = cors(app, allow_origin=CLIENT_URL)

async def index(broker):
    global is_setup
    if not is_setup:
        print('setting up', broker)
        app.add_background_task(broker.setup)
        is_setup = True

    data = dict(await request.form)
    print('data', type(data), data)

    message = data['message']
    print('message', message)

    await broker.publish(message)
    return json.dumps(data)

def run() -> None:
    broker = Broker()
    app.post("/", endpoint="index")(partial(index, broker=broker))
    print('Starting message server')
    app.run(port=5001)
