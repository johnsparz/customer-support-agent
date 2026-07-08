"""
Application configuration.

This module centralizes application configuration using Pydantic Settings.
Configuration values are loaded from environment variables (or a .env file),
validated once at startup, and exposed through a cached Settings instance.

Do not access environment variables directly elsewhere in the application.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import Field, PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict

from utils.exceptions import ConfigurationError


class Settings(BaseSettings):
    """
    Strongly typed application settings loaded from the environment.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ------------------------------------------------------------------
    # LLM
    # ------------------------------------------------------------------

    groq_api_key: str = Field(..., alias="GROQ_API_KEY")
    groq_model: str = Field(
        default="llama-3.3-70b-versatile",
        alias="GROQ_MODEL",
    )

    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------

    app_name: str = Field(
        default="AI Customer Support Agent",
        alias="APP_NAME",
    )

    app_env: str = Field(
        default="development",
        alias="APP_ENV",
    )

    app_debug: bool = Field(
        default=True,
        alias="APP_DEBUG",
    )

    log_level: str = Field(
        default="INFO",
        alias="LOG_LEVEL",
    )

    # ------------------------------------------------------------------
    # Paths
    # ------------------------------------------------------------------

    data_dir: Path = Field(default=Path("data"), alias="DATA_DIR")

    log_dir: Path = Field(default=Path("logs"), alias="LOG_DIR")

    vectorstore_dir: Path = Field(
        default=Path("data/vectorstore"),
        alias="VECTORSTORE_DIR",
    )

    company_handbook: Path = Field(
        default=Path("data/company_handbook.pdf"),
        alias="COMPANY_HANDBOOK",
    )

    # ------------------------------------------------------------------
    # Embeddings / RAG
    # ------------------------------------------------------------------

    embedding_model: str = Field(
        default="sentence-transformers/all-MiniLM-L6-v2",
        alias="EMBEDDING_MODEL",
    )

    chunk_size: PositiveInt = Field(
        default=1000,
        alias="CHUNK_SIZE",
    )

    chunk_overlap: PositiveInt = Field(
        default=200,
        alias="CHUNK_OVERLAP",
    )

    top_k: PositiveInt = Field(
        default=4,
        alias="TOP_K",
    )

    # ------------------------------------------------------------------
    # Web Search
    # ------------------------------------------------------------------

    web_search_max_results: PositiveInt = Field(
        default=5,
        alias="WEB_SEARCH_MAX_RESULTS",
    )

    web_search_timeout: PositiveInt = Field(
        default=20,
        alias="WEB_SEARCH_TIMEOUT",
    )

    # ------------------------------------------------------------------
    # Conversation
    # ------------------------------------------------------------------

    max_history_messages: PositiveInt = Field(
        default=20,
        alias="MAX_HISTORY_MESSAGES",
    )

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------

    log_file: str = Field(
        default="customer_support_agent.log",
        alias="LOG_FILE",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Return the cached application settings.

    Returns
    -------
    Settings
        The validated application settings.

    Raises
    ------
    ConfigurationError
        If required configuration cannot be loaded.
    """
    try:
        settings = Settings()

        settings.data_dir.mkdir(parents=True, exist_ok=True)
        settings.log_dir.mkdir(parents=True, exist_ok=True)
        settings.vectorstore_dir.mkdir(parents=True, exist_ok=True)

        return settings

    except Exception as exc:
        raise ConfigurationError(
            f"Failed to load application configuration: {exc}"
        ) from exc