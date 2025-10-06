import numpy as np 

# ----- Creating array filled with zeroes, ones, constant----------

# zero array
zero_arr = np.zeros((3, 4))
print("Zero array :\n",zero_arr)
# Zero array :
#  [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# ones array
ones_arr = np.ones((4, 5))
print("Ones array :\n", ones_arr)
# Ones array :
#  [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

# constant array
constant_arr = np.full((3, 3), 5)
print("Constat array :\n", constant_arr)
# Constat array :
#  [[5 5 5]
#  [5 5 5]
#  [5 5 5]]


# ------ create sequence array ------------

# using arrange(start, stop, step)
arr1  = np.arange(0, 10, 2)
print("Using arange :\n", arr1)
# Using arange :
#  [0 2 4 6 8]

# using linspace(start, stop, num)
arr2 = np.linspace(0, 1, 5)
print("Using linspace :\n", arr2)
# Using linspace :
#  [0.   0.25 0.5  0.75 1.  ]

# ---------identity & digonal  matrix-------------
I = np.eye(5)
print("Identity matrix :\n", I)
# Identity matrix :
#  [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

D = np.diag([1, 2, 3, 4, 5])
print("Digonal matrix :\n", D)
# Digonal matrix :
#  [[1 0 0 0 0]
#  [0 2 0 0 0]
#  [0 0 3 0 0]
#  [0 0 0 4 0]
#  [0 0 0 0 5]]

# ------ Random number array ------------------

# Random float values between 0 and 1
rand_arr = np.random.rand(3, 3)
print("Random float array:\n", rand_arr)
# Random float array:
#  [[0.61548037 0.25524018 0.71570042]
#  [0.27587972 0.87829494 0.64134184]
#  [0.58073964 0.38056034 0.71353071]]

# Random integer
rand_int_arr = np.random.randint(10, 50, size=(3, 4))
print("Random integer array :\n", rand_int_arr)
# Random integer array :
#  [[35 15 20 14]
#  [47 42 45 19]
#  [43 10 36 26]]

# -------- Empty array ----------------
empty_arr = np.empty((2, 3))
print("Empty array :\n", empty_arr)

# ------------ Type conversion --------------
arr = np.array([1.55, 2.3, 9.1, 7.8, 1.2])
int_arr = arr.astype(int)
print("Converted array :\n", int_arr)
# Converted array :
#  [1 2 9 7 1]

# ------------ Reshape array --------------
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(f"Before reshped :\n{arr}\nAfter reshape :\n{reshaped}")
# Before reshped :
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
# After reshape :
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# -----------Multiplying array---------------
arr = np.ones((3, 4)) * 9
print("Multiplied array :\n", arr)
# Multiplied array :
#  [[9. 9. 9. 9.]
#  [9. 9. 9. 9.]
#  [9. 9. 9. 9.]]

# --------- Repeat array ---------------

# repeat scalr 
arr = np.repeat(5, 6)
print("Using sclar repeat :\n", arr)
# Using sclar repeat :
#  [5 5 5 5 5 5]

# repeating each element of an array
arr = np.array([1, 2, 3])
rep = np.repeat(arr, 3)
print("Repeated array :\n", rep)
# Repeated array :
#  [1 1 1 2 2 2 3 3 3]

#  coustom repeat 
arr = np.array([10, 20, 30])
rep = np.repeat(arr, [1, 3, 2])
print("Coustom repeated :\n", rep)
# Coustom repeated :
#  [10 20 20 20 30 30]