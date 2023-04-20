from notefly.client import app as client_app
from notefly.queue import app as queue_app

def client() -> None:
    client_app.run(port=5000, headers={'Access-Control-Allow-Origin': '*'})

def queue() -> None:
    queue_app.run(port=5001, headers={'Access-Control-Allow-Origin': '*'})
