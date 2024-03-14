import requests
import os
from datetime import datetime 
from dotenv import load_dotenv, dotenv_values
import json
import config

load_dotenv()

APP_ID = config.APP_ID
API_KEY = config.API_KEY
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
AGE = 21
HEIGHT = 181
WEIGHT = 57
SHEETY_URL = "https://api.sheety.co/59d8629a5975549d3fecf8c34e5829f5/myWorkouts/sheet1"


user_input = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

excerise_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=URL, json= excerise_params, headers=headers)
response.raise_for_status()
data = response.json()

def today(frmt='%d/%m/%Y', string=True):
    t = datetime.now()
    if string:
        return t.strftime(frmt)
    return t

ty = today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

for exercise in data["exercises"]:
    new_data = {
        "sheet1": {
            "date": ty,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

new_response = requests.post(url=SHEETY_URL, json= new_data)




