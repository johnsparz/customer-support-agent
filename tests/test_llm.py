"""
Simple connectivity test for the configured LLM.
"""

from agent.llm import get_llm


def main():

    llm = get_llm()

    response = llm.invoke(
        "Reply with exactly: LLM connection successful."
    )

    print(response.content)


if __name__ == "__main__":
    main()