import httpx
from fetchers.base import BaseFetcher

class HTTPFetcher(BaseFetcher):

    def __init__(self, timeout: int = 30):
        self.timeout = timeout

    def fetch(self, url: str):

        response = httpx.get(
            url,
            timeout=self.timeout
        )

        response.raise_for_status()

        return response.text
