import streamlit as st
import pickle
import pandas as pd

# Load model
with open('gender_classification_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to predict gender
def predict_gender(features):
    prediction = model.predict([features])
    return "Male" if prediction[0] == 1 else "Female"

# Set page configuration
st.set_page_config(page_title="Gender Prediction", page_icon=":guardsman:", layout="wide")

# Add custom styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #66D3FA;
        }
        .title {
            color: #003366;
            font-size: 32px;
            font-weight: bold;
        }
        .stRadio, .stSlider {
            background-color: #2565AE;
            border-radius: 5px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton {
            background-color: #2565AE;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
    </style>
    """, unsafe_allow_html=True)

# Title of the app
st.markdown('<h1 class="title">Gender Prediction Model</h1>', unsafe_allow_html=True)

# User inputs
long_hair = st.radio("Does the person have long hair?", ("Yes", "No"))
long_hair = 1 if long_hair == "Yes" else 0

forehead_width_cm = st.slider("Forehead Width (cm)", min_value=1.0, max_value=10.0, step=0.5, value=5.5)
forehead_height_cm = st.slider("Forehead Height (cm)", min_value=1.0, max_value=10.0, step=0.5, value=5.5)

nose_wide = st.radio("Is the nose wide?", ("Yes", "No"))
nose_wide = 1 if nose_wide == "Yes" else 0

nose_long = st.radio("Is the nose long?", ("Yes", "No"))
nose_long = 1 if nose_long == "Yes" else 0

lips_thin = st.radio("Are the lips thin?", ("Yes", "No"))
lips_thin = 1 if lips_thin == "Yes" else 0

distance_nose_to_lip_long = st.radio("Is the distance from nose to lip long?", ("Yes", "No"))
distance_nose_to_lip_long = 1 if distance_nose_to_lip_long == "Yes" else 0

# Add a gap before the button
st.markdown("<br>", unsafe_allow_html=True)

# Predict button and display prediction
if st.button("Predict the Gender", key="predict_button"):
    features = [long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]
    prediction = predict_gender(features)
    st.markdown(f"<h3>The Predicted Gender is: {prediction}</h3>", unsafe_allow_html=True)
