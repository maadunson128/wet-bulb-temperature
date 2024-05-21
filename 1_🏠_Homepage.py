# importing libraries
import streamlit as st

# Setting initial page config
st.set_page_config(
    page_title="Wet Bulb Temperature App",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded",
    
)


st.title("🌡️ Wet-Bulb Temperature")

st.header("🔍 Understanding Wet-Bulb Temperature")

st.markdown("""
### What is Wet-Bulb Temperature? 🌧️
Wet-bulb temperature is the lowest temperature that can be reached by evaporating water into the air. It is a measure of how much moisture the air can hold and is an important factor in determining human comfort and safety.

### Why is Wet-Bulb Temperature Important? 🏖️
Wet-bulb temperature combines air temperature and humidity to give a more accurate measure of heat stress on the human body. High wet-bulb temperatures can be dangerous because the human body relies on evaporative cooling (sweating) to regulate its temperature. When the wet-bulb temperature is too high, sweating becomes less effective, and the risk of heat-related illnesses increases.

### Critical Wet-Bulb Temperature Thresholds
- **30°C (86°F) 🟡**: At this level, the body starts to struggle with heat dissipation, especially during physical exertion. People should start to take precautions like staying hydrated and avoiding prolonged outdoor activities.
- **32°C (89.6°F) 🟠**: This level is extremely dangerous for extended exposure. People are at a high risk of heat exhaustion and heat stroke. It's crucial to stay indoors in a cool environment and minimize physical activity.
- **35°C (95°F) 🔴**: This is considered the upper limit of human tolerance. At this temperature, the body cannot cool itself effectively, even at rest. The human body can theoretically withstand a 35°C wet-bulb temperature for up to 6 hours, but survival without artificial cooling (like air conditioning) is very unlikely over extended periods. Such conditions can lead to human fatality.

### Effects of High Wet-Bulb Temperature 🌡️
- **Heat Cramps 🤕**: Painful muscle contractions caused by excessive loss of salt and water.
- **Heat Exhaustion 😓**: Symptoms include heavy sweating, weakness, dizziness, nausea, and fainting.
- **Heat Stroke 🚑**: A severe condition that occurs when the body’s temperature regulation system fails. Symptoms include high body temperature, altered mental state, and even loss of consciousness. Heat stroke is a medical emergency.

### Precautions to Take During High Wet-Bulb Temperatures ⚠️
- **Stay Hydrated 💧**: Drink plenty of water throughout the day. Avoid caffeinated and alcoholic beverages as they can lead to dehydration.
- **Wear Appropriate Clothing 👕**: Light-colored, loose-fitting, and breathable clothing helps the body to cool down.
- **Limit Outdoor Activities 🏡**: Try to stay indoors during the hottest parts of the day, usually from late morning to early evening.
- **Use Fans and Air Conditioning 🌬️**: These can help reduce the indoor wet-bulb temperature and make the environment more comfortable.
- **Take Frequent Breaks ⛱️**: If you must be outside, take frequent breaks in the shade or a cool place.
- **Monitor Health 🚨**: Pay attention to the signs of heat-related illnesses and act quickly if symptoms appear.

By understanding and monitoring wet-bulb temperatures, we can take appropriate actions to stay safe and healthy, especially during extreme heat events. Stay informed and stay safe! 🌟
""")
