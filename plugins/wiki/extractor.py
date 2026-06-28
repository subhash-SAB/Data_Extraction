from plugins.base import BaseExtractor


class WikipediaExtractor(BaseExtractor):

    def name(self) -> str:
        return "WikipediaExtractor"

    def supports(self, url: str) -> bool:
        return "wikipedia.org" in url.lower()

    def strategy(self) -> str:
        return "STATIC_HTML"

    def supported_fields(self) -> list[str]:
        return [
            "title",
            "content",
            "references",
            "tables"
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

        return {
            "url": url,
            "requested_fields": fields,
            "message": "Wikipedia extractor is working."
        }
