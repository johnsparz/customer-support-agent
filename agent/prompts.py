"""
Prompt builder for the AI Customer Support Agent.
"""

from __future__ import annotations

from langchain_core.messages import SystemMessage


def build_system_prompt(context: str = "") -> SystemMessage:
    """
    Build the system prompt.

    Parameters
    ----------
    context:
        Retrieved company context.

    Returns
    -------
    SystemMessage
    """

    prompt = f"""
You are a professional AI Customer Support Assistant.

Rules:

- Be polite and concise.
- Answer only from the supplied company context when available.
- Never invent company policies.
- If the context is empty, answer using your general knowledge.
- If the retriever returned:
'I couldn't find this information in the company knowledge base.'
say exactly that.

Company Context:

{context}
"""

    return SystemMessage(content=prompt.strip())