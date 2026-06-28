#function 1

from .selectors import TITLE


def extract_title(soup):

    title = soup.select_one(TITLE)

    if title:
        return title.get_text(strip=True)

    return None

#function 2

from .selectors import CONTENT


def extract_content(soup):

    content = soup.select_one(CONTENT)

    if content:
        return content.get_text(" ", strip=True)

    return None

#function 3

from .selectors import TABLES


def extract_tables(soup):

    return soup.select(TABLES)
