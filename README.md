# python django demo server

This is a basic Django app that provides endpoints for creating and listing products.

## Prerequisites

To run this app, you'll need to have the following software installed on your computer:

- Python 3.9 or later
- Docker

## Installation

- Clone the repository:

```
$ git clone https://github.com/alarbada/django-demo
$ cd django-demo
```

- (Optionally) build the Docker image:

```
$ docker build -t my-django-app .
```

- Install the required Python packages:

```
$ pip install -r requirements.txt
```

## Usage

Start the Django development server:

```
$ python manage.py runserver
```
