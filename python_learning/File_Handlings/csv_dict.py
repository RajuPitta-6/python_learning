import csv
# File Name
file_name = "students_dict.csv"
Data = [{"Name":"Raju","Branch":"CSE","college":"RK"},{"Name":"Raju","Branch":"MECH","college":"MVGR"},{"Name":"Ramesh","Branch":"CSE","college":"Aditya"},{"Name":"Raghu","Branch":"ECE","college":"Raghu"}]
fieldname = ["Name","Branch","college"]
try:
    with open(file_name, 'w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldname)
        writer.writeheader()
        writer.writerows(Data)
        print("Data written sucessfully using Dictwriter")
except PermissionError:
    print("permissiom denied unable to write file!")
except Exception as e:
    print(f"Unexpected error :{e}")

try:
    with open(file_name, "r", encoding="UTF-8") as file:
        reader = csv.DictReader(file)
        print("Reading data using dict reader....")
        for row in reader:
            print(row)

except PermissionError:
    print("Ypu dont have permission to access this file!")
except FileNotFoundError:
    print("File not found, check file name!")
except Exception as e:
    print(f"Unexpected error :{e}")
finally:
    print("File operations completed....")