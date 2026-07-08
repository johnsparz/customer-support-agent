"""
Web search tool using DDGS.

This module performs external searches and summarizes
information before returning it to the user.
"""

from __future__ import annotations

from ddgs import DDGS

from agent.llm import get_llm
from langchain_core.messages import HumanMessage

from utils.exceptions import WebSearchError
from utils.logger import get_logger

logger = get_logger(__name__)


def web_search(query: str) -> str:
    """
    Search the web and summarize results.

    Parameters
    ----------
    query:
        Search query.

    Returns
    -------
    str
        Summarized search response.
    """

    try:
        logger.info(
            "Performing web search: %s",
            query,
        )

        with DDGS() as search:

            results = list(
                search.text(
                    query,
                    max_results=5,
                )
            )

        if not results:
            return "No web results were found."

        combined = "\n".join(
            result.get("body", "")
            for result in results
        )

        llm = get_llm()

        response = llm.invoke(
            [
                HumanMessage(
                    content=f"""
Summarize these web search results.

Provide a concise answer.

Results:

{combined}
"""
                )
            ]
        )

        return response.content.strip()

    except Exception as exc:
        logger.exception(
            "Web search failed."
        )

        raise WebSearchError(
            f"Web search failed: {exc}"
        ) from exc