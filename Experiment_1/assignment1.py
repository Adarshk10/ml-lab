# (Q1) Create a NumPy array containing the internal marks of 10 students. Calculate and print the
# mean, median, standard deviation, maximum, and minimum values.

import numpy as np

marks = np.array([78, 85, 92, 67, 74, 88, 90, 81, 76, 95])

mean_val = np.mean(marks)
median_val = np.median(marks)
std_dev = np.std(marks)
max_val = np.max(marks)
min_val = np.min(marks)

print("Marks of students:", marks)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)
print("Maximum:", max_val)
print("Minimum:", min_val)
