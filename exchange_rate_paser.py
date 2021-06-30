import json

with open('exchange_rates.json', 'r') as file:
    data = file.read()
    print(data)

obj = json.loads(data)
user_currency = input("Enter the country currency code to see exchange rate:")
for x,y in obj['rates']:
    if x == user_currency:
        print(x,y)

#print(f"{user_currency} exchange rate is {x.keys}")
