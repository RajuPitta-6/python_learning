import numpy as np

# np.savez_compressed same as np.savez() but with compression (ZIP) to reduce file size
a = np.arange(1000)
b = np.linspace(0, 10, 1000)
np.savez_compressed('compressed_data.npz', arr1 = a, arr2 = b)
data = np.load('compressed_data.npz')
print(data.files)
# ['arr1', 'arr2']

# # np.recfromcsv() read csv into structured array
# data = np.recfromcsv('array.csv', encoding = 'utf-8')
# print(data.dtype)
# print(data[0])

# saving with np.savez()+metadata

train = np.arange(6).reshape(2, 3)
test = np.arange(6, 12).reshape(2, 3)
np.savez('dataset.npz', train=train, test=test, desc = "train/test split")
data = np.load('dataset.npz')
print(data)