# Task 2 — Filtering & Conditional Extraction


import numpy as np
marks = np.array([45, 67, 89, 34, 56, 90, 76, 23])

# Extract marks greater than 60
print("Marks greater than 60 ",marks[marks > 60])
# Marks greater than 60  [67 89 90 76]

# Replace marks < 35 with 0 (fail)
marks[marks < 35] = 0
print(marks)
# [45 67 89  0 56 90 76  0]

# Count how many students passed 
print("Total students passed :", np.count_nonzero(marks))
# Total students passed : 6