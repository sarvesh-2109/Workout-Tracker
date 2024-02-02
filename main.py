import os
import requests
from datetime import datetime
import pytz

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
TOKEN = os.environ['TOKEN']

NUTRITIONIX_ENDPOINT = os.environ['NUTRITIONIX_ENDPOINT']
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-type": "application/json"
}

sheety_header = {
    "Authorization": TOKEN
}

nlp_params = {
    "query": input("Tell me which exercise you did today: ").title()
}

nlp_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nlp_params, headers=headers)

data = nlp_response.json()

exercise = data["exercises"][0]["name"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]
today = datetime.now(pytz.timezone('Asia/Kolkata'))

sheety_config = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories,
    }
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_config, headers=sheety_header)
sheety_response.raise_for_status()


