import wikipediaapi
import sys
import requests

from bs4 import BeautifulSoup

wiki_wiki = wikipediaapi.Wikipedia('fi')

if len(sys.argv) != 2:
    sys.exit("Missing bird's name as argument")
else:
    # Get info for our bird
    bird = sys.argv[1]
    print("Searching: %s" % bird)
    page_py = wiki_wiki.page(bird)

    # Let's make the soup!
    page = requests.get(page_py.fullurl).text
    soup = BeautifulSoup(page, 'html.parser')

    for raw_img in soup.find_all('img'):
        image = raw_img.get('src')
        break

    print(f"Page - Exists: {page_py.exists()}")
    print(f"Page - Title: {page_py.title}")
    print(f"Page - URL: {page_py.fullurl}")
    print(f"Page - Image URL: {image}")
