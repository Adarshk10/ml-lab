# (Q2) Construct a DataFrame containing the following columns: Student Name, Roll Number, Marks,
# and Attendance. Filter and display only the records of students who have scored above 80
# marks.

import pandas as pd

data = {
    "Student Name": ["Amit", "Riya", "Karan", "Sneha", "Vivek"],
    "Roll Number": [101, 102, 103, 104, 105],
    "Marks": [78, 85, 92, 67, 88],
    "Attendance": [90, 95, 85, 80, 92]
}

df = pd.DataFrame(data)

filtered_df = df[df["Marks"] > 80]

print("Original DataFrame:\n", df)
print("\nStudents with Marks > 80:\n", filtered_df)
