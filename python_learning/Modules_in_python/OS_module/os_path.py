import os

path = "sample.txt"

# Absolute Path
print("Absolute Path:", os.path.abspath(path))

# Check Path
print("Exists?", os.path.exists("student.json"))
print("Is File?", os.path.isfile(path))
print("Is Dir?", os.path.isdir(path))

# Join Paths
print("Joined Path:", os.path.join("folder", "file.txt"))

# Base & Dir Name
print("Basename:", os.path.basename("C:/Users/Admin/test.txt"))
print("Dirname:", os.path.dirname("C:/Users/Admin/test.txt"))


# Example output:
'''
Absolute Path: C:\Users\x\g\sample.txt
Exists? True
Is File? False
Is Dir? False
Joined Path: folder\file.txt
Basename: test.txt
Dirname: C:/Users/Admin'''