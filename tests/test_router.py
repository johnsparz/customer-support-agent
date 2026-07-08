from agent.router import classify


questions = [

    "Hello!",

    "What are your business hours?",

    "What is 95 * 64?",

    "Latest AI news"

]


for q in questions:

    print(q)

    print(classify(q))

    print("-"*60)