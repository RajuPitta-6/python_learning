# Task Covers: sum, mean, std, percentile, argmax, axis
import numpy as np

data = np.array([[10, 15, 20],
                 [25, 30, 35],
                 [40, 45, 50]])

# Column-wise mean and sum
mean = np.mean(data, axis = 0)
print(mean)

# Overall standard deviation
std = np.std(data)
print(std)

# Index of max value and its position
max_value = np.max(data)
index_position = np.argmax(data)
row, col = np.unravel_index(index_position, data.shape)
print(f"Max value :{max_value}\nIndex postion : Row : {row}, coloumn : {col}")

# 50th and 90th percentile of data
print("50th percentage of data :", np.percentile(data, 50))
print("90th percentage of data :", np.percentile(data, 90))
