import os
# current working Directory
print("Current Directory:", os.getcwd())

# change Directory
# os.chdir("c:/users")
# print("After  changing Directory:",os.getcwd())

# List Files
print("Files in curreent dir :",os.listdir())

# Create Folder
os.mkdir("TestFolder")
print("Created folder:","TestFolder")

# Rename Folder
os.rename("TestFolder", "NewFolder")
print("Rename to:","NewFolder")

# Delet Folder
os.rmdir("NewFolder")
print("Deleted folder :", "NewFolder")

# File create and delete
with open("Sample.txt", 'w') as file:
    file.write("Hello os module!")

print("Sample.txt exists ?")
print(os.path.exists("Sample.txt"))

os.remove("Sample.txt")
print("Sample.txt deleted")

print("Sample.txt exists ?")
print(os.path.exists("Sample.txt"))


# Example Output:
# Files in curreent dir : ['x', 'y', 'y', 'sz', 'k']
# Created folder: TestFolder
# Rename to: NewFolder
# Deleted folder : NewFolder
# Sample.txt exists ?
# True
# Sample.txt deleted
# Sample.txt exists ?
# False