import json
import os
import requests

SHEETY_ENDPOINT_URL = 'https://api.sheety.co/4912be90a27686848d17f047102527cc/flightDeals/prices'


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, sheety_bearer_token):
        self.HEADERS = {'Authorization': sheety_bearer_token}
        self.sheet_data = {}
        self.sheety_file = "sheety_data.json"

    def get_sheet_data(self):
        if os.path.exists(self.sheety_file):
            with open(self.sheety_file) as file:
                self.sheet_data = json.load(file)
        else:
            results = requests.get(url=SHEETY_ENDPOINT_URL, headers=self.HEADERS)
            with open(self.sheety_file, mode='x') as file:
                json.dump(results.json(), file)
            self.sheet_data = results.json()
        return self.sheet_data

    def update_sheet_data(self, update_sheety: dict):
        if os.path.exists(self.sheety_file):
            os.remove(self.sheety_file)
        # print(update_sheety)
        for value in update_sheety.values():
            # print(f"value:{value}")
            sheety_put_endpoint = f"https://api.sheety.co/4912be90a27686848d17f047102527cc/flightDeals/prices/{value['id']}"
            update_sheet_params = {
                'price': {
                    'iataCode': value['iataCode']
                }
            }
            response = requests.put(url=sheety_put_endpoint, headers=self.HEADERS, json=update_sheet_params)
            response.raise_for_status()
            # print(response.content)
            # print(response.text)

    def add_user_email(self, first_name, last_name, email):
        sheety_users_endpoint_url = 'https://api.sheety.co/4912be90a27686848d17f047102527cc/flightDeals/users'
        add_user_params = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }
        }
        response = requests.post(url=sheety_users_endpoint_url, json=add_user_params)
        response.raise_for_status()
        print(response.text)

    def get_user_emails(self):
        sheety_users_endpoint_url = 'https://api.sheety.co/4912be90a27686848d17f047102527cc/flightDeals/users'
        response = requests.get(url=sheety_users_endpoint_url)
        response.raise_for_status()
        print(response.text)
        return response.json()
