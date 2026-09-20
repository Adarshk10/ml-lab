# (Q2) Modify the decision threshold explicitly in Python to 0.3, 0.5, and 0.7. Compare how the
# Precision and Recall metrics change.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score

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

y_prob = model.predict_proba(X_test)[:, 1]  # probability of class 'Pass'

thresholds = [0.3, 0.5, 0.7]

for t in thresholds:
    y_pred = (y_prob >= t).astype(int)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    print(f"Threshold = {t}")
    print(f"Precision: {precision:.2f}, Recall: {recall:.2f}\n")
