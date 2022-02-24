import json
import os

import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# Alpha Vantage access key: WJA2U7XRUD2BC03P
# Alpha Vantage API: https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
# News API: 54e508e818b2403397f8f9cc4fad9b2e
ALPHA_VANTAGE_ACCESS_KEY = 'WJA2U7XRUD2BC03P'
alpha_vantage_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHA_VANTAGE_ACCESS_KEY
}

ALPHA_VANTAGE_URL = 'https://www.alphavantage.co/query'
file_path = "stock_data.json"
if os.path.exists(file_path) and os.stat(file_path).st_size != 0:
    with open('stock_data.json') as stock_file:
        data = json.load(stock_file)
else:
    if os.path.exists(file_path) and os.stat(file_path).st_size == 0:
        with open(file_path, mode='w') as stock_file:
            r = requests.get(ALPHA_VANTAGE_URL, alpha_vantage_params)
            json.dump(r.json(), stock_file)
            data = r.json()
    else:
        with open(file_path, mode='x') as stock_file:
            r = requests.get(ALPHA_VANTAGE_URL, alpha_vantage_params)
            json.dump(r.json(), stock_file)
            data = r.json()

from itertools import islice

print(data)
dct = data["Time Series (Daily)"]
yesterday_dict_key, day_before_dict_key = islice(dct.keys(), 2)
yesterday_values, day_before_values = islice(dct.values(), 2)
yesterday_opening_price = yesterday_values["1. open"]
day_before_closing_price = day_before_values["4. close"]
print(yesterday_dict_key, day_before_dict_key, yesterday_opening_price, day_before_closing_price)

NEWS_API_KEY = '54e508e818b2403397f8f9cc4fad9b2e'
NEWS_API_URL = 'https://newsapi.org/v2/everything'
NEWS_API_PARAMS = {
    'qInTitle': COMPANY_NAME,
    'from': day_before_dict_key,
    'sortBy': 'popularity',
    'apiKey': NEWS_API_KEY
}

y_o_p = float(yesterday_opening_price)
d_b_c_p = float(day_before_closing_price)
# STEP 2: Use https://newsapi.org
# Get the first 3 news pieces for the COMPANY_NAME.
r = requests.get(NEWS_API_URL, NEWS_API_PARAMS)
data = r.json()

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
account_sid = 'ACea5d472bd55dd339918decf7bbabe3c2'
TWILLIO_AUTH_TOKN = os.environ.get("TWILLIO_AUTH_TOKEN")
percentage = ((y_o_p - d_b_c_p) / d_b_c_p) * 100

company_articles = ""
print(data["articles"][:3])
for article in data["articles"][:3]:
    company_articles += f"Headline: {article['title']}\nBrief: {article['description']}\n\n"

if percentage > 0:
    formatted_percentage = f"🔺{percentage:.2f}"
else:
    formatted_percentage = f"🔻{abs(percentage):.2f}"
sms_message = f"{STOCK}: {formatted_percentage}\n\n{company_articles}"
print(sms_message)

client = Client(account_sid, TWILLIO_AUTH_TOKN)
message = client.messages.create(
    body=f"{sms_message}",
    from_='+14012510013',
    to='+16314133679'
)
print(message.status)

# # Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
