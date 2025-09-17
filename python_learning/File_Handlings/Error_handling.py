# Error handling
import csv
try:
    with open("Student.csv") as file:
        reader = csv.reader(file)
except FileNotFoundError:
    # File not found error handle
    print("Error : File not found! please check file name.")
except PermissionError:
    # File permission error handle
    print("Error : You dont have permission to access this file .")
except Exception as e:
    # Other error handle
    print(f"Unexpected error : {e}")
finally:
    print("Complete!")

# Example output:
# Error : File not found! please check file name.
# Complete!