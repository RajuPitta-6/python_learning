# importing pandas
import pandas as pd

# creating series
s = pd.Series([10, 20, 30, 40])
print(s)
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# creating series with custom index
s = pd.Series([10, 20, 30], index = ['A', "B", "C"])
print(s)
# A    10
# B    20
# C    30
# dtype: int64

# Accessing series --------------------
print(s[0]) # by postion
# 10
print(s['C']) # by label
# 30

# seies operations
s2 = pd.Series([1, 2, 3], index = ['A', 'B', 'C'])
print(s + s2)
# A    11
# B    22
# C    33
# dtype: int64

# index must be same 

# series attributes-------------------------
print(s.dtype)
print(s.size)
print(s.index)
# int64
# 3
# Index(['A', 'B', 'C'], dtype='object')

# series with Dictonary -------------------------
data = {'Math': 99, 'Science':85, 'Chemistry':85}
s = pd.Series(data)
print(s)
# Math         99
# Science      85
# Chemistry    85
# dtype: int64

# series slicing -----------------------------
print(s[:2]) # first two elements
print(s['Math':'Chemistry']) # label based slicing

# Math       99
# Science    85
# dtype: int64
# Math         99
# Science      85
# Chemistry    85
# dtype: int64

# series boolean filtering -----------------------------
print(s[s > 90])
# Math    99
# dtype: int64
print(s[s == 85])
# Science      85
# Chemistry    85

# series methods -------------------------------------
print(s.max())
# 99
print(s.sum())
# 269
print(s.min())
# 85
print(s.mean())
# 89.66666666666667
# print(s.describe())
# count     3.000000
# mean     89.666667
# std       8.082904
# min      85.000000
# 25%      85.000000
# 50%      85.000000
# 75%      92.000000
# max      99.000000
# dtype: float64