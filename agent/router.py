"""
Intent router for the AI Customer Support Agent.

This module uses the configured LLM to classify a user request into one
of the supported application routes.

Supported Routes
----------------
- GENERAL
- RAG
- CALCULATOR
- WEB

The router is intentionally provider-independent and does not rely on
tool calling or function calling.
"""

from __future__ import annotations

from langchain_core.messages import HumanMessage, SystemMessage

from agent.llm import get_llm
from utils.constants import Route
from utils.exceptions import RoutingError
from utils.logger import get_logger

logger = get_logger(__name__)


ROUTER_PROMPT = """
You are an intent classification engine.

Your task is to classify the user's request into EXACTLY ONE category.

Allowed outputs:

GENERAL
RAG
CALCULATOR
WEB

Definitions:

GENERAL
- Greetings
- Small talk
- Conversation
- General AI questions
- Requests that do not require company knowledge,
  arithmetic, or web search.

RAG
- Questions about company policies
- Company handbook
- Company procedures
- Employee benefits
- Refunds
- Internal documentation
- Working hours
- Company services

CALCULATOR
- Mathematical expressions
- Arithmetic
- Percentages
- Financial calculations
- Unit calculations

WEB
- Recent news
- Current events
- Latest information
- Internet search
- Anything requiring external knowledge unavailable
  in company documentation.

Return ONLY ONE WORD.

Do not explain your answer.

Do not include punctuation.
""".strip()


class Router:
    """
    LLM-based intent router.
    """

    VALID_ROUTES = {route.value for route in Route}

    def __init__(self) -> None:
        self._llm = get_llm()

    def classify(self, user_input: str) -> Route:
        """
        Classify a user request.

        Parameters
        ----------
        user_input:
            User prompt.

        Returns
        -------
        Route
            Selected application route.

        Raises
        ------
        RoutingError
            If classification fails.
        """
        try:
            messages = [
                SystemMessage(content=ROUTER_PROMPT),
                HumanMessage(content=user_input),
            ]

            response = self._llm.invoke(messages)

            prediction = response.content.strip().upper()

            logger.info("Router prediction: %s", prediction)

            if prediction not in self.VALID_ROUTES:
                logger.warning(
                    "Unexpected router output '%s'. "
                    "Falling back to GENERAL.",
                    prediction,
                )
                return Route.GENERAL

            return Route(prediction)

        except Exception as exc:
            logger.exception("Intent routing failed.")

            raise RoutingError(
                f"Unable to classify request: {exc}"
            ) from exc