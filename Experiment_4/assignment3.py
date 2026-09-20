# (Q3) Implement Polynomial Regression on the same dataset and compare the R2 score against stan-
# dard Linear Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

data = {
    "Area": [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500],
    "Bedrooms": [2, 3, 3, 4, 4, 5, 5, 6, 6, 7],
    "Price": [300000, 400000, 500000, 600000, 650000, 700000, 800000, 900000, 1000000, 1100000]
}
df = pd.DataFrame(data)

X = df[["Area"]]   
y = df["Price"]

lin_model = LinearRegression()
lin_model.fit(X, y)
y_pred_lin = lin_model.predict(X)
r2_lin = r2_score(y, y_pred_lin)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_pred_poly = poly_model.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)

print("R² Score (Linear Regression):", r2_lin)
print("R² Score (Polynomial Regression):", r2_poly)

plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, y_pred_lin, color="red", label="Linear Regression")
plt.plot(X, y_pred_poly, color="green", label="Polynomial Regression (deg=2)")
plt.xlabel("Area (sq.ft)")
plt.ylabel("Price")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.show()
