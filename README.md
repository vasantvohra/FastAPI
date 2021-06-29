# FAST-APIs
A boilerplate to get started with `fastapi` really fast.
![FastAPI](https://raw.githubusercontent.com/vasantvohra/FastAPI/main/FastAPI.png "FastAPI")

## DONE: 

Project Structure
```
├── README.md
├── __init__.py
├── app
│ ├── core
│ │ ├── __init__.py
│ │ ├── config.py
│ │ └── security.py
│ ├── db
│ │ ├── __init__.py
│ │ ├── base_class.py
│ │ ├── init_db.py
│ │ └── session.py
│ ├── fast_api.db
│ └── statistics
|     ├── __init__.py
│     ├── models
│     │ ├── __init__.py
│     │ ├── events.py
│     │ ├── registrants.py
│     │ └── users.py
│     ├── routers
│     │ ├── __init__.py
│     │ ├── api.py
│     │ ├── index.py
│     │ ├── login.py
│     │ └── users.py
│     └── schemas
│         ├── __init__.py
│         └── users.py
├── main.py
└── requirements.txt
```

- [x] API Authentication
- [x] SQL Alchemy, connecting POSTGRES, and automatically creating tables at beginning
- [x] Type checking with `Pydantic` Schemas.
- [x] New User account, update user account, authenticate user, get a user account by email, Delete an account.
- [x] CREATE(POST) READ(GET) UPDATE(PUT) DELETE(DELETE) by admins and other user accounts

## Getting started
1. Create a Virtual Environment using virtualenv or pipenv
```sh
pip3 install virtualenv
virtualenv FASTAPI
source FASTAPI/bin/activate
pip3 install -r requirements.txt
```
2. Create Postgres DB and define on config
3. Enter a first admin account credentials on `core/config.py`

## TODO:
- Change config.py to config file
- Move users out of statistics into a `separate` module `users` module.  
- Initiate Alembic
- Flake8
- Unit Tests

