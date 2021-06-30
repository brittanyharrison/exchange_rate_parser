from app.exchange_rate_paser import ExchangeRate

user_currency = input("What currency exchange rate would you like to view?")
currency = ExchangeRate()
currency.read_rates()
currency.convert_rates(user_currency)
