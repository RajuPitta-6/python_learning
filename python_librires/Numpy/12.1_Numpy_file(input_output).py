import numpy as np

# Save and load binary file
arr = np.array([1, 2, 3, 4, 5])

# save to binary file
np.save('my_array.npy', arr)

# load it back
loaded_arr = np.load('my_array.npy')
print(loaded_arr)
# [1 2 3 4 5]

# ------------------------------------------------
# save and multiple arrays
a = np.arange(5)
b = np.linspace(0, 1, 5)

# Save multiple arrays 
np.savez('multiple_array.npz', first = a, second = b)

# load it back
load_arr = np.load('multiple_array.npz')
print(load_arr['first'])
print(load_arr['second'])
# [0 1 2 3 4]
# [0.   0.25 0.5  0.75 1.  ]

# ----------------------------------------------------
# Save and load to text files 
arr = np.array([[1.5, 2.3, 3.1],[4.5, 5.2, 6.3]])
np.savetxt("array.csv", arr, delimiter=",", fmt = "%2f", comments = '')
loaded_csv = np.loadtxt('array.csv', delimiter=',')
print(loaded_csv)
# [[1.5 2.3 3.1]
#  [4.5 5.2 6.3]]

# ---- emory-mapped files(np.memmap)---------------------
# create memory mapped array
data = np.memmap('large_data.dat', dtype = 'float32', mode = 'w+', shape=(1000, 1000))
data[:] = np.random.rand(1000, 1000)
del data
# load agin
mmap = np.memmap('large_data.dat', dtype='float32', mode = 'r', shape=(1000, 1000))
print(mmap[1 : 5])
# [[0.84169847 0.9742685  0.39136326 ... 0.7501942  0.27351657 0.48668557]
#  [0.7847863  0.7158634  0.15602808 ... 0.7324472  0.75124866 0.5190378 ]
#  [0.43398502 0.83367074 0.67041206 ... 0.68172896 0.4052057  0.07696697]
#  [0.34821764 0.82302874 0.8597448  ... 0.14042692 0.68390447 0.7633798 ]]
print(np.shape(mmap))
# (1000, 1000)

# ----- Raw binary file ---------------------------
arr = np.arange(10, dtype=np.int32)

# Save raw binary data
arr.tofile('raw_data.bin')

# read it back(need dtype and shape)
loaded = np.fromfile('raw_data.bin', dtype=np.int32)
print(loaded)
# [0 1 2 3 4 5 6 7 8 9]