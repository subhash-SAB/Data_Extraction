from CORE.engine import ExtractionEngine
from CORE.registry import PluginRegistry
from CORE.router import Router

from fetchers.http import HTTPFetcher
from parsers.html_parser import HTMLParser

from plugins.wiki.extractor import WikipediaExtractor
from plugins.books.extractor import BooksExtractor



def build_engine():

    fetcher = HTTPFetcher()

    parser = HTMLParser()

    wikipedia = WikipediaExtractor(
        fetcher=fetcher,
        parser=parser
    )

    books = BooksExtractor(
         fetcher=fetcher,
         parser=parser
    )

    


    registry = PluginRegistry()

    registry.register(books)
    
    registry.register(wikipedia)

    router = Router(registry)

    engine = ExtractionEngine(router)

    return engine


if __name__ == "__main__":

    engine = build_engine()

    result = engine.extract(
        url="https://books.toscrape.com/",
        fields=[
            "title",
            "books"
        ]
    )

    print(result)
