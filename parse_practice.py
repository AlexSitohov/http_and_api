import requests
from bs4 import BeautifulSoup

page = input()
print(f'Страница - {page} \n')
url = f'https://v2.vost.pw/page/{page}/'
response = requests.get(url=url).text
bs = BeautifulSoup(response, 'html.parser')
data = bs.find_all(class_='shortstory')
for i in data:
    print(i.find(class_='current-rating1').get_text(), i.find('a').get_text(),  i.find('a')['href'], '\n')


