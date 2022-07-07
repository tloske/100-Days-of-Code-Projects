import requests
import json
import smtplib
import os

EMAIL = "test@email.com"
EMAIL_PASSWORD = os.env.get("GMAIL_APP_PW")

API_KEY = os.env.get("OWM_API_KEY")
LAT = 52.3167
LON = 7.1667
parameters = {"appid": API_KEY,
              "lat": LAT,
              "lon": LON,
              "exclude": "current,minutely,daily"}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

data = response.json()

data = data["hourly"][:12]

for hour in data:
    if hour["weather"][0]["id"] < 700:
        with smtplib.SMTP("smtp.gmail.com", 587) as conn:
            conn.starttls()
            conn.login(EMAIL, EMAIL_PASSWORD)
            conn.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                          msg="Subject:Rain\n\nIt's going to rain today. Remember to brin an umbrella.")
        break

# with open("weather_data.json", "w") as file:
#     json.dump(data, file, indent=4)
