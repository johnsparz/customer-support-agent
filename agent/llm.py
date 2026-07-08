"""
LLM factory for the AI Customer Support Agent.

This module is responsible for creating and configuring the application's
ChatGroq client. It exposes a cached singleton instance to avoid repeatedly
initializing the language model.

Responsibilities
----------------
- Create the ChatGroq client
- Validate configuration
- Configure model parameters
- Centralize LLM initialization
"""

from __future__ import annotations

from functools import lru_cache

from langchain_groq import ChatGroq

from utils.config import get_settings
from utils.exceptions import ConfigurationError, LLMError
from utils.logger import get_logger

logger = get_logger(__name__)


@lru_cache(maxsize=1)
def get_llm() -> ChatGroq:
    """
    Return the configured ChatGroq client.

    The client is created only once and reused throughout the
    lifetime of the application.

    Returns
    -------
    ChatGroq
        Configured ChatGroq language model.

    Raises
    ------
    ConfigurationError
        If the Groq API key is missing.

    LLMError
        If the LLM client cannot be initialized.
    """
    settings = get_settings()

    if not settings.groq_api_key.strip():
        raise ConfigurationError(
            "GROQ_API_KEY is missing. "
            "Please configure it in the .env file."
        )

    try:
        logger.info(
            "Initializing ChatGroq model '%s'.",
            settings.groq_model,
        )

        llm = ChatGroq(
            api_key=settings.groq_api_key,
            model=settings.groq_model,
            temperature=0.2,
            max_retries=3,
            timeout=60,
        )

        logger.info("ChatGroq initialized successfully.")

        return llm

    except Exception as exc:
        logger.exception("Failed to initialize ChatGroq.")

        raise LLMError(
            f"Unable to initialize ChatGroq: {exc}"
        ) from exc


def health_check() -> bool:
    """
    Verify that the configured LLM is available.

    Returns
    -------
    bool
        True if the LLM responds successfully.

    Raises
    ------
    LLMError
        If the health check fails.
    """
    try:
        llm = get_llm()

        response = llm.invoke("Reply with the single word: OK")

        if hasattr(response, "content"):
            logger.info("LLM health check passed.")
            return True

        raise LLMError("Unexpected health check response.")

    except Exception as exc:
        logger.exception("LLM health check failed.")

        raise LLMError(
            f"Health check failed: {exc}"
        ) from exc