from typing import Any

from plugins.base import BaseExtractor
from fetchers.http import HTTPFetcher
from .selectors import INFOBOX
from .utils import clean_text
from bs4 import BeautifulSoup
from parsers.html_parser import HTMLParser

try:
    from .fields import (
        extract_title, # type: ignore
        extract_content, # type: ignore
        extract_summary, # type: ignore
        extract_headings,
        extract_images,
        extract_references,
        extract_categories,
    )
except ImportError:  # pragma: no cover - fallback for minimal environments
    def extract_title(soup: BeautifulSoup) -> str:
        return ""

    def extract_content(soup: BeautifulSoup) -> str:
        return ""

    def extract_summary(soup: BeautifulSoup) -> str:
        return ""

    def extract_headings(soup: BeautifulSoup) -> list[str]:
        return []

    def extract_images(soup: BeautifulSoup) -> list[str]:
        return []

    def extract_references(soup: BeautifulSoup) -> list[str]:
        return []

    def extract_categories(soup: BeautifulSoup) -> list[str]:
        return []


class WikipediaExtractor(BaseExtractor):

    def __init__(
        self,
        fetcher: HTTPFetcher,
        parser: HTMLParser,
    ):
        self.fetcher = fetcher
        self.parser = parser

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
            "tables",
        ]

    def required_fields(self) -> list[str]:
        return ["title"]

    def extract_infobox(self, soup: BeautifulSoup) -> dict[str, str]:
        infobox = soup.select_one(INFOBOX)
        if infobox is None:
            return {}
        data: dict[str, str] = {}
        rows = infobox.select("tr")
        for row in rows:
            key = row.select_one("th")
            value = row.select_one("td")
            if key and value:
                data[clean_text(key.get_text())] = clean_text(value.get_text(" "))
        return data

    def extract(
        self,
        url: str,
        fields: list[str],
    ) -> dict[str, Any]:
        html = self.fetcher.fetch(url)
        soup = self.parser.parse(html)

        data: dict[str, Any] = {}
        field_extractors = {
            "title": extract_title,
            "summary": extract_summary,
            "content": extract_content,
            "headings": extract_headings,
            "infobox": self.extract_infobox,
            "images": extract_images,
            "references": extract_references,
            "categories": extract_categories,
        }

        for field in fields:
            extractor = field_extractors.get(field)
            if extractor is not None:
                data[field] = extractor(soup)

        return data

