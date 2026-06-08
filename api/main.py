import os
from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI(title="GreenOps AI Dashboard API")

DATASET_PATH = os.getenv(
    "DATASET_PATH",
    "data/cloud_usage_enriched.csv"
)

MODEL_PATH = os.getenv(
    "MODEL_PATH",
    "model/co2e_model.pkl"
)

df = pd.read_csv(DATASET_PATH)
model = joblib.load(MODEL_PATH)


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
    
@app.get("/green-score")
def green_score():

    daily = (
        df.groupby("date")["co2e_kg"]
        .sum()
        .reset_index()
    )

    avg_daily = daily["co2e_kg"].mean()

    if avg_daily < 2:
        grade = "A"
        action = "Excellent — no action needed"
        gate = "PASS"

    elif avg_daily < 5:
        grade = "B"
        action = "Good — minor optimisation advised"
        gate = "PASS"

    elif avg_daily < 10:
        grade = "C"
        action = "Moderate — review VM sizing"
        gate = "PASS"

    elif avg_daily < 20:
        grade = "D"
        action = "Poor — immediate rightsizing required"
        gate = "WARNING"

    else:
        grade = "F"
        action = "Critical — pipeline soft gate triggered"
        gate = "BLOCKED"

    return {
        "grade": grade,
        "avg_daily_co2e": round(float(avg_daily), 2),
        "action": action,
        "gate": gate
    }