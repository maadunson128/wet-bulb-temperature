# importing libraries
import requests
import math

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
    response = requests.get(base_url, params)

    # check for request code 200 (it means request was successful)
    if response.status_code == 200:
        # storimg the response (Json format )
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
    return temperature, humidity
# fetching the data for chennai
temperature, humidity = fetch_data('chennai')

# defining function to calculate wet bulb temperature
def wet_bulb_temperature(temp, humidity):
    # formula for calculating wet bulb temperature
    wet_temperature = temp * math.atan(0.151977 * math.sqrt(humidity + 8.313659)) + \
                        math.atan(temp + humidity) - math.atan(humidity - 1.676331) + \
                        0.00391838 * ((humidity) ** (3/2)) * math.atan(0.023101 * humidity) - \
                        4.686035
    
    return wet_temperature

wet_temperature = wet_bulb_temperature(temperature, humidity)

print(f"Wet bulb temperature: {round(wet_temperature, 2)}°C")