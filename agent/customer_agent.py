"""
Customer Agent.
"""

from __future__ import annotations

from langchain_core.messages import HumanMessage

from agent.llm import get_llm
from agent.memory import ConversationMemory
from agent.prompts import build_system_prompt
from agent.response import format_response
from agent.router import Router
from tools.calculator_tool import calculator
from tools.retriever_tool import retrieve_context
from tools.web_search_tool import web_search
from utils.constants import Route
from utils.logger import get_logger

logger = get_logger(__name__)


class CustomerAgent:
    """
    Main AI Customer Support Agent.
    """

    def __init__(self) -> None:
        self.llm = get_llm()
        self.memory = ConversationMemory()
        self.router = Router()

    def generate_response(self, user_input: str) -> str:
        """
        Generate an AI response.
        """

        route = self.router.classify(user_input)

        context = ""

        if route == Route.RAG:
            context = retrieve_context(user_input)

            messages = self.memory.get_messages()
            messages.insert(0, build_system_prompt(context))
            messages.append(HumanMessage(content=user_input))

            response = self.llm.invoke(messages)
            result = format_response(response.content)

        elif route == Route.CALCULATOR:
            result = calculator(user_input)

        elif route == Route.WEB:
            result = web_search(user_input)

        else:
            messages = self.memory.get_messages()
            messages.insert(0, build_system_prompt())
            messages.append(HumanMessage(content=user_input))

            response = self.llm.invoke(messages)
            result = format_response(response.content)

        # Save every interaction to memory
        self.memory.add_user_message(user_input)
        self.memory.add_ai_message(result)

        return result

        # route = self.router.classify(user_input)

        # context = ""

        # if route == Route.RAG:
        #     context = retrieve_context(user_input)

        # elif route == Route.CALCULATOR:
        #     return calculator(user_input)

        # elif route == Route.WEB:
        #     return web_search(user_input)

        # messages = self.memory.get_messages()

        # messages.insert(
        #     0,
        #     build_system_prompt(context),
        # )

        # messages.append(
        #     HumanMessage(content=user_input),
        # )

        # response = self.llm.invoke(messages)

        # answer = format_response(response.content)

        # self.memory.add_user_message(user_input)
        # self.memory.add_ai_message(answer)

        # return answer