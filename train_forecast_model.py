import pandas as pd
import matplotlib.pyplot as plt
import joblib
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load data

df = pd.read_csv("data/cloud_usage_enriched.csv")

df["date"] = pd.to_datetime(df["date"])

# Daily aggregation

daily = (
df.groupby("date")["co2e_kg"]
.sum()
.reset_index()
)

# Feature Engineering

daily["lag_7"] = daily["co2e_kg"].shift(7)
daily["lag_14"] = daily["co2e_kg"].shift(14)

daily["rolling_7"] = (
daily["co2e_kg"]
.rolling(7)
.mean()
)

daily["dow"] = daily["date"].dt.dayofweek

# Remove NaN rows

daily.dropna(inplace=True)

# Features and target

features = ["lag_7", "lag_14", "rolling_7", "dow"]

X = daily[features]
y = daily["co2e_kg"]

# Last 30 days test set

X_train = X[:-30]
X_test = X[-30:]

y_train = y[:-30]
y_test = y[-30:]

# Train model

model = LinearRegression()
model.fit(X_train, y_train)

# Predict

y_pred = model.predict(X_test)

# RMSE

mse = mean_squared_error(
    y_test,
    y_pred
)

rmse = np.sqrt(mse)

print("RMSE:", rmse)

mean_daily = y_test.mean()

print("Mean Daily CO2e:", mean_daily)

if rmse < (0.10 * mean_daily):
    print("Model performance is GOOD (<10%)")
else:
    print("Model performance needs improvement")

# Plot

plt.figure(figsize=(10,5))

plt.plot(
y_test.values,
label="Actual"
)

plt.plot(
y_pred,
label="Predicted"
)

plt.title(
"Actual vs Predicted CO2e"
)

plt.xlabel("Days")
plt.ylabel("CO2e")

plt.legend()

plt.tight_layout()

plt.savefig(
"model/forecast_plot.png"
)

plt.close()

# Save model

joblib.dump(
model,
"model/co2e_model.pkl"
)

print("Model Saved")    
