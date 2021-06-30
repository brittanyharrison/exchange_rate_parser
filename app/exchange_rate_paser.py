import json


class ExchangeRate:
    def read_rates(self):
        with open('exchange_rates.json', 'r') as file:
            data = file.read()
            print(data)

    def convert_rates(self, user_currency):
        with open('exchange_rates.json', "r") as file:
            data = file.read()
        obj = json.loads(data)
        p = obj['rates'].items()
        for key, value in p:
            if user_currency == key:
                print(f"{key} exchange rate is {value}.")



