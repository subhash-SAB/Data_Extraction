from fetchers.http import HTTPFetcher
from parsers.html_parser import HTMLParser

fetcher = HTTPFetcher()
parser = HTMLParser()

html = fetcher.fetch(
    "https://books.toscrape.com/"
)

soup = parser.parse(html)

title = soup.select_one("title")

print(title.text) # type: ignore
