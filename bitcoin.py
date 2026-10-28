#use sys and request
import sys
import requests
#exactly one command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
#text into float
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
#API adress with my API key
url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=186f1600e1c0a4f650472a0268e43a474bade3262512476c2d3fcbeb6e654c2c"
#Bitcoin data from API
try:
    response = requests.get(url)
except requests.RequestException:
    sys.exit("Could not get the Bitcoin price")
#JSON text in dictionary
content = response.json()
info = content["data"]
price = float(info["priceUsd"])
#endresult with 4 decimals 
amount = n * price
print(f"${amount:,.4f}")
