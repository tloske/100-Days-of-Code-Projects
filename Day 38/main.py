import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""
AUTH_TOKEN = ""

excercise_endpoint = ""
sheety_endpoint = ""

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

query = input("Tell me which excercise you did: ")

parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 72,
    "height_cm": 167,
    "age": 31
}

response = requests.post(
    excercise_endpoint, headers=headers, json=parameters)
response.raise_for_status()

exercise_data = response.json()["exercises"]

date = datetime.today().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

headers = {
    "Authorization": f"Bearer {AUTH_TOKEN}"
}
for exercise in exercise_data:
    parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(sheety_endpoint, json=parameters, headers=headers)
    response.raise_for_status()
