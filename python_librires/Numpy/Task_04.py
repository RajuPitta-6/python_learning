'''Data Creation & Manipulation (Core Foundation)

Q1. Create random dataset X (100×5) and labels y (100×1).
👉 Practice: np.random.rand(), np.random.randint(), .reshape()

Q2. Standardize X → (subtract mean, divide by std).
👉 Concept: Feature scaling (Z-score normalization)

Q3. Normalize X to range 0–1 using Min–Max scaling.
👉 Concept: ML preprocessing normalization

Q4. Split dataset into train (70%) and test (30%) using array slicing.
👉 Concept: Model training/testing preparation'''

import numpy as np
import pandas as pd

n_samples = 100
n_features = 5

# Creating dataset
X = np.random.rand(n_samples, n_features)

# Creating labels
Y = np.random.randint(0, 2, size=(n_samples, 1))

Data_set = pd.DataFrame(X, columns=[f" feature_{i}" for i in range(1, n_features+1)])
Data_set['Label']  = Y.ravel()
print(Data_set.head())
#    feature_1   feature_2   feature_3   feature_4   feature_5  Label
# 0    0.624259    0.566879    0.424303    0.828844    0.474197      1
# 1    0.381248    0.176912    0.341905    0.202204    0.983213      1
# 2    0.880504    0.100604    0.120299    0.327038    0.185558      0
# 3    0.981849    0.182086    0.172512    0.026703    0.740076      1
# 4    0.921177    0.310860    0.149932    0.655176    0.606480      0

# Q2. Standardize X → (subtract mean, divide by std).
mean = np.mean(X, axis=0)
std = np.std(X, axis=0)
z_score = (X - mean) / std

print(z_score[:5])
# [[ 0.36080951  0.36542286 -0.10640956  1.23556662 -0.15140036]
#  [-0.49503063 -0.9263569  -0.37886334 -0.98160306  1.64397361]
#  [ 1.26325375 -1.17913108 -1.1116164  -0.53991883 -1.16947406]
#  [ 1.62017181 -0.90922068 -0.93896903 -1.60255718  0.78639383]
#  [ 1.40649625 -0.48265157 -1.01363286  0.62109469  0.31518176]]
# Q3. Normalize X to range 0–1 using Min–Max scaling.
x_max = X.max(axis= 0)
x_min = X.min(axis=0)

normal = (X - x_min) / (x_max - x_min)
print(normal[:5])
# [[0.74923362 0.42148387 0.29956099 0.84651453 0.14113482]
#  [0.32049969 0.61695888 0.99443668 0.19860176 0.40127417]
#  [0.07852397 0.64265524 0.87374011 0.36813512 0.79343167]
#  [0.42083671 0.96919111 0.7444396  0.7172549  0.22471014]
#  [0.82265345 0.11496568 0.07724166 0.44369774 0.67722171]]
# Q4. Split dataset into train (70%) and test (30%) using array slicing.

train_size = int(0.7 * len(X))

train_x = X[:train_size]
train_y = Y[:train_size]

test_x = X[train_size:]
test_y = Y[train_size:]

print("X_train shape :", train_x.shape)
print("y_train shape :", train_y.shape)
# X_train shape : (70, 5)
# y_train shape : (70, 1)

print("X_test shape", test_x.shape)
print("y_test shape", test_y.shape)
# X_test shape (30, 5)
# y_test shape (30, 1)