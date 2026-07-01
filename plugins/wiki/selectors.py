# plugins/wikipedia/selectors.py
'''
TITLE_SELECTOR = "h1#firstHeading"
CONTENT_SELECTOR = "div.mw-parser-output"
TABLES = "table.wikitable"
REFERENCES = "ol.references"
HEADINGS = "span.mw-headline"
INFOBOX = "table.infobox"
IMAGES = "img"
REFERENCES = "ol.references li"
CATEGORIES = "#mw-normal-catlinks li a" 
'''

# plugins/wikipedia/selectors.py

# ==========================
# TEXT
# ==========================

TITLE = "h1#firstHeading"

SUMMARY = "div.mw-parser-output > p"

CONTENT = "div.mw-parser-output > p"

HEADINGS = "span.mw-headline"

# ==========================
# STRUCTURED DATA
# ==========================

INFOBOX = "table.infobox"

TABLES = "table.wikitable"

# ==========================
# MEDIA
# ==========================

IMAGES = "img"

# ==========================
# METADATA
# ==========================

REFERENCES = "ol.references li"

CATEGORIES = "#mw-normal-catlinks li a"

# ==========================
# LINKS
# ==========================

INTERNAL_LINKS = "a[href^='/wiki/']"

EXTERNAL_LINKS = "a.external"
