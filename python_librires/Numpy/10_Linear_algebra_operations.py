import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# 1. Using @ operator (recommended)
print(A @ B)

# 2. Using np.dot()
print(np.dot(A, B))

# 3. Using np.matmul()
print(np.matmul(A, B))

'''
[[19 22]
 [43 50]]
[[19 22]
 [43 50]]
[[19 22]
 [43 50]]
'''
A = np.array([[1, 2, 3],
              [4, 5, 6]])

print(A.T)
# [[1 4]
#  [2 5]
#  [3 6]]

from numpy.linalg import det
from numpy.linalg import inv
from numpy.linalg import matrix_rank
A = np.array([[2, 3],
              [1, 4]])
print(det(A))
print(np.trace(A))
print(inv(A))
print(matrix_rank(A))

# 5.000000000000001

# 6

# [[ 0.8 -0.6]
#  [-0.2  0.4]]

# 2


vals, vecs = np.linalg.eig(A)
print("Eigenvalues:", vals)
print("Eigenvectors:\n", vecs)
# Eigenvalues: [1. 5.]
# Eigenvectors:
#  [[-0.9486833  -0.70710678]
#  [ 0.31622777 -0.70710678]]

# Solving Linear Equations ---------------------
A = np.array([[3, 1],
              [1, 2]])
b = np.array([9, 8])

x = np.linalg.solve(A, b)
print("Solution x:", x)
# Solution x: [2. 3.]

# Norm of a Vector (Magnitude)---------------------------
from numpy.linalg import norm

v = np.array([3, 4])
print("Norm:", norm(v))  # Output: 5.0
# Norm: 5.0

# Singular Value Decomposition (SVD)
A = np.array([[1, 2], [3, 4], [5, 6]])
U, S, Vt = np.linalg.svd(A)
print("U:\n", U)
print("S:\n", S)
print("Vt:\n", Vt)

# U:
#  [[-0.2298477   0.88346102  0.40824829]
#  [-0.52474482  0.24078249 -0.81649658]
#  [-0.81964194 -0.40189603  0.40824829]]
# S:
#  [9.52551809 0.51430058]
# Vt:
#  [[-0.61962948 -0.78489445]
#  [-0.78489445  0.61962948]]

# Pseudo-inverse (Moore–Penrose Inverse)----------------
print(np.linalg.pinv(A))
# [[-1.33333333 -0.33333333  0.66666667]
#  [ 1.08333333  0.33333333 -0.41666667]]

# Condition Number — measures matrix stability-----------------
print(np.linalg.cond(A))
# 18.521305341258135

# Matrix Power
A = np.array([[1, 2], [3, 4]])
print(np.linalg.matrix_power(A, 3))
# [[ 37  54]
#  [ 81 118]]

# QR Decomposition--------------------

Q, R = np.linalg.qr(A)
print("Q = ",Q)
print("R = ",R)
# Q =  [[-0.31622777 -0.9486833 ]
#  [-0.9486833   0.31622777]]
# R =  [[-3.16227766 -4.42718872]
#  [ 0.         -0.63245553]]