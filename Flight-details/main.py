import requests
from datetime import datetime,timedelta
from flight_search import FlightSearch
from flight_data import FlightData

SHEETY_API = "https://api.sheety.co/59d8629a5975549d3fecf8c34e5829f5/copyOfFlightDeals/prices"

response = requests.get(url=SHEETY_API)
gs_data = response.json()

sheet_data = gs_data["prices"]

for item in sheet_data:
    if item["iataCode"] == "":
        flight_search = FlightSearch(item["city"])
        iatacode_city = flight_search.return_iatacode()
        sheety_put_url = f"{SHEETY_API}/{item['id']}"
        edit_data = {
            "price" : {
                "iataCode":iatacode_city,
            }
        }
        put_response = requests.put(url=sheety_put_url, json=edit_data)
        print(put_response.text)

for item in sheet_data:
    flightdata = FlightData(item["iataCode"])
    if flightdata is None:
        continue
    else:
        flight_price = flightdata.get_price()
        print(f"{item["city"]} : {flight_price}\n")        





