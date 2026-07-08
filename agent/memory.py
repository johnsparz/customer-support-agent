"""
Conversation history management for the AI Customer Support Agent.

This module provides a lightweight wrapper around LangChain's
InMemoryChatMessageHistory. It is intentionally provider-independent
and avoids deprecated memory abstractions.

The implementation can later be replaced with Redis, SQLite,
PostgreSQL, or another persistent backend without changing the
CustomerAgent interface.
"""

from __future__ import annotations

from threading import Lock

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
)

from utils.config import get_settings
from utils.logger import get_logger

logger = get_logger(__name__)


class ConversationMemory:
    """
    Manage conversation history.

    This class stores conversation messages using LangChain's
    modern chat history implementation while enforcing a
    configurable maximum history length.
    """

    def __init__(self) -> None:
        self._settings = get_settings()
        self._history = InMemoryChatMessageHistory()
        self._lock = Lock()

    def add_user_message(self, message: str) -> None:
        """
        Store a user message.

        Parameters
        ----------
        message:
            User input.
        """
        with self._lock:
            self._history.add_message(HumanMessage(content=message))
            self._trim_history()

    def add_ai_message(self, message: str) -> None:
        """
        Store an AI response.

        Parameters
        ----------
        message:
            Assistant response.
        """
        with self._lock:
            self._history.add_message(AIMessage(content=message))
            self._trim_history()

    def get_messages(self) -> list[BaseMessage]:
        """
        Return the current conversation history.

        Returns
        -------
        list[BaseMessage]
        """
        with self._lock:
            return list(self._history.messages)

    def clear(self) -> None:
        """
        Clear all stored conversation history.
        """
        with self._lock:
            self._history.clear()
            logger.info("Conversation history cleared.")

    def _trim_history(self) -> None:
        """
        Limit the number of stored messages.
        """
        max_messages = self._settings.max_history_messages

        if len(self._history.messages) > max_messages:
            self._history.messages = self._history.messages[-max_messages:]

            logger.debug(
                "Conversation history trimmed to %d messages.",
                max_messages,
            )

    @property
    def message_count(self) -> int:
        """
        Return the number of stored messages.
        """
        return len(self._history.messages)