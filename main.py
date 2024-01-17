from supersaver import SuperSaver
from json import loads, dumps

YOUR_CITY_NAME = "Nyon"

instance = SuperSaver()
json_data = instance.getTravels(YOUR_CITY_NAME)

str_formated_offers = dumps(json_data, indent=2)

print(str_formated_offers)



