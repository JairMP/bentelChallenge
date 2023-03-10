# Documentation

## Installation (in project folder)

Setup a virtualenv and activate.

```sh
pip install virtualenv
virtualenv env
source env/bin/activate
```

Setup the project.

```sh
make setup
```

## Start API

To start the API run.

```sh
make start
```

## Test

Run Tests.

```sh
make tests
```

## Endpoints

To consume API endponints:

```sh
BASE URL: http://127.0.0.1:8000/api/
```

```sh
GET-POST http://127.0.0.1:8000/api/account
```

```sh
GET-POST http://127.0.0.1:8000/api/transaction
```

```sh
GET-PUT-DELETE http://127.0.0.1:8000/api/account/:account_number
```

```sh
GET-PUT-DELETE http://127.0.0.1:8000/api/transaction/:transaction_id
```
