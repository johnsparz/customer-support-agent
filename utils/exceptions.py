"""
Custom exception hierarchy for the AI Customer Support Agent.

This module defines application-specific exceptions to provide
clear error handling across configuration, routing, RAG,
tools, and LLM interactions.
"""

from __future__ import annotations


class CustomerSupportAgentError(Exception):
    """
    Base exception for all application-specific errors.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


# ==========================================================
# Configuration
# ==========================================================


class ConfigurationError(CustomerSupportAgentError):
    """
    Raised when application configuration is invalid
    or required settings are missing.
    """


# ==========================================================
# Routing
# ==========================================================


class RoutingError(CustomerSupportAgentError):
    """
    Raised when the router cannot determine
    an appropriate route.
    """


# ==========================================================
# Retrieval / RAG
# ==========================================================


class VectorStoreError(CustomerSupportAgentError):
    """
    Raised when the vector store cannot be
    created, loaded, or queried.
    """


class DocumentLoadingError(CustomerSupportAgentError):
    """
    Raised when company documents cannot
    be loaded or parsed.
    """


class RetrievalError(CustomerSupportAgentError):
    """
    Raised when retrieval from the knowledge
    base fails.
    """


# ==========================================================
# LLM
# ==========================================================


class LLMError(CustomerSupportAgentError):
    """
    Raised when communication with the
    language model fails.
    """


# ==========================================================
# Memory
# ==========================================================


class MemoryError(CustomerSupportAgentError):
    """
    Raised when chat history cannot
    be stored or retrieved.
    """


# ==========================================================
# Tools
# ==========================================================


class ToolExecutionError(CustomerSupportAgentError):
    """
    Base exception for tool execution failures.
    """


class CalculatorError(ToolExecutionError):
    """
    Raised when the calculator tool
    cannot evaluate an expression.
    """


class WebSearchError(ToolExecutionError):
    """
    Raised when web search fails.
    """


class RetrieverToolError(ToolExecutionError):
    """
    Raised when the retriever tool
    encounters an error.
    """


# ==========================================================
# Validation
# ==========================================================


class ValidationError(CustomerSupportAgentError):
    """
    Raised when user input fails validation.
    """


# ==========================================================
# Response
# ==========================================================


class ResponseGenerationError(CustomerSupportAgentError):
    """
    Raised when a response cannot
    be generated successfully.
    """