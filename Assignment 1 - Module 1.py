#Assignment 1 - Module 1 Code
#Which use https://mhw-db.com/weapons/1 api

import requests
import json
import pprint


URL = "https://mhw-db.com/weapons/1"

response = requests.get(URL)
api_data = response.json()

#get full information of the id 1 weapon
pprint.pprint(api_data)

#get the name of the id 1 weapon
pprint.pprint(api_data.get("name"))

#get the type of the id 1 weapon
pprint.pprint(api_data.get("type"))
