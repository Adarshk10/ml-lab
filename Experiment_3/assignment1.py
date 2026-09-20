# (Q1) Create and preprocess a synthetic dataset containing the features: Age, Salary, Department,
# and Years of Experience. Inject missing values deliberately.

import pandas as pd
import numpy as np

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

print("Synthetic Dataset with Missing Values:\n", df)
