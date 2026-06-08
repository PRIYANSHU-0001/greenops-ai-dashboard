from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI(title="GreenOps AI Dashboard API")

df = pd.read_csv("data/cloud_usage_enriched.csv")
model = joblib.load("model/co2e_model.pkl")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics/summary")
def metrics_summary():

    total_co2e = float(df["co2e_kg"].sum())
    total_cost = float(df["cost_usd"].sum())

    top_team = (
        df.groupby("team")["co2e_kg"]
        .sum()
        .idxmax()
    )

    top_region = (
        df.groupby("region")["co2e_kg"]
        .sum()
        .idxmax()
    )

    return {
        "total_co2e": total_co2e,
        "total_cost": total_cost,
        "top_team": top_team,
        "top_region": top_region
    }


@app.get("/metrics/daily")
def metrics_daily():

    daily = (
        df.groupby("date")["co2e_kg"]
        .sum()
        .reset_index()
    )

    return daily.to_dict(orient="records")


@app.get("/metrics/team")
def metrics_team():

    team = (
        df.groupby("team")["co2e_kg"]
        .sum()
        .reset_index()
    )

    return team.to_dict(orient="records")


@app.get("/metrics/region")
def metrics_region():

    region = (
        df.groupby("region")["co2e_kg"]
        .sum()
        .reset_index()
    )

    return region.to_dict(orient="records")


@app.get("/forecast")
def forecast():

    daily = (
        df.groupby("date")["co2e_kg"]
        .sum()
        .reset_index()
    )

    forecast_values = (
        daily["co2e_kg"]
        .tail(30)
        .tolist()
    )

    return {
        "forecast": forecast_values
    }