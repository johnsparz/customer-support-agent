# Makes the utils directory a Python package.from rag.retriever import retrieve_context


def main():

    question = "What are the business hours?"

    context = retrieve_context(question)

    print("=" * 80)

    print(context)

    print("=" * 80)


if __name__ == "__main__":
    main()