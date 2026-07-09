"""
Streamlit application for the AI Customer Support Agent.

The UI layer only manages user interaction.
All AI logic is handled by CustomerAgent.
"""

from __future__ import annotations

from datetime import datetime

import streamlit as st

from agent.customer_agent import CustomerAgent
from utils.constants import PAGE_ICON, PAGE_TITLE
from utils.logger import get_logger

logger = get_logger(__name__)


# --------------------------------------------------------------------
# Initialization
# --------------------------------------------------------------------


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


# --------------------------------------------------------------------
# Sidebar
# --------------------------------------------------------------------


def render_sidebar() -> None:
    """
    Render application sidebar.
    """

    with st.sidebar:

        st.title("🤖 NovaTech AI Customer Support Agent")

        st.caption(
            "Production-ready AI assistant powered by "
            "Groq, LangChain, RAG and FAISS."
        )

        st.divider()

        st.subheader("📚 Example Questions")

        with st.expander("🏢 Company Knowledge", expanded=True):
            st.markdown(
                """
- What is the refund policy?
- What are your working hours?
- What benefits do employees receive?
                """
            )

        with st.expander("🧮 Calculator", expanded=True):
            st.markdown(
                """
- 875 / 46
                """
            )

        with st.expander("🌐 Web Search", expanded=True):
            st.markdown(
                """
- Latest AI news
- Who won the Champions League?
                """
            )

        with st.expander("💬 General Conversation"):
            st.markdown(
                """
- Tell me about your services.
                """
            )

        st.divider()

        st.subheader("⚙️ AI Stack")

        st.markdown(
            """
- Python 3.12
- LangChain 1.x
- Groq Llama 3.3
- FAISS
- HuggingFace Embeddings
- DDGS
- Streamlit
            """
        )

        st.divider()

        st.subheader("👨‍💻 Developer")

        st.markdown(
            """
**John Arije**

AI Engineer | Machine Learning Engineer

GitHub:
https://github.com/johnsparz

Live Demo:
https://customer-support-agent-johnsparz.streamlit.app/
            """
        )


# --------------------------------------------------------------------
# Chat history
# --------------------------------------------------------------------


def display_chat_history() -> None:
    """
    Display previous messages.
    """

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def add_message(
    role: str,
    content: str,
) -> None:
    """
    Store chat message.
    """

    st.session_state.messages.append(
        {
            "role": role,
            "content": content,
        }
    )

    # --------------------------------------------------------------------
# Main application
# --------------------------------------------------------------------


def main() -> None:
    """
    Run Streamlit application.
    """

    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="centered",
    )

    initialize_chat_history()

    agent = initialize_agent()

    render_sidebar()

    # ----------------------------------------------------------
    # Header
    # ----------------------------------------------------------

    st.title("🤖 AI Customer Support Agent")

    st.caption(
        "Production-ready AI Customer Support Assistant powered by "
        "Groq • LangChain • RAG • FAISS"
    )

    st.markdown(
        "**Developed by John Arije (johnsparz)**"
    )

    st.divider()

    # ----------------------------------------------------------
    # Welcome card
    # ----------------------------------------------------------

    if len(st.session_state.messages) == 0:

        st.info(
            """
### 👋 Welcome!

I can help you with:

- 📄 Company policies and handbook questions
- 🌍 Recent information from the web
- 🧮 Mathematical calculations
- 💬 General conversations

Use the examples in the sidebar to get started.
"""
        )

    # ----------------------------------------------------------
    # Previous conversation
    # ----------------------------------------------------------

    display_chat_history()

    # ----------------------------------------------------------
    # Chat input
    # ----------------------------------------------------------

    user_input = st.chat_input(
        "Ask about company policies, AI news, calculations..."
    )

    if not user_input:
        return

    add_message(
        "user",
        user_input,
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # ----------------------------------------------------------
    # Assistant response
    # ----------------------------------------------------------

    try:

        with st.chat_message("assistant"):

            with st.spinner(
                "🔍 Searching for the best answer..."
            ):

                response = agent.generate_response(
                    user_input
                )

                st.markdown(response)

        add_message(
            "assistant",
            response,
        )

    except Exception:

        logger.exception(
            "Application error."
        )

        error_message = (
            "Sorry, I was unable to process your request."
        )

        st.error(error_message)

        add_message(
            "assistant",
            error_message,
        )

    # ----------------------------------------------------------
    # Footer
    # ----------------------------------------------------------

    st.divider()

    current_year = datetime.now().year

    st.caption(
        f"""
Built with ❤️ using **Groq**, **LangChain**, **FAISS**, and **Streamlit**

© {current_year} John Arije (johnsparz). All rights reserved.
"""
    )

    # --------------------------------------------------------------------
# Optional UI Styling
# --------------------------------------------------------------------

st.markdown(
    """
<style>

/* Main container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 1rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    border-right: 1px solid #e6e6e6;
}

/* Chat input */
.stChatInputContainer {
    padding-top: 0.5rem;
}

/* Buttons */
button[kind="primary"] {
    border-radius: 8px;
}

/* Expander headers */
.streamlit-expanderHeader {
    font-weight: 600;
}

/* Footer spacing */
footer {
    visibility: hidden;
}

</style>
""",
    unsafe_allow_html=True,
)


# --------------------------------------------------------------------
# Entry Point
# --------------------------------------------------------------------

if __name__ == "__main__":
    main()