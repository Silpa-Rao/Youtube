# app.py

import streamlit as st
import pandas as pd
import joblib

# 1) Load the trained pipeline
@st.cache_resource
def load_model():
    return joblib.load("model_pipeline.pkl")

model = load_model()

st.title("YouTube Channel Earnings Predictor")
st.markdown("Enter channel statistics below to predict the **lowest yearly earnings**.")

# 2) Sidebar inputs for each feature
st.sidebar.header("Input Features")

# --- Categorical free-text inputs ---
category     = st.sidebar.text_input("Category", value="")
channel_type = st.sidebar.text_input("Channel Type", value="")
country      = st.sidebar.text_input("Country", value="")

gross_enroll = st.sidebar.number_input(
    "Gross tertiary education enrollment (%)", min_value=0.0, max_value=100.0, value=0.0
)
uploads = st.sidebar.number_input("Number of uploads", min_value=0, value=0)
video_views = st.sidebar.number_input("Total video views", min_value=0, value=0)
video_views_rank = st.sidebar.number_input("Video views rank", min_value=0, value=0)
population = st.sidebar.number_input("Population", min_value=0, value=0)
urban_population = st.sidebar.number_input("Urban population", min_value=0, value=0)
subscribers = st.sidebar.number_input("Total subscribers", min_value=0, value=0)
subs_last_30 = st.sidebar.number_input(
    "Subscribers in last 30 days", min_value=0, value=1
)
country_rank = st.sidebar.number_input("Country rank", min_value=0, value=0)
channel_type_rank = st.sidebar.number_input("Channel type rank", min_value=0, value=0)
views_last_30 = st.sidebar.number_input(
    "Views in last 30 days", min_value=0, value=0
)
unemployment = st.sidebar.number_input(
    "Unemployment rate (%)", min_value=0.0, max_value=100.0, value=5.0
)

# 3) Pack into DataFrame when user clicks “Predict”
if st.button("Predict Lowest Yearly Earnings"):
    input_dict = {
        "Gross tertiary education enrollment (%)": gross_enroll,
        "uploads": uploads,
        "video views": video_views,
        "video_views_rank": video_views_rank,
        "Population": population,
        "Urban_population": urban_population,
        "subscribers": subscribers,
        "subscribers_for_last_30_days": subs_last_30,
        "country_rank": country_rank,
        "channel_type_rank": channel_type_rank,
        "video_views_for_the_last_30_days": views_last_30,
        "Unemployment rate": unemployment,
        "category": category,
        "channel_type": channel_type,
        "Country": country,
    }
    input_df = pd.DataFrame([input_dict])

    try:
        prediction = model.predict(input_df)[0]
        st.success(f"📈 Predicted lowest yearly earnings: **${prediction:,.2f}**")
    except Exception as e:
        st.error(f"Model prediction failed: {e}")
