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
