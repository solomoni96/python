import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_BASE = os.getenv("API_BASE")

def get_current_weather():
    print('\n**** Check the weather conditions in a city ***\n')
    
    city = input('\nWhich city: ')

    weather_data = requests.get(API_BASE, params={
        'appid': API_KEY, 'q': city, 'units': 'imperial'
    }).json()
    
    
    print(f"\nCurrent weather in {weather_data['name']}")
    print(f"Temperature is {weather_data['main']['temp']}")
    print(f"{weather_data['weather'][0]['description'].capitalize()} and feels like {weather_data['main']['feels_like']}.")


if __name__ == "__main__":
    get_current_weather()
