"""
Retriever tool.

This tool provides company knowledge retrieval for the AI Customer
Support Agent. It formats retrieved context into plain text for the
LLM and returns a standard fallback message when no relevant
information is found.
"""

from __future__ import annotations

from rag.retriever import retrieve_documents

from utils.constants import KNOWLEDGE_BASE_FALLBACK
from utils.exceptions import RetrieverToolError
from utils.logger import get_logger

logger = get_logger(__name__)


def retrieve_context(query: str) -> str:
    """
    Retrieve relevant company context.

    Parameters
    ----------
    query:
        User question.

    Returns
    -------
    str
        Retrieved context suitable for prompt injection.
    """
    try:
        documents = retrieve_documents(query)

        if not documents:
            logger.info("No matching handbook content found.")
            return KNOWLEDGE_BASE_FALLBACK

        context = "\n\n".join(
            document.page_content.strip()
            for document in documents
            if document.page_content.strip()
        )

        if not context:
            logger.info("Retrieved documents contained no usable text.")
            return KNOWLEDGE_BASE_FALLBACK

        logger.info("Successfully formatted handbook context.")

        return context

    except Exception as exc:
        logger.exception("Retriever tool failed.")

        raise RetrieverToolError(
            f"Retriever tool failed: {exc}"
        ) from exc