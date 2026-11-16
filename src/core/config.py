
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Enterprise Agentic RAG"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    GROQ_API_KEY: str = ""

    DATABASE_URL: str = "postgresql://localhost:5432/rag_db"
    QDRANT_URL: str = "http://localhost:6333"

    EMBEDDING_MODEL_SMALL: str = "BAAI/bge-small-en-v1.5"
    EMBEDDING_MODEL_BASE: str = "BAAI/bge-base-en-v1.5"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
