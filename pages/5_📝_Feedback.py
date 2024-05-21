import streamlit as st
st.header('Feedback')
st.write("We value your feedback! Please fill out the form below to provide your comments and suggestions.")

# Embed Google Form for feedback
google_form_url = "https://forms.gle/mKLcCvdxx7CKFPvK8"  # Replace with your Google Form URL
st.markdown(f'<iframe src="{google_form_url}" width="640" height="700" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>', unsafe_allow_html=True)