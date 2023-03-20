"""
Script that help you to get information from a bird's file or bird's name.
There are two functions:
- read_from_input
- read_from_file

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

wiki_wiki = wikipediaapi.Wikipedia('fi')

def read_from_input(bird_name):
    """
    This function can be used after an import.
    
    import wiki
    read_from_input("<bird_name>")
    """
    try:
        print(f"Searching: {bird_name}")
        page_py = wiki_wiki.page(bird_name)

        # Let's make the soup!
        # Query website and return html page
        page = requests.get(page_py.fullurl, timeout= 10).text
        # Parse html using BeautifulSoup
        soup = BeautifulSoup(page, 'html.parser')

        # Loop to find image from the infobox
        # Stop it when found the img files. Regex to exclude svg files
        for raw_img in soup.find_all('img'):
            image_lnk = raw_img.get('src')
            if regex.search('wikipedia/.*/thumb/', image_lnk) and not regex.search('.svg', image_lnk):
                image_url = image_lnk
                break
            image_url = "Not found"

        print(f"Page - Exists: {page_py.exists()}")
        print(f"Page - Title: {page_py.title}")
        print(f"Page - URL: {page_py.fullurl}")
        if image_url == image_lnk:
            print(f"Page - Image URL: https:{image_url}")
        else:
            print(f"Page - Image URL: {image_url}")
    except KeyError:
        print(f"{bird_name} seems not to be a valid name")

def read_from_file(bird_filename):
    """
    This function can be used after an import.
    
    import wiki
    read_from_file("<bird_file>")

    The file must be a JSON Object
    """
    BASE_DIR = Path(__file__).resolve().parent
    LIST_OUT_PATH = BASE_DIR / "bird_species_array.json"

    birdsArray = []
    birdFile = BASE_DIR / bird_filename

    if birdFile.exists():
        with open(birdFile, "r", encoding="utf-8") as f_in:
            LIST = json.load(f_in)
    else:
        sys.exit(f"Error, file {bird_filename} doesn't exist")

    # Get info from our json file
    for birds in LIST:
        print(f"Searching: {birds}")
        page_py = wiki_wiki.page(birds)
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
                image_url = "https:" + image_lnk
                break
            image_url = "Not found"

        # Gathering data and append it to birdsArray
        data = {birds:{"URL": url, "Image URL": image_url}}
        birdsArray.append(data)

    # Dump data to a new .json file
    with open(LIST_OUT_PATH, "w", encoding="utf-8") as f_out:
        json.dump(birdsArray, f_out, indent=4)

    # End of process
    sys.exit("Process completed")
