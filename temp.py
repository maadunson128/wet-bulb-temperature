import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import math

# Calculate the wet bulb temperature
def calculate_wet_bulb_temperature(T, RH):
    T_w = T * math.atan(0.151977 * math.sqrt(RH + 8.313659)) + \
          math.atan(T + RH) - \
          math.atan(RH - 1.676331) + \
          0.00391838 * RH ** (3/2) * math.atan(0.023101 * RH) - \
          4.686035
    return T_w

# Load historical data
@st.cache
def load_historical_data(city):
    df = pd.read_csv(f'data/{city}_historical.csv', parse_dates=['date'])
    df['wet_bulb_temp'] = df.apply(lambda row: calculate_wet_bulb_temperature(row['temperature'], row['humidity']), axis=1)
    return df

# Streamlit app title and description
st.title("Wet Bulb Temperature Calculator and Historical Trends")
st.write("""
## Calculate the Wet Bulb Temperature for Coastal Cities in India

Enter the name of the city below to fetch the current weather data and calculate the wet bulb temperature.
""")

# Input city name for current calculation
city = st.text_input("Enter a city name:", "New Delhi,IN")

# Fetch and display weather data and wet bulb temperature
if city:
    temperature, humidity = fetch_weather(city)
    if temperature is not None and humidity is not None:
        wet_bulb_temp = calculate_wet_bulb_temperature(temperature, humidity)
        st.write(f"### Current Weather in {city}:")
        st.write(f"- **Temperature:** {temperature}°C")
        st.write(f"- **Humidity:** {humidity}%")
        st.write(f"- **Wet Bulb Temperature:** {wet_bulb_temp:.2f}°C")

        # Display warning message based on wet bulb temperature
        if wet_bulb_temp > 35:
            st.warning("⚠️ Wet-bulb temperatures above 35°C (95°F) pose a fatal danger to humans outside. It's extremely dangerous. Avoid direct sunlight and drink lots of water.")
        elif wet_bulb_temp > 32:
            st.warning("⚠️ Wet-bulb temperatures above 32°C (89.6°F) are critically dangerous. Avoid direct sunlight and drink lots of water.")
        elif wet_bulb_temp > 30:
            st.warning("⚠️ Wet-bulb temperatures above 30°C (86°F) pose potential fatal danger to humans outside. It's very uncomfortable. Avoid direct sunlight and drink lots of water.")

        # Create a Plotly figure for current weather
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[temperature], y=[wet_bulb_temp], mode='markers', name='Wet Bulb Temp'))
        fig.update_layout(title='Current Wet Bulb Temperature',
                          xaxis_title='Temperature (°C)',
                          yaxis_title='Wet Bulb Temperature (°C)')
        st.plotly_chart(fig)

# Section for historical data
st.write("## Historical Wet Bulb Temperature Trends")

# Dropdown for selecting a city for historical data
cities = ["Ahmedabad", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai"]
selected_city = st.selectbox("Select a city to view historical data:", cities)

# Load and display historical data
if selected_city:
    historical_data = load_historical_data(selected_city)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=historical_data['date'], y=historical_data['wet_bulb_temp'], mode='lines', name='Wet Bulb Temp'))
    fig.add_hline(y=32, line_dash="dash", line_color="red", annotation_text="Exceedingly harmful", annotation_position="top right")
    fig.update_layout(title=f'Historical Wet Bulb Temperature for {selected_city}',
                      xaxis_title='Date',
                      yaxis_title='Wet Bulb Temperature (°C)')
    st.plotly_chart(fig)
