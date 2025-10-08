import numpy as np


# -----------Concatenation ---------------------
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
# Axis = 0 --> row-wisw
result1 = np.concatenate((a, b), axis = 0)
print("Row wise concatination :\n", result1)
# Row wise concatination :
#  [[1 2]
#  [3 4]
#  [5 6]]

# Axis = 1 --> coloumn-wisw
c = np.array([[7], [8]])
result2 = np.concatenate((a, c), axis = 1)
print("Coloumn wise concatination :\n", result2)
# Coloumn wise concatination :
#  [[1 2 7]
#  [3 4 8]]

# -------------------Stack functions --------------------
# np.vstack() vertical stack(rows)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
v = np.vstack((a, b))
print("Vertical stack:\n", v)

# np.hstack() horizontal stack(coloumns)
h = np.hstack((a, b))
print("Horizontal stack:\n", h)

# np.dstack() depth stack(3 rd)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
d = np.dstack((a, b))
print("Depth stack:\n", d)

# Vertical stack:
#  [[1 2 3]
#  [4 5 6]]
# Horizontal stack:
#  [1 2 3 4 5 6]
# Depth stack:
#  [[[1 5]
#   [2 6]]

#  [[3 7]
#   [4 8]]]

# -----------split arrays -------------

arr = np.array([10, 20, 30, 40, 50, 60])
split_arr = np.split(arr, 3)
print("Split array:", split_arr)

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])
res = np.hsplit(arr, 2)
print("HSplit:", res)

res = np.vsplit(arr, 2)
print("VSplit:", res)

# Split array: [array([10, 20]), array([30, 40]), array([50, 60])]
# HSplit: [array([[1, 2],
#        [5, 6]]), array([[3, 4],
#        [7, 8]])]
# VSplit: [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]


# example for combining and spliting together
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6],[7, 8]])

combined = np.vstack((x, y))
print("Combined:\n", combined)

part1, part2 = np.vsplit(combined, 2)
print("Split 1:\n", part1)
print("Split 2:\n", part2)

# Combined:
#  [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
# Split 1:
#  [[1 2]
#  [3 4]]
# Split 2:
#  [[5 6]
#  [7 8]]

# --------- operations ---------------
arr = np.array([1, 2, 3])
new_arr = np.append(arr, [4, 5])
print("After append:", new_arr)

arr = np.array([10, 20, 30, 40])
new_arr = np.insert(arr, 2, [99, 100])
print("After insert:", new_arr)

arr = np.array([10, 20, 30, 40, 50])
new_arr = np.delete(arr, [1, 3])
print("After delete:", new_arr)

# After append: [1 2 3 4 5]
# After insert: [ 10  20  99 100  30  40]
# After delete: [10 30 50]
