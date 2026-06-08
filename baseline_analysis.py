import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data/cloud_usage_dataset.xlsx")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

print("Shape")
print(df.shape)

print("\nData Types")
print(df.dtypes)

print("\nFirst 10 Rows")
print(df.head(10))

print("\nNull Values")
print(df.isnull().sum())

# Handle missing values
df.fillna(0, inplace=True)

# Cost calculations
total_cost = df["cost_usd"].sum()

avg_daily_cost = (
    df.groupby(df["date"].dt.date)["cost_usd"]
    .sum()
    .mean()
)

print("\nTotal Cost:", total_cost)
print("Average Daily Cost:", avg_daily_cost)

# CO2e calculation
df["co2e_kg"] = (
    (df["cpu_hours"] * 0.0002)
    + (df["storage_gb"] * 0.00006 / 30)
    + (df["data_transfer_gb"] * 0.001)
)

print("\nTotal CO2e")
print(df["co2e_kg"].sum())

print("\nCO2e by Service Type")
print(
    df.groupby("service_type")["co2e_kg"]
    .sum()
)

print("\nCO2e by Team")
print(
    df.groupby("team")["co2e_kg"]
    .sum()
)

# Daily chart
daily_co2e = df.groupby("date")["co2e_kg"].sum()

plt.figure(figsize=(10,5))
daily_co2e.plot()
plt.title("Daily CO2e Emissions")
plt.xlabel("Date")
plt.ylabel("CO2e (kg)")
plt.tight_layout()
plt.savefig("data/daily_co2e.png")
plt.close()

# Region chart
region_co2e = df.groupby("region")["co2e_kg"].sum()

plt.figure(figsize=(8,5))
region_co2e.plot(kind="bar")
plt.title("CO2e by Region")
plt.ylabel("CO2e (kg)")
plt.tight_layout()
plt.savefig("data/co2e_by_region.png")
plt.close()

# Save enriched dataset
df.to_csv(
    "data/cloud_usage_enriched.csv",
    index=False
)

print("\nAnalysis Complete")