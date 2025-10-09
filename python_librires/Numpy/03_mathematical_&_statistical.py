import numpy as np 

# -------------Basic arthmetic operations --------------------
a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])

# Addition
print("Addition :\n",a + b)

# Subtraction
print("Subtraction :\n", a - b)

# Multipication
print("Multiplication :\n", a * b)

# Division
print("Division :\n",a / b)

# power
print("Power :\n", b ** 2)

# Trignometry
print("Sine :",np.sin(a))
print("Cosine :",np.cos(a))
print("Tan :",np.tan(b))

# Output
'''
Addition :
 [11 22 33 44 55]
Subtraction :
 [ 9 18 27 36 45]
Multiplication :
 [ 10  40  90 160 250]
Division :
 [10. 10. 10. 10. 10.]
Power :
 [ 1  4  9 16 25]
Sine : [-0.54402111  0.91294525 -0.98803162  0.74511316 -0.26237485]
Cosine : [-0.83907153  0.40808206  0.15425145 -0.66693806  0.96496603]
Tan : [ 1.55740772 -2.18503986 -0.14254654  1.15782128 -3.38051501]
'''

# -------Scalar operation (with single number)----------------

arr = np.array([5, 10, 15, 20])
print(arr + 5)
print(arr - 5)
print(arr * 5)
print(arr / 5)

'''
[10 15 20 25]
[ 0  5 10 15]
[ 25  50  75 100]
[1. 2. 3. 4.]'''

# ---------- Arithmetic with 2D array --------------------

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[4, 5, 6], [1, 2, 3]])

print("Addition :\n",np.add(A, B))
print("Subtraction :\n",np.subtract(A, B))
print("Multiplication :\n",np.multiply(A, B))
print("Division :\n",np.divide(A, B))
print("power :\n",np.power(A, B))
print("modulus :\n",np.mod(A, B))

'''
Addition :
 [[5 7 9]
 [5 7 9]]
Subtraction :
 [[-3 -3 -3]
 [ 3  3  3]]
Multiplication :
 [[ 4 10 18]
 [ 4 10 18]]
Division :
 [[0.25 0.4  0.5 ]
 [4.   2.5  2.  ]]
power :
 [[  1  32 729]
 [  4  25 216]]
modulus :
 [[1 2 3]
 [0 1 0]]'''

# ----------------In-place operation-----------------
a1 = np.array([5, 4, 3, 2, 1])
a1 += 5
print(a1) # [10  9  8  7  6]

# --------- Aggregate Arithmetic -----------------

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("sum : ",np.sum(arr))  # sum :  21
print("Coloumn-wise-sum : ", np.sum(arr, axis = 0))  # Coloumn-wise-sum :  [5 7 9]
print("Row-wise-sum : ", np.sum(arr, axis = 1))  # Row-wise-sum :  [ 6 15]
print("Product : ", np.prod(arr))  # Product :  720
print("Mean : ", np.mean(arr))  # Mean :  3.5
print("Standard deviation : ", np.std(arr))  # Standard deviation :  1.707825127659933
print("Variance : ", np.var(arr))  # Variance :  2.9166666666666665
print("Min : ", np.min(arr))  # Min :  1
print("Max : ", np.max(arr))  # Max :  6

# ----------- Cumulative operations --------------
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("cumulative sum :",np.cumsum(arr)) # cumulative sum : [ 1  3  6 10 15 21]
print("cumulative product :",np.cumprod(arr)) # cumulative product : [  1   2   6  24 120 720]

# ----------- Round, Floor, Ceil operations -----------------
arr = np.array([1.23, 4.56, 7.89])
print("Round :", np.round(arr)) # Round : [1. 5. 8.]
print("Floor :", np.floor(arr)) # Floor : [1. 4. 7.]
print("Ceil :", np.ceil(arr)) # Ceil : [2. 5. 8.]


# -----------Axis parameters-------------------------
arr = np.array([[10, 20, 40, 50],[1, 2, 8, 3]])
print("Row_wise sum", np.sum(arr, axis = 0))
print("Coloumn_wise sum", np.sum(arr, axis = 1))

# Row_wise sum [11 22 48 53]
# Coloumn_wise sum [120  14]

# --------------- Index functions ------------------
arr = np.array([10, 30, 20, 40, 30])

print("Index of min:", np.argmin(arr))
print("Index of max:", np.argmax(arr))
print("Sorted indices:", np.argsort(arr))

# Index of min: 0
# Index of max: 3
# Sorted indices: [0 2 1 4 3]

# ---------------- Difference & unique operations---------------
arr = np.array([2, 4, 6, 8])
print("Difference between elements:", np.diff(arr))

arr2 = np.array([1, 2, 2, 3, 4, 4, 5])
print("Unique elements:", np.unique(arr2))

# Difference between elements: [2 2 2]
# Unique elements: [1 2 3 4 5]

# ------------ Other topics --------------------

# np.clip()  Limit values with in a range
arr = np.array([1, 5, 9, 15, 25])
clipped = np.clip(arr, 5, 20)
print(clipped) # [ 5  5  9 15 20]

# np.ptp() ------------> range(peak-to-peak)
arr = np.array([10, 20, 15, 2, 25])
print("Range:", np.ptp(arr)) # Range: 23

# np.percentile() & np.quantile()
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("25th percentile:", np.percentile(arr, 25))
print("Median (50th):", np.percentile(arr, 50))
print("75th percentile:", np.percentile(arr, 75))

# 25th percentile: 3.0
# Median (50th): 5.0
# 75th percentile: 7.0

# np.all() & np.any() — Check logical conditions
arr = np.array([1, 2, 3, 0])
print("All non-zero:", np.all(arr))
print("Any non-zero:", np.any(arr))

# All non-zero: False
# Any non-zero: True

# np.count_nonzero() — Count non-zero elements
arr = np.array([[1, 0, 3], [0, 0, 5]])
print("Non-zero count:", np.count_nonzero(arr))

# Any non-zero: True
# Non-zero count: 3