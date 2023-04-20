import asyncio
import json

from quart import Quart, render_template, request
from quart_cors import cors

app = Quart(__name__)
app = cors(app, allow_origin="http://localhost:5000")

@app.post('/')
async def index():
    data = dict(await request.form)
    print('data', type(data), data)
    return json.dumps(data)

def run() -> None:
    app.run()
