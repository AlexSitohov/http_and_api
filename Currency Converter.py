import requests


def currency_converter(count_of_rubles):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    response = requests.get(url)
    re = response.json()
    usd_value = int(re.get('Valute').get('USD').get('Value'))
    return f'Рубли - {count_of_rubles}. Доллары - {round(count_of_rubles / usd_value, 2)}. На - {re.get("Date")}'


count_of_rub = int(input('Введите количество рублей  - '))
print(currency_converter(count_of_rub))
