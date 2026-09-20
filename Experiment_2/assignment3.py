# (Q3) Generate a correlation heatmap (using Seaborn’s heatmap) and identify the pair of features that
# exhibit the strongest positive correlation.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)

corr_matrix = df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Wine Dataset")
plt.show()


corr_unstacked = corr_matrix.unstack()
sorted_corr = corr_unstacked.sort_values(ascending=False)

strongest_pair = [(i, j, val) for i, j, val in zip(sorted_corr.index.get_level_values(0),
                                                   sorted_corr.index.get_level_values(1),
                                                   sorted_corr.values)
                  if i != j][0]

print("Strongest positive correlation is between:", strongest_pair[0], "and", strongest_pair[1],
      "with correlation =", strongest_pair[2])
