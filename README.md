```
# Calculator Backend

## Introduction
This is the backend of a front-end and back-end separated calculator system, built with Flask and SQLite.

## Tech Stack
- Python 3
- Flask
- Flask-CORS
- simpleeval
- SQLite

## Requirements
- Python 3.8+
- pip

## Installation
```

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

```

## Start
```

python -m src.app

```
The server runs on http://127.0.0.1:5000.

## API
- POST /api/calculate -- Calculate an expression
- GET /api/history -- Get all calculation history
- DELETE /api/history/<id> -- Delete a history record by id

## Database
SQLite file calculator.db is created automatically on first run.
```