# Notefly

This is a python application that uses microservices to publish messages to subscribers.
In order to allow this application to scale we employ the Inversion of Control (IoC) 
design pattern with dependency injection (DI). This allows the endpoints to access our 
message broker.

Endpoints are served by the Flask framework adjacent called "Quart".

## Installation

### Install `poetry`

	$ pip install --upgrade pip

	$ pip install poetry

### Install Notefly

	$ git clone git@github.com:stav/notefly.git

    $ poetry install

## Setup

Enter the `notefly` directory:

    $ cd notefly

Start two (2) microservices:

1. `$ poetry run client`
2. `$ poetry run broker`

## Usage

Subscribe to messages at http://localhost:5001/sub

Publish messages at http://localhost:5000/pub

## Specification

### Functional Requirements

* Log notifications
* Three types: SMS, e-mail, push
* Three categories: Finance, Movies, Sports
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

## Documentation

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
