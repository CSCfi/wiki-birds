import wikipediaapi
import sys
import requests
import regex
import json

from bs4 import BeautifulSoup
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LIST_IN_PATH = BASE_DIR / "bird_species_id.json"
LIST_OUT_PATH = BASE_DIR / "bird_species_array.json"

wiki_wiki = wikipediaapi.Wikipedia('fi')
birdsArray = []

if LIST_IN_PATH.exists():
    with open(LIST_IN_PATH, "r") as f_in:
        LIST = json.load(f_in)
else:
    sys.exit("Error, birds' list missing")

# Get info from our json file
for birds in LIST:
    print(f"Searching: {birds}")
    page_py = wiki_wiki.page(birds)
    title = page_py.title
    url = page_py.fullurl

    # Let's make the soup
    # Query website and return html page
    page = requests.get(page_py.fullurl).text
    # Parse html using BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')

    # Loop to find image from the infobox
    # Stop it when found the img files. Regex to exclude svg files
    for raw_img in soup.find_all('img'):
        image_lnk = raw_img.get('src')
        if regex.search('wikipedia/.*/thumb', image_lnk) and not regex.search('.svg', image_lnk):
            image_url = "https:" + image_lnk
            break
        else:
            image_url = "Not found"

    # Gathering data and append it to birdsArray
    data = {birds:{"URL": url, "Image URL": image_url}}
    birdsArray.append(data)

# Dump data to a new .json file
with open(LIST_OUT_PATH, "w") as f_out:
        json.dump(birdsArray, f_out, indent=4)

# End of process
sys.exit("Process completed")