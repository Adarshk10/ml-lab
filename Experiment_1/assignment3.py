# (Q3) Write a script to add a new dynamically calculated column named Grade to the DataFrame
# based on the Marks column (e.g., ¿90 is ’A’, 80-89 is ’B’, etc.).

import pandas as pd

data = {
    "Student Name": ["Amit", "Riya", "Karan", "Sneha", "Vivek"],
    "Roll Number": [101, 102, 103, 104, 105],
    "Marks": [78, 85, 92, 67, 88],
    "Attendance": [90, 95, 85, 80, 92]
}

df = pd.DataFrame(data)

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "D"

df["Grade"] = df["Marks"].apply(calculate_grade)

print("DataFrame with Grades:\n", df)
