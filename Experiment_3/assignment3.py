# (Q3) Compare and document the effect of StandardScaler vs MinMaxScaler by printing the trans-
# formed arrays and observing their numerical ranges.

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

data = {
    "Age": [25, 30, 35, 40, 28, 32, 45, 50, 29, 38],
    "Salary": [40000, 50000, 60000, 80000, 45000, 52000, 90000, 100000, 48000, 75000],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT", "Finance", "HR", "IT"],
    "Years_of_Experience": [2, 5, 7, 10, 3, 6, 15, 20, 4, 12]
}
df = pd.DataFrame(data)

df.loc[2, "Salary"] = np.nan
df.loc[5, "Age"] = np.nan
df.loc[7, "Department"] = np.nan
df.loc[9, "Years_of_Experience"] = np.nan

numeric_features = ["Age", "Salary", "Years_of_Experience"]

pipeline_standard = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

pipeline_minmax = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", MinMaxScaler())
])

standard_scaled = pipeline_standard.fit_transform(df[numeric_features])
minmax_scaled = pipeline_minmax.fit_transform(df[numeric_features])

standard_df = pd.DataFrame(standard_scaled, columns=numeric_features)
minmax_df = pd.DataFrame(minmax_scaled, columns=numeric_features)

print("Original Numerical Data:\n", df[numeric_features])
print("\nStandardScaler Output:\n", standard_df)
print("\nMinMaxScaler Output:\n", minmax_df)
