# 🚴‍♂️ Delivery Logistics Pipeline: Medallion Architecture

## 📌 Project Overview
In food delivery logistics, external factors like weather directly impact rider efficiency, delivery times, and order volumes. This project is an end-to-end data engineering pipeline that simulates food delivery orders in Amsterdam and joins them with real-world weather API data to extract business insights.

The pipeline is built using the **Databricks Medallion Architecture** (Bronze, Silver, Gold layers) and processes the data using **PySpark** and **Delta Lake**.

## 🏗️ Architecture & Data Flow

*(Note: Add a screenshot of your pipeline diagram here. You can draw one quickly in draw.io)*

1. **Extraction (Local/Python):** - `generate_orders.py`: Generates synthetic delivery order data using the `Faker` library.
   - `fetch_weather.py`: Pulls real, hourly weather data for Amsterdam using the Open-Meteo REST API.
2. **Bronze Layer (Raw Ingestion):** - Ingests raw CSV data into Databricks.
   - Saves the data in its native format as optimized Delta tables (`raw_orders_bronze`, `raw_weather_bronze`).
3. **Silver Layer (Cleansing & Joining):** - Casts string timestamps to `Timestamp` data types.
   - Calculates `delivery_duration_minutes`.
   - Joins the synthetic order data with the real weather data based on the exact hour the order was placed (`orders_weather_silver`).
4. **Gold Layer (Business Aggregations):** - Aggregates the cleaned data to answer core business questions.
   - Produces highly refined tables for BI/Analytics (`gold_weather_impact`, `gold_restaurant_performance`).

## 🛠️ Tech Stack
* **Language:** Python (Local scripting), PySpark (Data processing)
* **Compute & Orchestration:** Databricks (Serverless Free Edition)
* **Storage:** Delta Lake
* **Libraries:** `pandas`, `requests`, `Faker`
* **External APIs:** Open-Meteo API (No auth required)

## 📊 Business Insights Extracted (Gold Layer)
The final stage of the pipeline produces ready-to-query metrics, answering:
1. **Weather Impact:** Does rain increase the average delivery time? (Aggregates average delivery time by `is_raining` flag).
2. **Restaurant Performance:** Which restaurant has the highest average order value alongside the fastest average delivery time?
