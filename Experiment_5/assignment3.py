# (Q3) Plot the Receiver Operating Characteristic (ROC) curve and calculate the Area Under the Curve
# (AUC) score.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score

data = {
    "StudyHours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 92, 95, 98],
    "Pass":       [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]  # 0 = Fail, 1 = Pass
}
df = pd.DataFrame(data)

X = df[["StudyHours", "Attendance"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_prob = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_prob)

auc_score = roc_auc_score(y_test, y_prob)
print("AUC Score:", auc_score)

plt.plot(fpr, tpr, color="blue", label=f"ROC Curve (AUC = {auc_score:.2f})")
plt.plot([0, 1], [0, 1], color="red", linestyle="--", label="Random Guess")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Logistic Regression")
plt.legend()
plt.show()
