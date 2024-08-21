import requests
import sys

API_KEY = ''
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

if len(sys.argv) != 2:
    print('Usage: python weather_fetcher.py <city>')
else:
    city = sys.argv[1]

    response = requests.get(BASE_URL, params={
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    })

    if response.status_code == 200:
        data = response.json()
        print(f'Weather in {city}: {data['weather'][0]['description']}')
        print(f'Temperature: {data['main']['temp']}°C')
    else:
        print('Error fetching weather data for', city)
