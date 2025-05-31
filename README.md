# ✈️ Airline Market Fare Prediction App

This project builds a machine learning-based web application using Flask that predicts **average airline fares** based on key market and route-related factors. The model is trained on real airline data and optimized for performance using XGBoost.

---

## 🧠 Project Overview

- **Objective:** Predict the average fare of a flight route based on operational, market, and competition features.
- **Workflow:**
  - Data preprocessing and feature selection
  - Comparison of ANN, Random Forest, and XGBoost
  - Selection of top 10 important features
  - Final model deployment using Flask
- **End Result:** A lightweight and intuitive web application for predicting airline fares.

---

## 📈 Model Comparison

| Model                         | RMSE ↓  | R² Score ↑ | Notes                         |
|------------------------------|---------|------------|-------------------------------|
| **XGBoost (10 Features)**    | **5.53** | **0.9947**  | Best performance (final model)|
| Random Forest (500 Trees)    | 8.23    | 0.9882     | Solid, but less accurate      |
| ANN (2 Hidden Layers)        | 22.55   | 0.9041     | Performed worst               |

✅ **Selected Model:** XGBoost trained on top 10 features due to its superior accuracy and generalization.

---

## 🔍 Top 10 Features Used in Final Model

| Feature           | Description                                                  |
|-------------------|--------------------------------------------------------------|
| `MktMilesFlown`   | Total miles flown on the route                               |
| `LCC_Comp`        | Indicates if there is low-cost carrier competition (binary)  |
| `Carrier_freq`    | Frequency of the specific carrier on the route               |
| `Carrier`         | Encoded airline carrier identifier                           |
| `NonStopMiles`    | Miles flown without stopovers                                |
| `Pax`             | Number of passengers on the route                            |
| `MktCoupons`      | Average number of coupons (segments)                         |
| `Market_HHI`      | Herfindahl-Hirschman Index – market concentration measure    |
| `Market_share`    | Carrier's share in the market                                |
| `ODPairID_freq`   | Frequency of the origin-destination pair                     |

---

## ⚙️ Tech Stack

- **Languages:** Python, HTML
- **ML Libraries:** `xgboost`, `scikit-learn`, `numpy`, `pandas`
- **Modeling:** ANN (Keras), Random Forest, XGBoost
- **Deployment:** Flask
- **Visualization (EDA):** Matplotlib, Seaborn

---

## 🚀 Demo

Try out the Flask web app locally:
```bash
python app_airline_fare.py
```
Then visit http://127.0.0.1:5000/ in your browser.
