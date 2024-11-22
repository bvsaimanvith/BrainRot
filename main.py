import streamlit as st
import google.generativeai as genai
import os
import json

# working directory path
working_dir = os.path.dirname(os.path.abspath(__file__))

# path of config_data file
config_file_path = f"{working_dir}/config.json"
config_data = json.load(open("config.json"))

# loading the GOOGLE_API_KEY
API_KEY = config_data["GOOGLE_API_KEY"]
genai.configure(api_key=API_KEY)

# Function to transform text into brainrot
def transform_to_brainrot(input_text):
    try:
        gemini_pro_model = genai.GenerativeModel("gemini-pro")
        response = gemini_pro_model.generate_content(f"Translate this into brainrot style: {input_text}")
        # Extract the text response
        return response.text if response else "No response received"
    except Exception as e:
        return f"Error: {e}"

# Streamlit app
st.title("Brainrot Translator🧠✨")
st.markdown("Convert your text into chaotic 'brainrot' style using Google's Generative AI!")

# Input text field
user_input = st.text_input("Enter your text:", "")

# Translate button
if st.button("Translate to Brainrot"):
    if user_input.strip():
        brainrot_output = transform_to_brainrot(user_input)
        st.success(f"Brainrot Translation: {brainrot_output}")
    else:
        st.warning("Please enter some text to translate.")