import streamlit as st
import math

# defining function to calculate wet bulb temperature
def wet_bulb_temperature(temp, humidity):
    # formula for calculating wet bulb temperature
    wet_temperature = temp * math.atan(0.151977 * math.sqrt(humidity + 8.313659)) + \
                        math.atan(temp + humidity) - math.atan(humidity - 1.676331) + \
                        0.00391838 * ((humidity) ** (3/2)) * math.atan(0.023101 * humidity) - \
                        4.686035
    
    return wet_temperature




# Wet-bulb temperature calculator
st.title("Wet bulb temperature calculator")
temperature_input = st.number_input("Temperature(°C): ", placeholder= "Enter 32 for 32°C ", value= None)
humidity_input = st.number_input("Relative Humidity(%) :", placeholder = "Enter 77 for 77%", value= None)

if st.button("Calculate"):
    calculated_wet_temperature = wet_bulb_temperature(temperature_input, humidity_input)
    st.write(f"Wet bulb temperature: {calculated_wet_temperature:.2f}°C")


    if calculated_wet_temperature > 35:
        st.warning("⚠️ Wet-bulb temperatures above 35°C (95°F) pose a fatal danger to humans outside. It's extremely dangerous. Avoid direct sunlight and drink lots of water.")
    elif calculated_wet_temperature > 32:
        st.warning("⚠️ Wet-bulb temperatures above 32°C (89.6°F) are critically dangerous. Avoid direct sunlight and drink lots of water.")
    elif calculated_wet_temperature > 30:
        st.warning("⚠️ Wet-bulb temperatures above 30°C (86°F) pose potential fatal danger to humans outside. It's very uncomfortable. Avoid direct sunlight and drink lots of water.")
    else:
        st.markdown("<span style='color:green;'>Wet-bulb temperatures are within safe limits. Enjoy the weather and drink enough water to be hydrated.</span>", unsafe_allow_html=True)

st.markdown("""
    <span style='color: orange;'>Reference: https://www.omnicalculator.com/physics/wet-bulb
    """, unsafe_allow_html=True)