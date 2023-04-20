# Notefly

## Install

	$ pip install --upgrade pip

	$ pip install poetry

	$ pip --version
	pip 23.1 from /home/stav/.local/lib/python3.10/site-packages/pip (python 3.10)

	$ poetry add quart quart-cors
	$ poetry add --dev pytest-asyncio

## Specification

### Functional Requirements

* Log every notification dispatched, delivered, opened, seen, unsuccessful, canceled
* Three catagories: Sports, Finance, Movies
* Three types of: SMS, e-mail, push

### Non-Functional Requirements

* Low latency
* Highly available (Handling exceptions when any component failure occurs)
* High performance (real-time)
* Support as many devices as possible
* Durable — Message should not be lost, no duplication
* Scalable — Support a large number of publishers, subscribers, topics, and users
* Decoupled — follow the SOLID principle, and merge with another notification system
* Pluggable — Provide API integration with the other client applications.
