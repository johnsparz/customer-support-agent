"""
Document loader for the AI Customer Support Agent.

This module is responsible only for loading the company handbook
from disk. It does not perform chunking, embedding generation,
or vector store creation.
"""

from __future__ import annotations

from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

from utils.config import get_settings
from utils.exceptions import DocumentLoadingError
from utils.logger import get_logger

logger = get_logger(__name__)


def load_company_handbook() -> list[Document]:
    """
    Load the company handbook PDF.

    Returns
    -------
    list[Document]
        Loaded LangChain documents.

    Raises
    ------
    DocumentLoadingError
        If the handbook cannot be found or loaded.
    """
    settings = get_settings()

    handbook_path = Path(settings.company_handbook)

    if not handbook_path.exists():
        raise DocumentLoadingError(
            f"Company handbook not found: {handbook_path}"
        )

    try:
        logger.info("Loading handbook: %s", handbook_path)

        loader = PyPDFLoader(
            file_path=str(handbook_path),
        )

        documents = loader.load()

        logger.info(
            "Loaded %d document(s) from handbook.",
            len(documents),
        )

        return documents

    except Exception as exc:
        logger.exception("Failed to load handbook.")

        raise DocumentLoadingError(
            f"Unable to load handbook: {exc}"
        ) from exc