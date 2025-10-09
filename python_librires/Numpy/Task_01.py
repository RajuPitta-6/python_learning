# Task 1 -- Array creation and basic info
import numpy as np
arr = np.random.randint(10, 25, size=(4, 4))
print(arr)
print("Shape :",arr.shape)
print("Array size :", arr.size)
print("Array dtype :", arr.dtype)
print("Dimensions :", arr.ndim)

# [[16 19 12 18]
#  [10 23 20 20]
#  [12 16 11 21]
#  [16 16 17 13]]
# Shape : (4, 4)
# Array size : 16
# Array dtype : int32
# Dimensions : 2

# first row last coloumn
print("First row :",arr[0:1, 0:4]) # optinal = arr[0]

print("last coloumn :\n",arr[0:4, 0:1]) # optinoal = arr[:, -1:]

# First row : [[16 19 12 18]]
# last coloumn :
#  [[16]
#  [10]
#  [12]
#  [16]]

# Flatten the array into 1D
print("Faltten Arrar :", arr.flatten())
# Faltten Arrar : [16 19 12 18 10 23 20 20 12 16 11 21 16 16 17 13]