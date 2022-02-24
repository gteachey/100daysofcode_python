# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the \
# program requirements.
from datetime import datetime, timedelta
from smtplib import SMTP
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import re

SMS_GATEWAY_API_KEY = '9ffae14f8b0d7a88e112985a4c11f3e739a818e4'
sheety_bearer_token = 'Bearer vsavsavJC(CS3rOC9_(%$Svsdasfasgargw**XSh'
sheety_put_endpoint = 'https://api.sheety.co/4912be90a27686848d17f047102527cc/flightDeals/prices/[Row-NUM]'
tequila_api_key = 'uuKTsdshSM-mbWL0bJ8UUYKIPmWD8X1r'

there_was_an_issue = False
data_mgr = DataManager(sheety_bearer_token)

# Make a regular expression for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check_email_address(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False


def check_iata_codes(data):
    flight_searcher = FlightSearch()
    flight_searcher.tequila_api_key = tequila_api_key
    update_dict = {}
    num = 0
    for item_dict in data['prices']:
        if item_dict['iataCode'] == '':
            item_dict['iataCode'] = flight_searcher.get_iata_codes(item_dict['city'])
            update_dict[str(num)] = item_dict
            num += 1
    # print(sheet_data)
    print(update_dict)
    return update_dict


def get_iata_codes():
    global sheet_data, missing_iata_codes, there_was_an_issue
    sheet_data = data_mgr.get_sheet_data()
    if sheet_data:
        missing_iata_codes = check_iata_codes(sheet_data)
    else:
        there_was_an_issue = True


def update_flight__price_sheet_data():
    global sheet_data, there_was_an_issue
    if not there_was_an_issue:
        data_mgr.update_sheet_data(missing_iata_codes)
        sheet_data = data_mgr.get_sheet_data()
    else:
        there_was_an_issue = True


def send_email(flight_prices):
    results = data_mgr.get_user_emails()
    email_list = results['users']
    my_email = 'gt100daysofcode@gmail.com'
    with SMTP('smtp.gmail.com') as smtp_provider:
        smtp_provider.starttls()
        smtp_provider.login(user=my_email, password='T..h7RP#tz;G[t27bC,y')
        for recipient in email_list:
            first_name = recipient['firstName']
            message = f"Subject: Get Your Bags Ready!\n\nHello {first_name},\n\nHere's your current cheap flights!\n{flight_prices}"
            print(message)
            smtp_provider.sendmail(from_addr=my_email, to_addrs=recipient['email'], msg=message)


def get_flight_prices():
    global flight_data
    flight_data = FlightData()
    flight_data.flight_searcher.tequila_api_key = tequila_api_key
    flight_price = ""
    for location in sheet_data['prices']:
        city_code = location['iataCode']
        date_from = datetime.now().strftime('%d/%m/%Y')
        date_to = (datetime.now() + timedelta(days=(6 * 365 / 12))).strftime('%d/%m/%Y')
        print(city_code)
        print(date_from)
        print(date_to)
        results = flight_data.get_flight_data(city_code, date_from, date_to)

        print(results)
        if results['data']:
            flight_details = results['data'][0]
            price = flight_details['price']

            if price < location['lowestPrice']:
                dest_city = flight_details['cityTo']
                dest_airport = flight_details['flyTo']
                my_city = flight_details['cityFrom']
                my_airport = flight_details['flyFrom']
                leave_date_time = flight_details['route'][0]['local_departure']
                return_date_time = flight_details['route'][1]['local_departure']

                convert_leave = datetime.strptime(leave_date_time, '%Y-%m-%dT%H:%M:%S.%fZ')
                convert_return = datetime.strptime(return_date_time, '%Y-%m-%dT%H:%M:%S.%fZ')

                departure_time = convert_leave.strftime('%m-%d-%Y at %H:%M')
                return_time = convert_return.strftime('%m-%d-%Y at %H:%M')

                # message = send_sms(departure_time, dest_airport, dest_city, my_airport, my_city, price, return_time)
                flight_price += f"${price} to fly from {my_city}-{my_airport}" \
                                f" to {dest_city}-{dest_airport}! " \
                                f"It leaves {departure_time} and returns {return_time}\n"

    if flight_price:
        send_email(flight_price)
        # print(message)


def send_sms(departure_time, dest_airport, dest_city, my_airport, my_city, price, return_time):
    message = f"GET YOUR BAGS! Only ${price} to fly from {my_city}-{my_airport}" \
              f" to {dest_city}-{dest_airport}! " \
              f"It leaves {departure_time} and returns {return_time}"
    notification_mgr = NotificationManager()
    notification_mgr.api_key = SMS_GATEWAY_API_KEY
    notification_mgr.send_sms(message)
    return message


get_iata_codes()
update_flight__price_sheet_data()
if not there_was_an_issue:
    get_flight_prices()

# print("Welcome! Ready to save money on your next flight?")
# first_name = ""
# while not first_name:
#     first_name = input("Enter your first name:\n")
# last_name = ""
# while not last_name:
#     last_name = input("Now enter your last name:\n")
# email = ""
# confirm_email = "1"
# while email != confirm_email:
#     email = input("Please enter your email:\n")
#     if check_email_address(email):
#         confirm_email = input("One more time on that email. Let's make sure it's right!\n")
#         if email != confirm_email:
#             print("Something's not right on that email. Please try again.\n")
#
# data_mgr.add_user_email(first_name,last_name,email)


print("Done")
