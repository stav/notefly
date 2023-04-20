from quart import Quart, render_template

app = Quart(__name__)

@app.get("/")
async def index():
    return await render_template("index.html")

def run() -> None:
    app.run()
