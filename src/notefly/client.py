import asyncio

from quart import Quart, render_template

app = Quart(__name__)

@app.route('/')
def index():
    return """
    <html>
    <head></head>
    <body>
    <a href="/pub">/pub</a></br>
    <a href="/sub">/sub</a>
    </body>
    </html>
    """

@app.get('/pub')
async def pub():
    return await render_template("publish.html")

@app.get('/sub')
async def sub():
    return await render_template("subscribe.html")

def run() -> None:
    app.run(port=5000)
