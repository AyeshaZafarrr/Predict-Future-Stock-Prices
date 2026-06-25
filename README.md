# 📈 Stock Price Prediction using Machine Learning

## Overview

This project predicts the next day's stock closing price using historical stock market data obtained from Yahoo Finance. The project demonstrates the complete machine learning workflow, including data collection, preprocessing, exploratory data analysis, model training, evaluation, and prediction.

---

## Features

- Data fetched using yfinance API
- Exploratory Data Analysis (EDA)
- Feature engineering for time-series forecasting
- Linear Regression Model
- Random Forest Regressor
- Model Comparison
- Feature Importance Analysis
- Prediction visualization (Actual vs Predicted)

---

## Dataset

- Source: Yahoo Finance API (yfinance)
- Stock: Apple Inc. (AAPL)
- Features Used:
  - Open Price
  - High Price
  - Low Price
  - Trading Volume
- Target:
  - Next Day Closing Price

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- yfinance
- Joblib

---

## Machine Learning Models

### Linear Regression
A baseline regression model used for predicting stock prices.

### Random Forest Regressor
An ensemble model that improves prediction accuracy by capturing non-linear patterns.

---

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

---

## Project Structure

```text
Stock-Price-Prediction/
│
├── data/
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   └── train.py
│
├── models/
│   ├── linear_regression_model.pkl
│   └── random_forest_model.pkl
│
├── outputs/
├── README.md
├── requirements.txt
└── .gitignore
Key Learnings
Working with financial time-series data
Using APIs for real-world data collection
Building regression models
Comparing multiple ML algorithms
Model evaluation and visualization
Organizing production-ready ML projects
Future Improvements
Real-time stock prediction dashboard (Streamlit)
Deep learning models (LSTM)
Multi-stock prediction system
Live market integration
Author

Ayesha Zafar
Machine Learning | Data Science | Python