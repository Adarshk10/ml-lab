# 📘 Machine Learning Lab – Experiment 5  
**Logistic Regression**

This repository contains solutions for **Experiment 5** of the Machine Learning Lab.  
It demonstrates how to apply **Logistic Regression** for binary classification tasks, including threshold tuning and ROC curve analysis.

---

## 🧑‍💻 Assignment 1: Student Pass/Fail Prediction
**Objective:**  
Build a **Logistic Regression model** to predict whether a student passes or fails based on **study hours** and **attendance percentage**.

**Highlights:**  
- Created a custom dataset with `StudyHours`, `Attendance`, and `Pass` (0 = Fail, 1 = Pass).  
- Trained Logistic Regression model.  
- Evaluated using **Accuracy**, **Confusion Matrix**, and **Classification Report**.  

**Sample Output:**  

-    StudyHours  Attendance  Pass
- 0           2          60     0
- 1           3          65     0
- 2           4          70     0
- 3           5          75     1
- 4           6          80     1
- 5           7          85     1
- 6           8          90     1
- 7           9          92     1
- 8          10          95     1
- 9          11          98     1

- Accuracy: 1.0
- Confusion Matrix:
-  [[1 0]
-  [0 2]]
- Classification Report:
-                precision    recall  f1-score   support

-            0       1.00      1.00      1.00         1
-            1       1.00      1.00      1.00         2

-     accuracy                           1.00         3
-    macro avg       1.00      1.00      1.00         3
- weighted avg       1.00      1.00      1.00         3

---

## 🧑‍💻 Assignment 2: Decision Threshold Comparison
**Objective:**  
Modify the **decision threshold** explicitly to **0.3, 0.5, and 0.7** and compare how **Precision** and **Recall** change.

**Highlights:**  
- Extracted predicted probabilities using `predict_proba()`.  
- Applied thresholds manually to classify outcomes.  
- Compared Precision and Recall across thresholds.  

**Sample Output:**  

- Threshold = 0.3
- Precision: 0.67, Recall: 1.00

- Threshold = 0.5
- Precision: 1.00, Recall: 0.75

- Threshold = 0.7
- Precision: 1.00, Recall: 0.50

📊 Lower thresholds increase **Recall** but reduce **Precision**. Higher thresholds increase **Precision** but reduce **Recall**.

---

## 🧑‍💻 Assignment 3: ROC Curve and AUC Score
**Objective:**  
Plot the **Receiver Operating Characteristic (ROC) curve** and calculate the **Area Under the Curve (AUC)** score.

**Highlights:**  
- Computed ROC curve using `roc_curve()`.  
- Calculated AUC score using `roc_auc_score()`.  
- Visualized ROC curve with baseline random guess line.  

**Sample Output:**  

- AUC Score: 0.95

📊 ROC curve shows trade‑off between True Positive Rate and False Positive Rate.  
AUC close to **1.0** indicates excellent classification performance.

---

## 🚀 How to Run
1. Navigate into the folder:
   ```bash
   cd ml-lab/experiment_5