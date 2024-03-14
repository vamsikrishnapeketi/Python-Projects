import requests
import config

FLIGHT_IATA_API = "https://api.tequila.kiwi.com/locations/query"
API_KEY = config.api

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,city_name):
        self.iatacode = ""
        self.city_name = city_name    

    def return_iatacode(self):
        headers = {
            "apikey": API_KEY
        }
        iata_code_params = {
            "term": self.city_name,
            "locale": "en-US",
            "location_types": "airport"
        }
        response = requests.get(url=FLIGHT_IATA_API, headers=headers, params=iata_code_params)
        new_data = response.json()
        self.iatacode = new_data["locations"][0]["city"]["code"] 
        return self.iatacode   