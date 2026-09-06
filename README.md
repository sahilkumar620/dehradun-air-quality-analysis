# Dehradun Air Quality Analysis (2020-2021)

## Overview
Most beginner data analytics portfolios lean on the same handful of Kaggle
datasets (Titanic, Netflix, Iris...). This project instead uses **real
government air quality monitoring data** for my own city — Dehradun,
Uttarakhand — sourced from the Uttarakhand Pollution Control Board (UKPCB)
official reports, to answer a question that actually matters locally: *how
polluted is Dehradun's air, and when/where is it worst?*

## Data Source
- **Uttarakhand Pollution Control Board (UKPCB)** — official monthly AQI
  reports (`ukpcb.uk.gov.in`), covering 3 monitoring stations in Dehradun:
  - Clock Tower (Commercial zone)
  - Raipur Road (Commercial/Residential zone)
  - Himalayan Drug, ISBT (Commercial/Industrial zone)
- **Period covered:** January 2020 – December 2021
- **412 station-days** of PM10, PM2.5, SO2, NOx, and official AQI readings

## Analysis Performed
1. Data cleaning — parsed dates and pollutant values out of raw government
   report tables into a clean, tidy CSV
2. **Monthly trend** — how pollutant levels moved month by month across 2020-2021
3. **Seasonal pattern** — comparing Winter, Summer, Monsoon, and Post-Monsoon averages
4. **Weekday vs weekend comparison** — checking whether traffic-driven
   weekday pollution is measurably worse than weekends
5. **Pollutant comparison** — identifying which pollutant is the biggest
   problem in Dehradun on average
6. **AQI category breakdown** — using official CPCB AQI bands (Good /
   Satisfactory / Moderate / Poor / Very Poor / Severe) to classify every
   station-day

## Key Findings
- **PM10 is the dominant pollutant** in Dehradun, averaging ~144.5 µg/m³ —
  well above the national annual standard of 60 µg/m³.
- **Winter is the worst season for air quality**, consistent with the
  well-documented pattern of temperature inversions trapping pollutants
  closer to the ground in North Indian winters.
- **Weekday vs weekend pollution was roughly the same** (69.8 vs 70.4 on the
  combined pollutant average) — unlike bigger metros, Dehradun's air quality
  doesn't show a strong "weekday traffic effect," suggesting background
  sources (geography, heating, dust) may matter more than daily commute traffic.
- **Himalayan Drug, ISBT recorded the worst average AQI (192)** of the three
  stations — likely reflecting its Commercial/Industrial zoning and location
  near a transport hub.
- Across all 412 station-days: **0% were "Good," ~13% "Satisfactory," ~51%
  "Moderate," and ~36% "Poor."** Not a single day in the dataset qualified as
  clean ("Good") air — a genuinely striking finding for a city known for its
  greenery and hill-station reputation.

## Tech Stack
Python, Pandas, Matplotlib, Seaborn, NumPy

## Files in this Repo
- `Dehradun_Air_Quality_Analysis.ipynb` — full analysis notebook
- `dehradun_aqi_2020_2021.csv` — cleaned source dataset
- `outputs/dehradun_final_with_categories.csv` — final dataset with computed
  season, weekday, and AQI category columns
- `outputs/*.png` — the 5 charts (monthly trend, seasonal pattern, weekday
  vs weekend, pollutant comparison, AQI category breakdown)

## Author
Sahil Kumar — [GitHub](https://github.com/sahilkumar620) ·
[Portfolio](https://sahilkumar620.github.io/SAHIL-PROTFOLIO/)
