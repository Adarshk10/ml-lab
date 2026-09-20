# (Q1) Load and perform a complete EDA on the Wine dataset available in Scikit-learn.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target

print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nColumn names:\n", df.columns)
print("\nTarget classes:", np.unique(df['target']))

print("\nDescriptive statistics:\n", df.describe())

# Step 4: Check for missing values
print("\nMissing values:\n", df.isnull().sum())

plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=False, cmap="coolwarm")
plt.title("Correlation Heatmap of Wine Dataset")
plt.show()

sns.countplot(x='target', data=df, palette="Set2")
plt.title("Distribution of Wine Classes")
plt.show()

sns.pairplot(df, hue="target", vars=df.columns[:5])
plt.show()
