""""
This script makes API to call PokeApi
"""

import requests
from pprint import pprint

url = "https://pokeapi.co/api/v2/"

response = requests.get(url + "pokemon/ditto")
json_response =  response.json()
print(json_response)