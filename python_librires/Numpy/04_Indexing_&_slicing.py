import numpy as np

# ---------------- 1D Accessing elements(indexing and slicing)---------------------
# indexing
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])
print(arr[3])
print(arr[2])

# 10
# 40
# 30

# slicing (array[start:stop:step])
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4])
print(arr[0:-1:2])
print(arr[::-1])

# [20 30 40]
# [10 30 50]
# [60 50 40 30 20 10]

# ---------------- 2D Accessing elements(indexing and slicing)---------------------
# indexing
arr2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(arr2[0, 0])
print(arr2[-1, -1])
print(arr2[2,1])

# 10
# 90
# 80


# # slicing (array[start:stop:step])

arr2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]])
print(arr2[1:4, 1:2])
print(arr2[1:3, 1:3])
print(arr2[::-1, ::-1])

# [[ 50]
#  [ 80]
#  [110]]

# [[50 60]
#  [80 90]]

# [[120 110 100]
#  [ 90  80  70]
#  [ 60  50  40]
#  [ 30  20  10]]


# ----------- Fancy indexing ------------------------------

# 1D Array
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[[0, 2, 4]])
print(arr[[1, 3, 5]])

# [10 30 50]
# [20 40 60]

# 2D Array
arr2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]])
print(arr2[[0,2],[1, 2]])
print(arr2[[1,2],[2, 1]])

# [20 90]
# [60 80]

# ----------Boolean indexing (Conditional filtering)---------------
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[arr > 30])
print(arr[arr % 30 == 0])

# [40 50 60]
# [30 60]

print(arr[(arr % 10 == 0) & (arr > 30)])
print(arr[(arr > 20) & (arr < 60)])

# [40 50 60]
# [30 40 50]

# ---------Indexing with slice and condtion------------

arr = np.arange(1, 11)
print(arr[:8][arr[:8] % 2 == 0])
# [2 4 6 8]

# ---------- Modifying elements using indexing -------------------
arr = np.array([10, 20, 30, 40, 50, 60])
arr[2] = 0
print(arr)
# [10 20  0 40 50 60]
arr[arr < 20] = 0
print(arr)
# [ 0 20  0 40 50 60]