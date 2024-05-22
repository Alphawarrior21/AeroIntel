import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))

# Function to set background image from a URL
def set_background(image_url):
    css = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
        backgit config --global user.name "Your Name"ground-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set the background image using a URL
image_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXU0d29lZTB5aXJpMjQ1c2wxeXpwajAwbWU5dTE0eG5panZnemZ0diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MsjwOAnbFzOXm/giphy.gif"  # Replace YOUR_GIF_LINK_HERE with the actual URL
set_background(image_url)

# Streamlit UI elements
# Custom CSS for the title with increased font size
title_css = """
<style>
h1 {{
    font-size: 4em;  /* Significantly increases the font size */
    font-weight: bold;  /* Makes the font bold */
    color: #ffffff;  /* Changes the text color to white */
    text-shadow: 3px 3px 8px black;  /* Enhances the text shadow for better visibility */
    background: rgba(0, 0, 0, 0.5);  /* Adds a semi-transparent black background */
    padding: 15px 20px;  /* Adds more padding around the text */
    border-radius: 15px;  /* Optional: rounds the corners of the background */
}}
</style>
"""
st.markdown(title_css, unsafe_allow_html=True)
st.title('AeroIntel')

# Custom CSS for the input box
input_style = """
<style>
input[type="text"] {{
    font-size: 1.2em;  /* Larger font size */
    color: #000;  /* Dark text color */
    background-color: rgba(255, 255, 255, 0.8);  /* Semi-transparent white background */
    border: 2px solid #0078D4;  /* Adds a blue border */
    border-radius: 10px;  /* Rounds the corners of the input box */
    padding: 10px 15px;  /* Adds padding inside the input box */
}}
div[data-baseweb="base-input"] {{
    background-color: transparent !important;
}}
[data-testid="stAppViewContainer"] {{
    background-color: transparent !important;
}}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)

question = st.text_input(
    "Clear Answers for Clear Skies: Your Air Quality Information Hub",
    placeholder="Breathe Easy: Ask Aerointel Anything About Air Quality"
)
"Ft. Pathway, OpenAI"

if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")
