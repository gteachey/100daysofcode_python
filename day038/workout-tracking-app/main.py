import datetime

import requests

NUTRITIONIX_APP_KEY = '891df0b1d1853c7f7ae65f7d4c3d6d78'
NUTRITIONIX_APP_ID = '4359f4f2'
NUTRITIONIX_API_EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_API_ENDPOINT = 'https://api.sheety.co/4912be90a27686848d17f047102527cc/workoutTracker/workouts'
SHEETY_BEARER_TOKEN = 'Bearer aFDFfdMCo452twt3y54h436h3753jj3h3k75k7oOKC8cCCCCCCCCid92'
SHEETY_HEADERS = {
    "Authorization": SHEETY_BEARER_TOKEN
}
HEADERS = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_APP_KEY
}


def add_workouts(query):
    nutritionix_exercise_params = {
        "query": query,
        "gender": "male",
        "weight_kg": 118.84,
        "height_cm": 182.88,
        "age": 40
    }
    response = requests.post(url=NUTRITIONIX_API_EXERCISE_ENDPOINT, json=nutritionix_exercise_params, headers=HEADERS)
    response.raise_for_status()
    # print(response.text)
    for exercise in response.json()['exercises']:
        sheety_json = {
            "workout": {
                "date": datetime.datetime.now().strftime('%d/%m/%Y'),
                "time": datetime.datetime.now().strftime('%H:%M:%S'),
                "exercise": exercise['name'].title(),
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories'],
            }
        }
        sheety_response = requests.post(url=SHEETY_API_ENDPOINT, json=sheety_json, headers=SHEETY_HEADERS)
        sheety_response.raise_for_status()
        print(sheety_response.text)


user_input = input("Tell me which exercises you did: ")
add_workouts(user_input)
