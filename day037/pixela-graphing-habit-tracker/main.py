import requests
from requests.models import Response
from datetime import date, datetime, timedelta

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = "yehcaet"
GRAPH_ID = 'onehundred'
DELETE_USER_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
DELETE_GRAPH_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

TOKEN = '21avs3avsvaea3452fsda'

HEADERS = {
    'X-USER-TOKEN': TOKEN
}


# Homepage: https://pixe.la/@yehcaet

def delete_pixela_user():
    response = requests.delete(url=DELETE_USER_ENDPOINT, headers=HEADERS)
    print(response.text)


def create_pixela_user():
    create_user_params = {
        'token': TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=create_user_params)
    print(response.text)


def delete_pixela_graph():
    response = requests.delete(url=DELETE_GRAPH_ENDPOINT, headers=HEADERS)
    print(response.text)


def create_pixela_graph():
    graph_config = {
        'id': GRAPH_ID,
        'name': "100 Days of Code Learning Graph",
        'unit': "hour",
        "type": "int",
        "color": "shibafu"
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print(response.text)


def add_pixel(year_month_day: datetime, quantity: str):
    add_pixel_params = {
        'date': year_month_day.strftime('%Y%m%d'),
        'quantity': quantity
    }
    ADD_PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'
    response = requests.post(url=ADD_PIXEL_ENDPOINT, json=add_pixel_params, headers=HEADERS)
    print(response.text)


def update_pixel(year_month_day: datetime):
    # /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
    update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{year_month_day.strftime('%Y%m%d')}"
    update_pixel_params = {
        'quantity': '6'
    }
    response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=HEADERS)
    print(response.text)


def delete_pixel(year_month_day: datetime):
    # https://pixe.la/v1/users/a-know/graphs/test-graph/20180915
    delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{year_month_day.strftime('%Y%m%d')}"
    response = requests.delete(url=delete_pixel_endpoint, headers=HEADERS)
    print(response.text)


# delete_pixel(datetime.now())
# add_pixel(datetime.now(), '6')
day = (datetime.today() - timedelta(days=1))
hours_spent = '3'
# add_pixel(day, hours_spent)

SMS_GATEWAY_API_KEY = '9ffae14f8b0d7a88e112985a4c11f3e739a818e4'
SMS_GATEWAY_API_ENDPOINT = 'https://smschef.com/system/api/send'
sms_gateway_api_params = {
    'key': SMS_GATEWAY_API_KEY,
    'phone': 16314133679,
    'message': "Test Test. I did this with what I learned in my programming course :-)"
}
# response = requests.get(url=SMS_GATEWAY_API_ENDPOINT, params=sms_gateway_api_params)
# print(response.text)

COINBASE_API_KEY = 'C0RiSJX1LGw9E2c5'
COINBASE_API_SECRET = '4y1YpNWu2o6Augz4Hbw6SNyg1uQpI4C9'

# Done! Congratulations on your new bot. You will find it at t.me/GMTCryptoBot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

# Use this token to access the HTTP API:
# 5062246006:AAFdlD4m5kVg94-FW0igXTti8oj2UHUlJz4
# Keep your token secure and store it safely, it can be used by anyone to control your bot.

# For a description of the Bot API, see this page: https://core.telegram.org/bots/api
# {"ok":true,"result":{"id":5062246006,"is_bot":true,"first_name":"GTCryptoBot","username":"GMTCryptoBot","can_join_groups":true,"can_read_all_group_messages":false,"supports_inline_queries":false}}
# {"ok":true,"result":[{"update_id":135110217,
# "message":{"message_id":2,"from":{"id":5051103386,"is_bot":false,"first_name":"Max","last_name":"Nix","language_code":"en"},"chat":{"id":5051103386,"first_name":"Max","last_name":"Nix","type":"private"},"date":1640830819,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}}]}

import requests


def telegram_bot_sendtext(bot_message):
    bot_token = '5062246006:AAFdlD4m5kVg94-FW0igXTti8oj2UHUlJz4'
    bot_chatID = '5051103386'
    send_text_api_endpoint = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    send_text_api_endpoint_params = {
        'chat_id': bot_chatID,
        'parse_mode': 'Markdown',
        'text': bot_message
    }
    response = requests.get(send_text_api_endpoint, params=send_text_api_endpoint_params)

    return response.json()


day = (datetime.today() - timedelta(days=1))
test = telegram_bot_sendtext(day.strftime("%Y/%m/%d"))
print(test)
