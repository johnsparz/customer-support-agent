from tools.web_search_tool import web_search

print("=" * 80)

print(
    web_search(
        "Latest developments in artificial intelligence",
        news=True,
    )
)

print("=" * 80)