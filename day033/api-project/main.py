from smtplib import SMTP

import requests
import datetime

#
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
#
iss_longitude = float(data['iss_position']['longitude'])
iss_latitude = float(data['iss_position']['latitude'])
MY_LONG = float(-80.646610)
MY_LAT = float(35.181250)

# SMTP stuff
smtp_provider = "smtp.gmail.com"
username = "gt100daysofcode@gmail.com"
password = "T..h7RP#tz;G[t27bC,y"

# position + or - 5
if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and \
        (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    time_now = datetime.datetime.now(datetime.timezone.utc)
    hour = time_now.hour

    message = f"To:gteachey@outlook.com\n" \
              f"Subject:The ISS is in the area!\n\n" \
              f"Go Outside to see it!"
    if hour >= sunset_hour or hour <= sunrise_hour:
        with SMTP(smtp_provider) as smtp:
            smtp.starttls()
            smtp.login(user=username, password=password)
            smtp.sendmail(from_addr=username, to_addrs="gteachey@outlook.com", msg=message)
