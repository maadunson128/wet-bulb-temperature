# Importing libraries
import plotly.graph_objects as go
import streamlit as st
import pandas as pd


cities = ['Kolkatta', 'Bhubaneswar','Visakhapatnam','Vijayawada','Chennai','Puducherry','Tuticorin','Thiruvananthapuram','Cochin','Calicut','Mangalore','Goa','Mumbai','Surat','Portbandar','Bhuj','Bhaunagar','Rajahmundry','Tirupati','Kannur']

# User can select or enter the city name.
st.title("Historical data visualisation")
st.markdown("**Data Source:<span style='color:orange;'>https://mesonet.agron.iastate.edu/request/download.phtml</span> for historical data**", unsafe_allow_html=True)
st.write("Enter or select the city to see the historical data plots.")

selected_city = st.selectbox("Select a city", cities)

# Defining a function to load the csv of selected city to a dataframe
@st.cache_data
def load_historical_data(city):
    df = pd.read_csv(f"data/{city}_historical.csv", parse_dates = ['valid'])
    return df

@st.cache_data
def load_hourly_averages(city):
    file_path = f'data/{city}_hourly_averages.csv'
    return pd.read_csv(file_path)

# If any city is selcted, plot the historical data for that city
if selected_city:
    data_history = load_historical_data(selected_city)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = data_history['valid'], y = data_history['wet_bulb_temp'], mode = 'lines',name = 'wet_bulb_temp'))
    fig.add_hline(y = 30, line_dash = 'dash', line_color = 'green', annotation_text = 'Nearly harmful', annotation_position = 'top right')
    fig.add_hline(y = 32, line_dash = 'dash', line_color = 'yellow', annotation_text = 'Exceedingly harmful', annotation_position = 'top right')
    fig.add_hline(y = 35, line_dash = 'dash', line_color = 'red', annotation_text = 'Critical Threshold', annotation_position = 'top right')
    fig.update_layout(title=f'Historical Wet Bulb Temperature for {selected_city}',
                      xaxis_title='Date',
                      yaxis_title='Wet Bulb Temperature (°C)')
    st.plotly_chart(fig)

    st.title('Hourly Wet-Bulb Temperature Averages')


    # Load and display the data
    hourly_avg = load_hourly_averages(selected_city)
    # st.write(f'Hourly Wet-Bulb Temperature Averages for {selected_city}')
    # st.line_chart(hourly_avg.set_index('hour'))

     # Create a plotly figure for the hourly averages
    fig_hourly = go.Figure()
    fig_hourly.add_trace(go.Scatter(x=hourly_avg['hour'], y=hourly_avg['wet_bulb_temp'], mode='lines', name='Wet Bulb Temp'))
    fig_hourly.update_layout(title=f'Hourly Wet Bulb Temperature Averages for {selected_city}',
                             xaxis_title='Hour (GMT)',
                             yaxis_title='Wet Bulb Temperature (°C)')
    st.plotly_chart(fig_hourly)

    # Display the raw data
    st.write('Raw Data')
    hourly_avg_new = hourly_avg.rename(columns={'hour':'Hour (GMT)', 'wet_bulb_temp': 'Wet bulb temperature (°C)'})
    st.write(hourly_avg_new)



