# fetchers/http.py

import httpx
from fetchers.base import BaseFetcher


class HTTPFetcher(BaseFetcher):

    def __init__(self, timeout: int = 30):
        self.timeout = timeout

    def fetch(self, url: str) -> str:

        headers = {
            "User-Agent": (
                "DET-Extractor/1.0 "
                "(Educational project; Python httpx)"
            ),
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
        }

        with httpx.Client(
            headers=headers,
            timeout=self.timeout,
            follow_redirects=True,            
        ) as client:

            response = client.get(url)

            response.raise_for_status()
            print(response.status_code)
            print(response.headers)
            print(response.text[:300])

            return response.text
