from .selectors import *
from .utils import clean_text


def extract_title(soup):

    title = soup.select_one(TITLE)

    if title:
        return clean_text(title.text)

    return ""


def extract_books(soup):

    books = []

    for item in soup.select(BOOKS):

        name = item.select_one(BOOK_TITLE)

        price = item.select_one(PRICE)

        rating = item.select_one(RATING)

        availability = item.select_one(AVAILABILITY)

        image = item.select_one(IMAGE)

        books.append({

            "title":
                clean_text(name["title"]) if name else "",

            "price":
                clean_text(price.text) if price else "",

            "rating":
                rating["class"][-1] if rating else "",

            "availability":
                clean_text(availability.text)
                if availability else "",

            "image":
                image["src"] if image else ""

        })

    return books
