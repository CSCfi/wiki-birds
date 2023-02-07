import wikipediaapi
import sys
import requests
import regex

from bs4 import BeautifulSoup

wiki_wiki = wikipediaapi.Wikipedia('fi')

try:
    # Get info for our bird
    bird = sys.argv[1]
    print(f"Searching: {bird}")
    page_py = wiki_wiki.page(bird)

    # Let's make the soup!
    # Query website and return html page
    page = requests.get(page_py.fullurl).text
    # Parse html using BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')

    # Loop to find image from the infobox
    # Stop it when found the img files. Regex to exclude svg files
    for raw_img in soup.find_all('img'):
        image_lnk = raw_img.get('src')
        if regex.search('wikipedia/.*/thumb/', image_lnk) and not regex.search('.svg', image_lnk):
            image_url = image_lnk
            break

    print(f"Page - Exists: {page_py.exists()}")
    print(f"Page - Title: {page_py.title}")
    print(f"Page - URL: {page_py.fullurl}")
    print(f"Page - Image URL: https:{image_url}")

except IndexError:
    print("Missing bird's name as argument")