import requests
from datetime import datetime, timedelta
import config

FLIGHT_DATA_API = "https://api.tequila.kiwi.com/v2/search"
API_KEY = config.api

def tomorrow(frmt='%d/%m/%Y', string=True):
    t = datetime.now() + timedelta(1)
    if string:
        return t.strftime(frmt)
    return t

tom = tomorrow()

def six_months(frmt='%d/%m/%Y', string=True):
    t = datetime.now() + timedelta(6*30)
    if string:
        return t.strftime(frmt)
    return t
end_date = six_months()

def return_from_date(frmt='%d/%m/%Y', string=True):
    t = datetime.now() + timedelta(6*30 + 7)
    if string:
        return t.strftime(frmt)
    return t

def return_to_date(frmt='%d/%m/%Y', string=True):
    t = datetime.now() + timedelta(6*30 + 28)
    if string:
        return t.strftime(frmt)
    return t

r_to = return_to_date()
r_from = return_from_date()

class FlightData:
    def __init__(self,city_iata_code):
        self.d_from = tom
        self.d_to = end_date
        self.r_to = r_to
        self.r_from = r_from
        self.city_name = city_iata_code
        self.city_to = "LON"

    def get_price(self):
        headers = {
            "apikey": API_KEY
        }    

        flightdata_params = {
            "fly_from": self.city_name,
            "fly_to": self.city_to,
            "date_from": self.d_from,
            "date_to": self.d_to,
            "return_from": self.r_from,
            "return_to": self.r_to
        }

        response = requests.get(url=FLIGHT_DATA_API, headers=headers, params=flightdata_params)
        data = response.json()
        price = data["data"][0]["price"]
        return price

