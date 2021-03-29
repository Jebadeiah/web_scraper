import requests

start_currency = input()
cache_dict = {}


def add_to_dict(end_curr):
    cache_dict[end_curr] = requests.get(f"http://www.floatrates.com/daily/{end_curr}.json").json()


add_to_dict('usd')
add_to_dict('eur')

while True:
    end_currency = input()
    if end_currency == "":
        break
    amount_of_money = round(float(input()), 2)
    print("Checking the cache...")
    if end_currency in cache_dict:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        add_to_dict(end_currency)
    print(f"You received {round((amount_of_money * (1 / float(cache_dict[end_currency][start_currency]['rate']))), 2)}"
          f" {end_currency.upper()}.")
