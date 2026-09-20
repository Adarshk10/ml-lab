# (Q2) Plot Boxplots for all numerical attributes in the Wine dataset to visually identify any potential
# outliers.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)

plt.figure(figsize=(15, 10))
df.boxplot(rot=45)   
plt.title("Boxplots of Wine Dataset Features")
plt.show()

plt.figure(figsize=(20, 15))
for i, col in enumerate(df.columns, 1):
    plt.subplot(4, 4, i)
    sns.boxplot(y=df[col], color="skyblue")
    plt.title(col)
plt.tight_layout()
plt.show()
