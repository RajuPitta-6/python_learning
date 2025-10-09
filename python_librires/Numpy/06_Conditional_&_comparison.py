import numpy as np

arr = np.arange(3, 20, 3)
print(arr > 9)
print(arr % 6 == 0)
print(arr == 9)

# [False False False  True  True  True]
# [False  True False  True False  True]
# [False False  True False False False]

# Element-wise Comparison Between Two Arrays
a = np.array([1, 2, 3, 4])
b = np.array([1, 4, 2, 4])

print( a == b)
print( a > b)

# [ True False False  True]
# [False False  True False]
# Conditional selection
print(a[a == b]) # [1 4]
print(a[a > b]) # [3]

# np.where() — Conditional Replacement ------------------------
# np.where(condition, value_if_true, value_if_false)
arr = np.array([5, 10, 15, 20])
new_arr = np.where(arr > 10, "High", "Low")
print(new_arr)
# ['Low' 'Low' 'High' 'High']

# np.nonzero() — Indices of Non-Zero-----------
arr = np.array([0, 10, 0, 5, 0, 8])
print(np.nonzero(arr))
# (array([1, 3, 5]),)

# np.isin() — Check if Elements Exist in Another Array-------------
arr = np.array([10, 20, 30, 40, 50])
check = np.isin(arr, [20, 50, 70])
print(check)
print(arr[check]) 
# [False  True False False  True]
# [20 50]

# np.where() with multiple conditions---------------------
arr = np.array([5, 10, 15, 20, 25])
result = np.where(arr > 15, "High",
          np.where(arr > 10, "Medium", "Low"))
print(result)
# ['Low' 'Low' 'Medium' 'High' 'High']

# np.sign() — Get Sign of Numbers-----------------
arr = np.array([-1, -2, 0, 1, 2, 0])
print("signs :", np.sign(arr))
# signs : [-1 -1  0  1  1  0]

# np.allclose() — Check if Two Arrays Are Approximately
a = np.array([1.0001, 2.0000])
b = np.array([1.0001, 2.0000])
c = np.array([1.1, 2.3])
print(np.allclose(a, b))
print(np.allclose(a, c)) 

# True
# False