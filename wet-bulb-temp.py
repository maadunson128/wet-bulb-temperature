# importing library 
import requests

# Defining function to fetch the data using API
def fetch_data(city):
    # api key for OpenWeather API
    api_key = 'db6369f70933e38a8ae19cf30c6a5c95' 

    # base url for OpenWeather API website
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    # parameters for API request
    params = {
        'q' : city,
        'appid': api_key,
        'units' : 'metric' #unit for temperature -> metric for celsius

    }
    # Getting response using GET HTTP method
    response = requests.get(base_url, params=params)

    # check for request code 200 (it means request was successful)
    if response.status_code == 200:
        # converting the response into Json format
        data = response.json()

        # storing the required details
        weather_description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        # Printing the details
        print(f"City: {city}")
        print(f"Weather description: {weather_description}")
        print(f"Wind speed: {wind_speed}m/s")
        print(f"Temperature: {temperature}°C")
        print(f"Relative humidity: {humidity} %")

# fetching the data for salem
fetch_data('taramangalam')