from plugins.base import BaseExtractor

from .fields import *

FIELD_EXTRACTORS = {

    "title": extract_title,

    "books": extract_books

}

class BooksExtractor(BaseExtractor):

    def name(self) -> str:
        return "Books"

    def supports(self, url: str) -> bool:
        return "books.toscrape.com" in url

    def strategy(self) -> str:
        return "STATIC_HTML"

    def supported_fields(self) -> list[str]:
        return [
            "title",
            "books"
        ]

    def required_fields(self) -> list[str]:
        return [
            "title"
        ]

    def extract(
        self,
        url: str,
        fields: list[str]
    ) -> dict:

        html = self.fetcher.fetch(url)

        soup = self.parser.parse(html)

        data = {}

        for field in fields:

            extractor = FIELD_EXTRACTORS.get(field)

            if extractor:
                data[field] = extractor(soup)

        return data
