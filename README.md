# Python script to retrieve birds information from Wikipedia
This python v2 script will retrieve information from wikipedia such as Page title, URL, image URL.  
When you launch the script, it will read a file named "bird_species_id.json" (must be located as the same level as the python script) and output the result into a file named "bird_species_array.json".  
Here an example:
```
python3 wiki.py
Searching: Accipiter gentilis
Searching: Actitis hypoleucos
Searching: Alauda arvensis
Searching: Anas platyrhynchos
...
Searching: Vanellus vanellus
Process completed
```

And here, the contain of "bird_species_array.json":
```
[
    {
        "Accipiter gentilis": {
            "URL": "https://fi.wikipedia.org/wiki/Kanahaukka",
            "Image URL": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Northern_Goshawk_ad_M2.jpg/250px-Northern_Goshawk_ad_M2.jpg"
        }
    },
    {
        "Actitis hypoleucos": {
            "URL": "https://fi.wikipedia.org/wiki/Rantasipi",
            "Image URL": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Actitis_hypoleucos_a2.jpg/250px-Actitis_hypoleucos_a2.jpg"
        }
    },
    {
        "Alauda arvensis": {
            "URL": "https://fi.wikipedia.org/wiki/Kiuru",
            "Image URL": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Alauda_arvensis_2.jpg/275px-Alauda_arvensis_2.jpg"
        }
    },
    {
        "Anas platyrhynchos": {
            "URL": "https://fi.wikipedia.org/wiki/Sinisorsa",
            "Image URL": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Ducks_in_plymouth%2C_massachusetts.jpg/250px-Ducks_in_plymouth%2C_massachusetts.jpg"
        }
    },
...
    {
        "Vanellus vanellus": {
            "URL": "https://fi.wikipedia.org/wiki/T%C3%B6yht%C3%B6hyypp%C3%A4",
            "Image URL": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Northern-Lapwing-Vanellus-vanellus.jpg/250px-Northern-Lapwing-Vanellus-vanellus.jpg"
        }
    }
]
```
# How to use
## Create venv with Python
```
python3 -m venv <path>
```

## Enter into your venv
```
source bin/activate
```

## Install requirements
```
pip3 install -r requirements.txt
```