import asyncio

from quart import Quart, render_template

app = Quart(__name__)

@app.get('/')
async def index():
    return await render_template("client.html")

def run() -> None:
    app.run(port=5000)
