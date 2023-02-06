import wikipediaapi
import sys

from bs4 import BeautifulSoup

wiki_wiki = wikipediaapi.Wikipedia('fi')

if len(sys.argv) != 2:
    sys.exit("Missing bird's name as argument")
else:
    bird = sys.argv[1]
    print("Searching: %s" % bird)
    page_py = wiki_wiki.page(bird)

    print("Page - Exists: %s" % page_py.exists())
    print("Page - Title: %s" % page_py.title)
    print("Page - URL: %s" % page_py.fullurl)
