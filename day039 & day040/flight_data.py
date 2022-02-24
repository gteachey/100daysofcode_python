from flight_search import FlightSearch
from datetime import datetime


class FlightData():
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_searcher = FlightSearch()
        self.tequila_api_key = ""
        self.flight_searcher.tequila_api_key = self.tequila_api_key

    def get_flight_data(self, city_code, date_from, date_to):
        return self.flight_searcher.search_flights(city_code, date_from, date_to)
