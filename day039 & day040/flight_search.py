import json
import os

import requests

TEQUILA_API_SEARCH_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'
TEQUILA_API_LOCATIONS_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'


# https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021
class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.tequila_api_key = ""

    def get_iata_codes(self, term):
        locations_params = {
            'term': term,
            'location_types': 'city',
            'limit': 1
        }
        headers = {
            'apikey': self.tequila_api_key
        }
        response = requests.get(url=TEQUILA_API_LOCATIONS_ENDPOINT, params=locations_params, headers=headers)
        # print(response.json())
        return response.json()['locations'][0]['code']

    def search_flights(self, iata_code, date_from, date_to):
        headers = {
            'apikey': self.tequila_api_key
        }
        search_params = {
            'fly_from': 'CLT',
            'fly_to': iata_code,
            'dateFrom': date_from,
            'dateTo': date_to,
            'one_for_city': 1,
            'nights_in_dst_from': 4,
            'nights_in_dst_to': 14,
            'max_stopovers': 0,
            'flight_type': 'round'
        }
        response = requests.get(url=TEQUILA_API_SEARCH_ENDPOINT, headers=headers, params=search_params)
        response.raise_for_status()
        # print(response.text)
        return response.json()
