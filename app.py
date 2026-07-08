"""
Streamlit application for the AI Customer Support Agent.

The UI layer only manages user interaction.
All AI logic is handled by CustomerAgent.
"""

from __future__ import annotations

import streamlit as st

from agent.customer_agent import CustomerAgent
from utils.constants import PAGE_ICON, PAGE_TITLE
from utils.logger import get_logger

logger = get_logger(__name__)


def initialize_agent() -> CustomerAgent:
    """
    Initialize the customer agent.

    Returns
    -------
    CustomerAgent
        AI assistant instance.
    """

    if "agent" not in st.session_state:
        st.session_state.agent = CustomerAgent()

    return st.session_state.agent


def initialize_chat_history() -> None:
    """
    Initialize Streamlit chat history.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = []


def display_chat_history() -> None:
    """
    Display previous messages.
    """

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(
                message["content"]
            )


def add_message(
    role: str,
    content: str,
) -> None:
    """
    Store a chat message.

    Parameters
    ----------
    role:
        Message role.

    content:
        Message content.
    """

    st.session_state.messages.append(
        {
            "role": role,
            "content": content,
        }
    )


def main() -> None:
    """
    Run Streamlit application.
    """

    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="centered",
    )

    st.title(PAGE_TITLE)

    initialize_chat_history()

    agent = initialize_agent()

    display_chat_history()

    user_input = st.chat_input(
        "Ask me anything..."
    )

    if user_input:

        add_message(
            "user",
            user_input,
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        try:

            with st.chat_message("assistant"):

                with st.spinner(
                    "Thinking..."
                ):

                    response = (
                        agent.generate_response(
                            user_input
                        )
                    )

                    st.markdown(response)

            add_message(
                "assistant",
                response,
            )

        except Exception as exc:

            logger.exception(
                "Application error."
            )

            error_message = (
                "Sorry, I was unable to process "
                "your request."
            )

            st.error(error_message)

            add_message(
                "assistant",
                error_message,
            )


if __name__ == "__main__":
    main()