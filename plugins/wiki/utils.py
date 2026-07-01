# plugins/wikipedia/utils.py

from urllib.parse import urljoin


def clean_text(text: str) -> str:
    """
    Remove extra spaces, tabs and newlines.
    """
    if not text:
        return ""

    return " ".join(text.split())


def normalize_whitespace(text: str) -> str:
    """
    Normalize all whitespace characters.
    """
    return " ".join(text.split())


def safe_text(element) -> str:
    """
    Safely extract text from a BeautifulSoup element.
    """
    if element is None:
        return ""

    return clean_text(element.get_text(separator=" ", strip=True))


def safe_attribute(element, attribute: str) -> str:
    """
    Safely read an HTML attribute.
    """
    if element is None:
        return ""

    return element.get(attribute, "")


def absolute_url(base_url: str, url: str) -> str:
    """
    Convert relative URL into absolute URL.
    """
    if not url:
        return ""

    return urljoin(base_url, url)


def unique(items: list) -> list:
    """
    Remove duplicates while preserving order.
    """
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result
