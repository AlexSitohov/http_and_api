import requests
from requests import Response

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response: Response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'megageojson',
    'starttime': '2010-01-01',
    'endtime': '2020-01-01',
    'latitude': input('Широта '),
    'longitude': input('Долгота '),
    'maxradiuskm': input('Радиус '),
    'minmagnitude': input('Минимальная магнитуда ')
})
re: dict = response.json()
lst = re.get('features')

count = 0
for i in lst:
    re_pls = re.get('features')[count].get('properties')
    print(f'{count}. Магнитуда - {re_pls["mag"]}, Территория - {re_pls["place"]}')
    count += 1
