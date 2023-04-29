# Notefly

Messaging platforms provide a way for microservices to communicate and exchange 
data reliably and efficiently. This reliable communication between services 
architecture is crucial for completing tasks in microservice, as each service 
is responsible for managing one specific function.

## Message Queuing System

A message queuing system allows for asynchronous communication between
different components of your notification system. It ensures that messages
are not lost, even if the recipient is offline, and provides a buffer to
handle bursts of traffic.

Message queuing, also known as point-to-point communication, involves sending 
messages to a queue, where they are stored until the intended recipient processes
them. The sender and receiver do not need to be connected at the same time, 
facilitating asynchronous communication. The messages are stored in the queue 
until they can be delivered, and they are generally deleted after that.

Generally, queuing is appropriate for use cases where there’s no requirement 
for real-time delivery or processing, such as batch processing, order fulfillment, 
or offline data processing.

## Install

	$ pip install --upgrade pip

	$ pip install poetry

	$ pip --version
	pip 23.1 from /home/stav/.local/lib/python3.10/site-packages/pip (python 3.10)

	$ poetry add quart quart-cors
	$ poetry add --dev pytest-asyncio

## Usage

Start two (2) microservices:

If you have `nodemon`:

1. `$ nodemon --watch ./src/ --exec "poetry run client" src/notefly/client.py`
2. `$ nodemon --watch ./src/ --exec "poetry run broker" src/notefly/broker.py`

otherwise:

1. `$ poetry run client`
2. `$ poetry run broker`

## Specification

### Functional Requirements

* Log every notification dispatched, delivered, opened, seen, unsuccessful, canceled
* Three categories: Sports, Finance, Movies
* Three types: SMS, e-mail, push
* Scalable: add more types of notifications
* Users can subscribe to categories
* Users can select which message types they want to receive
* Manage requests to the Server by RESTful APIs

### Non-Functional Requirements

* Architecture: software design patterns
* OOP: use object oriented programming techniques
* Testing: register at least 3 users with different configurations
* Log: store activity but don't actually send any actual notifications
* Admin: no need for administration, just use mocks
* Ordering: message order does not need to be guaranteed
