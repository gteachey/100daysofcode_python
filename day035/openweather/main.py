import json
import os
from datetime import datetime
import time
import requests
from twilio.rest import Client

# rl: https://api.openweathermap.org/data/2.5/onecall?lat=35.2271&lon=-80.8431&exclude=current%2Cminutely%2Cdaily

# Twillio phone number = +14012510013
# TWILLIO_AUTH_TOKEN = 2c2e8b25cf04b15509bfebff4c13185b
# OWM_API_KEY = "6df789d9f4461d400321a5dff08c3940"
owm_api_key = os.environ.get("OWM_API_KEY")
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
#
account_sid = 'ACea5d472bd55dd339918decf7bbabe3c2'
TWILLIO_AUTH_TOKN = os.environ.get("TWILLIO_AUTH_TOKEN")


def get_48_hourly_forecast():
    try:

        with open("weather_data.json", mode='r') as weather_data_file:
            weather_data = json.load(weather_data_file)
    except FileNotFoundError:

        weather_params = {
            'lat': 35.2271,
            'lon': -80.8431,
            'appid': owm_api_key,
            'exclude': 'current,minutely,daily'
        }
        response = requests.get(OWM_ENDPOINT, params=weather_params)
        response.raise_for_status()
        weather_data = response.json()
        print(weather_data)
        with open("weather_data.json", mode='x') as weather_data_file:
            json.dump(weather_data, weather_data_file)
    output = ""
    for num in range(0, 12):
        get_time = datetime.utcfromtimestamp(weather_data['hourly'][num]['dt'])
        unix_epoch = time.mktime(get_time.timetuple())
        offset = datetime.fromtimestamp(unix_epoch) - datetime.utcfromtimestamp(unix_epoch)
        local_dt = get_time + offset
        weather_id = weather_data['hourly'][num]['weather'][0]['id']

        if weather_id < 700:
            output += f"Rain expected at: {local_dt}\n"

    if output != "":
        client = Client(account_sid, TWILLIO_AUTH_TOKN)
        message = client.messages.create(
            body=f"{output}",
            from_='+14012510013',
            to='+16314133679'
        )
        print(message.status)

    print(output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_48_hourly_forecast()
