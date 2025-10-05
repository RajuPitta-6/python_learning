import numpy as np

# ------ Creating Arrays ------------
# 1D Array
arr1 = np.array([1, 2, 4, 3, 5])
print(f"1D Array :\n{arr1}")

#  2D Array
arr2 = np.array([[1, 5, 4],[8, 6, 1]])
print(f"2D Array :\n{arr2}")

#  3D Array
arr3 = np.array([[[7, 6],[ 6, 1]],[[ 5, 4],[8, 1]]])
print(f"3D Array :\n{arr3}")

# output:
# 1D Array :
# [1 2 4 3 5]
# 2D Array :
# [[1 5 4]
#  [8 6 1]]
# 3D Array :
# [[[7 6]
#   [6 1]]

#  [[5 4]
#   [8 1]]]

# --------  checking types and shapes -------------
print("Type of arr1 :", type(arr1))
print("sahpe of arr2 :", arr2.shape)
print("Dimensions of arr3 :", arr3.ndim)
print("Data type of arr1 :", arr1.dtype)

# Type of arr1 : <class 'numpy.ndarray'>
# sahpe of arr2 : (2, 3)
# Dimensions of arr3 : 3
# Data type of arr1 : int64

# -------- converting list into numpy array -----------
py_list = [1, 2, 4, 7, 5]
np_arr = np.array(py_list)
print(f"Python list :{py_list}")
print(f"Numpy array :{np_arr}")

# Python list :[1, 2, 4, 7, 5]
# Numpy array :[1 2 4 7 5]