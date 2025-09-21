nums = list(map(int, input("Enter numbers into list separate by ','  :" ).split(',')))
# small = float('inf')
# big = float('-inf')
small = big = nums[0]

for i in nums:
    if i > big:
        big = i
    if i < small:
        small = i
    
print(f"Smallest number is:{small}, Biggest number is :{big}")

# Bulit in method
print(f"Smallest number is {min(nums)}, Greates number is {max(nums)}")