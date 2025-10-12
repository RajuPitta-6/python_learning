import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Select specific elements using index list
result = arr[[0, 2, 4]]
print(result)
# Output: [10 30 50]

arr2d = np.arange(12).reshape(3, 4)
print(arr2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# Select specific rows
rows = arr2d[[0, 2]]
print(rows)
# [[ 0  1  2  3]
#  [ 8  9 10 11]]

# Select specific elements from specific positions
elements = arr2d[[0, 1, 2], [1, 2, 3]]
print(elements)
# [ 1  6 11]

# Using Fancy Indexing for Assignment--------------------
arr = np.arange(10)
arr[[2, 5, 8]] = -1
print(arr)
# [ 0  1 -1  3  4 -1  6  7 -1  9]

# Conditional Assignment---------------------------
arr = np.array([10, 20, 30, 40, 50])

# Replace all values > 30 with 99
arr[arr > 30] = 99
print(arr)
# [10 20 30 99 99]

# np.where()  conditional operation
arr = np.array([10, 20, 30, 40, 50, 15, 11])

# Replace values > 25 with 1 else 0
res = np.where(arr > 25, 1, 0)
print(res)
# [0 0 1 1 1 0 0]

# np.take() & np.put() -----------------------
arr = np.array([10, 20, 30, 40, 50])

# np.take() selects values using indices 
print(np.take(arr, [0, 2, 3]))
# [10 30 40]

# np.put() modifies elements by indices
np.put(arr, [1, 3], [88, 99])
print(arr)
# [10 88 30 99 50]

# np.nonzero()------------
arr = np.array([0, 2, 0, 3, 8])
indicies = np.nonzero(arr)
print(indicies)
# (array([1, 3, 4]),)

# np.isin() check if element of one array exist in another array 
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([1, 3, 4, 6])
print(np.isin(a, b))
# [ True False  True  True False  True]

# np.extract()------------------------------
arr = np.arange(10)
condition = arr % 2 == 0
print(np.extract(condition, arr))
# [0 2 4 6 8]

# np.delete()-------------------------------
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.delete(arr, 1, axis= 1))
# [[1 3]
#  [4 6]
#  [7 9]]