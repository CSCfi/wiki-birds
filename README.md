# Python script to retrieve birds information from Wikipedia
This python script will retrieve information from wikipedia such as Page title, URL, image URL. It also checks if the wiki page exists.  
Here an output example:
```
python3 wiki.py "Haarapääsky"
Searching: Haarapääsky
Page - Exists: True
Page - Title: Haarapääsky
Page - URL: https://fi.wikipedia.org/wiki/Haarap%C3%A4%C3%A4sky
Page - Image URL: https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Landsvale.jpg/250px-Landsvale.jpg
```

### Create venv with Python
```
python3 -m venv <path>
```

### Enter your venv
```
source bin/activate
```

### Install requirements
```
pip3 install -r requirements.txt
```