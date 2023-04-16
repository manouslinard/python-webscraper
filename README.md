## Prerequisites:
It is recommended to use a venv in python. To do so, run the following:
```
python3 -m venv ./
```
Then to activate:
```
source bin/activate
```
You can install all the requirements specified in the txt like so:
```
pip install -r requirements.txt
```
To deactivate the venv, run:
```
deactivate
```
---
## Short Description:
This is a web scraper (currently scrapes witcher wikipedia) and gets/saves all the characters of all the books to an sqlite3 db. To use the scraper (saves also to db), run:
```
python3 scraper.py
```
Also there is a simple RESTful API made with Flask, to get all the elements of the characters table.
To run the api, run:
```
python3 rest.py
```
To get all the elements, run on postman:
```
http://127.0.0.1:5000/characters
```
This will return all the characters of all the witcher books as json.

---
## Configuration:
To config a db and the table of reference, go to config.py and change them to your liking.