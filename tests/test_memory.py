from agent.memory import (
    add_ai_message,
    add_user_message,
    get_history,
)

history = []

add_user_message(history, "Hello")

add_ai_message(history, "Hi! How can I help?")

add_user_message(history, "My name is John.")

for msg in get_history(history):
    print(type(msg).__name__, msg.content)