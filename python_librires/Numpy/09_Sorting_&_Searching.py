import numpy as  np
arr = np.array([52, 44, 89, 17, 25, 36])
print("Sorted array :",np.sort(arr))
# Sorted array : [17 25 36 44 52 89]

arr2 = np.array([[2, 4, 6],[88, 9, 4], [7, 5, 12]])

print(arr2)
print("Sorted array :\n",np.sort(arr2, axis=0))
print("Sorted array :\n",np.sort(arr2, axis=1))

# [[ 2  4  6]
#  [88  9  4]
#  [ 7  5 12]]
# Sorted array :
#  [[ 2  4  4]
#  [ 7  5  6]
#  [88  9 12]]
# Sorted array :
#  [[ 2  4  6]
#  [ 4  9 88]
#  [ 5  7 12]]

# np.argsort()--Get sorted index position
arr = np.array([40, 10, 30, 20])
idx = np.argsort(arr)
print("Indexes in sorted order :", idx)
print("Sorted using index :",arr[idx])
# Indexes in sorted order : [1 3 2 0]
# Sorted using index : [10 20 30 40]

# np.lexsort() -- Sort by multiple keys
names = np.array(["raju", "raz", 'vinay', 'ajay', 'bujji'])
marks = np.array([88, 99, 56, 72, 69]) 
idx = np.lexsort((marks, names)) # First by names then marks
print("Sorted by names then marks :")
print(names[idx], marks[idx])
# Sorted by names then marks :
# ['ajay' 'bujji' 'raju' 'raz' 'vinay'] [72 69 88 99 56]

arr = np.array([1, 2, 2, 3, 3, 3, 5, 4, 5, 4, 4])
print("Unique elements :", np.unique(arr))
# Unique elements : [1 2 3 4 5]

# np.searchsort() --Find insertion position
arr = np.array([10, 20, 30, 40, 50])
pos = np.searchsorted(arr, 23)
print("Insert 23 at index :", pos)
# Insert 35 at index : 2

# np.parition() -- partial sorting
arr = np.array([7, 2, 8, 6, 4, 5])
print("Elements :",np.partition(arr, 2))
print("Index :",np.argpartition(arr, 2))
# Elements : [2 4 5 6 7 8]
# Index : [1 4 5 3 0 2]

# np.argmax() & np.argmin() — Position of Max/Min Element
arr = np.array([10, 50, 20, 70, 30])
print("Index of max element:", np.argmax(arr))  # 3
print("Index of min element:", np.argmin(arr))  # 0
