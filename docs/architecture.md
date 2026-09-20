# Architecture

## Project

**Url Shortener Api**

A Python backend service built with Flask/FastAPI to provide short URLs, store original links, and track click analytics for each shortened URL.

## Structure

```text
src/
├── main.py
├── config.py
└── routes/
    ├── __init__.py
    └── health.py

tests/
├── __init__.py
└── test_health.py

docs/
├── architecture.md
└── api.md

examples/
└── README.md
