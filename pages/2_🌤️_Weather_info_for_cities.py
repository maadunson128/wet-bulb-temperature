import streamlit as st
import math
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

        # # Printing the details
        # print(f"City: {city}")
        # print(f"Weather description: {weather_description}")
        # print(f"Wind speed: {wind_speed}m/s")
        # print(f"Temperature: {temperature}°C")
        # print(f"Relative humidity: {humidity} %")
    return temperature, humidity

# defining function to calculate wet bulb temperature
def wet_bulb_temperature(temp, humidity):
    # formula for calculating wet bulb temperature
    wet_temperature = temp * math.atan(0.151977 * math.sqrt(humidity + 8.313659)) + \
                        math.atan(temp + humidity) - math.atan(humidity - 1.676331) + \
                        0.00391838 * ((humidity) ** (3/2)) * math.atan(0.023101 * humidity) - \
                        4.686035
    
    return wet_temperature

#Live Wet bulb temperature
st.title("Live Wet Bulb Temperature")
# Enter the city name in the website provided by streamlit
city = st.text_input("Enter the city name:", placeholder ='city name')

# If city is entered , then temperature, humiidty, wet temperature are displayed.
if st.button("Get weather info"):
    temperature, humidity = fetch_data(city)

    if temperature is not None and humidity is not None:
        wet_temperature = wet_bulb_temperature(temperature, humidity)

        st.write(f"**Weather in {city}**")
        st.write(f"- Temperature: {temperature}°C")
        st.write(f"- Relative humidity: {humidity}%")
        st.write(f"- Wet bulb temperature: {wet_temperature:.2f}°C")

        # Display warnings based on wet-bulb temperatures
        if wet_temperature > 35:
            st.warning("⚠️ Wet-bulb temperatures above 35°C (95°F) pose a fatal danger to humans outside. It's extremely dangerous. Avoid direct sunlight and drink lots of water.")
        elif wet_temperature > 32:
            st.warning("⚠️ Wet-bulb temperatures above 32°C (89.6°F) are critically dangerous. Avoid direct sunlight and drink lots of water.")
        elif wet_temperature > 30:
            st.warning("⚠️ Wet-bulb temperatures above 30°C (86°F) pose potential fatal danger to humans outside. It's very uncomfortable. Avoid direct sunlight and drink lots of water.")
        else:
            st.markdown("<span style='color:green;'>Wet-bulb temperatures are within safe limits. Enjoy the weather and drink enough water to be hydrated.</span>", unsafe_allow_html=True)

st.markdown("**Data Source:**<span style='color:orange;'> OpenWeatherMap API</span> for current weather data.", unsafe_allow_html=True)