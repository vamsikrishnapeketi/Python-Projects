#check day 35 for sending the sms and everything and how to automate the code again and again

import requests
import config
api_key = config.api_key
Latitude = 13.082680
Longitude = 80.270721

parameters = {
    "lat":Latitude,
    "lon":Longitude,
    "appid":api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code > 700:
        print("Bring Umbrella")
        break