from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

tavily_client = TavilyClient(api_key=API_KEY)
response = tavily_client.search(query="Who is the first president of Nigeria?")


class SearchEngine:
    def __init__(self, api_key: str):
        self.api_key = api_key
        if not api_key.startswith("tvly-"):
            raise ValueError("Invalid API key format.")

    def search(self, query):
        if not query:
            return {"status": "error", "message": "query cannot be empty"}
        return {
            "status": "success",
            "content": query,
            "results": []
        }

    def extract(self, url):
        return {
            "status": "success",
            "url": url,
            "content": "extracted content from the url"
        }


if __name__ == '__main__':
    # print(response['results'][0]['content'])

    search_web = SearchEngine(api_key=API_KEY)
    response = search_web.search(query="Who is the president of the united states?")
    print(response['content'])
