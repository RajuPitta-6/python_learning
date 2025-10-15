import numpy as np

# Random integers between [low, high) --------------
arr = np.random.randint(10, 50, size=(3, 4))
print("Intiger :\n",arr)
# Intiger :
#  [[45 48 11 27]
#  [46 47 21 37]
#  [39 24 33 32]]

# Random floats between 0 and 1----------------
arr2 = np.random.random((2, 4))
print("Float :\n",arr2)
# Float :
#  [[0.18243459 0.15565044 0.31227053 0.35168219]
#  [0.38589572 0.19219801 0.61854715 0.0973903 ]]

# Random Floats-----------
arr = np.random.rand(3, 3)
print(arr)
# [[0.19251798 0.55560195 0.94928798]
#  [0.08918479 0.11528024 0.36264453]
#  [0.32062844 0.90002988 0.64628966]]

# Random Normal Distribution------------
arr = np.random.randn(3, 3)
print(arr)
# [[-0.36280129 -0.82445752 -0.39212934]
#  [ 0.83798042 -0.82342017 -0.27842086]
#  [ 1.26877685 -0.96705833 -0.82470007]]

# For custom mean and std:---------------------
mu, sigma = 10, 2
data = np.random.normal(mu, sigma, (3, 3))
print(data)
# [[ 8.77961546 10.88770568  9.27312516]
#  [ 9.13203723 10.70451389 13.54354582]
#  [ 8.21059127  9.57394652 14.25647209]]

# Uniform Distribution---------------------
arr = np.random.uniform(0, 1, (2, 5))
print(arr)
# [[0.60827904 0.17241906 0.55227845 0.1672444  0.75197812]
#  [0.67926398 0.71774784 0.84734016 0.98194765 0.90352235]]

# Random Choice (Sampling from Array)-----------------
arr = np.array([10, 20, 30, 40, 50])
sample = np.random.choice(arr, size=3, replace=False)
print(sample)
# [20 50 10]

# Probability-Based Sampling------------------
arr = ['A', 'B', 'C']
prob = [0.1, 0.3, 0.6]
sample = np.random.choice(arr, size=10, p=prob)
print(sample)
# ['B' 'C' 'A' 'B' 'B' 'C' 'C' 'A' 'A' 'C']

# Shuffle and Permutation-----------------
arr = np.arange(10)
np.random.shuffle(arr)
print("Shuffled:", arr)

# Shuffled: [0 1 9 3 4 5 6 7 2 8]
arr = np.arange(5)
print("Permutation:", np.random.permutation(arr))
# Permutation: [4 0 3 1 2]

# Seed for Reproducibility----------------
np.random.seed(42)
print(np.random.randint(0, 10, 5))
# [6 3 7 4 6]

# Binomial Distribution-----------------
arr = np.random.binomial(n=10, p=0.5, size=5)
print(arr)
# [5 3 5 4 3]

# Poisson Distribution-----------------(np.random.poisson(lam, size))
arr = np.random.poisson(3,10)
print(arr)
# [1 2 3 0 2 2 6 0 3 2]