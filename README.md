# Python API Integration Demo

Original **synthetic** pre-contract portfolio example demonstrating Python, HTML, API request validation and data mapping. No client data, paid APIs or credentials.

## Run
```bash
python -m pip install -r requirements.txt
uvicorn app:app --reload
python -m pytest -q
```
Open http://127.0.0.1:8000 or /docs.

## Features
- FastAPI endpoints and HTML/JavaScript interface
- In-memory mock order source; deterministic mapping into external-system payload
- Validation and explicit missing-record errors; automated tests

## Limitations
No real external API, authentication, persistence, retries, queue, deployment or production security. This is not client work. Monetary values are represented as integer cents.
