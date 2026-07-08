"""
Application-wide constants.

This module contains immutable values that are shared across the
application. Configuration values that may vary between environments
must be defined in config.py and loaded from environment variables.
"""

from __future__ import annotations

from enum import Enum

# ==========================================================
# Application Metadata
# ==========================================================

APP_VERSION: str = "1.0.0"

# ==========================================================
# Routing
# ==========================================================


class Route(str, Enum):
    """Supported routing destinations."""

    GENERAL = "GENERAL"
    RAG = "RAG"
    CALCULATOR = "CALCULATOR"
    WEB = "WEB"


# ==========================================================
# Supported File Types
# ==========================================================

SUPPORTED_DOCUMENT_EXTENSIONS: tuple[str, ...] = (
    ".pdf",
)

# ==========================================================
# Conversation Roles
# ==========================================================

SYSTEM_ROLE: str = "system"
USER_ROLE: str = "user"
ASSISTANT_ROLE: str = "assistant"

# ==========================================================
# Default Responses
# ==========================================================

KNOWLEDGE_BASE_FALLBACK: str = (
    "I couldn't find this information in the company knowledge base."
)

GENERIC_ERROR_MESSAGE: str = (
    "Sorry, something went wrong while processing your request."
)

EMPTY_INPUT_MESSAGE: str = (
    "Please enter a message before submitting."
)

INVALID_CALCULATION_MESSAGE: str = (
    "The calculator could not evaluate the supplied expression."
)

WEB_SEARCH_FAILURE_MESSAGE: str = (
    "I couldn't retrieve web results at the moment."
)

# ==========================================================
# Logging
# ==========================================================

LOGGER_NAME: str = "customer_support_agent"

LOG_FORMAT: str = (
    "%(asctime)s | %(levelname)s | %(name)s | "
    "%(filename)s:%(lineno)d | %(message)s"
)

DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"

# ==========================================================
# Prompt Labels
# ==========================================================

COMPANY_CONTEXT_HEADER: str = "Company Knowledge"

CHAT_HISTORY_HEADER: str = "Conversation History"

USER_QUESTION_HEADER: str = "User Question"

# ==========================================================
# Streamlit
# ==========================================================

CHAT_INPUT_PLACEHOLDER: str = (
    "Ask me about company policies, products, calculations, or recent news..."
)

PAGE_TITLE: str = "AI Customer Support Agent"

PAGE_ICON: str = "🤖"

# ==========================================================
# Vector Store
# ==========================================================

VECTORSTORE_FILENAME: str = "faiss_index"

# ==========================================================
# Web Search
# ==========================================================

NEWS_KEYWORDS: tuple[str, ...] = (
    "today",
    "latest",
    "recent",
    "breaking",
    "news",
    "update",
)