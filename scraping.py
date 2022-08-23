from typing import Any

import requests
from bs4 import BeautifulSoup
from bs4.element import PageElement
from requests import Response

url = 'https://quotes.toscrape.com/'

response: Response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
html_data_quote = soup.find_all(class_='quote')
print(html_data_quote)

with open('text.txt', 'w+', encoding='utf-8') as f:
    for i in html_data_quote:
        s = f'{i.find(class_="text").get_text()} - {i.find(class_="author").get_text()}. Tags: {i.find(class_="keywords")["content"]}'
        print(s)
        f.write(s)
        f.write('\n')
