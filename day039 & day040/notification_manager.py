import requests


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    SMS_GATEWAY_API_ENDPOINT = 'https://smschef.com/system/api/send'
    SMS_PHONE_NUMBER = '16314133679'

    def __init__(self):
        self.api_key = ""

    def send_sms(self, message):
        self.sms_gateway_api_params = {
            'key': self.api_key,
            'phone': self.SMS_PHONE_NUMBER,
            'message': message
        }
        requests.get(url=self.SMS_GATEWAY_API_ENDPOINT, params=self.sms_gateway_api_params)
