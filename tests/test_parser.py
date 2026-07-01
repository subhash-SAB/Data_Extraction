from fetchers.http import HTTPFetcher
from parsers.html_parser import HTMLParser

fetcher = HTTPFetcher()
parser = HTMLParser()

url = "https://books.toscrape.com/"

html = fetcher.fetch(url)

soup = parser.parse(html)

print(type(soup))
print(soup.title)
print(soup.title.text) # type: ignore
