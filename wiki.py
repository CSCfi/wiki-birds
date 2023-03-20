"""
Script that help you to get information from a bird's file.
It will reach Wikipedia (FI) to retrieve:
- If Page exists
- Title
- URL
- Image URL

The output will be exported into a file named bird_species_array.json
"""
import sys
import json
import wikipediaapi
import requests
import regex


from bs4 import BeautifulSoup
from pathlib import Path

bird_filename = input("Enter the name of your file (must be in the same directory as the script): ")

BASE_DIR = Path(__file__).resolve().parent
LIST_IN_PATH = BASE_DIR / bird_filename
LIST_OUT_PATH = BASE_DIR / "bird_species_array.json"

wiki_wiki = wikipediaapi.Wikipedia('fi')
birdsArray = []

try:
    if LIST_IN_PATH.exists():
        with open(LIST_IN_PATH, "r", encoding="utf-8") as f_in:
            LIST = json.load(f_in)
    else:
        sys.exit(f"Error: file '{bird_filename}' not found")

    # Get info from our json file
    for birds in LIST:
        print(f"Searching: {birds}")
        page_py = wiki_wiki.page(birds)
        title = page_py.title
        url = page_py.fullurl

        # Let's make the soup
        # Query website and return html page
        page = requests.get(page_py.fullurl, timeout= 10).text
        # Parse html using BeautifulSoup
        soup = BeautifulSoup(page, 'html.parser')

        # Loop to find image from the infobox
        # Stop it when found the img files. Regex to exclude svg files
        for raw_img in soup.find_all('img'):
            image_lnk = raw_img.get('src')
            if regex.search('wikipedia/.*/thumb', image_lnk) and not regex.search('.svg', image_lnk):
                IMAGE_URL = "https:" + image_lnk
                break
            IMAGE_URL = "Not found"

        # Gathering data and append it to birdsArray
        data = {birds:{"URL": url, "Image URL": IMAGE_URL}}
        birdsArray.append(data)

    # Dump data to a new .json file
    with open(LIST_OUT_PATH, "w", encoding="utf-8") as f_out:
        json.dump(birdsArray, f_out, indent=4)

    # End of process
    sys.exit("Process completed")

except IsADirectoryError:
    print("Error: Filename missing")
    