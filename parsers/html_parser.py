# parsers/html_parser.py

from bs4 import BeautifulSoup

from parsers.base import BaseParser


class HTMLParser(BaseParser):

    def parse(self, html: str) -> BeautifulSoup:

        return BeautifulSoup(
            html,
            "lxml"
        )
