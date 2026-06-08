import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(
    page_title="GreenOps AI Dashboard",
    page_icon="🌱",
    layout="wide"
)

# Sidebar
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/427/427735.png",
    width=120
)

st.sidebar.title("GreenOps AI")

st.sidebar.success(
    "Cloud Sustainability Platform"
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Powered by Azure + FastAPI + ML"
)

# Header
st.markdown(
    """
    # 🌍 GreenOps AI Dashboard
    ### AI Powered Carbon Intelligence Platform
    """
)

# API Status
st.success("✅ FastAPI Connected Successfully")

summary = requests.get(
    "http://127.0.0.1:8000/metrics/summary"
).json()

green_score = requests.get(
    "http://127.0.0.1:8000/green-score"
).json()

st.markdown("## ♻️ Green Score")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Grade",
        green_score["grade"]
    )

with col2:
    st.metric(
        "Pipeline Gate",
        green_score["gate"]
    )

st.info(
    green_score["action"]
)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌱 Total CO2e",
        f"{summary['total_co2e']:.2f} kg"
    )

with col2:
    st.metric(
        "💰 Total Cost",
        f"${summary['total_cost']:.2f}"
    )

with col3:
    st.metric(
        "🏆 Top Team",
        summary["top_team"]
    )

with col4:
    st.metric(
        "🌳 Trees Needed",
        int(summary["total_co2e"] / 21)
    )

st.markdown("---")

# Daily Trend
daily = requests.get(
    "http://127.0.0.1:8000/metrics/daily"
).json()

daily_df = pd.DataFrame(daily)

daily_df["date"] = pd.to_datetime(
    daily_df["date"]
)

fig = px.line(
    daily_df,
    x="date",
    y="co2e_kg",
    title="📈 Daily Carbon Emission Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Charts Row
col1, col2 = st.columns(2)

with col1:

    team = requests.get(
        "http://127.0.0.1:8000/metrics/team"
    ).json()

    team_df = pd.DataFrame(team)

    fig_team = px.bar(
        team_df,
        x="team",
        y="co2e_kg",
        title="🏢 Emissions By Team"
    )

    st.plotly_chart(
        fig_team,
        use_container_width=True
    )

with col2:

    region = requests.get(
        "http://127.0.0.1:8000/metrics/region"
    ).json()

    region_df = pd.DataFrame(region)

    fig_region = px.pie(
        region_df,
        names="region",
        values="co2e_kg",
        title="🌎 Region Emission Distribution"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

# Forecast Section
st.markdown("---")

st.subheader("🔮 AI Forecast Engine")

if st.button("🚀 Generate Forecast"):

    forecast = requests.get(
        "http://127.0.0.1:8000/forecast"
    ).json()

    forecast_df = pd.DataFrame(
        forecast["forecast"],
        columns=["Predicted CO2e"]
    )

    fig_forecast = px.line(
        forecast_df,
        y="Predicted CO2e",
        title="30 Day Carbon Forecast"
    )

    st.plotly_chart(
        fig_forecast,
        use_container_width=True
    )

st.markdown("---")

st.caption(
    "Built with Azure • FastAPI • Streamlit • Machine Learning"
)