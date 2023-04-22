from notefly.client import app as client_app
from notefly.broker import app as broker_app

def client() -> None:
    client_app.run(port=5000)

def broker() -> None:
    broker_app.run(port=5001)
