# dialet.py

# Say "Hello, World!" using the custom openai API client.

if __name__ == "__main__":
    from openai_api import OpenAIAutoCompleteClient
    openai_api = OpenAIAutoCompleteClient(api_key="MOONSHOT_API_KEY")
    completion = openai_api.complete(prompt="Hello, World!")
    print(completion.content)
