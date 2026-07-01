# plugins/wikipedia/fields.py

from .selectors import TITLE, CONTENT, HEADINGS, IMAGES, REFERENCES, CATEGORIES
from .utils import clean_text


def extract_references(soup):

    references = []

    for reference in soup.select(REFERENCES):

        references.append(
            clean_text(
                reference.get_text(" ")
            )
        )

    return references

def extract_categories(soup):

    categories = []

    for category in soup.select(CATEGORIES):

        categories.append(
            clean_text(category.get_text())
        )

    return categories

def extract_images(soup):

    images = []

    for image in soup.select(IMAGES):

        src = image.get("src")

        if src:

            images.append(src)

    return images

def extract_title(soup):

    title = soup.select_one(TITLE)

    if title is None:
        return None

    return clean_text(title.get_text())

def extract_summary(soup):

    paragraphs = soup.select(CONTENT)

    if not paragraphs:
        return None

    return clean_text(
        paragraphs[0].get_text()
    )


def extract_content(soup):

    paragraphs = soup.select(CONTENT)

    content = []

    for paragraph in paragraphs:

        text = clean_text(
            paragraph.get_text()
        )

        if text:
            content.append(text)

    return content


def extract_headings(soup):

    headings = []

    for heading in soup.select(HEADINGS):

        headings.append(
            clean_text(
                heading.get_text()
            )
        )

    return headings
