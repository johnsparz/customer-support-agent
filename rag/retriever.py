"""
Retriever implementation for the AI Customer Support Agent.

This module loads the persisted FAISS vector store and exposes a
simple retrieval interface for the rest of the application.

The vector store is cached after the first load to avoid repeatedly
reading the FAISS index from disk.
"""

from __future__ import annotations

from functools import lru_cache

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

from utils.config import get_settings
from utils.exceptions import RetrievalError
from utils.logger import get_logger

logger = get_logger(__name__)


@lru_cache(maxsize=1)
def _load_vectorstore() -> FAISS:
    """
    Load the persisted FAISS vector store.

    Returns
    -------
    FAISS
        Loaded vector store.

    Raises
    ------
    RetrievalError
        If the vector store cannot be loaded.
    """
    settings = get_settings()

    try:
        logger.info("Loading FAISS vector store...")

        embeddings = HuggingFaceEmbeddings(
            model_name=settings.embedding_model,
        )

        vectorstore = FAISS.load_local(
            folder_path=str(settings.vectorstore_dir),
            embeddings=embeddings,
            allow_dangerous_deserialization=True,
        )

        logger.info("Vector store loaded successfully.")

        return vectorstore

    except Exception as exc:
        logger.exception("Unable to load vector store.")

        raise RetrievalError(
            f"Failed to load vector store: {exc}"
        ) from exc


def retrieve_documents(query: str) -> list[Document]:
    """
    Retrieve relevant handbook documents.

    Parameters
    ----------
    query:
        User query.

    Returns
    -------
    list[Document]
        Retrieved handbook chunks.

    Raises
    ------
    RetrievalError
        If retrieval fails.
    """
    settings = get_settings()

    try:
        retriever = _load_vectorstore().as_retriever(
            search_kwargs={
                "k": settings.top_k,
            }
        )

        documents = retriever.invoke(query)

        logger.info(
            "Retrieved %d document(s).",
            len(documents),
        )

        return documents

    except Exception as exc:
        logger.exception("Document retrieval failed.")

        raise RetrievalError(
            f"Retriever failed: {exc}"
        ) from exc