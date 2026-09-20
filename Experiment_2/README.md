# 📘 Machine Learning Lab – Experiment 2  
**Dataset Loading, Exploration, and Visualization**

This repository contains solutions for **Experiment 2** of the Machine Learning Lab.  
It demonstrates how to load datasets, perform exploratory data analysis (EDA), visualize distributions, and analyze correlations using Python libraries.

---

## 🧑‍💻 Assignment 1: Complete EDA on Wine Dataset
**Objective:**  
Load the Wine dataset from Scikit‑learn and perform a complete **Exploratory Data Analysis (EDA)**.

**Highlights:**  
- Loaded dataset using `sklearn.datasets.load_wine()`.  
- Converted to Pandas DataFrame for easier handling.  
- Inspected shape, columns, and target classes.  
- Generated descriptive statistics and checked for missing values.  
- Visualized distributions and relationships using Seaborn pairplots and countplots.  

**Sample Output:**  
- Dataset shape: `(178, 14)` → 178 samples, 13 features + target.  
- Target classes: `0, 1, 2`.  
- No missing values.  
- Pairplots show clear separation between wine classes for some features.

---

## 🧑‍💻 Assignment 2: Boxplots for Numerical Attributes
**Objective:**  
Plot **boxplots** for all numerical attributes in the Wine dataset to visually identify potential outliers.

**Highlights:**  
- Used Pandas `df.boxplot()` for quick overview.  
- Created individual Seaborn boxplots for detailed visualization.  
- Identified attributes like *proline* and *color_intensity* with visible outliers.  

**Sample Output:**  
- Boxplots reveal spread and skewness of features.  
- Outliers detected in certain attributes, important for preprocessing.

---

## 🧑‍💻 Assignment 3: Correlation Heatmap
**Objective:**  
Generate a correlation heatmap using **Seaborn’s heatmap** and identify the pair of features with the strongest positive correlation.

**Highlights:**  
- Computed correlation matrix with `df.corr()`.  
- Visualized using `sns.heatmap()`.  
- Identified strongest positive correlation pair:  
  - **flavanoids** and **od280/od315_of_diluted_wines** (≈ 0.79).  

**Sample Output:**  
- Heatmap shows feature relationships.  
- Strong correlation pairs suggest redundancy and guide feature selection.

---

## 🚀 How to Run
1. Navigate into the folder:
   ```bash
   cd ml-lab/experiment_2