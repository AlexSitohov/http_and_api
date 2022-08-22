# Скрипт сохраняющий фотки котиков используя api https://thecatapi.com/
import requests
from requests import Response

url = 'https://api.thecatapi.com/v1/images/search?'
params = {
    'x-api-key': 'YOUR_API_KEY',
    'limit': '10'}
response: Response = requests.get(url, headers={'Accept': 'application/json'}, params=params)
re = response.json()
for count in range(int(params.get('limit'))):
    url = re[count].get('url')
    r = requests.get(url, stream=True)

    with open('C:\\Users\\merc\\PycharmProjects\\http and api\\photos\\' + f'{count}.jpg', 'bw') as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)
