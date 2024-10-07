import uvicorn
from fastapi import FastAPI
import app.application
from app.router import app_router


def main() -> None:
    """Entrypoint of the application."""

    uvicorn.run(
        "app.application:get_app",
        workers=1,
        host="0.0.0.0",
        port=8090,
        reload=True,
        factory=True,
    )
