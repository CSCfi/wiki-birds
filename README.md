# Python script to retrieve birds information from Wikipedia
## Pre requisites
You need to install the requirements.txt. It's always good to use a virtual environment. You can proceed with this command:  
```py
python3 -m venv .venv
```
Enter into your virtual environment:  
```py
source .venv/bin/activate
```
And then install the requirements:  
```py
pip3 install -r requirements.txt
```

## How to use
This v3 version has two functions:  
- read_from_input()
- read_from_file()

For the function **read_from_input()** you have to specify the name of the bird you want to retrieve information. (read_from_input(<"birdName">)).  
For the function **read_from_file()**, you have to specify the name of the bird file. Should be a JSON Object file. (read_from_file(<"birdFilename">)).  

When you use python, you can import the python script **wiki** and call the desired function.  
Here is some examples:  
```py
python3
>>> import wiki
>>> wiki.read_from_input("Accipiter gentilis")
Searching: Accipiter gentilis
Page - Exists: True
Page - Title: Kanahaukka
Page - URL: https://fi.wikipedia.org/wiki/Kanahaukka
Page - Image URL: https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Northern_Goshawk_ad_M2.jpg/250px-Northern_Goshawk_ad_M2.jpg
```
or read from a JSON Object file:
```py
python3
>>> import wiki
>>> wiki.read_from_file("bird_species_id.json")
Searching: Accipiter gentilis
Searching: Actitis hypoleucos
Searching: Alauda arvensis
Searching: Anas platyrhynchos
...
Searching: Vanellus vanellus
Process completed
```
You'll find the output into a file called **bird_species_array.json**
