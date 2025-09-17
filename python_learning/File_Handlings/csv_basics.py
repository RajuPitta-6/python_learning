import csv

Data = [["Name", "Branch", "college"],["Raju", "CSE", "RK"],["Swathi","Physics", "RK"],["JR", "AI", "RK"]]

with open("Students.csv", "w", encoding='UTF-8', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(Data)
    print("Student data added sucessfully!")

with open("Students.csv", "r", encoding='UTF-8') as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)

new_data = [["BUjji", "CSE", "RK"], ["unkown", "CHEM", "RK"]]

with open("Students.csv", "a+", encoding='UTF-8', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_data)
    print("Student new_data added sucessfully!")

with open("Students.csv", "r", encoding='UTF-8') as file:
    print("-----------------Student data After added new student data --------------------")
    reader = csv.reader(file)
    for i in reader:
        print(i)

# Example OUPUT:
'''Student data added sucessfully!
['Name', 'Branch', 'college']
['Raju', 'CSE', 'RK']
['Swathi', 'Physics', 'RK']
['JR', 'AI', 'RK']
Student new_data added sucessfully!
-----------------Student data After added new student data --------------------
['Name', 'Branch', 'college']
['Raju', 'CSE', 'RK']
['Swathi', 'Physics', 'RK']
['JR', 'AI', 'RK']
['BUjji', 'CSE', 'RK']
['unkown', 'CHEM', 'RK']
'''
