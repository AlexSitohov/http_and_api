import requests
from requests import Response

responce: Response = requests.get('https://www.youtube.com')

print(responce.url)
