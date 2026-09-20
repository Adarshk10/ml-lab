# 📘 Machine Learning Lab – Experiment 4  
**Linear Regression**

This repository contains solutions for **Experiment 4** of the Machine Learning Lab.  
It demonstrates how to apply **Linear Regression, Multiple Linear Regression, and Polynomial Regression** to predict house prices using synthetic datasets.

---

## 🧑‍💻 Assignment 1: Predict House Prices Based on Area
**Objective:**  
Build a **Linear Regression model** that predicts house prices using only the **house area (sq.ft)** feature.

**Highlights:**  
- Created dataset with `Area` and `Price`.  
- Trained a simple Linear Regression model.  
- Evaluated using **Mean Squared Error (MSE)** and **R² Score**.  
- Visualized regression line against actual data points.  

**Sample Output:**  

- Mean Squared Error: 25000000.0
- R² Score: 0.85

📊 Scatter plot shows actual house prices vs area, with regression line capturing the positive correlation.

---

## 🧑‍💻 Assignment 2: Multiple Linear Regression
**Objective:**  
Implement **Multiple Linear Regression** using two or more features (e.g., house area and number of bedrooms).

**Highlights:**  
- Created dataset with `Area`, `Bedrooms`, and `Price`.  
- Trained model using both predictors.  
- Printed coefficients to interpret feature impact.  
- Compared accuracy with single‑feature regression.  

**Sample Output:**  

- Mean Squared Error: 12000000.0
- R² Score: 0.95
- Intercept: 50000.0
- Coefficients: [150.0, 20000.0]

📊 Each extra sq.ft increases price by ~₹150, and each extra bedroom adds ~₹20,000.

---

## 🧑‍💻 Assignment 3: Polynomial Regression vs Linear Regression
**Objective:**  
Implement **Polynomial Regression** on the same dataset and compare its performance against standard Linear Regression.

**Highlights:**  
- Applied PolynomialFeatures (degree = 2).  
- Trained Polynomial Regression model.  
- Compared R² scores with Linear Regression.  
- Visualized both regression lines.  

**Sample Output:**  

- R² Score (Linear Regression): 0.95
- R² Score (Polynomial Regression): 0.99

📊 Polynomial Regression fits a curve, capturing non‑linear relationships better than Linear Regression.

---

## 🚀 How to Run
1. Navigate into the folder:
   ```bash
   cd ml-lab/experiment_4