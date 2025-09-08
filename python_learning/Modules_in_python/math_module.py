import math

# Basic functions
print(math.sqrt(16))
print(math.pow(5, 5))
print(math.fabs(-10))

# output :
# 4.0
# 3125.0
# 10.0

# Rounding Functions
print(math.floor(4.9))
print(math.ceil(4.1))
print(math.trunc(4.7))

# output :
# 4
# 5
# 4

# Trigonometric Functions
print(math.sin(0))
print(math.cos(0))
print(math.tan(45))

# Output :
# 0.0
# 1.0
# 1.6197751905438615

# Logarithmic Functions
print(math.log(10))
print(math.log10(100))

# Output :
# 2.302585092994046
# 2.0

# Factorial & combinatorics
print(math.factorial(5))
print(math.comb(5, 2))
print(math.perm(5, 2))

# output :
# 120
# 10
# 20

# Constants
print(math.pi)
print(math.e)
print(math.inf)

# output :
# 3.141592653589793
# 2.718281828459045
# inf

# Example program
radius = 7
area = math.pi * math.pow(radius, 2)
print(f"Area of a circle with radius {radius} = {area:.3f}") # Area of a circle with radius 7 = 153.938