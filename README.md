# url-shortener-api

A Python backend service built with Flask/FastAPI to provide short URLs, store original links, and track click analytics for each shortened URL.

## Problem Statement

This project provides a small, maintainable starting point for the problem described above, with a health endpoint and a structure ready for incremental feature work.

## Features

- Health and service information endpoints
- Environment-based configuration
- Automated API tests
- CI validation through GitHub Actions

## Tech Stack

- Python 3.12
- FastAPI and Uvicorn
- Pytest

## Architecture

The application entry point lives in `src/main.py`. Routes are kept under `src/routes`, configuration is isolated in `src/config.py`, and tests mirror the public API under `tests`.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and adjust `APP_ENV` and `PORT` as needed. Secrets should remain in the environment and must not be committed.

## Running Locally

```bash
uvicorn src.main:app --reload
```

The service is available at `http://localhost:8000`; health status is at `/health`.

## Testing

```bash
pytest
```

## CI/CD

The included GitHub Actions workflow installs dependencies and runs the test suite on pushes and pull requests.

## Future Improvements

- Add domain-specific endpoints and persistence
- Add structured logging and observability
- Expand integration and contract test coverage

## License

MIT. See [LICENSE](LICENSE).
