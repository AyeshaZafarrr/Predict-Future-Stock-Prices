# 📈 Stock Price Prediction using Machine Learning

## Overview

This project predicts the next day's stock closing price using historical stock market data obtained from Yahoo Finance. The project demonstrates the complete machine learning workflow, including data collection, preprocessing, exploratory data analysis, model training, evaluation, and prediction.

## Objectives

* Retrieve historical stock market data using the yfinance API
* Analyze stock price trends and patterns
* Predict the next day's closing stock price
* Compare multiple regression models
* Visualize model performance and predictions

---

## Dataset

* Source: Yahoo Finance API (yfinance)
* Stock: Apple Inc. (AAPL)
* Features Used:

  * Open Price
  * High Price
  * Low Price
  * Trading Volume
* Target:

  * Next Day Closing Price

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* yfinance
* Joblib

---

## Machine Learning Models

### Linear Regression

A baseline regression model used for predicting future closing prices.

### Random Forest Regressor

An ensemble learning model used to improve prediction performance and capture non-linear relationships.

---

## Project Workflow

1. Data Collection using Yahoo Finance API
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Prediction Visualization
9. Model Serialization using Joblib

---

## Evaluation Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

---

## Visualizations

The project includes:

* Stock Closing Price Trend
* Actual vs Predicted Stock Prices
* Random Forest Prediction Comparison
* Feature Importance Analysis

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
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Key Learning Outcomes

* Working with financial time-series data
* Using APIs for real-world data collection
* Building regression-based machine learning models
* Comparing model performance
* Visualizing prediction results
* Organizing machine learning projects for production-ready repositories

---

## Future Improvements

* Real-time stock prediction dashboard
* Streamlit deployment
* LSTM-based deep learning forecasting
* Multi-stock prediction support

---

## Author

Ayesha Zafar

Machine Learning | Data Science | Python
