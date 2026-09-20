# (Q2) Implement Multiple Linear Regression using two or more features (e.g., house area and number
# of bedrooms).

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = {
    "Area": [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500],
    "Bedrooms": [2, 3, 3, 4, 4, 5, 5, 6, 6, 7],
    "Price": [300000, 400000, 500000, 600000, 650000, 700000, 800000, 900000, 1000000, 1100000]
}
df = pd.DataFrame(data)

print("Sample Dataset:\n", df)

X = df[["Area", "Bedrooms"]]   
y = df["Price"]                

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nMean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
