import logging
from fastapi import FastAPI

from src.core.config import settings
from src.core.logging_config import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    description="An adaptive multi-document RAG application",
    version=settings.APP_VERSION,
)


@app.get("/health")
async def health_check():
    logger.info("Health check requested")

    return {
        "status": "healthy",
        "service": settings.APP_NAME,
    }