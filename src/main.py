"""Application entry point for Url Shortener Api."""

from fastapi import FastAPI

from src.routes.health import router as health_router


app = FastAPI(
    title="Url Shortener Api",
    description="A Python backend service built with Flask/FastAPI to provide short URLs, store original links, and track click analytics for each shortened URL.",
    version="1.0.0",
)

app.include_router(health_router)


@app.get("/")
def root() -> dict[str, str]:
    """Return basic service information."""

    return {
        "service": "url-shortener-api",
        "version": "1.0.0",
        "status": "running",
        "message": "API is running successfully",
    }
