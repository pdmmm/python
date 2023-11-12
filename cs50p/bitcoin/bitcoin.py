import json
import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py [number of bitcoins]")
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    rate = data["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("Error fetching data from CoinDesk API")

cost = bitcoins * rate

print(f"${cost:,.4f}")
