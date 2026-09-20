# 📘 Machine Learning Lab – Experiment 1  
**Python and ML Environment Basics**

This repository contains solutions for **Experiment 1** of the Machine Learning Lab.  
It covers basic Python, NumPy, and Pandas operations to build a strong foundation for ML.

---

## 📂 Assignments

### ✅ Assignment 1: NumPy Statistics
**Objective:**  
Create a NumPy array containing the internal marks of 10 students.  
Calculate and print the **mean, median, standard deviation, maximum, and minimum values**.

**Code File:** `assignment1.py`  
**Key Functions Used:**  
- `np.mean()`  
- `np.median()`  
- `np.std()`  
- `np.max()`  
- `np.min()`  

**Sample Output:**
- Marks of students: [78 85 92 67 74 88 90 81 76 95]
- Mean: 82.6
- Median: 83.0
- Standard Deviation: 8.74
- Maximum: 95
- Minimum: 67

---

### ✅ Assignment 2: Pandas DataFrame Filtering
**Objective:**  
Construct a DataFrame with columns:  
- Student Name  
- Roll Number  
- Marks  
- Attendance  

Filter and display only the records of students who scored **above 80 marks**.

**Code File:** `assignment2.py`  
**Key Functions Used:**  
- `pd.DataFrame()`  
- Filtering with `df[df["Marks"] > 80]`

**Sample Output:**
- Students with Marks > 80:
-     Student Name  Roll Number  Marks  Attendance
- 1           Riya          102     85          95
- 2          Karan          103     92          85
- 4          Vivek          105     88          92

---

### ✅ Assignment 3: Adding Grade Column
**Objective:**  
Add a new dynamically calculated column **Grade** to the DataFrame based on Marks:  
- ≥90 → A  
- 80–89 → B  
- 70–79 → C  
- <70 → D  

**Code File:** `assignment3.py`  
**Key Functions Used:**  
- `apply()` with custom function for grading

**Sample Output:**
- DataFrame with Grades:
-     Student Name  Roll Number  Marks  Attendance Grade
- 0           Amit          101     78          90     C
- 1           Riya          102     85          95     B
- 2          Karan          103     92          85     A
- 3          Sneha          104     67          80     D
- 4          Vivek          105     88          92     B

---

## 🚀 How to Run
1. Navigate into the folder:
   ```bash
   cd ml-lab/experiment_1