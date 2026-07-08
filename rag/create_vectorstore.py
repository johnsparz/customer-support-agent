"""
Vector store creation for the AI Customer Support Agent.

This module builds and persists a FAISS vector store from the
company handbook. It is intended to be executed whenever the
knowledge base changes.

Responsibilities
----------------
- Load handbook documents
- Split documents into chunks
- Generate embeddings
- Build a FAISS vector store
- Persist the vector store to disk
"""

from __future__ import annotations

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from rag.loader import load_company_handbook
from utils.config import get_settings
from utils.exceptions import VectorStoreError
from utils.logger import get_logger

logger = get_logger(__name__)


def split_documents():
    """
    Split handbook documents into chunks.

    Returns
    -------
    list
        Chunked LangChain documents.
    """
    settings = get_settings()

    logger.info("Loading company handbook...")
    documents = load_company_handbook()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    )

    chunks = splitter.split_documents(documents)

    logger.info("Created %d text chunks.", len(chunks))

    return chunks


def build_vectorstore() -> FAISS:
    """
    Build a FAISS vector store.

    Returns
    -------
    FAISS
        Newly created vector store.
    """
    settings = get_settings()

    chunks = split_documents()

    logger.info("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name=settings.embedding_model,
    )

    logger.info("Generating embeddings...")

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings,
    )

    logger.info("Vector store created successfully.")

    return vectorstore


def save_vectorstore(vectorstore: FAISS) -> None:
    """
    Persist the FAISS vector store.

    Parameters
    ----------
    vectorstore:
        The FAISS vector store.
    """
    settings = get_settings()

    logger.info(
        "Saving vector store to %s",
        settings.vectorstore_dir,
    )

    vectorstore.save_local(
        folder_path=str(settings.vectorstore_dir),
    )

    logger.info("Vector store saved successfully.")


def create_vectorstore() -> None:
    """
    Complete vector store creation workflow.

    Raises
    ------
    VectorStoreError
        If vector store creation fails.
    """
    try:
        vectorstore = build_vectorstore()
        save_vectorstore(vectorstore)

        logger.info("Knowledge base successfully indexed.")

    except Exception as exc:
        logger.exception("Vector store creation failed.")

        raise VectorStoreError(
            f"Failed to create vector store: {exc}"
        ) from exc


if __name__ == "__main__":
    create_vectorstore()