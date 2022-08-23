import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(url)
re = response.json()
all_valute = re.get('Valute')


def currency_converter(valute_from, valute_in, count_of):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    response = requests.get(url)
    re = response.json()
    valute_from_course = float(re.get('Valute').get(valute_from).get('Value'))
    valute_in_course = float(re.get('Valute').get(valute_in).get('Value'))
    return f'Расчет на {re.get("Date")}. Вы получите - {round((valute_from_course / valute_in_course) * count_of, 2)} {valute_in}'


print([*all_valute.keys()])
valute_from = input('Введите валюту которую надо поменять - ').upper()
count_of = int(input('Введите количество валюты которой надо поменять - '))
valute_in = input('Введите валюту которую надо получить  - ').upper()
print(currency_converter(valute_from, valute_in, count_of))
