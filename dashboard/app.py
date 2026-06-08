import streamlit as st
import pandas as pd
import requests

st.title("🌱 GreenOps AI Dashboard")

# Summary
summary = requests.get(
    "http://127.0.0.1:8000/metrics/summary"
).json()

st.metric(
    "Total CO2e (kg)",
    round(summary["total_co2e"], 2)
)

st.metric(
    "Total Cost (USD)",
    round(summary["total_cost"], 2)
)

st.metric(
    "Highest Emission Team",
    summary["top_team"]
)

# Daily trend
daily = requests.get(
    "http://127.0.0.1:8000/metrics/daily"
).json()

daily_df = pd.DataFrame(daily)

st.subheader("Daily CO2e Trend")

st.line_chart(
    daily_df.set_index("date")["co2e_kg"]
)

# Forecast
if st.button("Show Forecast"):

    forecast = requests.get(
        "http://127.0.0.1:8000/forecast"
    ).json()

    forecast_df = pd.DataFrame(
        forecast["forecast"],
        columns=["Predicted CO2e"]
    )

    st.subheader("30 Day Forecast")

    st.line_chart(forecast_df)