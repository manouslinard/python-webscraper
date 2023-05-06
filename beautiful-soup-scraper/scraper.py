import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
import requests
import config

base_witcher_url = 'https://witcher.fandom.com/wiki/'

html_text = requests.get(base_witcher_url+'Category:Characters_in_the_stories').text
soup = BeautifulSoup(html_text, 'lxml')
books = soup.find_all('a', class_='category-page__member-link')
res = []
for b in books:
    # print(b.text)
    html_characters = requests.get(base_witcher_url+b.text).text
    soup_characters = BeautifulSoup(html_characters, 'lxml')
    characters = soup_characters.find_all('a', class_='category-page__member-link')
    for c in characters:
        #print(c.text)
        res.append({'title':b.text[9:-11], 'character':c.text})
    # print("====================================")
# print(res)
df = pd.DataFrame(res)
# print(df)

# create a connection to the SQLite database
conn = sqlite3.connect(config.db_name)
print('Saving Characters...')
# save the DataFrame to a table called 'witcher_characters' in the database
df.to_sql(config.table_name, conn, if_exists='replace', index=False)

# close the database connection
conn.close()
print('Database Created')
