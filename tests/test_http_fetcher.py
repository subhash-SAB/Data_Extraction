from fetchers.http import HTTPFetcher

fetcher = HTTPFetcher()

url = "https://books.toscrape.com/"

html = fetcher.fetch(url)

print(html[:1000])
