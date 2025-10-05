import sys
print("Arguments :", sys.argv)

# Exit program(sys.exit())----------------------------------

# name = input("Enter name :")
# if name == "":
#     print("Empty name, exiting program.")
#     sys.exit()
# print("Welcome", name)

# System version (sys.version)----------------------------------
print(sys.version)

# python path(sys.path)----------------------------------
print(sys.path)

# sys.stdin, sys.stdout, sys.deer ------------------------------------------


name = sys.stdin.readline()
print("Name :", name)

sys.stdout.write("Hello, thisi  is printed using sys.stdout\n")

sys.stderr.write("This is an error message!\n")

# sys.getsizeof()--------------------------------------------------
x = [1, 2, 3, 5]
print(sys.getsizeof(x))

# sys.modules------------------------------------------------------
print(sys.modules.keys())

# sys.platform----------------------------------------------------
print(sys.platform)

# sys.maxsize
print(sys.maxsize)