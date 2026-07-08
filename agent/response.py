"""
Response formatter.
"""

from __future__ import annotations


def format_response(response: str) -> str:
    """
    Clean the LLM response.
    """

    return response.strip()