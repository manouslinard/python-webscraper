## Repository Description:
This is a repo with selenium and beautiful soup that webscrapes the characters and the books they appear in from the [witcher wiki fandom page](https://witcher.fandom.com/wiki/Witcher_Wiki). To test out the selenium, go to the selenium-scraper folder, else to test beautiful soup go to beautiful-soup-scraper folder. Then follow the rest of README as shown below:

---
## Prerequisites:
It is recommended to use a venv in python. To do so, run the following in the root project folder (python-webscraper):
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
# Web-scrapers

To use the web-scraper of your liking, navigate to the correct folder, and run the following:

---
## Execution:
To use the scraper (saves also to db), run:
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
To config a db and the table of reference, go to config.py of the wanted scraper's folder and change them to your liking.

---
## Tutorials Followed:
* [Thu Vu data analytics](https://www.youtube.com/watch?v=RuNolAh_4bU&ab_channel=ThuVudataanalytics)
* [FreeCodeCamp](https://www.youtube.com/watch?v=XVv6mJpFOb0&t=516s&ab_channel=freeCodeCamp.org)
