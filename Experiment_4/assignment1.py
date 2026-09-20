# (Q1)  Download a real-estate dataset and predict house prices based solely on the house area (in sq.
# ft).

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = {
    "Area": [1000, 1500, 2000, 2500, 3000],
    "Price": [500000, 750000, 1000000, 1250000, 1500000]
}
df = pd.DataFrame(data)
df.to_csv("real_estate.csv", index=False)  

print("First 5 rows:\n", df.head())

X = df[["Area"]]   
y = df["Price"]    

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", linewidth=2, label="Regression Line")
plt.xlabel("Area (sq.ft)")
plt.ylabel("Price")
plt.title("Linear Regression: House Price vs Area")
plt.legend()
plt.show()
