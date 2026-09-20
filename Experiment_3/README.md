# 📘 Machine Learning Lab – Experiment 3  
**Data Preprocessing**

This repository contains solutions for **Experiment 3** of the Machine Learning Lab.  
It demonstrates how to create synthetic datasets, handle missing values, and apply different scaling techniques using preprocessing pipelines.

---

## 🧑‍💻 Assignment 1: Synthetic Dataset Creation with Missing Values
**Objective:**  
Create a synthetic dataset with features: **Age, Salary, Department, Years of Experience** and deliberately inject missing values.

**Highlights:**  
- Constructed dataset using Pandas DataFrame.  
- Injected missing values (`NaN`) into numerical and categorical columns.  
- Prepared dataset for preprocessing tasks.  

**Sample Output:**  

-     Age   Salary   Department  Years_of_Experience
- 0  25.0  40000.0           HR                  2.0
- 1  30.0  50000.0           IT                  5.0
- 2  35.0      NaN      Finance                  7.0
- 3  40.0  80000.0           IT                 10.0
...

---

## 🧑‍💻 Assignment 2: MinMaxScaler Pipeline
**Objective:**  
Modify the preprocessing pipeline to apply **MinMaxScaler** instead of **StandardScaler**.

**Highlights:**  
- Used `SimpleImputer` to handle missing values.  
- Applied `MinMaxScaler` to scale numerical features into the range [0, 1].  
- Converted scaled arrays back into DataFrame for readability.  

**Sample Output:**  

- Scaled Numerical Data (MinMaxScaler):
-         Age    Salary  Years_of_Experience
- 0  0.000000  0.000000             0.000000
- 1  0.166667  0.125000             0.166667
- 2  0.333333  0.250000             0.250000
...

---

## 🧑‍💻 Assignment 3: Comparing StandardScaler vs MinMaxScaler
**Objective:**  
Compare the effect of **StandardScaler** and **MinMaxScaler** by printing transformed arrays and observing numerical ranges.

**Highlights:**  
- StandardScaler: Centers data (mean = 0, std = 1). Values can be negative.  
- MinMaxScaler: Normalizes data into fixed range [0, 1]. Preserves relative distances.  
- Comparison shows how scaling choice affects feature values.  

**Sample Output:**  

- StandardScaler Output:
-         Age    Salary  Years_of_Experience
- 0 -1.437591 -1.462494            -1.437591
- 1 -1.006314 -1.154648            -1.006314
...

- MinMaxScaler Output:
-         Age    Salary  Years_of_Experience
- 0  0.000000  0.000000             0.000000
- 1  0.166667  0.125000             0.166667
...

---

## 🚀 How to Run
1. Navigate into the folder:
   ```bash
   cd ml-lab/experiment_3