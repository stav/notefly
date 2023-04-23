import asyncio
import json

from typing import AsyncGenerator

from quart import Quart, render_template, request
from quart_cors import cors

from notefly.kafka_broker import Broker

CLIENT_URL = 'http://localhost:5000'

app = Quart(__name__)
app = cors(app, allow_origin=CLIENT_URL)

@app.post('/')
async def index():
    data = dict(await request.form)
    print('data', type(data), data)
    return json.dumps(data)

def run() -> None:
    app.run(port=5001)
