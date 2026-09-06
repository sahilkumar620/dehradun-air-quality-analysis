"""
Dehradun Air Quality Analysis (using uploaded dehradun_aqi_2020_2021.csv)
============================================================================
Data: 412 station-days, Jan 2020 - Dec 2021, 3 Dehradun stations
(Clock Tower, Raipur Road, Himalayan Drug ISBT), sourced from UKPCB PDF reports.

Run this in Colab AFTER uploading dehradun_aqi_2020_2021.csv (already done).
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")
OUT_DIR = "outputs"
os.makedirs(OUT_DIR, exist_ok=True)

# %% 1. Load data ----------------------------------------------------------
df = pd.read_csv("dehradun_aqi_2020_2021.csv", parse_dates=["date"])
POLLUTANTS = ["PM10", "PM2.5", "SO2", "NOx"]  # (no CO/O3 in this dataset)

print(f"Loaded {len(df)} rows, {df['date'].min().date()} to {df['date'].max().date()}")
print(df["station"].value_counts())

# %% 2. Chart 1 — Monthly trend --------------------------------------------
monthly = df.groupby(df["date"].dt.to_period("M"))[POLLUTANTS].mean()
monthly.index = monthly.index.to_timestamp()

plt.figure(figsize=(12, 6))
for p in POLLUTANTS:
    plt.plot(monthly.index, monthly[p], marker="o", label=p)
plt.title("Monthly Average Pollutant Levels — Dehradun (2020-2021)")
plt.xlabel("Month")
plt.ylabel("Concentration (µg/m³)")
plt.legend()
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/1_monthly_trend.png", dpi=150)
plt.show()

# %% 3. Chart 2 — Seasonal pattern ------------------------------------------
def month_to_season(m):
    if m in [12, 1, 2]:
        return "Winter"
    elif m in [3, 4, 5]:
        return "Summer"
    elif m in [6, 7, 8, 9]:
        return "Monsoon"
    else:
        return "Post-Monsoon"

df["season"] = df["month"].apply(month_to_season)
seasonal = df.groupby("season")[POLLUTANTS].mean().reindex(
    ["Winter", "Summer", "Monsoon", "Post-Monsoon"]
)

seasonal.plot(kind="bar", figsize=(10, 6))
plt.title("Seasonal Average Pollutant Levels — Dehradun")
plt.ylabel("Concentration (µg/m³)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/2_seasonal_pattern.png", dpi=150)
plt.show()

# %% 4. Chart 3 — Weekday vs weekend -----------------------------------------
wk = df.groupby("is_weekend")[POLLUTANTS].mean()
wk.index = wk.index.map({True: "Weekend", False: "Weekday"})

wk.T.plot(kind="bar", figsize=(10, 6))
plt.title("Weekday vs Weekend Pollutant Levels — Dehradun")
plt.ylabel("Concentration (µg/m³)")
plt.xlabel("Pollutant")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/3_weekday_vs_weekend.png", dpi=150)
plt.show()

# %% 5. Chart 4 — Pollutant comparison (which is worst) ----------------------
avg_levels = df[POLLUTANTS].mean().sort_values(ascending=False)

plt.figure(figsize=(9, 6))
sns.barplot(x=avg_levels.values, y=avg_levels.index, hue=avg_levels.index,
            palette="rocket", legend=False)
plt.title("Average Pollutant Levels — Dehradun (Overall)")
plt.xlabel("Average Concentration (µg/m³)")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/4_pollutant_comparison.png", dpi=150)
plt.show()

# %% 6. Chart 5 — AQI category breakdown -------------------------------------
def aqi_category(aqi):
    if pd.isna(aqi):
        return np.nan
    if aqi <= 50: return "Good"
    if aqi <= 100: return "Satisfactory"
    if aqi <= 200: return "Moderate"
    if aqi <= 300: return "Poor"
    if aqi <= 400: return "Very Poor"
    return "Severe"

df["AQI_category"] = df["AQI"].apply(aqi_category)
cat_order = ["Good", "Satisfactory", "Moderate", "Poor", "Very Poor", "Severe"]
cat_counts = df["AQI_category"].value_counts().reindex(cat_order).fillna(0)

plt.figure(figsize=(9, 6))
colors = ["#2ecc71", "#a3d977", "#f1c40f", "#e67e22", "#e74c3c", "#7d0d0d"]
plt.bar(cat_counts.index, cat_counts.values, color=colors)
plt.title("Days by AQI Category — Dehradun (2020-2021)")
plt.ylabel("Number of Station-Days")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/5_aqi_category_breakdown.png", dpi=150)
plt.show()

# %% 7. Findings summary (for the README) ------------------------------------
worst_pollutant = avg_levels.index[0]
worst_season = seasonal.mean(axis=1).idxmax()
weekday_avg = wk.loc["Weekday"].mean()
weekend_avg = wk.loc["Weekend"].mean()
station_avg_aqi = df.groupby("station")["AQI"].mean().sort_values(ascending=False)

print("\n=== KEY FINDINGS (draft for README) ===")
print(f"- Data covers {df['date'].min().date()} to {df['date'].max().date()} "
      f"({len(df)} station-days, 3 Dehradun stations).")
print(f"- Worst-performing pollutant on average: {worst_pollutant} "
      f"({avg_levels.iloc[0]:.1f} µg/m³).")
print(f"- Worst season for air quality: {worst_season}.")
print(f"- Weekday avg pollution ({weekday_avg:.1f}) vs weekend avg "
      f"({weekend_avg:.1f}) — {'higher' if weekday_avg > weekend_avg else 'lower'} "
      f"on weekdays.")
print(f"- Station with worst average AQI: {station_avg_aqi.index[0]} "
      f"(avg AQI {station_avg_aqi.iloc[0]:.0f}).")
print(f"- AQI category breakdown (station-days): {cat_counts.to_dict()}")

df.to_csv(f"{OUT_DIR}/dehradun_final_with_categories.csv", index=False)
print(f"\nAll charts + final CSV saved in the '{OUT_DIR}/' folder.")
