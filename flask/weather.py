from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_BASE = os.getenv("API_BASE")

def get_current_weather(city):
    weather_data = requests.get(API_BASE, params={
        'appid': API_KEY, 'q': city, 'units': 'imperial'
    }).json()
    
    return weather_data

if __name__ == "__main__":
    print('\n**** Check the weather conditions in a city ***\n')
    city = input('\nWhich city: ')
    
    if not bool(city.strip()):
        city="Londsdon"
    
    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)

