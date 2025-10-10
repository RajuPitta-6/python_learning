# scalar broadcasting
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr + 10)
# [[11 12 13]
#  [14 15 16]]

# Compatible case
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([10, 20, 30])
print(A + B)

# [[11 22 33]
#  [14 25 36]]

# Column Broadcasting
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
B = np.array([[10],
              [20],
              [30]])  # shape (3,1)
print(A + B)
# [[11 12 13]
#  [24 25 26]
#  [37 38 39]]

# Multi-Dimensional Broadcasting
x = np.arange(4).reshape(4, 1)
y = np.arange(5)
print((x + y))
# [[0 1 2 3 4]
#  [1 2 3 4 5]
#  [2 3 4 5 6]
#  [3 4 5 6 7]]

# Function-based Broadcasting
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[10], [20]])

print(np.add(A, B))
print(np.multiply(A, B))
# [[11 12 13]
#  [24 25 26]]
# [[ 10  20  30]
#  [ 80 100 120]]

# Example 1
data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

mean = data.mean(axis=0)
std = data.std(axis=0)

normalized = (data - mean) / std
print(normalized)
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

# Example 2
data = np.random.randint(50, 100, size=(5, 3))
mean = np.mean(data, axis=0)
print(data)
print(mean)
centered = data - mean
print("Centered data:\n", centered)

# [[85 94 90]
#  [62 91 57]
#  [56 71 60]
#  [54 96 63]
#  [51 86 99]]
# [61.6 87.6 73.8]
# Centered data:
#  [[ 23.4   6.4  16.2]
#  [  0.4   3.4 -16.8]
#  [ -5.6 -16.6 -13.8]
#  [ -7.6   8.4 -10.8]
#  [-10.6  -1.6  25.2]]
