import pandas as pd
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import config

# create Chrome options (no tab):
options = Options()
options.add_argument('--headless')
# create Chrome service - installs chrome driver:
service = Service(ChromeDriverManager().install())
# initialise driver:
driver = webdriver.Chrome(service=service, options=options)
# go to url:
page_url = "https://witcher.fandom.com/wiki/Category:Characters_in_the_stories"
print('Opening Page...')
driver.get(page_url)

# accept cookies:
driver.find_element(By.XPATH, '//div[text()="ACCEPT"]').click()

print('Finding Books...')
contents = driver.find_elements(By.CLASS_NAME, 'category-page__member-link')
books = []
for c in contents:
    # removes unnecessary characters from title:
    books.append({'title':c.text[9:-11], 'url':c.get_attribute('href')})

print('Finding Characters...')
character_list = []
for book in books:
    driver.get(book['url'])
    characters = driver.find_elements(By.CLASS_NAME, 'category-page__member-link')
    for c in characters:
        character_list.append({'title':book['title'], 'character': c.text})

df = pd.DataFrame(character_list)

# makes graph of books with most characters appeared.
print('Drawing Plot...')
df['title'].value_counts().plot(kind='bar')
plt.show()

# create a connection to the SQLite database
conn = sqlite3.connect(config.db_name)
print('Saving Characters...')
# save the DataFrame to a table called 'witcher_characters' in the database
df.to_sql(config.table_name, conn, if_exists='replace', index=False)

# close the database connection
conn.close()
print('Database Created')
driver.quit()